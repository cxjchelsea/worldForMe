from pathlib import Path
import re
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); WORKS=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'/'R8_VERIFIED_ANCHOR_REPAIR_BATCH1_V1.md'
R8='R8 东南亚文学'; TOPIC='WL-TOPIC-R8-SOUTHEAST-ASIA'

def split(text):
 m=re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$',text,re.S); return (m.group(1),m.group(2)) if m else ('',text)
def scalar(f,k):
 m=re.search(rf'(?m)^{re.escape(k)}:\s*["\']?(.*?)["\']?\s*$',f); return m.group(1).strip(' "\'') if m else ''
def q(v): return '"'+str(v).replace('\\','\\\\').replace('"','\\"')+'"'
def set_scalar(f,k,v):
 line=f'{k}: {q(v)}'
 if re.search(rf'(?m)^{re.escape(k)}:',f): return re.sub(rf'(?m)^{re.escape(k)}:.*$',line,f,1)
 return f.rstrip()+'\n'+line
def set_year(f,y):
 line='year: null' if y is None else f'year: {y}'
 if re.search(r'(?m)^year:',f): return re.sub(r'(?m)^year:.*$',line,f,1)
 return f.rstrip()+'\n'+line
def list_field(f,k):
 lines=f.splitlines(); out=[]
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(k)}:\s*$',line):
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if m: out.append(m.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []
def set_list(f,k,vals):
 block=k+':\n'+''.join('  - '+q(v)+'\n' for v in vals)
 pat=rf'(?ms)^{re.escape(k)}:\s*\n(?:\s*-.*\n)*'
 if re.search(pat,f): return re.sub(pat,block,f,1)
 return f.rstrip()+'\n'+block.rstrip()
def render(f,b): return '---\n'+f.strip()+'\n---\n'+b.lstrip('\n')
def by_title(title):
 p=WORKS/(title+'.md');
 if p.exists(): return p
 for x in WORKS.glob('*.md'):
  try: f,_=split(x.read_text(encoding='utf-8'))
  except: continue
  if scalar(f,'title')==title: return x
 return None

def promote(title,author,year,orig,aliases,sources,note=''):
 p=by_title(title)
 if not p: raise RuntimeError('missing candidate '+title)
 text=p.read_text(encoding='utf-8'); f,b=split(text)
 f=set_scalar(f,'type','work'); f=set_scalar(f,'author',author); f=set_year(f,year)
 if orig: f=set_scalar(f,'title_original',orig)
 old=list_field(f,'aliases'); f=set_list(f,'aliases',list(dict.fromkeys(old+aliases)))
 f=set_scalar(f,'verification_status','手工核验'); f=set_scalar(f,'bibliography_status','verified_r8_anchor_repair_v1')
 f=set_list(f,'bibliography_sources',sources)
 if note: f=set_scalar(f,'authorship_note',note)
 p.write_text(render(f,b),encoding='utf-8'); return p.name

items=[
('素心','Hoàng Ngọc Phách',1925,'Tố Tâm',['To Tam'],['https://tdr.lib.ntu.edu.tw/retrieve/4a4b47e2-a43b-4f7d-8843-48a51fad918e/ntu-112-2.pdf']),
('志飘','Nam Cao',1941,'Chí Phèo',['Chi Pheo'],['https://books.google.com/books/about/Ch%C3%AD_Ph%C3%A8o.html?id=Myns0AEACAAJ']),
('哀痛的战争','Bảo Ninh',1991,'Nỗi buồn chiến tranh',['The Sorrow of War','Thân phận tình yêu'],['https://openlibrary.org/books/OL1097719M/The_sorrow_of_war']),
('无尽的田野','Nguyễn Ngọc Tư',None,'Cánh đồng bất tận',['The Endless Field'],['https://www.ach.or.kr/achNewsletter/mgzinSubViewPage.do?langTy=ENG&mgzinSn=15602&mgzinSubSn=25634']),
('人生戏剧','Akatdamkoeng Raphiphat',1929,'Lakhon Haeng Chiwit',['Circus of Life'],['https://kotobank.jp/word/%E3%81%82%E3%83%BC%E3%81%8B%E3%83%BC%E3%81%A8%E3%81%A0%E3%82%80%E3%81%8F%E3%83%BC%E3%82%93-24369']),
('乡村教师','Khammaan Khonkhai',1978,'ครูบ้านนอก',['The Teachers of Mad Dog Swamp'],['https://www.car.chula.ac.th/']),
('大地之子','Kampoon Boontawee',1976,'ลูกอีสาน',['A Child of the Northeast','Son of the Northeast'],['https://researchers.une.edu.au/en/publications/kampoon-boontawees-a-child-of-the-northeast-as-literary-ethnobota-5/']),
('利亚姆盖尔','佚名（高棉传统）',None,'រាមកេរ្តិ៍',['Reamker'],['https://en.wikipedia.org/wiki/Reamker']),
('图姆提乌','Preah Botumthera Som',1915,'Tum Teav',['Tum Teav'],['https://en.wikipedia.org/wiki/Tum_Teav']),
('枯萎的花','Nou Hach',1949,'Phka Srapoun',['Phka Sropoun'],['https://en.wikipedia.org/wiki/Phka_Srapoun']),
('杀戮场的女儿','Loung Ung',2000,'First They Killed My Father',['First They Killed My Father'],['https://en.wikipedia.org/wiki/First_They_Killed_My_Father']),
('辛赛','Pang Kham',None,'ສັງສີນໄຂ',['Sang Sinxay','Sinxay','Sinsai'],['https://en.wikipedia.org/wiki/Sang_Sinxay']),
('错误的教育','Abdul Muis',1928,'Salah Asuhan',['Salah Asuhan'],['https://en.wikipedia.org/wiki/Salah_Asuhan']),
('帕西翁','Gaspar Aquino de Belén',1704,'Ang Mahal na Pasión ni Jesu Christong Panginoon Natin na Tola',['Pasyon','Pasyóng Mahál'],['https://en.wikipedia.org/wiki/Pasyon']),
('起义者','José Rizal',1891,'El filibusterismo',['El Filibusterismo','The Reign of Greed'],['https://en.wikipedia.org/wiki/El_filibusterismo']),
('恶魔之手','F. Sionil José',1962,'The Pretenders',['The Pretenders'],['https://en.wikipedia.org/wiki/The_Pretenders_(novel)']),
('国家','Lualhati Bautista',1983,"Dekada '70",["Dekada '70"],['https://en.wikipedia.org/wiki/Dekada_%2770_(novel)']),
('狗食','Jessica Hagedorn',1990,'Dogeaters',['Dogeaters'],['https://en.wikipedia.org/wiki/Dogeaters']),
]
repaired=[]
for x in items: repaired.append(promote(*x))

# Create two correct replacements for quarantined wrong/generic placeholders.
def create_verified(title,author,year,orig,trad,role,prio,aliases,sources):
 p=WORKS/(title+'.md')
 if p.exists(): return p.name
 wid='WL-WORK-R8-VERIFIED-'+re.sub(r'[^A-Za-z0-9]+','-',orig).strip('-').upper()[:40]
 f='\n'.join([
 f'id: {q(wid)}','type: work',f'title: {q(title)}',f'title_original: {q(orig)}',f'author: {q(author)}',f'year: {year}',
 'aliases:']+['  - '+q(a) for a in aliases]+['axis_r:','  - '+q(R8),'topics:','  - '+q(TOPIC),f'r8_priority: {q(prio)}',f'r8_tradition: {q(trad)}','r8_role:','  - '+q(role),'verification_status: "手工核验"','bibliography_status: "verified_r8_anchor_repair_v1"','bibliography_sources:']+['  - '+q(s) for s in sources])
 body=f'# {title}\n\n> R8 书目重验证后建立的真实 canonical Work；替代旧的结构占位条目。\n'
 p.write_text(render(f,body),encoding='utf-8'); return p.name
created=[]
created.append(create_verified('Ronggeng Dukuh Paruk','Ahmad Tohari',1982,'Ronggeng Dukuh Paruk','印尼—爪哇与群岛文学传统','1965记忆/女性','◆',['The Dancer'],['https://ensiklopedia.kemendikdasmen.go.id/sastra/artikel/Ronggeng_Dukuh_Paruk','https://books.google.com/books/about/Ronggeng_Dukuh_Paruk.html?hl=id&id=VcRkAAAAMAAJ']))
created.append(create_verified('State of Emergency','Jeremy Tiang',2017,'State of Emergency','新加坡—海峡多语文学传统','当代国家/语言小说','◆',['紧急状态'],['https://www.goodreads.com/work/editions/53834561-state-of-emergency']))

lines=['# R8 Verified Anchor Repair Batch 1 V1','',f'- Promoted verified candidates: **{len(repaired)}**',f'- Correct replacement Works created: **{len(created)}**','', '## Promoted','']+['- '+x for x in repaired]+['','## Created','']+['- '+x for x in created]+['','- Quarantined wrong/generic placeholders were not reactivated.','- Every promoted/created Work now has an explicit author; uncertain original dates remain `year: null` rather than guessed.','', '`R8_VERIFIED_ANCHOR_REPAIR_BATCH1_V1 = APPLIED`','']
AUD.parent.mkdir(parents=True,exist_ok=True); AUD.write_text('\n'.join(lines),encoding='utf-8')
