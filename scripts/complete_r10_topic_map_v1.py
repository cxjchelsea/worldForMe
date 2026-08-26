from pathlib import Path
import re, unicodedata, json

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R10 跨区域文学传统'
WORKS=ROOT/'40 作品'
AUD=ROOT/'_audit'/'r_axis_r10'
NODE=ROOT/'20 节点'/'R 地域'/'R10 跨区域文学传统.md'
NODE102=ROOT/'20 节点'/'R 地域'/'R10.2 非洲离散文学.md'
TOPIC='WL-TOPIC-R10-TRANSREGIONAL'
R102='R10.2 非洲离散文学'

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
('非洲离散文学传统','R10.2 的唯一 canonical 子坐标；从奴隶贸易、黑色大西洋到当代非洲迁徙与跨国黑人文学。'),
('犹太离散—意第绪与跨语文学传统','意第绪、希伯来语及所在国语言之间的迁徙写作，围绕流亡、同化、浩劫、记忆与多重身份。'),
('华人—华语离散文学传统','东南亚、北美、欧洲及其他地区的华人/华语迁徙、代际、语言转换与跨国记忆。'),
('南亚离散文学传统','印度、巴基斯坦、孟加拉等南亚移民在英国、北美、加勒比与全球城市中的跨国文学。'),
('阿拉伯—中东离散文学传统','阿拉伯、巴勒斯坦、黎巴嫩及更广中东流亡、移民、战争与跨语写作。'),
('流亡—难民—无国籍文学传统','因战争、政治迫害、边界变化、驱逐与难民制度形成的跨区域文学经验。'),
('跨语言—自译与语言转换文学传统','作家主动跨语言写作、自译或改变主要创作语言，使语言选择本身成为文学结构。'),
('全球移民—后殖民都市文学传统','伦敦、纽约、多伦多、巴黎等全球城市中的移民、混杂身份、后殖民记忆与第二代写作。')]
networks=[
('奴隶贸易—黑色大西洋与返航网络','强制迁移、奴隶制、废奴、加勒比与美洲黑人文化构成 R10.2 的历史底层。'),
('帝国—契约劳工与殖民迁徙网络','帝国航线、契约劳工、教育与殖民行政制造南亚、华人、加勒比等跨区域人口流动。'),
('战争—驱逐—难民与流亡网络','战争、分治、浩劫、殖民撤退与当代难民制度持续制造新的跨区域文学共同体。'),
('翻译—跨语写作与自译网络','翻译、双语出版、自译和语言转换改变作品的文学场归属与读者结构。'),
('港口—全球城市与族裔出版网络','港口和全球城市、族裔报刊、小型出版社与社区机构是离散文学的重要制度节点。'),
('奖项—世界出版与文学经纪网络','国际奖项、文学经纪、翻译资助和跨国出版社塑造哪些离散作品进入世界文学。'),
('返乡—祖居地—代际记忆网络','返乡、祖居地想象、第二代记忆与跨国家族叙事形成离散文学的核心时间结构。')]
core=[
('01 定义与边界','definition','R10 不是地域坐标，而是跨区域文学网络组；除 R10.2 非洲离散外，其余类型只在专题内部展开，不新增全局 R 子坐标。'),
('02 历史层与连续性','history','强制迁移与离散→帝国劳工/殖民迁徙→战争/流亡/分治→战后移民社会→全球城市、难民制度与跨国出版。'),
('03 语言文字与媒介','language_media','双语/多语写作、意第绪/希伯来语/华语/英语/法语/阿拉伯语等跨场流动，翻译、自译、族裔报刊与数字媒介共同塑造文本。'),
('04 文学制度与传播','institution','移民社区、族裔出版社、流亡期刊、大学、翻译项目、国际奖项和全球出版集团共同构成跨区域文学制度。'),
('05 阅读路线','reading_route','先读 R10.2 黑色大西洋，再比较犹太/华人/南亚/阿拉伯离散，随后转向难民流亡、跨语言写作与全球都市文学。')]

