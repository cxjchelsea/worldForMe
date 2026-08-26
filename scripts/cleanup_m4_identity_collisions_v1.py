from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
WORKS=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'/'40 作品'
PAIRS=[
('卡勒瓦拉.md','卡勒瓦拉（埃利亚斯·伦罗特）.md'),
('甘蔗.md','甘蔗（让·图默）.md'),
('神的木片.md','神的木片（奥斯曼·森贝纳）.md'),
]
def parts(text):
    e=text.find('\n---\n',4); return text[4:e],text[e+5:]
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm); return m.group(1).strip() if m else ''
def listv(fm,key):
    lines=fm.splitlines(); out=[]
    for i,x in enumerate(lines):
        if x.startswith(key+':'):
            j=i+1
            while j<len(lines) and lines[j].startswith('- '): out.append(lines[j][2:].strip()); j+=1
            return out
    return out
def union(fm,key,vals):
    lines=fm.splitlines(); i=next((i for i,x in enumerate(lines) if x.startswith(key+':')),None)
    if i is None: return fm+'\n'+key+':\n'+'\n'.join('- '+v for v in vals)
    old=[]; j=i+1
    while j<len(lines) and lines[j].startswith('- '): old.append(lines[j][2:].strip()); j+=1
    new=old+[v for v in vals if v not in old]; lines[i:j]=[key+':']+['- '+v for v in new]
    return '\n'.join(lines)
def setscalar(fm,key,val):
    line=f'{key}: "{val}"'; pat=rf'(?m)^{re.escape(key)}:.*$'
    return re.sub(pat,line,fm,count=1) if re.search(pat,fm) else fm+'\n'+line
for keep_name,dup_name in PAIRS:
    keep=WORKS/keep_name; dup=WORKS/dup_name
    if not keep.exists() or not dup.exists(): continue
    kfm,kbody=parts(keep.read_text(encoding='utf-8')); dfm,_=parts(dup.read_text(encoding='utf-8'))
    kfm=union(kfm,'axis_m',listv(dfm,'axis_m')); kfm=union(kfm,'topics',listv(dfm,'topics'))
    kfm=setscalar(kfm,'m4_priority',scalar(dfm,'m4_priority')); kfm=setscalar(kfm,'m4_movement_cluster',scalar(dfm,'m4_movement_cluster')); kfm=union(kfm,'m4_axes',listv(dfm,'m4_axes'))
    keep.write_text('---\n'+kfm+'\n---\n'+kbody,encoding='utf-8'); dup.unlink()
    print('merged',dup_name,'->',keep_name)
