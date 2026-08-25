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

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学")
AUDIT = ROOT / "_audit/t_axis_completeness"
TRIAGE = AUDIT / "missing_t_triage_v1.csv"
OL = AUDIT / "openlibrary_priority_v2.csv"
OUT = AUDIT / "p2_wikidata_v1.csv"
SAFE = AUDIT / "p2_wikidata_safe_v1.csv"
REVIEW = AUDIT / "p2_wikidata_review_v1.csv"
REPORT = AUDIT / "P2_WIKIDATA_V1.md"
BOUNDARIES = {500, 1500, 1800, 1890, 1945, 1980}
UA = "worldForMe-literature-metadata-audit/1.0 (GitHub repository cxjchelsea/worldForMe)"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.casefold().replace("／", "/")
    s = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def sim(a: str, b: str) -> float:
    a, b = norm(a), norm(b)
    if not a or not b: return 0.0
    if a == b: return 1.0
    return SequenceMatcher(None, a, b).ratio()


def t_for_year(y: int | None) -> str:
    if y is None: return ""
    if y < 500: return "T0"
    if y < 1500: return "T1"
    if y < 1800: return "T2"
    if y < 1890: return "T3"
    if y < 1945: return "T4"
    if y < 1980: return "T5"
    return "T6"


def parse_int(s: str) -> int | None:
    m = re.search(r"-?\d{1,4}", s or "")
    return int(m.group(0)) if m else None


def api(params: dict[str, str]) -> dict:
    url = "https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode({**params, "format": "json", "origin": "*"})
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def claim_year(entity: dict) -> int | None:
    years = []
    for c in entity.get("claims", {}).get("P577", []):
        try:
            timev = c["mainsnak"]["datavalue"]["value"]["time"]
            m = re.match(r"[+-](\d{1,})-", timev)
            if m:
                years.append(int(m.group(1)))
        except Exception:
            pass
    return min(years) if years else None


def author_ids(entity: dict) -> list[str]:
    out = []
    for c in entity.get("claims", {}).get("P50", []):
        try:
            out.append(c["mainsnak"]["datavalue"]["value"]["id"])
        except Exception:
            pass
    return out


def labels_for(ids: list[str]) -> dict[str, str]:
    if not ids: return {}
    try:
        data = api({"action": "wbgetentities", "ids": "|".join(ids[:50]), "props": "labels", "languages": "en|zh|fr|es|pt|de|it|ja|ru"})
    except Exception:
        return {}
    out = {}
    for qid, ent in data.get("entities", {}).items():
        labels = ent.get("labels", {})
        vals = [v.get("value", "") for v in labels.values() if v.get("value")]
        out[qid] = " / ".join(dict.fromkeys(vals))
    return out


def resolve(row: dict[str, str]) -> dict[str, str]:
    titles = [x for x in [row.get("title_original", ""), row.get("title", "")] if x]
    author = row.get("author_original") or row.get("author") or ""
    search_title = titles[0] if titles else ""
    if not search_title:
        return {"wd_status": "NO_TITLE"}
    try:
        sr = api({"action": "wbsearchentities", "search": search_title, "language": "en", "uselang": "en", "type": "item", "limit": "10"})
        ids = [x.get("id", "") for x in sr.get("search", []) if x.get("id")]
        if not ids:
            return {"wd_status": "NO_MATCH"}
        data = api({"action": "wbgetentities", "ids": "|".join(ids), "props": "labels|aliases|claims", "languages": "en|zh|fr|es|pt|de|it|ja|ru"})
    except Exception as e:
        return {"wd_status": "ERROR", "wd_error": type(e).__name__}

    entities = data.get("entities", {})
    all_author_ids = []
    for e in entities.values(): all_author_ids.extend(author_ids(e))
    amap = labels_for(list(dict.fromkeys(all_author_ids)))

    best = None
    for qid in ids:
        e = entities.get(qid, {})
        labels = [v.get("value", "") for v in e.get("labels", {}).values() if v.get("value")]
        aliases = []
        for arr in e.get("aliases", {}).values():
            aliases.extend(v.get("value", "") for v in arr if v.get("value"))
        names = labels + aliases
        ts = max((sim(t, n) for t in titles for n in names), default=0.0)
        aids = author_ids(e)
        alabel = " / ".join(amap.get(a, "") for a in aids if amap.get(a, ""))
        aus = sim(author, alabel) if author else 0.0
        y = claim_year(e)
        if y is None: continue
        # Work-level title/author match. Permit small author normalization differences.
        score = ts * 0.65 + aus * 0.35
        if ts >= 0.86 and aus >= 0.68:
            cand = (score, -y, qid, y, ts, aus, labels[0] if labels else "", alabel)
            if best is None or cand > best: best = cand
    if best is None:
        return {"wd_status": "NO_RELIABLE_WORK_MATCH"}
    _, _, qid, y, ts, aus, label, alabel = best
    return {
        "wd_status": "MATCH", "wd_qid": qid, "wd_year": str(y), "wd_t": t_for_year(y),
        "wd_label": label, "wd_authors": alabel,
        "wd_title_similarity": f"{ts:.3f}", "wd_author_similarity": f"{aus:.3f}",
    }


