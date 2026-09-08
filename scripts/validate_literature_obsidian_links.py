# -*- coding: utf-8 -*-
"""Read-only validation for world-literature namespace v2.

Canonical architecture:
- coordinate system: T / R / M / G / TH / TY
- knowledge network: IM / CN
- physical roots: 10 作品坐标系统 / 20 作品知识网络

This gate validates architecture-governed paths and fields. It is not a whole-vault
broken-link auditor for unrelated historical notes.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORLD = REPO / "个人通识知识系统_v2_A2" / "30 世界文学"
COORD = WORLD / "10 作品坐标系统"
NETWORK = WORLD / "20 作品知识网络"
WORKS = WORLD / "40 作品"
WORK_BASE = WORKS / "00 世界文学作品库.base"
NODE_BASE = WORLD / "03 世界文学节点.base"

CANVASES = (WORLD / "01 世界文学总地图.canvas", WORLD / "02 专题入口.canvas")
REQUIRED_DIRS = (
    COORD / "T 时间",
    COORD / "R 地域",
    COORD / "M 思潮与美学",
    COORD / "G 体裁",
    COORD / "TH 主题",
    COORD / "TY 类型与叙事机制",
    NETWORK / "IM 意象",
    NETWORK / "CN 文化叙事",
)
LEGACY_DIRS = (WORLD / "10 轴", WORLD / "20 节点")

WIKILINK_SCOPE_FILES = (
    WORLD / "00 世界文学使用规则.md",
    WORKS / "01 作品字段规范.md",
)
WIKILINK_SCOPE_DIRS = (
    WORLD / "04 系统架构",
    COORD,
    NETWORK,
)

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
FENCED_CODE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
KNOWN_FILE_SUFFIXES = {".md", ".canvas", ".base"}
WORLD_ROOT_PREFIXES = {
    "00 世界文学使用规则.md",
    "01 世界文学总地图.canvas",
    "02 专题入口.canvas",
    "03 世界文学节点.base",
    "04 系统架构",
    "10 作品坐标系统",
    "20 作品知识网络",
    "30 专题",
    "40 作品",
    "50 作者",
    "60 奖项",
    "70 世界名著",
    "_source",
}
TOP_KEY_RE = re.compile(r"^([A-Za-z0-9_]+):(?:\s|$)")


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5 :]


def top_keys(fm: str) -> set[str]:
    keys = set()
    for line in fm.splitlines():
        if line.startswith((" ", "\t")):
            continue
        m = TOP_KEY_RE.match(line)
        if m:
            keys.add(m.group(1))
    return keys


def top_scalar(fm: str, key: str):
    for line in fm.splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip().strip('"\'')
    return None


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
        if "/" not in target and "\\" not in target:
            return []
        root = base.parent
    path = (root / target_path).resolve()
    candidates = [path]
    if path.suffix.lower() not in KNOWN_FILE_SUFFIXES:
        candidates.extend(Path(str(path) + ext) for ext in (".md", ".canvas", ".base"))
    return candidates


def strip_markdown_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub("", text))


def iter_wikilink_scope() -> list[Path]:
    paths: set[Path] = set()
    for path in WIKILINK_SCOPE_FILES:
        if path.exists():
            paths.add(path)
    for directory in WIKILINK_SCOPE_DIRS:
        if directory.exists():
            paths.update(directory.rglob("*.md"))
    return sorted(paths)


def validate_physical_architecture() -> list[str]:
    errors = []
    for path in REQUIRED_DIRS:
        if not path.exists():
            errors.append(f"Missing canonical directory: {path.relative_to(REPO)}")
    for path in LEGACY_DIRS:
        if path.exists():
            errors.append(f"Legacy physical directory still exists: {path.relative_to(REPO)}")
    return errors


def validate_works() -> list[str]:
    errors = []
    old_fields = {"axis_q", "axis_qh", "axis_qt", "qx", "qc_relations"}
    count = 0
    for path in WORKS.glob("*.md"):
        fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None or top_scalar(fm, "type") != "work":
            continue
        count += 1
        keys = top_keys(fm)
        bad = sorted(keys & old_fields)
        if bad:
            errors.append(f"Work uses retired canonical fields: {path.relative_to(REPO)} -> {bad}")
            if len(errors) >= 30:
                break
    if count != 4062:
        errors.append(f"Work count changed unexpectedly: expected 4062, got {count}")
    return errors


def validate_namespace_nodes() -> list[str]:
    errors = []
    specs = (
        (COORD / "TH 主题", "TH", "axis: TH"),
        (COORD / "TY 类型与叙事机制", "TY", "axis: TY"),
        (NETWORK / "IM 意象", "IM", "namespace: IM"),
        (NETWORK / "CN 文化叙事", "CN", "namespace: CN"),
    )
    for root, prefix, marker in specs:
        for path in root.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            fm, _ = split_frontmatter(text)
            if fm is None:
                continue
            code = top_scalar(fm, "code")
            if code and not code.startswith(prefix):
                errors.append(f"Namespace/code mismatch: {path.relative_to(REPO)} code={code}")
            if code and marker not in fm:
                errors.append(f"Namespace metadata missing {marker}: {path.relative_to(REPO)}")
            if "axis: Q" in fm:
                errors.append(f"Canonical node still uses axis Q: {path.relative_to(REPO)}")
    return errors


def validate_canvases() -> list[str]:
    errors = []
    for path in CANVASES:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid Canvas JSON: {path.relative_to(REPO)} ({exc})")
            continue
        nodes = data.get("nodes", [])
        node_ids = {node.get("id") for node in nodes if node.get("id")}
        for node in nodes:
            if node.get("type") == "file":
                raw = node.get("file")
                if not raw or not (REPO / raw).exists():
                    errors.append(f"Broken Canvas file node: {path.relative_to(REPO)} id={node.get('id')} -> {raw}")
        for edge in data.get("edges", []):
            if edge.get("fromNode") not in node_ids:
                errors.append(f"Canvas edge missing fromNode: {path.relative_to(REPO)} id={edge.get('id')}")
            if edge.get("toNode") not in node_ids:
                errors.append(f"Canvas edge missing toNode: {path.relative_to(REPO)} id={edge.get('id')}")
    return errors


def validate_wikilinks() -> list[str]:
    errors = []
    for path in iter_wikilink_scope():
        text = strip_markdown_code(path.read_text(encoding="utf-8"))
        for match in WIKILINK_RE.finditer(text):
            raw = match.group(1)
            candidates = candidate_paths(path, raw)
            if not candidates:
                continue
            if not all(REPO == c or REPO in c.parents for c in candidates):
                errors.append(f"WikiLink escapes repository: {path.relative_to(REPO)} -> [[{raw}]]")
            elif not any(c.exists() for c in candidates):
                errors.append(f"Broken explicit WikiLink: {path.relative_to(REPO)} -> [[{raw}]]")
    return errors


def validate_bases() -> list[str]:
    errors = []
    if not WORK_BASE.exists():
        return [f"Missing work Base: {WORK_BASE.relative_to(REPO)}"]
    text = WORK_BASE.read_text(encoding="utf-8")
    required = (
        "note.axis_th:",
        "note.axis_ty:",
        "note.imagery:",
        "note.cultural_narrative_relations:",
        "note.legacy_axis_q:",
    )
    for marker in required:
        if marker not in text:
            errors.append(f"Work Base missing canonical field declaration: {marker}")
    retired = ("note.axis_qh:", "note.axis_qt:", "note.axis_q:", "note.qx:", "note.qc_relations:")
    for marker in retired:
        if marker in text:
            errors.append(f"Work Base still exposes retired field: {marker}")
    if not NODE_BASE.exists():
        errors.append(f"Missing node Base: {NODE_BASE.relative_to(REPO)}")
    else:
        node_text = NODE_BASE.read_text(encoding="utf-8")
        for code in ("TH", "TY", "IM", "CN"):
            if f'code.startsWith("{code}")' not in node_text:
                errors.append(f"Node Base missing namespace projection: {code}")
    return errors


def validate_topic_namespace_paths() -> list[str]:
    errors = []
    topic_root = WORLD / "30 专题"
    if not topic_root.exists():
        return errors
    for path in topic_root.iterdir():
        if path.name.startswith(("QH", "QT", "QX", "QC")):
            errors.append(f"Legacy topic namespace path remains: {path.relative_to(REPO)}")
    return errors


def main() -> int:
    errors = []
    errors += validate_physical_architecture()
    errors += validate_works()
    errors += validate_namespace_nodes()
    errors += validate_canvases()
    errors += validate_wikilinks()
    errors += validate_bases()
    errors += validate_topic_namespace_paths()
    if errors:
        print(f"literature_namespace_v2_validation=FAIL errors={len(errors)}")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("literature_namespace_v2_validation=PASS errors=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
