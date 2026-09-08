# -*- coding: utf-8 -*-
"""Migrate QH/QT/QX/QC node roles and the topic-entry Canvas to the new literature architecture.

This script is intentionally structural only:
- no taxonomy expansion;
- no node rename/move/delete;
- legacy `axis: Q` is preserved;
- QH/QT gain canonical `system_role: work_coordinate`;
- QX/QC gain canonical `system_role: work_knowledge_network`;
- old Q-path wording is changed only for explicit navigation breadcrumb lines;
- 02 专题入口.canvas is regrouped and stale file nodes whose topic packages do not exist are pruned.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORLD = REPO / "个人通识知识系统_v2_A2" / "30 世界文学"
QROOT = WORLD / "20 节点" / "Q 主题"
CANVAS = WORLD / "02 专题入口.canvas"
REPORT = WORLD / "04 系统架构" / "04 Q节点角色迁移审计.md"

ROLE_BY_DIR = {
    "QH 主题": ("QH", "work_coordinate", "作品坐标系统"),
    "QT 类型": ("QT", "work_coordinate", "作品坐标系统"),
    "QX 意象": ("QX", "work_knowledge_network", "作品知识网络"),
    "QC 母题": ("QC", "work_knowledge_network", "作品知识网络"),
}
TOP_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$")

# These ids are legacy topic-entry nodes. Their target topic packages are absent in the
# current repository. Removing them from the Canvas does NOT delete or rename QT taxonomy
# nodes under 20 节点; it only removes false navigation promises.
LEGACY_STALE_TOPIC_NODE_IDS = {
    "qt-myth",
    "qt8",
    "q15-wuxia",
    "q15-knight",
    "q15-samurai",
    "q15-swash",
    "q15-western",
    "q15-gaucho",
    "q15-outlaw",
    "q15-pirate",
}


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end], text[end + 5 :]


def top_key_index(lines: list[str], key: str):
    for i, line in enumerate(lines):
        m = TOP_KEY_RE.match(line)
        if m and m.group(1) == key:
            return i, (m.group(2) or "").strip()
    return None


def set_scalar(lines: list[str], key: str, value: str, after_keys=("type", "axis", "legacy_axis", "facet")):
    found = top_key_index(lines, key)
    newline = f"{key}: {value}"
    if found is not None:
        i, old = found
        if old == value:
            return lines, False, None
        return lines, False, f"{key} 已存在不同值 `{old}`，未覆盖"

    insert_at = 0
    for candidate in after_keys:
        item = top_key_index(lines, candidate)
        if item is not None:
            insert_at = max(insert_at, item[0] + 1)
    return lines[:insert_at] + [newline] + lines[insert_at:], True, None


def migrate_nodes(apply: bool):
    stats = {k: {"files": 0, "changed": 0, "conflicts": []} for k in ROLE_BY_DIR}
    for dirname, (facet, role, breadcrumb_root) in ROLE_BY_DIR.items():
        root = QROOT / dirname
        if not root.exists():
            stats[dirname]["conflicts"].append("目录不存在")
            continue
        for path in sorted(root.rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            fm, body = split_frontmatter(text)
            if fm is None:
                continue
            stats[dirname]["files"] += 1
            lines = fm.splitlines()
            lines2, inserted, conflict = set_scalar(lines, "system_role", role)
            if conflict:
                stats[dirname]["conflicts"].append(f"{path.relative_to(QROOT).as_posix()}: {conflict}")
                lines2 = lines

            # Only rewrite explicit breadcrumb prose; do not globally rewrite historical discussion.
            body2 = re.sub(
                r"(?m)^(>\s*路径：)Q轴(\s*→)",
                rf"\1{breadcrumb_root}\2",
                body,
            )
            new_text = "---\n" + "\n".join(lines2) + "\n---\n" + body2
            changed = new_text != text
            if apply and changed:
                path.write_text(new_text, encoding="utf-8")
            if changed:
                stats[dirname]["changed"] += 1
    return stats


def ensure_canvas_node(nodes, node):
    for i, old in enumerate(nodes):
        if old.get("id") == node["id"]:
            if old != node:
                nodes[i] = node
                return True
            return False
    nodes.append(node)
    return True


def ensure_canvas_edge(edges, edge):
    for i, old in enumerate(edges):
        if old.get("id") == edge["id"]:
            if old != edge:
                edges[i] = edge
                return True
            return False
    edges.append(edge)
    return True


def prune_stale_topic_nodes(nodes, edges):
    stale_present = {node.get("id") for node in nodes if node.get("id") in LEGACY_STALE_TOPIC_NODE_IDS}
    if not stale_present:
        return False
    nodes[:] = [node for node in nodes if node.get("id") not in stale_present]
    edges[:] = [
        edge
        for edge in edges
        if edge.get("fromNode") not in stale_present and edge.get("toNode") not in stale_present
    ]
    return True


def migrate_canvas(apply: bool):
    data = json.loads(CANVAS.read_text(encoding="utf-8"))
    nodes = data.setdefault("nodes", [])
    edges = data.setdefault("edges", [])
    changed = False

    # The old Canvas advertised QT9/QT8 topic packages which are not present in the
    # repository. Keep taxonomy nodes and compatibility codes, but remove broken topic links.
    changed |= prune_stale_topic_nodes(nodes, edges)

    for node in nodes:
        if node.get("id") == "g-q":
            if node.get("label") != "作品坐标专题 · QH / QT":
                node["label"] = "作品坐标专题 · QH / QT"
                changed = True
        if node.get("id") == "axis-q":
            target = "个人通识知识系统_v2_A2/30 世界文学/04 系统架构/01 作品坐标系统.md"
            if node.get("file") != target:
                node["file"] = target
                changed = True

    network_nodes = [
        {"id":"g-knowledge-network","type":"group","x":2940,"y":720,"width":940,"height":430,"label":"作品知识网络 · QX / QC","color":"5"},
        {"id":"knowledge-network","type":"file","x":3190,"y":790,"width":440,"height":110,"file":"个人通识知识系统_v2_A2/30 世界文学/04 系统架构/02 作品知识网络.md","color":"5"},
        {"id":"qx-network","type":"file","x":2960,"y":960,"width":440,"height":100,"file":"个人通识知识系统_v2_A2/30 世界文学/20 节点/Q 主题/QX 意象/QX 文学意象与场景.md","color":"5"},
        {"id":"qc-network","type":"file","x":3420,"y":960,"width":440,"height":100,"file":"个人通识知识系统_v2_A2/30 世界文学/20 节点/Q 主题/QC 母题/QC 母题与叙事组件.md","color":"5"},
    ]
    for node in network_nodes:
        changed |= ensure_canvas_node(nodes, node)

    network_edges = [
        {"id":"e-overview-knowledge-network","fromNode":"overview","fromSide":"bottom","toNode":"knowledge-network","toSide":"top"},
        {"id":"e-knowledge-network-qx","fromNode":"knowledge-network","fromSide":"bottom","toNode":"qx-network","toSide":"top"},
        {"id":"e-knowledge-network-qc","fromNode":"knowledge-network","fromSide":"bottom","toNode":"qc-network","toSide":"top"},
    ]
    for edge in network_edges:
        changed |= ensure_canvas_edge(edges, edge)

    if apply and changed:
        CANVAS.write_text(json.dumps(data, ensure_ascii=False, indent="\t") + "\n", encoding="utf-8")
        json.loads(CANVAS.read_text(encoding="utf-8"))
    return changed


def render_report(stats, canvas_changed):
    total = sum(v["files"] for v in stats.values())
    changed = sum(v["changed"] for v in stats.values())
    conflicts = [c for v in stats.values() for c in v["conflicts"]]
    lines = [
        "---",
        "id: WL-ARCH-Q-NODE-ROLE-AUDIT",
        "type: literature_governance",
        "scope: q_node_role_migration",
        "status: ACTIVE",
        "generated_by: scripts/migrate_literature_q_node_roles.py",
        "---",
        "# Q 节点角色迁移审计",
        "",
        "> 本迁移只增加 canonical 系统角色并调整专题入口导航，不移动、删除或重编号任何 QH/QT/QX/QC 节点。旧 `axis: Q` 可继续作为兼容元数据存在。",
        "",
        f"- 扫描节点文件：**{total}**",
        f"- 需要/完成角色或 breadcrumb 更新：**{changed}**",
        f"- metadata 冲突：**{len(conflicts)}**",
        f"- `02 专题入口.canvas` 结构调整：**{'是' if canvas_changed else '否（已是目标状态）'}**",
        "",
        "## 分域结果",
        "",
    ]
    for dirname, (facet, role, _) in ROLE_BY_DIR.items():
        item = stats[dirname]
        lines.append(f"- **{facet}**：{item['files']} 文件；目标 `system_role: {role}`；本次变更 {item['changed']}。")
    lines += ["", "## 冲突", ""]
    if conflicts:
        lines.extend(f"- `{c}`" for c in conflicts)
    else:
        lines.append("无。")
    lines += [
        "",
        "## Canvas 目标结构",
        "",
        "- 原 `Q · 内容域` 组改为 `作品坐标专题 · QH / QT`；",
        "- 原 `axis-q` 节点保留 id 以兼容边关系，但入口改指向 `04 系统架构/01 作品坐标系统.md`；",
        "- 新增 `作品知识网络 · QX / QC` 组，分别进入 QX 与 QC 现有节点；",
        "- QT8 taxonomy 与兼容代码继续保留；Canvas 中指向不存在的 QT9/QT8 专题包的旧 file node 与相关边已移除。",
        "",
    ]
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    stats = migrate_nodes(apply=args.apply)
    canvas_changed = migrate_canvas(apply=args.apply)
    report = render_report(stats, canvas_changed)
    if args.apply:
        REPORT.write_text(report, encoding="utf-8")
    conflicts = sum(len(v["conflicts"]) for v in stats.values())
    print(f"nodes={sum(v['files'] for v in stats.values())} conflicts={conflicts} canvas_changed={canvas_changed}")
    return 1 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
