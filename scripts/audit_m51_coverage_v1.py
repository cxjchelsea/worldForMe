from pathlib import Path
import re,json
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]; W=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'; TOP='WL-TOPIC-M5.1-POSTWAR-AESTHETICS'; AX='M5.1 战后思想与美学范式'
def fm(t):
 if not t.startswith('---\n'): return ''
 e=t.find('\n---\n',4); return t[4:e] if e!=-1 else ''
def scalar(x,k):
 m=re.search(rf'(?m)^{re.escape(k)}:\s*["\']?(.*?)["\']?\s*$',x); return m.group(1).strip() if m else ''
def vals(x,k):
 ls=x.splitlines(); i=next((i for i,z in enumerate(ls) if z.startswith(k+':')),None)
 if i is None:return []
 inline=ls[i].split(':',1)[1].strip()
 if inline.startswith('['): return [z.strip(" '\"") for z in inline.strip('[]').split(',') if z.strip()]
 out=[]
 for z in ls[i+1:]:
  if re.match(r'^\s*- ',z): out.append(z.split('-',1)[1].strip().strip("'\""))
  else: break
 return out
rows=[]
for p in W.glob('*.md'):
 x=fm(p.read_text(encoding='utf-8'))
 if TOP in vals(x,'topics'):
  rows.append((p,scalar(x,'title') or p.stem,scalar(x,'author'),scalar(x,'m51_priority'),scalar(x,'m51_movement_cluster'),vals(x,'m51_axes'),vals(x,'axis_m'),scalar(x,'year')))
mov=Counter(r[4] for r in rows); axes=Counter(a for r in rows for a in r[5]); pri=Counter(r[3] for r in rows); titles=Counter(r[1] for r in rows)
expected={'存在主义':14,'荒诞':12,'法国新小说':10,'魔幻现实主义':19,'后现代主义':25}
report={'count':len(rows),'priority':dict(pri),'movements':dict(mov),'missing_priority':sum(not r[3] for r in rows),'missing_movement':sum(not r[4] for r in rows),'missing_axes':sum(not r[5] for r in rows),'missing_author':sum(not r[2] for r in rows),'axis_m_mismatch':sum(AX not in r[6] for r in rows),'duplicate_titles':{k:v for k,v in titles.items() if v>1},'year_missing':sum(not r[7] or r[7]=='null' for r in rows),'axes_top':axes.most_common(30)}
print('# M5.1 战后思想与美学范式书目覆盖审计')
for k in ['count','missing_priority','missing_movement','missing_axes','missing_author','axis_m_mismatch','year_missing']: print(k,report[k])
print('priority',report['priority']); print('movements',report['movements']); print('duplicates',report['duplicate_titles']); print('axes',report['axes_top'])
ok=(len(rows)==80 and mov==Counter(expected) and pri['★']+pri['◆']==80 and report['missing_priority']==report['missing_movement']==report['missing_axes']==report['missing_author']==report['axis_m_mismatch']==0 and not report['duplicate_titles'])
Path(ROOT/'reports').mkdir(exist_ok=True); (ROOT/'reports'/'m51_coverage_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
if not ok: raise SystemExit(1)
