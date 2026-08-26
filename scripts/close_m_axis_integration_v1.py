from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / '个人通识知识系统_v2_A2' / '30 世界文学'
NODES = LIT / '20 节点' / 'M 思潮'
TOPICS = LIT / '30 专题'

CFG = {
'M1': dict(folder='M1 早期现代思想与美学', home='00 早期现代思想与美学', node='M1 早期现代思想与美学.md', topic='WL-TOPIC-M1-EARLY-MODERN', priority='m1_priority', cluster='m1_movement_cluster', axes='m1_axes', cluster_zh='思潮'),
'M2': dict(folder='M2 19世纪文学思潮', home='00 19世纪文学思潮', node='M2 19世纪文学思潮.md', topic='WL-TOPIC-M2-19C-MOVEMENTS', priority='m2_priority', cluster='m2_movement_cluster', axes='m2_axes', cluster_zh='思潮'),
'M3.1': dict(folder='M3.1 现代主义', home='00 现代主义文学', node='M3.1 现代主义.md', topic='WL-TOPIC-M3-MODERNISM', priority='modernism_priority', cluster='modernism_tradition_cluster', axes='modernism_axes', cluster_zh='传统'),
'M3.2': dict(folder='M3.2 先锋派', home='00 先锋派', node='M3.2 先锋派.md', topic='WL-TOPIC-M3.2-AVANT-GARDE', priority='m32_priority', cluster='m32_movement_cluster', axes='m32_axes', cluster_zh='运动'),
'M4': dict(folder='M4 集体文学运动与文化政治', home='00 集体文学运动与文化政治', node='M4 政治、民族与文化运动.md', topic='WL-TOPIC-M4-COLLECTIVE-MOVEMENTS', priority='m4_priority', cluster='m4_movement_cluster', axes='m4_axes', cluster_zh='运动'),
'M5.1': dict(folder='M5.1 战后思想与美学范式', home='00 战后思想与美学范式', node='M5.1 战后思想与美学范式.md', topic='WL-TOPIC-M5.1-POSTWAR-AESTHETICS', priority='m51_priority', cluster='m51_movement_cluster', axes='m51_axes', cluster_zh='范式'),
'M5.2': dict(folder='M5.2 权力、身份与世界批评', home='00 权力、身份与世界批评', node='M5.2 权力、身份与世界批评.md', topic='WL-TOPIC-M5.2-POWER-IDENTITY-WORLD', priority='m52_priority', cluster='m52_framework_cluster', axes='m52_axes', cluster_zh='框架', role='m52_role'),
}

DIM_MAP = {
'01': 'definition', '02': 'history', '03': 'historical_system', '04': 'mechanism',
'05': 'transmission', '06': 'comparison', '07': 'reading_route', '00': 'overview'
}

def split_fm(text: str):
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---\n', 4)
    if end < 0:
        return {}, text
    raw, body = text[4:end], text[end+5:]
    data = {}
    for line in raw.splitlines():
        m = re.match(r'^([A-Za-z0-9_.-]+):\s*(.*)$', line)
        if m:
            data[m.group(1)] = m.group(2)
    return data, body

def ensure_structure_frontmatter(path: Path, topic_id: str, folder: str):
    text = path.read_text(encoding='utf-8')
    _, body = split_fm(text)
    rel = path.relative_to(TOPICS / folder).as_posix()
    name = path.stem
    seqm = re.match(r'^(\d+)', name)
    seq = int(seqm.group(1)) if seqm else 0
    if rel.startswith('10 核心结构/'):
        typ = 'literature_topic_structure'
        dim = DIM_MAP.get(f'{seq:02d}', 'core_question')
    elif rel.startswith('11 '):
        typ = 'literature_topic_section'; dim = 'literary_field'
    elif rel.startswith('12 '):
        typ = 'literature_topic_mechanism'; dim = 'mechanism'
    elif rel.startswith('13 '):
        typ = 'literature_topic_section'; dim = 'comparison'
    else:
        return
    fm = f'---\ntype: {typ}\ntopic_id: {topic_id}\ndimension: {dim}\nsequence: {seq}\nparent: {topic_id}\n---\n'
    path.write_text(fm + body.lstrip('\n'), encoding='utf-8')

