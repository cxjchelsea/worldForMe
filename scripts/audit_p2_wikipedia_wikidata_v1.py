from pathlib import Path
import csv,json,re,time,unicodedata,urllib.parse,urllib.request
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor,as_completed

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_residual_review_v1.csv'; SAFE=AUDIT/'p2_wikipedia_wikidata_safe_v1.csv'; REVIEW=AUDIT/'p2_wikipedia_wikidata_review_v1.csv'; REPORT=AUDIT/'P2_WIKIPEDIA_WIKIDATA_V1.md'; MARKER=AUDIT/'RUN_P2_WIKIPEDIA_WIKIDATA_V1'
UA={'User-Agent':'worldForMe-literature-audit/1.0 (bibliographic verification)'}
YEAR_RE=re.compile(r'([12][0-9]{3})')
BOUND={500,1500,1800,1890,1945,1980}

def t_of(y):
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'

def norm(s):
    s=unicodedata.normalize('NFKD',str(s or '')).casefold();return ''.join(c for c in s if c.isalnum())
def sim(a,b):
    a,b=norm(a),norm(b)
    if not a or not b:return 0.0
    return 1.0 if a==b else SequenceMatcher(None,a,b).ratio()
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=12) as r:return json.loads(r.read().decode('utf-8'))
def entity(qid):return get(f'https://www.wikidata.org/wiki/Special:EntityData/{qid}.json')['entities'][qid]
def names(e):
    vals=[]
    for obj in (e.get('labels') or {}).values(): vals.append(obj.get('value',''))
    for arr in (e.get('aliases') or {}).values(): vals += [x.get('value','') for x in arr]
    return [x for x in vals if x]
def p577_years(e):
    out=[]
    for c in (e.get('claims') or {}).get('P577',[]):
        v=((c.get('mainsnak') or {}).get('datavalue') or {}).get('value')
        if isinstance(v,dict):
            m=YEAR_RE.search(str(v.get('time','')))
            if m:out.append(int(m.group(1)))
    return sorted(set(out))
def p50(e):
    out=[]
    for c in (e.get('claims') or {}).get('P50',[]):
        v=((c.get('mainsnak') or {}).get('datavalue') or {}).get('value')
        if isinstance(v,dict) and v.get('id'):out.append(v['id'])
    return out

def verify(r):
    title=r.get('title_original') or r.get('title') or ''
    author=r.get('author_original') or r.get('author') or ''
    try:
        q=urllib.parse.urlencode({'action':'query','format':'json','generator':'search','gsrsearch':f'intitle:"{title}"','gsrlimit':4,'prop':'pageprops','ppprop':'wikibase_item','redirects':1})
        data=get('https://en.wikipedia.org/w/api.php?'+q)
    except Exception as e:return dict(r,ww_status='API_ERROR',ww_error=type(e).__name__)
    best=None
    for p in (data.get('query') or {}).get('pages',{}).values():
        qid=(p.get('pageprops') or {}).get('wikibase_item');pt=p.get('title','')
        ts=sim(title,pt)
        if not qid or ts<0.86:continue
        try:e=entity(qid)
        except Exception:continue
        # Entity title/aliases must also match strongly.
        ets=max([sim(title,n) for n in names(e)] or [0])
        if max(ts,ets)<0.92:continue
        years=p577_years(e); authors=p50(e)
        if not years or not authors:continue
        author_score=0.0;matched_author=''
        for aq in authors[:4]:
            try:ae=entity(aq)
            except Exception:continue
            for n in names(ae):
                s=sim(author,n)
                if s>author_score:author_score=s;matched_author=n
        if author_score<0.88:continue
        # Prefer earliest work-level P577; block operational boundary years.
        y=min(years)
        if y in BOUND:continue
        score=max(ts,ets)+author_score
        cand=(score,y,qid,pt,matched_author,author_score,years)
        if best is None or cand[0]>best[0]:best=cand
    if not best:return dict(r,ww_status='REVIEW_NO_STRONG_WORK_AUTHOR_DATE')
    _,y,qid,pt,ma,ascore,years=best
    return dict(r,ww_status='SAFE_T_WORK_P577',ww_proven_t=t_of(y),ww_year=str(y),ww_qid=qid,ww_page_title=pt,ww_author_match=ma,ww_author_score=f'{ascore:.3f}',ww_p577_years=';'.join(map(str,years)))

rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
res=[]
with ThreadPoolExecutor(max_workers=4) as ex:
    futs={ex.submit(verify,r):r for r in rows}
    for i,f in enumerate(as_completed(futs),1):
        try:res.append(f.result())
        except Exception as e:res.append(dict(futs[f],ww_status='ERROR',ww_error=type(e).__name__))
        if i%25==0:print(i,flush=True)
safe=[r for r in res if r.get('ww_status')=='SAFE_T_WORK_P577'];review=[r for r in res if r.get('ww_status')!='SAFE_T_WORK_P577']
fields=[]
for r in safe+review:
    for k in r:
        if k not in fields:fields.append(k)
for p,data in [(SAFE,safe),(REVIEW,review)]:
    with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
REPORT.write_text('# P2 Wikipedia→Wikidata Work Verification V1\n\n> Read-only. A candidate is accepted only when an English Wikipedia work page maps to a Wikidata entity with strong title match, strong P50 author match, and work-level P577 publication date. Boundary years are blocked.\n\n'+f'- Residual inspected: **{len(rows)}**\n- SAFE_T_WORK_P577: **{len(safe)}**\n- REVIEW: **{len(review)}**\n\nNo Work files were mutated.\n\n`P2_WIKIPEDIA_WIKIDATA_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8');MARKER.unlink();print({'safe':len(safe),'review':len(review)})