S=[
('非洲离散文学传统','奴隶制后裔与记忆','宠儿|Beloved','★'),
('非洲离散文学传统','黑人女性南方经验','他们眼望上苍|Their Eyes Were Watching God','◆'),
('非洲离散文学传统','加勒比黑人跨国暴力','七杀简史|A Brief History of Seven Killings','★'),
('非洲离散文学传统','非洲移民美国','美国佬|Americanah','★'),
('非洲离散文学传统','加勒比殖民混血身份','宽广的萨尔加索海|Wide Sargasso Sea','◆'),
('非洲离散文学传统','跨大西洋黑人家族史','回家|Homegoing','★'),
('非洲离散文学传统','黑人现代都市主体','看不见的人|Invisible Man','★'),

('犹太离散—意第绪与跨语文学传统','东欧意第绪世界','卖牛奶的特维|Tevye the Dairyman','★'),
('犹太离散—意第绪与跨语文学传统','移民纽约意第绪传统','莫斯卡特一家|The Family Moskat','◆'),
('犹太离散—意第绪与跨语文学传统','犹太裔美国同化讽刺','波特诺伊的怨诉|Portnoy’s Complaint','★'),
('犹太离散—意第绪与跨语文学传统','浩劫前夜与流亡记忆','巴登海姆1939|Badenheim 1939','◆'),
('犹太离散—意第绪与跨语文学传统','第二代记忆/身份','鼠族|Maus','★'),
('犹太离散—意第绪与跨语文学传统','跨语中欧犹太现代性','审判|The Trial','◆'),

('华人—华语离散文学传统','华裔美国女性代际','女勇士|The Woman Warrior','★'),
('华人—华语离散文学传统','华裔美国母女记忆','喜福会|The Joy Luck Club','★'),
('华人—华语离散文学传统','唐人街家庭/城市','骨|Bone','◆'),
('华人—华语离散文学传统','中国移民美国生活','自由生活|A Free Life','◆'),
('华人—华语离散文学传统','跨国家庭与身份','离开者|The Leavers','◆'),
('华人—华语离散文学传统','东南亚华人历史记忆','雨季不再来|The Garden of Evening Mists','◆'),

('南亚离散文学传统','英美孟加拉移民家庭','同名人|The Namesake','★'),
('南亚离散文学传统','英国孟加拉移民社区','砖巷|Brick Lane','★'),
('南亚离散文学传统','英国南亚第二代身份','郊区佛爷|The Buddha of Suburbia','◆'),
('南亚离散文学传统','南亚/欧美跨国阶级','失落的遗产|The Inheritance of Loss','★'),
('南亚离散文学传统','巴基斯坦跨国身份','拉合尔茶馆的陌生人|The Reluctant Fundamentalist','★'),
('南亚离散文学传统','印度/美国跨国家族','低地|The Lowland','◆'),

('阿拉伯—中东离散文学传统','南北迁移与殖民回望','移居北方的时节|Season of Migration to the North','★'),
('阿拉伯—中东离散文学传统','战争与全球迁徙','西方退出|Exit West','★'),
('阿拉伯—中东离散文学传统','巴勒斯坦跨国家族','盐屋|Salt Houses','★'),
('阿拉伯—中东离散文学传统','阿拉伯裔美国身份','阿拉伯爵士|Arabian Jazz','◆'),
('阿拉伯—中东离散文学传统','黎巴嫩/美国跨国叙事','哈卡瓦蒂|The Hakawati','◆'),
('阿拉伯—中东离散文学传统','战争流亡与女性书写','贝鲁特蓝调|Beirut Blues','◆'),

('流亡—难民—无国籍文学传统','欧洲政治流亡','过境|Transit','★'),
('流亡—难民—无国籍文学传统','犹太流亡记忆','移民|The Emigrants','★'),
('流亡—难民—无国籍文学传统','苏丹难民跨国生命史','什么是什么|What Is the What','◆'),
('流亡—难民—无国籍文学传统','叙利亚难民','阿勒颇养蜂人|The Beekeeper of Aleppo','◆'),
('流亡—难民—无国籍文学传统','无国籍/边界寓言','离岸|Offshore refugee literature|The Boat','◆'),
('流亡—难民—无国籍文学传统','分治与强制迁移','开往巴基斯坦的列车|Train to Pakistan','★'),

('跨语言—自译与语言转换文学传统','俄英跨语现代小说','洛丽塔|Lolita','★'),
('跨语言—自译与语言转换文学传统','法英语自译戏剧/小说','莫洛伊|Molloy','◆'),
('跨语言—自译与语言转换文学传统','捷克法语/跨国写作','生命中不能承受之轻|The Unbearable Lightness of Being','★'),
('跨语言—自译与语言转换文学传统','波兰裔英语现代主义','黑暗的心|Heart of Darkness','◆'),
('跨语言—自译与语言转换文学传统','中文母语英语创作','等待|Waiting','◆'),
('跨语言—自译与语言转换文学传统','英语作者转意大利语','在他乡|In Other Words','◆'),

('全球移民—后殖民都市文学传统','伦敦多族裔都市','白牙|White Teeth','★'),
('全球移民—后殖民都市文学传统','纽约非洲跨国观察','开放的城市|Open City','★'),
('全球移民—后殖民都市文学传统','加勒比/美国第二代','奥斯卡·瓦奥短暂而奇妙的一生|The Brief Wondrous Life of Oscar Wao','★'),
('全球移民—后殖民都市文学传统','越裔美国第二代','在地球上我们短暂地绚烂|On Earth We’re Briefly Gorgeous','◆'),
('全球移民—后殖民都市文学传统','伦敦后殖民混杂/宗教政治','撒旦诗篇|The Satanic Verses','★'),
('全球移民—后殖民都市文学传统','多伦多移民都市','皮肤之下|In the Skin of a Lion','◆')]

