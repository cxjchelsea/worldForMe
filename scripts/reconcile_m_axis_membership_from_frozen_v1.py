from __future__ import annotations
import re, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORKS=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
BASE='origin/topic/m-axis-integration-closure-v1'
CFG={
'M1':('WL-TOPIC-M1-EARLY-MODERN',['m1_priority','m1_movement_cluster','m1_axes']),
'M2':('WL-TOPIC-M2-19C-MOVEMENTS',['m2_priority','m2_movement_cluster','m2_axes']),
'M3.1':('WL-TOPIC-M3-MODERNISM',['modernism_priority','modernism_tradition_cluster','modernism_axes']),
'M3.2':('WL-TOPIC-M3.2-AVANT-GARDE',['m32_priority','m32_movement_cluster','m32_axes']),
'M4':('WL-TOPIC-M4-COLLECTIVE-MOVEMENTS',['m4_priority','m4_movement_cluster','m4_axes']),
'M5.1':('WL-TOPIC-M5.1-POSTWAR-AESTHETICS',['m51_priority','m51_movement_cluster','m51_axes']),
'M5.2':('WL-TOPIC-M5.2-POWER-IDENTITY-WORLD',['m52_priority','m52_framework_cluster','m52_role','m52_axes']),
}
EXPECTED={'M1':76,'M2':85,'M3.1':149,'M3.2':68,'M4':90,'M5.1':80,'M5.2':74}

def split(text):
    if not text.startswith('---\n'): return '',text
    e=text.find('\n---\n',4)
    return (text[4:e],text[e+5:]) if e>=0 else ('',text)
def lst(fm,key):
    ls=fm.splitlines(); out=[]
    for i,l in enumerate(ls):
        if l.startswith(key+':'):
            tail=l.split(':',1)[1].strip()
            if tail.startswith('[') and tail.endswith(']'): return [x.strip().strip('"\'') for x in tail[1:-1].split(',') if x.strip()]
            j=i+1
            while j<len(ls) and ls[j].startswith('-'):
                out.append(ls[j][1:].strip().strip('"\'')); j+=1
            return out
    return out
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm)
    return m.group(1).strip().strip('"\'') if m else ''
def replace_scalar(text,key,val):
    fm,body=split(text); ls=fm.splitlines(); out=[]; done=False; i=0
    while i<len(ls):
        if ls[i].startswith(key+':'):
            out.append(f'{key}: "{val}"'); done=True; i+=1
            while i<len(ls) and ls[i].startswith('-'): i+=1
        else: out.append(ls[i]); i+=1
    if not done: out.append(f'{key}: "{val}"')
    return '---\n'+'\n'.join(out)+'\n---\n'+body
def replace_list(text,key,vals):
    fm,body=split(text); ls=fm.splitlines(); out=[]; done=False; i=0
    while i<len(ls):
        if ls[i].startswith(key+':'):
            out.append(key+':'); out.extend('- '+v for v in vals); done=True; i+=1
            while i<len(ls) and ls[i].startswith('-'): i+=1
        else: out.append(ls[i]); i+=1
    if not done:
        out.append(key+':'); out.extend('- '+v for v in vals)
    return '---\n'+'\n'.join(out)+'\n---\n'+body
def base_text(p):
    rel=p.relative_to(ROOT).as_posix()
    r=subprocess.run(['git','show',f'{BASE}:{rel}'],cwd=ROOT,text=True,encoding='utf-8',errors='replace',capture_output=True)
    return r.stdout if r.returncode==0 else ''

counts={k:0 for k in CFG}
restored={k:0 for k in CFG}
for p in WORKS.glob('*.md'):
    cur=p.read_text(encoding='utf-8'); b=base_text(p)
    if not b: continue
    bfm,_=split(b)
    changed=False
    for code,(topic,fields) in CFG.items():
        if topic not in lst(bfm,'topics'): continue
        counts[code]+=1
        cfm,_=split(cur)
        topics=lst(cfm,'topics')
        if topic not in topics:
            topics.append(topic); cur=replace_list(cur,'topics',topics); changed=True; restored[code]+=1
        # Restore only M-topic-owned fields from frozen source; preserve all newer T/R/G/Q metadata.
        for f in fields:
            vals=lst(bfm,f)
            sv=scalar(bfm,f)
            if vals:
                cur=replace_list(cur,f,vals); changed=True
            elif sv:
                cur=replace_scalar(cur,f,sv); changed=True
        # Preserve/add the exact M-axis coordinate(s) that existed in the frozen source.
        curfm,_=split(cur); curr_axis=lst(curfm,'axis_m'); base_axis=lst(bfm,'axis_m')
        for x in base_axis:
            if (x.startswith(code+' ') or x.startswith(code+'/') or (code=='M3.1' and x.startswith('M3.1')) or (code=='M3.2' and x.startswith('M3.2')) or (code=='M5.1' and x.startswith('M5.1')) or (code=='M5.2' and x.startswith('M5.2'))) and x not in curr_axis:
                curr_axis.append(x); changed=True
        if changed: cur=replace_list(cur,'axis_m',curr_axis)
    if changed:p.write_text(cur,encoding='utf-8')

for code,n in counts.items():
    if n!=EXPECTED[code]: raise SystemExit(f'{code}: frozen source count {n} != {EXPECTED[code]}')
print('frozen_membership_counts',counts)
print('restored_missing_topics',restored)
