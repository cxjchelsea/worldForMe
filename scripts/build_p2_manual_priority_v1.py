from pathlib import Path
import csv
from collections import Counter

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_residual_review_v1.csv'; OUT=AUDIT/'p2_manual_priority_v1.csv'; REPORT=AUDIT/'P2_MANUAL_PRIORITY_V1.md'; MARKER=AUDIT/'RUN_P2_MANUAL_PRIORITY_V1'

def count_list(s):
    return len([x for x in (s or '').split(';') if x.strip()])

def score(r):
    pts=0; reasons=[]
    if (r.get('canon_id') or '').strip(): pts+=4;reasons.append('CANON')
    if (r.get('awards') or '').strip(): pts+=3;reasons.append('AWARD')
    tc=count_list(r.get('topics'))
    if tc>=3:pts+=2;reasons.append('MULTI_TOPIC_3PLUS')
    elif tc>=2:pts+=1;reasons.append('MULTI_TOPIC_2')
    sc=count_list(r.get('source_ref_keys'))
    if sc>=2:pts+=1;reasons.append('MULTI_SOURCE_REF')
    bucket=r.get('residual_bucket','')
    # Work-level dating is usually easiest when author identity is already known.
    if bucket=='AUTHOR_RANGE_SPANS_T':pts+=2;reasons.append('WORK_DATE_ONLY')
    elif bucket=='AUTHOR_DATE_MISSING':pts+=1;reasons.append('AUTHOR_DATE_MISSING')
    if pts>=6:tier='P2M-A'
    elif pts>=3:tier='P2M-B'
    else:tier='P2M-C'
    return pts,tier,';'.join(reasons)

def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
    out=[]
    for r in rows:
        pts,tier,reasons=score(r);x=dict(r);x['manual_priority_score']=str(pts);x['manual_priority_tier']=tier;x['manual_priority_reasons']=reasons;out.append(x)
    out.sort(key=lambda r:(-int(r['manual_priority_score']),r.get('title','').casefold()))
    fields=[]
    for r in out:
        for k in r:
            if k not in fields:fields.append(k)
    with OUT.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
    c=Counter(r['manual_priority_tier'] for r in out);bc=Counter(r.get('residual_bucket','') for r in out)
    top=out[:30]
    lines=['# P2 Manual Review Priority V1','', '> Read-only prioritization of the current P2 residual. No Work file is modified.','',f'- Residual population: **{len(out)}**',f'- P2M-A (highest): **{c["P2M-A"]}**',f'- P2M-B: **{c["P2M-B"]}**',f'- P2M-C: **{c["P2M-C"]}**','','## Residual buckets','']
    for k,v in sorted(bc.items()):lines.append(f'- {k}: **{v}**')
    lines += ['','## Top 30 manual-research targets','']
    for r in top:lines.append(f"- {r['manual_priority_tier']} score={r['manual_priority_score']} | `{r.get('file','')}` | {r.get('author_original') or r.get('author','')} | {r.get('residual_bucket','')} | {r.get('manual_priority_reasons','')}")
    lines += ['','`P2_MANUAL_PRIORITY_V1 = BUILT_READ_ONLY`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink();print(dict(c))
if __name__=='__main__':main()
