from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学")
WORKS = ROOT / "40 作品"
OUT = ROOT / "_audit/r_axis_r1"
MARKER = OUT / "RUN_R1_TOPIC_COVERAGE_V1"
R1_LABEL = "R1 西亚—地中海古老传统"
T_LABELS = {
    "T0 文学源头与古代文学": "T0",
    "T1 中古多中心文学世界": "T1",
    "T2 早期现代文学": "T2",
    "T3 19世纪现代文学体系": "T3",
    "T4 全球现代主义时代": "T4",
    "T5 二战后多极文学": "T5",
    "T6 当代全球文学": "T6",
}


def fm(text: str) -> str:
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    return m.group(1) if m else ""


def scalar(front: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", front)
    if not m:
        return ""
    v = m.group(1).strip().strip("\"'")
    return "" if v.lower() in {"null", "none", "~"} else v


def list_field(front: str, key: str) -> list[str]:
    lines = front.splitlines()
    for i, line in enumerate(lines):
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
                if nxt.strip() and not nxt.startswith((" ", "\t")):
                    break
            return out
    return []


def main() -> None:
    if not MARKER.exists():
        raise SystemExit("R1 coverage authorization marker missing")
    OUT.mkdir(parents=True, exist_ok=True)

    rows = []
    t_counts = Counter()
    source_counts = Counter()
    missing_year = 0
    missing_priority = 0
    missing_tradition = 0
    missing_role = 0
    total_works = 0

    for p in sorted(WORKS.glob("*.md"), key=lambda x: x.name.casefold()):
        text = p.read_text(encoding="utf-8-sig")
        front = fm(text)
        if not front or scalar(front, "type") != "work":
            continue
        total_works += 1
        axis_r = list_field(front, "axis_r")
        if R1_LABEL not in axis_r:
            continue

        axis_t = list_field(front, "axis_t")
        for label in axis_t:
            if label in T_LABELS:
                t_counts[T_LABELS[label]] += 1

        year = scalar(front, "year")
        priority = scalar(front, "r1_priority")
        tradition = scalar(front, "r1_tradition")
        role = list_field(front, "r1_role") or ([scalar(front, "r1_role")] if scalar(front, "r1_role") else [])
        if not year:
            missing_year += 1
        if not priority:
            missing_priority += 1
        if not tradition:
            missing_tradition += 1
        if not role:
            missing_role += 1

        sources = []
        for key in ["batch1_source_refs", "batch2_source_refs", "batch3_source_refs", "batch4_source_refs", "batch5_source_refs", "batch6_source_refs"]:
            vals = list_field(front, key)
            if vals:
                source_counts[key] += 1
                sources.extend(vals)

        rows.append({
            "file": p.name,
            "id": scalar(front, "id"),
            "title": scalar(front, "title") or p.stem,
            "title_original": scalar(front, "title_original"),
            "author": scalar(front, "author"),
            "author_original": scalar(front, "author_original"),
            "year": year,
            "axis_t": ";".join(axis_t),
            "axis_r": ";".join(axis_r),
            "r1_priority": priority,
            "r1_tradition": tradition,
            "r1_role": ";".join(role),
            "canon_id": scalar(front, "canon_id"),
            "read_status": scalar(front, "read_status"),
            "verification_status": scalar(front, "verification_status"),
            "source_refs": ";".join(sources),
        })

    fields = list(rows[0].keys()) if rows else []
    with (OUT / "r1_works_v1.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

    no_year = [r for r in rows if not r["year"]]
    with (OUT / "r1_missing_year_v1.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(no_year)

    md = [
        "# R1 Topic Coverage Audit V1", "",
        "> Read-only audit. No canonical Work was modified.", "",
        "## Population", "",
        f"- Total canonical Work entities: **{total_works}**",
        f"- Works currently mapped to R1: **{len(rows)}**",
        f"- R1 share of canonical Works: **{(len(rows)/total_works*100 if total_works else 0):.1f}%**", "",
        "## R1 metadata completeness", "",
        f"- Missing `year`: **{missing_year}**",
        f"- Missing `r1_priority`: **{missing_priority}**",
        f"- Missing `r1_tradition`: **{missing_tradition}**",
        f"- Missing `r1_role`: **{missing_role}**", "",
        "## T distribution inside R1", "",
    ]
    for t in ["T0","T1","T2","T3","T4","T5","T6"]:
        md.append(f"- {t}: **{t_counts[t]}**")
    md += ["", "## Provenance coverage", ""]
    for k, v in sorted(source_counts.items()):
        md.append(f"- {k}: **{v}** works")
    md += [
        "", "## Interpretation", "",
        "1. This audit measures current R1 mapping coverage, not the historical completeness of the R1 canon.",
        "2. Empty `r1_*` fields are expected before topic enrichment; they define the next enrichment queue.",
        "3. Works with missing year should reuse the governed year/T bibliographic policy rather than infer dates from modern editions.",
        "4. A later semantic review must test whether current R1 assignments contain false positives and whether major R1 works are currently unmapped.",
        "", "`R1_TOPIC_COVERAGE_V1 = AUDITED_READ_ONLY`", "",
    ]
    (OUT / "README.md").write_text("\n".join(md), encoding="utf-8")
    MARKER.unlink()
    print(f"TOTAL={total_works} R1={len(rows)} MISSING_YEAR={missing_year} MISSING_TRADITION={missing_tradition}")


if __name__ == "__main__":
    main()
