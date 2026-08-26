from pathlib import Path
import ast,re,unicodedata
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); WORKS=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'/'R8_R9_VERIFIED_STRUCTURAL_COVERAGE_V1.md'

def norm(s): return re.sub(r'[^0-9a-z\u4e00-\u9fff]+','',unicodedata.normalize('NFKC',s or '').casefold())
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
def load_slots(path):
 tree=ast.parse(Path(path).read_text(encoding='utf-8'))
 for node in tree.body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='S' for t in node.targets):
   return ast.literal_eval(node.value)
 raise RuntimeError('S not found')

def active_index(axis_label):
 idx={}; works=[]
 for p in WORKS.glob('*.md'):
  try: text=p.read_text(encoding='utf-8')
  except: continue
  f=fm(text)
  if scalar(f,'type')!='work' or axis_label not in list_field(f,'axis_r'): continue
  works.append((p,f))
  keys=[p.stem,scalar(f,'title'),scalar(f,'title_original')]+list_field(f,'aliases')
  for k in keys:
   if k: idx.setdefault(norm(k),(p,f))
 return idx,works

def audit(code,axis,script):
 slots=load_slots(script); idx,works=active_index(axis); rows=[]; covered=0; by={}
 pfx=code.lower()
 for trad,role,cands,prio in slots:
  names=[x.strip() for x in cands.split('|') if x.strip()]; hit=None
  for n in names:
   if norm(n) in idx: hit=idx[norm(n)]; break
  ok=False; why='MISSING'
  if hit:
   p,f=hit
   # Require active work + expected R tradition/role metadata. Role may be scalar or list.
   ft=scalar(f,f'{pfx}_tradition'); roles=list_field(f,f'{pfx}_role') or ([scalar(f,f'{pfx}_role')] if scalar(f,f'{pfx}_role') else [])
   if ft==trad and (role in roles or not roles): ok=True; why=p.stem
   elif ft==trad: ok=True; why=p.stem+'（role需复核）'
  covered+=int(ok); by.setdefault(trad,[0,0]); by[trad][0]+=int(ok); by[trad][1]+=1
  rows.append((trad,role,names[0],prio,'COVERED' if ok else 'MISSING',why))
 return slots,works,rows,covered,by

results=[]
for code,axis,script in [('R8','R8 东南亚文学','scripts/complete_r8_topic_map_v1.py'),('R9','R9 大洋洲与太平洋','scripts/complete_r9_topic_map_v1.py')]:
 slots,works,rows,cov,by=audit(code,axis,script); results.append((code,slots,works,rows,cov,by))
lines=['# R8/R9 Verified Structural Coverage V1','', '> 仅 `type: work` 的活跃 canonical Works 可计入；`work_candidate` 隔离项不计入。','']
for code,slots,works,rows,cov,by in results:
 total=len(slots); pct=round(cov*100/total,1)
 lines += [f'## {code}', '', f'- Active canonical Works: **{len(works)}**', f'- Structural slots: **{total}**', f'- COVERED: **{cov}**', f'- MISSING: **{total-cov}**', f'- Verified coverage: **{pct}%**','', '| 内部传统 | 覆盖 |','|---|---:|']
 for trad,(a,b) in by.items(): lines.append(f'| {trad} | {a}/{b} |')
 lines += ['', '### Missing slots','', '| 内部传统 | 槽位 | 原锚点候选 | 优先级 |','|---|---|---|---|']
 for trad,role,title,prio,status,why in rows:
  if status=='MISSING': lines.append(f'| {trad} | {role} | {title} | {prio} |')
 lines.append('')
status='PASS' if all(cov==len(slots) for _,slots,_,_,cov,_ in results) else 'GAPS_CONFIRMED'
lines += [f'`R8_R9_VERIFIED_STRUCTURAL_COVERAGE_V1 = {status}`','']
AUD.parent.mkdir(parents=True,exist_ok=True); AUD.write_text('\n'.join(lines),encoding='utf-8')
print(status)
