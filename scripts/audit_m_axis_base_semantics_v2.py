from __future__ import annotations
import re, yaml
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
VALID={'★','◆','△'}; issues=[]; counts={}

def first_yaml(text):
    t=text.replace('\r\n','\n').replace('\r','\n')
    m=re.match(r'^---\s*\n(.*?)\n---\s*(?:\n|$)',t,re.S)
    if not m:return None,'NO_FRONTMATTER'
    try:
        d=yaml.safe_load(m.group(1)) or {}
        return (d,None) if isinstance(d,dict) else (None,'FRONTMATTER_NOT_MAPPING')
    except Exception as e:return None,'YAML_ERROR: '+str(e).split('\n')[0]

parsed={}
for wp in WORKS.glob('*.md'):
    d,err=first_yaml(wp.read_text(encoding='utf-8',errors='strict')); parsed[wp]=(d,err)

for code,(folder,pri,cluster,axes,hist,expected) in CFG.items():
    td=TOPICS/folder
    b3=next(td.glob('03 *.base')).read_text(encoding='utf-8')
    required3=[
        'file.folder == "个人通识知识系统_v2_A2/30 世界文学/40 作品"',
        f'{pri} == "★"',f'{pri} == "◆"',f'{pri} == "△"',
        f'note.{cluster}:\n    displayName: 专题思潮',f'note.{hist}:\n    displayName: 历史位置',
        f'note.{axes}:\n    displayName: 专题机制','note.axis_m:\n    displayName: M轴坐标',
        'name: 按专题思潮','name: 按历史位置']
    for x in required3:
        if x not in b3:issues.append(f'{code}: work Base missing {x}')
    if 'topics.contains(' in b3:issues.append(f'{code}: Base still depends on topics.contains')

    members=[]
    for wp,(d,err) in parsed.items():
        # If the topic field exists textually but YAML is unreadable, Obsidian will miss it: hard fail.
        if err:
            text=wp.read_text(encoding='utf-8',errors='ignore')
            if re.search(rf'(?m)^{re.escape(pri)}:',text):issues.append(f'{code}: Obsidian-unreadable YAML {wp.name}: {err}')
            continue
        if d.get('type')!='work' or str(d.get(pri,'')).strip() not in VALID:continue
        members.append(wp)
        if not d.get(cluster):issues.append(f'{code}: missing topic cluster {wp.name}')
        if not d.get(hist):issues.append(f'{code}: missing history position {wp.name}')
        av=d.get(axes); av=av if isinstance(av,list) else ([av] if av else [])
        if not av:issues.append(f'{code}: missing topic mechanism {wp.name}')
    counts[code]=len(members)
    if len(members)!=expected:issues.append(f'{code}: Obsidian-readable membership {len(members)} != frozen {expected}')

    b2=next(td.glob('02 *.base')).read_text(encoding='utf-8')
    for x in ['name: 按类型','property: formula.type_zh','note.parent_name:\n    displayName: 父节点','formula.history_zh:\n    displayName: 历史位置','formula.mechanism_zh:\n    displayName: 机制']:
        if x not in b2:issues.append(f'{code}: structure Base missing {x}')
    mechanism_nodes=0
    for sp in td.rglob('*.md'):
        rel=sp.relative_to(td).as_posix()
        if not rel.startswith(('10 ','11 ','12 ','13 ')):continue
        d,err=first_yaml(sp.read_text(encoding='utf-8',errors='strict'))
        if err:issues.append(f'{code}: structure YAML invalid {rel}: {err}');continue
        if not d.get('parent_name'):issues.append(f'{code}: missing Chinese parent_name {rel}')
        if d.get('type')=='literature_topic_mechanism' or d.get('dimension')=='mechanism':
            mechanism_nodes+=1
            mv=d.get('mechanism'); mv=mv if isinstance(mv,list) else ([mv] if mv else [])
            if not mv:issues.append(f'{code}: mechanism node empty {rel}')
    if mechanism_nodes==0:issues.append(f'{code}: no mechanism nodes')

status='PASS' if not issues else 'FAIL'
report=['# M-axis Base Semantic Audit v4','', '- parser: **PyYAML / first frontmatter only (Obsidian-equivalent membership contract)**',f'- status: **{status}**',f'- Obsidian-readable counts: `{counts}`',f'- issues: **{len(issues)}**','']
if issues:report+=['## Issues','']+[f'- {x}' for x in issues[:300]]
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports'/'m_axis_base_semantic_audit_v2.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('\n'.join(report))
if issues:raise SystemExit(2)
