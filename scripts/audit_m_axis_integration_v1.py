from __future__ import annotations
import json, re, subprocess
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
NODES=LIT/'20 节点'/'M 思潮'
TOPICS=LIT/'30 专题'
WORKS=LIT/'40 作品'
BASE='origin/topic/m-axis-m5.2-v2'

CFG={
'M1':('M1 早期现代思想与美学','M1 早期现代思想与美学.md','00 早期现代思想与美学','WL-TOPIC-M1-EARLY-MODERN',76),
'M2':('M2 19世纪文学思潮','M2 19世纪文学思潮.md','00 19世纪文学思潮','WL-TOPIC-M2-19C-MOVEMENTS',85),
'M3.1':('M3.1 现代主义','M3.1 现代主义.md','00 现代主义文学','WL-TOPIC-M3-MODERNISM',149),
'M3.2':('M3.2 先锋派','M3.2 先锋派.md','00 先锋派','WL-TOPIC-M3.2-AVANT-GARDE',68),
'M4':('M4 集体文学运动与文化政治','M4 政治、民族与文化运动.md','00 集体文学运动与文化政治','WL-TOPIC-M4-COLLECTIVE-MOVEMENTS',90),
'M5.1':('M5.1 战后思想与美学范式','M5.1 战后思想与美学范式.md','00 战后思想与美学范式','WL-TOPIC-M5.1-POSTWAR-AESTHETICS',80),
'M5.2':('M5.2 权力、身份与世界批评','M5.2 权力、身份与世界批评.md','00 权力、身份与世界批评','WL-TOPIC-M5.2-POWER-IDENTITY-WORLD',74),
}
REQ_WORK_VIEWS=['全部作品','核心 ★','重点 ◆','扩展 △','未读','已读','按地域','按思潮','按类型','按主题','待校验']
REQ_STRUCT_VIEWS=['全部知识节点','核心结构','专题分支','形成机制']
REQ_STRUCT_KEYS=['id:','type:','topic_id:','parent:','dimension:','sequence:']
issues=[]
counts={}

for code,(folder,nodefile,home,topic_id,expected) in CFG.items():
    td=TOPICS/folder
    node=(NODES/nodefile).read_text(encoding='utf-8')
    expected_map=f'../../30 专题/{folder}/{home}'
    if f'topic_map: "{expected_map}"' not in node: issues.append(f'{code}: bad topic_map')
    if not (td/(home+'.md')).exists(): issues.append(f'{code}: missing homepage')
    b2=next(td.glob('02 *.base')).read_text(encoding='utf-8')
    b3=next(td.glob('03 *.base')).read_text(encoding='utf-8')
    if f'topic_id == "{topic_id}"' not in b2: issues.append(f'{code}: structure base topic filter')
    for v in REQ_STRUCT_VIEWS:
        if f'name: {v}' not in b2: issues.append(f'{code}: missing structure view {v}')
    if 'type == "work"' not in b3 or f'topics.contains("{topic_id}")' not in b3:
        issues.append(f'{code}: work base filter')
    for v in REQ_WORK_VIEWS:
        if f'name: {v}' not in b3: issues.append(f'{code}: missing work view {v}')
    struct_files=[]
    for p in td.rglob('*.md'):
        rel=p.relative_to(td).as_posix()
        if rel.startswith(('10 ','11 ','12 ','13 ')):
            struct_files.append(p)
            txt=p.read_text(encoding='utf-8')
            if not txt.startswith('---\n'): issues.append(f'{code}: no fm {rel}')
            for k in REQ_STRUCT_KEYS:
                if k not in txt.split('\n---\n',1)[0]: issues.append(f'{code}: missing {k} {rel}')
            if f'topic_id: "{topic_id}"' not in txt.split('\n---\n',1)[0]: issues.append(f'{code}: wrong topic_id {rel}')
    if not struct_files: issues.append(f'{code}: no structure docs')
    n=0
    for p in WORKS.glob('*.md'):
        txt=p.read_text(encoding='utf-8')
        fm=txt.split('\n---\n',1)[0] if txt.startswith('---\n') else ''
        if topic_id in fm: n+=1
    counts[code]=n
    if n!=expected: issues.append(f'{code}: works {n} != {expected}')

for code in ['M4','M5.1','M5.2']:
    folder=CFG[code][0]; td=TOPICS/folder
    canvas=next(td.glob('01 *.canvas'))
    data=json.loads(canvas.read_text(encoding='utf-8'))
    if len(data.get('nodes',[]))<7: issues.append(f'{code}: canvas too thin')
    if sum(1 for n in data.get('nodes',[]) if n.get('type')=='file')<4: issues.append(f'{code}: canvas lacks file anchors')
    for p in (td/'10 核心结构').glob('*.md'):
        body=p.read_text(encoding='utf-8').split('\n---\n',1)[-1]
        if len(body.strip())<100: issues.append(f'{code}: thin core doc {p.name}')

# Integration closure must not mutate canonical works.
p=subprocess.run(['git','diff','--name-only',f'{BASE}...HEAD','--','个人通识知识系统_v2_A2/30 世界文学/40 作品'],cwd=ROOT,text=True,capture_output=True)
work_changes=[x for x in p.stdout.splitlines() if x.strip()]
if work_changes: issues.append(f'canonical works changed: {len(work_changes)}')

status='PASS' if not issues else 'FAIL'
print('# M-axis Final Integration Audit')
print('status',status)
print('counts',counts)
print('canonical_work_changes',len(work_changes))
print('issues',issues)
Path('reports').mkdir(exist_ok=True)
Path('reports/m_axis_integration_audit.json').write_text(json.dumps({'status':status,'counts':counts,'canonical_work_changes':work_changes,'issues':issues},ensure_ascii=False,indent=2),encoding='utf-8')
Path('reports/m_axis_integration_audit.md').write_text('# M-axis Final Integration Audit\n\n- status: **'+status+'**\n- counts: `'+json.dumps(counts,ensure_ascii=False)+'`\n- canonical work changes: **'+str(len(work_changes))+'**\n- issues: `'+json.dumps(issues,ensure_ascii=False)+'`\n',encoding='utf-8')
if issues: raise SystemExit(1)
