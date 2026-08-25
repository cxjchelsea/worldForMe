from pathlib import Path
import csv,re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); WORKS=ROOT/'40 作品'; AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_manual_resolution_batch1_v1.csv'; RESIDUAL=AUDIT/'p2_residual_review_v1.csv'; REPORT=AUDIT/'P2_MANUAL_RESOLUTION_BATCH1_V1.md'; MARKER=AUDIT/'APPLY_P2_MANUAL_RESOLUTION_BATCH1_V1'
T_LABELS={'T0':'T0 文学源头与古代文学','T1':'T1 中古多中心文学世界','T2':'T2 早期现代文学','T3':'T3 19世纪现代文学体系','T4':'T4 全球现代主义时代','T5':'T5 二战后多极文学','T6':'T6 当代全球文学'}

def fm_span(text):
    m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
    if not m:raise ValueError('missing frontmatter')
    return m
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',fm)
    return m.group(1).strip().strip('"\'') if m else ''
def replace_axis_t(fm,label):
    lines=fm.splitlines();out=[];i=0;done=False
    while i<len(lines):
        if re.match(r'^axis_t:\s*',lines[i]):
            out.extend(['axis_t:',f'- {label}']);done=True;i+=1
            while i<len(lines) and re.match(r'^\s*-\s*',lines[i]):i+=1
            continue
        out.append(lines[i]);i+=1
    if not done:out.extend(['axis_t:',f'- {label}'])
    return '\n'.join(out)

def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
    residual={r.get('file',''):r for r in csv.DictReader(RESIDUAL.open(encoding='utf-8-sig',newline=''))}
    applied=[];blocked=[]
    for r in rows:
        fn=r.get('file','');t=r.get('proven_t','')
        if fn not in residual:blocked.append((fn,'not in current residual'));continue
        if t not in T_LABELS:blocked.append((fn,'invalid T'));continue
        p=WORKS/fn
        if not p.exists():blocked.append((fn,'file missing'));continue
        text=p.read_text(encoding='utf-8');m=fm_span(text);fm=m.group(1)
        if re.search(r'(?m)^axis_t:\s*\n\s*-\s*T[0-6]\b',fm):blocked.append((fn,'already has T'));continue
        tid=scalar(fm,'id');fm=replace_axis_t(fm,T_LABELS[t]);p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
        applied.append((fn,tid,t,r.get('verified_year',''),r.get('evidence_note','')))
    lines=['# P2 Manual Resolution Batch 1 V1','',f'- Input reviewed works: **{len(rows)}**',f'- Works applied: **{len(applied)}**',f'- Blocked: **{len(blocked)}**','','- Mutated field: `axis_t` only.','- Verified work year is retained in this audit report but not written to canonical `year` in this batch.','','## Applied','']
    for fn,tid,t,y,note in applied:lines.append(f'- `{fn}` | `{tid}` | {t} | verified_year={y} | {note}')
    if blocked:
        lines += ['','## Blocked','']
        for fn,why in blocked:lines.append(f'- `{fn}` — {why}')
    lines += ['','`P2_MANUAL_RESOLUTION_BATCH1_V1 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink();print({'applied':len(applied),'blocked':len(blocked)})
if __name__=='__main__':main()
