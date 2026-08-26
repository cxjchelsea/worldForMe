from pathlib import Path
import re

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS = ROOT/'40 作品'
TOP = ROOT/'30 专题'
AUD = ROOT/'_audit'/'r_axis_acceptance'/'R_AXIS_METADATA_COMPLETENESS_V1.md'

TOPICS = {
'R1': ('R1 西亚—地中海古老传统','R1 西亚—地中海古老传统'),
'R2': ('R2 东亚文学','R2 东亚文学'),
'R3': ('R3 南亚文学','R3 南亚文学'),
'R4': ('R4 欧洲文学','R4 欧洲文学'),
'R5': ('R5 北美文学','R5 北美文学'),
'R6': ('R6 拉丁美洲与加勒比','R6 拉丁美洲与加勒比'),
'R7': ('R7 非洲文学','R7 非洲文学'),
'R8': ('R8 东南亚文学','R8 东南亚文学'),
'R9': ('R9 大洋洲与太平洋文学','R9 大洋洲与太平洋'),
}

def fm(txt):
    m=re.match(r'^---\s*\n(.*?)\n---',txt,re.S)
    return m.group(1) if m else ''

def scalar(front,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',front)
    return m.group(1).strip(' "\'') if m else ''

def list_field(front,key):
    lines=front.splitlines(); out=[]
    for i,line in enumerate(lines):
        if re.match(rf'^{re.escape(key)}:\s*\[\]\s*$', line): return []
        if re.match(rf'^{re.escape(key)}:\s*$', line):
            for n in lines[i+1:]:
                m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
                if m: out.append(m.group(1)); continue
                if n.strip() and not n.startswith((' ','\t')): break
            return out
    return []

rows=[]
for code,(folder,label) in TOPICS.items():
    total=mp=mt=mr=ma=mm=mg=mq=0
    pfx=code.lower()
    for p in WORKS.glob('*.md'):
        f=fm(p.read_text(encoding='utf-8'))
        if label not in list_field(f,'axis_r'): continue
        total+=1
        if not scalar(f,f'{pfx}_priority'): mp+=1
        if not scalar(f,f'{pfx}_tradition'): mt+=1
        if not scalar(f,f'{pfx}_role'): mr+=1
        if not scalar(f,'author'): ma+=1
        if not list_field(f,'axis_m'): mm+=1
        if not list_field(f,'axis_g'): mg+=1
        if not list_field(f,'axis_q'): mq+=1
    rows.append((code,total,mp,mt,mr,ma,mm,mg,mq))

# R10 topic membership
code='R10'; pfx='r10'; total=mp=mt=mr=ma=mm=mg=mq=0
for p in WORKS.glob('*.md'):
    f=fm(p.read_text(encoding='utf-8'))
    if 'WL-TOPIC-R10-TRANSREGIONAL' not in list_field(f,'topics'): continue
    total+=1
    if not scalar(f,'r10_priority'): mp+=1
    if not scalar(f,'r10_tradition'): mt+=1
    if not scalar(f,'r10_role'): mr+=1
    if not scalar(f,'author'): ma+=1
    if not list_field(f,'axis_m'): mm+=1
    if not list_field(f,'axis_g'): mg+=1
    if not list_field(f,'axis_q'): mq+=1
rows.append((code,total,mp,mt,mr,ma,mm,mg,mq))

# structure mechanism gaps and actual group dirs
struct=[]
for code,(folder,*_) in {**TOPICS,'R10':('R10 跨区域文学传统',)}.items():
    d=TOP/folder
    nodes=[]
    for sub in ['10 核心结构','11 内部传统','12 跨传统网络']:
        sd=d/sub
        if sd.exists():
            for p in sd.glob('*.md'):
                f=fm(p.read_text(encoding='utf-8'))
                if scalar(f,'topic_id'):
                    nodes.append((sub,p,scalar(f,'mechanism')))
    struct.append((code,len(nodes),sum(1 for _,_,m in nodes if not m), sorted(set(s for s,_,_ in nodes))))

lines=['# R Axis Metadata Completeness V1','', '## Work metadata gaps','', '| R | Works | priority缺失 | tradition缺失 | role缺失 | author缺失 | axis_m缺失 | axis_g缺失 | axis_q缺失 |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for r in rows:
    lines.append('| '+' | '.join(map(str,r))+' |')
lines += ['', '## Structure metadata gaps','', '| R | 结构节点 | mechanism缺失 | 实际专题分组 |','|---|---:|---:|---|']
for code,n,miss,groups in struct:
    lines.append(f'| {code} | {n} | {miss} | {" / ".join(groups)} |')
AUD.parent.mkdir(parents=True,exist_ok=True)
AUD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(AUD)
