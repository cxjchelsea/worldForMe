from __future__ import annotations

import csv,re
from pathlib import Path

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_completeness'
AUTHOR_ONLY=AUDIT/'p2_author_only_t_safe_v1.csv'
LIFESPAN=AUDIT/'p2_author_lifespan_safe_v1.csv'
WORK_AUTHOR=AUDIT/'p2_work_author_key_safe_v1.csv'
WIKIPEDIA_WIKIDATA=AUDIT/'p2_wikipedia_wikidata_safe_v1.csv'
REPORT=AUDIT/'T_AXIS_COMPLETION_P2_TONLY_V1.md'
MARKER=AUDIT/'APPLY_T_AXIS_COMPLETION_P2_TONLY_V1'
T_LABELS={
'T0':'T0 文学源头与古代文学','T1':'T1 中古多中心文学世界','T2':'T2 早期现代文学',
'T3':'T3 19世纪现代文学体系','T4':'T4 全球现代主义时代','T5':'T5 二战后多极文学','T6':'T6 当代全球文学'}

def fm_span(text:str):
    m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
    if not m: raise ValueError('missing frontmatter')
    return m

def scalar(fm:str,key:str)->str:
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',fm)
    return m.group(1).strip().strip('"\'') if m else ''

def replace_axis_t(fm:str,label:str)->str:
    lines=fm.splitlines();out=[];i=0;done=False
    while i<len(lines):
        if re.match(r'^axis_t:\s*',lines[i]):
            out.extend(['axis_t:',f'- {label}']);done=True;i+=1
            while i<len(lines) and re.match(r'^\s*-\s*',lines[i]): i+=1
            continue
        out.append(lines[i]);i+=1
    if not done: out.extend(['axis_t:',f'- {label}'])
    return '\n'.join(out)

def load_candidates():
    by_key={}; conflicts=[]; conflict_keys=set(); sources=[]
    specs=[
        (AUTHOR_ONLY,'author_only_status','SAFE_T_AUTHOR_RANGE','author_only_proven_t','author_only'),
        (LIFESPAN,'lifespan_status','SAFE_T_LIFESPAN_RANGE','lifespan_proven_t','lifespan_crosscheck'),
        (WORK_AUTHOR,'work_author_key_status','SAFE_T_DIRECT_WORK_AUTHOR','proven_t','direct_work_author'),
        (WIKIPEDIA_WIKIDATA,'ww_status','SAFE_T_WORK_P577','ww_proven_t','wikipedia_wikidata_p577'),
    ]
    for path,status_key,status_value,t_key,src in specs:
        if not path.exists(): continue
        with path.open(encoding='utf-8-sig',newline='') as f:
            for r in csv.DictReader(f):
                if r.get(status_key)==status_value:
                    sources.append((r,r.get(t_key,''),src))
    for r,t,src in sources:
        key=(r.get('id',''),r.get('file',''))
        if key in conflict_keys or t not in T_LABELS: continue
        if key in by_key and by_key[key]['t']!=t:
            conflicts.append((key,by_key[key]['t'],t));by_key.pop(key,None);conflict_keys.add(key);continue
        if key not in by_key: by_key[key]={'row':r,'t':t,'sources':[src]}
        elif src not in by_key[key]['sources']: by_key[key]['sources'].append(src)
    return list(by_key.values()),conflicts

def main():
    if not MARKER.exists(): raise SystemExit('authorization marker missing')
    rows,conflicts=load_candidates()
    if not rows and not conflicts: raise SystemExit('no safe evidence CSV available')
    applied=[];skipped=[]
    for item in rows:
        r=item['row']; t=item['t']; evidence='+'.join(item['sources'])
        fn=r.get('file',''); tid=r.get('id',''); p=WORKS/fn
        if not p.exists(): skipped.append((fn,'file missing')); continue
        text=p.read_text(encoding='utf-8');m=fm_span(text);fm=m.group(1)
        if scalar(fm,'id')!=tid: skipped.append((fn,'id mismatch')); continue
        if re.search(r'(?m)^axis_t:\s*\n\s*-\s*T[0-6]\b',fm): skipped.append((fn,'already has T')); continue
        fm=replace_axis_t(fm,T_LABELS[t]);p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
        applied.append((fn,tid,t,evidence))
    lines=['# T-axis Completion P2 T-only V1','',f'- Safe unique candidates available: **{len(rows)}**',f'- Evidence conflicts blocked: **{len(conflicts)}**',f'- Works applied: **{len(applied)}**',f'- Skipped: **{len(skipped)}**','', '- Mutated field: `axis_t` only.','- `year` intentionally remains unchanged/null when no exact work-level year is verified.','- R/M/G/Q/topics/priority/history/mechanism unchanged.','','## Applied','']
    for fn,tid,t,evidence in applied: lines.append(f'- `{fn}` | `{tid}` | {t} | evidence={evidence}')
    if conflicts:
        lines += ['','## Blocked evidence conflicts','']
        for (tid,fn),a,b in conflicts: lines.append(f'- `{fn}` | `{tid}` | {a} vs {b}')
    if skipped:
        lines += ['','## Skipped','']
        for fn,why in skipped: lines.append(f'- `{fn}` — {why}')
    lines += ['','`T_AXIS_COMPLETION_P2_TONLY_V1 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink()
    print(f'candidates={len(rows)} conflicts={len(conflicts)} applied={len(applied)} skipped={len(skipped)}')

if __name__=='__main__': main()
