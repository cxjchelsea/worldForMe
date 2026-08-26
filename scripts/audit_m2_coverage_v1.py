from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "40 作品"
OUT = ROOT / "reports"
TOPIC = "WL-TOPIC-M2-19C-MOVEMENTS"
EXPECTED_MOVEMENTS = [
    "浪漫主义",
    "超验主义",
    "现实主义",
    "自然主义",
    "象征主义",
    "唯美主义",
    "颓废主义",
    "拉美 Modernismo",
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
    records.append({
        "file": path.name,
        "id": scalar(fm, "id"),
        "title": scalar(fm, "title") or path.stem,
        "author": scalar(fm, "author"),
        "year": scalar(fm, "year"),
        "priority": scalar(fm, "m2_priority"),
        "movement": scalar(fm, "m2_movement_cluster"),
        "axes": list_value(fm, "m2_axes"),
        "axis_m": list_value(fm, "axis_m"),
        "bibliography_status": scalar(fm, "bibliography_status"),
    })

priority = Counter(r["priority"] or "<missing>" for r in records)
movement = Counter(r["movement"] or "<missing>" for r in records)
axes = Counter(a for r in records for a in r["axes"])
missing = {
    "priority": [r["file"] for r in records if not r["priority"]],
    "movement": [r["file"] for r in records if not r["movement"]],
    "axes": [r["file"] for r in records if not r["axes"]],
    "author": [r["file"] for r in records if not r["author"]],
    "year": [r["file"] for r in records if not r["year"]],
}
unexpected = {k: v for k, v in movement.items() if k not in EXPECTED_MOVEMENTS and k != "<missing>"}
axis_m_mismatch = [
    r["file"] for r in records
    if r["movement"] and f"M2 19世纪文学思潮 / {r['movement']}" not in r["axis_m"]
]

payload = {
    "topic": TOPIC,
    "canonical_work_count": len(records),
    "priority_counts": dict(priority),
    "movement_counts": dict(movement),
    "axis_counts": dict(axes.most_common()),
    "expected_movement_coverage": {k: movement.get(k, 0) for k in EXPECTED_MOVEMENTS},
    "missing_counts": {k: len(v) for k, v in missing.items()},
    "unexpected_movements": unexpected,
    "axis_m_mismatch_count": len(axis_m_mismatch),
    "axis_m_mismatch_files": axis_m_mismatch,
    "records": records,
}
OUT.mkdir(exist_ok=True)
(OUT / "m2_coverage_audit.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

lines = [
    "# M2 19世纪文学思潮书目覆盖审计",
    "",
    f"- canonical works: **{len(records)}**",
    f"- ★: **{priority.get('★', 0)}**",
    f"- ◆: **{priority.get('◆', 0)}**",
    f"- missing priority: **{priority.get('<missing>', 0)}**",
    f"- unexpected movements: **{sum(unexpected.values())}**",
    f"- axis_m mismatch: **{len(axis_m_mismatch)}**",
    "",
    "## 八个思潮覆盖",
    "",
    "| movement | works |",
    "|---|---:|",
]
for name in EXPECTED_MOVEMENTS:
    lines.append(f"| {name} | {movement.get(name, 0)} |")

lines += ["", "## 机制覆盖（Top 30）", "", "| mechanism | works |", "|---|---:|"]
for name, n in axes.most_common(30):
    lines.append(f"| {name} | {n} |")

lines += ["", "## 元数据缺口", ""]
for key in ["priority", "movement", "axes", "author", "year"]:
    lines.append(f"- {key}: **{len(missing[key])}**")

if unexpected:
    lines += ["", "## 非预期思潮", ""]
    for k, v in unexpected.items():
        lines.append(f"- {k}: {v}")
if axis_m_mismatch:
    lines += ["", "## axis_m 与 movement 不一致", ""]
    for f in axis_m_mismatch:
        lines.append(f"- {f}")

report = "\n".join(lines) + "\n"
(OUT / "m2_coverage_audit.md").write_text(report, encoding="utf-8")
print(report)
