# -*- coding: utf-8 -*-
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(r"d:\worldForMe\个人通识知识系统_v2_A2\30 世界文学\40 作品")
OUT = Path(r"d:\worldForMe\个人通识知识系统_v2_A2\30 世界文学\30 专题\QX 文学意象与场景\04 意象关系索引.md")
OUT_WORKS = Path(r"d:\worldForMe\个人通识知识系统_v2_A2\30 世界文学\30 专题\QX 文学意象与场景\05 作品意象一览.md")

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

LEAF = {
    "QX1.1": "文学中的雨",
    "QX3.1": "文学中的海",
    "QX16.1": "文学中的书信",
}

SAL_RANK = {"dominant": 0, "core": 1, "significant": 2, "minor": 3}


def split_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[4:end] if end > 0 else ""


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", fm, re.M)
    if not m:
        return ""
    val = m.group(1).strip().strip("'\"")
    return val


def extract_qx_yaml(fm: str) -> list:
    m = re.search(r"^qx:\s*$", fm, re.M)
    if not m:
        return []
    start = m.end()
    rest = fm[start:]
    nxt = re.search(r"^[A-Za-z_][A-Za-z0-9_]*:", rest, re.M)
    block = rest[: nxt.start()] if nxt else rest
    try:
        data = yaml.safe_load("qx:\n" + block)
    except Exception:
        return []
    items = (data or {}).get("qx") or []
    return items if isinstance(items, list) else []


def as_list(val) -> list:
    if val is None:
        return []
    if isinstance(val, list):
        return [str(x) for x in val]
    return [str(val)]


def collect():
    rels = []
    work_files = 0
    for p in sorted(ROOT.glob("*.md")):
        fm = split_frontmatter(p.read_text(encoding="utf-8"))
        if not fm:
            continue
        items = extract_qx_yaml(fm)
        if not items:
            continue
        work_files += 1
        title = scalar(fm, "title") or p.stem
        author = scalar(fm, "author")
        for item in items:
            if not isinstance(item, dict):
                continue
            obj = item.get("object")
            if not obj:
                continue
            if item.get("admission_status") == "candidate":
                continue
            rels.append(
                {
                    "file": p.stem,
                    "title": title,
                    "author": author,
                    "qx_id": item.get("qx_id"),
                    "object": str(obj).strip(),
                    "group": str(item.get("primary_group") or "").strip(),
                    "salience": str(item.get("salience") or "").strip(),
                    "manifestation": str(item.get("manifestation") or "").strip(),
                    "function": as_list(item.get("function")),
                    "evidence": as_list(item.get("evidence")),
                }
            )
    return work_files, rels


