# -*- coding: utf-8 -*-
"""Second-stage namespace and physical-layout migration for world literature.

Canonical target:

10 作品坐标系统/
  T 时间/  R 地域/  M 思潮与美学/  G 体裁/  TH 主题/  TY 类型与叙事机制/
20 作品知识网络/
  IM 意象/  CN 文化叙事/

Namespace mapping:
  QH -> TH
  QT -> TY
  QX -> IM
  QC -> CN

Work-field mapping:
  axis_qh -> axis_th
  axis_qt -> axis_ty
  axis_q  -> legacy_axis_q
  qx -> imagery
  qx_count -> imagery_count
  qc_relations -> cultural_narrative_relations

The migration does not invent, delete, merge, or expand taxonomy concepts. It only
moves/renames existing structures and rewrites references mechanically.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORLD = REPO / "个人通识知识系统_v2_A2" / "30 世界文学"
OLD_AXIS = WORLD / "10 轴"
OLD_NODES = WORLD / "20 节点"
COORD = WORLD / "10 作品坐标系统"
NETWORK = WORLD / "20 作品知识网络"
TOPICS = WORLD / "30 专题"
WORKS = WORLD / "40 作品"
ARCH = WORLD / "04 系统架构"
REPORT = ARCH / "06 命名空间与物理目录迁移审计.md"

CODE_MAP = (("QH", "TH"), ("QT", "TY"), ("QX", "IM"), ("QC", "CN"))
WORK_KEY_MAP = {
    "axis_qh": "axis_th",
    "axis_qt": "axis_ty",
    "axis_q": "legacy_axis_q",
    "qx": "imagery",
    "qx_count": "imagery_count",
    "qc_relations": "cultural_narrative_relations",
}

ENTRY_MOVES = {
    "T轴 世界文学时间史.md": ("T 时间", "00 T 时间入口.md"),
    "R轴 世界文学传统.md": ("R 地域", "00 R 地域入口.md"),
    "M轴 文学思潮与美学范式.md": ("M 思潮与美学", "00 M 思潮与美学入口.md"),
    "G轴 体裁与类型.md": ("G 体裁", "00 G 体裁入口.md"),
}
NODE_DIR_MOVES = {
    OLD_NODES / "T 时间": COORD / "T 时间",
    OLD_NODES / "R 地域": COORD / "R 地域",
    OLD_NODES / "M 思潮": COORD / "M 思潮与美学",
    OLD_NODES / "G 类型": COORD / "G 体裁",
    OLD_NODES / "Q 主题" / "QH 主题": COORD / "TH 主题",
    OLD_NODES / "Q 主题" / "QT 类型": COORD / "TY 类型与叙事机制",
    OLD_NODES / "Q 主题" / "QX 意象": NETWORK / "IM 意象",
    OLD_NODES / "Q 主题" / "QC 母题": NETWORK / "CN 文化叙事",
}
TEXT_SUFFIXES = {".md", ".base", ".canvas"}
TOP_KEY = re.compile(r"^([A-Za-z0-9_]+):(?:\s|$)")


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5 :]


def transform_codes(text: str) -> str:
    # Long field names first.
    text = text.replace("qc_relations", "cultural_narrative_relations")
    text = text.replace("qx_count", "imagery_count")
    text = text.replace("axis_qh", "axis_th")
    text = text.replace("axis_qt", "axis_ty")
    text = re.sub(r"\bqx_", "im_", text)
    text = re.sub(r"\bqc_", "cn_", text)
    for old, new in CODE_MAP:
        text = text.replace(old, new)
    return text


def transform_name(name: str) -> str:
    out = name
    for old, new in CODE_MAP:
        out = out.replace(old, new)
    return out


def top_blocks(lines: list[str]):
    starts: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        m = TOP_KEY.match(line)
        if m and not line.startswith((" ", "\t")):
            starts.append((i, m.group(1)))
    blocks: list[tuple[int, int, str]] = []
    for pos, (start, key) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        blocks.append((start, end, key))
    return blocks


def scalar_value(lines: list[str], key: str):
    for start, end, k in top_blocks(lines):
        if k != key:
            continue
        raw = lines[start].split(":", 1)[1].strip().strip('"\'')
        return raw or None
    return None


def rewrite_work(text: str) -> tuple[str, bool]:
    fm, body = split_frontmatter(text)
    if fm is None:
        return transform_codes(text), False
    lines = fm.splitlines()
    blocks = top_blocks(lines)
    if scalar_value(lines, "type") != "work":
        return transform_codes(text), False

    out: list[str] = []
    for start, end, key in blocks:
        block = lines[start:end]
        new_key = WORK_KEY_MAP.get(key, key)
        first = block[0]
        if key in WORK_KEY_MAP:
            first = new_key + ":" + first.split(":", 1)[1]
        new_block = [first] + block[1:]
        # Preserve the historical combined Q values exactly as an audit trail.
        if new_key != "legacy_axis_q":
            new_block = [transform_codes(line) for line in new_block]
        out.extend(new_block)

    new_body = transform_codes(body)
    new_text = "---\n" + "\n".join(out) + "\n---\n" + new_body
    return new_text, True


def set_or_add_scalar(lines: list[str], key: str, value: str, after: str | None = None):
    for start, end, k in top_blocks(lines):
        if k == key:
            lines[start] = f"{key}: {value}"
            return lines
    insert_at = len(lines)
    if after:
        for start, end, k in top_blocks(lines):
            if k == after:
                insert_at = end
                break
    lines[insert_at:insert_at] = [f"{key}: {value}"]
    return lines


def rewrite_namespace_node(text: str, namespace: str) -> str:
    fm, body = split_frontmatter(text)
    if fm is None:
        return transform_codes(text)
    original = fm.splitlines()
    old_code = scalar_value(original, "code")
    old_id = scalar_value(original, "id")
    existing_legacy_code = scalar_value(original, "legacy_code")

    # Protect pre-existing older legacy_code semantics while canonical text is renamed.
    protected: list[str] = []
    for line in original:
        if line.startswith("legacy_code:"):
            protected.append(line)
        else:
            protected.append(transform_codes(line))

    lines = protected
    # Remove old axis: Q for network namespaces; coordinate namespaces get their own axis.
    rebuilt: list[str] = []
    for line in lines:
        if line.startswith("axis: Q"):
            if namespace in {"TH", "TY"}:
                rebuilt.append(f"axis: {namespace}")
            else:
                rebuilt.append(f"namespace: {namespace}")
                rebuilt.append("legacy_axis: Q")
        else:
            rebuilt.append(line)
    lines = rebuilt

    if old_code and old_code.startswith(tuple(x[0] for x in CODE_MAP)):
        if existing_legacy_code and existing_legacy_code != old_code:
            # Preserve both generations without overwriting the older migration provenance.
            lines = [line for line in lines if not line.startswith("legacy_code:")]
            insert = 0
            for i, line in enumerate(lines):
                if line.startswith("code:"):
                    insert = i + 1
                    break
            lines[insert:insert] = ["legacy_codes:", f"- {old_code}", f"- {existing_legacy_code}"]
        elif not existing_legacy_code:
            lines = set_or_add_scalar(lines, "legacy_code", old_code, after="code")
    if old_id and any(old in old_id for old, _ in CODE_MAP):
        lines = set_or_add_scalar(lines, "legacy_id", old_id, after="id")

    return "---\n" + "\n".join(lines) + "\n---\n" + transform_codes(body)


def move_tree(src: Path, dst: Path, apply: bool, moves: list[tuple[str, str]]):
    if not src.exists():
        return
    for path in sorted(src.rglob("*"), key=lambda p: len(p.parts)):
        if path.is_dir():
            continue
        rel = path.relative_to(src)
        target = dst / rel
        moves.append((path.relative_to(WORLD).as_posix(), target.relative_to(WORLD).as_posix()))
        if apply:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise RuntimeError(f"destination already exists: {target}")
            shutil.move(str(path), str(target))
    if apply and src.exists():
        shutil.rmtree(src)


def rename_coded_paths(root: Path, apply: bool, moves: list[tuple[str, str]]):
    if not root.exists():
        return
    paths = sorted(root.rglob("*"), key=lambda p: len(p.parts), reverse=True)
    for path in paths:
        new_name = transform_name(path.name)
        if new_name == path.name:
            continue
        target = path.with_name(new_name)
        moves.append((path.relative_to(WORLD).as_posix(), target.relative_to(WORLD).as_posix()))
        if apply:
            if target.exists():
                raise RuntimeError(f"rename collision: {target}")
            path.rename(target)


def remove_empty_legacy_dirs(apply: bool):
    if not apply:
        return
    for root in (OLD_NODES, OLD_AXIS):
        if root.exists():
            for d in sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
                try:
                    d.rmdir()
                except OSError:
                    pass
            try:
                root.rmdir()
            except OSError:
                pass


def classify_namespace_path(path: Path) -> str | None:
    try:
        rel = path.relative_to(WORLD)
    except ValueError:
        return None
    s = rel.as_posix()
    if s.startswith("10 作品坐标系统/TH 主题/"):
        return "TH"
    if s.startswith("10 作品坐标系统/TY 类型与叙事机制/"):
        return "TY"
    if s.startswith("20 作品知识网络/IM 意象/"):
        return "IM"
    if s.startswith("20 作品知识网络/CN 文化叙事/"):
        return "CN"
    return None


def rewrite_world_texts(apply: bool, changed: list[str]):
    for path in sorted(WORLD.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        if path.parent == WORKS and path.suffix == ".md":
            new, _ = rewrite_work(text)
        else:
            ns = classify_namespace_path(path)
            new = rewrite_namespace_node(text, ns) if ns and path.suffix == ".md" else transform_codes(text)

        # Q nodes moved one directory shallower; their topic links need one fewer ../.
        ns = classify_namespace_path(path)
        if ns in {"TH", "TY", "IM", "CN"}:
            new = new.replace("../../../30 专题/", "../../30 专题/")

        # Canonical physical path references.
        path_replacements = {
            "10 轴/T轴 世界文学时间史.md": "10 作品坐标系统/T 时间/00 T 时间入口.md",
            "10 轴/R轴 世界文学传统.md": "10 作品坐标系统/R 地域/00 R 地域入口.md",
            "10 轴/M轴 文学思潮与美学范式.md": "10 作品坐标系统/M 思潮与美学/00 M 思潮与美学入口.md",
            "10 轴/G轴 体裁与类型.md": "10 作品坐标系统/G 体裁/00 G 体裁入口.md",
            "10 轴/Q轴 文学主题与人类问题.md": "04 系统架构/05 Q历史兼容说明.md",
            "20 节点/T 时间": "10 作品坐标系统/T 时间",
            "20 节点/R 地域": "10 作品坐标系统/R 地域",
            "20 节点/M 思潮": "10 作品坐标系统/M 思潮与美学",
            "20 节点/G 类型": "10 作品坐标系统/G 体裁",
            "20 节点/Q 主题/QH 主题": "10 作品坐标系统/TH 主题",
            "20 节点/Q 主题/QT 类型": "10 作品坐标系统/TY 类型与叙事机制",
            "20 节点/Q 主题/QX 意象": "20 作品知识网络/IM 意象",
            "20 节点/Q 主题/QC 母题": "20 作品知识网络/CN 文化叙事",
        }
        for old, target in path_replacements.items():
            new = new.replace(old, transform_codes(target))

        if new != text:
            changed.append(path.relative_to(REPO).as_posix())
            if apply:
                path.write_text(new, encoding="utf-8")


def write_system_readmes(apply: bool):
    files = {
        COORD / "00 作品坐标系统.md": """# 作品坐标系统\n\n本目录是作品的 canonical 定位系统。\n\n- T：时间\n- R：地域\n- M：思潮与美学\n- G：体裁\n- TH：主题（原 QH）\n- TY：类型／叙事机制（原 QT）\n\nTH/TY 与 T/R/M/G 同属作品坐标；不再视为 Q 的子轴。\n""",
        NETWORK / "00 作品知识网络.md": """# 作品知识网络\n\n本目录承载稀疏、可抽取、可关系化的作品知识。\n\n- IM：意象（原 QX）\n- CN：文化叙事（原 QC）\n\nIM/CN 不是坐标轴，不要求每部作品覆盖。\n""",
    }
    if not apply:
        return
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(content, encoding="utf-8")


