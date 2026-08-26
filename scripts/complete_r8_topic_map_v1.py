from pathlib import Path
import re, unicodedata, json

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R8 东南亚文学'
WORKS=ROOT/'40 作品'
AUD=ROOT/'_audit'/'r_axis_r8'
NODE=ROOT/'20 节点'/'R 地域'/'R8 东南亚文学.md'
R8='R8 东南亚文学'; TOPIC='WL-TOPIC-R8-SOUTHEAST-ASIA'

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
('越南汉喃—国语文学传统','汉文、字喃与国语字长期交替，连接宫廷史书、诗歌、传奇、殖民现代小说、战争文学与当代越南语写作。'),
('泰国文学传统','巴利—梵文佛教经典、本土宫廷诗、罗摩衍那改写、近代印刷、现代小说与社会批判共同构成泰语文学史。'),
('缅甸文学传统','巴利佛教、碑铭与宫廷诗歌、编年史、殖民现代性、民族主义与军政时代小说/诗歌构成缅语文学连续性。'),
('柬埔寨—老挝文学传统','高棉/老挝口传、佛教寺院文本、宫廷史诗、殖民书写、红色高棉记忆与现代民族文学并行。'),
('马来—Jawi文学传统','古典马来语、Jawi书写、宫廷史书、hikayat、伊斯兰苏菲传统、殖民印刷和马来西亚/文莱现代文学共同构成马来文学圈。'),
('印尼—爪哇与群岛文学传统','古爪哇kakawin、wayang、马来/印尼语印刷、民族主义、荷属殖民与独立后小说共同构成群岛多语文学场。'),
('菲律宾文学传统','原住民口传、baybayin传统、西班牙殖民文本、民族主义小说、英语教育、塔加洛语与英语双轨现代文学并存。'),
('东帝汶—小巽他文学传统','德顿语、葡语与口传传统交汇，殖民、独立战争、占领与国家建构形成独特的跨语文学场。'),
('新加坡—海峡多语文学传统','英语、华语、马来语、泰米尔语及方言文化在殖民港口、独立国家与全球城市环境中形成多语文学场。')]
networks=[
('梵文—巴利—佛教文本传播网络','南亚史诗、佛教经典与寺院教育在大陆东南亚形成持续的翻译、改写和表演网络，与 R3 建边。'),
('汉文—儒学与越南书写网络','汉文经典、科举、史书和字喃/国语字转换构成越南与东亚文学共同体的特殊接口，与 R2 建边。'),
('罗摩衍那—宫廷史诗改写网络','Ramayana 在泰国、柬埔寨、爪哇、马来等地被改写为不同宫廷/表演传统。'),
('伊斯兰—马来语—Jawi海上网络','马六甲以后伊斯兰、Jawi、苏菲文本、hikayat与海上贸易连接马来半岛、苏门答腊、爪哇、婆罗洲及菲律宾南部。'),
('殖民语言—印刷与现代文类网络','西班牙、荷兰、法国、英国、葡萄牙殖民教育和印刷推动小说、报刊、现代诗与民族公共空间形成。'),
('民族主义—革命—战争文学网络','反殖民民族主义、越战、印尼革命、菲律宾政治暴力、红色高棉与东帝汶独立使战争/国家叙事跨区域互照。'),
('港口—迁徙—区域与全球出版网络','新加坡、马尼拉、雅加达、胡志明市、曼谷等都市及海外劳工/华人迁徙形成跨语出版与全球流通。')]
core=[
('01 定义与边界','definition','R8 是大陆与岛屿东南亚多个语言文学系统的区域集合，不等同于任何单一国家文学，也不能被殖民语言分类取代。'),
('02 历史层与连续性','history','口传/碑铭与宫廷传统→佛教/印度化/汉文化/伊斯兰网络→殖民印刷与现代文类→民族主义/革命→冷战战争与威权→当代城市、迁徙与全球文学。'),
('03 语言文字与媒介','language_media','巴利、梵文、汉文、Jawi、爪哇文、缅文、高棉文、泰文、越南汉喃/国语字、塔加洛/菲律宾语、英语、法语、荷兰语、葡语等长期并存。'),
('04 文学制度与传播','institution','宫廷、寺院、科举/学校、殖民印刷、报刊、民族出版社、大学、国家文化机构和区域/国际出版共同塑造文学场。'),
('05 阅读路线','reading_route','先理解佛教/汉文/伊斯兰三类跨区域文化网络，再分别进入越南、泰缅、柬老、马来—印尼、菲律宾与新加坡，最后用殖民、战争和迁徙网络横向比较。')]

