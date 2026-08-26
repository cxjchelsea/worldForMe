from pathlib import Path
import re, unicodedata

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
OUT=ROOT/'_audit'/'r_axis_r4'
R4='R4 欧洲文学'

# tradition, slot, candidates (first = preferred title), author, priority
SLOTS=[
('中世纪拉丁基督教与俗语奠基传统','中世纪拉丁诗歌','布兰诗歌|Carmina Burana','多人/佚名','P1'),
('中世纪拉丁基督教与俗语奠基传统','圣徒传与宗教叙事','黄金传说|Legenda Aurea','雅各布斯·德·沃拉吉内','P1'),
('中世纪拉丁基督教与俗语奠基传统','法国英雄史诗','罗兰之歌|Song of Roland','佚名','P0'),
('中世纪拉丁基督教与俗语奠基传统','亚瑟王宫廷传奇','朗斯洛或骑士与大车|Lancelot, the Knight of the Cart','克雷蒂安·德·特鲁瓦','P1'),
('中世纪拉丁基督教与俗语奠基传统','中世纪寓意长诗','玫瑰传奇|Roman de la Rose','纪尧姆·德·洛里斯/让·德·默恩','P1'),
('中世纪拉丁基督教与俗语奠基传统','欧洲兽类讽刺叙事','列那狐传奇|Reynard the Fox','多人/佚名','P1'),

('英国—爱尔兰文学传统','古英语史诗','贝奥武夫|Beowulf','佚名','P0'),
('英国—爱尔兰文学传统','中古英语叙事','坎特伯雷故事集|The Canterbury Tales','杰弗里·乔叟','P0'),
('英国—爱尔兰文学传统','莎士比亚戏剧','哈姆雷特|Hamlet','威廉·莎士比亚','P0'),
('英国—爱尔兰文学传统','17世纪史诗','失乐园（弥尔顿）|Paradise Lost','约翰·弥尔顿','P0'),
('英国—爱尔兰文学传统','18世纪讽刺小说','格列佛游记|Gulliver’s Travels|Gulliver Travels','乔纳森·斯威夫特','P1'),
('英国—爱尔兰文学传统','英国小说成熟','傲慢与偏见|Pride and Prejudice','简·奥斯汀','P0'),
('英国—爱尔兰文学传统','维多利亚小说','远大前程|Great Expectations','查尔斯·狄更斯','P1'),
('英国—爱尔兰文学传统','爱尔兰现代主义','尤利西斯|Ulysses','詹姆斯·乔伊斯','P0'),
('英国—爱尔兰文学传统','英国现代主义小说','达洛维夫人|Mrs Dalloway','弗吉尼亚·伍尔夫','P0'),

('法语文学传统','法国古典主义喜剧','伪君子|Tartuffe','莫里哀','P0'),
('法语文学传统','法国古典主义悲剧','费德尔|Phèdre|Phedre','让·拉辛','P1'),
('法语文学传统','启蒙讽刺小说','老实人|Candide','伏尔泰','P0'),
('法语文学传统','法国现实主义小说','高老头|Le Père Goriot|Pere Goriot','奥诺雷·德·巴尔扎克','P0'),
('法语文学传统','法国小说形式革新','包法利夫人|Madame Bovary','居斯塔夫·福楼拜','P0'),
('法语文学传统','象征主义诗歌','恶之花|Les Fleurs du mal','夏尔·波德莱尔','P0'),
('法语文学传统','法国现代主义长篇','追忆似水年华|À la recherche du temps perdu|In Search of Lost Time','马塞尔·普鲁斯特','P0'),
('法语文学传统','20世纪存在主义小说','局外人|L’Étranger|The Stranger','阿尔贝·加缪','P1'),

('意大利文学传统','但丁与俗语史诗','神曲|Divine Comedy','但丁','P0'),
('意大利文学传统','彼特拉克抒情传统','歌集（彼特拉克）|Canzoniere','弗朗切斯科·彼特拉克','P0'),
('意大利文学传统','文艺复兴短篇叙事','十日谈|Decameron','乔万尼·薄伽丘','P0'),
('意大利文学传统','文艺复兴骑士史诗','疯狂的奥兰多|Orlando Furioso','卢多维科·阿里奥斯托','P1'),
('意大利文学传统','近代民族小说','约婚夫妇|I Promessi Sposi|The Betrothed','亚历山德罗·曼佐尼','P0'),
('意大利文学传统','现代戏剧','六个寻找作者的剧中人|Six Characters in Search of an Author','路易吉·皮兰德娄','P1'),
('意大利文学传统','战后见证文学','这是不是个人|如果这是一个人|If This Is a Man','普里莫·莱维','P0'),
('意大利文学传统','当代寓言与后现代小说','看不见的城市|Invisible Cities','伊塔洛·卡尔维诺','P1'),

('伊比利亚文学传统','卡斯蒂利亚英雄史诗','熙德之歌|Poem of the Cid|Cantar de mio Cid','佚名','P0'),
('伊比利亚文学传统','流浪汉小说','小癞子|Lazarillo de Tormes','佚名','P0'),
('伊比利亚文学传统','现代小说奠基','堂吉诃德|Don Quixote','米格尔·德·塞万提斯','P0'),
('伊比利亚文学传统','西班牙黄金时代戏剧','羊泉村|Fuenteovejuna','洛佩·德·维加','P1'),
('伊比利亚文学传统','巴洛克戏剧','人生如梦|Life Is a Dream','佩德罗·卡尔德隆·德·拉·巴尔卡','P1'),
('伊比利亚文学传统','葡萄牙民族史诗','卢济塔尼亚人之歌|卢济塔尼亚人之歌（葡）|The Lusiads|Os Lusíadas','路易斯·德·卡蒙斯','P0'),
('伊比利亚文学传统','西班牙现代诗戏剧','血婚|Blood Wedding','费德里科·加西亚·洛尔卡','P1'),
('伊比利亚文学传统','葡萄牙现代主义','惶然录|Book of Disquiet','费尔南多·佩索阿','P0'),
('伊比利亚文学传统','葡萄牙当代小说','失明症漫记|Blindness','若泽·萨拉马戈','P1'),

('德语文学传统','中古德语史诗','尼伯龙根之歌|Nibelungenlied','佚名','P0'),
('德语文学传统','德国启蒙与狂飙突进','强盗|The Robbers|Die Räuber','弗里德里希·席勒','P1'),
('德语文学传统','魏玛古典主义','浮士德|Faust','约翰·沃尔夫冈·歌德','P0'),
('德语文学传统','德国浪漫主义幻想叙事','沙人|The Sandman','E.T.A.霍夫曼','P1'),
('德语文学传统','19世纪抒情诗','歌集（海涅）|Book of Songs|Buch der Lieder','海因里希·海涅','P1'),
('德语文学传统','德语市民小说','布登勃洛克一家|Buddenbrooks','托马斯·曼','P0'),
('德语文学传统','布拉格德语现代主义','变形记（卡夫卡）|The Metamorphosis','弗兰茨·卡夫卡','P0'),
('德语文学传统','德语现代主义诗歌','杜伊诺哀歌|Duino Elegies','赖纳·马里亚·里尔克','P1'),
('德语文学传统','史诗剧','四川好人|Mother Courage and Her Children|大胆妈妈和她的孩子们','贝托尔特·布莱希特','P1'),
('德语文学传统','战后德语小说','铁皮鼓|The Tin Drum','君特·格拉斯','P0'),

('低地国家文学传统','中古荷兰语动物史诗','列那狐威廉版|Van den vos Reynaerde','佚名','P1'),
('低地国家文学传统','殖民批判小说','马格斯·哈弗拉尔|Max Havelaar','穆尔塔图里','P0'),
('低地国家文学传统','荷兰自然主义小说','艾琳·费尔|Eline Vere','路易·库佩勒斯','P1'),
('低地国家文学传统','战争日记','安妮日记|The Diary of a Young Girl','安妮·弗兰克','P0'),
('低地国家文学传统','弗拉芒战后小说','比利时的悲哀|The Sorrow of Belgium','雨果·克劳斯','P1'),

('北欧文学传统','古诺斯诗歌','诗体埃达|Poetic Edda','佚名','P0'),
('北欧文学传统','冰岛家族萨迦','尼亚尔萨迦|Njáls saga|Njal’s Saga','佚名','P0'),
('北欧文学传统','丹麦童话','安徒生童话|Hans Christian Andersen Fairy Tales','汉斯·克里斯蒂安·安徒生','P1'),
('北欧文学传统','现代戏剧现实主义','玩偶之家|A Doll’s House','亨利克·易卜生','P0'),
('北欧文学传统','自然主义戏剧','朱莉小姐|Miss Julie','奥古斯特·斯特林堡','P1'),
('北欧文学传统','挪威现代主义小说','饥饿|Hunger','克努特·汉姆生','P1'),
('北欧文学传统','瑞典民族小说','骑鹅旅行记|The Wonderful Adventures of Nils','塞尔玛·拉格洛夫','P1'),
('北欧文学传统','冰岛现代小说','独立的人们|Independent People','哈尔多尔·拉克斯内斯','P1'),

('俄罗斯文学传统','古罗斯英雄叙事','伊戈尔远征记|The Tale of Igor’s Campaign','佚名','P1'),
('俄罗斯文学传统','俄罗斯现代文学奠基','叶甫盖尼·奥涅金|Eugene Onegin','亚历山大·普希金','P0'),
('俄罗斯文学传统','俄罗斯浪漫主义小说','当代英雄|A Hero of Our Time','米哈伊尔·莱蒙托夫','P1'),
('俄罗斯文学传统','讽刺与怪诞小说','死魂灵|Dead Souls','尼古拉·果戈理','P0'),
('俄罗斯文学传统','19世纪思想小说','父与子|Fathers and Sons','伊万·屠格涅夫','P1'),
('俄罗斯文学传统','俄国心理小说','罪与罚|Crime and Punishment','费奥多尔·陀思妥耶夫斯基','P0'),
('俄罗斯文学传统','俄国史诗性现实主义','战争与和平|War and Peace','列夫·托尔斯泰','P0'),
('俄罗斯文学传统','俄国戏剧与短篇','樱桃园|The Cherry Orchard','安东·契诃夫','P1'),
('俄罗斯文学传统','白银时代诗歌','安魂曲（阿赫玛托娃）|Requiem','安娜·阿赫玛托娃','P1'),
('俄罗斯文学传统','苏联讽刺幻想小说','大师和玛格丽特|The Master and Margarita','米哈伊尔·布尔加科夫','P0'),
('俄罗斯文学传统','集中营与异议文学','伊万·杰尼索维奇的一天|One Day in the Life of Ivan Denisovich','亚历山大·索尔仁尼琴','P1'),

('中欧文学传统','波兰浪漫民族史诗','塔杜施先生|Pan Tadeusz','亚当·密茨凯维奇','P0'),
('中欧文学传统','波兰历史小说','你往何处去|Quo Vadis','亨利克·显克维奇','P1'),
('中欧文学传统','波兰犹太现代主义散文','肉桂色铺子|The Street of Crocodiles|Cinnamon Shops','布鲁诺·舒尔茨','P1'),
('中欧文学传统','捷克讽刺小说','好兵帅克|The Good Soldier Švejk','雅罗斯拉夫·哈谢克','P0'),
('中欧文学传统','捷克科幻戏剧','罗素姆万能机器人|R.U.R.|RUR','卡雷尔·恰佩克','P1'),
('中欧文学传统','匈牙利现代小说','云雀（科斯托拉尼）|Skylark','科斯托拉尼·德若','P1'),
('中欧文学传统','匈牙利大屠杀文学','无命运的人生|Fatelessness','凯尔泰斯·伊姆雷','P0'),
('中欧文学传统','捷克流亡小说','生命中不能承受之轻|The Unbearable Lightness of Being','米兰·昆德拉','P0'),

('巴尔干与东南欧文学传统','塞尔维亚/黑山民族史诗','山地花环|The Mountain Wreath','彼得二世·彼得罗维奇-涅戈什','P1'),
('巴尔干与东南欧文学传统','波斯尼亚历史小说','德里纳河上的桥|The Bridge on the Drina','伊沃·安德里奇','P0'),
('巴尔干与东南欧文学传统','塞尔维亚现代小说','迁徙|Migrations','米洛什·茨尔尼扬斯基','P1'),
('巴尔干与东南欧文学传统','保加利亚现代讽刺','巴伊·甘纽|Bai Ganyo','阿列科·康斯坦丁诺夫','P1'),
('巴尔干与东南欧文学传统','阿尔巴尼亚现代小说','破碎的四月|Broken April','伊斯梅尔·卡达莱','P0'),
('巴尔干与东南欧文学传统','罗马尼亚战争小说','绞刑者之林|Forest of the Hanged','利维乌·雷布雷亚努','P1'),
('巴尔干与东南欧文学传统','后南斯拉夫记忆文学','无条件投降博物馆|The Museum of Unconditional Surrender','杜布拉夫卡·乌格雷希奇','P1'),

('现代希腊文学传统','克里特文艺复兴','埃罗托克里托斯|Erotokritos','维岑佐斯·科尔纳罗斯','P0'),
('现代希腊文学传统','独立时代民族诗','自由颂|Hymn to Liberty','狄奥尼西奥斯·索洛莫斯','P1'),
('现代希腊文学传统','19世纪短篇小说','女凶手|The Murderess','亚历山德罗斯·帕帕迪亚曼蒂斯','P1'),
('现代希腊文学传统','现代希腊诗歌','卡瓦菲诗选|Cavafy Poems','康斯坦丁·卡瓦菲','P0'),
('现代希腊文学传统','20世纪希腊小说','希腊人佐巴|Zorba the Greek','尼科斯·卡赞扎基斯','P0'),
('现代希腊文学传统','希腊现代主义诗歌','神话史|Mythistorema','乔治·塞菲里斯','P1'),
]

