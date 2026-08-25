from __future__ import annotations

import csv
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学/40 作品")
OUT = Path("个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis_completeness")
MARKER = OUT / "RUN_OPENLIBRARY_YEAR_CANDIDATES_V1"
BOUNDARIES = {500, 1500, 1800, 1890, 1945, 1980}
UA = "worldForMe-bibliography-audit/1.0 (GitHub repository audit)"


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    return m.group(1) if m else ""


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", fm)
    if not m:
        return ""
    v = m.group(1).strip()
    if v.lower() in {"null", "none", "~"}:
        return ""
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v


def list_field(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:\s*\[\s*\]\s*$", line): return []
        inline = re.match(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", line)
        if inline:
            raw = inline.group(1).strip()
            return [] if not raw else [x.strip().strip("\"'") for x in raw.split(",")]
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            out=[]
            for nxt in lines[i+1:]:
                m=re.match(r"^\s*-\s*(.*?)\s*$", nxt)
                if m:
                    out.append(m.group(1).strip().strip("\"'")); continue
                if re.match(r"^[A-Za-z0-9_\u4e00-\u9fff].*?:", nxt): break
                if nxt.strip() and not nxt.startswith((" ","\t")): break
            return out
    return []


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").casefold()
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return "".join(ch for ch in s if ch.isalnum())


def sim(a: str, b: str) -> float:
    na, nb = norm(a), norm(b)
    if not na or not nb: return 0.0
    if na == nb: return 1.0
    return SequenceMatcher(None, na, nb).ratio()


def t_for_year(y: int) -> str:
    if y < 500: return "T0"
    if y < 1500: return "T1"
    if y < 1800: return "T2"
    if y < 1890: return "T3"
    if y < 1945: return "T4"
    if y < 1980: return "T5"
    return "T6"


def is_cjk(s: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in (s or ""))


def query_one(item: dict) -> dict:
    qtitle = item["title_original"] or item["title"]
    author = item["author_original"] or item["author"]
    if not qtitle or not author:
        return {**item, "status":"NO_QUERY_KEYS", "candidate_year":"", "suggested_t":"", "confidence":"", "ol_title":"", "ol_authors":"", "ol_key":"", "title_similarity":"", "author_similarity":"", "reason":"missing usable title/author"}
    # Chinese-only title is unlikely to match OL reliably; still query only when no original title is available.
    params = urllib.parse.urlencode({"title": qtitle, "author": author, "fields":"title,author_name,first_publish_year,key", "limit":3})
    url = "https://openlibrary.org/search.json?" + params
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
    except Exception as e:
        return {**item, "status":"LOOKUP_ERROR", "candidate_year":"", "suggested_t":"", "confidence":"", "ol_title":"", "ol_authors":"", "ol_key":"", "title_similarity":"", "author_similarity":"", "reason":type(e).__name__}
    docs = data.get("docs") or []
    best = None
    best_score = -1.0
    for d in docs:
        year = d.get("first_publish_year")
        if not isinstance(year, int):
            continue
        ts = max(sim(qtitle, d.get("title", "")), sim(item["title"], d.get("title", "")), sim(item["title_original"], d.get("title", "")))
        authors = d.get("author_name") or []
        aus = max([sim(author, a) for a in authors] + [0.0])
        score = 0.65 * ts + 0.35 * aus
        if score > best_score:
            best_score = score; best = (d, year, ts, aus)
    if not best:
        return {**item, "status":"NO_MATCH", "candidate_year":"", "suggested_t":"", "confidence":"", "ol_title":"", "ol_authors":"", "ol_key":"", "title_similarity":"", "author_similarity":"", "reason":"no result with first_publish_year"}
    d, year, ts, aus = best
    if ts >= 0.96 and aus >= 0.88:
        conf = "HIGH"
    elif ts >= 0.88 and aus >= 0.75:
        conf = "MEDIUM"
    else:
        conf = "LOW"
    status = "CANDIDATE_BOUNDARY" if year in BOUNDARIES else "CANDIDATE"
    return {**item, "status":status, "candidate_year":str(year), "suggested_t":t_for_year(year), "confidence":conf, "ol_title":d.get("title", ""), "ol_authors":";".join(d.get("author_name") or []), "ol_key":d.get("key", ""), "title_similarity":f"{ts:.3f}", "author_similarity":f"{aus:.3f}", "reason":"Open Library first_publish_year candidate"}


def main() -> None:
    if not MARKER.exists():
        raise SystemExit("Open Library candidate authorization marker missing")
    OUT.mkdir(parents=True, exist_ok=True)
    items=[]
    for p in sorted(ROOT.glob("*.md"), key=lambda x:x.name.casefold()):
        text=p.read_text(encoding="utf-8-sig"); fm=frontmatter(text)
        if not fm or scalar(fm,"type")!="work": continue
        if list_field(fm,"axis_t"): continue
        if re.search(r"-?\d{1,4}", scalar(fm,"year")): continue
        items.append({
            "file":p.name,"id":scalar(fm,"id"),"title":scalar(fm,"title") or p.stem,
            "title_original":scalar(fm,"title_original"),"author":scalar(fm,"author"),
            "author_original":scalar(fm,"author_original"),"canon_id":scalar(fm,"canon_id"),
        })

    rows=[]
    # Conservative concurrency to avoid overloading the public service.
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs={ex.submit(query_one,it):it for it in items}
        for i,f in enumerate(as_completed(futs),1):
            rows.append(f.result())
            if i % 100 == 0: print(f"resolved {i}/{len(items)}")
            time.sleep(0.02)
    rows.sort(key=lambda r:r["file"].casefold())
    fields=list(rows[0].keys()) if rows else []
    with (OUT/"openlibrary_candidates_v1.csv").open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

    high=[r for r in rows if r.get("confidence")=="HIGH" and r.get("status")=="CANDIDATE"]
    medium=[r for r in rows if r.get("confidence")=="MEDIUM" and r.get("status")=="CANDIDATE"]
    low=[r for r in rows if r.get("confidence")=="LOW" and r.get("status")=="CANDIDATE"]
    boundary=[r for r in rows if r.get("status")=="CANDIDATE_BOUNDARY"]
    no_match=[r for r in rows if r.get("status") in {"NO_MATCH","NO_QUERY_KEYS","LOOKUP_ERROR"}]
    for name,subset in [("openlibrary_high_confidence_v1.csv",high),("openlibrary_review_v1.csv",medium+low+boundary),("openlibrary_unresolved_v1.csv",no_match)]:
        with (OUT/name).open("w",encoding="utf-8-sig",newline="") as f:
            w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(subset)

    md=[
        "# Open Library Missing-T Year Candidate Audit V1","",
        f"- Works queried: **{len(items)}**",
        f"- HIGH confidence non-boundary candidates: **{len(high)}**",
        f"- MEDIUM candidates: **{len(medium)}**",
        f"- LOW candidates: **{len(low)}**",
        f"- Boundary-year candidates: **{len(boundary)}**",
        f"- Unresolved / lookup error: **{len(no_match)}**","",
        "This stage is read-only. `first_publish_year` is treated as an external candidate, not canonical truth.","",
        "## Policy","",
        "- HIGH requires title similarity >= 0.96 and author similarity >= 0.88.",
        "- Boundary years are never eligible for blind application.",
        "- Anthologies, oral traditions, collected editions, and historically layered texts still require semantic review even if a HIGH result exists.",
        "- MEDIUM/LOW results remain review-only.","",
        "`OPENLIBRARY_MISSING_T_YEAR_CANDIDATES_V1 = AUDITED_READ_ONLY`",""
    ]
    (OUT/"OPENLIBRARY_CANDIDATES_V1.md").write_text("\n".join(md),encoding="utf-8",newline="\n")
    MARKER.unlink()
    print(f"HIGH={len(high)} MEDIUM={len(medium)} LOW={len(low)} BOUNDARY={len(boundary)} UNRESOLVED={len(no_match)}")

if __name__=="__main__": main()