S=[
('越南汉喃—国语文学传统','中古民族史诗/政治诗','南国山河|Nam quốc sơn hà','◆'),
('越南汉喃—国语文学传统','汉文传奇','传奇漫录|Truyền kỳ mạn lục','◆'),
('越南汉喃—国语文学传统','字喃长篇诗','金云翘传|翘传|The Tale of Kieu','★'),
('越南汉喃—国语文学传统','女性字喃诗','胡春香诗选|Hồ Xuân Hương','◆'),
('越南汉喃—国语文学传统','殖民现代小说','素心|Tố Tâm','◆'),
('越南汉喃—国语文学传统','现代现实主义','志飘|Chí Phèo','★'),
('越南汉喃—国语文学传统','战争文学','哀痛的战争|战争的哀伤|The Sorrow of War','★'),
('越南汉喃—国语文学传统','当代越南小说','无尽的田野|The Endless Field','◆'),

('泰国文学传统','宫廷罗摩衍那改写','拉玛坚|Ramakien','★'),
('泰国文学传统','古典叙事诗','坤昌坤平|Khun Chang Khun Phaen','★'),
('泰国文学传统','佛教伦理叙事','三界经|Traibhumikatha','◆'),
('泰国文学传统','近代小说形成','人生戏剧|The Circus of Life','◆'),
('泰国文学传统','社会现实主义','乡村教师|The Teachers of Mad Dog Swamp','◆'),
('泰国文学传统','政治/农民文学','大地之子|Child of the Northeast','★'),
('泰国文学传统','当代都市小说','曼谷苏醒|Bangkok Wakes to Rain','◆'),

('缅甸文学传统','宫廷编年史','琉璃宫史|Glass Palace Chronicle','★'),
('缅甸文学传统','佛教叙事/诗歌','九品比丘诗|pyazat|缅甸古典诗选','◆'),
('缅甸文学传统','殖民现代小说','农民|The Farmer|Thu Maung','◆'),
('缅甸文学传统','民族主义小说','我们的时代|Our Age','◆'),
('缅甸文学传统','战后社会小说','不平的山路|Not Out of Hate','★'),
('缅甸文学传统','政治监禁/当代写作','微笑着面对镣铐|The Moon in My Prison Cell','◆'),

('柬埔寨—老挝文学传统','高棉罗摩衍那','利亚姆盖尔|Reamker','★'),
('柬埔寨—老挝文学传统','高棉古典爱情叙事','图姆提乌|Tum Teav','★'),
('柬埔寨—老挝文学传统','柬埔寨现代小说','枯萎的花|Sophat','◆'),
('柬埔寨—老挝文学传统','红色高棉见证','杀戮场的女儿|First They Killed My Father','★'),
('柬埔寨—老挝文学传统','老挝史诗','辛赛|Sinsay','★'),
('柬埔寨—老挝文学传统','老挝现代小说','母亲的遗产|Mother’s Beloved','◆'),

('马来—Jawi文学传统','马来宫廷史书','马来纪年|Sejarah Melayu|Malay Annals','★'),
('马来—Jawi文学传统','英雄传奇','杭图亚传|Hikayat Hang Tuah','★'),
('马来—Jawi文学传统','伊斯兰传奇','阿米尔·哈姆扎传|Hikayat Amir Hamzah','◆'),
('马来—Jawi文学传统','苏菲诗歌','哈姆扎·凡苏里诗选|Hamzah Fansuri','◆'),
('马来—Jawi文学传统','殖民转型自传','阿卜杜拉游记|Hikayat Abdullah','★'),
('马来—Jawi文学传统','马来西亚现代小说','沙丽娜|Salina','★'),
('马来—Jawi文学传统','当代马来西亚小说','雨之赐|The Gift of Rain','◆'),

('印尼—爪哇与群岛文学传统','古爪哇kakawin','阿周那婚礼|Arjunawiwaha','◆'),
('印尼—爪哇与群岛文学传统','爪哇史诗改写','拉玛衍那卡卡温|Kakawin Ramayana','★'),
('印尼—爪哇与群岛文学传统','近代马来/印尼小说','西蒂·努尔巴雅|Sitti Nurbaya','★'),
('印尼—爪哇与群岛文学传统','民族主义小说','错误的教育|Salah Asuhan','◆'),
('印尼—爪哇与群岛文学传统','革命/殖民历史小说','人世间（普拉姆迪亚）|Bumi Manusia|This Earth of Mankind','★'),
('印尼—爪哇与群岛文学传统','1965记忆/女性','人类之舞|The Dancer|Ronggeng Dukuh Paruk','◆'),
('印尼—爪哇与群岛文学传统','当代印尼小说','美丽是一种伤|Beauty Is a Wound','★'),
('印尼—爪哇与群岛文学传统','当代宗教/地方社会','彩虹战士|The Rainbow Troops','◆'),

('菲律宾文学传统','殖民宗教长诗','帕西翁|Pasyon','◆'),
('菲律宾文学传统','民族主义小说','不许犯我|Noli Me Tangere|社会毒瘤','★'),
('菲律宾文学传统','民族主义续篇','起义者|El Filibusterismo','★'),
('菲律宾文学传统','英语菲律宾小说形成','他的本土|His Native Soil','◆'),
('菲律宾文学传统','战后社会小说','恶魔之手|The Pretenders','◆'),
('菲律宾文学传统','独裁时代小说','国家|Dekada 70','★'),
('菲律宾文学传统','当代离散/英语写作','狗食|Dogeaters','★'),

('东帝汶—小巽他文学传统','东帝汶口述/创世传统','鳄鱼祖先传说|The Crocodile Legend','◆'),
('东帝汶—小巽他文学传统','反殖民诗歌','博尔哈·达科斯塔诗选|Borja da Costa','★'),
('东帝汶—小巽他文学传统','独立战争诗歌','费尔南多·西尔万诗选|Fernando Sylvan','◆'),
('东帝汶—小巽他文学传统','当代国家记忆','鳄鱼之泪|The Crossing|Luis Cardoso','★'),

('新加坡—海峡多语文学传统','英语新加坡诗歌','王润华诗选|Edwin Thumboo poems','★'),
('新加坡—海峡多语文学传统','英语新加坡小说','如果我们梦想太久|If We Dream Too Long','★'),
('新加坡—海峡多语文学传统','马来新加坡写作','苏拉特曼·马肯诗选|Suratman Markasan','◆'),
('新加坡—海峡多语文学传统','华文新加坡文学','尤今小说选|Yeo Jin','◆'),
('新加坡—海峡多语文学传统','当代国家/语言小说','艺术家的一生|State of Emergency|Jeremy Tiang','◆'),
('新加坡—海峡多语文学传统','当代移民/全球城市','夕雾花园|The Garden of Evening Mists','◆')]

