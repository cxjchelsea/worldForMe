from pathlib import Path
import csv,re,unicodedata
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'; AUDIT=ROOT/'_audit/r_axis_r2'; SLOTS=AUDIT/'r2_structural_slots_v1.csv'; OUT=AUDIT/'R2_STRUCTURAL_COVERAGE_V1.md'
R2='R2 东亚文学'
def norm(s):
 s=unicodedata.normalize('NFKC',s or '').casefold(); return re.sub(r'[\s·・—_\-:：,，。.!！?？()（）《》〈〉“”"\'’]+','',s)
def fm(text):
 m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S); return m.group(1) if m else ''
def scalar(f,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',f)
 if not m:return ''
 return m.group(1).strip().strip('"\'')
def list_field(f,key):
 lines=f.splitlines()
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   out=[]
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*(.*?)\s*$',n)
    if m: out.append(m.group(1).strip().strip('"\'')); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []
def main():
 index={}
 for p in WORKS.glob('*.md'):
  f=fm(p.read_text(encoding='utf-8-sig'))
  if not f or scalar(f,'type')!='work':continue
  vals={scalar(f,'title') or p.stem, scalar(f,'title_original'), p.stem}
  vals.update(list_field(f,'aliases'))
  rec={'file':p.name,'title':scalar(f,'title') or p.stem,'axis_r':list_field(f,'axis_r')}
  for v in vals:
   if v:index.setdefault(norm(v),[]).append(rec)
 rows=list(csv.DictReader(SLOTS.open(encoding='utf-8-sig')))
 covered=0; miss=[]; lines=['# R2 Structural Coverage Audit V1','', '| Tradition | Slot | Status | Anchor | Priority |','|---|---|---|---|---|']
 for r in rows:
  hit=None
  for c in r['candidates'].split('|'):
   for rec in index.get(norm(c),[]):
    if R2 in rec['axis_r']:
     hit=rec; break
   if hit: break
  if hit:
   covered+=1; status='COVERED'; anchor=hit['title']
  else:
   status='MISSING'; anchor='—'; miss.append(r)
  lines.append(f"| {r['tradition']} | {r['slot']} | {status} | {anchor} | {r['priority']} |")
 total=len(rows); pct=covered/total*100 if total else 0
 lines[1:1]=[f'- Structural slots: **{total}**',f'- Covered: **{covered}**',f'- Missing: **{len(miss)}**',f'- Coverage: **{pct:.1f}%**','']
 lines += ['','## Missing P0/P1','']
 for p in ('P0','P1'):
  lines.append(f'### {p}'); lines.append('')
  subset=[r for r in miss if r['priority']==p]
  if not subset: lines.append('- None')
  for r in subset: lines.append(f"- {r['tradition']} / {r['slot']} → {r['candidates']}")
  lines.append('')
 lines.append('`R2_STRUCTURAL_COVERAGE_V1 = AUDITED_READ_ONLY`')
 OUT.write_text('\n'.join(lines),encoding='utf-8')
 print(f'TOTAL={total} COVERED={covered} MISSING={len(miss)} COVERAGE={pct:.1f}%')
if __name__=='__main__': main()
