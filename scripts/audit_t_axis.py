from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学/40 作品")
OUT = Path("个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis")

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


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    return m.group(1) if m else ""


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", fm)
    if not m:
        return ""
    value = m.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]
    return value


def list_field(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    out: list[str] = []
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:\s*\[\s*\]\s*$", line):
            return []
        inline = re.match(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", line)
        if inline:
            raw = inline.group(1).strip()
            if not raw:
                return []
            return [x.strip().strip('"\'') for x in raw.split(",")]
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            for nxt in lines[i + 1 :]:
                if not nxt.startswith((" ", "\t")):
                    break
                m = re.match(r"^\s*-\s*(.*?)\s*$", nxt)
                if m:
                    out.append(m.group(1).strip().strip('"\''))
            return out
    return []


def parse_year(fm: str) -> int | None:
    raw = scalar(fm, "year")
    if not raw:
        return None
    m = re.search(r"-?\d{1,4}", raw)
    return int(m.group(0)) if m else None


def expected_t(year: int) -> str | None:
    if year in BOUNDARIES:
        return None
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


def classify(current: list[str], year: int | None) -> tuple[str, str, str]:
    if len(current) > 1:
        return "REVIEW", "", "一个作品同时挂多个 T 节点"
    if year is None:
        return "REVIEW", "", "缺少可机器读取的 year；需要按成书/定稿/首次发表史人工核验"
    if year in BOUNDARIES:
        return "BOUNDARY", "", f"year={year} 恰落在 T 轴操作性断点，需要人工确认归属口径"
    exp = expected_t(year)
    cur = current[0] if current else ""
    if cur == exp:
        return "PASS", exp or "", "按 year 与正式 T 轴范围一致"
    return "MOVE_CANDIDATE", exp or "", f"year={year} 与当前 {cur} 不一致"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []

    for path in sorted(ROOT.glob("*.md"), key=lambda p: p.name.casefold()):
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if not fm:
            continue
        axis_t = list_field(fm, "axis_t")
        current = [LABEL_TO_T[x] for x in axis_t if x in LABEL_TO_T]
        if not current:
            continue
        year = parse_year(fm)
        status, suggested, reason = classify(current, year)
        rows.append(
            {
                "file": path.name,
                "title": scalar(fm, "title") or path.stem,
                "author": scalar(fm, "author"),
                "year": "" if year is None else str(year),
                "current_t": ";".join(current),
                "current_axis_t": ";".join(axis_t),
                "suggested_t_by_year": suggested,
                "status": status,
                "reason": reason,
                "verification_status": scalar(fm, "verification_status"),
                "id": scalar(fm, "id"),
            }
        )

    fields = [
        "file", "title", "author", "year", "current_t", "current_axis_t",
        "suggested_t_by_year", "status", "reason", "verification_status", "id",
    ]

    with (OUT / "all_t_axis_works.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    by_t: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        for t in row["current_t"].split(";"):
            if t:
                by_t[t].append(row)
    for t in T_LABELS:
        with (OUT / f"{t}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(by_t[t])

    anomalies = [r for r in rows if r["status"] != "PASS"]
    with (OUT / "anomalies.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(anomalies)

    counts = Counter(r["status"] for r in rows)
    t_counts = {t: len(by_t[t]) for t in T_LABELS}
    lines = [
        "# T0–T6 全量时间归类机器初筛",
        "",
        "> 本报告只做机器初筛，不修改任何作品实体。PASS 仅表示 `year` 与当前 T 轴范围一致；古代长期成书文本、边界年份及缺 year 项仍需人工语义核验。",
        "",
        "## 总量",
        "",
        f"- 命中 T0–T6 的作品实体：**{len(rows)}**",
    ]
    for t in T_LABELS:
        lines.append(f"- {t}: **{t_counts[t]}**")
    lines += ["", "## 初筛状态", ""]
    for key in ["PASS", "MOVE_CANDIDATE", "BOUNDARY", "REVIEW"]:
        lines.append(f"- {key}: **{counts[key]}**")
    lines += [
        "",
        "## 审计口径",
        "",
        "- T0：< 500；500 为边界年",
        "- T1：500–1500；1500 为边界年",
        "- T2：1500–1800；1800 为边界年",
        "- T3：1800–1890；1890 为边界年",
        "- T4：1890–1945；1945 为边界年",
        "- T5：1945–1980；1980 为边界年",
        "- T6：1980–至今",
        "",
        "机器阶段对恰落断点的年份统一标为 `BOUNDARY`，不自动决定左右归属。",
        "",
        "## 下一步",
        "",
        "1. 人工核验全部 `MOVE_CANDIDATE`。",
        "2. 人工核验全部 `BOUNDARY`。",
        "3. 对 `REVIEW` 中缺 year 的古代/中古文本按成书史、定型史与现存文本史核验。",
        "4. 人工核验完成后再统一修改作品实体。",
    ]
    (OUT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"works={len(rows)}")
    print(" ".join(f"{k}={counts[k]}" for k in ["PASS", "MOVE_CANDIDATE", "BOUNDARY", "REVIEW"]))
    print(" ".join(f"{t}={t_counts[t]}" for t in T_LABELS))


if __name__ == "__main__":
    main()
