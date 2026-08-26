from __future__ import annotations
import re,json
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WORKS=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
REPORT=ROOT/'reports'; REPORT.mkdir(exist_ok=True)
TOPIC='WL-TOPIC-M5.2-POWER-IDENTITY-WORLD'
EXPECTED={'后殖民':14,'去殖民':10,'女性主义':14,'酷儿':12,'生态批评':10,'生态文学':14}

def parts(t):
    if not t.startswith('---\n'): return None
    e=t.find('\n---\n',4); return (t[4:e],t[e+5:]) if e!=-1 else None
def scalar(fm,k):
    m=re.search(rf'(?m)^{re.escape(k)}:\s*["\']?(.*?)["\']?\s*$',fm); return m.group(1).strip() if m else ''
def vals(fm,k):
    ls=fm.splitlines(); out=[]
    for i,x in enumerate(ls):
        if x.startswith(k+':'):
            inline=x.split(':',1)[1].strip()
            if inline.startswith('['): return [z.strip().strip('"\'') for z in inline.strip('[]').split(',') if z.strip()]
            j=i+1
            while j<len(ls) and re.match(r'^\s*- ',ls[j]): out.append(ls[j].split('-',1)[1].strip().strip('"\'')); j+=1
            return out
    return out
def norm(s): return re.sub(r'[\s·・\-—_.（）()《》“”"\'：:，,/／]','',s or '').lower()
rows=[]
for p in WORKS.glob('*.md'):
    t=p.read_text(encoding='utf-8',errors='ignore'); z=parts(t)
    if not z: continue
    fm,_=z
    if TOPIC not in vals(fm,'topics'): continue
    rows.append({'file':p.name,'title':scalar(fm,'title') or p.stem,'author':scalar(fm,'author'),'priority':scalar(fm,'m52_priority'),'framework':scalar(fm,'m52_framework_cluster'),'role':scalar(fm,'m52_role'),'axes':vals(fm,'m52_axes'),'year':scalar(fm,'year'),'topics':vals(fm,'topics'),'axis_m':vals(fm,'axis_m') or ([scalar(fm,'axis_m')] if scalar(fm,'axis_m') else [])})
frameworks=Counter(r['framework'] for r in rows); priorities=Counter(r['priority'] for r in rows); roles=Counter(r['role'] for r in rows)
missing={'priority':sum(not r['priority'] for r in rows),'framework':sum(not r['framework'] for r in rows),'role':sum(not r['role'] for r in rows),'axes':sum(not r['axes'] for r in rows),'author':sum(not r['author'] for r in rows)}
d=defaultdict(list)
for r in rows: d[norm(r['title'])].append(r['file'])
dups={k:v for k,v in d.items() if len(v)>1}
mm={k:(frameworks.get(k,0),v) for k,v in EXPECTED.items() if frameworks.get(k,0)!=v}
year_missing=sum(r['year'] in ('','null','None') for r in rows)
overlap_m4=sum('WL-TOPIC-M4-COLLECTIVE-MOVEMENTS' in r['topics'] for r in rows)
overlap_m51=sum('WL-TOPIC-M5.1-POSTWAR-AESTHETICS' in r['topics'] for r in rows)
primary_m52=sum('M5.2 权力、身份与世界批评' in r['axis_m'] for r in rows)
legacy_primary=len(rows)-primary_m52
axes=Counter(a for r in rows for a in r['axes'])
status='PASS' if len(rows)==74 and not any(missing.values()) and not mm and not dups else 'FAIL'
lines=['# M5.2 权力、身份与世界批评书目覆盖审计','',f'status {status}',f'count {len(rows)}',f'missing {missing}',f'priority {dict(priorities)}',f'frameworks {dict(frameworks)}',f'framework_mismatch {mm}',f'roles {dict(roles)}',f'duplicates {dups}',f'year_missing {year_missing}',f'overlap_m4 {overlap_m4}',f'overlap_m51 {overlap_m51}',f'primary_axis_m52 {primary_m52}',f'preserved_legacy_primary_axis {legacy_primary}',f'axes {axes.most_common(40)}']
text='\n'.join(lines)+'\n'; print(text)
(REPORT/'m52_coverage_audit.md').write_text(text,encoding='utf-8')
(REPORT/'m52_coverage_audit.json').write_text(json.dumps({'status':status,'count':len(rows),'missing':missing,'priorities':priorities,'frameworks':frameworks,'roles':roles,'framework_mismatch':mm,'duplicates':dups,'year_missing':year_missing,'overlap_m4':overlap_m4,'overlap_m51':overlap_m51,'primary_axis_m52':primary_m52,'preserved_legacy_primary_axis':legacy_primary,'axes':axes},ensure_ascii=False,indent=2,default=dict),encoding='utf-8')
if status!='PASS': raise SystemExit(2)