def migrate(apply: bool):
    moves: list[tuple[str, str]] = []
    changed: list[str] = []

    # Axis entry files.
    for filename, (subdir, newname) in ENTRY_MOVES.items():
        src = OLD_AXIS / filename
        dst = COORD / subdir / newname
        if src.exists():
            moves.append((src.relative_to(WORLD).as_posix(), dst.relative_to(WORLD).as_posix()))
            if apply:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dst))

    # Q-axis compatibility entry leaves the canonical coordinate tree.
    q_entry = OLD_AXIS / "Q轴 文学主题与人类问题.md"
    q_target = ARCH / "05 Q历史兼容说明.md"
    if q_entry.exists():
        moves.append((q_entry.relative_to(WORLD).as_posix(), q_target.relative_to(WORLD).as_posix()))
        if apply:
            q_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(q_entry), str(q_target))

    # Taxonomy directories.
    for src, dst in NODE_DIR_MOVES.items():
        move_tree(src, dst, apply, moves)

    if apply:
        remove_empty_legacy_dirs(True)

    # Rename code-bearing files/directories after they are in canonical locations.
    for root in (
        COORD / "TH 主题",
        COORD / "TY 类型与叙事机制",
        NETWORK / "IM 意象",
        NETWORK / "CN 文化叙事",
        TOPICS,
    ):
        rename_coded_paths(root, apply, moves)

    if apply:
        write_system_readmes(True)
        rewrite_world_texts(True, changed)

    return moves, changed


