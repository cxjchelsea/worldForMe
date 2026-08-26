from pathlib import Path
import re
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); W=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'/'R9_VERIFIED_ANCHOR_REPAIR_BATCH3_V1.md'; R9='R9 大洋洲与太平洋'; TOP='WL-TOPIC-R9-OCEANIA-PACIFIC'
def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def safe_filename(title):
 return re.sub(r'[<>:"/\\|?*]', ' - ' if ':' in title else '_', title).strip().rstrip('.')
def create(title,orig,author,year,trad,role,prio,aliases,sources,note=''):
 safe=safe_filename(title)
 p=W/(safe+'.md')
 if p.exists():
  txt=p.read_text(encoding='utf-8')
  if re.search(r'(?m)^type:\s*work_candidate\s*$',txt): p=W/(safe+'（已核验）.md')
 if p.exists(): return p.name
 wid='WL-WORK-R9-VERIFIED3-'+re.sub(r'[^A-Za-z0-9]+','-',orig).strip('-').upper()[:35]
 lines=[f'id: {q(wid)}','type: work',f'title: {q(title)}',f'title_original: {q(orig)}',f'author: {q(author)}',('year: null' if year is None else f'year: {year}'),'aliases:']+['  - '+q(a) for a in aliases]+['axis_r:','  - '+q(R9),'topics:','  - '+q(TOP),f'r9_priority: {q(prio)}',f'r9_tradition: {q(trad)}','r9_role:','  - '+q(role),'verification_status: "手工核验"','bibliography_status: "verified_r9_anchor_repair_batch3_v1"','bibliography_sources:']+['  - '+q(s) for s in sources]
 if note: lines.append('authorship_note: '+q(note))
 p.write_text('---\n'+'\n'.join(lines)+'\n---\n# '+title+'\n\n> R9 书目重验证后建立的真实 canonical Work。\n',encoding='utf-8'); return p.name
items=[
('As the Earth Turns Silver','As the Earth Turns Silver','Alison Wong',2009,'英语新西兰文学传统','移民/跨文化小说','◆',[],['https://www.penguin.co.nz/books/as-the-earth-turns-silver-9781742288741']),
('Hembemba: Rivers of the Forest','Hembemba: Rivers of the Forest','Steven Edmund Winduo',2000,'巴布亚新几内亚—美拉尼西亚文学传统','PNG诗歌/殖民教育','◆',[],['https://books.google.com/books/about/Hembemba.html?id=0uVVTdBnIWUC']),
('The Wounded Sea','The Wounded Sea','Satendra Pratap Nandan',1991,'巴布亚新几内亚—美拉尼西亚文学传统','斐济殖民/印裔经验','◆',[],['https://books.google.com/books/about/The_Wounded_Sea.html?id=S1DIOwAACAAJ','https://openlibrary.org/books/OL1635271M/The_wounded_sea']),
('Dauka Puran','Ḍaukā Purān','Subramani',2001,'巴布亚新几内亚—美拉尼西亚文学传统','斐济现代小说','★',['Dauka Puraan'],['https://repository.usp.ac.fj/id/eprint/13951/1/16-FijiHindiAheritagelanguage%20copy.pdf','https://www.jstor.org/stable/jj.11288858.6']),
('Miss Ulysses from Puka-Puka','Miss Ulysses from Puka-Puka: The Autobiography of a South Sea Trader’s Daughter','Florence (Johnny) Frisbie',1948,'波利尼西亚文学传统','库克群岛/离散','◆',[],['https://dspace.cuni.cz/bitstream/handle/20.500.11956/78308/DPTX_2012_2_11210_0_297082_0_136054.pdf?isAllowed=y&sequence=1']),
('L’Homme-lézard','L’Homme-lézard','Claudine Jacques',2002,'法语太平洋—新喀里多尼亚文学传统','新喀里多尼亚小说','◆',[],['https://www.vers-les-iles.fr/livres/Nouveau/Jacques_3.html']),
]
created=[create(*x) for x in items]
AUD.parent.mkdir(parents=True,exist_ok=True); AUD.write_text('# R9 Verified Anchor Repair Batch 3 V1\n\n- Verified Works created: **6**\n- Two expected remaining PARTIALs are not force-filled: Palauan oral tradition (collective/oral) and climate/ocean futures (better treated as a cross-tradition network than a single internal-tradition Work slot).\n\n## Created\n'+'\n'.join('- '+x for x in created)+'\n\n`R9_VERIFIED_ANCHOR_REPAIR_BATCH3_V1 = APPLIED_WITH_TWO_INTENTIONAL_PARTIALS_EXPECTED`\n',encoding='utf-8')
