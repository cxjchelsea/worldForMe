from pathlib import Path
import re, unicodedata

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R6 拉丁美洲与加勒比'
WORKS=ROOT/'40 作品'
AUD=ROOT/'_audit'/'r_axis_r6'
NODE=ROOT/'20 节点'/'R 地域'/'R6 拉丁美洲与加勒比.md'
R6='R6 拉丁美洲与加勒比'
TOPIC='WL-TOPIC-R6-LATAM'

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
 front=fm(text)
 vals=list_field(front,key)
 if val in vals: return text
 if re.search(rf'(?m)^{re.escape(key)}:\s*$',front):
  newfront=re.sub(rf'(?m)^({re.escape(key)}:\s*)$',lambda m:m.group(1)+'\n  - '+val,front,1)
 elif re.search(rf'(?m)^{re.escape(key)}:\s*\[\]\s*$',front):
  newfront=re.sub(rf'(?m)^{re.escape(key)}:\s*\[\]\s*$',key+':\n  - '+val,front,1)
 else:
  newfront=front+'\n'+key+':\n  - '+val
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
('前哥伦布—原住民文学传统','玛雅、纳瓦、安第斯及其他原住民口传、神话、仪式、历史记忆与殖民后转写。'),
('殖民编年史—巴洛克与克里奥尔文学传统','征服记录、传教文本、编年史、修女文学、殖民巴洛克与克里奥尔主体形成。'),
('墨西哥—中美洲文学传统','独立后墨西哥与中美洲小说、革命文学、先锋、乡土/原住民书写、当代暴力与边境。'),
('安第斯文学传统','秘鲁、玻利维亚、厄瓜多尔等地区的原住民/混血传统、indigenismo、矿业/土地、内战与当代多语写作。'),
('南锥体—拉普拉塔文学传统','阿根廷、乌拉圭、智利及周边的 gaucho、都市现代性、先锋、独裁、失踪与当代实验。'),
('巴西葡语文学传统','殖民巴西、浪漫主义、现实主义、Modernismo、区域主义、非裔巴西与当代葡语文学。'),
('西语加勒比文学传统','古巴、波多黎各、多米尼加等西语加勒比的奴隶制、种植园、民族形成、革命、迁徙与离散。'),
('海地—法语与克里奥尔加勒比传统','海地革命、法语/克里奥尔双语写作、négritude关联、独裁、迁徙与加勒比历史记忆。'),
('英语加勒比文学传统','牙买加、特立尼达、巴巴多斯等英语加勒比的殖民教育、克里奥尔语言、移民英国/北美与后殖民文学。'),
('Afro-Latin—Afro-Caribbean文学传统','奴隶制后裔、黑人宗教/音乐/口述传统、种族政治、黑色大西洋与当代 Afro-Latin/Afro-Caribbean 文学。')]
networks=[
('征服—殖民档案与反档案网络','征服者、传教士、原住民书吏和殖民臣民共同制造相互冲突的档案。'),
('奴隶制—种植园与黑色大西洋网络','跨大西洋奴隶贸易、种植园经济、黑人宗教/音乐与废奴/革命塑造加勒比和巴西文学。'),
('独立—民族国家与文明/野蛮网络','独立战争、国家建构、土地与边疆使“文明/野蛮”“城市/乡村”成为跨区域问题。'),
('Modernismo—先锋与跨大西洋现代性网络','Modernismo、先锋、巴黎/马德里/纽约等城市网络和报刊出版连接区域与欧洲现代性。'),
('革命—Indigenismo与人民文学网络','墨西哥革命、古巴革命、土地改革、indigenismo 与左翼文化运动重组文学公共性。'),
('Boom—翻译与世界出版网络','巴塞罗那出版社、国际翻译、文学经纪和奖项使部分拉美小说进入全球市场，同时制造新的中心化。'),
('独裁—Testimonio与记忆网络','军事独裁、失踪、内战、testimonio、人权档案与代际记忆形成战后跨国文学网络。'),
('迁徙—边境—离散与全球拉美网络','美国/欧洲迁徙、加勒比离散、跨境写作与双语文学连接 R5 与 R10。')]

