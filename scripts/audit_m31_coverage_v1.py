from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "40 作品"
OUT = ROOT / "reports"
TOPIC = "WL-TOPIC-M3-MODERNISM"

EXPECTED_TRADITIONS = [
    "19世纪前史",
    "英国—爱尔兰现代主义",
    "法国现代主义",
    "德语—奥地利—中欧现代主义",
    "俄罗斯与东欧现代主义",
    "美国与Harlem Renaissance",
    "伊比利亚与意大利现代主义",
    "拉丁美洲先锋与巴西Modernismo",
    "日本与中国现代主义",
    "南亚、波斯与阿拉伯现代主义",
    "殖民与跨国现代主义",
]


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    if not m:
        return ""
    v = m.group(1).strip()
    if v in {"null", "''", '""'}:
        return ""
    return v.strip("'\"")


def list_value(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    values: list[str] = []
    for i, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            inline = line.split(":", 1)[1].strip()
            if inline.startswith("[") and inline.endswith("]"):
                return [x.strip().strip("'\"") for x in inline[1:-1].split(",") if x.strip()]
            for nxt in lines[i + 1 :]:
                if re.match(r"^[A-Za-z0-9_]+:", nxt):
                    break
                m = re.match(r"^\s*-\s+(.*)$", nxt)
                if m:
                    values.append(m.group(1).strip().strip("'\""))
            break
    return values


records = []
for path in sorted(WORKS.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if not fm or TOPIC not in list_value(fm, "topics"):
        continue
    records.append(
        {
            "file": path.name,
            "id": scalar(fm, "id"),
            "title": scalar(fm, "title") or path.stem,
            "author": scalar(fm, "author"),
            "author_original": scalar(fm, "author_original"),
            "year": scalar(fm, "year"),
            "priority": scalar(fm, "modernism_priority"),
            "tradition": scalar(fm, "modernism_tradition_cluster"),
            "axes": list_value(fm, "modernism_axes"),
            "verification_status": scalar(fm, "verification_status"),
            "bibliography_status": scalar(fm, "bibliography_status"),
        }
    )

priority = Counter(r["priority"] or "<missing>" for r in records)
tradition = Counter(r["tradition"] or "<missing>" for r in records)
axis = Counter(a for r in records for a in r["axes"])
missing = {
    "priority": [r["file"] for r in records if not r["priority"]],
    "tradition": [r["file"] for r in records if not r["tradition"]],
    "axes": [r["file"] for r in records if not r["axes"]],
    "author": [r["file"] for r in records if not r["author"]],
    "year": [r["file"] for r in records if not r["year"]],
}

payload = {
    "topic": TOPIC,
    "canonical_work_count": len(records),
    "priority_counts": dict(priority),
    "tradition_counts": dict(sorted(tradition.items())),
    "axis_counts": dict(axis.most_common()),
    "expected_tradition_coverage": {k: tradition.get(k, 0) for k in EXPECTED_TRADITIONS},
    "missing_counts": {k: len(v) for k, v in missing.items()},
    "missing_files": missing,
    "records": records,
}

OUT.mkdir(exist_ok=True)
(OUT / "m31_coverage_audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

lines = [
    "# M3.1 现代主义书目覆盖审计",
    "",
    f"- canonical works: **{len(records)}**",
    f"- ★: **{priority.get('★', 0)}**",
    f"- ◆: **{priority.get('◆', 0)}**",
    f"- △: **{priority.get('△', 0)}**",
    f"- missing priority: **{priority.get('<missing>', 0)}**",
    "",
    "## 地域/传统覆盖",
    "",
    "| tradition | works |",
    "|---|---:|",
]
for name in EXPECTED_TRADITIONS:
    lines.append(f"| {name} | {tradition.get(name, 0)} |")
for name, n in sorted(tradition.items()):
    if name not in EXPECTED_TRADITIONS:
        lines.append(f"| {name} | {n} |")

lines += ["", "## 机制覆盖（Top 30）", "", "| mechanism | works |", "|---|---:|"]
for name, n in axis.most_common(30):
    lines.append(f"| {name} | {n} |")

lines += ["", "## 元数据缺口", ""]
for key in ["priority", "tradition", "axes", "author", "year"]:
    lines.append(f"- {key}: **{len(missing[key])}**")

lines += ["", "## 缺失机制标注的作品", ""]
for f in missing["axes"]:
    lines.append(f"- {f}")

report = "\n".join(lines) + "\n"
(OUT / "m31_coverage_audit.md").write_text(report, encoding="utf-8")
print(report)
