from pathlib import Path
import json

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R4 欧洲文学'
NODE=ROOT/'20 节点'/'R 地域'/'R4 欧洲文学.md'
TOPIC='WL-TOPIC-R4-EUROPE'

CORE=[
('01 定义与边界','definition','R4 不是“欧洲国家文学大全”。它从中世纪拉丁基督教、多种俗语文学与宫廷/城市文化的并存出发，解释欧洲文学如何形成相互翻译、竞争和分化的多中心体系。古希腊与古罗马的主坐标仍在 R1；R4 只讨论它们作为后世经典资源的再接受。'),
('02 历史层与连续性','history','从中世纪拉丁与俗语文学、文艺复兴与宗教改革、17世纪宫廷/城市文化、启蒙与公共领域、浪漫主义与民族文学、19世纪现实主义，到现代主义、战争经验、冷战和当代欧洲文学。R4 的时间层用于解释传统自身变化，不替代 T 轴。'),
('03 语言文字与媒介','language_media','拉丁语长期作为跨区域学术与宗教语言；英语、法语、意大利语、西班牙语、葡萄牙语、德语、荷兰语、北欧语言、斯拉夫语言、匈牙利语、现代希腊语等逐步形成各自书写共同体。手稿、印刷、报刊、出版社、翻译和大众教育不断改变文学公共性。'),
('04 文学制度与传播','institution','修道院与教会学校、大学、宫廷赞助、城市书商、剧院、沙龙、咖啡馆、报刊、出版社、文学奖和跨国翻译市场共同塑造欧洲文学。现代“国民文学”只是其中一个阶段。'),
('05 阅读路线','reading_route','建议先从《神曲》、乔叟、塞万提斯、莎士比亚、莫里哀/拉辛、歌德、简·奥斯汀、巴尔扎克、托尔斯泰/陀思妥耶夫斯基、易卜生、卡夫卡、乔伊斯/伍尔夫、普鲁斯特等骨架进入，再按内部传统和跨区域网络扩展。')]
TRADS=[
('01 中世纪拉丁基督教与俗语奠基传统','中世纪拉丁基督教与俗语奠基传统','中世纪拉丁诗文、圣徒传、骑士叙事、城市与宫廷俗语文学，以及古典资源的基督教化重读。'),
('02 英国—爱尔兰文学传统','英国—爱尔兰文学传统','古英语/中古英语、乔叟、莎士比亚、英国小说、浪漫主义、维多利亚文学、爱尔兰复兴与现代主义，以及战后和当代写作。'),
('03 法语文学传统','法语文学传统','中世纪法语、古典主义戏剧、启蒙、浪漫主义、现实主义/自然主义、象征主义、现代主义与法语世界的欧洲核心传统。'),
('04 意大利文学传统','意大利文学传统','但丁—彼特拉克—薄伽丘的人文主义奠基、文艺复兴史诗与戏剧、近代语言统一、现实主义/现代主义及战后文学。'),
('05 伊比利亚文学传统','伊比利亚文学传统','西班牙与葡萄牙及半岛多语文学：史诗、骑士文学、黄金时代戏剧与小说、葡萄牙史诗、19世纪转型、现代主义和内战/独裁经验。'),
('06 德语文学传统','德语文学传统','中古德语、宗教改革书写、启蒙、狂飙突进与古典主义、浪漫主义、现实主义、维也纳/德语现代主义以及战后德语文学。'),
('07 低地国家文学传统','低地国家文学传统','荷兰语与弗拉芒文学，从中世纪城市文化、黄金时代到现代殖民反思、战争记忆与当代写作。'),
('08 北欧文学传统','北欧文学传统','冰岛萨迦与古诺斯诗歌、丹麦/挪威/瑞典/芬兰等现代文学，易卜生、斯特林堡及北欧现代主义和社会小说。'),
('09 俄罗斯文学传统','俄罗斯文学传统','古罗斯宗教/编年传统、普希金以来的现代文学、19世纪小说高峰、白银时代、革命与苏联文学、流亡和后苏联文学。'),
('10 中欧文学传统','中欧文学传统','波兰、捷克、匈牙利及多语哈布斯堡空间；浪漫民族文化、现实主义、现代主义、战争/极权经验与异议文学。'),
('11 巴尔干与东南欧文学传统','巴尔干与东南欧文学传统','南斯拉夫及其继承地区、罗马尼亚、保加利亚、阿尔巴尼亚等多语文学，帝国边界、民族建构、战争和记忆构成核心问题。'),
('12 现代希腊文学传统','现代希腊文学传统','拜占庭之后的希腊语文学、克里特文艺复兴、民族独立、语言问题、现代诗歌与20世纪希腊文学。')]
NETS=[
('01 拉丁基督教—大学与手稿网络','拉丁基督教、大学与手稿使文本跨越王国边界，形成共同的学术、神学与修辞资源。'),
('02 印刷—宗教改革与俗语标准化网络','印刷、宗教改革和圣经翻译推动俗语标准化，扩大读者并重组作者—出版—公共领域关系。'),
('03 文艺复兴—古典复兴与人文主义网络','意大利人文主义、古典文本再发现与翻译扩散到欧洲各地，推动戏剧、诗学、政治书写和教育改革。'),
('04 启蒙—沙龙报刊与共和国书信网络','法语等跨区域文化语言、沙龙、期刊、百科全书和书信共和国形成18世纪欧洲公共讨论空间。'),
('05 浪漫主义—民族文学与民间传统网络','浪漫主义把民歌、史诗、神话和语言研究转化为民族文学工程，同时形成高度跨国的审美运动。'),
('06 现实主义—自然主义与都市出版网络','19世纪小说、报刊连载、城市读者和跨国翻译让现实主义/自然主义成为欧洲级形式网络。'),
('07 现代主义跨城市网络','巴黎、伦敦、都柏林、维也纳、布拉格、柏林、圣彼得堡等城市通过杂志、翻译、流亡与先锋艺术形成现代主义网络。'),
('08 战争—流亡—极权与记忆网络','两次世界大战、革命、法西斯主义、纳粹主义、共产主义和流亡重塑欧洲文学的证言、记忆和身份问题。')]

