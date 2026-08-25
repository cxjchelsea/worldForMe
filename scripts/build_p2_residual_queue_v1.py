from pathlib import Path
import csv,re
from collections import Counter

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORK=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_completeness'
INPUTS=[AUDIT/'p2_openlibrary_deep_safe_v1.csv',AUDIT/'p2_openlibrary_deep_review_v1.csv']
AUTHOR_REVIEW=AUDIT/'p2_author_only_t_review_v1.csv'
OUT=AUDIT/'p2_residual_review_v1.csv'
REPORT=AUDIT/'P2_RESIDUAL_REVIEW_V1.md'
MARKER=AUDIT/'RUN_P2_RESIDUAL_REVIEW_V1'

def has_t(path):
    if not path.exists(): return False
    text=path.read_text(encoding='utf-8-sig')
    return bool(re.search(r'(?m)^axis_t:\s*\n\s*-\s*T[0-6]\b',text) or re.search(r'(?m)^axis_t:\s*\[\s*T[0-6]',text))

rows={}
for p in INPUTS:
    if p.exists():
        with p.open(encoding='utf-8-sig',newline='') as f:
            for r in csv.DictReader(f): rows[(r.get('id',''),r.get('file',''))]=dict(r)
author_reason={}
if AUTHOR_REVIEW.exists():
    with AUTHOR_REVIEW.open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f): author_reason[(r.get('id',''),r.get('file',''))]=r.get('author_only_status','')

out=[]
for key,r in rows.items():
    fn=r.get('file','')
    if has_t(WORK/fn): continue
    reason=author_reason.get(key,'') or 'NO_AUTHOR_ONLY_RESULT'
    deep=r.get('deep_status','') or r.get('resolution_status','')
    bucket='OTHER_REVIEW'
    if reason.startswith('ACTIVE_RANGE_SPANS_T'): bucket='AUTHOR_RANGE_SPANS_T'
    elif reason.startswith('NO_STRONG_MATCH'): bucket='AUTHOR_IDENTITY_REVIEW'
    elif reason=='NO_BIRTH': bucket='AUTHOR_DATE_MISSING'
    elif reason.startswith('API:'): bucket='AUTHOR_API_RETRY'
    elif reason=='MULTI_OR_EMPTY': bucket='MULTI_OR_MISSING_AUTHOR'
    elif deep in {'NO_RELIABLE_MATCH',''}: bucket='WORK_BIBLIOGRAPHY_REVIEW'
    x=dict(r);x['author_only_reason']=reason;x['residual_bucket']=bucket
    out.append(x)

fields=[]
for r in out:
    for k in r:
        if k not in fields:fields.append(k)
with OUT.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(out)
c=Counter(r['residual_bucket'] for r in out)
md=['# P2 Residual Review Queue V1','', '> Read-only residual queue after governed P2 T-only automation. It contains only members of the original 421 P2 cohort that still lack a canonical T coordinate.','',f'- Original P2 cohort: **{len(rows)}**',f'- Resolved / now has T: **{len(rows)-len(out)}**',f'- Residual unresolved: **{len(out)}**','', '## Residual buckets','']
for k,v in sorted(c.items()):md.append(f'- {k}: **{v}**')
md += ['','No Work files were mutated.','','`P2_RESIDUAL_REVIEW_V1 = BUILT_READ_ONLY`','']
REPORT.write_text('\n'.join(md),encoding='utf-8')
MARKER.unlink()
print({'original':len(rows),'resolved':len(rows)-len(out),'residual':len(out),'buckets':dict(c)})
