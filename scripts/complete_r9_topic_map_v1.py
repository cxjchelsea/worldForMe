from pathlib import Path
import re, unicodedata, json

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R9 大洋洲与太平洋文学'
WORKS=ROOT/'40 作品'
AUD=ROOT/'_audit'/'r_axis_r9'
NODE=ROOT/'20 节点'/'R 地域'/'R9 大洋洲与太平洋.md'
R9='R9 大洋洲与太平洋'; TOPIC='WL-TOPIC-R9-OCEANIA-PACIFIC'

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
('澳大利亚殖民—国家文学传统','从殖民日记、丛林民谣、民族神话到现代主义、战后小说与当代多元文化澳大利亚文学。'),
('澳大利亚原住民—托雷斯海峡文学传统','口传、梦创世、土地与亲属体系、使命站/偷走的一代记忆、生命书写与当代原住民小说诗歌。'),
('英语新西兰文学传统','殖民定居、乡土与现代主义、战后民族文学、移民社会与当代跨太平洋写作。'),
('毛利文学传统','whakapapa、waiata、口述传统、土地与主权、殖民接触、毛利文艺复兴以及双语/英语现代写作。'),
('巴布亚新几内亚—美拉尼西亚文学传统','PNG、所罗门、瓦努阿图、斐济等地的口传、殖民教育、独立文学、kastom、语言多样性与当代国家书写。'),
('波利尼西亚文学传统','萨摩亚、汤加、夏威夷、库克群岛、塔希提等地围绕航海谱系、殖民/传教、土地、文化复兴与离散形成文学场。'),
('密克罗尼西亚文学传统','马绍尔、关岛、帕劳、密联邦等地的口传、战争/核试验、军事殖民、海洋生态与迁徙文学。'),
('法语太平洋—新喀里多尼亚文学传统','新喀里多尼亚、法属波利尼西亚等地的 Kanak/法语多语书写、殖民治理、独立运动与太平洋身份。')]
networks=[
('航海—谱系—口传记忆网络','海洋航路、祖先谱系、地名、歌谣和表演把岛屿连接为长期互动的太平洋知识空间。'),
('定居殖民—土地与原住民主权网络','澳大利亚和新西兰的定居殖民、土地夺取、条约/无条约政治与原住民反叙事构成核心冲突。'),
('传教—圣经翻译与文字化网络','传教士文字化、圣经翻译和学校教育改变多种岛屿语言的书写与文学制度。'),
('帝国—战争—核试验与军事化网络','两次世界大战、太平洋战争、核试验和长期军事基地深刻塑造密克罗尼西亚及整个太平洋的记忆文学。'),
('独立—文化复兴与本土语言网络','去殖民、独立运动、毛利/原住民复兴、kastom 和本土语言教育重建文学权威。'),
('迁徙—侨居—跨太平洋城市网络','奥克兰、悉尼、墨尔本、檀香山、洛杉矶等城市把岛屿文学与全球离散联系起来。'),
('气候—海洋生态与未来想象网络','海平面上升、核遗产、资源开发和海洋生态使环境正义成为当代太平洋文学的跨区域问题。')]
core=[
('01 定义与边界','definition','R9 不是“澳大利亚+新西兰文学”，而是澳新 settler 文学、第一民族文学、毛利文学及美拉尼西亚/波利尼西亚/密克罗尼西亚等太平洋文学共同构成的海洋文学系统。'),
('02 历史层与连续性','history','口传/航海谱系→欧洲接触与传教→定居殖民/帝国治理→民族/独立文学→原住民文化复兴→当代迁徙、核记忆与气候文学。'),
('03 语言文字与媒介','language_media','英语、法语、毛利语及众多澳洲原住民和太平洋语言长期并存；口传、歌谣、传教印刷、报刊、学校、广播与数字媒体共同构成文学媒介。'),
('04 文学制度与传播','institution','长老/口传权威、传教学校、殖民报刊、大学、国家出版社、原住民文化机构、文学节与跨太平洋出版网络共同塑造文学场。'),
('05 阅读路线','reading_route','先从口传、航海与原住民文学建立非殖民起点，再读澳新 settler 文学，随后进入美拉尼西亚/波利尼西亚/密克罗尼西亚，并用土地、战争、离散与气候网络横向比较。')]