def write(path,content):
 path.parent.mkdir(parents=True,exist_ok=True); path.write_text(content,encoding='utf-8')

def front(id_,typ,dim,seq):
 return f'---\nid: "{id_}"\ntype: "{typ}"\ntopic_id: "{TOPIC}"\ndimension: "{dim}"\nsequence: {seq}\n---\n\n'

def main():
 TOP.mkdir(parents=True,exist_ok=True)
 overview='''---\nid: WL-TOPIC-R4-EUROPE\ntype: literature_topic_map\nname: "欧洲文学"\nprimary_anchor: WL-R4\nanchor_mode: exact\ntaxonomy_version: literature-taxonomy-v2\ntopic_role: direct\nstructure_status: active\nstructure_database: "[[02 R4文学结构.base]]"\nwork_database: "[[03 R4文学作品.base]]"\ntemplate_version: literature-topic-r-v1\n---\n# R4｜欧洲文学\n\n> 路径：[[../../00 世界文学使用规则|世界文学]] → [[../../10 轴/R轴 世界文学传统|R轴]] → **R4 欧洲文学**\n\n## 专题定位\nR4 研究中世纪以来欧洲多语文学体系的形成、分化与跨国互动。古希腊/古罗马的主传统属于 R1；它们在 R4 中主要作为经典接受和再写资源。\n\n## 核心问题\n> **欧洲文学如何从拉丁基督教与地方俗语并存的中世纪世界，发展为现代多民族、多语言又高度互译互通的文学体系？**\n\n## 导航\n- [[01 欧洲文学.canvas|R4 Canvas]]\n- [[02 R4文学结构.base|R4 文学结构数据库]]\n- [[03 R4文学作品.base|R4 作品数据库]]\n\n### 核心结构\n- [[10 核心结构/01 定义与边界|定义与边界]]\n- [[10 核心结构/02 历史层与连续性|历史层与连续性]]\n- [[10 核心结构/03 语言文字与媒介|语言文字与媒介]]\n- [[10 核心结构/04 文学制度与传播|文学制度与传播]]\n- [[10 核心结构/05 阅读路线|阅读路线]]\n\n### 内部传统\n'''
 for i,(fn,name,desc) in enumerate(TRADS,1): overview+=f'{i}. [[11 内部传统/{fn}|{name}]]\n'
 overview+='\n### 跨传统网络\n'
 for fn,desc in NETS: overview+=f'- [[12 跨传统网络/{fn}|{fn[3:]}]]\n'
 overview+='''\n## 边界\n- 古希腊/古罗马主坐标在 R1；R4 处理其后世接受。\n- 俄罗斯归入 R4 是地图管理选择，不否认其欧亚性质。\n- 殖民地与离散作品按主要文学场判断；跨区域身份成为主框架时同时连接 R10。\n- 欧洲内部传统不升级为全局 R 子坐标。\n\n## 状态\n`R4_TOPIC_MAP_STRUCTURE = ACTIVE`\n'''
 write(TOP/'00 欧洲文学.md',overview)
 structure='''filters:\n  and:\n    - topic_id == "WL-TOPIC-R4-EUROPE"\nproperties:\n  file.name:\n    displayName: 节点\n  note.dimension:\n    displayName: 维度\n  note.sequence:\n    displayName: 顺序\nviews:\n  - type: table\n    name: 全部 R4 知识节点\n    order: [file.name, dimension, sequence]\n  - type: table\n    name: 内部传统\n    filters:\n      and:\n        - dimension == "internal_tradition"\n    order: [file.name, sequence]\n  - type: table\n    name: 跨传统网络\n    filters:\n      and:\n        - dimension == "literary_network"\n    order: [file.name, sequence]\n'''
 write(TOP/'02 R4文学结构.base',structure)
 works='''filters:\n  and:\n    - type == "work"\n    - axis_r.contains("R4 欧洲文学")\nproperties:\n  file.name: {displayName: 作品}\n  note.author: {displayName: 作者}\n  note.year: {displayName: 年份}\n  note.r4_priority: {displayName: R4优先级}\n  note.r4_tradition: {displayName: 内部传统}\n  note.r4_role: {displayName: R4机制/意义}\n  note.axis_t: {displayName: 时间}\n  note.read_status: {displayName: 阅读状态}\nviews:\n  - type: table\n    name: 全部 R4 作品\n    order: [file.name, author, year, r4_priority, r4_tradition, r4_role, axis_t]\n  - type: table\n    name: 核心 ★\n    filters:\n      and:\n        - r4_priority == "★"\n    order: [file.name, author, year, r4_tradition, r4_role]\n  - type: table\n    name: 按内部传统\n    groupBy: {property: r4_tradition, direction: ASC}\n    order: [file.name, author, year, r4_priority, r4_role]\n'''
 write(TOP/'03 R4文学作品.base',works)
 for i,(fn,dim,text) in enumerate(CORE,1): write(TOP/'10 核心结构'/f'{fn}.md',front(f'WL-TOPIC-R4-CORE-{i:02d}','literature_topic_section',dim,i)+f'# {fn}\n\n{text}\n')
 for i,(fn,name,desc) in enumerate(TRADS,1): write(TOP/'11 内部传统'/f'{fn}.md',front(f'WL-TOPIC-R4-TRAD-{i:02d}','literature_topic_section','internal_tradition',i)+f'# {name}\n\n{desc}\n')
 for i,(fn,desc) in enumerate(NETS,1): write(TOP/'12 跨传统网络'/f'{fn}.md',front(f'WL-TOPIC-R4-NET-{i:02d}','literature_topic_section','literary_network',i)+f'# {fn[3:]}\n\n{desc}\n')
 # canvas
 nodes=[]; edges=[]; y=0
 nodes.append({'id':'root','type':'file','file':'00 欧洲文学.md','x':0,'y':0,'width':320,'height':120})
 for i,(fn,name,_) in enumerate(TRADS,1):
  nid=f't{i}'; nodes.append({'id':nid,'type':'file','file':f'11 内部传统/{fn}.md','x':450+((i-1)%3)*360,'y':-700+((i-1)//3)*220,'width':300,'height':100}); edges.append({'id':f'e{i}','fromNode':'root','toNode':nid})
 for i,(fn,_) in enumerate(NETS,1):
  nid=f'n{i}'; nodes.append({'id':nid,'type':'file','file':f'12 跨传统网络/{fn}.md','x':-900+((i-1)%2)*350,'y':-650+((i-1)//2)*210,'width':300,'height':100}); edges.append({'id':f'en{i}','fromNode':'root','toNode':nid})
 write(TOP/'01 欧洲文学.canvas',json.dumps({'nodes':nodes,'edges':edges},ensure_ascii=False,indent=2))
 node=NODE.read_text(encoding='utf-8')
 node=node.replace('topic_map: null','topic_map: "[[../../30 专题/R4 欧洲文学/00 欧洲文学|R4 欧洲文学]]"')
 node=node.replace('> 暂未接入。','- [[../../30 专题/R4 欧洲文学/00 欧洲文学|R4 欧洲文学]]\n- [[../../30 专题/R4 欧洲文学/01 欧洲文学.canvas|R4 Canvas]]\n- [[../../30 专题/R4 欧洲文学/03 R4文学作品.base|R4 作品数据库]]')
 NODE.write_text(node,encoding='utf-8')
 print('R4 topic map built')
if __name__=='__main__': main()
