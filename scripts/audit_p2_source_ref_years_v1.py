from pathlib import Path
import csv,re,yaml

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORK=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_openlibrary_deep_review_v1.csv'
OUT=AUDIT/'p2_source_ref_years_v1.csv'
REPORT=AUDIT/'P2_SOURCE_REF_YEARS_V1.md'

YEAR_RE=re.compile(r'(?<!\d)(1[0-9]{3}|20[0-2][0-9])(?!\d)')
REFKEY_RE=re.compile(r'.*_source_refs$')

def fm(path):
    s=path.read_text(encoding='utf-8-sig')
    if not s.startswith('---'):
        return {}
    _,front,_=s.split('---',2)
    return yaml.safe_load(front) or {}

def find_source(name):
    hits=[]
    for p in ROOT.rglob(name):
        if p.is_file() and '_audit' not in p.parts and '40 作品' not in p.parts:
            hits.append(p)
    return hits

def t_of(y):
    y=int(y)
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'

p2_files=[]
if IN.exists():
    with IN.open(encoding='utf-8-sig',newline='') as f:
        p2_files=[r['file'] for r in csv.DictReader(f)]
else:
    p2_files=[p.name for p in WORK.glob('*.md') if not (fm(p).get('axis_t') or [])]

rows=[]
for fn in p2_files:
    wp=WORK/fn
    if not wp.exists(): continue
    d=fm(wp)
    refs=[]
    for k,v in d.items():
        if REFKEY_RE.match(str(k)):
            if isinstance(v,list): refs.extend(map(str,v))
            elif v: refs.append(str(v))
    evidence=[]
    for ref in refs:
        m=re.match(r'(.+\.md):(\d+)$',ref)
        if not m: continue
        name,ln=m.group(1),int(m.group(2))
        for sp in find_source(name):
            lines=sp.read_text(encoding='utf-8-sig',errors='replace').splitlines()
            a=max(0,ln-3); b=min(len(lines),ln+2)
            window=' | '.join(lines[a:b])
            years=sorted(set(int(x) for x in YEAR_RE.findall(window)))
            if years:
                evidence.append((str(sp.relative_to(ROOT)),ln,years,window[:500]))
    flat=sorted(set(y for _,_,ys,_ in evidence for y in ys))
    status='NO_SOURCE_YEAR'
    chosen=''
    chosen_t=''
    if len(flat)==1:
        chosen=str(flat[0]); chosen_t=t_of(flat[0]); status='SOURCE_YEAR_SINGLE'
    elif flat:
        ts={t_of(y) for y in flat}
        status='SOURCE_YEAR_SAME_T' if len(ts)==1 else 'SOURCE_YEAR_CONFLICT'
        if len(ts)==1:
            chosen=str(min(flat)); chosen_t=next(iter(ts))
    rows.append({
        'file':fn,'id':d.get('id',''),'title':d.get('title',''),'author':d.get('author_original') or d.get('author',''),
        'refs':' ; '.join(refs),'source_years':' ; '.join(map(str,flat)),'status':status,
        'chosen_year':chosen,'chosen_t':chosen_t,
        'evidence':' || '.join(f'{p}:{ln} years={ys} :: {w}' for p,ln,ys,w in evidence)
    })

AUDIT.mkdir(parents=True,exist_ok=True)
with OUT.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys() if rows else ['file'])
    w.writeheader(); w.writerows(rows)
from collections import Counter
c=Counter(r['status'] for r in rows)
REPORT.write_text('# P2 Source-Ref Year Recovery V1\n\n> Read-only provenance audit. Years are extracted only from the original source files referenced by each canonical Work.\n\n'+f'- P2 rows inspected: **{len(rows)}**\n'+''.join(f'- {k}: **{v}**\n' for k,v in sorted(c.items()))+'\nNo Work files were mutated.\n\n`P2_SOURCE_REF_YEARS_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8')
print(c)
