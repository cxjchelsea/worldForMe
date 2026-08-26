from __future__ import annotations
import re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
TOPICS = LIT/'30 专题'
BASE_REF = 'origin/topic/m-axis-m5.2-v2'

CFG = {
'M1': ('M1 早期现代思想与美学','WL-TOPIC-M1-EARLY-MODERN'),
'M2': ('M2 19世纪文学思潮','WL-TOPIC-M2-19C-MOVEMENTS'),
'M3.1': ('M3.1 现代主义','WL-TOPIC-M3-MODERNISM'),
'M3.2': ('M3.2 先锋派','WL-TOPIC-M3.2-AVANT-GARDE'),
'M4': ('M4 集体文学运动与文化政治','WL-TOPIC-M4-COLLECTIVE-MOVEMENTS'),
'M5.1': ('M5.1 战后思想与美学范式','WL-TOPIC-M5.1-POSTWAR-AESTHETICS'),
'M5.2': ('M5.2 权力、身份与世界批评','WL-TOPIC-M5.2-POWER-IDENTITY-WORLD'),
}

DIM_DEFAULT = {'01':'definition','02':'history','03':'historical_system','04':'mechanism','05':'transmission','06':'comparison','07':'reading_route','00':'overview'}


def split_frontmatter(text:str):
    if not text.startswith('---\n'):
        return '', text
    end=text.find('\n---\n',4)
    if end<0:
        return '', text
    return text[4:end], text[end+5:]


def scalar(raw:str,key:str):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?([^\n"\']+)["\']?\s*$',raw)
    return m.group(1).strip() if m else None


def base_frontmatter(path:Path):
    rel=path.relative_to(ROOT).as_posix()
    p=subprocess.run(['git','show',f'{BASE_REF}:{rel}'],cwd=ROOT,text=True,encoding='utf-8',errors='replace',capture_output=True)
    if p.returncode!=0:
        return ''
    raw,_=split_frontmatter(p.stdout)
    return raw


def clean_common(raw:str):
    common={'id','type','topic_id','parent','dimension','sequence'}
    out=[]
    for line in raw.splitlines():
        m=re.match(r'^([A-Za-z0-9_.-]+):',line)
        if m and m.group(1) in common:
            continue
        out.append(line)
    return '\n'.join(out).strip()


def default_id(code:str, rel:str):
    nums=re.findall(r'(^|/)(\d+)',rel)
    parts=[n for _,n in nums]
    suffix='-'.join(parts) if parts else re.sub(r'\W+','-',Path(rel).stem).strip('-')
    return f'WL-{code}-NODE-{suffix}'


def classify(code:str, rel:str, base_raw:str):
    first=Path(rel).name[:2]
    seq=int(first) if first.isdigit() else 0
    if rel.startswith('10 核心结构/'):
        typ='literature_topic_structure'; dim=DIM_DEFAULT.get(first,'core_question')
    elif rel.startswith('11 '):
        typ='literature_topic_section'
        dim={'M1':'movement','M2':'movement','M3.1':'tradition','M3.2':'movement','M4':'movement','M5.1':'paradigm','M5.2':'framework'}.get(code,'literary_field')
    elif rel.startswith('12 '):
        typ='literature_topic_mechanism'; dim='mechanism'
    elif rel.startswith('13 '):
        typ='literature_topic_section'; dim='comparison'
    else:
        raise ValueError(rel)
    return typ, scalar(base_raw,'dimension') or dim, int(scalar(base_raw,'sequence') or seq)


def rewrite_structure_base(td:Path, topic_id:str):
    b2=next(td.glob('02 *.base'))
    text=b2.read_text(encoding='utf-8')
    text=re.sub(r'dimension\.replace\("historical_system", "谱系与内部结构"\)',
                'dimension.replace("tradition", "传统与地域").replace("movement", "思潮与运动").replace("paradigm", "美学范式").replace("framework", "批评框架").replace("historical_system", "谱系与内部结构")', text)
    b2.write_text(text,encoding='utf-8')

for code,(folder,topic_id) in CFG.items():
    td=TOPICS/folder
    for path in td.rglob('*.md'):
        rel=path.relative_to(td).as_posix()
        if not rel.startswith(('10 ','11 ','12 ','13 ')):
            continue
        current=path.read_text(encoding='utf-8')
        _,body=split_frontmatter(current)
        old=base_frontmatter(path)
        typ,dim,seq=classify(code,rel,old)
        ident=scalar(old,'id') or default_id(code,rel)
        parent=scalar(old,'parent') or topic_id
        extra=clean_common(old)
        fm=[f'id: "{ident}"',f'type: "{typ}"',f'topic_id: "{topic_id}"',f'parent: "{parent}"',f'dimension: "{dim}"',f'sequence: {seq}']
        if extra: fm.append(extra)
        path.write_text('---\n'+'\n'.join(fm)+'\n---\n'+body.lstrip('\n'),encoding='utf-8')
    rewrite_structure_base(td,topic_id)

print('restored topic-specific metadata while preserving T-axis common schema')
