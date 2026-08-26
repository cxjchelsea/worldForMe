from __future__ import annotations
import subprocess, re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKS_REL = '个人通识知识系统_v2_A2/30 世界文学/40 作品'
WORKS = ROOT / WORKS_REL
CFG = {
    'M1': ('origin/topic/m-axis-m1-v2', 'm1_priority', 76),
    'M2': ('origin/topic/m-axis-m2-v2', 'm2_priority', 85),
    'M3.1': ('origin/topic/m-axis-m3.1-v2', 'modernism_priority', 149),
    'M3.2': ('origin/topic/m-axis-m3.2-v2', 'm32_priority', 68),
    'M4': ('origin/topic/m-axis-m4-v2', 'm4_priority', 90),
    'M5.1': ('origin/topic/m-axis-m5.1-v2', 'm51_priority', 80),
    'M5.2': ('origin/topic/m-axis-m5.2-v2', 'm52_priority', 74),
}
VALID = {'★','◆','△'}

def first_frontmatter(text: str):
    t=text.replace('\r\n','\n').replace('\r','\n')
    m=re.match(r'^---\s*\n(.*?)\n---\s*(?:\n|$)',t,re.S)
    return m.group(1) if m else None

def parse_yaml(text: str):
    fm=first_frontmatter(text)
    if fm is None: return None,'NO_FRONTMATTER'
    try:
        data=yaml.safe_load(fm) or {}
        if not isinstance(data,dict): return None,'FRONTMATTER_NOT_MAPPING'
        return data,None
    except Exception as e:
        return None,'YAML_ERROR: '+str(e).split('\n')[0]

def run(args,check=True):
    r=subprocess.run(['git',*args],cwd=ROOT,text=True,encoding='utf-8',errors='replace',capture_output=True)
    if check and r.returncode!=0:
        raise RuntimeError('git '+' '.join(args)+'\n'+r.stderr)
    return r

def branch_members(branch,field):
    # Fast historical membership: ask git grep for files that contain a valid priority line.
    pat=rf'^{re.escape(field)}:[[:space:]]*["\x27]?[★◆△]["\x27]?[[:space:]]*$'
    r=run(['grep','-l','-E',pat,branch,'--',WORKS_REL],check=False)
    if r.returncode not in (0,1):
        raise RuntimeError(r.stderr)
    out=set()
    for line in r.stdout.splitlines():
        # format is branch:path
        rel=line.split(':',1)[1] if ':' in line else line
        if rel.endswith('.md'): out.add(Path(rel).name)
    return out

def current_members(field):
    out=set(); problems={}
    for p in WORKS.glob('*.md'):
        txt=p.read_text(encoding='utf-8',errors='strict')
        data,err=parse_yaml(txt)
        if err:
            if re.search(rf'(?m)^{re.escape(field)}:',txt): problems[p.name]=err
            continue
        val=str(data.get(field,'')).strip()
        if val in VALID and data.get('type')=='work': out.add(p.name)
        elif field in data: problems[p.name]=f'FIELD={data.get(field)!r}, type={data.get("type")!r}'
    return out,problems

lines=['# M-axis Obsidian Membership Gap Audit v1','']
fail=False
for code,(branch,field,declared) in CFG.items():
    expected=branch_members(branch,field)
    current,probs=current_members(field)
    missing=sorted(expected-current); extra=sorted(current-expected)
    lines += [f'## {code}',f'- frozen branch: `{branch}`',f'- frozen members discovered: **{len(expected)}** (declared {declared})',f'- current Obsidian-readable members: **{len(current)}**',f'- missing: **{len(missing)}**',f'- extra: **{len(extra)}**']
    if missing:
        lines += ['- Missing files:']+[f'  - `{x}` — {probs.get(x,"field absent from first YAML")}' for x in missing]
    if extra:
        lines += ['- Extra files:']+[f'  - `{x}`' for x in extra]
    lines.append('')
    if len(expected)!=declared or len(current)!=declared or missing or extra: fail=True
report='\n'.join(lines)+'\n'
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports'/'m_axis_obsidian_membership_gap_v1.md').write_text(report,encoding='utf-8')
print(report)
if fail: sys.exit(2)