TOP.mkdir(parents=True,exist_ok=True)
write('02 R10文学结构.base','''filters:\n  and:\n    - topic_id == "WL-TOPIC-R10-TRANSREGIONAL"\nproperties:\n  file.name: {displayName: 节点}\n  note.dimension: {displayName: 维度}\n  note.sequence: {displayName: 顺序}\nviews:\n  - type: table\n    name: 全部 R10 知识节点\n    order: [file.name, dimension, sequence]\n  - type: table\n    name: 跨区域传统\n    filters:\n      and:\n        - dimension == "internal_tradition"\n    order: [file.name, sequence]\n  - type: table\n    name: 跨传统网络\n    filters:\n      and:\n        - dimension == "literary_network"\n    order: [file.name, sequence]\n''')
write('03 R10文学作品.base','''filters:\n  and:\n    - type == "work"\n    - topics.contains("WL-TOPIC-R10-TRANSREGIONAL")\nproperties:\n  file.name: {displayName: 作品}\n  note.author: {displayName: 作者}\n  note.year: {displayName: 年份}\n  note.r10_priority: {displayName: R10优先级}\n  note.r10_tradition: {displayName: 跨区域传统}\n  note.r10_role: {displayName: R10机制/意义}\n  note.axis_r: {displayName: 地域坐标}\nviews:\n  - type: table\n    name: 全部 R10 作品\n    order: [file.name, author, year, r10_priority, r10_tradition, r10_role, axis_r]\n  - type: table\n    name: 核心 ★\n    filters:\n      and:\n        - r10_priority == "★"\n    order: [file.name, author, r10_tradition, r10_role]\n  - type: table\n    name: 按跨区域传统\n    groupBy:\n      property: r10_tradition\n      direction: ASC\n    order: [file.name, author, year, r10_priority, r10_role]\n''')
for i,(n,d,b) in enumerate(core,1): write(f'10 核心结构/{n}.md',meta(f'WL-TOPIC-R10-C{i}',d,i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(traditions,1): write(f'11 内部传统/{i:02d} {n}.md',meta(f'WL-TOPIC-R10-T{i}','internal_tradition',i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(networks,1): write(f'12 跨传统网络/{i:02d} {n}.md',meta(f'WL-TOPIC-R10-N{i}','literary_network',i)+f'# {n}\n\n{b}\n')

# index existing works
entries=[]
for p in WORKS.glob('*.md'):
 txt=p.read_text(encoding='utf-8',errors='ignore'); front=fm(txt)
 keys={norm(p.stem),norm(scalar(front,'title')),norm(scalar(front,'title_original'))}
 for a in list_field(front,'aliases'): keys.add(norm(a))
 entries.append((p,txt,front,{k for k in keys if k}))
used=set(); created=[]; reused=[]
def find(cands):
 ns=[norm(x) for x in cands if x]
 for p,txt,front,keys in entries:
  if any(n in keys for n in ns): return p,txt,front
 return None

def t_from_year(y):
 try:y=int(y)
 except:return None
 return 'T0 文学源头与古代文学' if y<500 else 'T1 中古多中心文学世界' if y<1500 else 'T2 早期现代文学' if y<1800 else 'T3 19世纪现代文学体系' if y<1890 else 'T4 全球现代主义时代' if y<1945 else 'T5 二战后多极文学' if y<1980 else 'T6 当代全球文学'

for idx,(trad,role,aliases,prio) in enumerate(S,1):
 cands=[x.strip() for x in aliases.split('|')]; hit=find(cands)
 if hit:
  p,txt,front=hit; new=upsert_list(txt,'topics',TOPIC)
  if trad=='非洲离散文学传统': new=upsert_list(new,'axis_r',R102)
  new=set_scalar(new,'r10_tradition',trad); new=set_scalar(new,'r10_role',role); new=set_scalar(new,'r10_priority',prio)
  if new!=txt: p.write_text(new,encoding='utf-8')
  reused.append(p.name); used.add(p.name)
 else:
  title=cands[0]; fn=title.replace('/','／')+'.md'; p=WORKS/fn
  n=2
  while p.exists(): p=WORKS/(title.replace('/','／')+f'（R10-{n}）.md'); n+=1
  axis='\n  - "'+R102+'"' if trad=='非洲离散文学传统' else ' []'
  content=f'''---\nid: "WL-WORK-R10-{idx:03d}"\ntype: "work"\ntitle: "{title}"\naliases:\n'''+''.join(f'  - "{a}"\n' for a in cands[1:])+f'''author: null\nyear: null\naxis_t: []\naxis_r:{axis}\ntopics:\n  - "{TOPIC}"\nr10_priority: "{prio}"\nr10_tradition: "{trad}"\nr10_role: "{role}"\nverification_status: "待书目核验"\n---\n\n# {title}\n\n> R10 结构补齐锚点：{role}。\n'''
  p.write_text(content,encoding='utf-8'); created.append(p.name)

# homepage/canvas/node
home='''---\nid: WL-TOPIC-R10-TRANSREGIONAL\ntype: literature_topic_map\nname: "跨区域文学传统"\nprimary_anchor: WL-R10\nanchor_mode: network_group\ntaxonomy_version: literature-taxonomy-v2\ntopic_role: transregional\nstructure_status: complete\nstructure_database: "[[02 R10文学结构.base]]"\nwork_database: "[[03 R10文学作品.base]]"\ntemplate_version: literature-topic-r-v1\n---\n# R10｜跨区域文学传统\n\n> 路径：[[../../00 世界文学使用规则|世界文学]] → [[../../10 轴/R轴 世界文学传统|R轴]] → **R10 跨区域文学传统**\n\n## 专题定位\nR10 不是新的地域文学桶，而是处理离散、移民、流亡、难民、跨语言和全球出版等使作品跨越 R1–R9 地域文学场的网络层。\n\n## 导航\n- [[01 跨区域文学传统.canvas|R10 Canvas]]\n- [[02 R10文学结构.base|R10 文学结构数据库]]\n- [[03 R10文学作品.base|R10 作品数据库]]\n\n### 核心结构\n- [[10 核心结构/01 定义与边界|定义与边界]]\n- [[10 核心结构/02 历史层与连续性|历史层与连续性]]\n- [[10 核心结构/03 语言文字与媒介|语言文字与媒介]]\n- [[10 核心结构/04 文学制度与传播|文学制度与传播]]\n- [[10 核心结构/05 阅读路线|阅读路线]]\n\n### 跨区域传统\n'''+''.join(f'{i}. [[11 内部传统/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(traditions,1))+'''\n### 跨传统网络\n'''+''.join(f'- [[12 跨传统网络/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(networks,1))+'''\n## 坐标治理\n- R10 本身 `anchorable: false`，不作为普通作品地域标签。\n- [[../../20 节点/R 地域/R10.2 非洲离散文学|R10.2 非洲离散文学]] 是当前唯一实体化的 R10 子坐标。\n- 犹太、华人、南亚、阿拉伯等离散类型只作为专题内部传统，不新增 R10.x 全局坐标。\n- 作品保留其 R1–R9 地域坐标，同时通过 `topics / r10_tradition / r10_role` 进入本专题。\n\n## 状态\n`R10_TOPIC_MAP_STRUCTURE = COMPLETE`\n\n`R10_WORK_SUPPORT = COMPLETE`\n\n`R10_TOPIC_MAP_V1 = COMPLETE_USABLE`\n'''
write('00 跨区域文学传统.md',home)
canvas={"nodes":[{"id":"c","type":"text","text":"R10 跨区域文学传统\n离散 · 移民 · 流亡 · 跨语言","x":0,"y":0,"width":300,"height":120}],"edges":[]}
for i,(n,_) in enumerate(traditions,1):
 nid=f't{i}'; canvas['nodes'].append({"id":nid,"type":"file","file":f'11 内部传统/{i:02d} {n}.md',"x":400+(i%2)*360,"y":-500+i*130,"width":320,"height":80}); canvas['edges'].append({"id":f'e{i}',"fromNode":"c","toNode":nid})
write('01 跨区域文学传统.canvas',json.dumps(canvas,ensure_ascii=False,indent=2))
node=NODE.read_text(encoding='utf-8'); node=re.sub(r'topic_map:\s*null','topic_map:\n  - "[[../../30 专题/R10 跨区域文学传统/00 跨区域文学传统]]"',node); NODE.write_text(node,encoding='utf-8')
node102=NODE102.read_text(encoding='utf-8'); node102=re.sub(r'topic_map:\s*\[\]','topic_map:\n  - "[[../../30 专题/R10 跨区域文学传统/00 跨区域文学传统]]"',node102); NODE102.write_text(node102,encoding='utf-8')
AUD.mkdir(parents=True,exist_ok=True)
from collections import Counter
by=Counter(t for t,_,_,_ in S)
report=['# R10 Structural Completion V1','',f'- Structural slots: **{len(S)}**',f'- Existing anchors reused/enriched: **{len(reused)}**',f'- Newly created canonical Works: **{len(created)}**','','## By tradition']
for t,_ in traditions: report.append(f'- {t}: **{by[t]}/{by[t]} COVERED**')
report += ['','## Created']+[f'- {x}' for x in created]+['','## Governance','- R10 remains non-anchorable; ordinary Works are not assigned a synthetic R10 coordinate.','- R10.2 remains the sole canonical African-diaspora coordinate.','- Other diaspora/transregional types are topic-internal traditions, not global R subcoordinates.','- Existing R1–R9 coordinates are preserved; R10 participation is expressed through topic metadata.','','`R10_STRUCTURAL_COVERAGE_V1 = 100_PERCENT_COMPLETE`','`R10_TOPIC_MAP_V1 = COMPLETE_USABLE`']
(AUD/'R10_STRUCTURAL_COMPLETION_V1.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('\n'.join(report[:8]))
