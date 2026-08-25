from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学/40 作品")
OUT = Path("个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis_completeness")
MARKER = OUT / "RUN_T_AXIS_COMPLETENESS_V1"

T_LABELS = {
    "T0": "T0 文学源头与古代文学",
    "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学",
    "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代",
    "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}
LABEL_TO_T = {v: k for k, v in T_LABELS.items()}
BOUNDARIES = {500, 1500, 1800, 1890, 1945, 1980}
SPECIAL_PATTERNS = re.compile(r"(全集|文集|选集|诗选|短篇小说集|故事集|传说|神话|史诗|往世书|歌谣|民谣|口传|选篇|作品集)")


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


def parse_year(fm: str) -> int | None:
    raw = scalar(fm, "year")
    if not raw:
        return None
    m = re.search(r"-?\d{1,4}", raw)
    return int(m.group(0)) if m else None


def expected_t(year: int) -> str:
    if year < 500:
        return "T0"
    if year < 1500:
        return "T1"
    if year < 1800:
        return "T2"
    if year < 1890:
        return "T3"
    if year < 1945:
        return "T4"
    if year < 1980:
        return "T5"
    return "T6"


def special_hint(title: str, fm: str) -> str:
    hints = []
    if SPECIAL_PATTERNS.search(title):
        hints.append("title_aggregate_or_tradition")
    if list_field(fm, "literary_traditions"):
        hints.append("literary_traditions")
    if scalar(fm, "author") in {"佚名", "匿名", "民间", "口传传统"}:
        hints.append("anonymous_or_oral")
    return ";".join(hints)


def main() -> None:
    if not MARKER.exists():
        raise SystemExit("T-axis completeness authorization marker missing")
    OUT.mkdir(parents=True, exist_ok=True)

    rows = []
    counts = Counter()
    valid_t_counts = Counter()

    for path in sorted(ROOT.glob("*.md"), key=lambda p: p.name.casefold()):
        text = path.read_text(encoding="utf-8-sig")
        fm = frontmatter(text)
        if not fm or scalar(fm, "type") != "work":
            continue

        title = scalar(fm, "title") or path.stem
        axis_t_raw = list_field(fm, "axis_t")
        valid_t = [LABEL_TO_T[x] for x in axis_t_raw if x in LABEL_TO_T]
        invalid_t = [x for x in axis_t_raw if x not in LABEL_TO_T]
        year = parse_year(fm)
        hint = special_hint(title, fm)

        if valid_t:
            status = "HAS_T"
            suggestion = ""
            reason = "已有有效 T0–T6 坐标"
            for t in valid_t:
                valid_t_counts[t] += 1
        elif invalid_t:
            status = "INVALID_T_LABEL"
            suggestion = expected_t(year) if year is not None and year not in BOUNDARIES else ""
            reason = "axis_t 非空但不匹配正式 T0–T6 标签"
        elif year is not None and year in BOUNDARIES:
            status = "MISSING_T_BOUNDARY_YEAR"
            suggestion = expected_t(year)
            reason = f"缺 T；year={year} 为操作性边界年，需人工按既定边界政策确认"
        elif year is not None:
            status = "MISSING_T_AUTO_CANDIDATE"
            suggestion = expected_t(year)
            reason = "缺 T；year 可机器读取，可按正式时间区间生成候选"
        else:
            status = "MISSING_T_REVIEW_NO_YEAR"
            suggestion = ""
            reason = "缺 T 且缺少可机器读取 year，需要书目/成书史核验"

        counts[status] += 1
        rows.append({
            "file": path.name,
            "id": scalar(fm, "id"),
            "title": title,
            "title_original": scalar(fm, "title_original"),
            "author": scalar(fm, "author"),
            "author_original": scalar(fm, "author_original"),
            "year": "" if year is None else str(year),
            "axis_t_raw": ";".join(axis_t_raw),
            "valid_t": ";".join(valid_t),
            "invalid_t": ";".join(invalid_t),
            "status": status,
            "suggested_t": suggestion,
            "special_hint": hint,
            "reason": reason,
            "verification_status": scalar(fm, "verification_status"),
            "bibliography_status": scalar(fm, "bibliography_status"),
            "canon_id": scalar(fm, "canon_id"),
        })

    fields = list(rows[0].keys()) if rows else []
    with (OUT / "all_works.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

    missing = [r for r in rows if r["status"] != "HAS_T"]
    with (OUT / "missing_t.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(missing)

    for status in ["MISSING_T_AUTO_CANDIDATE", "MISSING_T_BOUNDARY_YEAR", "MISSING_T_REVIEW_NO_YEAR", "INVALID_T_LABEL"]:
        subset = [r for r in rows if r["status"] == status]
        with (OUT / f"{status.lower()}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(subset)

    total = len(rows)
    has_t = counts["HAS_T"]
    missing_total = total - has_t
    special_missing = sum(1 for r in missing if r["special_hint"])

    md = [
        "# T-axis Completeness Audit V1", "",
        "> Read-only audit. No Work entity is modified by this stage.", "",
        "## Population", "",
        f"- Total canonical Work entities: **{total}**",
        f"- With valid T0–T6 coordinate: **{has_t}**",
        f"- Missing / invalid T coordinate: **{missing_total}**",
        f"- Missing/invalid with aggregate/oral/tradition hint: **{special_missing}**", "",
        "## Missing-T classification", "",
        f"- MISSING_T_AUTO_CANDIDATE: **{counts['MISSING_T_AUTO_CANDIDATE']}**",
        f"- MISSING_T_BOUNDARY_YEAR: **{counts['MISSING_T_BOUNDARY_YEAR']}**",
        f"- MISSING_T_REVIEW_NO_YEAR: **{counts['MISSING_T_REVIEW_NO_YEAR']}**",
        f"- INVALID_T_LABEL: **{counts['INVALID_T_LABEL']}**", "",
        "## Current valid T distribution", "",
    ]
    for t in T_LABELS:
        md.append(f"- {t}: **{valid_t_counts[t]}**")
    md += [
        "", "## Governance interpretation", "",
        "1. `MISSING_T_AUTO_CANDIDATE` is eligible for a governed batch-fill only after a sample/reasonableness check; year is a candidate signal, not proof for long-formation texts.",
        "2. `MISSING_T_BOUNDARY_YEAR` must follow the already-frozen boundary policy and should not be assigned by generic interval code alone.",
        "3. `MISSING_T_REVIEW_NO_YEAR` requires bibliographic/formation-history review; aggregate, oral, anonymous, and tradition texts should be reviewed first as model-special cases.",
        "4. `INVALID_T_LABEL` is a schema-integrity issue, not a missing-data issue.",
        "", "## Next stage", "",
        "- First resolve schema-invalid/boundary/special-text cases and sample-check AUTO candidates.",
        "- Then apply T-axis completion in controlled batches with postcondition checks.",
        "", "`T_AXIS_COMPLETENESS_V1 = AUDITED_READ_ONLY`", "",
    ]
    (OUT / "README.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    MARKER.unlink()

    print(f"TOTAL={total} HAS_T={has_t} MISSING_OR_INVALID={missing_total}")
    for key in ["MISSING_T_AUTO_CANDIDATE", "MISSING_T_BOUNDARY_YEAR", "MISSING_T_REVIEW_NO_YEAR", "INVALID_T_LABEL"]:
        print(f"{key}={counts[key]}")
    print(f"SPECIAL_MISSING={special_missing}")


if __name__ == "__main__":
    main()
