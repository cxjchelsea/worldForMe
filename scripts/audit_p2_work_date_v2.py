from pathlib import Path
import csv,json,re,unicodedata,urllib.parse,urllib.request
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor,as_completed

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_residual_review_v1.csv'; SAFE=AUDIT/'p2_work_date_v2_safe.csv'; REVIEW=AUDIT/'p2_work_date_v2_review.csv'; REPORT=AUDIT/'P2_WORK_DATE_V2.md'; MARKER=AUDIT/'RUN_P2_WORK_DATE_V2'
UA={'User-Agent':'worldForMe-literature-audit/2.0 (bibliographic verification)'}
YEAR_RE=re.compile(r'([12][0-9]{3})'); BOUND={500,1500,1800,1890,1945,1980}

def t_of(y):
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'

def norm(s):
    s=unicodedata.normalize('NFKD',str(s or '')).casefold()
    return ''.join(c for c in s if c.isalnum())
def sim(a,b):
    a,b=norm(a),norm(b)
    if not a or not b:return 0.0
    if a==b:return 1.0
    return SequenceMatcher(None,a,b).ratio()
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=15) as r:return json.loads(r.read().decode('utf-8'))
def entity(qid):return get(f'https://www.wikidata.org/wiki/Special:EntityData/{qid}.json')['entities'][qid]
def names(e):
    vals=[]
    for o in (e.get('labels') or {}).values(): vals.append(o.get('value',''))
    for arr in (e.get('aliases') or {}).values(): vals.extend(x.get('value','') for x in arr)
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

def wikipedia_qids(title,author):
    terms=[f'"{title}" {author}',title]
    out=[]
    for term in terms:
        try:
            q=urllib.parse.urlencode({'action':'query','format':'json','generator':'search','gsrsearch':term,'gsrlimit':6,'prop':'pageprops','ppprop':'wikibase_item','redirects':1})
            data=get('https://en.wikipedia.org/w/api.php?'+q)
            for p in (data.get('query') or {}).get('pages',{}).values():
                qid=(p.get('pageprops') or {}).get('wikibase_item')
                if qid and qid not in out: out.append(qid)
        except Exception: pass
    return out[:8]
def wikidata_qids(title):
    out=[]
    for lang in ['en']:
        try:
            q=urllib.parse.urlencode({'action':'wbsearchentities','format':'json','language':lang,'search':title,'limit':8,'type':'item'})
            data=get('https://www.wikidata.org/w/api.php?'+q)
            for x in data.get('search',[]):
                qid=x.get('id')
                if qid and qid not in out: out.append(qid)
        except Exception: pass
    return out[:8]
def author_match_score(author,author_qids):
    best=(0.0,'')
    for aq in author_qids[:5]:
        try: ae=entity(aq)
        except Exception: continue
        for n in names(ae):
            s=sim(author,n)
            if s>best[0]:best=(s,n)
    return best

def evaluate_qid(qid,title,author,source):
    try:e=entity(qid)
    except Exception:return None
    ts=max([sim(title,n) for n in names(e)] or [0])
    if ts<0.90:return None
    years=p577_years(e);authors=p50(e)
    if not years or not authors:return None
    ascore,aname=author_match_score(author,authors)
    if ascore<0.88:return None
    y=min(years)
    if y in BOUND:return None
    return {'qid':qid,'source':source,'year':y,'t':t_of(y),'title_score':ts,'author_score':ascore,'author_match':aname,'years':years}

def verify(r):
    title=r.get('title_original') or r.get('title') or ''
    author=r.get('author_original') or r.get('author') or ''
    cands=[]
    for qid in wikipedia_qids(title,author):
        x=evaluate_qid(qid,title,author,'wikipedia_search')
        if x:cands.append(x)
    for qid in wikidata_qids(title):
        if any(x['qid']==qid for x in cands):continue
        x=evaluate_qid(qid,title,author,'wikidata_search')
        if x:cands.append(x)
    if not cands:return dict(r,wd2_status='REVIEW_NO_STRONG_WORK_AUTHOR_DATE')
    # Keep best per qid, then require all accepted strong candidates to agree on T.
    uniq={x['qid']:x for x in cands}; vals=list(uniq.values())
    ts=sorted(set(x['t'] for x in vals))
    if len(ts)!=1:
        return dict(r,wd2_status='REVIEW_CANDIDATE_T_CONFLICT',wd2_candidate_ts=';'.join(ts),wd2_candidate_qids=';'.join(x['qid'] for x in vals))
    vals.sort(key=lambda x:(x['title_score']+x['author_score'],-x['year']),reverse=True)
    b=vals[0]
    return dict(r,wd2_status='SAFE_T_WORK_DATE_V2',wd2_proven_t=b['t'],wd2_year=str(b['year']),wd2_qid=b['qid'],wd2_source=b['source'],wd2_title_score=f"{b['title_score']:.3f}",wd2_author_match=b['author_match'],wd2_author_score=f"{b['author_score']:.3f}",wd2_p577_years=';'.join(map(str,b['years'])),wd2_strong_candidate_count=str(len(vals)))

def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
    rows=[r for r in rows if r.get('residual_bucket')=='AUTHOR_RANGE_SPANS_T']
    res=[]
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs={ex.submit(verify,r):r for r in rows}
        for i,f in enumerate(as_completed(futs),1):
            try:res.append(f.result())
            except Exception as e:res.append(dict(futs[f],wd2_status='ERROR',wd2_error=type(e).__name__))
            if i%20==0:print(i,flush=True)
    safe=[r for r in res if r.get('wd2_status')=='SAFE_T_WORK_DATE_V2'];review=[r for r in res if r.get('wd2_status')!='SAFE_T_WORK_DATE_V2']
    fields=[]
    for r in safe+review:
        for k in r:
            if k not in fields:fields.append(k)
    for p,data in [(SAFE,safe),(REVIEW,review)]:
        with p.open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
    conflicts=sum(1 for r in review if r.get('wd2_status')=='REVIEW_CANDIDATE_T_CONFLICT')
    REPORT.write_text('# P2 Work-level Date Verification V2\n\n> Read-only. Scope: residual `AUTHOR_RANGE_SPANS_T` only. Candidates come from English Wikipedia search and Wikidata entity search; acceptance requires strong work-title match, strong P50 author match, and work-level P577. Strong-candidate T conflicts are blocked.\n\n'+f'- Input AUTHOR_RANGE_SPANS_T: **{len(rows)}**\n- SAFE_T_WORK_DATE_V2: **{len(safe)}**\n- Candidate T conflicts blocked: **{conflicts}**\n- REVIEW: **{len(review)}**\n\nNo Work files were mutated.\n\n`P2_WORK_DATE_V2 = AUDITED_READ_ONLY`\n',encoding='utf-8')
    MARKER.unlink();print({'input':len(rows),'safe':len(safe),'conflicts':conflicts,'review':len(review)})
if __name__=='__main__':main()
