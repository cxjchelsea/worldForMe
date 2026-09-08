# -*- coding: utf-8 -*-
"""Repair deterministic navigation leftovers after namespace-v2 physical moves.

This script does not change taxonomy semantics. It only normalizes metadata and
filesystem-relative navigation after T/R/M/G/TH/TY/IM/CN were moved.
"""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORLD = REPO / "个人通识知识系统_v2_A2" / "30 世界文学"
COORD = WORLD / "10 作品坐标系统"
NETWORK = WORLD / "20 作品知识网络"

PATH_REPLACEMENTS = {
    "10 轴/T轴 世界文学时间史": "10 作品坐标系统/T 时间/00 T 时间入口",
    "10 轴/R轴 世界文学传统": "10 作品坐标系统/R 地域/00 R 地域入口",
    "10 轴/M轴 文学思潮与美学范式": "10 作品坐标系统/M 思潮与美学/00 M 思潮与美学入口",
    "10 轴/G轴 体裁与类型": "10 作品坐标系统/G 体裁/00 G 体裁入口",
    "10 轴/Q轴 文学主题与人类问题": "04 系统架构/05 Q历史兼容说明",
    "20 节点/Q 主题/TH 主题": "10 作品坐标系统/TH 主题",
    "20 节点/Q 主题/TY 类型": "10 作品坐标系统/TY 类型与叙事机制",
    "20 节点/Q 主题/IM 意象": "20 作品知识网络/IM 意象",
    "20 节点/Q 主题/CN 母题": "20 作品知识网络/CN 文化叙事",
    "20 节点/Q 主题/QH 主题": "10 作品坐标系统/TH 主题",
    "20 节点/Q 主题/QT 类型": "10 作品坐标系统/TY 类型与叙事机制",
    "20 节点/Q 主题/QX 意象": "20 作品知识网络/IM 意象",
    "20 节点/Q 主题/QC 母题": "20 作品知识网络/CN 文化叙事",
    "20 节点/T 时间": "10 作品坐标系统/T 时间",
    "20 节点/R 地域": "10 作品坐标系统/R 地域",
    "20 节点/M 思潮": "10 作品坐标系统/M 思潮与美学",
    "20 节点/G 类型": "10 作品坐标系统/G 体裁",
}

ENTRY_DIRS = {
    COORD / "T 时间": "T 时间",
    COORD / "R 地域": "R 地域",
    COORD / "M 思潮与美学": "M 思潮与美学",
    COORD / "G 体裁": "G 体裁",
}


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5 :]


def normalize_network_metadata(path: Path, namespace: str, text: str) -> str:
    fm, body = split_frontmatter(text)
    if fm is None:
        return text
    lines = fm.splitlines()
    out = []
    has_namespace = any(line.startswith("namespace:") for line in lines)
    has_legacy_axis = any(line.startswith("legacy_axis:") for line in lines)
    for line in lines:
        if line.startswith("axis: Q"):
            if not has_namespace:
                out.append(f"namespace: {namespace}")
                has_namespace = True
            if not has_legacy_axis:
                out.append("legacy_axis: Q")
                has_legacy_axis = True
            continue
        if namespace == "IM" and line.startswith("work_field: qx"):
            out.append("work_field: imagery")
            continue
        out.append(line)
    return "---\n" + "\n".join(out) + "\n---\n" + body


def repair_text(path: Path, text: str) -> str:
    new = text
    for old, target in PATH_REPLACEMENTS.items():
        new = new.replace(old, target)

    # T/R/M/G entry documents were moved together with their child nodes.
    for directory, label in ENTRY_DIRS.items():
        if path.parent == directory and path.name.startswith("00 "):
            new = new.replace(f"[[../10 作品坐标系统/{label}/", "[[")
            new = new.replace("[[../00 世界文学使用规则", "[[../../00 世界文学使用规则")

    # Nodes inside coordinate subdirectories: ../../ from a node reaches WORLD.
    # Old-axis back links become correct after the global old->new replacement above.

    # TH/TY root entry documents were formerly one directory deeper.
    if path in {
        COORD / "TH 主题" / "TH 主题与人类问题.md",
        COORD / "TY 类型与叙事机制" / "TY 类型与叙事传统.md",
    }:
        new = new.replace("[[../../../04 系统架构/", "[[../../04 系统架构/")
        new = new.replace("[[../../../00 世界文学使用规则", "[[../../00 世界文学使用规则")

    # TY8 cross-system links now point from coordinate tree to CN network tree.
    if path == COORD / "TY 类型与叙事机制" / "TY8 世界文化母题、原型与叙事传统.md":
        new = new.replace("[[../CN 母题/CN1 世界文化叙事传统", "[[../../20 作品知识网络/CN 文化叙事/CN1 世界文化叙事传统")
        new = new.replace("[[../CN 母题/CN2 世界文化母题、原型与叙事结构", "[[../../20 作品知识网络/CN 文化叙事/CN2 世界文化母题、原型与叙事结构")

    # Knowledge-network roots were formerly one directory deeper.
    if path in {
        NETWORK / "IM 意象" / "IM 文学意象与场景.md",
        NETWORK / "CN 文化叙事" / "CN 母题与叙事组件.md",
    }:
        new = new.replace("[[../../../04 系统架构/", "[[../../04 系统架构/")
        new = new.replace("[[../../../10 作品坐标系统/", "[[../../10 作品坐标系统/")
        new = new.replace("[[../../../04 系统架构/05 Q历史兼容说明", "[[../../04 系统架构/05 Q历史兼容说明")

    # Network metadata is canonical namespace, never an axis.
    try:
        rel = path.relative_to(NETWORK)
        first = rel.parts[0] if rel.parts else ""
        if first == "IM 意象":
            new = normalize_network_metadata(path, "IM", new)
        elif first == "CN 文化叙事":
            new = normalize_network_metadata(path, "CN", new)
    except ValueError:
        pass

    return new


def repair_canvases() -> int:
    changed = 0
    for path in (WORLD / "01 世界文学总地图.canvas", WORLD / "02 专题入口.canvas"):
        data = json.loads(path.read_text(encoding="utf-8"))
        touched = False
        for node in data.get("nodes", []):
            raw = node.get("file")
            if not isinstance(raw, str):
                continue
            fixed = raw
            for old, target in PATH_REPLACEMENTS.items():
                fixed = fixed.replace(old, target)
            if fixed != raw:
                node["file"] = fixed
                touched = True
        if touched:
            path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
            changed += 1
    return changed


def main() -> int:
    changed = 0
    for path in sorted(WORLD.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        new = repair_text(path, text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    changed += repair_canvases()
    print(f"namespace_v2_navigation_repair changed={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