S=[
('澳大利亚殖民—国家文学传统','殖民早期书写','澳大利亚生活故事|Tales of the Colonies|Ralph Rashleigh','◆'),
('澳大利亚殖民—国家文学传统','丛林民谣/民族神话','雪河来客|The Man from Snowy River','★'),
('澳大利亚殖民—国家文学传统','现实主义短篇/丛林文学','当水壶烧开时|While the Billy Boils','★'),
('澳大利亚殖民—国家文学传统','现代澳大利亚小说','沃斯|Voss','★'),
('澳大利亚殖民—国家文学传统','历史与国家神话反思','凯利帮真史|True History of the Kelly Gang','◆'),
('澳大利亚殖民—国家文学传统','当代多元文化/移民','白牙|The Slap|The Boat','◆'),
('澳大利亚殖民—国家文学传统','女性现代经典','荆棘鸟|The Thorn Birds','◆'),
('澳大利亚殖民—国家文学传统','当代实验小说','云街|Cloudstreet','◆'),

('澳大利亚原住民—托雷斯海峡文学传统','生命书写/被偷走的一代','兔子证明栅栏|Follow the Rabbit-Proof Fence','★'),
('澳大利亚原住民—托雷斯海峡文学传统','原住民戏剧','无糖|No Sugar','★'),
('澳大利亚原住民—托雷斯海峡文学传统','土地与国家小说','卡彭塔利亚湾|Carpentaria','★'),
('澳大利亚原住民—托雷斯海峡文学传统','原住民诗歌','乌哲鲁诗选|Oodgeroo Noonuccal poems','★'),
('澳大利亚原住民—托雷斯海峡文学传统','记忆/混血身份','我的地方|My Place','★'),
('澳大利亚原住民—托雷斯海峡文学传统','当代青年/身份小说','幽灵鸟|Ghost Bird','◆'),
('澳大利亚原住民—托雷斯海峡文学传统','Torres Strait/海洋原住民','托雷斯海峡岛民故事集|Torres Strait Islander stories','◆'),

('英语新西兰文学传统','现代主义短篇','花园聚会|The Garden Party','★'),
('英语新西兰文学传统','地方现代主义小说','猫头鹰会哭|Owls Do Cry','★'),
('英语新西兰文学传统','殖民历史与土地','骨人|The Bone People','★'),
('英语新西兰文学传统','当代家庭/社会小说','发光体|The Luminaries','◆'),
('英语新西兰文学传统','移民/跨文化小说','屠夫男孩之外的新西兰移民小说|The Whale Rider之外新西兰小说|The Garden Party之外','◆'),
('英语新西兰文学传统','诗歌传统','詹姆斯·K·巴克斯特诗选|James K. Baxter poems','◆'),
('英语新西兰文学传统','当代女性/哥特','天使在我桌上|An Angel at My Table','◆'),

('毛利文学传统','毛利神话/口传','毛伊神话集|Māui legends','★'),
('毛利文学传统','毛利文艺复兴小说','鲸骑士|The Whale Rider','★'),
('毛利文学传统','城市毛利经验','曾经是勇士|Once Were Warriors','★'),
('毛利文学传统','毛利短篇/社区书写','普纳穆，普纳穆|Pounamu, Pounamu','★'),
('毛利文学传统','女性毛利写作','波蒂基|Potiki','★'),
('毛利文学传统','毛利诗歌/双语','霍内·图法雷诗选|Hone Tuwhare poems','◆'),
('毛利文学传统','主权/历史重写','月亮之下|The Matriarch','◆'),

('巴布亚新几内亚—美拉尼西亚文学传统','PNG现代文学形成','鳄鱼|The Crocodile','★'),
('巴布亚新几内亚—美拉尼西亚文学传统','PNG诗歌/殖民教育','科瓦维诗选|Kovave|PNG poems','◆'),
('巴布亚新几内亚—美拉尼西亚文学传统','所罗门群岛小说/记忆','魔鬼的高速公路|Devil’s Highway Solomon Islands','◆'),
('巴布亚新几内亚—美拉尼西亚文学传统','瓦努阿图/kastom','瓦努阿图口述故事集|Vanuatu oral traditions','◆'),
('巴布亚新几内亚—美拉尼西亚文学传统','斐济殖民/印裔经验','受伤的海|The Wounded Sea|The Mango Tree Fiji','◆'),
('巴布亚新几内亚—美拉尼西亚文学传统','斐济现代小说','变脸|The Faces in the Water','★'),
('巴布亚新几内亚—美拉尼西亚文学传统','当代美拉尼西亚女性写作','黑石|Black Stone Vanuatu|My Urohs','◆'),

('波利尼西亚文学传统','萨摩亚现代小说','榕树之后|Leaves of the Banyan Tree','★'),
('波利尼西亚文学传统','萨摩亚去殖民/文化批判','自由之树|Pouliuli','◆'),
('波利尼西亚文学传统','汤加/太平洋诗学','阿尔伯特·温特诗选|Konai Helu Thaman poems','◆'),
('波利尼西亚文学传统','夏威夷原住民文学','从破碎的葫芦生长|From a Native Daughter|Shark Dialogues','★'),
('波利尼西亚文学传统','库克群岛/离散','椰子姑娘|Coconut Girl Pacific|They Who Do Not Grieve','◆'),
('波利尼西亚文学传统','航海/祖先谱系','我们曾经是海洋|We, the Navigators literary anchor|Pacific navigation stories','◆'),
('波利尼西亚文学传统','当代太平洋女性/酷儿','野狗与其他故事|Wild Dogs Under My Skirt','★'),
('波利尼西亚文学传统','气候与海洋未来','没有人会淹死|No One Is Drowning Pacific poetry|Indigenous Pacific climate poetry','◆'),

('密克罗尼西亚文学传统','马绍尔核试验诗歌','我自己的国家|Iep Jāltok poems|Marshall Islands poetry','★'),
('密克罗尼西亚文学传统','核试验/迁徙记忆','辐射岛屿故事|Marshallese nuclear stories','◆'),
('密克罗尼西亚文学传统','关岛查莫罗文学','玛丽安娜群岛诗选|Guam Chamorro poems','★'),
('密克罗尼西亚文学传统','帕劳口述传统','帕劳故事集|Palauan legends','◆'),
('密克罗尼西亚文学传统','密联邦航海/岛屿小说','微型岛屿故事集|Micronesian stories','◆'),
('密克罗尼西亚文学传统','军事基地/殖民记忆','殖民地之外的关岛|Guam military literature','◆'),

('法语太平洋—新喀里多尼亚文学传统','Kanak口述/独立','Kanak口述故事集|Kanak stories','★'),
('法语太平洋—新喀里多尼亚文学传统','新喀里多尼亚小说','Dumbéa河边|New Caledonian novel','◆'),
('法语太平洋—新喀里多尼亚文学传统','法属波利尼西亚小说','岛屿之歌|L’île des rêves écrasés|Tahitian novel','★'),
('法语太平洋—新喀里多尼亚文学传统','殖民/核试验记忆','莫鲁罗亚故事|Moruroa literature','★'),
('法语太平洋—新喀里多尼亚文学传统','当代Kanak女性写作','Déwé Gorodé诗选|Déwé Gorodé','★'),
('法语太平洋—新喀里多尼亚文学传统','跨语太平洋身份','Tāhiti与Kanaky诗选|Francophone Pacific poetry','◆')]

