from __future__ import annotations
import re, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
TOPICS=LIT/'30 专题'; WORKS=LIT/'40 作品'
PRE='fa1e870648948a806277b284454c61271e5faf32'
CFG={
'M1':('M1 早期现代思想与美学','WL-TOPIC-M1-EARLY-MODERN','m1_priority','m1_movement_cluster','m1_axes','m1_history_position',76),
'M2':('M2 19世纪文学思潮','WL-TOPIC-M2-19C-MOVEMENTS','m2_priority','m2_movement_cluster','m2_axes','m2_history_position',85),
'M3.1':('M3.1 现代主义','WL-TOPIC-M3-MODERNISM','modernism_priority','modernism_tradition_cluster','modernism_axes','modernism_history_position',149),
'M3.2':('M3.2 先锋派','WL-TOPIC-M3.2-AVANT-GARDE','m32_priority','m32_movement_cluster','m32_axes','m32_history_position',68),
'M4':('M4 集体文学运动与文化政治','WL-TOPIC-M4-COLLECTIVE-MOVEMENTS','m4_priority','m4_movement_cluster','m4_axes','m4_history_position',90),
'M5.1':('M5.1 战后思想与美学范式','WL-TOPIC-M5.1-POSTWAR-AESTHETICS','m51_priority','m51_movement_cluster','m51_axes','m51_history_position',80),
'M5.2':('M5.2 权力、身份与世界批评','WL-TOPIC-M5.2-POWER-IDENTITY-WORLD','m52_priority','m52_framework_cluster','m52_axes','m52_history_position',74),
}
issues=[]; counts={}

def split(text):
    if not text.startswith('---\n'):return '',text
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
            if tail.startswith('[') and tail.endswith(']'): return [x.strip().strip('"\'') for x in tail[1:-1].split(',') if x.strip()]
            j=i+1
            while j<len(ls) and ls[j].startswith('-'):
                out.append(ls[j][1:].strip().strip('"\''));j+=1
            return out
    return out
def field_block(fm,key):
    ls=fm.splitlines()
    for i,l in enumerate(ls):
        if l.startswith(key+':'):
            out=[l]; j=i+1
            while j<len(ls) and ls[j].startswith('-'):
                out.append(ls[j]);j+=1
            return '\n'.join(out)
    return ''
def valid_link(raw):
    s=raw.strip("'\"")
    if not(s.startswith('[[') and s.endswith(']]')): return False
    target=s[2:-2].split('|',1)[0]
    p=(WORKS/target).resolve()
    return (p.exists() or Path(str(p)+'.md').exists()) and str(p).startswith(str(ROOT.resolve()))

def old_text(p):
    rel=p.relative_to(ROOT).as_posix()
    r=subprocess.run(['git','show',f'{PRE}:{rel}'],cwd=ROOT,text=True,encoding='utf-8',errors='replace',capture_output=True)
    return r.stdout if r.returncode==0 else ''

for code,(folder,topic,p,c,a,h,expected) in CFG.items():
    td=TOPICS/folder
    b3=next(td.glob('03 *.base')).read_text(encoding='utf-8')
    required=['file.folder == "个人通识知识系统_v2_A2/30 世界文学/40 作品"',f'topics.contains("{topic}")',f'note.{h}:',f'note.{a}:','displayName: M轴坐标','name: 按历史位置']
    for x in required:
        if x not in b3: issues.append(f'{code}: Base missing {x}')
    b2=next(td.glob('02 *.base')).read_text(encoding='utf-8')
    for x in ['note.history_position:','note.mechanism:','name: 形成机制']:
        if x not in b2: issues.append(f'{code}: structure Base missing {x}')
    members=[]
    for wp in WORKS.glob('*.md'):
        text=wp.read_text(encoding='utf-8'); fm,_=split(text)
        if topic not in lst(fm,'topics'): continue
        members.append(wp)
        if not scalar(fm,p):issues.append(f'{code}: missing priority {wp.name}')
        if not scalar(fm,c):issues.append(f'{code}: missing cluster {wp.name}')
        if not lst(fm,a):issues.append(f'{code}: missing mechanism {wp.name}')
        if not scalar(fm,h):issues.append(f'{code}: missing history {wp.name}')
        links=lst(fm,'topic_links')
        dead=[x for x in links if not valid_link(x)]
        if dead:issues.append(f'{code}: dead topic_links {wp.name}: {dead[:2]}')
        old=old_text(wp)
        if old:
            ofm,_=split(old)
            keys=set()
            for line in ofm.splitlines():
                m=re.match(r'^([A-Za-z0-9_.-]+):',line)
                if m and (m.group(1)=='axis_t' or re.match(r'^t[0-6]_',m.group(1)) or m.group(1).startswith('postwar_')): keys.add(m.group(1))
            for k in keys:
                if field_block(fm,k)!=field_block(ofm,k): issues.append(f'{code}: T-field changed {wp.name} {k}')
    counts[code]=len(members)
    if len(members)!=expected:issues.append(f'{code}: count {len(members)} != {expected}')
    struct=[]; mech_nonempty=0
    for sp in td.rglob('*.md'):
        rel=sp.relative_to(td).as_posix()
        if not rel.startswith(('10 ','11 ','12 ','13 ')):continue
        sfm,_=split(sp.read_text(encoding='utf-8')); struct.append(sp)
        if not scalar(sfm,'history_position'):issues.append(f'{code}: structure history empty {rel}')
        if lst(sfm,'mechanism'):mech_nonempty+=1
    if not struct:issues.append(f'{code}: no structure docs')
    if mech_nonempty==0:issues.append(f'{code}: no populated structure mechanism')

status='PASS' if not issues else 'FAIL'
report=['# M-axis Base Semantic Audit v2','',f'- status: **{status}**',f'- counts: `{counts}`',f'- issues: **{len(issues)}**','']
if issues:
    report+=['## Issues','']+[f'- {x}' for x in issues[:200]]
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports'/'m_axis_base_semantic_audit_v2.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('\n'.join(report))
if issues:raise SystemExit(2)