def main() -> None:
    with TRIAGE.open(encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r.get("tier") == "P2_EXTERNAL_MATCH_FRIENDLY"]
    with OL.open(encoding="utf-8-sig", newline="") as f:
        olmap = {r.get("id", ""): r for r in csv.DictReader(f) if r.get("tier") == "P2_EXTERNAL_MATCH_FRIENDLY"}

    wdmap = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(resolve, r): r for r in rows}
        for i, fut in enumerate(as_completed(futs), 1):
            r = futs[fut]
            try: wdmap[r["id"]] = fut.result()
            except Exception as e: wdmap[r["id"]] = {"wd_status": "ERROR", "wd_error": type(e).__name__}
            if i % 50 == 0: print(f"wikidata_done={i}/{len(rows)}", flush=True)

    out, safe, review = [], [], []
    for r in rows:
        ol = olmap.get(r.get("id", ""), {})
        wd = wdmap.get(r.get("id", ""), {})
        oy = parse_int(ol.get("candidate_year", "")) if ol.get("confidence") == "HIGH" else None
        ot = ol.get("suggested_t", "") if ol.get("confidence") == "HIGH" else ""
        wy = parse_int(wd.get("wd_year", "")) if wd.get("wd_status") == "MATCH" else None
        wt = wd.get("wd_t", "") if wd.get("wd_status") == "MATCH" else ""

        status, chosen_t, year_candidate, year_action, reason = "REVIEW", "", "", "LEAVE_BLANK", ""
        if wy is None:
            reason = "Wikidata 无可靠作品级 P577+P50 匹配"
        elif wy in BOUNDARIES:
            reason = "Wikidata P577 落在冻结边界年"
        elif oy is not None and ot:
            if oy in BOUNDARIES:
                reason = "Open Library 候选落在冻结边界年"
            elif ot != wt:
                reason = f"跨来源 T 冲突：OL={oy}/{ot}, WD={wy}/{wt}"
            else:
                status, chosen_t = "SAFE_T", wt
                gap = abs(oy - wy)
                reason = f"Wikidata 作品级日期与 Open Library 落在同一 {wt}；年份差 {gap} 年"
                # Prefer Wikidata P577 as work-level canonical publication signal.
                year_candidate, year_action = str(wy), "FILL_YEAR_WIKIDATA"
        else:
            # Wikidata work-level P577 + P50 + title is sufficient for T when OL lacks a reliable hit.
            status, chosen_t = "SAFE_T_WIKIDATA_ONLY", wt
            year_candidate, year_action = str(wy), "FILL_YEAR_WIKIDATA"
            reason = "Wikidata 标题+作者+作品级 P577 高置信；Open Library 无 HIGH 候选"

        merged = dict(r)
        merged.update({
            "ol_year": "" if oy is None else str(oy), "ol_t": ot,
            "ol_title": ol.get("ol_title", ""), "ol_authors": ol.get("ol_authors", ""),
            **wd,
            "resolution_status": status, "chosen_t": chosen_t,
            "canonical_year_candidate": year_candidate, "year_action": year_action,
            "resolution_reason": reason,
        })
        out.append(merged)
        (safe if status.startswith("SAFE_T") else review).append(merged)

    fields = list(dict.fromkeys(k for row in out for k in row.keys()))
    for path, rr in [(OUT, out), (SAFE, safe), (REVIEW, review)]:
        with path.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rr)

    both = sum(r["resolution_status"] == "SAFE_T" for r in safe)
    wdonly = sum(r["resolution_status"] == "SAFE_T_WIKIDATA_ONLY" for r in safe)
    lines = [
        "# P2 Wikidata Bibliographic Verification V1", "",
        "> Read-only. Wikidata P577/P50 is treated as a work-level bibliographic signal; no Work mutation occurs here.", "",
        f"- P2 population: **{len(rows)}**",
        f"- SAFE total: **{len(safe)}**",
        f"  - SAFE_T cross-source agreement: **{both}**",
        f"  - SAFE_T_WIKIDATA_ONLY work-level match: **{wdonly}**",
        f"- REVIEW: **{len(review)}**", "",
        "## Rules", "",
        "- Wikidata candidate requires strong title match, author P50 match, and work-level publication date P577.",
        "- When Open Library HIGH exists, both sources must agree on the T interval.",
        "- A cross-T conflict blocks automatic completion.",
        "- Exact frozen boundary years are blocked.",
        "- For accepted rows, canonical year candidate comes from Wikidata P577 rather than edition-oriented catalog dates.", "",
        "`P2_WIKIDATA_V1 = AUDITED_READ_ONLY`", "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"p2={len(rows)} safe={len(safe)} cross={both} wd_only={wdonly} review={len(review)}")


if __name__ == "__main__": main()
