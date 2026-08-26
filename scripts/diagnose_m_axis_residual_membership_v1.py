from __future__ import annotations
from pathlib import Path
import ast,re,yaml
ROOT=Path(__file__).resolve().parents[1]; S=ROOT/'scripts'; W=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
CFG={
'M1':('apply_m1_v2_structure_and_bibliography_v1.py','m1_priority',76),
'M2':('apply_m2_v2_structure_and_map_existing_v1.py','m2_priority',85),
'M4':('apply_m4_v2_structure_and_bibliography_v1.py','m4_priority',90),
'M5.1':('apply_m51_v2_structure_and_bibliography_v1.py','m51_priority',80),
'M5.2':('apply_m52_v2_structure_and_bibliography_v1.py','m52_priority',74),
}
VALID={'★','◆','△'}
def fm(text):
 t=text.replace('\r\n','\n').replace('\r','\n'); m=re.match(r'^---\s*\n(.*?)\n---\s*(?:\n|$)',t,re.S); return m.group(1) if m else None
def parse(p):
 f=fm(p.read_text(encoding='utf-8'))
 if f is None:return None,'NO_FM'
 try:
  d=yaml.safe_load(f) or {}; return (d,None) if isinstance(d,dict) else (None,'NOT_MAP')
 except Exception as e:return None,'YAML:'+str(e).split('\n')[0]
def get_bib(fn):
 tree=ast.parse((S/fn).read_text(encoding='utf-8'))
 for n in tree.body:
  if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='BIB' for t in n.targets): return ast.literal_eval(n.value)
 raise RuntimeError('no BIB '+fn)
def norm(s): return re.sub(r'[\s·・\-—–_.，,（）()\[\]【】:/／]+','',str(s)).lower()
# current index by title + filename, with author retained
entries=[]
for p in W.glob('*.md'):
 d,e=parse(p); text=p.read_text(encoding='utf-8')
 if d: entries.append((p,d,text))

def find_target(title,author):
 tn,an=norm(title),norm(author); candidates=[]
 for p,d,text in entries:
  dt=norm(d.get('title') or p.stem); da=norm(d.get('author') or '')
  if dt==tn or norm(p.stem).startswith(tn) or tn.startswith(norm(p.stem)):
   score=0
   if dt==tn:score+=4
   if da==an:score+=6
   elif an and da and (an in da or da in an):score+=3
   candidates.append((score,p,d))
 candidates.sort(key=lambda x:x[0],reverse=True)
 return candidates

for code,(fn,field,declared) in CFG.items():
 bib=get_bib(fn); print('\n##',code,'BIB',len(bib),'current target',declared)
 missing=[]; ambiguous=[]
 for row in bib:
  title,author=row[0],row[1]; c=find_target(title,author)
  if not c or c[0][0]<4:
   missing.append((title,author,'NO_MATCH')); continue
  best=c[0]
  if len(c)>1 and c[1][0]==best[0]: ambiguous.append((title,author,[(x[0],x[1].name,x[2].get('author')) for x in c[:3]]))
  val=str(best[2].get(field,'')).strip()
  if val not in VALID or best[2].get('type')!='work': missing.append((title,author,f'{best[1].name}: {field}={val!r}, type={best[2].get("type")!r}'))
 print('MISSING',len(missing))
 for x in missing:print(' ',x)
 if ambiguous:
  print('AMBIGUOUS',len(ambiguous))
  for x in ambiguous:print(' ',x)

# M3.1: identify current non-members with textual modernism residue / topic residue.
field='modernism_priority'; topic='WL-TOPIC-M3-MODERNISM'; candidates=[]
for p in W.glob('*.md'):
 text=p.read_text(encoding='utf-8'); d,e=parse(p); readable=d and str(d.get(field,'')).strip() in VALID and d.get('type')=='work'
 if readable:continue
 if field in text or topic in text:
  candidates.append((p.name,e, None if not d else d.get(field), None if not d else d.get('type'), text.count(field),text.count(topic)))
print('\n## M3.1 residual candidates',len(candidates))
for x in candidates:print(' ',x)
