# -*- coding: utf-8 -*-
"""Migrate world-literature work coordinates from legacy axis_q to axis_qh/axis_qt.

Safety contract:
- Source of truth remains 个人通识知识系统_v2_A2/30 世界文学/40 作品/*.md.
- Classification is lexical only: values beginning with QH -> axis_qh; QT -> axis_qt.
- Unknown / malformed values are reported and never inferred.
- legacy axis_q is preserved unchanged for compatibility.
- qx and qc_relations are never created or modified.
- Existing axis_qh / axis_qt values are preserved and only missing legacy values are appended.

Run:
  python scripts/migrate_literature_q_fields.py --check
  python scripts/migrate_literature_q_fields.py --apply
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORLD = REPO / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = WORLD / "40 作品"
DEFAULT_REPORT = WORLD / "04 系统架构" / "03 Q字段迁移审计.md"

TOP_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$")
LIST_RE = re.compile(r"^\s*-\s+(.*)$")


@dataclass
class AuditItem:
    path: Path
    legacy: list[str] = field(default_factory=list)
    qh: list[str] = field(default_factory=list)
    qt: list[str] = field(default_factory=list)
    unknown: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    has_qx: bool = False
    has_qc: bool = False
    changed: bool = False


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5 :]


def key_span(lines: list[str], key: str):
    start = None
    inline = None
    for i, line in enumerate(lines):
        m = TOP_KEY_RE.match(line)
        if m and m.group(1) == key:
            start = i
            inline = (m.group(2) or "").strip()
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if TOP_KEY_RE.match(lines[j]):
            end = j
            break
    return start, end, inline


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        quote = value[0]
        body = value[1:-1]
        if quote == '"':
            body = body.replace('\\"', '"').replace('\\\\', '\\')
        else:
            body = body.replace("''", "'")
        return body
    return value


def parse_inline_list(inline: str, key: str) -> tuple[list[str] | None, str | None]:
    if inline in ("[]", "null", "~"):
        return [], None
    if not (inline.startswith("[") and inline.endswith("]")):
        return None, f"{key} 使用不支持的行内格式：{inline}"
    try:
        try:
            value = json.loads(inline)
        except json.JSONDecodeError:
            value = ast.literal_eval(inline)
    except Exception as exc:
        return None, f"{key} 行内列表无法解析：{inline} ({exc})"
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        return None, f"{key} 行内值不是字符串列表：{inline}"
    return list(value), None


def parse_list(lines: list[str], key: str) -> tuple[list[str] | None, str | None]:
    span = key_span(lines, key)
    if span is None:
        return None, None
    start, end, inline = span
    if inline:
        return parse_inline_list(inline, key)
    values: list[str] = []
    for line in lines[start + 1 : end]:
        if not line.strip():
            continue
        m = LIST_RE.match(line)
        if not m:
            return None, f"{key} 含非列表行：{line.strip()}"
        values.append(unquote(m.group(1)))
    return values, None


def yaml_quote(value: str) -> str:
    # JSON string syntax is valid YAML and keeps Chinese readable.
    return json.dumps(value, ensure_ascii=False)


def replace_or_insert_list(lines: list[str], key: str, values: list[str], before_key: str) -> list[str]:
    span = key_span(lines, key)
    block = [f"{key}:"] + [f"- {yaml_quote(v)}" for v in values]
    if not values:
        block = [f"{key}: []"]
    if span is not None:
        start, end, _ = span
        return lines[:start] + block + lines[end:]
    before = key_span(lines, before_key)
    index = before[0] if before is not None else len(lines)
    return lines[:index] + block + lines[index:]


def classify(values: list[str]) -> tuple[list[str], list[str], list[str]]:
    qh, qt, unknown = [], [], []
    for value in values:
        token = value.lstrip()
        if re.match(r"^QH(?:\d|\.)", token, re.I):
            qh.append(value)
        elif re.match(r"^QT(?:\d|\.)", token, re.I):
            qt.append(value)
        else:
            unknown.append(value)
    return qh, qt, unknown


def dedup(values: list[str]) -> list[str]:
    out: list[str] = []
    seen = set()
    for value in values:
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def scalar(lines: list[str], key: str) -> str:
    span = key_span(lines, key)
    if span is None:
        return ""
    _, _, inline = span
    return unquote(inline or "")


def inspect_and_migrate(path: Path, apply: bool) -> AuditItem | None:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None:
        return None
    lines = fm.splitlines()
    if scalar(lines, "type") != "work":
        return None

    item = AuditItem(path=path)
    item.has_qx = key_span(lines, "qx") is not None
    item.has_qc = key_span(lines, "qc_relations") is not None

    legacy, err = parse_list(lines, "axis_q")
    if err:
        item.errors.append(err)
        return item
    if legacy is None:
        return item
    item.legacy = legacy

    qh_old, err_qh = parse_list(lines, "axis_qh")
    qt_old, err_qt = parse_list(lines, "axis_qt")
    if err_qh:
        item.errors.append(err_qh)
    if err_qt:
        item.errors.append(err_qt)
    if item.errors:
        return item

    qh_from_legacy, qt_from_legacy, unknown = classify(legacy)
    item.unknown = unknown
    if unknown:
        # Unknown legacy values make this file non-mechanical. Do not partially rewrite it.
        return item

    item.qh = dedup((qh_old or []) + qh_from_legacy)
    item.qt = dedup((qt_old or []) + qt_from_legacy)

    # Only change if canonical fields are missing/incomplete. axis_q is intentionally untouched.
    needs_change = (qh_old is None or item.qh != qh_old) or (qt_old is None or item.qt != qt_old)
    if apply and needs_change:
        new_lines = replace_or_insert_list(lines, "axis_qh", item.qh, "axis_q")
        new_lines = replace_or_insert_list(new_lines, "axis_qt", item.qt, "axis_q")
        new_fm = "\n".join(new_lines)
        new_text = "---\n" + new_fm + "\n---\n" + body
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            item.changed = True
    return item


def scan(apply: bool) -> tuple[list[AuditItem], int]:
    items: list[AuditItem] = []
    changed = 0
    for path in sorted(WORKS.glob("*.md")):
        item = inspect_and_migrate(path, apply=apply)
        if item is not None:
            items.append(item)
            changed += int(item.changed)
    return items, changed


def validate_structure() -> dict[str, list[str]]:
    result = {"ok": [], "warn": [], "error": []}
    required = [
        WORLD / "04 系统架构" / "00 作品坐标与知识网络总则.md",
        WORLD / "04 系统架构" / "01 作品坐标系统.md",
        WORLD / "04 系统架构" / "02 作品知识网络.md",
        WORKS / "01 作品字段规范.md",
        WORKS / "00 世界文学作品库.base",
        WORLD / "03 世界文学节点.base",
        WORLD / "01 世界文学总地图.canvas",
    ]
    for path in required:
        if path.exists():
            result["ok"].append(f"存在：{path.relative_to(REPO).as_posix()}")
        else:
            result["error"].append(f"缺失：{path.relative_to(REPO).as_posix()}")

    canvas = WORLD / "01 世界文学总地图.canvas"
    if canvas.exists():
        try:
            json.loads(canvas.read_text(encoding="utf-8"))
            result["ok"].append("世界文学总地图.canvas JSON 可解析")
        except Exception as exc:
            result["error"].append(f"世界文学总地图.canvas JSON 解析失败：{exc}")

    work_base = WORKS / "00 世界文学作品库.base"
    if work_base.exists():
        base_text = work_base.read_text(encoding="utf-8")
        for key in ("axis_qh", "axis_qt", "qx", "qc_relations"):
            if key not in base_text:
                result["error"].append(f"作品 Base 未发现字段：{key}")
        if "axis_q" in base_text:
            result["ok"].append("作品 Base 仍保留 axis_q 兼容观察入口")

    map_text = canvas.read_text(encoding="utf-8") if canvas.exists() else ""
    for label in ("作品坐标系统", "作品知识网络", "QH", "QT", "QX", "QC"):
        if label not in map_text:
            result["warn"].append(f"总地图未检出文本：{label}")
    return result


def legacy_semantic_hits() -> list[str]:
    hits: list[str] = []
    patterns = ("五轴", "Q轴", "axis: Q")
    suffixes = {".md", ".base", ".canvas", ".py", ".yml", ".yaml"}
    for path in sorted(WORLD.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for no, line in enumerate(lines, 1):
            if any(p in line for p in patterns):
                rel = path.relative_to(WORLD).as_posix()
                hits.append(f"{rel}:{no}: {line.strip()[:180]}")
    return hits


def render_report(items: list[AuditItem], applied: int, structure: dict[str, list[str]], semantic_hits: list[str]) -> str:
    works = len(items)
    with_legacy = [i for i in items if i.legacy or key_exists(i.path, "axis_q")]
    errors = [i for i in items if i.errors]
    unknown = [i for i in items if i.unknown]
    canonical_qh = [i for i in items if key_exists(i.path, "axis_qh")]
    canonical_qt = [i for i in items if key_exists(i.path, "axis_qt")]
    qx = [i for i in items if i.has_qx]
    qc = [i for i in items if i.has_qc]

    lines = [
        "---",
        "id: WL-ARCH-Q-MIGRATION-AUDIT",
        "type: literature_governance",
        "scope: q_coordinate_network_migration",
        "status: ACTIVE",
        "generated_by: scripts/migrate_literature_q_fields.py",
        "---",
        "# Q 字段迁移审计",
        "",
        "> 本报告由迁移脚本生成。迁移只依据既有 `axis_q` 值的 `QH*` / `QT*` 前缀做机械拆分，不推断作品内容；旧 `axis_q` 保留兼容；`qx` / `qc_relations` 不由本脚本创建或改写。",
        "",
        "## 1. 作品字段覆盖",
        "",
        f"- 扫描 `type: work`：**{works}** 部",
        f"- 含 legacy `axis_q`：**{len(with_legacy)}** 部",
        f"- 含 canonical `axis_qh`：**{len(canonical_qh)}** 部",
        f"- 含 canonical `axis_qt`：**{len(canonical_qt)}** 部",
        f"- 含 `qx` 字段：**{len(qx)}** 部",
        f"- 含 `qc_relations` 字段：**{len(qc)}** 部",
        f"- 本次自动改写：**{applied}** 部",
        f"- 非机械异常：**{len(errors) + len(unknown)}** 部",
        "",
        "### 迁移原则",
        "",
        "- `QH*` → `axis_qh`",
        "- `QT*` → `axis_qt`",
        "- 既有 `axis_qh` / `axis_qt` 只补缺，不覆盖人工校准值",
        "- `axis_q` 保留，作为迁移期兼容字段",
        "- 无法由前缀确定的值不迁移，只报告",
        "- 不生成任何 QX / QC 关系",
        "",
        "## 2. 非机械异常",
        "",
    ]
    if not errors and not unknown:
        lines.append("未发现阻断自动拆分的异常。")
    else:
        for item in errors + unknown:
            rel = item.path.relative_to(WORKS).as_posix()
            reasons = item.errors + (["未知 axis_q 值：" + "；".join(item.unknown)] if item.unknown else [])
            lines.append(f"- `{rel}`：{'；'.join(reasons)}")

    lines += ["", "## 3. 架构 / Base / Canvas 校验", ""]
    for msg in structure["ok"]:
        lines.append(f"- PASS：{msg}")
    for msg in structure["warn"]:
        lines.append(f"- WARN：{msg}")
    for msg in structure["error"]:
        lines.append(f"- FAIL：{msg}")

    lines += [
        "",
        "## 4. 旧语义残留扫描",
        "",
        "> 下列命中不自动等于错误。兼容入口、迁移说明、历史审计记录可以合法保留；这里的作用是防止旧“五轴 / Q轴同类子轴”语义无意继续成为 canonical 规则。",
        "",
    ]
    if semantic_hits:
        lines.extend(f"- `{hit}`" for hit in semantic_hits)
    else:
        lines.append("未检出 `五轴` / `Q轴` / `axis: Q` 文本。")

    lines += [
        "",
        "## 5. 结论",
        "",
        "当前迁移的机器数据模型以 `axis_t/r/m/g/qh/qt` 为作品坐标，以 `qx` / `qc_relations` 为稀疏知识网络关系。`axis_q` 与旧 Q 路径只承担兼容职责，在覆盖率与链接核验完成前不删除。",
        "",
    ]
    return "\n".join(lines)


def key_exists(path: Path, key: str) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, _ = split_frontmatter(text)
    if fm is None:
        return False
    return key_span(fm.splitlines(), key) is not None


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="Apply mechanical QH/QT field migration")
    mode.add_argument("--check", action="store_true", help="Audit only (default)")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    items, applied = scan(apply=args.apply)
    # Re-scan after apply so coverage and structure reflect the resulting repository state.
    if args.apply:
        items, _ = scan(apply=False)
    structure = validate_structure()
    hits = legacy_semantic_hits()
    report = render_report(items, applied, structure, hits)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(report, encoding="utf-8")

    anomalies = sum(bool(i.errors or i.unknown) for i in items)
    failures = len(structure["error"])
    print(
        f"works={len(items)} applied={applied} anomalies={anomalies} "
        f"structure_failures={failures} report={args.report}"
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