def collect_stats():
    stats = {
        "works": 0,
        "axis_th": 0,
        "axis_ty": 0,
        "imagery": 0,
        "cultural_narrative_relations": 0,
        "legacy_axis_q": 0,
        "old_fields": {"axis_qh": 0, "axis_qt": 0, "qx": 0, "qc_relations": 0},
    }
    if not WORKS.exists():
        return stats
    for path in WORKS.glob("*.md"):
        fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            continue
        lines = fm.splitlines()
        if scalar_value(lines, "type") != "work":
            continue
        stats["works"] += 1
        keys = {k for _, _, k in top_blocks(lines)}
        for key in ("axis_th", "axis_ty", "imagery", "cultural_narrative_relations", "legacy_axis_q"):
            if key in keys:
                stats[key] += 1
        for key in stats["old_fields"]:
            if key in keys:
                stats["old_fields"][key] += 1
    return stats


def audit_errors():
    errors: list[str] = []
    required_dirs = [
        COORD / "T 时间", COORD / "R 地域", COORD / "M 思潮与美学", COORD / "G 体裁",
        COORD / "TH 主题", COORD / "TY 类型与叙事机制",
        NETWORK / "IM 意象", NETWORK / "CN 文化叙事",
    ]
    for d in required_dirs:
        if not d.exists():
            errors.append(f"missing canonical directory: {d.relative_to(WORLD)}")
    for d in (OLD_AXIS, OLD_NODES):
        if d.exists():
            errors.append(f"legacy physical directory still exists: {d.relative_to(WORLD)}")

    # Old top-level topic namespaces should not remain as canonical topic paths.
    if TOPICS.exists():
        for p in TOPICS.iterdir():
            if any(p.name.startswith(old) for old, _ in CODE_MAP):
                errors.append(f"legacy topic namespace path remains: {p.relative_to(WORLD)}")

    stats = collect_stats()
    for key, count in stats["old_fields"].items():
        if count:
            errors.append(f"legacy work field remains as canonical key: {key} ({count})")
    return errors, stats


