from pathlib import Path
import re
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); W=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'/'R9_VERIFIED_ANCHOR_REPAIR_BATCH1_V1.md'; R9='R9 大洋洲与太平洋'; TOP='WL-TOPIC-R9-OCEANIA-PACIFIC'
def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def create(title,orig,author,year,trad,role,prio,aliases,sources,note=''):
 p=W/(title+'.md')
 if p.exists():
  text=p.read_text(encoding='utf-8')
  # Existing title may be a quarantined candidate; do not overwrite it in-place with a different entity unless exact title is the same intended work.
  if re.search(r'(?m)^type:\s*work_candidate\s*$',text): p=W/(title+'（已核验）.md')
 if p.exists(): return p.name
 wid='WL-WORK-R9-VERIFIED1-'+re.sub(r'[^A-Za-z0-9]+','-',orig).strip('-').upper()[:36]
 lines=[f'id: {q(wid)}','type: work',f'title: {q(title)}',f'title_original: {q(orig)}',f'author: {q(author)}',('year: null' if year is None else f'year: {year}'),'aliases:']+['  - '+q(a) for a in aliases]+['axis_r:','  - '+q(R9),'topics:','  - '+q(TOP),f'r9_priority: {q(prio)}',f'r9_tradition: {q(trad)}','r9_role:','  - '+q(role),'verification_status: "手工核验"','bibliography_status: "verified_r9_anchor_repair_batch1_v1"','bibliography_sources:']+['  - '+q(s) for s in sources]
 if note: lines.append('authorship_note: '+q(note))
 p.write_text('---\n'+'\n'.join(lines)+'\n---\n# '+title+'\n\n> R9 书目重验证后建立的真实 canonical Work。\n',encoding='utf-8'); return p.name
items=[
('Quintus Servinton','Quintus Servinton: A Tale Founded upon Incidents of Real Occurrence','Henry Savery',1831,'澳大利亚殖民—国家文学传统','殖民早期书写','◆',[],['https://www.nma.gov.au/defining-moments/resources/quintus-servinton','https://adb.anu.edu.au/biography/savery-henry-2632']),
('While the Billy Boils','While the Billy Boils','Henry Lawson',1896,'澳大利亚殖民—国家文学传统','现实主义短篇/丛林文学','★',['当水壶烧开时'],['https://www.nla.gov.au/sites/default/files/a_nation_imagined_exhibition_checklist_presented_by_the_national_library_of_australia_and_art_gallery_of_new_south_wales_1.pdf']),
('Myths and Legends of Torres Strait','Myths and Legends of Torres Strait','Margaret Lawrie',1970,'澳大利亚原住民—托雷斯海峡文学传统','Torres Strait/海洋原住民','◆',['托雷斯海峡神话与传说'],['https://collections.slq.qld.gov.au/guide/tr1791/overview','https://www.slq.qld.gov.au/collections/family-history/whos-your-mob/margaret-lawrie-collection'],'采录、整理与编译；叙事来源于 Torres Strait Islander 讲述者与社区传统'),
('Myths and Legends of Maoriland','Myths and Legends of Maoriland','A. W. Reed',1946,'毛利文学传统','毛利神话/口传','★',['Māori Myths & Legendary Tales','毛利神话与传说'],['https://natlib.govt.nz/records/21616242'],'现代采录/改写文本；所承载神话属于毛利集体口传传统'),
('The Matriarch','The Matriarch','Witi Ihimaera',1986,'毛利文学传统','主权/历史重写','◆',['女族长'],['https://teara.govt.nz/en/interactive/41946/new-zealand-fiction-award-winners']),
]
created=[create(*x) for x in items]
AUD.parent.mkdir(parents=True,exist_ok=True); AUD.write_text('# R9 Verified Anchor Repair Batch 1 V1\n\n- Verified Works created: **5**\n\n## Created\n'+'\n'.join('- '+x for x in created)+'\n\n`R9_VERIFIED_ANCHOR_REPAIR_BATCH1_V1 = APPLIED`\n',encoding='utf-8')
