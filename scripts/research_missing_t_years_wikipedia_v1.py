from __future__ import annotations

import csv,json,re,unicodedata,urllib.parse,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
from difflib import SequenceMatcher
from pathlib import Path

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
AUDIT=ROOT/'_audit/t_axis_year_backfill'
IN=AUDIT/'missing_t_year_backfill_v1.csv'
OUT=AUDIT/'missing_t_year_wikipedia_v1.csv'
SAFE=AUDIT/'missing_t_year_wikipedia_safe_v1.csv'
REPORT=AUDIT/'WIKIPEDIA_RESEARCH_V1.md'
MARKER=AUDIT/'RUN_MISSING_T_YEAR_WIKIPEDIA_V1'
UA={'User-Agent':'worldForMe-literature-audit/1.0'}
BOUND={500,1500,1800,1890,1945,1980}

def norm(s):
    s=unicodedata.normalize('NFKD',str(s or '')).casefold()
    return ''.join(c for c in s if c.isalnum())
def sim(a,b):
    a,b=norm(a),norm(b)
    if not a or not b:return 0.0
    return 1.0 if a==b else SequenceMatcher(None,a,b).ratio()
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=12) as r:return json.loads(r.read().decode('utf-8'))
def t_of(y):
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'
def strip_markup(s):
    s=re.sub(r'<ref[^>]*>.*?</ref>',' ',s,flags=re.S|re.I)
    s=re.sub(r'\{\{[^{}]*\}\}',' ',s)
    s=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]+)\]\]',r'\1',s)
    s=re.sub(r'<[^>]+>',' ',s)
    return re.sub(r'\s+',' ',s).strip()
def field(wikitext,names):
    for name in names:
        m=re.search(rf'(?im)^\s*\|\s*{re.escape(name)}\s*=\s*(.+)$',wikitext)
        if m:return m.group(1).strip()
    return ''
def page_candidates(title):
    q=urllib.parse.urlencode({'action':'query','format':'json','list':'search','srsearch':f'intitle:"{title}"','srlimit':5})
    try:d=get('https://en.wikipedia.org/w/api.php?'+q)
    except:return []
    return [(x.get('title',''),x.get('pageid')) for x in d.get('query',{}).get('search',[]) if x.get('pageid')]
def wikitext(pageid):
    q=urllib.parse.urlencode({'action':'query','format':'json','pageids':str(pageid),'prop':'revisions','rvprop':'content','rvslots':'main','formatversion':'2'})
    d=get('https://en.wikipedia.org/w/api.php?'+q)
    pages=d.get('query',{}).get('pages',[])
    if not pages:return ''
    revs=pages[0].get('revisions',[])
    if not revs:return ''
    return (((revs[0].get('slots') or {}).get('main') or {}).get('content') or '')
def research(r):
    title=r.get('title_original') or r.get('title') or ''
    author=r.get('author_original') or r.get('author') or ''
    rr=dict(r);rr.update({'wiki_status':'REVIEW','wiki_page':'','wiki_title_score':'','wiki_author_field':'','wiki_author_score':'','wiki_year':'','wiki_date_field':''})
    if not title or not author or '/' in author or author in {'佚名','匿名','民间','口传传统'}:return rr
    best=None
    for pt,pid in page_candidates(title):
        ts=sim(title,pt)
        if ts<0.86:continue
        try:wt=wikitext(pid)
        except:continue
        af=strip_markup(field(wt,['author','authors','writer','written_by']))
        if not af:continue
        ascore=sim(author,af)
        if ascore<0.82:continue
        df=strip_markup(field(wt,['published','publication_date','pub_date','release_date','first_published']))
        if not df:continue
        years=[int(x) for x in re.findall(r'(?<!\d)(1[5-9]\d{2}|20\d{2})(?!\d)',df)]
        if not years:continue
        y=min(years)
        score=ts+ascore
        cand=(score,y,pt,ts,af,ascore,df)
        if best is None or cand[0]>best[0]:best=cand
    if not best:return rr
    _,y,pt,ts,af,ascore,df=best
    rr.update({'wiki_status':'WORK_PAGE_YEAR','wiki_page':pt,'wiki_title_score':f'{ts:.3f}','wiki_author_field':af,'wiki_author_score':f'{ascore:.3f}','wiki_year':str(y),'wiki_date_field':df,'suggested_t':t_of(y)})
    return rr

def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
    out=[]
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs={ex.submit(research,r):r for r in rows}
        for i,f in enumerate(as_completed(futs),1):
            try:out.append(f.result())
            except:out.append(dict(futs[f],wiki_status='ERROR'))
            if i%50==0:print(i,flush=True)
    order={r.get('id'):i for i,r in enumerate(rows)};out.sort(key=lambda r:order.get(r.get('id'),10**9))
    # Cross-check against OL candidate from existing research if present; safe when wiki+OL exact/1y same T, or wiki page strong + no contradictory OL.
    research_map={}
    rp=AUDIT/'missing_t_year_research_v1.csv'
    if rp.exists():
        for r in csv.DictReader(rp.open(encoding='utf-8-sig',newline='')):research_map[r.get('id')]=r
    safe=[]
    for r in out:
        if r.get('wiki_status')!='WORK_PAGE_YEAR':continue
        base=research_map.get(r.get('id'),{})
        try:wy=int(r.get('wiki_year',''))
        except:continue
        try:oy=int(base.get('ol_year','')) if base.get('ol_year') else None
        except:oy=None
        if wy in BOUND:continue
        reason=''
        if oy is not None:
            if t_of(oy)!=t_of(wy):continue
            if abs(oy-wy)>1:continue
            reason='WIKIPEDIA_WORKPAGE_PLUS_OL_EXACT_OR_1Y'
        else:
            # Single-source work-page evidence remains MEDIUM, not safe for canonical year.
            continue
        x=dict(r);x.update({'publication_year':str(min(wy,oy)),'confidence':'HIGH','review_status':'READY_FOR_WRITEBACK','year_source_1':'Wikipedia:'+r.get('wiki_page',''),'year_source_2':'OpenLibrary:'+base.get('ol_key',''),'source_agreement':reason,'suggested_t':t_of(wy)})
        safe.append(x)
    fields=[]
    for r in out+safe:
        for k in r:
            if k not in fields:fields.append(k)
    for p,data in [(OUT,out),(SAFE,safe)]:
        with p.open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
    REPORT.write_text('# Missing-T Wikipedia Work-page Research V1\n\n'+f'- Input: **{len(rows)}**\n- Work pages with strong title+author+date: **{sum(1 for r in out if r.get("wiki_status")=="WORK_PAGE_YEAR")}**\n- HIGH after Open Library cross-check: **{len(safe)}**\n\nNo Work file was modified.\n\n`MISSING_T_WIKIPEDIA_RESEARCH_V1 = COMPLETE_READ_ONLY`\n',encoding='utf-8')
    MARKER.unlink();print({'safe':len(safe)},flush=True)

if __name__=='__main__':main()
