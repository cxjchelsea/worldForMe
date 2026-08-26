from __future__ import annotations

import json, re
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
WORKS=LIT/'40 作品'
TOPIC='WL-TOPIC-M1-EARLY-MODERN'
EXPECTED={'人文主义','文艺复兴','巴洛克','古典主义','启蒙主义','感伤主义'}


def split_doc(text):
    if text.startswith('---\n'):
        e=text.find('\n---\n',4)
        if e!=-1:return text[4:e],text[e+5:]
    return '',text

def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*[\"\']?(.*?)[\"\']?\s*$',fm)
    return m.group(1).strip().strip('\"\'') if m else ''
def lst(fm,key):
    lines=fm.splitlines(); out=[]
    for i,line in enumerate(lines):
        if line.startswith(key+':'):
            tail=line.split(':',1)[1].strip()
            if tail.startswith('[') and tail.endswith(']'):
                return [x.strip().strip('\"\'') for x in tail[1:-1].split(',') if x.strip()]
            j=i+1
            while j<len(lines) and lines[j].startswith('-'):
                out.append(lines[j][1:].strip().strip('\"\'')); j+=1
            return out
    return out

rows=[]
for p in WORKS.glob('*.md'):
    text=p.read_text(encoding='utf-8',errors='ignore'); fm,_=split_doc(text)
    if TOPIC not in lst(fm,'topics'): continue
    rows.append({
        'path':str(p.relative_to(ROOT)), 'title':scalar(fm,'title') or p.stem,
        'author':scalar(fm,'author'), 'priority':scalar(fm,'m1_priority'),
        'movement':scalar(fm,'m1_movement_cluster'), 'axes':lst(fm,'m1_axes'),
        'axis_m':lst(fm,'axis_m'), 'year':scalar(fm,'year'), 'topics':lst(fm,'topics')})

mov=Counter(r['movement'] for r in rows)
pri=Counter(r['priority'] for r in rows)
axes=Counter(a for r in rows for a in r['axes'])
missing={
'priority':sum(not r['priority'] for r in rows),
'movement':sum(not r['movement'] for r in rows),
'axes':sum(not r['axes'] for r in rows),
'author':sum(not r['author'] for r in rows),
'year':sum(not r['year'] or r['year'].lower() in {'null','none'} for r in rows)}
unexpected=sorted(set(mov)-EXPECTED)
axis_m_mismatch=[r['title'] for r in rows if 'M1 早期现代思想与美学' not in r['axis_m']]
bytitle=defaultdict(list)
for r in rows: bytitle[r['title']].append(r)
dups={t:v for t,v in bytitle.items() if len(v)>1}
m2_overlap=[r['title'] for r in rows if any(x.startswith('M2 ') for x in r['axis_m'])]

report=['# M1 早期现代思想与美学书目覆盖审计','',f'- canonical works: **{len(rows)}**',f'- ★: **{pri.get("★",0)}**',f'- ◆: **{pri.get("◆",0)}**',f'- missing priority: **{missing["priority"]}**',f'- missing movement: **{missing["movement"]}**',f'- missing axes: **{missing["axes"]}**',f'- missing author: **{missing["author"]}**',f'- unexpected movements: **{len(unexpected)}**',f'- axis_m mismatch: **{len(axis_m_mismatch)}**',f'- duplicate M1 titles: **{len(dups)}**',f'- overlaps with M2: **{len(m2_overlap)}**','','## 六个板块覆盖','', '| movement | works |','|---|---:|']
for m in ['人文主义','文艺复兴','巴洛克','古典主义','启蒙主义','感伤主义']:
    report.append(f'| {m} | {mov.get(m,0)} |')
report += ['', '## 机制覆盖（Top 30）','', '| mechanism | works |','|---|---:|']
for a,n in axes.most_common(30): report.append(f'| {a} | {n} |')
report += ['', '## 元数据缺口','',f'- priority: **{missing["priority"]}**',f'- movement: **{missing["movement"]}**',f'- axes: **{missing["axes"]}**',f'- author: **{missing["author"]}**',f'- year: **{missing["year"]}**']
if dups:
    report += ['', '## M1 内同名实体','']
    for t,rs in dups.items(): report.append(f'- {t}: '+ ' / '.join(r['author'] for r in rs))
if m2_overlap:
    report += ['', '## 与 M2 重叠','', '- '+ '、'.join(m2_overlap)]

out='\n'.join(report)+'\n'
print(out)
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports'/'m1_coverage_audit.md').write_text(out,encoding='utf-8')
(ROOT/'reports'/'m1_coverage_audit.json').write_text(json.dumps({'count':len(rows),'priority':pri,'movements':mov,'axes':axes,'missing':missing,'unexpected':unexpected,'axis_m_mismatch':axis_m_mismatch,'duplicate_titles':{k:[r['author'] for r in v] for k,v in dups.items()},'m2_overlap':m2_overlap},ensure_ascii=False,indent=2),encoding='utf-8')

if len(rows)!=76 or missing['priority'] or missing['movement'] or missing['axes'] or missing['author'] or unexpected or axis_m_mismatch or dups:
    raise SystemExit(2)
