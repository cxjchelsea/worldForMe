# -*- coding: utf-8 -*-
"""Render QX human-readable views from work-level YAML.

Source of truth: 40 作品/*.md frontmatter `qx`.
Generated outputs:
1. Each work page gets a readable `## 文学意象` block.
2. 04 意象关系索引 becomes an imagery -> works navigation page.
3. 05 作品意象一览 becomes a works -> imagery navigation page.

Do not manually maintain generated blocks; edit only the work-level `qx` YAML.
"""

import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
WORLD = REPO / "个人通识知识系统_v2_A2" / "30 世界文学"
ROOT = WORLD / "40 作品"
QX_DIR = WORLD / "30 专题" / "QX 文学意象与场景"
TOPIC_DIR = QX_DIR / "10 已激活专题"
OUT = QX_DIR / "04 意象关系索引.md"
OUT_WORKS = QX_DIR / "05 作品意象一览.md"

START = "<!-- QX:GENERATED:START -->"
END = "<!-- QX:GENERATED:END -->"

GROUPS = [
    ("QX1", "自然与天气"),
    ("QX2", "天体与天空"),
    ("QX3", "水域与液体"),
    ("QX4", "植物与生长"),
    ("QX5", "动物"),
    ("QX6", "自然空间"),
    ("QX7", "建筑与室内空间"),
    ("QX8", "城市与现代性场景"),
    ("QX9", "身体与身体部位"),
    ("QX10", "色彩"),
    ("QX11", "光影与视觉"),
    ("QX12", "火、热与毁灭"),
    ("QX13", "饮食与宴饮"),
    ("QX14", "服饰与身体装饰"),
    ("QX15", "器物与日常物件"),
    ("QX16", "书写、知识与媒介"),
    ("QX17", "道路、交通与旅行场景"),
    ("QX18", "死亡与纪念空间"),
    ("QX19", "超自然与阈限场景"),
    ("QX20", "社会仪式与公共场景"),
]
GROUP_LABEL = dict(GROUPS)
SAL_RANK = {"dominant": 0, "core": 1, "significant": 2, "minor": 3}
SAL_ZH = {"dominant": "主导", "core": "核心", "significant": "显著", "minor": "次要"}


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[4:end], text[end + 4 :].lstrip("\n")


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", fm, re.M)
    if not m:
        return ""
    return m.group(1).strip().strip("'\"")


