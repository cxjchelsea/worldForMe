from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "_audit" / "r_axis_r1"
MATRIX = AUDIT / "r1_structural_coverage_v1.csv"
OUT = AUDIT / "R1_STRUCTURAL_COVERAGE_SUMMARY_V1.md"

WEIGHT = {"COVERED": 1.0, "PARTIAL": 0.5, "MISSING": 0.0}


def pct(score: float, total: int) -> str:
    return f"{(score / total * 100):.1f}%" if total else "0.0%"


def main() -> None:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    unknown = sorted({r["status"] for r in rows if r["status"] not in WEIGHT})
    if unknown:
        raise SystemExit(f"Unknown statuses: {unknown}")

    by_tradition: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_tradition[row["tradition"]].append(row)

    total_score = sum(WEIGHT[r["status"]] for r in rows)
    total = len(rows)
    covered = sum(r["status"] == "COVERED" for r in rows)
    partial = sum(r["status"] == "PARTIAL" for r in rows)
    missing = sum(r["status"] == "MISSING" for r in rows)

    lines = [
        "# R1 Structural Coverage Summary V1",
        "",
        "> Generated from `r1_structural_coverage_v1.csv`. This report measures structural coverage, not raw book count or T-axis balance.",
        "",
        "## Overall",
        "",
        f"- Structural slots: **{total}**",
        f"- COVERED: **{covered}**",
        f"- PARTIAL: **{partial}**",
        f"- MISSING: **{missing}**",
        f"- Weighted structural coverage: **{pct(total_score, total)}** (`COVERED=1`, `PARTIAL=0.5`)",
        "",
        "## By tradition",
        "",
        "| Tradition | Slots | Covered | Partial | Missing | Weighted coverage |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    ranked = []
    for tradition, items in by_tradition.items():
        score = sum(WEIGHT[r["status"]] for r in items)
        c = sum(r["status"] == "COVERED" for r in items)
        p = sum(r["status"] == "PARTIAL" for r in items)
        m = sum(r["status"] == "MISSING" for r in items)
        ranked.append((score / len(items), tradition, len(items), c, p, m, score))

    for _, tradition, n, c, p, m, score in sorted(ranked, reverse=True):
        lines.append(f"| {tradition} | {n} | {c} | {p} | {m} | {pct(score, n)} |")

    lines += ["", "## Highest-priority structural gaps", ""]
    for priority in ("P0", "P1"):
        subset = [r for r in rows if r["priority"] == priority and r["status"] != "COVERED"]
        lines.append(f"### {priority}")
        lines.append("")
        if not subset:
            lines.append("- None")
        else:
            for r in subset:
                candidate = r["gap_candidate"] or "—"
                lines.append(f"- **{r['tradition']} / {r['slot']}** → {candidate} ({r['status']})")
        lines.append("")

    lines += [
        "## Governance",
        "",
        "- This audit does not mutate canonical Works.",
        "- A high book count cannot compensate for missing structural slots.",
        "- Candidate additions must first be searched against `40 作品/` to avoid duplicate Work creation.",
        "- T0–T6 balance is a secondary validation after R1 structural coverage is stable.",
        "",
        "`R1_STRUCTURAL_COVERAGE_V1 = AUDITED_READ_ONLY`",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"slots={total} covered={covered} partial={partial} missing={missing} weighted={pct(total_score, total)}")


if __name__ == "__main__":
    main()
