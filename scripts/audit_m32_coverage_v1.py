from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORKS=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
TOPIC='WL-TOPIC-M3.2-AVANT-GARDE'
EXPECTED=['意大利未来主义','俄国未来主义','德语表现主义','达达主义','超现实主义','意象主义与漩涡主义','构成主义、LEF与事实文学','伊比利亚与拉美先锋派']

def fm(text):
    m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
    return m.group(1) if m else ''
def scalar(f,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*)$',f)
    return m.group(1).strip().strip("'\"") if m else ''
def lv(f,key):
    lines=f.splitlines(); out=[]
    for i,line in enumerate(lines):
        if line.startswith(key+':'):
            inline=line.split(':',1)[1].strip()
            if inline.startswith('[') and inline.endswith(']'):
                return [x.strip().strip("'\"") for x in inline[1:-1].split(',') if x.strip()]
            for n in lines[i+1:]:
                if re.match(r'^[A-Za-z0-9_]+:',n): break
                m=re.match(r'^\s*-\s+(.*)$',n)
                if m: out.append(m.group(1).strip().strip("'\""))
            break
    return out

records=[]
for p in WORKS.glob('*.md'):
    text=p.read_text(encoding='utf-8-sig'); f=fm(text)
    if not f or TOPIC not in lv(f,'topics'): continue
    records.append({'file':p.name,'title':scalar(f,'title') or p.stem,'author':scalar(f,'author'),'priority':scalar(f,'m32_priority'),'movement':scalar(f,'m32_movement_cluster'),'axes':lv(f,'m32_axes'),'axis_m':lv(f,'axis_m'),'year':scalar(f,'year'),'bibliography_status':scalar(f,'bibliography_status')})
priority=Counter(r['priority'] or '<missing>' for r in records)
movement=Counter(r['movement'] or '<missing>' for r in records)
axes=Counter(a for r in records for a in r['axes'])
missing={
 'priority':[r['file'] for r in records if not r['priority']],
 'movement':[r['file'] for r in records if not r['movement']],
 'axes':[r['file'] for r in records if not r['axes']],
 'author':[r['file'] for r in records if not r['author']],
 'year':[r['file'] for r in records if not r['year'] or r['year']=='null'],
}
unexpected={k:v for k,v in movement.items() if k not in EXPECTED and k!='<missing>'}
axis_m_mismatch=[r['file'] for r in records if 'M3.2 先锋派' not in r['axis_m']]
m31_overlap=[r['file'] for r in records if 'M3.1 现代主义' in r['axis_m']]
payload={'count':len(records),'priority':dict(priority),'movement':dict(movement),'axes':dict(axes),'missing_counts':{k:len(v) for k,v in missing.items()},'unexpected':unexpected,'axis_m_mismatch':axis_m_mismatch,'m31_overlap_count':len(m31_overlap),'m31_overlap':m31_overlap}
Path('reports').mkdir(exist_ok=True)
Path('reports/m32_coverage_audit.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# M3.2 先锋派书目覆盖审计','',f'- canonical works: **{len(records)}**',f"- ★: **{priority.get('★',0)}**",f"- ◆: **{priority.get('◆',0)}**",f"- missing priority: **{priority.get('<missing>',0)}**",f'- unexpected movements: **{sum(unexpected.values())}**',f'- axis_m mismatch: **{len(axis_m_mismatch)}**',f'- overlaps with M3.1: **{len(m31_overlap)}**','','## 八个运动群覆盖','','| movement | works |','|---|---:|']
for m in EXPECTED: lines.append(f'| {m} | {movement.get(m,0)} |')
lines += ['','## 机制覆盖（Top 30）','','| mechanism | works |','|---|---:|']
for k,v in axes.most_common(30): lines.append(f'| {k} | {v} |')
lines += ['','## 元数据缺口','']
for k in ['priority','movement','axes','author','year']: lines.append(f'- {k}: **{len(missing[k])}**')
report='\n'.join(lines)+'\n'
Path('reports/m32_coverage_audit.md').write_text(report,encoding='utf-8')
print(report)
