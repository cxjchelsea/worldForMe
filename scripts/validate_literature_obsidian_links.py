# -*- coding: utf-8 -*-
"""Read-only validation for the world-literature Obsidian architecture.

Checks only structural references that can be resolved deterministically:
- every `.canvas` is valid JSON;
- every Canvas `file` node points to an existing repository file;
- every Canvas edge points to existing node ids;
- explicit path WikiLinks (`[[../...]]`, `[[30 专题/...]]`, etc.) point to an existing file;
- the work Base exposes canonical `qx` directly and does not require a duplicate `qx_count` fact.

Bare-name WikiLinks such as `[[某节点]]` are intentionally ignored because Obsidian resolves
those through vault-wide name lookup and aliases; validating them as filesystem paths would
create false positives.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORLD = REPO / "个人通识知识系统_v2_A2" / "30 世界文学"
WORK_BASE = WORLD / "40 作品" / "00 世界文学作品库.base"

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
WORLD_ROOT_PREFIXES = {
    "00 世界文学使用规则.md",
    "01 世界文学总地图.canvas",
    "02 专题入口.canvas",
    "03 世界文学节点.base",
    "04 系统架构",
    "10 轴",
    "20 节点",
    "30 专题",
    "40 作品",
    "50 作者",
    "60 奖项",
    "70 世界名著",
    "_source",
}


def candidate_paths(base: Path, raw_target: str) -> list[Path]:
    target = raw_target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target:
        return []
    target_path = Path(target)

    if target.startswith("../") or target.startswith("./"):
        root = base.parent
    elif target_path.parts and target_path.parts[0] in WORLD_ROOT_PREFIXES:
        root = WORLD
    else:
        # Only explicit path links are validated. Bare-name links are Obsidian-resolved.
        if "/" not in target and "\\" not in target:
            return []
        root = base.parent

    path = (root / target_path).resolve()
    candidates = [path]
    if path.suffix == "":
        candidates.extend([Path(str(path) + ext) for ext in (".md", ".canvas", ".base")])
    return candidates


def validate_wikilinks() -> list[str]:
    errors: list[str] = []
    for path in sorted(WORLD.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in WIKILINK_RE.finditer(text):
            raw = match.group(1)
            candidates = candidate_paths(path, raw)
            if not candidates:
                continue
            # Keep references inside the repository; an escaped path is always invalid here.
            if not all(REPO == c or REPO in c.parents for c in candidates):
                errors.append(f"WikiLink escapes repository: {path.relative_to(REPO)} -> [[{raw}]]")
                continue
            if not any(c.exists() for c in candidates):
                errors.append(f"Broken explicit WikiLink: {path.relative_to(REPO)} -> [[{raw}]]")
    return errors


def validate_canvases() -> list[str]:
    errors: list[str] = []
    for path in sorted(WORLD.rglob("*.canvas")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid Canvas JSON: {path.relative_to(REPO)} ({exc})")
            continue

        nodes = data.get("nodes", [])
        edges = data.get("edges", [])
        node_ids = {node.get("id") for node in nodes if node.get("id")}

        for node in nodes:
            if node.get("type") != "file":
                continue
            raw = node.get("file")
            if not raw:
                errors.append(f"Canvas file node missing path: {path.relative_to(REPO)} id={node.get('id')}")
                continue
            target = REPO / raw
            if not target.exists():
                errors.append(f"Broken Canvas file node: {path.relative_to(REPO)} id={node.get('id')} -> {raw}")

        for edge in edges:
            from_id = edge.get("fromNode")
            to_id = edge.get("toNode")
            if from_id not in node_ids:
                errors.append(f"Canvas edge missing fromNode: {path.relative_to(REPO)} id={edge.get('id')} -> {from_id}")
            if to_id not in node_ids:
                errors.append(f"Canvas edge missing toNode: {path.relative_to(REPO)} id={edge.get('id')} -> {to_id}")
    return errors


def validate_work_base() -> list[str]:
    errors: list[str] = []
    if not WORK_BASE.exists():
        return [f"Missing work Base: {WORK_BASE.relative_to(REPO)}"]
    text = WORK_BASE.read_text(encoding="utf-8")
    required = ("note.axis_qh:", "note.axis_qt:", "note.qx:", "note.qc_relations:")
    for marker in required:
        if marker not in text:
            errors.append(f"Work Base missing canonical field declaration: {marker}")
    if "note.qx_count:" in text or "- qx_count" in text:
        errors.append("Work Base still depends on duplicate qx_count instead of canonical qx")
    return errors


def main() -> int:
    errors = validate_canvases() + validate_wikilinks() + validate_work_base()
    if errors:
        print(f"literature_obisidian_validation=FAIL errors={len(errors)}")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("literature_obisidian_validation=PASS errors=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
