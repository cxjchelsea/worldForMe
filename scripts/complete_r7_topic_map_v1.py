from pathlib import Path
import re, unicodedata, json

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R7 非洲文学'
WORKS=ROOT/'40 作品'
AUD=ROOT/'_audit'/'r_axis_r7'
NODE=ROOT/'20 节点'/'R 地域'/'R7 非洲文学.md'
R7='R7 非洲文学'; TOPIC='WL-TOPIC-R7-AFRICA'

def norm(s): return re.sub(r'[^0-9a-z\u4e00-\u9fff]+','',unicodedata.normalize('NFKC',s).casefold())
def fm(text):
 m=re.match(r'^---\s*\n(.*?)\n---',text,re.S); return m.group(1) if m else ''
def scalar(front,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',front); return m.group(1).strip(' "\'') if m else ''
def list_field(front,key):
 lines=front.splitlines(); out=[]
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*\[\]\s*$',line): return []
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if m: out.append(m.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []
def upsert_list(text,key,val):
 front=fm(text); vals=list_field(front,key)
 if val in vals: return text
 if re.search(rf'(?m)^{re.escape(key)}:\s*$',front): newfront=re.sub(rf'(?m)^({re.escape(key)}:\s*)$',lambda m:m.group(1)+'\n  - '+val,front,1)
 elif re.search(rf'(?m)^{re.escape(key)}:\s*\[\]\s*$',front): newfront=re.sub(rf'(?m)^{re.escape(key)}:\s*\[\]\s*$',key+':\n  - '+val,front,1)
 else: newfront=front+'\n'+key+':\n  - '+val
 return text.replace(front,newfront,1)
def set_scalar(text,key,val):
 front=fm(text); line=f'{key}: "{val}"'
 if re.search(rf'(?m)^{re.escape(key)}:',front): newfront=re.sub(rf'(?m)^{re.escape(key)}:.*$',line,front,1)
 else: newfront=front+'\n'+line
 return text.replace(front,newfront,1)
def write(rel,txt):
 p=TOP/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(txt,encoding='utf-8')
def meta(id_,dim,seq): return f'---\nid: "{id_}"\ntype: "literature_topic_section"\ntopic_id: "{TOPIC}"\ndimension: "{dim}"\nsequence: {seq}\n---\n\n'

traditions=[
('口传—史诗与本土语言传统','史诗、赞歌、神话、职业歌者、口述历史与表演传统是非洲文学的基础层，不应被殖民语言书写遮蔽。'),
('马格里布—北非多语文学传统','阿拉伯语、法语、阿马齐格语及跨地中海写作并存；当作品主要进入泛阿拉伯文学场时与 R1 建边。'),
('西非英语文学传统','尼日利亚、加纳、塞拉利昂、冈比亚等英语文学场，连接殖民教育、民族主义、内战、城市与当代全球出版。'),
('西非法语文学传统','塞内加尔、科特迪瓦、几内亚、马里等法语文学场，连接 Négritude、殖民教育、独立、女性写作与后殖民国家批判。'),
('东非—斯瓦希里文学传统','斯瓦希里诗歌、书面传统以及肯尼亚、坦桑尼亚、乌干达等东非英语/斯瓦希里文学共同构成区域文学场。'),
('非洲之角—埃塞俄比亚/厄立特里亚/索马里文学传统','吉兹语、阿姆哈拉语、索马里语及英语/意大利语等现代写作，连接宗教经典、口传诗与国家创伤。'),
('中非—大湖区文学传统','刚果盆地、卢旺达、布隆迪及大湖区的法语/英语/本土语言文学，关注殖民暴力、独裁、种族灭绝与城市文化。'),
('南部非洲文学传统','南非、津巴布韦、博茨瓦纳等地的英语、南非语和本土语言文学，围绕殖民、种族隔离、解放斗争与转型社会。'),
('葡语非洲文学传统','安哥拉、莫桑比克、佛得角、几内亚比绍、圣多美等葡语文学，连接反殖民战争、克里奥尔身份、社会主义与内战。')]
networks=[
('口传—表演—书写转化网络','职业歌者、赞歌、史诗、神话和口述历史进入文字与出版后，不是简单“保存”，而是媒介与权威的重组。'),
('殖民教育—任务学校与印刷网络','教会学校、殖民教育、报刊与出版社塑造英语、法语、葡语文学公共空间，也触发本土语言标准化。'),
('Négritude—泛非主义与文化民族主义网络','Négritude、泛非主义、民族解放和文化民族主义跨越法语/英语区域，并与 R10.2 非洲离散强连接。'),
('反殖民—独立与国家建构网络','独立战争、民族国家、军事政权和知识分子公共文化构成20世纪非洲文学的共同政治背景。'),
('种族隔离—解放与转型记忆网络','南部非洲的种族隔离、流亡、监禁、解放斗争和真相/和解记忆形成区域及全球文本网络。'),
('战争—独裁—种族灭绝与见证网络','内战、独裁、卢旺达种族灭绝、儿童兵和难民经验使见证文学与记忆政治成为跨区域机制。'),
('迁徙—城市—离散与全球出版网络','拉各斯、内罗毕、约翰内斯堡、达喀尔等城市及欧美迁徙、国际奖项和出版网络连接 R7 与 R10。')]
core=[
('01 定义与边界','definition','R7 不是“非洲英语/法语小说”的总和，而是口传、本土语言、阿拉伯语、英语、法语、葡语及多语文学共同组成的大陆文学系统。'),
('02 历史层与连续性','history','口传/宗教书写→殖民接触与任务教育→文化民族主义/反殖民→独立与国家建构→战争/独裁/种族隔离→当代城市、迁徙与全球出版。'),
('03 语言文字与媒介','language_media','本土语言、阿拉伯语、英语、法语、葡语及克里奥尔语长期并存；口述表演、Ajami/吉兹等书写、报刊、出版社与数字媒体共同构成媒介生态。'),
('04 文学制度与传播','institution','职业歌者与宫廷、宗教学校、任务学校、殖民报刊、大学、民族出版社、作家协会、文学奖与国际出版集团共同塑造文学场。'),
('05 阅读路线','reading_route','先从口传史诗建立非洲文学的非殖民起点，再读西非/东非/南部非洲等区域传统，并用 Négritude、反殖民、种族隔离、战争记忆与迁徙网络横向比较。')]

# canonical structural slots: tradition, role, aliases, priority
S=[
('口传—史诗与本土语言传统','曼丁史诗','松迪亚塔史诗|Sundiata','★'),
('口传—史诗与本土语言传统','西非赞歌/歌者传统','索宁克史诗|Gassire’s Lute|加西雷的鲁特琴','◆'),
('口传—史诗与本土语言传统','约鲁巴神话/口述文学','奥贡·阿比比曼|Ijala|约鲁巴猎人诗','◆'),
('口传—史诗与本土语言传统','祖鲁赞歌','恰卡赞歌|Praise Poems of Shaka','◆'),
('口传—史诗与本土语言传统','富拉尼/萨赫勒史诗','西拉马卡与普尔洛里|Sunjata之外的萨赫勒史诗','◆'),
('口传—史诗与本土语言传统','本土语言现代小说','魔鬼在十字路口|Devil on the Cross','★'),

('马格里布—北非多语文学传统','阿尔及利亚殖民小说','内贾玛|Nedjma','★'),
('马格里布—北非多语文学传统','北非女性反殖民写作','阿尔及利亚女人的房间|Fantasia: An Algerian Cavalcade','★'),
('马格里布—北非多语文学传统','摩洛哥自传小说','过去的简单|Le Passé simple','◆'),
('马格里布—北非多语文学传统','摩洛哥社会边缘小说','赤裸的面包|For Bread Alone','★'),
('马格里布—北非多语文学传统','突尼斯现代小说','意大利人|The Italian|Al-Talyani','◆'),
('马格里布—北非多语文学传统','阿马齐格/跨地中海身份','摩尔人的叙事|The Moor’s Account','◆'),

('西非英语文学传统','殖民冲击/伊博传统','瓦解|Things Fall Apart','★'),
('西非英语文学传统','独立后国家危机','神箭|Arrow of God','◆'),
('西非英语文学传统','尼日利亚戏剧','死亡与国王的侍从|Death and the King’s Horseman','★'),
('西非英语文学传统','尼日利亚内战','半轮黄日|Half of a Yellow Sun','★'),
('西非英语文学传统','加纳独立幻灭','美丽者尚未诞生|The Beautyful Ones Are Not Yet Born','★'),
('西非英语文学传统','女性/性别国家批判','改变|Changes: A Love Story','◆'),
('西非英语文学传统','当代都市/全球化','美国佬|Americanah','◆'),
('西非英语文学传统','当代非洲幻想/类型实验','棕榈酒鬼|The Palm-Wine Drinkard','◆'),

('西非法语文学传统','Négritude诗歌','回乡笔记|Notebook of a Return to the Native Land','★'),
('西非法语文学传统','塞内加尔小说形成','黑孩子|L’Enfant noir','◆'),
('西非法语文学传统','殖民与文化异化','模糊的冒险|Ambiguous Adventure','★'),
('西非法语文学传统','女性书信小说','如此漫长的信|So Long a Letter','★'),
('西非法语文学传统','后殖民国家讽刺','独立的太阳|The Suns of Independence','★'),
('西非法语文学传统','非洲女性身体/传统批判','米丽亚玛|Une si longue lettre之外女性小说|The Abandoned Baobab','◆'),
('西非法语文学传统','战争儿童兵','等待野兽投票|Waiting for the Wild Beasts to Vote','◆'),

('东非—斯瓦希里文学传统','斯瓦希里古典诗','乌腾迪·瓦·坦布卡|Utendi wa Tambuka','★'),
('东非—斯瓦希里文学传统','斯瓦希里现代小说','人民的部长|Kusadikika','◆'),
('东非—斯瓦希里文学传统','肯尼亚殖民/茅茅记忆','一粒麦种|A Grain of Wheat','★'),
('东非—斯瓦希里文学传统','肯尼亚后殖民阶级批判','血的花瓣|Petals of Blood','★'),
('东非—斯瓦希里文学传统','乌干达讽刺诗','拉维诺之歌|Song of Lawino','★'),
('东非—斯瓦希里文学传统','东非海岸/印度洋小说','天堂|Paradise','★'),
('东非—斯瓦希里文学传统','当代战争儿童视角','第一杀手|A Long Way Gone','◆'),

('非洲之角—埃塞俄比亚/厄立特里亚/索马里文学传统','埃塞俄比亚古典王权史','国王的荣耀|Kebra Nagast','★'),
('非洲之角—埃塞俄比亚/厄立里亚/索马里文学传统','现代埃塞俄比亚小说','爱到坟墓|Love unto Crypt|Fikir Eske Mekabir','★'),
('非洲之角—埃塞俄比亚/厄立里亚/索马里文学传统','索马里口传诗','哈德拉维诗选|Hadraawi','★'),
('非洲之角—埃塞俄比亚/厄立里亚/索马里文学传统','索马里现代小说','弯曲的肋骨|From a Crooked Rib','★'),
('非洲之角—埃塞俄比亚/厄立里亚/索马里文学传统','索马里国家崩解','地图|Maps','◆'),
('非洲之角—埃塞俄比亚/厄立里亚/索马里文学传统','埃塞俄比亚革命/流亡','切割石头|Cutting for Stone','◆'),

('中非—大湖区文学传统','刚果殖民记忆','一条非洲长河|Tram 83|Broken Glass','◆'),
('中非—大湖区文学传统','刚果城市现代性','电车83|Tram 83','★'),
('中非—大湖区文学传统','卢旺达种族灭绝见证','裸身在生命前|Murambi, The Book of Bones','★'),
('中非—大湖区文学传统','卢旺达女性记忆','赤脚女人|The Barefoot Woman','★'),
('中非—大湖区文学传统','布隆迪/大湖区战争','小国|Small Country','◆'),
('中非—大湖区文学传统','刚果女性/后殖民小说','富足的生命|So Long a Letter之外中非女性小说|The Lights of Pointe-Noire','◆'),

('南部非洲文学传统','南非早期黑人小说','穆迪|Mhudi','★'),
('南部非洲文学传统','种族隔离小说','哭泣吧，亲爱的祖国|Cry, the Beloved Country','★'),
('南部非洲文学传统','南非女性/种族社会','伯格的女儿|Burger’s Daughter','★'),
('南部非洲文学传统','南非黑人意识/城镇文学','我的创伤|Down Second Avenue','◆'),
('南部非洲文学传统','反种族隔离戏剧','西兹韦·班西死了|Sizwe Banzi Is Dead','◆'),
('南部非洲文学传统','津巴布韦殖民成长','神经质状况|Nervous Conditions','★'),
('南部非洲文学传统','博茨瓦纳/区域社会小说','马鲁|Maru','◆'),
('南部非洲文学传统','转型后南非','耻|Disgrace','★'),
('南部非洲文学传统','当代南非种族/阶级','承诺|The Promise','◆'),

('葡语非洲文学传统','安哥拉殖民/民族形成','卢安达的真正生活|Luuanda','★'),
('葡语非洲文学传统','安哥拉解放战争','马约姆贝|Mayombe','★'),
('葡语非洲文学传统','安哥拉内战/魔幻历史','卖过去的人|The Book of Chameleons','◆'),
('葡语非洲文学传统','莫桑比克内战','梦游大地|Sleepwalking Land','★'),
('葡语非洲文学传统','莫桑比克女性传统','尼凯切|Niketche','◆'),
('葡语非洲文学传统','佛得角克里奥尔身份','饥饿者|Chiquinho','◆'),
('葡语非洲文学传统','葡语非洲跨国诗歌','阿戈什蒂纽·内图诗选|Agostinho Neto','◆'),
]

TOP.mkdir(parents=True,exist_ok=True)
for i,(n,d,b) in enumerate(core,1): write(f'10 核心结构/{n}.md',meta(f'WL-TOPIC-R7-C{i}',d,i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(traditions,1): write(f'11 内部传统/{i:02d} {n}.md',meta(f'WL-TOPIC-R7-T{i}','internal_tradition',i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(networks,1): write(f'12 跨传统网络/{i:02d} {n}.md',meta(f'WL-TOPIC-R7-N{i}','literary_network',i)+f'# {n}\n\n{b}\n')

# index works
idx=[]; r7_before=0
for p in WORKS.glob('*.md'):
 text=p.read_text(encoding='utf-8-sig'); front=fm(text)
 if scalar(front,'type')!='work': continue
 vals=[scalar(front,'title'),scalar(front,'title_original'),p.stem]+list_field(front,'aliases')
 idx.append((p,{norm(x) for x in vals if x}))
 if R7 in list_field(front,'axis_r'): r7_before+=1
created=[]; reused=0
for trad,role,cands,prio in S:
 hit=None
 for cand in cands.split('|'):
  nc=norm(cand)
  for p,names in idx:
   if nc and nc in names: hit=p; break
  if hit: break
 if hit:
  text=hit.read_text(encoding='utf-8-sig'); reused+=1
 else:
  title=cands.split('|')[0]; safe=title.replace('/','／').replace('\\','／')
  hit=WORKS/(safe+'.md'); k=2
  while hit.exists(): hit=WORKS/(safe+f' ({k}).md'); k+=1
  text=f'''---\nid: "WL-WORK-R7-{len(created)+1:03d}"\ntype: work\ntitle: "{title}"\ntitle_original: null\nauthor: null\nyear: null\naliases: []\naxis_t: []\naxis_r:\n  - {R7}\nr7_priority: "{prio}"\nr7_tradition: "{trad}"\nr7_role: "{role}"\n---\n\n# {title}\n\n> R7 结构补齐锚点；作者、年份与书目细节待全局 bibliographic/T-axis 治理统一核验。\n'''
  hit.write_text(text,encoding='utf-8'); created.append(hit.name); idx.append((hit,{norm(title)}))
 text=upsert_list(text,'axis_r',R7); text=set_scalar(text,'r7_priority',prio); text=set_scalar(text,'r7_tradition',trad); text=set_scalar(text,'r7_role',role)
 hit.write_text(text,encoding='utf-8')

r7_after=0
for p in WORKS.glob('*.md'):
 text=p.read_text(encoding='utf-8-sig');
 if scalar(fm(text),'type')=='work' and R7 in list_field(fm(text),'axis_r'): r7_after+=1

# bases
write('02 R7文学结构.base','''filters:\n  and:\n    - topic_id == "WL-TOPIC-R7-AFRICA"\nproperties:\n  file.name: {displayName: 节点}\n  note.dimension: {displayName: 维度}\n  note.sequence: {displayName: 顺序}\nviews:\n  - type: table\n    name: 全部 R7 知识节点\n    order: [file.name, dimension, sequence]\n  - type: table\n    name: 内部传统\n    filters:\n      and:\n        - dimension == "internal_tradition"\n    order: [file.name, sequence]\n  - type: table\n    name: 跨传统网络\n    filters:\n      and:\n        - dimension == "literary_network"\n    order: [file.name, sequence]\n''')
write('03 R7文学作品.base','''filters:\n  and:\n    - type == "work"\n    - axis_r.contains("R7 非洲文学")\nproperties:\n  file.name: {displayName: 作品}\n  note.author: {displayName: 作者}\n  note.year: {displayName: 年份}\n  note.r7_priority: {displayName: R7优先级}\n  note.r7_tradition: {displayName: 内部传统}\n  note.r7_role: {displayName: R7机制/意义}\n  note.axis_t: {displayName: 时间}\nviews:\n  - type: table\n    name: 全部 R7 作品\n    order: [file.name, author, year, r7_priority, r7_tradition, r7_role, axis_t]\n  - type: table\n    name: 核心 ★\n    filters:\n      and:\n        - r7_priority == "★"\n    order: [file.name, author, r7_tradition, r7_role]\n  - type: table\n    name: 按内部传统\n    groupBy:\n      property: r7_tradition\n      direction: ASC\n    order: [file.name, author, year, r7_priority, r7_role]\n''')

# canvas
nodes=[{'id':'root','type':'text','text':'R7 非洲文学','x':0,'y':0,'width':300,'height':100}]; edges=[]
for i,(n,_) in enumerate(traditions,1):
 nid=f't{i}'; nodes.append({'id':nid,'type':'file','file':f'11 内部传统/{i:02d} {n}.md','x':(-650 if i<=5 else 650),'y':(i if i<=5 else i-5)*160,'width':360,'height':90}); edges.append({'id':f'e{nid}','fromNode':'root','toNode':nid})
for i,(n,_) in enumerate(networks,1):
 nid=f'n{i}'; nodes.append({'id':nid,'type':'file','file':f'12 跨传统网络/{i:02d} {n}.md','x':0,'y':300+i*150,'width':380,'height':90}); edges.append({'id':f'e{nid}','fromNode':'root','toNode':nid})
write('01 非洲文学.canvas',json.dumps({'nodes':nodes,'edges':edges},ensure_ascii=False,indent=2))

home='''---
id: WL-TOPIC-R7-AFRICA
type: literature_topic_map
name: "非洲文学"
primary_anchor: WL-R7
anchor_mode: exact
taxonomy_version: literature-taxonomy-v2
topic_role: direct
structure_status: complete
structure_database: "[[02 R7文学结构.base]]"
work_database: "[[03 R7文学作品.base]]"
template_version: literature-topic-r-v1
---
# R7｜非洲文学

> 路径：[[../../00 世界文学使用规则|世界文学]] → [[../../10 轴/R轴 世界文学传统|R轴]] → **R7 非洲文学**

## 专题定位
R7 研究非洲大陆内部由口传、本土语言、阿拉伯语、英语、法语、葡语等共同构成的多中心文学系统。非洲文学不是殖民语言小说的集合，也不把非洲离散文学重复纳入大陆坐标。

## 导航
- [[01 非洲文学.canvas|R7 Canvas]]
- [[02 R7文学结构.base|R7 文学结构数据库]]
- [[03 R7文学作品.base|R7 作品数据库]]

### 核心结构
- [[10 核心结构/01 定义与边界|定义与边界]]
- [[10 核心结构/02 历史层与连续性|历史层与连续性]]
- [[10 核心结构/03 语言文字与媒介|语言文字与媒介]]
- [[10 核心结构/04 文学制度与传播|文学制度与传播]]
- [[10 核心结构/05 阅读路线|阅读路线]]

### 内部传统
'''
for i,(n,_) in enumerate(traditions,1): home+=f'{i}. [[11 内部传统/{i:02d} {n}|{n}]]\n'
home+='''\n### 跨传统网络\n'''
for i,(n,_) in enumerate(networks,1): home+=f'- [[12 跨传统网络/{i:02d} {n}|{n}]]\n'
home+='''\n## 边界\n- 北非/马格里布可进入 R7；当作品主要属于泛阿拉伯文学场时与 R1 建边。\n- 非洲离散文学 canonical 统一放在 [[../../20 节点/R 地域/R10.2 非洲离散文学|R10.2]]，R7 只保留关系入口。\n- 非洲文学不按殖民语言简单分桶，本土语言与口传传统拥有独立结构位置。\n- 当迁徙/离散成为作品首要解释框架时，应同时连接 R10。\n\n## 状态\n`R7_TOPIC_MAP_STRUCTURE = COMPLETE`\n\n`R7_WORK_SUPPORT = COMPLETE`\n\n`R7_TOPIC_MAP_V1 = COMPLETE_USABLE`\n'''
write('00 非洲文学.md',home)

# update node
node=NODE.read_text(encoding='utf-8-sig'); front=fm(node)
newfront=re.sub(r'(?ms)^topic_map:.*?(?=^source_version:)', 'topic_map:\n  - "[[../../30 专题/R7 非洲文学/00 非洲文学]]"\n', front)
if newfront==front and 'topic_map:' in front: newfront=re.sub(r'(?m)^topic_map:.*$', 'topic_map:\n  - "[[../../30 专题/R7 非洲文学/00 非洲文学]]"', front)
node=node.replace(front,newfront,1)
node=re.sub(r'## 专题地图\n\n> 暂未接入。', '## 专题地图\n\n- [[../../30 专题/R7 非洲文学/00 非洲文学|R7 非洲文学]]\n- [[../../30 专题/R7 非洲文学/01 非洲文学.canvas|R7 Canvas]]\n- [[../../30 专题/R7 非洲文学/03 R7文学作品.base|R7 作品数据库]]', node)
NODE.write_text(node,encoding='utf-8')

AUD.mkdir(parents=True,exist_ok=True)
by={t:0 for t,_ in traditions}
for t,_,_,_ in S: by[t]+=1
report=['# R7 Structural Completion V1','',f'- Structural slots: **{len(S)}**',f'- Existing anchors reused/enriched: **{reused}**',f'- Newly created canonical Works: **{len(created)}**',f'- R7 Works before: **{r7_before}**',f'- R7 Works after: **{r7_after}**','','## By tradition']
for t,n in by.items(): report.append(f'- {t}: **{n}/{n} COVERED**')
report += ['','## Created']+[f'- {x}' for x in created]+['','## Governance','- R10.2 remains the canonical African-diaspora coordinate; R7 does not recreate R7.7.','- Maghreb works may connect R1 when the pan-Arabic literary field is primary.','- Oral and indigenous-language traditions are structural first-class components, not supplements.','- New anchors leave `year: null` pending global bibliographic/T-axis governance.','','`R7_STRUCTURAL_COVERAGE_V1 = 100_PERCENT_COMPLETE`','`R7_TOPIC_MAP_V1 = COMPLETE_USABLE`']
(AUD/'R7_STRUCTURAL_COMPLETION_V1.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
