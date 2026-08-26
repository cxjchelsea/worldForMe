from pathlib import Path
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R5 北美文学'
NODE=ROOT/'20 节点'/'R 地域'/'R5 北美文学.md'

def write(rel,txt):
 p=TOP/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(txt,encoding='utf-8')

def fm(id_,typ,dim,seq):
 return f'---\nid: "{id_}"\ntype: "{typ}"\ntopic_id: "WL-TOPIC-R5-NORTH-AMERICA"\ndimension: "{dim}"\nsequence: {seq}\n---\n\n'

TOP.mkdir(parents=True,exist_ok=True)
write('00 北美文学.md','''---
id: WL-TOPIC-R5-NORTH-AMERICA
type: literature_topic_map
name: "北美文学"
primary_anchor: WL-R5
anchor_mode: exact
taxonomy_version: literature-taxonomy-v2
topic_role: direct
structure_status: active
structure_database: "[[02 R5文学结构.base]]"
work_database: "[[03 R5文学作品.base]]"
template_version: literature-topic-r-v1
---
# R5｜北美文学

> 路径：[[../../00 世界文学使用规则|世界文学]] → [[../../10 轴/R轴 世界文学传统|R轴]] → **R5 北美文学**

## 专题定位
R5 研究美国、加拿大及北美原住民、非裔、移民与少数族裔文学在殖民、奴隶制、定居殖民、移民、都市化、种族政治、双语/多语文化与全球出版中的形成。墨西哥及拉丁美洲主传统属于 R6；跨边境的奇卡诺/拉美裔美国文学按主要文学场进入 R5，并与 R6 建边。

## 核心问题
> **北美文学如何在定居殖民、奴隶制与移民社会的历史条件下，形成彼此竞争又持续互相改写的多传统文学场？**

## 导航
- [[01 北美文学.canvas|R5 Canvas]]
- [[02 R5文学结构.base|R5 文学结构数据库]]
- [[03 R5文学作品.base|R5 作品数据库]]

### 核心结构
- [[10 核心结构/01 定义与边界|定义与边界]]
- [[10 核心结构/02 历史层与连续性|历史层与连续性]]
- [[10 核心结构/03 语言文字与媒介|语言文字与媒介]]
- [[10 核心结构/04 文学制度与传播|文学制度与传播]]
- [[10 核心结构/05 阅读路线|阅读路线]]

### 内部传统
1. [[11 内部传统/01 北美原住民文学传统|北美原住民文学传统]]
2. [[11 内部传统/02 殖民地—清教徒与早期共和国文学传统|殖民地—清教徒与早期共和国文学传统]]
3. [[11 内部传统/03 十九世纪—现代美国文学传统|十九世纪—现代美国文学传统]]
4. [[11 内部传统/04 非裔美国文学传统|非裔美国文学传统]]
5. [[11 内部传统/05 犹太裔美国文学传统|犹太裔美国文学传统]]
6. [[11 内部传统/06 亚裔美国文学传统|亚裔美国文学传统]]
7. [[11 内部传统/07 拉美裔—奇卡诺美国文学传统|拉美裔—奇卡诺美国文学传统]]
8. [[11 内部传统/08 英语加拿大文学传统|英语加拿大文学传统]]
9. [[11 内部传统/09 法语加拿大—魁北克文学传统|法语加拿大—魁北克文学传统]]

### 跨传统网络
- [[12 跨传统网络/01 定居殖民—原住民接触与反叙事网络|定居殖民—原住民接触与反叙事网络]]
- [[12 跨传统网络/02 奴隶制—废奴与黑色大西洋网络|奴隶制—废奴与黑色大西洋网络]]
- [[12 跨传统网络/03 边疆—西部与国家神话网络|边疆—西部与国家神话网络]]
- [[12 跨传统网络/04 移民—都市与族裔出版网络|移民—都市与族裔出版网络]]
- [[12 跨传统网络/05 哈莱姆—民权与黑人文化运动网络|哈莱姆—民权与黑人文化运动网络]]
- [[12 跨传统网络/06 美加双语—区域主义与跨境网络|美加双语—区域主义与跨境网络]]
- [[12 跨传统网络/07 当代跨国—离散与全球出版网络|当代跨国—离散与全球出版网络]]

## 边界
- 墨西哥文学主坐标属于 R6；奇卡诺/拉美裔美国文学按美国文学场进入 R5，并与 R6 连接。
- 非裔美国文学属于 R5；当黑色大西洋/非洲离散成为首要框架时同时连接 R10.2。
- 原住民传统不能被美国/加拿大国界完全切开，R5 以文学共同体和语言传统为优先。
- 加拿大法语文学单列，不把魁北克文学压入英语加拿大框架。

## 状态
`R5_TOPIC_MAP_STRUCTURE = ACTIVE`
''')
write('02 R5文学结构.base','''filters:\n  and:\n    - topic_id == "WL-TOPIC-R5-NORTH-AMERICA"\nproperties:\n  file.name:\n    displayName: 节点\n  note.dimension:\n    displayName: 维度\n  note.sequence:\n    displayName: 顺序\nviews:\n  - type: table\n    name: 全部 R5 知识节点\n    order: [file.name, dimension, sequence]\n  - type: table\n    name: 内部传统\n    filters:\n      and:\n        - dimension == "internal_tradition"\n    order: [file.name, sequence]\n  - type: table\n    name: 跨传统网络\n    filters:\n      and:\n        - dimension == "literary_network"\n    order: [file.name, sequence]\n''')
write('03 R5文学作品.base','''filters:\n  and:\n    - type == "work"\n    - axis_r.contains("R5 北美文学")\nproperties:\n  file.name: {displayName: 作品}\n  note.author: {displayName: 作者}\n  note.year: {displayName: 年份}\n  note.r5_priority: {displayName: R5优先级}\n  note.r5_tradition: {displayName: 内部传统}\n  note.r5_role: {displayName: R5机制/意义}\n  note.axis_t: {displayName: 时间}\n  note.read_status: {displayName: 阅读状态}\nviews:\n  - type: table\n    name: 全部 R5 作品\n    order: [file.name, author, year, r5_priority, r5_tradition, r5_role, axis_t]\n  - type: table\n    name: 核心 ★\n    filters:\n      and:\n        - r5_priority == "★"\n    order: [file.name, author, r5_tradition, r5_role]\n  - type: table\n    name: 按内部传统\n    groupBy:\n      property: r5_tradition\n      direction: ASC\n    order: [file.name, author, year, r5_priority, r5_role]\n''')
cores=[
('01 定义与边界','definition','R5 不是美国文学的同义词，而是美国、加拿大及跨国原住民、非裔、移民与族裔文学共同构成的多中心文学场。'),
('02 历史层与连续性','history','从原住民口传与殖民接触、清教徒与共和国书写、奴隶叙事、十九世纪民族文学，到现代主义、哈莱姆文艺复兴、战后民权与多元文化，再到当代跨国文学。'),
('03 语言文字与媒介','language_media','英语占据主导出版位置，但法语、原住民语言、西班牙语及多语移民写作长期并存；口述、报刊、杂志、小型出版社、大学写作项目和商业出版共同塑造文学场。'),
('04 文学制度与传播','institution','教会与殖民印刷、十九世纪报刊与杂志、废奴出版、哈莱姆期刊、大学与小型出版社、奖项体系和跨国出版集团构成主要制度。'),
('05 阅读路线','reading_route','建议先读原住民与殖民接触，再进入奴隶叙事和十九世纪美国经典，随后读现代主义/哈莱姆、加拿大双语传统、族裔文学与当代跨国写作。')]
for i,(name,dim,body) in enumerate(cores,1): write(f'10 核心结构/{name}.md',fm(f'WL-TOPIC-R5-C{i}','literature_topic_section',dim,i)+f'# {name}\n\n{body}\n')
traditions=[
('01 北美原住民文学传统','口述神话、仪式诗歌、创世叙事、接触书写、寄宿学校记忆、土地与主权叙事以及当代原住民小说/诗歌。'),
('02 殖民地—清教徒与早期共和国文学传统','清教徒日记/布道、殖民见证、革命与共和国政治文体，以及早期美国小说。'),
('03 十九世纪—现代美国文学传统','超验主义、浪漫主义、哥特、现实主义、自然主义、现代主义、南方文学、战后小说与当代主流文学。'),
('04 非裔美国文学传统','奴隶叙事、废奴演说、重建后写作、哈莱姆文艺复兴、民权/黑人艺术运动、黑人女性主义与当代非裔文学。'),
('05 犹太裔美国文学传统','意第绪移民文化、都市现代性、同化与身份、浩劫记忆、战后犹太裔美国小说与当代多重身份。'),
('06 亚裔美国文学传统','排华/移民限制背景、日裔拘禁、华裔/日裔/韩裔/南亚裔等移民经验、代际与语言转换、跨太平洋记忆。'),
('07 拉美裔—奇卡诺美国文学传统','边境、双语、移民、奇卡诺运动、加勒比裔美国经验与拉丁裔都市文学；与 R6 保持跨边境联系。'),
('08 英语加拿大文学传统','殖民与定居、荒野/地域书写、草原与大西洋区域主义、现代主义、战后民族文学、移民和多元文化。'),
('09 法语加拿大—魁北克文学传统','法属殖民记忆、天主教社会、乡土小说、静默革命、现代魁北克戏剧/小说与法语北美身份。')]
for i,(name,body) in enumerate(traditions,1): write(f'11 内部传统/{name}.md',fm(f'WL-TOPIC-R5-T{i}','literature_topic_section','internal_tradition',i)+f'# {name}\n\n{body}\n')
networks=[
('01 定居殖民—原住民接触与反叙事网络','殖民见证、条约、传教、寄宿学校与土地叙事构成持续冲突的文本网络；原住民作品不是美国/加拿大国家叙事的附录。'),
('02 奴隶制—废奴与黑色大西洋网络','奴隶叙事、废奴运动、黑人报刊、宗教修辞和跨大西洋阅读网络共同形成非裔北美文学的早期公共空间。'),
('03 边疆—西部与国家神话网络','边疆神话、拓殖、原住民驱逐、西部小说与反西部书写共同塑造北美国家想象。'),
('04 移民—都市与族裔出版网络','纽约、芝加哥、旧金山、多伦多、蒙特利尔等都市及族裔报刊、小型出版社形成多语移民文学场。'),
('05 哈莱姆—民权与黑人文化运动网络','哈莱姆文艺复兴、民权运动、黑人艺术运动与黑人女性主义构成20世纪非裔文学的关键网络。'),
('06 美加双语—区域主义与跨境网络','英语/法语加拿大、美国—加拿大边境与北美区域主义说明国家边界并非文学传播的唯一尺度。'),
('07 当代跨国—离散与全球出版网络','跨太平洋、跨大西洋、加勒比与拉美迁移使北美文学进入全球英语/法语/西语出版体系，并与 R10 交叉。')]
for i,(name,body) in enumerate(networks,1): write(f'12 跨传统网络/{name}.md',fm(f'WL-TOPIC-R5-N{i}','literature_topic_section','literary_network',i)+f'# {name}\n\n{body}\n')
canvas={'nodes':[], 'edges':[]}
import json
labels=[('root','R5 北美文学')]+[(f't{i}',x[0][3:]) for i,x in enumerate(traditions,1)]+[(f'n{i}',x[0][3:]) for i,x in enumerate(networks,1)]
for idx,(nid,label) in enumerate(labels):
 canvas['nodes'].append({'id':nid,'type':'text','text':label,'x':(idx%5)*340,'y':(idx//5)*220,'width':280,'height':100})
for i in range(1,len(traditions)+1): canvas['edges'].append({'id':f'e{i}','fromNode':'root','toNode':f't{i}'})
for i in range(1,len(networks)+1): canvas['edges'].append({'id':f'en{i}','fromNode':'root','toNode':f'n{i}'})
write('01 北美文学.canvas',json.dumps(canvas,ensure_ascii=False,indent=2))
node=NODE.read_text(encoding='utf-8')
node=node.replace('topic_map: null','topic_map: "[[../../30 专题/R5 北美文学/00 北美文学|R5 北美文学]]"').replace('> 暂未接入。','- [[../../30 专题/R5 北美文学/00 北美文学|R5 北美文学]]\n- [[../../30 专题/R5 北美文学/01 北美文学.canvas|R5 Canvas]]\n- [[../../30 专题/R5 北美文学/03 R5文学作品.base|R5 作品数据库]]')
NODE.write_text(node,encoding='utf-8')
print('R5 topic map built')
