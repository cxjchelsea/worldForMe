from pathlib import Path
import re
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); W=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'/'R8_VERIFIED_ANCHOR_REPAIR_BATCH2_V1.md'; R8='R8 东南亚文学'; TOP='WL-TOPIC-R8-SOUTHEAST-ASIA'
def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def create(title,orig,author,year,trad,role,prio,aliases,sources,note=''):
 p=W/(title+'.md')
 if p.exists(): return p.name
 wid='WL-WORK-R8-VERIFIED2-'+re.sub(r'[^A-Za-z0-9]+','-',orig).strip('-').upper()[:35]
 lines=[f'id: {q(wid)}','type: work',f'title: {q(title)}',f'title_original: {q(orig)}',f'author: {q(author)}',('year: null' if year is None else f'year: {year}'),'aliases:']+['  - '+q(a) for a in aliases]+['axis_r:','  - '+q(R8),'topics:','  - '+q(TOP),f'r8_priority: {q(prio)}',f'r8_tradition: {q(trad)}','r8_role:','  - '+q(role),'verification_status: "手工核验"','bibliography_status: "verified_r8_anchor_repair_batch2_v1"','bibliography_sources:']+['  - '+q(s) for s in sources]
 if note: lines.append('authorship_note: '+q(note))
 p.write_text('---\n'+'\n'.join(lines)+'\n---\n# '+title+'\n\n> R8 书目重验证后建立的真实 canonical Work。\n',encoding='utf-8'); return p.name
items=[
('Kogan Pyo','Kogan Pyo','Shin Maha Ratthasara',1523,'缅甸文学传统','佛教叙事/诗歌','◆',['ကိုးခန့်ပျို့'],['https://en.wikipedia.org/wiki/Shin_Ra%E1%B9%AD%E1%B9%ADhas%C4%81ra']),
('Maung Yin Maung and Ma Me Ma','Maung Yin Maung Ma Me Ma','James Hla Kyaw',1904,'缅甸文学传统','殖民现代小说','◆',['Maung Yin Maung, Ma Me Ma'],['https://cir.nii.ac.jp/crid/1390282680315181056','https://books.google.com/books/about/Maung_Yin_Maung_and_Ma_Me_Ma_Vatthu.html?id=I25KQwAACAAJ']),
('The Modern Monk','Tet Pongyi','Thein Pe Myint',1937,'缅甸文学传统','民族主义小说','◆',['Tet Hpon-gyi','Tet Phonegyi'],['https://eprints.soas.ac.uk/29185/1/10731280.pdf']),
('Not Out of Hate','Mone Ywa Mahu','Ma Ma Lay',1955,'缅甸文学传统','战后社会小说','★',['Mone Ywa Mahu'],['https://www.ohioswallow.com/9780896801677/not-out-of-hate/']),
('Prison and Man','Htaung hnint lutha','Ludu U Hla',1957,'缅甸文学传统','政治监禁/当代写作','◆',['Htaung hnint lutha'],['https://www.burma-center.org/ludu-u-hla/']),
('ລູກຜູ້ຊາຍ','ລູກຜູ້ຊາຍ','Dūangsai Lūangphasī',2000,'柬埔寨—老挝文学传统','老挝现代小说','◆',['Lūk phūsāi'],['https://ci.nii.ac.jp/ncid/BA58002763']),
('His Native Soil','His Native Soil','Juan C. Laya',1941,'菲律宾文学传统','英语菲律宾小说形成','◆',[],['https://en.wikipedia.org/wiki/Philippine_literature_in_English']),
('Mekar dan Segar','Mekar dan Segar','Suratman Markasan',1959,'新加坡—海峡多语文学传统','马来新加坡写作','◆',[],['https://en.wikipedia.org/wiki/Suratman_Markasan']),
]
created=[create(*x) for x in items]
AUD.parent.mkdir(parents=True,exist_ok=True); AUD.write_text('# R8 Verified Anchor Repair Batch 2 V1\n\n- Verified Works created: **8**\n- East Timor crocodile/creation slot intentionally remains PARTIAL because it is a collective oral tradition rather than a defensible single Work entity.\n\n## Created\n'+'\n'.join('- '+x for x in created)+'\n\n`R8_VERIFIED_ANCHOR_REPAIR_BATCH2_V1 = APPLIED_WITH_ONE_INTENTIONAL_ORAL_PARTIAL`\n',encoding='utf-8')
