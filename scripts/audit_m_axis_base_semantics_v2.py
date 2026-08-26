from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
TOPICS=LIT/'30 专题'; WORKS=LIT/'40 作品'
CFG={
'M1':('M1 早期现代思想与美学','m1_priority','m1_movement_cluster','m1_axes','m1_history_position',76),
'M2':('M2 19世纪文学思潮','m2_priority','m2_movement_cluster','m2_axes','m2_history_position',85),
'M3.1':('M3.1 现代主义','modernism_priority','modernism_tradition_cluster','modernism_axes','modernism_history_position',149),
'M3.2':('M3.2 先锋派','m32_priority','m32_movement_cluster','m32_axes','m32_history_position',68),
'M4':('M4 集体文学运动与文化政治','m4_priority','m4_movement_cluster','m4_axes','m4_history_position',90),
'M5.1':('M5.1 战后思想与美学范式','m51_priority','m51_movement_cluster','m51_axes','m51_history_position',80),
'M5.2':('M5.2 权力、身份与世界批评','m52_priority','m52_framework_cluster','m52_axes','m52_history_position',74),
}
issues=[]; counts={}

def split(text):
    if not text.startswith('---\n'): return '',text
    e=text.find('\n---\n',4)
    return (text[4:e],text[e+5:]) if e>=0 else ('',text)
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm)
    return m.group(1).strip().strip('"\'') if m else ''
def lst(fm,key):
    ls=fm.splitlines(); out=[]
    for i,l in enumerate(ls):
        if l.startswith(key+':'):
            tail=l.split(':',1)[1].strip()
            if tail.startswith('[') and tail.endswith(']'):
                return [x.strip().strip('"\'') for x in tail[1:-1].split(',') if x.strip()]
            j=i+1
            while j<len(ls) and ls[j].startswith('-'):
                out.append(ls[j][1:].strip().strip('"\'')); j+=1
            return out
    return out

for code,(folder,pri,cluster,axes,hist,expected) in CFG.items():
    td=TOPICS/folder
    b3=next(td.glob('03 *.base')).read_text(encoding='utf-8')
    # UI / filtering contract: canonical folder + topic-priority membership, one shared label.
    required3=[
        'file.folder == "个人通识知识系统_v2_A2/30 世界文学/40 作品"',
        f'{pri} == "★"', f'{pri} == "◆"', f'{pri} == "△"',
        f'note.{cluster}:\n    displayName: 专题思潮',
        f'note.{hist}:\n    displayName: 历史位置',
        f'note.{axes}:\n    displayName: 专题机制',
        'note.axis_m:\n    displayName: M轴坐标',
        'name: 按专题思潮','name: 按历史位置'
    ]
    for x in required3:
        if x not in b3: issues.append(f'{code}: work Base missing {x}')
    if 'topics.contains(' in b3:
        issues.append(f'{code}: work Base still depends on topics.contains membership')

    b2=next(td.glob('02 *.base')).read_text(encoding='utf-8')
    required2=[
        'name: 按类型','property: formula.type_zh','note.parent_name:\n    displayName: 父节点',
        'formula.history_zh:\n    displayName: 历史位置',
        'formula.mechanism_zh:\n    displayName: 机制',
        'mechanism_zh: if(mechanism, mechanism, "—")'
    ]
    for x in required2:
        if x not in b2: issues.append(f'{code}: structure Base missing {x}')

    members=[]
    for wp in WORKS.glob('*.md'):
        fm,_=split(wp.read_text(encoding='utf-8',errors='ignore'))
        p=scalar(fm,pri)
        if p not in {'★','◆','△'}: continue
        members.append(wp)
        if not scalar(fm,cluster): issues.append(f'{code}: missing topic cluster {wp.name}')
        if not scalar(fm,hist): issues.append(f'{code}: missing history position {wp.name}')
        if not lst(fm,axes): issues.append(f'{code}: missing topic mechanism {wp.name}')
    counts[code]=len(members)
    if len(members)!=expected: issues.append(f'{code}: Base membership count {len(members)} != frozen {expected}')

    struct=[]; mechanism_nodes=0
    for sp in td.rglob('*.md'):
        rel=sp.relative_to(td).as_posix()
        if not rel.startswith(('10 ','11 ','12 ','13 ')): continue
        sfm,_=split(sp.read_text(encoding='utf-8',errors='ignore')); struct.append(sp)
        if not scalar(sfm,'parent_name'): issues.append(f'{code}: missing Chinese parent_name {rel}')
        if scalar(sfm,'type')=='literature_topic_mechanism' or scalar(sfm,'dimension')=='mechanism':
            mechanism_nodes += 1
            if not lst(sfm,'mechanism'): issues.append(f'{code}: mechanism node empty {rel}')
    if not struct: issues.append(f'{code}: no structure docs')
    if mechanism_nodes==0: issues.append(f'{code}: no mechanism nodes')

status='PASS' if not issues else 'FAIL'
report=['# M-axis Base Semantic Audit v3','',f'- status: **{status}**',f'- Base membership counts: `{counts}`',f'- issues: **{len(issues)}**','']
if issues: report += ['## Issues',''] + [f'- {x}' for x in issues[:200]]
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports'/'m_axis_base_semantic_audit_v2.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('\n'.join(report))
if issues: raise SystemExit(2)
