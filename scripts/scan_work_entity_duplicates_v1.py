from __future__ import annotations

import csv
import re
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学/40 作品")
OUT = Path("个人通识知识系统_v2_A2/30 世界文学/_audit/entity_dedup_scan")
MARKER = OUT / "RUN_ENTITY_DEDUP_SCAN_V1"


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
        if re.match(rf"^{re.escape(key)}:\s*\[\s*\]\s*$", line):
            return []
        inline = re.match(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", line)
        if inline:
            raw = inline.group(1).strip()
            return [] if not raw else [x.strip().strip("\"'") for x in raw.split(",")]
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            out = []
            for nxt in lines[i + 1 :]:
                m = re.match(r"^\s*-\s*(.*?)\s*$", nxt)
                if m:
                    out.append(m.group(1).strip().strip("\"'"))
                    continue
                if re.match(r"^[A-Za-z0-9_\u4e00-\u9fff].*?:", nxt):
                    break
                if nxt.strip() and not nxt.startswith((" ", "\t")):
                    break
            return out
    return []


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").casefold()
    s = s.replace("·", "").replace("・", "")
    return "".join(ch for ch in s if ch.isalnum() or "\u4e00" <= ch <= "\u9fff")


def author_keys(r: dict) -> set[str]:
    vals = [r["author"], r["author_original"]]
    return {norm(x) for x in vals if norm(x)}


def title_keys(r: dict) -> set[str]:
    vals = [r["title"], r["title_original"], *r["aliases"]]
    return {norm(x) for x in vals if len(norm(x)) >= 2}


def same_author(a: dict, b: dict) -> bool:
    return bool(author_keys(a) & author_keys(b))


def year_gap(a: dict, b: dict) -> int | None:
    try:
        ya, yb = int(a["year"]), int(b["year"])
        return abs(ya - yb)
    except Exception:
        return None


def classify(a: dict, b: dict) -> tuple[str, float, str]:
    ta, tb = title_keys(a), title_keys(b)
    ak, bk = author_keys(a), author_keys(b)
    exact_title = bool(ta & tb)
    same_auth = bool(ak & bk)
    same_canon = bool(a["canon_id"] and a["canon_id"] == b["canon_id"])
    gap = year_gap(a, b)

    if same_canon:
        return "HIGH_CONFIDENCE", 1.0, "same canon_id"
    if exact_title and same_auth:
        if gap is None or gap <= 2:
            return "HIGH_CONFIDENCE", 0.99, "same normalized title/original/alias + same author"
        return "REVIEW", 0.90, f"same title+author but year gap={gap}"
    if exact_title and not same_auth:
        return "TITLE_COLLISION", 0.20, "same normalized title but author differs/unknown"

    if same_auth:
        best = 0.0
        pair = ("", "")
        for x in ta:
            for y in tb:
                score = SequenceMatcher(None, x, y).ratio()
                if score > best:
                    best, pair = score, (x, y)
        if best >= 0.93 and min(len(pair[0]), len(pair[1])) >= 4:
            return "REVIEW", best, "very similar title + same author"
        if best >= 0.84 and min(len(pair[0]), len(pair[1])) >= 6:
            return "REVIEW", best, "similar title + same author"
    return "", 0.0, ""


def main() -> None:
    if not MARKER.exists():
        raise SystemExit("scan authorization marker missing")
    OUT.mkdir(parents=True, exist_ok=True)

    works = []
    for p in sorted(ROOT.glob("*.md"), key=lambda x: x.name.casefold()):
        fm = frontmatter(p.read_text(encoding="utf-8-sig"))
        if not fm or scalar(fm, "type") != "work":
            continue
        works.append({
            "file": p.name,
            "id": scalar(fm, "id"),
            "title": scalar(fm, "title") or p.stem,
            "title_original": scalar(fm, "title_original"),
            "aliases": list_field(fm, "aliases"),
            "author": scalar(fm, "author"),
            "author_original": scalar(fm, "author_original"),
            "year": scalar(fm, "year"),
            "canon_id": scalar(fm, "canon_id"),
        })

    rows = []
    for i, a in enumerate(works):
        for b in works[i + 1:]:
            status, score, reason = classify(a, b)
            if not status:
                continue
            rows.append({
                "status": status,
                "score": f"{score:.3f}",
                "file_a": a["file"], "id_a": a["id"], "title_a": a["title"], "author_a": a["author"], "year_a": a["year"],
                "file_b": b["file"], "id_b": b["id"], "title_b": b["title"], "author_b": b["author"], "year_b": b["year"],
                "reason": reason,
            })

    order = {"HIGH_CONFIDENCE": 0, "REVIEW": 1, "TITLE_COLLISION": 2}
    rows.sort(key=lambda r: (order[r["status"]], -float(r["score"]), r["file_a"], r["file_b"]))
    fields = list(rows[0].keys()) if rows else ["status","score","file_a","id_a","title_a","author_a","year_a","file_b","id_b","title_b","author_b","year_b","reason"]
    with (OUT / "candidates.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

    counts = defaultdict(int)
    for r in rows: counts[r["status"]] += 1
    md = [
        "# Canonical Work Duplicate Candidate Scan V1", "",
        f"- Work entities scanned: **{len(works)}**",
        f"- HIGH_CONFIDENCE pairs: **{counts['HIGH_CONFIDENCE']}**",
        f"- REVIEW pairs: **{counts['REVIEW']}**",
        f"- TITLE_COLLISION pairs: **{counts['TITLE_COLLISION']}**", "",
        "This scan is read-only for `40 作品`: it does not merge or delete Work entities.", "",
        "## HIGH_CONFIDENCE", "",
    ]
    high = [r for r in rows if r["status"] == "HIGH_CONFIDENCE"]
    if high:
        for r in high:
            md.append(f"- `{r['file_a']}` ↔ `{r['file_b']}` — {r['reason']}")
    else:
        md.append("- None")
    md += ["", "## REVIEW", ""]
    rev = [r for r in rows if r["status"] == "REVIEW"]
    if rev:
        for r in rev[:200]:
            md.append(f"- `{r['file_a']}` ↔ `{r['file_b']}` — score {r['score']}; {r['reason']}")
    else:
        md.append("- None")
    md += ["", "## TITLE_COLLISION", "", "Same/similar titles with different or unresolved authors are explicitly not auto-merge candidates.", ""]
    col = [r for r in rows if r["status"] == "TITLE_COLLISION"]
    for r in col[:200]:
        md.append(f"- `{r['file_a']}` ↔ `{r['file_b']}` — {r['reason']}")
    md += ["", "`ENTITY_DEDUP_SCAN_V1 = COMPLETE_READ_ONLY_SCAN`", ""]
    (OUT / "ENTITY_DEDUP_SCAN_V1.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    MARKER.unlink()

if __name__ == "__main__":
    main()