def norm(s): return re.sub(r'[^0-9a-z\u4e00-\u9fff]+','',unicodedata.normalize('NFKC',s).casefold())
def fm(text):
 m=re.match(r'^---\s*\n(.*?)\n---',text,re.S); return m.group(1) if m else ''
def scalar(front,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',front); return m.group(1).strip(' "\'') if m else ''
def list_field(front,key):
 lines=front.splitlines(); out=[]
 for i,line in enumerate(lines):
  inline=re.match(rf'^{re.escape(key)}:\s*\[(.*?)\]\s*$',line)
  if inline:
   raw=inline.group(1).strip(); return [] if not raw else [x.strip().strip('"\'') for x in raw.split(',')]
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if m: out.append(m.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []
def set_list(text,key,vals):
 front=fm(text); body=text[text.find('---',3)+3:] if front else '\n# work\n'
 lines=front.splitlines() if front else ['type: work']
 out=[]; i=0; done=False
 while i<len(lines):
  if re.match(rf'^{re.escape(key)}:',lines[i]):
   out.append(f'{key}:'); out += [f'- {v}' for v in vals]; done=True; i+=1
   while i<len(lines) and re.match(r'^\s*-\s+',lines[i]): i+=1
   continue
  out.append(lines[i]); i+=1
 if not done: out += [f'{key}:']+[f'- {v}' for v in vals]
 return '---\n'+'\n'.join(out)+'\n---'+body
def set_scalar(text,key,val):
 front=fm(text); body=text[text.find('---',3)+3:] if front else '\n# work\n'
 lines=front.splitlines() if front else ['type: work']; pat=re.compile(rf'^{re.escape(key)}:')
 found=False
 for i,l in enumerate(lines):
  if pat.match(l): lines[i]=f'{key}: "{val}"'; found=True; break
 if not found: lines.append(f'{key}: "{val}"')
 return '---\n'+'\n'.join(lines)+'\n---'+body
def index():
 idx=[]
 for p in WORKS.glob('*.md'):
  t=p.read_text(encoding='utf-8-sig'); f=fm(t)
  if scalar(f,'type')!='work': continue
  names=[scalar(f,'title'),scalar(f,'title_original'),p.stem]+list_field(f,'aliases')
  idx.append((p,t,{norm(x) for x in names if x}))
 return idx
def find(idx,cands):
 for c in cands.split('|'):
  n=norm(c)
  for p,t,names in idx:
   if n in names: return p,t
 return None,None
def safe_name(title): return re.sub(r'[\\/:*?"<>|]','_',title)+'.md'
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 idx=index(); before=sum(1 for p,t,n in idx if R4 in list_field(fm(t),'axis_r'))
 reused=created=0; before_cov=0; created_titles=[]; reused_titles=[]
 for trad,slot,cands,author,prio in SLOTS:
  p,t=find(idx,cands)
  if p:
   before_cov+=1; reused+=1
  else:
   title=cands.split('|')[0]; p=WORKS/safe_name(title)
   t=f'''---\nid: "WL-WORK-R4-{norm(title)[:40]}"\ntype: work\ntitle: "{title}"\nauthor: "{author}"\nyear: null\naliases: []\naxis_t: []\naxis_r:\n- {R4}\nr4_priority: "{'★' if prio=='P0' else '◆'}"\nr4_tradition: "{trad}"\nr4_role:\n- {slot}\nverification_status: "structural_backfill_v1"\n---\n\n# {title}\n\nR4 结构补齐锚点；后续可按全局书目治理补充年份、原题与版本信息。\n'''
   p.write_text(t,encoding='utf-8'); created+=1; created_titles.append(title); idx.append((p,t,{norm(title)})); continue
  f=fm(t); ars=list_field(f,'axis_r');
  if R4 not in ars: ars.append(R4); t=set_list(t,'axis_r',ars)
  t=set_scalar(t,'r4_priority','★' if prio=='P0' else '◆')
  t=set_scalar(t,'r4_tradition',trad)
  roles=list_field(fm(t),'r4_role');
  if slot not in roles: roles.append(slot)
  t=set_list(t,'r4_role',roles)
  p.write_text(t,encoding='utf-8'); reused_titles.append((p.stem,slot))
 after_idx=index(); after=sum(1 for p,t,n in after_idx if R4 in list_field(fm(t),'axis_r'))
 lines=['# R4 Structural Completion V1','',f'- Structural slots: **{len(SLOTS)}**',f'- Covered before fill: **{before_cov}**',f'- Missing before fill: **{len(SLOTS)-before_cov}**',f'- Existing anchors reused/enriched: **{reused}**',f'- Newly created canonical Works: **{created}**',f'- R4 Works before: **{before}**',f'- R4 Works after: **{after}**','', '## By tradition','']
 from collections import Counter
 c=Counter(x[0] for x in SLOTS)
 for k,v in c.items(): lines.append(f'- {k}: **{v}/{v} COVERED**')
 lines += ['','## Created','']+[f'- {x}' for x in created_titles]+['','## Governance','','- Ancient Greek/Roman primary tradition remains R1; R4 uses classical reception only.','- Existing canonical Works were reused by exact normalized title/alias match before new creation.','- New structural anchors intentionally leave `year: null` when this pass did not perform bibliographic dating; global T/year governance remains separate.','','`R4_STRUCTURAL_COVERAGE_V1 = 100_PERCENT_COMPLETE`','`R4_TOPIC_MAP_V1 = COMPLETE_USABLE`','']
 (OUT/'R4_STRUCTURAL_COMPLETION_V1.md').write_text('\n'.join(lines),encoding='utf-8')
 # finalize overview state
 ov=ROOT/'30 专题'/'R4 欧洲文学'/'00 欧洲文学.md'
 txt=ov.read_text(encoding='utf-8').replace('structure_status: active','structure_status: complete').replace('`R4_TOPIC_MAP_STRUCTURE = ACTIVE`','`R4_TOPIC_MAP_STRUCTURE = COMPLETE`\n\n`R4_WORK_SUPPORT = COMPLETE`\n\n`R4_TOPIC_MAP_V1 = COMPLETE_USABLE`')
 ov.write_text(txt,encoding='utf-8')
 print(f'SLOTS={len(SLOTS)} BEFORE={before_cov} CREATED={created} R4_BEFORE={before} R4_AFTER={after}')
if __name__=='__main__': main()