def extract_qx_yaml(fm: str) -> list:
    m = re.search(r"^qx:\s*$", fm, re.M)
    if not m:
        return []
    rest = fm[m.end() :]
    nxt = re.search(r"^[A-Za-z_][A-Za-z0-9_]*:", rest, re.M)
    block = rest[: nxt.start()] if nxt else rest
    try:
        data = yaml.safe_load("qx:\n" + block)
    except Exception:
        return []
    items = (data or {}).get("qx") or []
    if not isinstance(items, list):
        return []
    return [
        item
        for item in items
        if isinstance(item, dict)
        and item.get("object")
        and item.get("admission_status") != "candidate"
    ]


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def md_cell(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ")


def discover_leaf_topics():
    topics = {}
    if not TOPIC_DIR.exists():
        return topics
    for d in TOPIC_DIR.iterdir():
        if not d.is_dir():
            continue
        m = re.match(r"^(QX\d+\.\d+)\s+(.+)$", d.name)
        if not m:
            continue
        qid, label = m.groups()
        pages = sorted(d.glob("00 *.md"))
        if not pages:
            continue
        topics[qid] = {
            "label": label,
            "path": pages[0],
            "dir": d,
        }
    return topics


LEAF = discover_leaf_topics()


def topic_link_from_work(qid):
    topic = LEAF.get(str(qid or ""))
    if not topic:
        return ""
    target = topic["path"].relative_to(WORLD).with_suffix("")
    return f"[[../{target.as_posix()}|{topic['label']}]]"


def topic_link_from_qx(qid):
    topic = LEAF.get(str(qid or ""))
    if not topic:
        return ""
    target = topic["path"].relative_to(QX_DIR).with_suffix("")
    return f"[[{target.as_posix()}|{topic['label']}]]"


def collect():
    rels = []
    works = {}
    for p in sorted(ROOT.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        if not fm:
            continue
        items = extract_qx_yaml(fm)
        if not items:
            continue
        title = scalar(fm, "title") or p.stem
        author = scalar(fm, "author")
        normalized = []
        for item in items:
            rel = {
                "file": p.stem,
                "path": p,
                "title": title,
                "author": author,
                "qx_id": item.get("qx_id"),
                "object": str(item.get("object") or "").strip(),
                "group": str(item.get("primary_group") or "").strip(),
                "salience": str(item.get("salience") or "").strip(),
                "manifestation": str(item.get("manifestation") or "").strip(),
                "function": as_list(item.get("function")),
                "evidence": as_list(item.get("evidence")),
            }
            rels.append(rel)
            normalized.append(rel)
        works[p.stem] = {"path": p, "title": title, "author": author, "rels": normalized}
    return works, rels


def render_work_block(rels):
    lines = [
        START,
        "## 文学意象",
        "",
        "> 本节由页首 `qx` YAML 自动生成。作品级意象事实只维护 YAML；这里用于日常阅读。",
        "",
    ]
    for r in sorted(rels, key=lambda x: (SAL_RANK.get(x["salience"], 9), x["object"])):
        lines += [f"### {r['object']}", ""]
        group_label = GROUP_LABEL.get(r["group"], "")
        group_text = f"{r['group']} {group_label}".strip()
        if group_text:
            lines.append(f"- **分类**：{group_text}")
        if r["salience"]:
            lines.append(f"- **强度**：{SAL_ZH.get(r['salience'], r['salience'])}（`{r['salience']}`）")
        if r["manifestation"]:
            lines.append(f"- **具体表现**：{r['manifestation']}")
        if r["function"]:
            lines.append(f"- **叙事功能**：{'；'.join(r['function'])}")
        leaf = topic_link_from_work(r["qx_id"])
        if leaf:
            lines.append(f"- **跨作品专题**：{leaf}")
        if r["evidence"]:
            lines += ["- **文本依据**："]
            for evidence in r["evidence"]:
                lines.append(f"  - {evidence}")
        lines.append("")
    lines += [END, ""]
    return "\n".join(lines)


def update_work_pages(works):
    changed = 0
    block_re = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    for work in works.values():
        p = work["path"]
        text = p.read_text(encoding="utf-8")
        block = render_work_block(work["rels"]).rstrip()
        if block_re.search(text):
            new_text = block_re.sub(block, text)
        else:
            new_text = text.rstrip() + "\n\n" + block + "\n"
        if new_text != text:
            p.write_text(new_text, encoding="utf-8")
            changed += 1
    return changed


def work_link(title: str) -> str:
    return f"[[../../40 作品/{title}|{title}]]"


def aggregate_objects(rels):
    by_group = defaultdict(lambda: defaultdict(list))
    for r in rels:
        by_group[r["group"]][r["object"]].append(r)
    return by_group


def top_functions(items, limit=4):
    c = Counter(f for r in items for f in r["function"])
    return [name for name, _ in c.most_common(limit)]


def best_salience(items):
    return min((r["salience"] for r in items if r["salience"]), key=lambda s: SAL_RANK.get(s, 9), default="")


def write_imagery_index(works, rels):
    by_group = aggregate_objects(rels)
    lines = [
        "---",
        "id: WL-TOPIC-QX-REL-INDEX",
        "topic_id: WL-TOPIC-QX",
        "type: derived_index",
        "name: QX 意象导航",
        "axis: Q",
        "facet: QX",
        "source_of_truth: work_qx_relations",
        "manual_edit: false",
        "status: ACTIVE",
        "---",
        "# 意象 → 作品",
        "",
        "> 从 `40 作品` 的正式 `qx` YAML 自动生成。这里用于**从意象进入作品**；具体证据请进入作品页，跨作品解释请进入已激活专题。",
        "",
        f"当前覆盖 **{len(works)} 部作品 / {len(rels)} 条正式关系**。",
        "",
        "## 已激活跨作品专题",
        "",
    ]
    if LEAF:
        for qid, topic in sorted(LEAF.items()):
            members = [r for r in rels if str(r["qx_id"] or "") == qid]
            works_text = "、".join(f"《{r['title']}》" for r in members)
            lines.append(f"- {topic_link_from_qx(qid)} · {len(members)} 条关系 · {works_text or '暂无关系'}")
    else:
        lines.append("暂无已激活专题。")

    lines += ["", "## 按一级分类浏览", ""]
    for code, name in GROUPS:
        rel_count = sum(len(v) for v in by_group.get(code, {}).values())
        work_count = len({r["file"] for values in by_group.get(code, {}).values() for r in values})
        lines.append(f"- [[#{code} {name}|{code} {name}]] · {rel_count} 条关系 · {work_count} 部作品")

    for code, name in GROUPS:
        objects = by_group.get(code, {})
        lines += ["", f"## {code} {name}", ""]
        if not objects:
            lines.append("当前没有正式关系。")
            continue
        lines += ["| 意象 | 作品数 | 作品 | 最高强度 | 常见功能 | 专题 |", "|---|---:|---|---|---|---|"]
        rows = []
        for obj, items in objects.items():
            titles = []
            seen = set()
            for r in sorted(items, key=lambda x: x["title"]):
                if r["title"] not in seen:
                    seen.add(r["title"])
                    titles.append(work_link(r["title"]))
            qids = [str(r["qx_id"]) for r in items if r["qx_id"] and str(r["qx_id"]) in LEAF]
            leaf = topic_link_from_qx(qids[0]) if qids else ""
            funcs = "；".join(top_functions(items))
            sal = best_salience(items)
            rows.append((len(titles), obj, titles, sal, funcs, leaf))
        rows.sort(key=lambda x: (-x[0], x[1]))
        for n, obj, titles, sal, funcs, leaf in rows:
            lines.append(
                f"| {md_cell(obj)} | {n} | {md_cell('；'.join(titles))} | {md_cell(sal)} | {md_cell(funcs)} | {leaf} |"
            )

    lines += ["", "## 返回", "", "- [[00 文学意象与场景]]", "- [[05 作品意象一览]]", ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")


def write_work_index(works, rels):
    lines = [
        "---",
        "id: WL-TOPIC-QX-WORK-INDEX",
        "topic_id: WL-TOPIC-QX",
        "type: derived_index",
        "name: QX 作品意象导航",
        "axis: Q",
        "facet: QX",
        "source_of_truth: work_qx_relations",
        "manual_edit: false",
        "status: ACTIVE",
        "---",
        "# 作品 → 意象",
        "",
        "> 从 `40 作品` 的正式 `qx` YAML 自动生成。这里用于**从作品进入意象**；点击作品名可查看完整的“文学意象”正文区和文本依据。",
        "",
        f"当前覆盖 **{len(works)} 部作品 / {len(rels)} 条正式关系**。",
        "",
        "| 作品 | 作者 | 意象数 | 主导 | 核心 | 显著 |",
        "|---|---|---:|---|---|---|",
    ]
    for work in sorted(works.values(), key=lambda x: x["title"]):
        buckets = defaultdict(list)
        for r in work["rels"]:
            buckets[r["salience"]].append(r["object"])
        lines.append(
            "| {work} | {author} | {count} | {dominant} | {core} | {significant} |".format(
                work=work_link(work["title"]),
                author=md_cell(work["author"]),
                count=len(work["rels"]),
                dominant=md_cell("；".join(buckets["dominant"])) or "—",
                core=md_cell("；".join(buckets["core"])) or "—",
                significant=md_cell("；".join(buckets["significant"])) or "—",
            )
        )
    lines += ["", "## 返回", "", "- [[00 文学意象与场景]]", "- [[04 意象关系索引]]", ""]
    OUT_WORKS.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    works, rels = collect()
    changed = update_work_pages(works)
    write_imagery_index(works, rels)
    write_work_index(works, rels)
    print(f"works={len(works)} rels={len(rels)} rendered_work_pages={changed}")
