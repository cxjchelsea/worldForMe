from pathlib import Path
import re
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); W=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'/'R10_AUTHOR_CLEANUP_V1.md'; TOP=ROOT/'30 专题'/'R10 跨区域文学传统'/'00 跨区域文学传统.md'
TOPIC='WL-TOPIC-R10-TRANSREGIONAL'

def fm(text):
 m=re.match(r'^---\s*\n(.*?)\n---',text,re.S); return m.group(1) if m else ''
def scalar(front,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',front); return m.group(1).strip(' "\'') if m else ''
def list_field(front,key):
 lines=front.splitlines(); out=[]
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if m: out.append(m.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []
def set_scalar(text,key,val):
 front=fm(text); line=f'{key}: "{val}"'
 if re.search(rf'(?m)^{re.escape(key)}:',front): nf=re.sub(rf'(?m)^{re.escape(key)}:.*$',line,front,1)
 else: nf=front+'\n'+line
 return text.replace(front,nf,1)

authors={
'莫斯卡特一家':'Isaac Bashevis Singer','巴登海姆1939':'Aharon Appelfeld','骨':'Fae Myenne Ng','自由生活':'Ha Jin','离开者':'Lisa Ko','砖巷':'Monica Ali','郊区佛爷':'Hanif Kureishi','拉合尔茶馆的陌生人':'Mohsin Hamid','西方退出':'Mohsin Hamid','盐屋':'Hala Alyan','阿拉伯爵士':'Diana Abu-Jaber','哈卡瓦蒂':'Rabih Alameddine','过境':'Anna Seghers','移民':'W. G. Sebald','什么是什么':'Dave Eggers','阿勒颇养蜂人':'Christy Lefteri','莫洛伊':'Samuel Beckett','等待':'Ha Jin','在他乡':'Jhumpa Lahiri','开放的城市':'Teju Cole','在地球上我们短暂地绚烂':'Ocean Vuong','撒旦诗篇':'Salman Rushdie','宽广的萨尔加索海':'Jean Rhys','七杀简史':'Marlon James'}
updated=[]
for p in W.glob('*.md'):
 try: txt=p.read_text(encoding='utf-8')
 except: continue
 f=fm(txt)
 if scalar(f,'type')!='work' or TOPIC not in list_field(f,'topics'): continue
 a=scalar(f,'author')
 if a and a.lower() not in ('null','none'): continue
 if p.stem in authors:
  txt=set_scalar(txt,'author',authors[p.stem]); txt=set_scalar(txt,'bibliography_status','author_verified_r10_cleanup_v1'); p.write_text(txt,encoding='utf-8'); updated.append(p.name)
# quarantine the known structural placeholder 离岸
p=W/'离岸.md'
if p.exists():
 txt=p.read_text(encoding='utf-8'); f=fm(txt)
 if scalar(f,'type')=='work':
  txt=set_scalar(txt,'type','work_candidate'); txt=set_scalar(txt,'candidate_status','quarantined_pending_bibliographic_verification'); txt=set_scalar(txt,'bibliography_status','quarantined_structural_placeholder_r10_v1'); p.write_text(txt,encoding='utf-8')
# recount active R10 author gaps after quarantine
active=0; gaps=[]
for p in W.glob('*.md'):
 try: txt=p.read_text(encoding='utf-8')
 except: continue
 f=fm(txt)
 if scalar(f,'type')!='work' or TOPIC not in list_field(f,'topics'): continue
 active+=1; a=scalar(f,'author')
 if not a or a.lower() in ('null','none'): gaps.append(p.name)
if TOP.exists():
 txt=TOP.read_text(encoding='utf-8')
 txt=txt.replace('`R10_WORK_SUPPORT = COMPLETE`','`R10_WORK_SUPPORT = AUTHOR_CLEANUP_COMPLETE_WITH_ONE_STRUCTURAL_PLACEHOLDER_QUARANTINED`')
 TOP.write_text(txt,encoding='utf-8')
AUD.parent.mkdir(parents=True,exist_ok=True)
AUD.write_text('# R10 Author Cleanup V1\n\n- Known R10 author mappings governed by cleanup: **'+str(len(authors))+'**\n- Repairs applied on this run: **'+str(len(updated))+'**\n- Quarantined structural placeholder: **离岸.md**\n- Active R10 Works after cleanup: **'+str(active)+'**\n- Active R10 author gaps after cleanup: **'+str(len(gaps))+'**\n\n## Remaining active gaps\n'+(''.join('- '+x+'\n' for x in gaps) if gaps else '- None\n')+'\n`R10_AUTHOR_CLEANUP_V1 = '+('PASS' if not gaps else 'REQUIRES_FOLLOWUP')+'`\n',encoding='utf-8')
print('known',len(authors),'updated',len(updated),'active',active,'gaps',len(gaps))
