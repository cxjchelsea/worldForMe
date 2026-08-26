from pathlib import Path
from collections import Counter,defaultdict
import re,json
ROOT=Path(__file__).resolve().parents[1]
WORKS=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
TOPIC='WL-TOPIC-M4-COLLECTIVE-MOVEMENTS'; AXIS='M4 集体文学运动与文化政治'
EXPECTED={'民族主义文学':10,'无产阶级文学':10,'革命文学':10,'社会主义现实主义':10,'哈莱姆文艺复兴':10,'Négritude':8,'反殖民文学运动':12,'垮掉的一代':10,'拉丁美洲Boom':10}
def parts(t):
    if not t.startswith('---\n'): return None
    e=t.find('\n---\n',4); return (t[4:e],t[e+5:]) if e!=-1 else None
def scalar(fm,k):
    m=re.search(rf'(?m)^{re.escape(k)}:\s*["\']?(.*?)["\']?\s*$',fm); return m.group(1).strip() if m else ''
def vals(fm,k):
    lines=fm.splitlines(); out=[]
    for i,x in enumerate(lines):
        if x.startswith(k+':'):
            inline=x.split(':',1)[1].strip()
            if inline.startswith('['): return [v.strip(' "\'') for v in inline.strip('[]').split(',') if v.strip()]
            j=i+1
            while j<len(lines) and lines[j].startswith('- '): out.append(lines[j][2:].strip()); j+=1
            return out
    return out
rows=[]
for p in WORKS.glob('*.md'):
    t=p.read_text(encoding='utf-8'); pr=parts(t)
    if not pr: continue
    fm,_=pr
    if TOPIC not in vals(fm,'topics'): continue
    rows.append({'file':p.name,'title':scalar(fm,'title') or p.stem,'author':scalar(fm,'author'),'priority':scalar(fm,'m4_priority'),'movement':scalar(fm,'m4_movement_cluster'),'axes':vals(fm,'m4_axes'),'axis_m':vals(fm,'axis_m'),'year':scalar(fm,'year'),'topics':vals(fm,'topics')})
mov=Counter(r['movement'] for r in rows); pri=Counter(r['priority'] for r in rows); titles=defaultdict(list)
for r in rows: titles[r['title']].append(r['file'])
dups={k:v for k,v in titles.items() if len(v)>1 and k!='屠场'}
# 屠场 is an intentional same-Chinese-title different-author case in the central library; within M4 only Sinclair's entity should be tagged.
res={
'count':len(rows),'priority':dict(pri),'movements':dict(mov),'missing_priority':sum(not r['priority'] for r in rows),'missing_movement':sum(not r['movement'] for r in rows),'missing_axes':sum(not r['axes'] for r in rows),'missing_author':sum(not r['author'] for r in rows),'axis_m_mismatch':sum(AXIS not in r['axis_m'] for r in rows),'unexpected_movements':sorted(set(mov)-set(EXPECTED)),'movement_mismatch':{k:(mov.get(k,0),v) for k,v in EXPECTED.items() if mov.get(k,0)!=v},'duplicate_m4_titles':dups,'year_missing':sum(not r['year'] or r['year']=='null' for r in rows),'overlap_m31':sum('WL-TOPIC-M3-MODERNISM' in r['topics'] for r in rows),'overlap_m51':sum('WL-TOPIC-M5.1-POSTWAR-AESTHETICS' in r['topics'] for r in rows),'axes_top':Counter(a for r in rows for a in r['axes']).most_common(30)}
print('# M4 集体文学运动与文化政治书目覆盖审计')
for k in ['count','missing_priority','missing_movement','missing_axes','missing_author','axis_m_mismatch','year_missing','overlap_m31','overlap_m51']: print(k,res[k])
print('priority',res['priority']); print('movements',res['movements']); print('movement_mismatch',res['movement_mismatch']); print('duplicates',res['duplicate_m4_titles']); print('axes',res['axes_top'])
REP=ROOT/'reports'; REP.mkdir(exist_ok=True)
(REP/'m4_coverage_audit.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# M4 集体文学运动与文化政治书目覆盖审计','',f'- canonical works: **{len(rows)}**',f'- ★: **{pri.get("★",0)}**',f'- ◆: **{pri.get("◆",0)}**',f'- missing priority: **{res["missing_priority"]}**',f'- missing movement: **{res["missing_movement"]}**',f'- missing axes: **{res["missing_axes"]}**',f'- missing author: **{res["missing_author"]}**',f'- axis_m mismatch: **{res["axis_m_mismatch"]}**',f'- duplicate M4 titles: **{len(dups)}**','', '## 九个运动群覆盖','', '| movement | works |','|---|---:|']+[f'| {k} | {mov.get(k,0)} |' for k in EXPECTED]+['','## 机制覆盖 Top 30','']+[f'- {a}: {n}' for a,n in res['axes_top']]+['','## 合法跨专题重叠','',f'- M3.1 overlap: **{res["overlap_m31"]}**',f'- M5.1 overlap: **{res["overlap_m51"]}**','',f'- year metadata pending: **{res["year_missing"]}**']
(REP/'m4_coverage_audit.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
assert len(rows)==90,res
assert not any(res[k] for k in ['missing_priority','missing_movement','missing_axes','missing_author','axis_m_mismatch']),res
assert not res['unexpected_movements'] and not res['movement_mismatch'] and not dups,res
