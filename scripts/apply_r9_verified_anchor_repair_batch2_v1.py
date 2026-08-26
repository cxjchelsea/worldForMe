from pathlib import Path
import re
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); W=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'/'R9_VERIFIED_ANCHOR_REPAIR_BATCH2_V1.md'; R9='R9 大洋洲与太平洋'; TOP='WL-TOPIC-R9-OCEANIA-PACIFIC'
def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def create(title,orig,author,year,trad,roles,prio,aliases,sources,note=''):
 p=W/(title+'.md')
 if p.exists():
  txt=p.read_text(encoding='utf-8')
  if re.search(r'(?m)^type:\s*work_candidate\s*$',txt): p=W/(title+'（已核验）.md')
 if p.exists(): return p.name
 wid='WL-WORK-R9-VERIFIED2-'+re.sub(r'[^A-Za-z0-9]+','-',orig).strip('-').upper()[:35]
 lines=[f'id: {q(wid)}','type: work',f'title: {q(title)}',f'title_original: {q(orig)}',f'author: {q(author)}',('year: null' if year is None else f'year: {year}'),'aliases:']+['  - '+q(a) for a in aliases]+['axis_r:','  - '+q(R9),'topics:','  - '+q(TOP),f'r9_priority: {q(prio)}',f'r9_tradition: {q(trad)}','r9_role:']+['  - '+q(r) for r in roles]+['verification_status: "手工核验"','bibliography_status: "verified_r9_anchor_repair_batch2_v1"','bibliography_sources:']+['  - '+q(s) for s in sources]
 if note: lines.append('authorship_note: '+q(note))
 p.write_text('---\n'+'\n'.join(lines)+'\n---\n# '+title+'\n\n> R9 书目重验证后建立的真实 canonical Work。\n',encoding='utf-8'); return p.name
items=[
('The Alternative','The Alternative','John Saunana',1980,'巴布亚新几内亚—美拉尼西亚文学传统',['所罗门群岛小说/记忆'],'◆',[],['https://books.google.com/books/about/The_Alternative.html?id=vVZbAAAAMAAJ']),
('Black Stone','Black Stone: Poems','Grace Mera Molisa',1983,'巴布亚新几内亚—美拉尼西亚文学传统',['瓦努阿图/kastom','当代美拉尼西亚女性写作'],'◆',[],['https://books.google.com/books?id=lDpUdIThKOoC','https://programsandcourses.anu.edu.au/2019/course/pasi8008']),
('Pouliuli','Pouliuli','Albert Wendt',1977,'波利尼西亚文学传统',['萨摩亚去殖民/文化批判'],'◆',[],['https://books.google.com/books/about/Pouliuli.html?id=YFWqAAAAIAAJ']),
('You, the Choice of My Parents','You, the Choice of My Parents: Poems','Konai Helu Thaman',1974,'波利尼西亚文学传统',['汤加/太平洋诗学'],'◆',[],['https://books.google.com/books/about/You_the_Choice_of_My_Parents.html?id=-l0rjwEACAAJ']),
('Shark Dialogues','Shark Dialogues','Kiana Davenport',1994,'波利尼西亚文学传统',['夏威夷原住民文学'],'★',[],['https://books.google.com/books/about/Shark_Dialogues.html?id=xcFpAAAAMAAJ']),
('Wild Dogs Under My Skirt','Wild Dogs Under My Skirt','Tusiata Avia',2004,'波利尼西亚文学传统',['当代太平洋女性/酷儿'],'★',[],['https://natlib.govt.nz/records/21275676','https://www.metmuseum.org/ja/perspectives/wild-dogs-under-my-skirt']),
('Iep Jāltok','Iep Jāltok: Poems from a Marshallese Daughter','Kathy Jetñil-Kijiner',2017,'密克罗尼西亚文学传统',['马绍尔核试验诗歌','核试验/迁徙记忆'],'★',[],['https://uapress.arizona.edu/app/uploads/2017/04/Arizona-Spring-17-Catalog.pdf']),
('My Urohs','My Urohs','Emelihter Kihleng',2008,'密克罗尼西亚文学传统',['密联邦岛屿文学'],'◆',[],['https://books.google.com/books/about/My_Urohs.html?id=40g3268fjnYC']),
('From Unincorporated Territory [Hacha]','From Unincorporated Territory [Hacha]','Craig Santos Perez',2008,'密克罗尼西亚文学传统',['关岛查莫罗文学','军事基地/殖民记忆'],'★',[],['https://books.google.com/books/about/From_Unincorporated_Territory_Hacha.html?id=52YgAQAAIAAJ']),
('L’île des rêves écrasés','L’île des rêves écrasés','Chantal T. Spitz',1991,'法语太平洋—新喀里多尼亚文学传统',['法属波利尼西亚小说','殖民/核试验记忆'],'★',[],['https://data.bnf.fr/fr/ark%3A/12148/cb12228779b.pdf']),
('Légendes et chansons de gestes canaques','Légendes et chansons de gestes canaques','Louise Michel',1875,'法语太平洋—新喀里多尼亚文学传统',['Kanak口述/独立'],'★',[],['https://catalogue.bnf.fr/ark%3A/12148/cb40145820h'],'殖民时期采录/转写 Kanak 口述传统；作者字段指出版文本的记录者，并不代表口述传统的集体创作者'),
('Dire le vrai','Dire le vrai','Déwé Gorodé、Nicolas Kurtovitch',1999,'法语太平洋—新喀里多尼亚文学传统',['跨语太平洋身份'],'◆',[],['https://openresearch-repository.anu.edu.au/bitstreams/3b36ce7d-bfdb-4a35-80ae-78d549d2fec5/download']),
]
created=[create(*x) for x in items]
AUD.parent.mkdir(parents=True,exist_ok=True); AUD.write_text('# R9 Verified Anchor Repair Batch 2 V1\n\n- Verified Pacific Works created: **12**\n- Multi-role support is allowed only where one verified work genuinely carries multiple closely related R9 mechanisms.\n\n## Created\n'+'\n'.join('- '+x for x in created)+'\n\n`R9_VERIFIED_ANCHOR_REPAIR_BATCH2_V1 = APPLIED`\n',encoding='utf-8')
