from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / '个人通识知识系统_v2_A2' / '30 世界文学' / '30 专题'
M_PREFIXES = ['M1 ', 'M2 ', 'M3.1 ', 'M3.2 ', 'M4 ', 'M5.1 ', 'M5.2 ']


def split_doc(text: str):
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            return text[4:end], text[end+5:]
    return '', text


def scalar(fm: str, key: str) -> str:
    m = re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$', fm)
    return m.group(1).strip().strip('"\'') if m else ''


def upsert_scalar(fm: str, key: str, value: str) -> str:
    line = f'{key}: "{value.replace(chr(34), chr(39))}"'
    pat = rf'(?m)^{re.escape(key)}:.*$'
    if re.search(pat, fm):
        return re.sub(pat, line, fm, count=1)
    return fm.rstrip() + '\n' + line + '\n'


def topic_dirs():
    return sorted([p for p in TOPICS.iterdir() if p.is_dir() and any(p.name.startswith(x) for x in M_PREFIXES)])


def meta_for_dir(d: Path):
    wb = next(d.glob('03 *.base'))
    txt = wb.read_text(encoding='utf-8')
    # Find topic id and topic-specific fields from current Base.
    tid = re.search(r'topics\.contains\("([^"]+)"\)', txt)
    if not tid:
        # structure base always has topic_id
        sb = next(d.glob('02 *.base')).read_text(encoding='utf-8')
        tid = re.search(r'topic_id == "([^"]+)"', sb)
    topic_id = tid.group(1)
    pri = re.search(r'note\.([A-Za-z0-9_]+_priority):', txt).group(1)
    # cluster is the first topic-specific property after priority that is not history/axes
    fields = re.findall(r'note\.([A-Za-z0-9_]+):\n\s+displayName:', txt)
    cluster = next(f for f in fields if f != pri and f.endswith(('_movement_cluster','_tradition_cluster','_framework_cluster')))
    history = next(f for f in fields if f.endswith('_history_position'))
    axes = next(f for f in fields if f.endswith('_axes'))
    return topic_id, pri, cluster, history, axes


def rewrite_work_base(d: Path):
    path = next(d.glob('03 *.base'))
    old = path.read_text(encoding='utf-8')
    topic_id, pri, cluster, history, axes = meta_for_dir(d)
    folder = '个人通识知识系统_v2_A2/30 世界文学/40 作品'
    props = f'''properties:\n  file.name:\n    displayName: 作品\n  note.author:\n    displayName: 作者\n  note.read_status:\n    displayName: 阅读状态\n  note.topic_links:\n    displayName: 专题\n  note.topics:\n    displayName: 专题编号\n  note.{pri}:\n    displayName: 优先级\n  note.{cluster}:\n    displayName: 专题思潮\n  note.{history}:\n    displayName: 历史位置\n  note.{axes}:\n    displayName: 专题机制\n  note.axis_t:\n    displayName: 时间\n  note.axis_r:\n    displayName: 地域\n  note.axis_m:\n    displayName: M轴坐标\n  note.axis_g:\n    displayName: 类型\n  note.axis_q:\n    displayName: 主题\n  note.id:\n    displayName: 编号\n  note.verification_status:\n    displayName: 校验状态\n'''
    common_order = [
        'file.name','author','read_status','topic_links',pri,cluster,history,axes,
        'axis_t','axis_r','axis_m','axis_g','axis_q','id'
    ]
    def order_block(items=None):
        items = items or common_order
        return ''.join(f'      - {x}\n' for x in items)
    views = 'views:\n'
    views += '  - type: table\n    name: 全部作品\n    order:\n' + order_block()
    for label, sym in [('核心 ★','★'),('重点 ◆','◆'),('扩展 △','△')]:
        views += f'  - type: table\n    name: {label}\n    filters:\n      and:\n        - {pri} == "{sym}"\n    order:\n' + order_block()
    views += '  - type: table\n    name: 未读\n    filters:\n      and:\n        - read_status == "未读"\n    order:\n' + order_block()
    views += '  - type: table\n    name: 已读\n    filters:\n      and:\n        - or:\n            - read_status == "已读"\n            - read_status == "重读"\n    order:\n' + order_block()
    for name, field in [('按历史位置',history),('按专题思潮',cluster),('按地域','axis_r'),('按M轴坐标','axis_m'),('按类型','axis_g'),('按主题','axis_q')]:
        views += f'  - type: table\n    name: {name}\n    groupBy:\n      property: {field}\n      direction: ASC\n    order:\n' + order_block()
    views += '  - type: table\n    name: 待校验\n    filters:\n      and:\n        - verification_status != "自动通过"\n        - verification_status != "手工核验"\n    order:\n' + order_block(['file.name','author','verification_status','topic_links',pri,cluster,history,axes,'axis_t','axis_r','axis_m','axis_g','axis_q','id'])
    filters = f'''filters:\n  and:\n    - type == "work"\n    - file.folder == "{folder}"\n    - or:\n        - {pri} == "★"\n        - {pri} == "◆"\n        - {pri} == "△"\n'''
    path.write_text(filters + props + views, encoding='utf-8')