def md_cell(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def work_link(title: str) -> str:
    return f"[[../../40 作品/{title}|{title}]]"


def write_index(work_files: int, rels: list) -> None:
    by_group = defaultdict(list)
    for r in rels:
        by_group[r["group"]].append(r)

    lines = [
        "---",
        "id: WL-TOPIC-QX-REL-INDEX",
        "topic_id: WL-TOPIC-QX",
        "type: literature_qx_relation_index",
        "name: QX 意象关系索引",
        "axis: Q",
        "facet: QX",
        "status: ACTIVE",
        "---",
        "# QX 意象关系索引",
        "",
        "> 从 `40 作品` 的正式 `qx` 关系汇总，一行一条意象关系。候选（`admission_status: candidate`）不计入。",
        "",
        f"当前：{work_files} 部作品，{len(rels)} 条正式关系。",
        "",
        "## 一类数量",
        "",
        "| 一类 | 名称 | 关系数 | 作品数 |",
        "|---|---|---:|---:|",
    ]
    for code, name in GROUPS:
        items = by_group.get(code, [])
        n_works = len({r["file"] for r in items})
        lines.append(f"| {code} | {name} | {len(items)} | {n_works} |")
    other = [r for r in rels if r["group"] not in GROUP_LABEL]
    if other:
        lines.append(f"| （未归类） |  | {len(other)} | {len({r['file'] for r in other})} |")

    lines += [
        "",
        "## 已激活叶节点",
        "",
        "| 叶节点 | 关系数 | 作品 |",
        "|---|---:|---|",
    ]
    for qid, label in LEAF.items():
        items = [r for r in rels if r["qx_id"] == qid]
        works = "；".join(f"《{r['title']}》" for r in items)
        lines.append(f"| [[{qid} {label}|{label}]] | {len(items)} | {works or '—'} |")

    for code, name in GROUPS:
        items = by_group.get(code, [])
        items.sort(key=lambda r: (SAL_RANK.get(r["salience"], 9), r["object"], r["title"]))
        lines += ["", f"## {code} {name}", ""]
        if not items:
            lines.append("当前没有正式关系。")
            continue
        lines += [
            "| 对象 | 作品 | 强度 | 主要功能 | 叶节点 |",
            "|---|---|---|---|---|",
        ]
        for r in items:
            leaf = LEAF.get(r["qx_id"] or "", "")
            leaf_cell = f"[[{r['qx_id']} {leaf}|{leaf}]]" if leaf else ""
            func = "；".join(r["function"][:4])
            lines.append(
                f"| {md_cell(r['object'])} | {work_link(r['title'])} | {md_cell(r['salience'])} | {md_cell(func)} | {leaf_cell} |"
            )

    lines += ["", "## 返回", "", "- [[00 文学意象与场景]]", "- [[05 作品意象一览]]", ""]
    OUT.write_text("\n".join(lines), encoding="utf-8")


def write_work_index(work_files: int, rels: list) -> None:
    by_work = defaultdict(list)
    meta = {}
    for r in rels:
        by_work[r["file"]].append(r)
        meta[r["file"]] = (r["title"], r["author"])

    lines = [
        "---",
        "id: WL-TOPIC-QX-WORK-INDEX",
        "topic_id: WL-TOPIC-QX",
        "type: literature_qx_work_index",
        "name: QX 作品意象一览",
        "axis: Q",
        "facet: QX",
        "status: ACTIVE",
        "---",
        "# QX 作品意象一览",
        "",
        "> 按作品看正式意象。证据仍在各作品页的 `qx` 字段；按对象反查见 [[04 意象关系索引]]。",
        "",
        f"当前：{work_files} 部作品，{len(rels)} 条正式关系。",
        "",
        "| 作品 | 作者 | 条数 | 意象 |",
        "|---|---|---:|---|",
    ]
    for file in sorted(by_work, key=lambda k: meta[k][0]):
        items = sorted(by_work[file], key=lambda r: (SAL_RANK.get(r["salience"], 9), r["object"]))
        title, author = meta[file]
        bits = []
        for r in items:
            leaf = LEAF.get(r["qx_id"] or "", "")
            label = f"{r['object']}"
            if r["group"]:
                label += f"/{r['group']}"
            if r["salience"]:
                label += f" {r['salience']}"
            if leaf:
                label += f"（{leaf}）"
            bits.append(label)
        lines.append(
            f"| {work_link(title)} | {md_cell(author)} | {len(items)} | {md_cell('；'.join(bits))} |"
        )
    lines += ["", "## 返回", "", "- [[00 文学意象与场景]]", "- [[04 意象关系索引]]", ""]
    OUT_WORKS.write_text("\n".join(lines), encoding="utf-8")


def rain_rows(rels: list) -> list:
    rows = []
    for r in rels:
        if r["qx_id"] == "QX1.1" or ("雨" in r["object"] and r["group"] == "QX1"):
            rows.append(r)
    rows.sort(key=lambda r: (SAL_RANK.get(r["salience"], 9), r["title"]))
    return rows


if __name__ == "__main__":
    work_files, rels = collect()
    write_index(work_files, rels)
    write_work_index(work_files, rels)
    rain = rain_rows(rels)
    print(f"works={work_files} rels={len(rels)} rain={len(rain)}")
    for r in rain:
        evid = r["evidence"][0] if r["evidence"] else ""
        print("---")
        print(r["title"])
        print(r["author"])
        print(r["object"])
        print(r["salience"])
        print(r["manifestation"])
        print(" | ".join(r["function"]))
        print(evid)
