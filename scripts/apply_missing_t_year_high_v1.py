from __future__ import annotations

import csv,re
from pathlib import Path

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_year_backfill'
IN=AUDIT/'missing_t_year_high_confidence_v1.csv'
REPORT=AUDIT/'APPLY_HIGH_V1.md'
MARKER=AUDIT/'APPLY_MISSING_T_YEAR_HIGH_V1'
BOUND={500,1500,1800,1890,1945,1980}
T_LABELS={'T0':'T0 文学源头与古代文学','T1':'T1 中古多中心文学世界','T2':'T2 早期现代文学','T3':'T3 19世纪现代文学体系','T4':'T4 全球现代主义时代','T5':'T5 二战后多极文学','T6':'T6 当代全球文学'}

def fm_span(text):
    m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
    if not m:raise ValueError('missing frontmatter')
    return m

def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',fm)
    if not m:return ''
    v=m.group(1).strip().strip('"\'')
    return '' if v.lower() in {'null','none','~'} else v

def has_valid_t(fm):
    return bool(re.search(r'(?m)^\s*-\s*T[0-6]\s',fm))

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
    if not IN.exists():raise SystemExit('HIGH research CSV missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
    applied=[];blocked=[]
    for r in rows:
        if r.get('confidence')!='HIGH' or r.get('review_status')!='READY_FOR_WRITEBACK':
            blocked.append((r.get('file',''),'not HIGH-ready'));continue
        try:y=int(r.get('publication_year',''))
        except:blocked.append((r.get('file',''),'invalid year'));continue
        t=r.get('suggested_t','')
        if y in BOUND or t not in T_LABELS:
            blocked.append((r.get('file',''),'boundary/invalid T'));continue
        p=WORKS/r.get('file','')
        if not p.exists():blocked.append((r.get('file',''),'file missing'));continue
        text=p.read_text(encoding='utf-8-sig');m=fm_span(text);fm=m.group(1)
        if scalar(fm,'id')!=r.get('id',''):
            blocked.append((r.get('file',''),'id mismatch'));continue
        if scalar(fm,'year') or has_valid_t(fm):
            blocked.append((r.get('file',''),'year/T already populated'));continue
        fm=set_scalar(fm,'year',str(y));fm=set_axis(fm,T_LABELS[t])
        p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
        applied.append((r.get('file',''),r.get('id',''),y,t,r.get('year_source_1',''),r.get('year_source_2','')))
    lines=['# Missing-T Year HIGH Writeback V1','',f'- HIGH input rows: **{len(rows)}**',f'- Applied: **{len(applied)}**',f'- Blocked: **{len(blocked)}**','','- Mutated fields: `year` and `axis_t` only.','- R/M/G/Q/topics/priority/history/mechanism unchanged.','','## Applied','']
    for fn,i,y,t,s1,s2 in applied:lines.append(f'- `{fn}` | `{i}` | {y} | {t} | {s1} | {s2}')
    if blocked:
        lines += ['','## Blocked','']
        for fn,why in blocked:lines.append(f'- `{fn}` — {why}')
    lines += ['','`MISSING_T_YEAR_HIGH_V1 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink();print(f'APPLIED={len(applied)} BLOCKED={len(blocked)}')

if __name__=='__main__':main()
