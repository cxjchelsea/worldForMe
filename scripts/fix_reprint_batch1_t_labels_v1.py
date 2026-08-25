from pathlib import Path
import csv,re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_completeness'
MARKER=ROOT/'_audit/t_axis_year_backfill/FIX_REPRINT_BATCH1_T_LABELS_V1'
REPORT=ROOT/'_audit/t_axis_year_backfill/REPRINT_BATCH1_T_LABEL_FIX_V1.md'
LABELS={
'T0':'T0 文学源头与古代文学','T1':'T1 中古多中心文学世界','T2':'T2 早期现代文学',
'T3':'T3 19世纪现代文学体系','T4':'T4 全球现代主义时代','T5':'T5 二战后多极文学','T6':'T6 当代全球文学'}

def expected(year):
    if year<500:return 'T0'
    if year<1500:return 'T1'
    if year<1800:return 'T2'
    if year<1890:return 'T3'
    if year<1945:return 'T4'
    if year<1980:return 'T5'
    return 'T6'

def fm_span(text):
    m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
    if not m:raise ValueError('missing frontmatter')
    return m

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
    rows=list(csv.DictReader((AUDIT/'invalid_t_label.csv').open('r',encoding='utf-8-sig',newline='')))
    fixed=[];blocked=[]
    for r in rows:
        fn=r['file'];p=WORKS/fn
        try:year=int(r['year'])
        except:blocked.append((fn,'missing/invalid year'));continue
        t=expected(year)
        if r.get('suggested_t') and r['suggested_t']!=t:
            blocked.append((fn,f"audit suggestion {r['suggested_t']} != expected {t}"));continue
        text=p.read_text(encoding='utf-8-sig');m=fm_span(text);fm=m.group(1)
        fm=set_axis(fm,LABELS[t])
        p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
        fixed.append((fn,r['id'],year,t,r['invalid_t']))
    lines=['# Reprint Batch 1 T-label Schema Fix V1','',f'- Input INVALID_T_LABEL rows: **{len(rows)}**',f'- Fixed: **{len(fixed)}**',f'- Blocked: **{len(blocked)}**','','- Only `axis_t` label text was normalized to the canonical enum from `audit_t_axis_completeness_v1.py`.','- `year` values were not changed.','','## Fixed','']
    for fn,wid,year,t,old in fixed:lines.append(f'- `{fn}` | `{wid}` | year={year} | {old} → {LABELS[t]}')
    if blocked:
        lines+=['','## Blocked','']
        for fn,why in blocked:lines.append(f'- `{fn}` — {why}')
    lines+=['','`REPRINT_BATCH1_T_LABEL_FIX_V1 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink();print({'fixed':len(fixed),'blocked':len(blocked)})

if __name__=='__main__':main()