def update_parent_names(d: Path):
    sb = next(d.glob('02 *.base'))
    stext = sb.read_text(encoding='utf-8')
    tid = re.search(r'topic_id == "([^"]+)"', stext).group(1)
    # collect every structure md carrying this topic_id
    nodes = []
    for p in d.rglob('*.md'):
        text = p.read_text(encoding='utf-8', errors='ignore')
        fm, body = split_doc(text)
        if scalar(fm, 'topic_id') == tid and scalar(fm, 'id'):
            nodes.append((p, fm, body))
    id_name = {scalar(fm,'id'): p.stem for p,fm,_ in nodes}
    root_name = d.name.split(' ',1)[1] if ' ' in d.name else d.name
    id_name[tid] = root_name
    for p, fm, body in nodes:
        parent = scalar(fm, 'parent')
        parent_name = id_name.get(parent, parent if parent else '—')
        fm2 = upsert_scalar(fm, 'parent_name', parent_name)
        if fm2 != fm:
            p.write_text('---\n' + fm2.rstrip() + '\n---\n' + body, encoding='utf-8')
    return tid


def rewrite_structure_base(d: Path):
    path = next(d.glob('02 *.base'))
    tid = update_parent_names(d)
    type_formula = 'if(type == "literature_topic_mechanism", "形成机制", if(type == "literature_topic_section", "专题分支", if(dimension == "mechanism", "形成机制", "核心结构")))'
    dimension_formula = 'if(dimension, dimension.replace("tradition", "传统与地域").replace("movement", "思潮与运动").replace("paradigm", "美学范式").replace("framework", "批评框架").replace("historical_system", "谱系与内部结构").replace("core_question", "核心问题").replace("reading_route", "阅读路线").replace("transmission", "传播与地域").replace("comparison", "比较与边界").replace("definition", "定义与边界").replace("history", "时间框架与问题意识").replace("mechanism", "形成机制"), "")'
    text = f'''filters:\n  and:\n    - topic_id == "{tid}"\nformulas:\n  type_zh: {type_formula}\n  dimension_zh: {dimension_formula}\n  history_zh: if(history_position, history_position, "—")\n  mechanism_zh: if(mechanism, mechanism, "—")\nproperties:\n  file.name:\n    displayName: 节点\n  formula.type_zh:\n    displayName: 类型\n  formula.dimension_zh:\n    displayName: 维度\n  note.sequence:\n    displayName: 顺序\n  note.parent_name:\n    displayName: 父节点\n  formula.history_zh:\n    displayName: 历史位置\n  formula.mechanism_zh:\n    displayName: 机制\n  note.id:\n    displayName: 编号\nviews:\n'''
    order = '[file.name, formula.type_zh, formula.dimension_zh, sequence, parent_name, formula.history_zh, formula.mechanism_zh, id]'
    # All nodes explicitly grouped by type, matching T-axis interaction.
    text += f'''  - type: table\n    name: 全部知识节点\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order: {order}\n  - type: table\n    name: 按类型\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order: {order}\n  - type: table\n    name: 核心结构\n    filters:\n      and:\n        - 'type != "literature_topic_section"'\n        - 'type != "literature_topic_mechanism"'\n        - 'dimension != "mechanism"'\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order: {order}\n  - type: table\n    name: 专题分支\n    filters:\n      and:\n        - 'type == "literature_topic_section"'\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order: {order}\n  - type: table\n    name: 形成机制\n    filters:\n      or:\n        - 'type == "literature_topic_mechanism"'\n        - 'dimension == "mechanism"'\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order: {order}\n'''
    path.write_text(text, encoding='utf-8')


for d in topic_dirs():
    rewrite_work_base(d)
    rewrite_structure_base(d)
    print('repaired', d.name)
