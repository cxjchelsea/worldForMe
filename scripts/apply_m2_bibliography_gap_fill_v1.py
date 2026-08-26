from __future__ import annotations

import ast
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = LIT / "40 作品"
TOPIC_DIR = LIT / "30 专题" / "M2 19世纪文学思潮"
SOURCE_SCRIPT = ROOT / "scripts" / "apply_m2_v2_structure_and_map_existing_v1.py"
TOPIC_ID = "WL-TOPIC-M2-19C-MOVEMENTS"
LINK = "[[../30 专题/M2 19世纪文学思潮/00 19世纪文学思潮|19世纪文学思潮]]"


def read_bib():
    tree = ast.parse(SOURCE_SCRIPT.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "BIB" for t in node.targets):
            return ast.literal_eval(node.value)
    raise RuntimeError("BIB not found")


def make_id(title: str) -> str:
    digest = hashlib.sha1(title.encode("utf-8")).hexdigest()[:12].upper()
    return f"WL-WORK-M2-{digest}"


def content(title, author, movement, priority, axes):
    wid = make_id(title)
    return f'''---\nid: {wid}\ntype: work\ntitle: {title}\ntitle_original: ''\naliases: []\nauthor: {author}\nyear: null\nliterary_traditions: []\nread_status: 未读\naxis_t:\n- T3 19世纪现代文学体系\naxis_r: []\naxis_m:\n- M2 19世纪文学思潮 / {movement}\naxis_g: []\naxis_q: []\naxis_source: manual_m2_structural_gap_fill_v1\ntopics:\n- {TOPIC_ID}\ntopic_links:\n- '{LINK}'\nm2_priority: {priority}\nm2_movement_cluster: {movement}\nm2_axes:\n''' + ''.join(f'- {x}\n' for x in axes) + '''verification_status: 手工核验\nbibliography_status: structural_anchor_metadata_pending\n---\n# ''' + title + f'''\n\n## M2 专题角色\n\n- 思潮：{movement}\n- 专题优先级：{priority}\n- 机制：{'；'.join(axes)}\n\n> M2 V2 Structural Gap Fill：该作品因支撑19世纪文学思潮的结构槽位而补入中央作品库；作品实体只保留于 `40 作品/`。书目年份、原文标题与其他轴元数据后续由中央作品库治理统一校验。\n'''

bib = read_bib()
created=[]; existing=[]
for title,author,movement,priority,axes in bib:
    path = WORKS / f"{title}.md"
    if path.exists():
        existing.append(title)
        continue
    path.write_text(content(title,author,movement,priority,axes),encoding="utf-8")
    created.append(title)

report = ["# M2 结构性书目补齐 v1","",f"- target bibliography: **{len(bib)}**",f"- existing canonical works: **{len(existing)}**",f"- newly created canonical works: **{len(created)}**","","## 新增作品",""] + [f"- {x}" for x in created] + ["","## 治理边界","","- 不按年代批量吸收所有19世纪作品。","- 新增作品均来自 M2 八个思潮的结构槽位。","- 不复制专题内作品实体；`03 19世纪文学思潮作品.base` 仅动态投影中央作品库。","- 新增实体的年份/原文标题等非结构性元数据保持 metadata pending，不在本阶段猜填。",""]
(TOPIC_DIR / "04 19世纪文学思潮书目覆盖审计.md").write_text("\n".join(report),encoding="utf-8")
print(f"target={len(bib)} existing={len(existing)} created={len(created)}")
for x in created: print("CREATED",x)
