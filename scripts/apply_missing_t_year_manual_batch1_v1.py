from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_year_backfill'
MARKER=AUDIT/'APPLY_MISSING_T_YEAR_MANUAL_BATCH1_V1'
REPORT=AUDIT/'MANUAL_BATCH1_V1.md'
T_LABELS={'T6':'T6 当代全球文学'}
ROWS=[
    {'file':'A Head Full of Ghosts.md','id':'WL-WORK-0489','year':2015,'t':'T6','sources':'Google Books; Chappaqua Library first-edition catalog; Wikidata Q24521290'},
    {'file':'A Hunger Like No Other.md','id':'WL-WORK-1934','year':2006,'t':'T6','sources':'Kresley Cole official printable booklist; WorldCat OCLC 65188335; Wikidata Q20668221'},
]

def fm_span(text):
    m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
    if not m:raise ValueError('missing frontmatter')
    return m

def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',fm)
    if not m:return ''
    v=m.group(1).strip().strip('"\'')
    return '' if v.lower() in {'null','none','~'} else v

def set_scalar(fm,key,value):
    pat=rf'(?m)^{re.escape(key)}:\s*.*$'
    if re.search(pat,fm):return re.sub(pat,f'{key}: {value}',fm,count=1)
    return fm+f'\n{key}: {value}'

def set_axis(fm,label):
    lines=fm.splitlines();out=[];i=0;done=False
    while i<len(lines):
        if re.match(r'^axis_t:\s*',lines[i]):
            out += ['axis_t:',f'- {label}'];done=True;i+=1
            while i<len(lines) and re.match(r'^\s*-\s*',lines[i]):i+=1
            continue
        out.append(lines[i]);i+=1
    if not done:out += ['axis_t:',f'- {label}']
    return '\n'.join(out)

def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    applied=[];blocked=[]
    for r in ROWS:
        p=WORKS/r['file']
        if not p.exists():blocked.append((r['file'],'file missing'));continue
        text=p.read_text(encoding='utf-8-sig');m=fm_span(text);fm=m.group(1)
        if scalar(fm,'id')!=r['id']:blocked.append((r['file'],'id mismatch'));continue
        if scalar(fm,'year') or re.search(r'(?m)^\s*-\s*T[0-6]\s',fm):blocked.append((r['file'],'already populated'));continue
        fm=set_scalar(fm,'year',str(r['year']));fm=set_axis(fm,T_LABELS[r['t']])
        p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
        applied.append(r)
    lines=['# Missing-T Year Manual Batch 1 V1','',f'- Input: **{len(ROWS)}**',f'- Applied: **{len(applied)}**',f'- Blocked: **{len(blocked)}**','','- Mutated fields: `year` and `axis_t` only.','', '## Applied','']
    for r in applied:lines.append(f"- `{r['file']}` | `{r['id']}` | {r['year']} | {r['t']} | {r['sources']}")
    if blocked:
        lines += ['','## Blocked','']
        for fn,why in blocked:lines.append(f'- `{fn}` — {why}')
    lines += ['','`MISSING_T_YEAR_MANUAL_BATCH1_V1 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink();print(f'APPLIED={len(applied)} BLOCKED={len(blocked)}')

if __name__=='__main__':main()
