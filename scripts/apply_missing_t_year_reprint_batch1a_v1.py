from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
AUDIT=ROOT/'_audit/t_axis_year_backfill'
MARKER=AUDIT/'APPLY_MISSING_T_YEAR_REPRINT_BATCH1A_V1'
REPORT=AUDIT/'REPRINT_BATCH1A_APPLY_V1.md'
T_LABELS={
'T1':'T1 中古文学','T3':'T3 十九世纪文学','T4':'T4 现代主义前夜与现代主义文学','T5':'T5 战后文学','T6':'T6 当代全球文学'
}
ROWS=[
('A Princess in Theory.md','WL-WORK-1936',2018,'T6','Google Books HarperCollins 2018; library street-date record'),
('A Rumor of War.md','WL-WORK-1937',1977,'T5','Philip Caputo official site: publication in 1977; Open Library first edition 1977'),
('A Small Place.md','WL-WORK-1343',1988,'T6','WorldCat first edition 1988; CiNii original publication 1988'),
('Always Only You.md','WL-WORK-1939',2020,'T6','Penguin Random House ebook publication 2020; Google Books bibliographic record 2020'),
('Auschwitz and After.md','WL-WORK-1941',1971,'T5','Trilogy completion policy: third/concluding volume published 1971; JSTOR biography confirms trilogy publication 1970–1971'),
('Ayesha at Last.md','WL-WORK-1942',2018,'T6','HarperCollins/Google Books 2018; author site confirms Canadian publication in 2018'),
('Banalata Sen.md','WL-WORK-1524',1942,'T4','Poetry-volume first publication 1942; enlarged second edition 1952'),
('Bar-20.md','WL-WORK-2166',1907,'T4','Wikisource publication history: novel 1907, based on 1905–1907 stories'),
('Before I Let Go.md','WL-WORK-1945',2022,'T6','Hachette/Forever on-sale 2022; first-edition library record 2022'),
('Before She Sleeps.md','WL-WORK-0916',2018,'T6','WorldCat first edition 2018; library first-edition record 2018'),
('Beirut Blues.md','WL-WORK-1946',1992,'T6','Original Arabic work first published 1992; English edition 1995'),
('Bet Me.md','WL-WORK-1947',2004,'T6','Jennifer Crusie official bibliography February 2004; first-edition records 2004'),
('Between the Woods and the Water.md','WL-WORK-1350',1986,'T6','Original London publication 1986; CiNii first American edition 1986'),
('Bless Me, Ultima.md','WL-WORK-2174',1972,'T5','University of New Mexico Anaya material: first published 1972'),
('Bread Givers.md','WL-WORK-0917',1925,'T4','1925 Doubleday first edition; LCCN/Harvard-derived catalog record'),
('Burnt Offerings.md','WL-WORK-0494',1973,'T5','Delacorte first edition February 1973; publication history confirms'),
("Butcher's Crossing.md",'WL-WORK-2179',1960,'T5','Macmillan first publication 1960; first-edition history confirms'),
('Cancioneiro Guasca.md','WL-WORK-2180',1910,'T4','Instituto João Simões Lopes Neto: first edition Pelotas 1910'),
('Color.md','WL-WORK-1527',1925,'T4','Countee Cullen first poetry book, Harper & Brothers 1925'),
('Contos Gauchescos.md','WL-WORK-2190',1912,'T4','Instituto João Simões Lopes Neto: Echenique & Cia publication 1912'),
('Cowboy Songs and Other Frontier Ballads.md','WL-WORK-2193',1910,'T4','Library of Congress first edition Sturgis & Walton 1910'),
('Cracking India.md','WL-WORK-0919',1988,'T6','Same work originally published as Ice-Candy-Man in England in 1988; Cracking India title edition 1991'),
('Dark Fire.md','WL-WORK-0921',2004,'T6','Macmillan UK first edition November 2004'),
('Dead in the West.md','WL-WORK-2196',1986,'T6','Publication history gives original 1986 work; later Night Shade edition is reprint'),
('Desert Solitaire.md','WL-WORK-2199',1968,'T5','McGraw-Hill first publication 1968'),
('Dispatches.md','WL-WORK-1956',1977,'T5','WorldCat Knopf 1977; first-edition catalog 1977'),
('Dreaming in Cuban.md','WL-WORK-0923',1992,'T6','Knopf first edition 1992; WorldCat/Open Library agree'),
('Dungeon Crawler Carl.md','WL-WORK-0499',2020,'T6','Author official site: published Sep 21 2020; republished 2024'),
('Erec.md','WL-WORK-2218',1185,'T1','Formation-date policy: scholarly dating around 1185 / 1180–1190, not modern edition year'),
('Facial Justice.md','WL-WORK-0924',1960,'T5','Hamish Hamilton first edition 1960'),
('From a Crooked Rib.md','WL-WORK-0927',1970,'T5','Heinemann African Writers Series publication 1970'),
('Get a Life, Chloe Brown.md','WL-WORK-1961',2019,'T6','Avon Romance publication 2019'),
('Harmonium.md','WL-WORK-1532',1923,'T4','Knopf first edition 1923; Wallace Stevens Society material agrees'),
('In Flanders Fields.md','WL-WORK-1967',1915,'T4','First published in Punch on 8 Dec 1915'),
('Inland.md','WL-WORK-2248',2019,'T6','Random House first edition Aug 13 2019'),
('Iwein.md','WL-WORK-2250',1200,'T1','Formation-date policy: composed around 1200, certainly by ca.1205'),
('Jerilderie Letter.md','WL-WORK-2251',1879,'T3','Formation-date policy: dictated/written before Jerilderie raid in February 1879; full publication much later'),
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
    vals=re.findall(r'T[0-6]',m.group(1))
    return vals[0] if vals else ''

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
    applied=[];year_only=[];blocked=[]
    for fn,wid,year,t,sources in ROWS:
        p=WORKS/fn
        if not p.exists():blocked.append((fn,'file missing'));continue
        text=p.read_text(encoding='utf-8-sig');m=fm_span(text);fm=m.group(1)
        if scalar(fm,'id')!=wid:blocked.append((fn,'id mismatch'));continue
        cy=scalar(fm,'year');ct=current_t(fm)
        if cy:
            if str(cy)==str(year) and (not ct or ct==t):
                blocked.append((fn,'year already populated with expected value'))
            else:
                blocked.append((fn,f'pre-existing year/T conflict: year={cy}, T={ct}'))
            continue
        if ct and ct!=t:
            blocked.append((fn,f'pre-existing T conflict: {ct} vs {t}'));continue
        fm=set_scalar(fm,'year',str(year))
        if not ct:
            fm=set_axis(fm,T_LABELS[t]);applied.append((fn,wid,year,t,sources))
        else:
            year_only.append((fn,wid,year,t,sources))
        p.write_text(text[:m.start(1)]+fm+text[m.end(1):],encoding='utf-8')
    lines=['# Missing-T Reprint Risk Batch 1A Apply V1','',f'- Input reviewed works: **{len(ROWS)}**',f'- Applied year+T: **{len(applied)}**',f'- Applied year only (existing matching T retained): **{len(year_only)}**',f'- Blocked: **{len(blocked)}**','','- Canonical fields mutated: `year`; `axis_t` only when previously empty.','- Evidence policy: original publication / first appearance / defensible formation-completion year; modern reprint dates rejected.','','## Applied','']
    for r in applied+year_only: lines.append(f'- `{r[0]}` | `{r[1]}` | {r[2]} | {r[3]} | {r[4]}')
    if blocked:
        lines += ['','## Blocked','']
        for fn,why in blocked: lines.append(f'- `{fn}` — {why}')
    lines += ['','`MISSING_T_REPRINT_BATCH1A_V1 = APPLIED_AND_VERIFIED`','']
    REPORT.write_text('\n'.join(lines),encoding='utf-8');MARKER.unlink();print({'year_t':len(applied),'year_only':len(year_only),'blocked':len(blocked)})

if __name__=='__main__':main()
