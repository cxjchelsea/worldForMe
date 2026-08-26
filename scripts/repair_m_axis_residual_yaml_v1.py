from __future__ import annotations
from pathlib import Path
import re,yaml
ROOT=Path(__file__).resolve().parents[1]
W=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
TARGETS={
'十日谈.md','费德尔.md','草叶集.md','白鲸.md','红字.md','哈克贝利·费恩历险记.md','一位女士的画像.md',
'了不起的盖茨比.md','喧哗与骚动.md','土生子.md','他们眼望上苍.md','天堂.md','宠儿.md','紫色.md','使女的故事.md'
}
FIELDS=['m1_','m2_','modernism_','m32_','m4_','m51_','m52_']
VALID={'★','◆','△'}
CFG={'M1':('m1_priority',76),'M2':('m2_priority',85),'M3.1':('modernism_priority',149),'M3.2':('m32_priority',68),'M4':('m4_priority',90),'M5.1':('m51_priority',80),'M5.2':('m52_priority',74)}

def norm(text):return text.replace('\r\n','\n').replace('\r','\n')
def first_parts(text):
 t=norm(text); m=re.match(r'^---\s*\n(.*?)\n---\s*(?:\n|$)(.*)$',t,re.S)
 return (m.group(1),m.group(2)) if m else (None,t)
def blocks(fm):
 lines=fm.splitlines(); out=[]; i=0
 while i<len(lines):
  m=re.match(r'^([A-Za-z0-9_.-]+):',lines[i])
  if not m:i+=1;continue
  k=m.group(1); b=[lines[i]]; i+=1
  while i<len(lines) and not re.match(r'^([A-Za-z0-9_.-]+):',lines[i]):b.append(lines[i]);i+=1
  out.append((k,b))
 return out
def listitems(b):
 if not b:return []
 head=b[0].split(':',1)[1].strip()
 if head.startswith('[') and head.endswith(']'):return [x.strip() for x in head[1:-1].split(',') if x.strip()]
 return [m.group(1) for x in b[1:] if (m:=re.match(r'^\s*-\s*(.+)$',x))]
def renderlist(k,vals):return [k+':']+['- '+x for x in vals]
def merge_overlay(overlay,canon):
 fb=blocks(overlay); sb=blocks(canon); fm={k:b for k,b in fb}; sm={k:b for k,b in sb}
 for k in ('topics','topic_links','axis_m'):
  vals=[]
  for b in (sm.get(k),fm.get(k)):
   for x in listitems(b):
    if x not in vals:vals.append(x)
  if vals:sm[k]=renderlist(k,vals)
 for k,b in fb:
  if any(k.startswith(pre) for pre in FIELDS):sm[k]=b
 rendered=[];seen=set()
 for k,_ in sb:
  if k not in seen:rendered+=sm[k];seen.add(k)
 for k,_ in fb:
  if k not in seen and any(k.startswith(pre) for pre in FIELDS):rendered+=sm[k];seen.add(k)
 return '\n'.join(rendered).rstrip()+'\n'
def sanitize(fm):
 lines=[]
 for x in fm.splitlines():
  if re.match(r'^\s*\[\]\s*$',x):continue
  # All entity frontmatter sequences here are top-level properties; normalize corrupted mixed indentation.
  m=re.match(r'^\s+-\s+(.*)$',x)
  if m:x='- '+m.group(1)
  lines.append(x)
 return '\n'.join(lines).rstrip()+'\n'
def valid_yaml(fm):
 try:
  d=yaml.safe_load(fm) or {}; return d if isinstance(d,dict) else None
 except Exception:return None

def repair(p):
 text=norm(p.read_text(encoding='utf-8')); fm,rest=first_parts(text)
 if fm is None:raise RuntimeError(f'{p.name}: no frontmatter')
 fm=sanitize(fm); d=valid_yaml(fm)
 if (not d or d.get('type')!='work') and re.match(r'^---\s*\n',rest):
  displaced=re.sub(r'^---\s*\n','',rest,count=1)
  m=re.match(r'^(.*?)\n---\s*(?:\n|$)(.*)$',displaced,re.S)
  canon,body=(m.group(1),m.group(2)) if m else (displaced,'')
  canon=sanitize(canon); cd=valid_yaml(canon)
  if not cd or cd.get('type')!='work':raise RuntimeError(f'{p.name}: displaced canonical YAML invalid')
  merged=sanitize(merge_overlay(fm,canon)); md=valid_yaml(merged)
  if not md or md.get('type')!='work':raise RuntimeError(f'{p.name}: merged YAML invalid')
  p.write_text('---\n'+merged+'---\n'+body,encoding='utf-8'); return 'merged-overlay'
 if not d or d.get('type')!='work':raise RuntimeError(f'{p.name}: sanitized YAML still invalid/type={None if not d else d.get("type")}')
 _,oldrest=first_parts(text)
 p.write_text('---\n'+fm+'---\n'+oldrest,encoding='utf-8'); return 'sanitized'

for name in sorted(TARGETS):
 p=W/name
 if not p.exists():raise RuntimeError('missing target '+name)
 print(repair(p),name)

counts={}
for code,(field,expected) in CFG.items():
 n=0
 for p in W.glob('*.md'):
  fm,_=first_parts(p.read_text(encoding='utf-8'))
  if fm is None:continue
  d=valid_yaml(fm)
  if d and d.get('type')=='work' and str(d.get(field,'')).strip() in VALID:n+=1
 counts[code]=n; print(code,n,'expected',expected)
 if n!=expected:raise RuntimeError(f'{code}: {n} != {expected}')
print('STRICT_OBSIDIAN_COUNTS_PASS',counts)
