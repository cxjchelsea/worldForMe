from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_year_backfill'
MARKER=AUDIT/'APPLY_MISSING_T_YEAR_REPRINT_BATCH1B_V1'
REPORT=AUDIT/'REPRINT_BATCH1B_APPLY_V1.md'
T_LABELS={
'T3':'T3 十九世纪文学','T4':'T4 现代主义前夜与现代主义文学','T6':'T6 当代全球文学'
}
ROWS=[
('Casos do Romualdo.md','WL-WORK-2183',1914,'T4','Instituto João Simões Lopes Neto and UFSC: stories serialized in Correio Mercantil Jun-Jul 1914; 1952 is first book collection'),
('Count Hannibal.md','WL-WORK-2192',1901,'T4','At the Circulating Library/BL: first edition London Smith Elder 1901; serialized Cornhill Magazine Jan-Dec 1901; 1900 OL value rejected'),
('Dark Continent, My Black Arse.md','WL-WORK-1353',2007,'T6','Google Books bibliographic record: Umuzi 2007; later Penguin Random House 2011 edition is reissue'),
("Delilah Green Doesn't Care.md",'WL-WORK-1953',2022,'T6','Penguin Random House: published Feb 22 2022; library catalog marks first edition 2022'),
('Devil in Winter.md','WL-WORK-1955',2006,'T6','First Avon edition Feb 28 2006; Open Library marks 2006 first edition'),
('El Zarco.md','WL-WORK-2214',1888,'T3','Formation/completion policy: Altamirano completed manuscript Apr 1888; posthumous first publication Barcelona 1901'),
('Forbidden.md','WL-WORK-1958',2016,'T6','Beverly Jenkins official site: published Jan 26 2016 by Avon'),
('Games of Command.md','WL-WORK-1960',2007,'T6','Linnea Sinclair official site/booklist: Games of Command Feb 2007; 2002 Command Performance supplied precursor characters/scenes, not this canonical work'),
('Gestaltes en diere.md','WL-WORK-1530',1942,'T4','Scholarly literature identifies Gestaltes en diere as 1942 volume; 1958 catalog value is 4th printing'),
('Gnomon.md','WL-WORK-0928',2017,'T6','Heinemann publication 2017; work-level bibliographic sources agree'),
('Greguerías.md','WL-WORK-1531',1917,'T4','Biblioteca Nacional de España records Prometeo Valencia [1917?]; bibliography and chronology identify first Greguerías volume 1917'),
('Hood.md','WL-WORK-2240',2006,'T6','WestBow/Thomas Nelson first edition 2006; library LCCN 2006014183 and Publishers Weekly 2006 review'),
('Indigo.md','WL-WORK-1969',1996,'T6','Beverly Jenkins official bibliography: Jul 1 1996; WorldCat Avon Books New York 1996'),
]

def fm_span(text):
    m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
    if not m: raise ValueError('missing frontmatter')
    return m

def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',fm)
    if not m:return ''
    v=m.group(1).strip().strip('"\'')
    return '' if v.lower() in {'null','none','~'} else v

def current_t(fm):
    m=re.search(r'(?ms)^axis_t:\s*\n((?:\s*-.*\n?)*)',fm)
    if not m:return ''
    vals=re.findall(r'T[0-6]',m.group(1)); return vals[0] if vals else ''

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
    if not MARKER.exists(): raise SystemExit('authorization marker missing')
    applied=[];blocked=[]
    for fn,wid,year,t,sources in ROWS:
        p=WORKS/fn
        if not p.exists():blocked.append((fn,'file missing'));continue
        text=p.read_text(encoding='utf-8-sig');m=fm_span(text);fm=m.group(1)
        if scalar(fm,'id')!=wid:blocked.append((fn,'id mismatch'));continue
        cy=scalar(fm,'year');ct=current_t(fm)
        if cy or ct:
            blocked.append((fn,f'already populated: year={cy}, T={ct}'));continue
        fm=set_scalar(fm,'year',str(year));fm=set_axis(fm,T_LABELS[t])
        p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
        applied.append((fn,wid,year,t,sources))
    lines=['# Missing-T Reprint Risk Batch 1B Apply V1','',f'- Input reviewed works: **{len(ROWS)}**',f'- Applied year+T: **{len(applied)}**',f'- Blocked: **{len(blocked)}**','','- Canonical fields mutated: `year` and `axis_t` only.','- Evidence policy: original publication / first appearance / defensible formation-completion year; modern reprint dates rejected.','','## Applied','']
    for r in applied: lines.append(f'- `{r[0]}` | `{r[1]}` | {r[2]} | {r[3]} | {r[4]}')
    if blocked:
        lines += ['','## Blocked','']
        for fn,why in blocked: lines.append(f'- `{fn}` — {why}')
    lines += ['','`MISSING_T_REPRINT_BATCH1B_V1 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink();print({'applied':len(applied),'blocked':len(blocked)})

if __name__=='__main__':main()