def structure_base(topic_id: str) -> str:
    return f'''filters:\n  and:\n    - topic_id == "{topic_id}"\nformulas:\n  type_zh: if(type == "literature_topic_mechanism", "形成机制", if(type == "literature_topic_section", "专题分支", "核心结构"))\n  dimension_zh: if(dimension, dimension.replace("historical_system", "谱系与内部结构").replace("core_question", "核心问题").replace("reading_route", "阅读路线").replace("comparison", "边界与比较").replace("definition", "定义与边界").replace("history", "历史条件与问题意识").replace("mechanism", "形成机制").replace("transmission", "传播、地域与非同步性").replace("literary_field", "专题分支"), "")\n  parent_zh: if(parent == "{topic_id}", "{topic_id}", parent)\nproperties:\n  file.name:\n    displayName: 节点\n  formula.type_zh:\n    displayName: 类型\n  formula.dimension_zh:\n    displayName: 维度\n  note.sequence:\n    displayName: 顺序\n  formula.parent_zh:\n    displayName: 父节点\n  note.mechanism:\n    displayName: 机制\n  note.id:\n    displayName: 编号\nviews:\n  - type: table\n    name: 全部知识节点\n    groupBy:\n      property: formula.type_zh\n      direction: ASC\n    order: [file.name, formula.type_zh, formula.dimension_zh, sequence, formula.parent_zh, mechanism, id]\n  - type: table\n    name: 核心结构\n    filters:\n      and:\n        - 'type != "literature_topic_section"'\n        - 'type != "literature_topic_mechanism"'\n    order: [file.name, formula.dimension_zh, sequence, id]\n  - type: table\n    name: 专题分支\n    filters:\n      and:\n        - 'type == "literature_topic_section"'\n    order: [file.name, formula.dimension_zh, sequence, id]\n  - type: table\n    name: 形成机制\n    filters:\n      and:\n        - 'type == "literature_topic_mechanism"'\n    order: [file.name, formula.dimension_zh, sequence, mechanism, id]\n'''

def work_base(c: dict) -> str:
    p, cl, ax = c['priority'], c['cluster'], c['axes']
    role_prop = ''
    role_order = ''
    if c.get('role'):
        role_prop = f'  note.{c["role"]}:\n    displayName: 角色\n'
        role_order = f'      - {c["role"]}\n'
    common = f'''      - file.name\n      - author\n      - read_status\n      - topic_links\n      - {p}\n      - {cl}\n{role_order}      - {ax}\n      - axis_t\n      - axis_r\n      - axis_m\n      - axis_g\n      - axis_q\n      - id\n'''
    return f'''filters:\n  and:\n    - type == "work"\n    - topics.contains("{c['topic']}")\nproperties:\n  file.name:\n    displayName: 作品\n  note.author:\n    displayName: 作者\n  note.read_status:\n    displayName: 阅读状态\n  note.topic_links:\n    displayName: 专题\n  note.topics:\n    displayName: 专题编号\n  note.{p}:\n    displayName: 优先级\n  note.{cl}:\n    displayName: {c['cluster_zh']}\n{role_prop}  note.{ax}:\n    displayName: 机制\n  note.axis_t:\n    displayName: 时间\n  note.axis_r:\n    displayName: 地域\n  note.axis_m:\n    displayName: 思潮\n  note.axis_g:\n    displayName: 类型\n  note.axis_q:\n    displayName: 主题\n  note.id:\n    displayName: 编号\n  note.verification_status:\n    displayName: 校验状态\nviews:\n  - type: table\n    name: 全部作品\n    order:\n{common}  - type: table\n    name: 核心 ★\n    filters:\n      and:\n        - {p} == "★"\n    order:\n{common}  - type: table\n    name: 重点 ◆\n    filters:\n      and:\n        - {p} == "◆"\n    order:\n{common}  - type: table\n    name: 扩展 △\n    filters:\n      and:\n        - {p} == "△"\n    order:\n{common}  - type: table\n    name: 未读\n    filters:\n      and:\n        - read_status == "未读"\n    order:\n{common}  - type: table\n    name: 已读\n    filters:\n      and:\n        - or:\n            - read_status == "已读"\n            - read_status == "重读"\n    order:\n{common}  - type: table\n    name: 按{c['cluster_zh']}\n    groupBy:\n      property: {cl}\n      direction: ASC\n    order:\n{common}  - type: table\n    name: 按地域\n    groupBy:\n      property: axis_r\n      direction: ASC\n    order:\n{common}  - type: table\n    name: 按思潮\n    groupBy:\n      property: axis_m\n      direction: ASC\n    order:\n{common}  - type: table\n    name: 按类型\n    groupBy:\n      property: axis_g\n      direction: ASC\n    order:\n{common}  - type: table\n    name: 按主题\n    groupBy:\n      property: axis_q\n      direction: ASC\n    order:\n{common}  - type: table\n    name: 待校验\n    filters:\n      and:\n        - verification_status != "自动通过"\n        - verification_status != "手工核验"\n    order:\n{common}'''

