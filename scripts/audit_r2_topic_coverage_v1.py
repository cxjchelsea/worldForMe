from pathlib import Path
import re, csv
from collections import Counter
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
OUT=ROOT/'_audit/r_axis_r2'
R2='R2 东亚文学'

def fm(text):
 m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S); return m.group(1) if m else ''
def scalar(front,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',front)
 if not m:return ''
 v=m.group(1).strip().strip('"\''); return '' if v.lower() in {'null','none','~'} else v
def list_field(front,key):
 lines=front.splitlines()
 for i,line in enumerate(lines):
  inline=re.match(rf'^{re.escape(key)}:\s*\[(.*?)\]\s*$',line)
  if inline:
   raw=inline.group(1).strip(); return [] if not raw else [x.strip().strip('"\'') for x in raw.split(',')]
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   out=[]
   for nxt in lines[i+1:]:
    m=re.match(r'^\s*-\s*(.*?)\s*$',nxt)
    if m: out.append(m.group(1).strip().strip('"\'')); continue
    if nxt.strip() and not nxt.startswith((' ','\t')): break
   return out
 return []

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 rows=[]; tc=Counter(); total=0
 for p in sorted(WORKS.glob('*.md'),key=lambda x:x.name.casefold()):
  f=fm(p.read_text(encoding='utf-8-sig'))
  if not f or scalar(f,'type')!='work': continue
  total+=1
  ar=list_field(f,'axis_r')
  if R2 not in ar: continue
  at=list_field(f,'axis_t')
  for x in at:
   if x.startswith('T') and len(x)>1: tc[x[:2]]+=1
  rows.append({'file':p.name,'id':scalar(f,'id'),'title':scalar(f,'title') or p.stem,'author':scalar(f,'author'),'year':scalar(f,'year'),'axis_t':';'.join(at),'r2_priority':scalar(f,'r2_priority'),'r2_tradition':scalar(f,'r2_tradition'),'r2_role':';'.join(list_field(f,'r2_role'))})
 fields=list(rows[0]) if rows else ['file','id','title','author','year','axis_t','r2_priority','r2_tradition','r2_role']
 with (OUT/'r2_works_v1.csv').open('w',encoding='utf-8-sig',newline='') as fh:
  w=csv.DictWriter(fh,fieldnames=fields); w.writeheader(); w.writerows(rows)
 lines=['# R2 Topic Coverage Audit V1','',f'- Total canonical Works: **{total}**',f'- Works mapped to R2: **{len(rows)}**','','## T distribution','']
 for t in ['T0','T1','T2','T3','T4','T5','T6']: lines.append(f'- {t}: **{tc[t]}**')
 lines += ['', '## Current works','']
 for r in rows: lines.append(f"- {r['title']} | {r['author'] or '-'} | {r['axis_t'] or '-'}")
 lines += ['', '`R2_TOPIC_COVERAGE_V1 = AUDITED_READ_ONLY`','']
 (OUT/'README.md').write_text('\n'.join(lines),encoding='utf-8')
 print(f'TOTAL={total} R2={len(rows)}')
if __name__=='__main__': main()