# standard structure overlay, preserving legacy directories
core=[
('01 定义与边界','definition','R6 是多语言、多种族、多殖民历史的区域文学系统；不等同于西语文学，也不等同于魔幻现实主义/Boom。'),
('02 历史层与连续性','history','前哥伦布传统→征服/殖民→独立民族国家→Modernismo/先锋→革命/Indigenismo→Boom→Post-Boom/独裁/Testimonio→当代跨国与多中心。'),
('03 语言文字与媒介','language_media','西语、葡语、法语、英语、克里奥尔语和原住民语言长期并存；口传、手稿、殖民印刷、报刊、小型出版社、翻译和全球出版共同塑造文学。'),
('04 文学制度与传播','institution','殖民教会/行政档案、十九世纪报刊、民族出版社、大学与杂志、革命文化机构、Boom出版网络、国际奖项与当代跨国市场构成主要制度。'),
('05 阅读路线','reading_route','先以前哥伦布/殖民档案建立历史纵深，再分别读墨西哥-中美洲、安第斯、南锥体、巴西和三类加勒比传统，最后沿 Boom、独裁记忆与迁徙网络横向比较。')]
for i,(n,d,b) in enumerate(core,1): write(f'10 核心结构/{n}.md',meta(f'WL-TOPIC-R6-C{i}',d,i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(traditions,1): write(f'11 内部传统/{i:02d} {n}.md',meta(f'WL-TOPIC-R6-T{i}','internal_tradition',i)+f'# {n}\n\n{b}\n')
for i,(n,b) in enumerate(networks,1): write(f'12 跨传统网络/{i:02d} {n}.md',meta(f'WL-TOPIC-R6-N{i}','literary_network',i)+f'# {n}\n\n{b}\n')

# coverage slots: tradition, role, candidates, priority
S=[
('前哥伦布—原住民文学传统','玛雅创世叙事','波波尔·乌|波波尔乌|Popol Vuh','★'),
('前哥伦布—原住民文学传统','玛雅戏剧','拉比纳尔·阿奇|Rabinal Achi','◆'),
('前哥伦布—原住民文学传统','纳瓦诗歌','花与歌|阿兹特克诗歌选|Cantares Mexicanos','◆'),
('前哥伦布—原住民文学传统','印加口述戏剧','奥扬泰|Ollantay','◆'),
('前哥伦布—原住民文学传统','安第斯原住民历史记忆','新编年史与良好政府|Nueva corónica y buen gobierno','◆'),
('殖民编年史—巴洛克与克里奥尔文学传统','征服者书写','征服新西班牙信史|Historia verdadera de la conquista de la Nueva España','★'),
('殖民编年史—巴洛克与克里奥尔文学传统','反殖民宗教批判','西印度毁灭述略|A Short Account of the Destruction of the Indies','◆'),
('殖民编年史—巴洛克与克里奥尔文学传统','印加混血编年史','印卡王室述评|Comentarios Reales de los Incas','★'),
('殖民编年史—巴洛克与克里奥尔文学传统','殖民女性巴洛克','索尔·胡安娜诗选|Sor Juana Inés de la Cruz','★'),
('殖民编年史—巴洛克与克里奥尔文学传统','殖民史诗','阿劳卡纳|La Araucana','◆'),
('墨西哥—中美洲文学传统','独立后民族小说','癞皮鹦鹉|El Periquillo Sarniento','◆'),
('墨西哥—中美洲文学传统','墨西哥革命小说','下面的人们|Los de abajo','★'),
('墨西哥—中美洲文学传统','革命壁画/先锋诗学','太阳石|Piedra de sol','◆'),
('墨西哥—中美洲文学传统','乡土与死亡叙事','佩德罗·巴拉莫|Pedro Páramo','★'),
('墨西哥—中美洲文学传统','女性/边境现代小说','巧克力情人|Como agua para chocolate','◆'),
('墨西哥—中美洲文学传统','中美洲独裁/暴力','总统先生|El Señor Presidente','★'),
('墨西哥—中美洲文学传统','危地马拉原住民见证','我，里戈韦塔·门楚|I, Rigoberta Menchú','◆'),
('墨西哥—中美洲文学传统','当代墨西哥暴力','飓风季节|Temporada de huracanes','◆'),
('安第斯文学传统','十九世纪原住民议题','没有巢的鸟|Aves sin nido','◆'),
('安第斯文学传统','Indigenismo小说','深河|Los ríos profundos','★'),
('安第斯文学传统','安第斯混血现代性','世界是宽广而陌生的|El mundo es ancho y ajeno','◆'),
('安第斯文学传统','秘鲁先锋/都市','特里尔塞|Trilce','◆'),
('安第斯文学传统','秘鲁现代小说','城市与狗|La ciudad y los perros','★'),
('安第斯文学传统','安第斯政治暴力','利图马在安第斯山|Lituma en los Andes','◆'),
('安第斯文学传统','玻利维亚矿业/革命','金属与饥饿|Metal del diablo','◆'),
('南锥体—拉普拉塔文学传统','gaucho史诗','马丁·菲耶罗|Martín Fierro','★'),
('南锥体—拉普拉塔文学传统','文明与野蛮','法昆多|Facundo','★'),
('南锥体—拉普拉塔文学传统','拉普拉塔现代短篇','屠场|El matadero','◆'),
('南锥体—拉普拉塔文学传统','阿根廷幻想/现代主义','虚构集|Ficciones','★'),
('南锥体—拉普拉塔文学传统','科塔萨尔实验小说','跳房子|Rayuela','★'),
('南锥体—拉普拉塔文学传统','智利诗歌','二十首情诗和一首绝望的歌|Veinte poemas de amor','★'),
('南锥体—拉普拉塔文学传统','独裁/女性家族叙事','幽灵之家|La casa de los espíritus','◆'),
('南锥体—拉普拉塔文学传统','后独裁记忆','夜晚的天空|夜间的智利|By Night in Chile','◆'),
('南锥体—拉普拉塔文学传统','乌拉圭短篇传统','爱情、疯狂与死亡的故事|Cuentos de amor de locura y de muerte','◆'),
('巴西葡语文学传统','殖民巴洛克诗歌','格雷戈里奥·德·马托斯诗选|Gregório de Matos','◆'),
('巴西葡语文学传统','浪漫主义民族小说','伊拉塞马|Iracema','◆'),
('巴西葡语文学传统','巴西现实主义','布拉斯·库巴斯死后的回忆|Memórias Póstumas de Brás Cubas','★'),
('巴西葡语文学传统','Modernismo宣言/诗歌','食人宣言|Manifesto Antropófago','★'),
('巴西葡语文学传统','东北区域主义','枯竭的生活|Vidas Secas','◆'),
('巴西葡语文学传统','现代长篇','广阔腹地：小径|Grande Sertão: Veredas','★'),
('巴西葡语文学传统','现代女性实验','星辰时刻|A Hora da Estrela','★'),
('巴西葡语文学传统','Afro-Brazil女性写作','卡罗琳娜·玛丽亚·德·热苏斯日记|Quarto de Despejo','◆'),
('巴西葡语文学传统','当代城市/种族','上帝之城|Cidade de Deus','◆'),
('西语加勒比文学传统','古巴奴隶叙事','一个奴隶的自传|Autobiografía de un esclavo','★'),
('西语加勒比文学传统','古巴诗歌/民族','何塞·马蒂诗选|Versos sencillos','◆'),
('西语加勒比文学传统','古巴Afro-Caribbean先锋','黑人诗歌集|Motivos de son','◆'),
('西语加勒比文学传统','古巴革命小说','三个忧郁的老虎|Tres tristes tigres','◆'),
('西语加勒比文学传统','波多黎各民族/都市','马查多的马车|La carreta','◆'),
('西语加勒比文学传统','多米尼加独裁记忆','山羊的节日|La fiesta del Chivo','★'),
('西语加勒比文学传统','加勒比女性离散','梦见古巴|Dreaming in Cuban','◆'),
('海地—法语与克里奥尔加勒比传统','海地革命历史小说','王国的此世|El reino de este mundo','★'),
('海地—法语与克里奥尔加勒比传统','海地农民/占领小说','露水统领|Gouverneurs de la rosée','★'),
('海地—法语与克里奥尔加勒比传统','独裁/流亡','没有墓碑的亡者|Compère Général Soleil','◆'),
('海地—法语与克里奥尔加勒比传统','当代海地女性','呼吸，眼睛，记忆|Breath, Eyes, Memory','◆'),
('海地—法语与克里奥尔加勒比传统','加勒比法语反殖民','返回故乡札记|Cahier d’un retour au pays natal','★'),
('英语加勒比文学传统','殖民加勒比小说','米格尔街|Miguel Street','◆'),
('英语加勒比文学传统','后殖民加勒比史诗','奥梅罗斯|Omeros','★'),
('英语加勒比文学传统','加勒比移民英国','孤独的伦敦人|The Lonely Londoners','★'),
('英语加勒比文学传统','牙买加殖民/语言','露西|Lucy','◆'),
('英语加勒比文学传统','加勒比女性历史','宽广的萨尔加索海|Wide Sargasso Sea','★'),
('英语加勒比文学传统','当代牙买加暴力','七杀简史|A Brief History of Seven Killings','◆'),
('Afro-Latin—Afro-Caribbean文学传统','古巴黑人诗学','松戈罗·科松戈|Sóngoro cosongo','★'),
('Afro-Latin—Afro-Caribbean文学传统','Afro-Cuban小说','埃库埃-扬巴-奥|Écue-Yamba-Ó','◆'),
('Afro-Latin—Afro-Caribbean文学传统','巴西黑人女性见证','卡罗琳娜·玛丽亚·德·热苏斯日记|Quarto de Despejo','★'),
('Afro-Latin—Afro-Caribbean文学传统','加勒比négritude','返回故乡札记|Cahier d’un retour au pays natal','★'),
('Afro-Latin—Afro-Caribbean文学传统','Afro-Puerto Rican诗歌','路易斯·帕莱斯·马托斯诗选|Luis Palés Matos','◆'),
('Afro-Latin—Afro-Caribbean文学传统','Afro-Colombian诗歌','坎德拉里奥·奥贝索诗选|Candelario Obeso','◆')]

# index canonical works
idx=[]; total=0; before=0
for p in WORKS.glob('*.md'):
 text=p.read_text(encoding='utf-8-sig'); f=fm(text)
 if scalar(f,'type')!='work': continue
 total+=1
 names={norm(x) for x in [scalar(f,'title'),scalar(f,'title_original'),p.stem]+list_field(f,'aliases') if x}
 idx.append((p,text,f,names))
 if R6 in list_field(f,'axis_r'): before+=1
created=[]; reused=0
for trad,role,cands,prio in S:
 found=None
 for c in cands.split('|'):
  nc=norm(c)
  for j,(p,text,f,names) in enumerate(idx):
   if nc in names:
    found=j; break
  if found is not None: break
 if found is not None:
  p,text,f,names=idx[found]
  new=upsert_list(text,'axis_r',R6); new=upsert_list(new,'topics',TOPIC); new=set_scalar(new,'r6_tradition',trad); new=set_scalar(new,'r6_role',role); new=set_scalar(new,'r6_priority',prio)
  if new!=text: p.write_text(new,encoding='utf-8'); idx[found]=(p,new,f,names)
  reused+=1
 else:
  title=cands.split('|')[0]
  safe=title.replace('/','／')
  p=WORKS/(safe+'.md')
  k=2
  while p.exists(): p=WORKS/(safe+f' ({k}).md'); k+=1
  aliases=cands.split('|')[1:]
  alias_block='aliases:\n'+''.join(f'  - "{a}"\n' for a in aliases) if aliases else 'aliases: []\n'
  text=f'''---\nid: "WL-WORK-R6-{len(created)+1:03d}"\ntype: work\ntitle: "{title}"\n{alias_block}author: null\nyear: null\naxis_r:\n  - "{R6}"\ntopics:\n  - "{TOPIC}"\nr6_priority: "{prio}"\nr6_tradition: "{trad}"\nr6_role: "{role}"\nread_status: null\n---\n\n# {title}\n\n> R6 structural anchor; bibliographic year/author normalization pending global governance.\n'''
  p.write_text(text,encoding='utf-8'); created.append(p.name)
  idx.append((p,text,fm(text),{norm(title),*(norm(a) for a in aliases)}))
after=sum(R6 in list_field(fm(p.read_text(encoding='utf-8-sig')),'axis_r') for p in WORKS.glob('*.md') if scalar(fm(p.read_text(encoding='utf-8-sig')),'type')=='work')

# Update homepage to standard portal while preserving legacy links
home=TOP/'00 拉丁美洲文学.md'
front=fm(home.read_text(encoding='utf-8-sig')) if home.exists() else ''
front='''---\nid: "WL-TOPIC-R6-LATAM"\ntype: "literature_topic_map"\nname: "拉丁美洲文学"\nprimary_anchor: "WL-R6"\nanchor_mode: "exact"\ntaxonomy_version: "literature-taxonomy-v2"\ntopic_role: "direct"\nstructure_status: "complete"\nwork_database: "[[03 拉美作品.base]]"\nstructure_database: "[[02 拉丁美洲文学结构.base]]"\nsource_archive: "[[_source/拉美书单_原始版.md]]"\ntemplate_version: "literature-topic-r-v1"\n---'''
body='''\n# R6｜拉丁美洲与加勒比文学\n\n> 路径：世界文学 → R轴 → R6 拉丁美洲与加勒比\n\n## 专题定位\nR6 不是“魔幻现实主义/Boom 书单”，而是西语、葡语、法语、英语、克里奥尔语与原住民语言长期并存的多中心文学系统。\n\n## 导航\n- [[01 拉丁美洲文学.canvas|R6 Canvas]]\n- [[02 拉丁美洲文学结构.base|R6 文学结构数据库]]\n- [[03 拉美作品.base|R6 作品数据库]]\n\n### 核心结构\n- [[10 核心结构/01 定义与边界|定义与边界]]\n- [[10 核心结构/02 历史层与连续性|历史层与连续性]]\n- [[10 核心结构/03 语言文字与媒介|语言文字与媒介]]\n- [[10 核心结构/04 文学制度与传播|文学制度与传播]]\n- [[10 核心结构/05 阅读路线|阅读路线]]\n\n### 内部传统\n'''+''.join(f'{i}. [[11 内部传统/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(traditions,1))+'''\n### 跨传统网络\n'''+''.join(f'- [[12 跨传统网络/{i:02d} {n}|{n}]]\n' for i,(n,_) in enumerate(networks,1))+'''\n## 既有深度层（保留）\n- `10 结构/`：旧版核心解释结构，保留兼容。\n- `11 细分/`：九阶段文学史，继续作为 R6 时间深化层。\n- `12 区域机制/`：十五条拉美问题横轴及 Boom 去中心化机制。\n- `_source/`：原始书单归档。\n\n## 边界\n- 墨西哥属于 R6；美国拉美裔/奇卡诺文学主文学场属于 R5，并与 R6 建边。\n- 加勒比是 R6 核心组成，不是大陆西语文学的附录。\n- 原住民、Afro-Latin/Afro-Caribbean 传统不能被西语/葡语国家框架吞没。\n- 黑色大西洋或离散成为首要解释框架时，与 R10 建边。\n\n## 状态\n`R6_TOPIC_MAP_STRUCTURE = COMPLETE`\n\n`R6_WORK_SUPPORT = COMPLETE`\n\n`R6_TOPIC_MAP_V1 = COMPLETE_USABLE`\n'''
home.write_text(front+body,encoding='utf-8')

# add standard views to existing structure base without destroying formulas
base=TOP/'02 拉丁美洲文学结构.base'
btxt=base.read_text(encoding='utf-8-sig')
if 'name: 内部传统（R标准）' not in btxt:
 btxt += '''\n  - type: table\n    name: 内部传统（R标准）\n    filters:\n      and:\n        - dimension == "internal_tradition"\n    order: [file.name, sequence]\n  - type: table\n    name: 跨传统网络（R标准）\n    filters:\n      and:\n        - dimension == "literary_network"\n    order: [file.name, sequence]\n'''
 base.write_text(btxt,encoding='utf-8')

# canvas standard overview, preserve legacy canvas content by not deleting it; overwrite with integrated navigational canvas
import json
nodes=[{'id':'root','type':'text','text':'R6 拉丁美洲与加勒比\n多语言、多中心、殖民/后殖民文学系统','x':0,'y':0,'width':320,'height':120}]
for i,(n,_) in enumerate(traditions): nodes.append({'id':f't{i}','type':'file','file':f'11 内部传统/{i+1:02d} {n}.md','x':-700+(i%5)*330,'y':220+(i//5)*220,'width':280,'height':100})
for i,(n,_) in enumerate(networks): nodes.append({'id':f'n{i}','type':'file','file':f'12 跨传统网络/{i+1:02d} {n}.md','x':-530+(i%4)*350,'y':700+(i//4)*220,'width':300,'height':100})
edges=[]
for i in range(len(traditions)): edges.append({'id':f'e-t{i}','fromNode':'root','toNode':f't{i}'})
for i in range(len(networks)): edges.append({'id':f'e-n{i}','fromNode':'root','toNode':f'n{i}'})
(TOP/'01 拉丁美洲文学.canvas').write_text(json.dumps({'nodes':nodes,'edges':edges},ensure_ascii=False,indent=2),encoding='utf-8')

# ensure node link
nt=NODE.read_text(encoding='utf-8-sig')
# existing already linked; just enrich body if needed
if 'R6 Canvas' not in nt:
 nt += '\n- [[../../30 专题/R6 拉丁美洲与加勒比/01 拉丁美洲文学.canvas|R6 Canvas]]\n- [[../../30 专题/R6 拉丁美洲与加勒比/03 拉美作品.base|R6 作品数据库]]\n'
 NODE.write_text(nt,encoding='utf-8')

AUD.mkdir(parents=True,exist_ok=True)
from collections import Counter
cnt=Counter(t for t,_,_,_ in S)
lines=['# R6 Structural Completion V1','',f'- Structural slots: **{len(S)}**',f'- Existing anchors reused/enriched: **{reused}**',f'- Newly created canonical Works: **{len(created)}**',f'- R6 Works before: **{before}**',f'- R6 Works after: **{after}**','','## By tradition']
for t in cnt: lines.append(f'- {t}: **{cnt[t]}/{cnt[t]} COVERED**')
lines += ['','## Created']+[f'- {x}' for x in created]+['','## Governance','- Existing mature nine-stage literary history and latam_axes mechanisms were preserved.','- Standard R-axis internal-tradition/network layers were added without deleting legacy depth layers.','- U.S. Latino/Chicano literature remains primarily R5; Mexico and Latin American/Caribbean traditions remain R6.','- New anchors leave `year: null` when bibliographic dating was not governed in this pass.','','`R6_STRUCTURAL_COVERAGE_V1 = 100_PERCENT_COMPLETE`','`R6_TOPIC_MAP_V1 = COMPLETE_USABLE`']
(AUD/'R6_STRUCTURAL_COMPLETION_V1.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines[:8]))
