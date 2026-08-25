from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学/40 作品")
OUT = Path("个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis_completeness")
MARKER = OUT / "RUN_MISSING_T_INTERNAL_YEAR_EVIDENCE_V1"

T_LABELS = {
    "T0": "T0 文学源头与古代文学",
    "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学",
    "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代",
    "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}
BOUNDARIES = {500, 1500, 1800, 1890, 1945, 1980}

YEAR_LABEL_PATTERNS = [
    re.compile(r"(?:首次出版(?:年)?|首次发表(?:年)?|初版(?:年)?|出版(?:年)?|成书(?:时间|年)?|定稿(?:年)?|首刊(?:年)?|年代\s*/\s*首次成书时间)\s*[：:]\s*(?:约\s*)?(-?\d{1,4})"),
    re.compile(r"(?:首次出版|首次发表|初版|成书|定稿|首刊)\s*(?:于|：|:)\s*(?:约\s*)?(-?\d{1,4})\s*年?"),
]


def frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else ("", text)


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
            for nxt in lines[i + 1:]:
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


def parse_year_scalar(fm: str) -> int | None:
    raw = scalar(fm, "year")
    if not raw:
        return None
    m = re.search(r"-?\d{1,4}", raw)
    return int(m.group(0)) if m else None


def t_for_year(year: int) -> str:
    if year < 500: return "T0"
    if year < 1500: return "T1"
    if year < 1800: return "T2"
    if year < 1890: return "T3"
    if year < 1945: return "T4"
    if year < 1980: return "T5"
    return "T6"


def extract_body_year(body: str) -> tuple[int | None, str]:
    hits = []
    for pat in YEAR_LABEL_PATTERNS:
        for m in pat.finditer(body):
            try:
                y = int(m.group(1))
            except Exception:
                continue
            if -3000 <= y <= 2100:
                hits.append((y, m.group(0)))
    uniq = []
    seen = set()
    for y, ctx in hits:
        if y not in seen:
            uniq.append((y, ctx)); seen.add(y)
    if len(uniq) == 1:
        return uniq[0]
    return None, " | ".join(ctx for _, ctx in uniq[:5])


def source_ref_keys(fm: str) -> list[str]:
    out = []
    for m in re.finditer(r"(?m)^([A-Za-z0-9_]+_source_refs):\s*$", fm):
        out.append(m.group(1))
    return out


def main() -> None:
    if not MARKER.exists():
        raise SystemExit("internal year-evidence authorization marker missing")
    OUT.mkdir(parents=True, exist_ok=True)

    rows = []
    source_counts = Counter()
    topic_counts = Counter()
    body_year_count = 0

    for path in sorted(ROOT.glob("*.md"), key=lambda p: p.name.casefold()):
        text = path.read_text(encoding="utf-8-sig")
        fm, body = frontmatter(text)
        if not fm or scalar(fm, "type") != "work":
            continue
        if list_field(fm, "axis_t"):
            continue
        if parse_year_scalar(fm) is not None:
            continue

        body_year, evidence = extract_body_year(body)
        if body_year is not None:
            body_year_count += 1
        src_keys = source_ref_keys(fm)
        for k in src_keys:
            source_counts[k] += 1
        topics = list_field(fm, "topics")
        for t in topics:
            topic_counts[t] += 1

        rows.append({
            "file": path.name,
            "id": scalar(fm, "id"),
            "title": scalar(fm, "title") or path.stem,
            "author": scalar(fm, "author"),
            "body_year": "" if body_year is None else str(body_year),
            "suggested_t": "" if body_year is None else t_for_year(body_year),
            "is_boundary_year": "YES" if body_year in BOUNDARIES else "NO",
            "evidence": evidence,
            "source_ref_keys": ";".join(src_keys),
            "topics": ";".join(topics),
            "canon_id": scalar(fm, "canon_id"),
            "awards": ";".join(list_field(fm, "awards")),
            "verification_status": scalar(fm, "verification_status"),
            "bibliography_status": scalar(fm, "bibliography_status"),
        })

    fields = list(rows[0].keys()) if rows else []
    with (OUT / "internal_year_evidence.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    recovered = [r for r in rows if r["body_year"]]
    with (OUT / "internal_year_recovered.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(recovered)

    md = [
        "# Missing-T Internal Year Evidence Audit V1", "",
        f"- Missing-T / missing-frontmatter-year works inspected: **{len(rows)}**",
        f"- Unique explicit publication/formation year recoverable from Work body: **{body_year_count}**",
        f"- Still requiring other evidence: **{len(rows) - body_year_count}**", "",
        "## Source-ref coverage", "",
    ]
    if source_counts:
        for k, n in source_counts.most_common():
            md.append(f"- {k}: **{n}**")
    else:
        md.append("- No batch source-ref keys detected")
    md += ["", "## Most common topic sources among unresolved population", ""]
    for k, n in topic_counts.most_common(30):
        md.append(f"- {k}: **{n}**")
    md += [
        "", "## Interpretation", "",
        "- A body-year hit is only an internal evidence candidate. It should be applied only after excluding anthology/edition dates and boundary-year ambiguities.",
        "- The source-ref distribution identifies which ingestion batches should be repaired upstream so year and T can be populated systematically rather than title-by-title.",
        "", "`MISSING_T_INTERNAL_YEAR_EVIDENCE_V1 = AUDITED_READ_ONLY`", "",
    ]
    (OUT / "INTERNAL_YEAR_EVIDENCE_V1.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    MARKER.unlink()

    print(f"INSPECTED={len(rows)} RECOVERABLE_BODY_YEAR={body_year_count} UNRESOLVED={len(rows)-body_year_count}")
    print("SOURCE_COUNTS=" + ",".join(f"{k}:{v}" for k,v in source_counts.most_common()))


if __name__ == "__main__":
    main()