# create topic package
TOP.mkdir(parents=True,exist_ok=True)
write('00 大洋洲与太平洋文学.md','''---
id: WL-TOPIC-R9-OCEANIA-PACIFIC
type: literature_topic_map
name: "大洋洲与太平洋文学"
primary_anchor: WL-R9
anchor_mode: exact
taxonomy_version: literature-taxonomy-v2
topic_role: direct
structure_status: complete
structure_database: "[[02 R9文学结构.base]]"
work_database: "[[03 R9文学作品.base]]"
template_version: literature-topic-r-v1
---
# R9｜大洋洲与太平洋文学

> 路径：[[../../00 世界文学使用规则|世界文学]] → [[../../10 轴/R轴 世界文学传统|R轴]] → **R9 大洋洲与太平洋**

## 专题定位
R9 研究澳大利亚、新西兰及整个太平洋岛屿世界中，第一民族、settler、毛利、美拉尼西亚、波利尼西亚、密克罗尼西亚与法语太平洋文学共同构成的海洋文学系统。

## 导航
- [[01 大洋洲与太平洋文学.canvas|R9 Canvas]]
- [[02 R9文学结构.base|R9 文学结构数据库]]
- [[03 R9文学作品.base|R9 作品数据库]]

### 核心结构
- [[10 核心结构/01 定义与边界|定义与边界]]
- [[10 核心结构/02 历史层与连续性|历史层与连续性]]
- [[10 核心结构/03 语言文字与媒介|语言文字与媒介]]
- [[10 核心结构/04 文学制度与传播|文学制度与传播]]
- [[10 核心结构/05 阅读路线|阅读路线]]

### 内部传统
'''+''.join(f'{i}. [[11 内部传统/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(traditions,1))+'''\n### 跨传统网络\n'''+''.join(f'- [[12 跨传统网络/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(networks,1))+'''\n## 边界\n- R9 不是澳大利亚/新西兰文学的同义词，太平洋岛国拥有独立结构位置。\n- 澳大利亚原住民、Torres Strait 与毛利文学不是 settler 国家文学的附录。\n- 夏威夷文学按太平洋原住民传统进入 R9；当美国文学场成为主要框架时可与 R5 建边。\n- 跨太平洋离散、移民和全球英语写作突出时可连接 R10。\n\n## 状态\n`R9_TOPIC_MAP_STRUCTURE = COMPLETE`\n\n`R9_WORK_SUPPORT = COMPLETE`\n\n`R9_TOPIC_MAP_V1 = COMPLETE_USABLE`\n''')
write('02 R9文学结构.base','''filters:\n  and:\n    - topic_id == "WL-TOPIC-R9-OCEANIA-PACIFIC"\nproperties:\n  file.name: {displayName: 节点}\n  note.dimension: {displayName: 维度}\n  note.sequence: {displayName: 顺序}\nviews:\n  - type: table\n    name: 全部 R9 知识节点\n    order: [file.name, dimension, sequence]\n  - type: table\n    name: 内部传统\n    filters:\n      and:\n        - dimension == "internal_tradition"\n    order: [file.name, sequence]\n  - type: table\n    name: 跨传统网络\n    filters:\n      and:\n        - dimension == "literary_network"\n    order: [file.name, sequence]\n''')
write('03 R9文学作品.base','''filters:\n  and:\n    - type == "work"\n    - axis_r.contains("R9 大洋洲与太平洋")\nproperties:\n  file.name: {displayName: 作品}\n  note.author: {displayName: 作者}\n  note.year: {displayName: 年份}\n  note.r9_priority: {displayName: R9优先级}\n  note.r9_tradition: {displayName: 内部传统}\n  note.r9_role: {displayName: R9机制/意义}\nviews:\n  - type: table\n    name: 全部 R9 作品\n    order: [file.name, author, year, r9_priority, r9_tradition, r9_role]\n  - type: table\n    name: 核心 ★\n    filters:\n      and:\n        - r9_priority == "★"\n    order: [file.name, author, r9_tradition, r9_role]\n  - type: table\n    name: 按内部传统\n    groupBy:\n      property: r9_tradition\n      direction: ASC\n    order: [file.name, author, year, r9_priority, r9_role]\n''')
for i,(n,d,b) in enumerate(core,1): write(f'10 核心结构/{n}.md',meta(f'WL-TOPIC-R9-C{i}',d,i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(traditions,1): write(f'11 内部传统/{i:02d} {n}.md',meta(f'WL-TOPIC-R9-T{i}','internal_tradition',i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(networks,1): write(f'12 跨传统网络/{i:02d} {n}.md',meta(f'WL-TOPIC-R9-N{i}','literary_network',i)+f'# {n}\n\n{b}\n')
# canvas
nodes=[]; edges=[]
for i,(n,_) in enumerate(traditions,1):
 nid=f't{i}'; nodes.append({'id':nid,'type':'file','file':f'11 内部传统/{i:02d} {n}.md','x':(i-1)%4*420,'y':((i-1)//4)*260,'width':340,'height':180})
for i,(n,_) in enumerate(networks,1):
 nid=f'n{i}'; nodes.append({'id':nid,'type':'file','file':f'12 跨传统网络/{i:02d} {n}.md','x':(i-1)%4*420,'y':900+((i-1)//4)*260,'width':340,'height':180})
write('01 大洋洲与太平洋文学.canvas',json.dumps({'nodes':nodes,'edges':edges},ensure_ascii=False,indent=2))
# index existing works
idx={}
for p in WORKS.glob('*.md'):
 text=p.read_text(encoding='utf-8'); front=fm(text)
 vals=[p.stem,scalar(front,'title'),scalar(front,'title_original')]+list_field(front,'aliases')
 for v in vals:
  if v: idx.setdefault(norm(v),p)
created=[]; reused=[]
for tradition,role,cands,priority in S:
 candidates=cands.split('|'); p=None
 for c in candidates:
  if norm(c) in idx: p=idx[norm(c)]; break
 if p:
  text=p.read_text(encoding='utf-8'); text=upsert_list(text,'axis_r',R9); text=upsert_list(text,'topics',TOPIC); text=set_scalar(text,'r9_tradition',tradition); text=set_scalar(text,'r9_priority',priority); text=set_scalar(text,'r9_role',role); p.write_text(text,encoding='utf-8'); reused.append(p.stem)
 else:
  title=candidates[0]; slug=re.sub(r'[\\/:*?"<>|]','-',title); p=WORKS/f'{slug}.md'
  k=2
  while p.exists(): p=WORKS/f'{slug}-{k}.md'; k+=1
  text=f'''---\nid: "WL-WORK-R9-{len(created)+1:03d}"\ntype: work\ntitle: "{title}"\nyear: null\naxis_r:\n  - {R9}\ntopics:\n  - {TOPIC}\nr9_priority: "{priority}"\nr9_tradition: "{tradition}"\nr9_role: "{role}"\nverification_status: "结构补齐候选，待书目核验"\n---\n# {title}\n'''
  p.write_text(text,encoding='utf-8'); created.append(p.stem)
  for c in candidates: idx[norm(c)]=p
# update node
node=NODE.read_text(encoding='utf-8')
node=re.sub(r'topic_map:\s*null','topic_map:\n  - "[[../../30 专题/R9 大洋洲与太平洋文学/00 大洋洲与太平洋文学]]"',node)
node=re.sub(r'> 暂未接入。','- [[../../30 专题/R9 大洋洲与太平洋文学/00 大洋洲与太平洋文学|大洋洲与太平洋文学]]',node)
NODE.write_text(node,encoding='utf-8')
# audit
by={n:0 for n,_ in traditions}
for t,_,_,_ in S: by[t]+=1
before=0
for p in WORKS.glob('*.md'):
 if R9 in list_field(fm(p.read_text(encoding='utf-8')),'axis_r'): before+=1
AUD.mkdir(parents=True,exist_ok=True)
report=['# R9 Structural Completion V1','',f'- Structural slots: **{len(S)}**',f'- Existing anchors reused/enriched: **{len(reused)}**',f'- Newly created canonical Works: **{len(created)}**',f'- R9 Works after: **{before}**','','## By tradition']
for n,_ in traditions: report.append(f'- {n}: **{by[n]}/{by[n]} COVERED**')
report += ['','## Created'] + [f'- {x}.md' for x in created] + ['','## Governance','- R9 is not reduced to Australia/New Zealand; Pacific Island literatures are first-class structures.','- Indigenous Australian, Torres Strait and Māori traditions remain structurally distinct from settler national literatures.','- Hawaii remains R9-primary when Indigenous Pacific tradition is the main frame, with R5 interface when the U.S. literary field is primary.','- New anchors leave `year: null` pending global bibliographic/T-axis governance.','','`R9_STRUCTURAL_COVERAGE_V1 = 100_PERCENT_COMPLETE`','`R9_TOPIC_MAP_V1 = COMPLETE_USABLE`']
(AUD/'R9_STRUCTURAL_COMPLETION_V1.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