def write_report(moves, changed, errors, stats):
    lines = [
        "# 命名空间与物理目录迁移审计",
        "",
        "## 目标",
        "",
        "- 坐标：`T / R / M / G / TH / TY`",
        "- 知识网络：`IM / CN`",
        "- 物理目录：`10 作品坐标系统/` + `20 作品知识网络/`",
        "- legacy Q 仅保留为迁移 provenance，不再作为 canonical 目录或字段。",
        "",
        "## 作品字段",
        "",
        f"- type: work：**{stats['works']}**",
        f"- axis_th：**{stats['axis_th']}**",
        f"- axis_ty：**{stats['axis_ty']}**",
        f"- imagery：**{stats['imagery']}**",
        f"- cultural_narrative_relations：**{stats['cultural_narrative_relations']}**",
        f"- legacy_axis_q：**{stats['legacy_axis_q']}**",
        "",
        "## 旧 canonical 字段残留",
        "",
    ]
    for key, count in stats["old_fields"].items():
        lines.append(f"- {key}: **{count}**")
    lines.extend([
        "",
        "## 文件迁移",
        "",
        f"- 物理 move/rename 记录：**{len(moves)}**",
        f"- 内容重写文件：**{len(changed)}**",
        "",
        "## 结构错误",
        "",
        f"- errors: **{len(errors)}**",
    ])
    for error in errors:
        lines.append(f"- {error}")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report-only", action="store_true")
    args = parser.parse_args()

    if args.report_only:
        errors, stats = audit_errors()
        write_report([], [], errors, stats)
        print(f"namespace_v2_check errors={len(errors)} works={stats['works']}")
        return 1 if errors else 0

    moves, changed = migrate(args.apply)
    if args.apply:
        errors, stats = audit_errors()
        write_report(moves, changed, errors, stats)
        print(f"namespace_v2_apply moves={len(moves)} changed={len(changed)} errors={len(errors)} works={stats['works']}")
        return 1 if errors else 0

    print(f"namespace_v2_plan moves={len(moves)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