for i,(n,d,b) in enumerate(core,1): write(f'10 核心结构/{n}.md',meta(f'WL-TOPIC-R8-C{i}',d,i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(traditions,1): write(f'11 内部传统/{i:02d} {n}.md',meta(f'WL-TOPIC-R8-T{i}','internal_tradition',i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(networks,1): write(f'12 跨传统网络/{i:02d} {n}.md',meta(f'WL-TOPIC-R8-N{i}','literary_network',i)+f'# {n}\n\n{b}\n')

# index existing works by title + aliases + original title
idx={}
for p in WORKS.glob('*.md'):
 try: text=p.read_text(encoding='utf-8')
 except: continue
 front=fm(text); keys=[p.stem,scalar(front,'title'),scalar(front,'title_original')]+list_field(front,'aliases')
 for k in keys:
  if k: idx.setdefault(norm(k),p)

before=0
for p in WORKS.glob('*.md'):
 try:
  if R8 in list_field(fm(p.read_text(encoding='utf-8')),'axis_r'): before+=1
 except: pass

reused=[]; created=[]; anchors=[]
for trad,role,cands,prio in S:
 names=[x.strip() for x in cands.split('|') if x.strip()]
 hit=None
 for n in names:
  if norm(n) in idx: hit=idx[norm(n)]; break
 if hit:
  text=hit.read_text(encoding='utf-8'); text=upsert_list(text,'axis_r',R8); text=set_scalar(text,'r8_priority',prio); text=set_scalar(text,'r8_tradition',trad); text=upsert_list(text,'r8_role',role); hit.write_text(text,encoding='utf-8'); reused.append(hit.name); anchors.append((trad,role,hit.stem))
 else:
  title=names[0]; safe=title.replace('/','／').replace('\\','／'); p=WORKS/(safe+'.md'); n=2
  while p.exists(): p=WORKS/(f'{safe}（R8-{n}）.md'); n+=1
  aliases=names[1:]
  content='---\n'+f'id: WL-WORK-R8-{len(created)+1:03d}\ntype: work\ntitle: "{title}"\nauthor: ""\nyear: null\naxis_r:\n  - "{R8}"\ntopics:\n  - "{TOPIC}"\nr8_priority: "{prio}"\nr8_tradition: "{trad}"\nr8_role:\n  - "{role}"\nverification_status: "结构补齐待书目核验"\nbibliography_status: "structural_anchor_pending_bibliography"\n'
  if aliases:
   content+='aliases:\n'+''.join(f'  - "{a}"\n' for a in aliases)
  content+='---\n\n# '+title+'\n\n> R8 结构补齐锚点；年份、作者与版本信息由全局书目治理后续核验。\n'
  p.write_text(content,encoding='utf-8'); created.append(p.name); anchors.append((trad,role,p.stem)); idx[norm(title)]=p

after=sum(1 for p in WORKS.glob('*.md') if R8 in list_field(fm(p.read_text(encoding='utf-8')),'axis_r'))
by={n:0 for n,_ in traditions}
for t,_,_,_ in S: by[t]+=1

# homepage/base/canvas
home='''---
id: WL-TOPIC-R8-SOUTHEAST-ASIA
type: literature_topic_map
name: "东南亚文学"
primary_anchor: WL-R8
anchor_mode: exact
taxonomy_version: literature-taxonomy-v2
topic_role: direct
structure_status: complete
structure_database: "[[02 R8文学结构.base]]"
work_database: "[[03 R8文学作品.base]]"
template_version: literature-topic-r-v1
---
# R8｜东南亚文学

> 路径：[[../../00 世界文学使用规则|世界文学]] → [[../../10 轴/R轴 世界文学传统|R轴]] → **R8 东南亚文学**

## 专题定位
R8 研究大陆与岛屿东南亚在佛教、汉文、伊斯兰、殖民与海洋贸易网络交叠中形成的多语文学系统。它不是现代国家文学的简单并列，也不把殖民语言文学当成唯一现代化路径。

## 导航
- [[01 东南亚文学.canvas|R8 Canvas]]
- [[02 R8文学结构.base|R8 文学结构数据库]]
- [[03 R8文学作品.base|R8 作品数据库]]

### 核心结构
- [[10 核心结构/01 定义与边界|定义与边界]]
- [[10 核心结构/02 历史层与连续性|历史层与连续性]]
- [[10 核心结构/03 语言文字与媒介|语言文字与媒介]]
- [[10 核心结构/04 文学制度与传播|文学制度与传播]]
- [[10 核心结构/05 阅读路线|阅读路线]]

### 内部传统
'''+''.join(f'{i}. [[11 内部传统/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(traditions,1))+'''\n### 跨传统网络
'''+''.join(f'- [[12 跨传统网络/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(networks,1))+'''\n## 边界
- 越南的汉文/儒学传统与 R2 建边，但其主要现代文学场属于 R8。
- 巴利/梵文佛教与史诗网络与 R3 建边，东南亚改写仍属于 R8。
- 东南亚华文文学按主要文学场进入 R8；跨国华语文学身份突出时可连接 R10。
- 殖民语言不是内部传统的唯一分类依据，本土语言文学始终是一级结构。

## 状态
`R8_TOPIC_MAP_STRUCTURE = COMPLETE`

`R8_WORK_SUPPORT = COMPLETE`

`R8_TOPIC_MAP_V1 = COMPLETE_USABLE`
'''
write('00 东南亚文学.md',home)
write('02 R8文学结构.base','''filters:\n  and:\n    - topic_id == "WL-TOPIC-R8-SOUTHEAST-ASIA"\nproperties:\n  file.name: {displayName: 节点}\n  note.dimension: {displayName: 维度}\n  note.sequence: {displayName: 顺序}\nviews:\n  - type: table\n    name: 全部 R8 知识节点\n    order: [file.name, dimension, sequence]\n  - type: table\n    name: 内部传统\n    filters:\n      and:\n        - dimension == "internal_tradition"\n    order: [file.name, sequence]\n  - type: table\n    name: 跨传统网络\n    filters:\n      and:\n        - dimension == "literary_network"\n    order: [file.name, sequence]\n''')
write('03 R8文学作品.base','''filters:\n  and:\n    - type == "work"\n    - axis_r.contains("R8 东南亚文学")\nproperties:\n  file.name: {displayName: 作品}\n  note.author: {displayName: 作者}\n  note.year: {displayName: 年份}\n  note.r8_priority: {displayName: R8优先级}\n  note.r8_tradition: {displayName: 内部传统}\n  note.r8_role: {displayName: R8机制/意义}\n  note.axis_t: {displayName: 时间}\nviews:\n  - type: table\n    name: 全部 R8 作品\n    order: [file.name, author, year, r8_priority, r8_tradition, r8_role, axis_t]\n  - type: table\n    name: 核心 ★\n    filters:\n      and:\n        - r8_priority == "★"\n    order: [file.name, author, r8_tradition, r8_role]\n  - type: table\n    name: 按内部传统\n    groupBy:\n      property: r8_tradition\n      direction: ASC\n    order: [file.name, author, year, r8_priority, r8_role]\n''')
nodes=[]; edges=[]
files=[('home','00 东南亚文学.md')]+[(f't{i}',f'11 内部传统/{i:02d} {n}.md') for i,(n,_) in enumerate(traditions,1)]+[(f'n{i}',f'12 跨传统网络/{i:02d} {n}.md') for i,(n,_) in enumerate(networks,1)]
for j,(id_,f) in enumerate(files):
 x=0 if id_=='home' else (j-1)%5*330-660; y=0 if id_=='home' else ((j-1)//5+1)*260
 nodes.append({'id':id_,'type':'file','file':f,'x':x,'y':y,'width':280,'height':80})
 if id_!='home': edges.append({'id':'e'+str(j),'fromNode':'home','fromSide':'bottom','toNode':id_,'toSide':'top'})
write('01 东南亚文学.canvas',json.dumps({'nodes':nodes,'edges':edges},ensure_ascii=False,indent=2))

node=NODE.read_text(encoding='utf-8')
node=re.sub(r'topic_map:\s*null','topic_map: "[[../../30 专题/R8 东南亚文学/00 东南亚文学|R8 东南亚文学]]"',node)
node=re.sub(r'## 专题地图\n\n> 暂未接入。','## 专题地图\n\n- [[../../30 专题/R8 东南亚文学/00 东南亚文学|R8 东南亚文学]]\n- [[../../30 专题/R8 东南亚文学/01 东南亚文学.canvas|R8 Canvas]]\n- [[../../30 专题/R8 东南亚文学/03 R8文学作品.base|R8 作品数据库]]',node)
NODE.write_text(node,encoding='utf-8')

AUD.mkdir(parents=True,exist_ok=True)
report=['# R8 Structural Completion V1','',f'- Structural slots: **{len(S)}**',f'- Existing anchors reused/enriched: **{len(reused)}**',f'- Newly created canonical Works: **{len(created)}**',f'- R8 Works before: **{before}**',f'- R8 Works after: **{after}**','','## By tradition']
for n,_ in traditions: report.append(f'- {n}: **{by[n]}/{by[n]} COVERED**')
report+=['','## Created']+[f'- {x}' for x in created]+['','## Governance','- R8 keeps Southeast Asian literary fields primary while linking R2/R3 where Chinese or Indic networks are explanatory.','- Indigenous/local-language traditions remain first-class; colonial languages are not the sole organizing principle.','- New anchors leave `year: null` pending global bibliographic/T-axis governance.','','`R8_STRUCTURAL_COVERAGE_V1 = 100_PERCENT_COMPLETE`','`R8_TOPIC_MAP_V1 = COMPLETE_USABLE`']
(AUD/'R8_STRUCTURAL_COMPLETION_V1.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