def update_node(code: str, c: dict):
    p = NODES / c['node']
    text = p.read_text(encoding='utf-8')
    topic_path = f'../../30 专题/{c["folder"]}/{c["home"]}'
    if re.search(r'(?m)^topic_map:', text):
        # Replace scalar/null or simple YAML list block.
        text = re.sub(r'(?ms)^topic_map:\s*(?:\n\s+-[^\n]*)?[^\n]*', f'topic_map: "{topic_path}"', text, count=1)
    else:
        text = text.replace('anchorable: true\n', f'anchorable: true\ntopic_map: "{topic_path}"\n', 1)
    text = text.replace('> 暂未接入。', f'- [[{topic_path}|进入 {code} 专题地图]]')
    p.write_text(text, encoding='utf-8')

def upgrade_thin_topic(code: str, c: dict):
    if code not in {'M4','M5.1','M5.2'}: return
    td = TOPICS / c['folder']
    if code == 'M4':
        core = {
'01 定义与边界.md': '# 定义与边界\n\nM4 研究真实发生的集体文学运动、文化共同体、政治纲领与跨国网络，而不是把所有政治主题作品都收入。判定重点是作品是否在运动组织、身份共同体、制度化纲领或跨国文学网络中具有结构作用。\n\nM4 与 M3 的区别在于：M3 更关注形式与艺术制度的先锋化，M4 更关注文学如何组织集体主体并进入历史行动。与 M5.2 的区别在于：M4 研究真实运动，M5.2 研究后续批评框架。\n',
'02 历史条件与问题意识.md': '# 历史条件与问题意识\n\n民族国家、工业资本主义、阶级政治、殖民体系、革命、种族秩序、大众出版与跨国文化市场，使文学越来越以群体身份和公共行动组织自身。M4 因而不以单一风格串联，而以“谁组成共同体、共同体如何行动、文学如何传播”作为主问题。\n',
'03 运动谱系与内部结构.md': '# 运动谱系与内部结构\n\nM4 分为三条线：政治与阶级文学（民族主义、无产阶级、革命文学、社会主义现实主义）；身份与文化解放（Harlem Renaissance、Négritude、反殖民文学运动）；文学群体与跨国网络（Beat Generation、Latin American Boom）。三条线分别展示国家/阶级、种族/殖民身份、代际/出版网络如何形成文学共同体。\n',
'04 集体机制与文学行动.md': '# 集体机制与文学行动\n\n关键机制包括宣言与纲领、杂志与出版社、社团与作家群、革命组织、国家文化制度、朗诵与表演空间、翻译与文学代理、国际出版市场。阅读时应把作品放回这些组织机制，而不是只按主题解释。\n',
'05 传播、地域与非同步性.md': '# 传播、地域与非同步性\n\n不同运动并不同步：民族主义文学可早至19世纪，Harlem Renaissance 与 Négritude 通过跨大西洋网络关联，社会主义现实主义依赖制度传播，Boom 则高度依赖跨国出版与翻译。地域传播不能被压缩成一条欧洲中心时间线。\n',
'06 与M3、M5.1、M5.2的边界.md': '# 与 M3、M5.1、M5.2 的边界\n\nM3.1/M3.2 解释现代主义和先锋派如何改变形式与艺术制度；M4 解释文学如何成为集体行动。M5.1 解释战后美学范式，M5.2 解释权力与身份批评框架。Boom 属于 M4 的网络现象，魔幻现实主义属于 M5.1 的美学模式；Négritude 属于 M4 的历史运动，后殖民理论属于 M5.2。\n',
'07 阅读路线.md': '# 阅读路线\n\n先各读一组 ★ 骨架建立三类共同体：民族/阶级与革命 → 黑人文化与反殖民 → Beat 与 Boom。随后沿“组织机制”横读：宣言与纲领、杂志与社群、国家制度、跨国出版与翻译。最后再把同一作品投影到 M3、M5.1、M5.2，区分形式、运动与批评框架三种问题。\n'}
    elif code == 'M5.1':
        core = {
'01 定义与边界.md':'# 定义与边界\n\nM5.1 研究二战后文学内部关于主体、意义、现实、语言、叙事与文本权威的重组，不等于所有战后文学。进入本专题的作品必须能解释存在主义、荒诞、新小说、魔幻现实主义或后现代主义中的一种结构变化。\n',
'02 历史条件与问题意识.md':'# 历史条件与问题意识\n\n二战、大屠杀、冷战、核威胁、去殖民、消费社会与媒介扩张，使“理性主体—透明现实—连续叙事”的稳定前提进一步松动。文学因而从现代主义的形式危机推进到意义、再现和文本权威本身的危机。\n',
'03 范式谱系与内部结构.md':'# 范式谱系与内部结构\n\n存在主义从自由、选择与责任切入；荒诞把危机推进到语言和行动失效；法国新小说怀疑人物、心理和情节的透明再现；魔幻现实主义重组现实层级与历史经验；后现代主义进一步暴露文本、历史与符号系统的不稳定。\n',
'04 美学机制与叙事重组.md':'# 美学机制与叙事重组\n\n主要机制包括等待与重复、语言失效、去心理化、物的凝视、叙事不确定、循环时间、神话现实、元小说、拼贴、互文、历史戏仿、阴谋叙事与媒介过载。机制页用于跨范式比较，不把机制本身等同于流派。\n',
'05 传播、地域与非同步性.md':'# 传播、地域与非同步性\n\n战后美学并非从法国向全球单向扩散。拉美魔幻现实主义、美国后现代主义、东欧和非洲等地的现实重组各有不同历史条件。专题采用多中心传播视角，并允许同一作品与 M4、M5.2 形成合法投影。\n',
'06 与M3.1、M4、M5.2的边界.md':'# 与 M3.1、M4、M5.2 的边界\n\nM3.1 主要解释现代经验为何迫使文学改变形式；M5.1 进一步追问主体、意义、现实和文本权威是否稳定。M4 研究真实运动与网络；M5.2 研究权力与知识框架。Boom ≠ 魔幻现实主义，后殖民理论也不等于后殖民文学的美学样式。\n',
'07 阅读路线.md':'# 阅读路线\n\n建议沿“主体危机 → 语言/行动危机 → 再现危机 → 现实层级重组 → 文本权威危机”阅读：存在主义 → 荒诞 → 法国新小说 → 魔幻现实主义 / 后现代主义。每一阶段先读 ★ 骨架，再用 ◆ 扩展地域和机制。\n'}
    else:
        core = {
'01 定义与边界.md':'# 定义与边界\n\nM5.2 不是“女性、殖民、同性欲望、自然”等主题标签集合，而是研究批评框架如何重新定义主体、文明、性别、知识与世界。作品进入本专题，必须能支撑后殖民、去殖民、女性主义、酷儿、生态批评或生态文学中的结构性问题。\n',
'02 历史条件与问题意识.md':'# 历史条件与问题意识\n\n去殖民、民权与女性运动、性政治、知识生产批判、环境危机与全球化共同推动文学研究从“作品表达了什么”转向“谁有权定义、谁被表述、谁被排除、什么被视为正常或自然”。\n',
'03 批评谱系与内部结构.md':'# 批评谱系与内部结构\n\n殖民与知识权力线包含后殖民与去殖民；性别、身体与身份线包含女性主义与酷儿；人类与非人世界线包含生态批评与生态文学。三条线从被排除的人类主体逐渐推进到对“人类中心主义”本身的反思。\n',
'04 权力机制与文学重读.md':'# 权力机制与文学重读\n\n关键机制包括他者化、殖民话语、知识地缘政治、父权制、性别表演、规范性、交叉权力、环境正义、慢暴力、自然/文化二分与多物种共生。理论文本提供概念，文学文本用于检验这些概念如何改变具体阅读。\n',
'05 传播、地域与非同步性.md':'# 传播、地域与非同步性\n\n这些框架并非统一时间表：后殖民与去殖民来自不同殖民经验，女性主义内部存在种族和阶级差异，酷儿理论与不同地域性规范交织，生态批评也因工业化、原住民土地与气候风险而异。必须保留地域语境。\n',
'06 与M4、M5.1的边界.md':'# 与 M4、M5.1 的边界\n\nM4 研究真实文学运动与共同体，M5.2 研究批评框架；M5.1 研究战后文学内部的美学变化，M5.2 追问谁有权定义这些主体和现实。同一作品可多专题投影，但后加入的 M5.2 不覆盖既有 M 轴主坐标。\n',
'07 阅读路线.md':'# 阅读路线\n\n先读理论 ★ 骨架建立概念，再用文学作品验证：后殖民 → 去殖民；女性主义 → 酷儿；生态批评 → 生态文学。第二轮沿“谁能说话 / 谁被看见 / 谁定义知识 / 谁被视为正常 / 人是否仍是唯一尺度”横向比较。\n'}
    for fn, body in core.items():
        p = td/'10 核心结构'/fn
        if p.exists(): p.write_text(body, encoding='utf-8')

    # Richer cognitive canvas with file nodes where possible.
    if code == 'M4':
        nodes=[('root','file','00 集体文学运动与文化政治.md',0,0),('ctx','file','10 核心结构/02 历史条件与问题意识.md',0,-300),('p','text','政治与阶级文学\n民族主义 / 无产阶级 / 革命 / 社会主义现实主义',-520,220),('i','text','身份与文化解放\nHarlem / Négritude / 反殖民',0,220),('n','text','文学群体与跨国网络\nBeat / Latin American Boom',520,220),('m','file','10 核心结构/04 集体机制与文学行动.md',0,500),('r','file','10 核心结构/07 阅读路线.md',0,760)]
    elif code == 'M5.1':
        nodes=[('root','file','00 战后思想与美学范式.md',0,0),('ctx','file','10 核心结构/02 历史条件与问题意识.md',0,-300),('e','text','主体与意义危机\n存在主义 → 荒诞',-520,220),('r','text','再现危机\n法国新小说',0,220),('t','text','现实与文本权威危机\n魔幻现实主义 / 后现代主义',520,220),('m','file','10 核心结构/04 美学机制与叙事重组.md',0,500),('route','file','10 核心结构/07 阅读路线.md',0,760)]
    else:
        nodes=[('root','file','00 权力、身份与世界批评.md',0,0),('ctx','file','10 核心结构/02 历史条件与问题意识.md',0,-300),('c','text','殖民与知识权力\n后殖民 → 去殖民',-520,220),('g','text','性别、身体与身份\n女性主义 → 酷儿',0,220),('e','text','人类与非人世界\n生态批评 → 生态文学',520,220),('m','file','10 核心结构/04 权力机制与文学重读.md',0,500),('route','file','10 核心结构/07 阅读路线.md',0,760)]
    arr=[]
    for nid,typ,val,x,y in nodes:
        d={'id':nid,'type':typ,'x':x,'y':y,'width':360,'height':120}
        d['file' if typ=='file' else 'text']=val; arr.append(d)
    edges=[]
    for j,(a,b) in enumerate([('ctx','root'),('root','p' if code=='M4' else ('e' if code=='M5.1' else 'c')),('root','i' if code=='M4' else ('r' if code=='M5.1' else 'g')),('root','n' if code=='M4' else ('t' if code=='M5.1' else 'e')),('p' if code=='M4' else ('e' if code=='M5.1' else 'c'),'m'),('i' if code=='M4' else ('r' if code=='M5.1' else 'g'),'m'),('n' if code=='M4' else ('t' if code=='M5.1' else 'e'),'m'),('m','r' if code=='M4' else 'route')],1):
        edges.append({'id':f'e{j}','fromNode':a,'toNode':b})
    canvas = td / ('01 '+c['folder'].split(' ',1)[1]+'.canvas')
    if canvas.exists(): canvas.write_text(json.dumps({'nodes':arr,'edges':edges},ensure_ascii=False,indent=2),encoding='utf-8')

for code,c in CFG.items():
    update_node(code,c)
    td=TOPICS/c['folder']
    # rewrite Bases in T-axis style
    b2=next(td.glob('02 *.base')); b2.write_text(structure_base(c['topic']),encoding='utf-8')
    b3=next(td.glob('03 *.base')); b3.write_text(work_base(c),encoding='utf-8')
    # normalize internal structure metadata
    for p in td.rglob('*.md'):
        rel=p.relative_to(td).as_posix()
        if rel.startswith(('10 ','11 ','12 ','13 ')):
            ensure_structure_frontmatter(p,c['topic'],c['folder'])
    upgrade_thin_topic(code,c)

print('M-axis integration closure applied for', ', '.join(CFG))
