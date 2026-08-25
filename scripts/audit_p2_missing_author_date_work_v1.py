from pathlib import Path
import csv,json,re,unicodedata,urllib.parse,urllib.request
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor,as_completed

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_residual_review_v1.csv'; SAFE=AUDIT/'p2_missing_author_date_work_safe_v1.csv'; REVIEW=AUDIT/'p2_missing_author_date_work_review_v1.csv'; REPORT=AUDIT/'P2_MISSING_AUTHOR_DATE_WORK_V1.md'; MARKER=AUDIT/'RUN_P2_MISSING_AUTHOR_DATE_WORK_V1'
UA={'User-Agent':'worldForMe-literature-audit/2.1 (bibliographic verification)'}
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
    s=unicodedata.normalize('NFKD',str(s or '')).casefold();return ''.join(c for c in s if c.isalnum())
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
    for o in (e.get('labels') or {}).values():vals.append(o.get('value',''))
    for arr in (e.get('aliases') or {}).values():vals.extend(x.get('value','') for x in arr)
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
def search_qids(title,author):
    out=[]
    for term in [f'"{title}" {author}',title]:
        try:
            q=urllib.parse.urlencode({'action':'query','format':'json','generator':'search','gsrsearch':term,'gsrlimit':6,'prop':'pageprops','ppprop':'wikibase_item','redirects':1})
            data=get('https://en.wikipedia.org/w/api.php?'+q)
            for p in (data.get('query') or {}).get('pages',{}).values():
                qid=(p.get('pageprops') or {}).get('wikibase_item')
                if qid and qid not in out:out.append(qid)
        except Exception:pass
    try:
        q=urllib.parse.urlencode({'action':'wbsearchentities','format':'json','language':'en','search':title,'limit':8,'type':'item'})
        data=get('https://www.wikidata.org/w/api.php?'+q)
        for x in data.get('search',[]):
            qid=x.get('id')
            if qid and qid not in out:out.append(qid)
    except Exception:pass
    return out[:12]
def author_score(author,qids):
    best=(0.0,'')
    for qid in qids[:5]:
        try:e=entity(qid)
        except Exception:continue
        for n in names(e):
            s=sim(author,n)
            if s>best[0]:best=(s,n)
    return best
def verify(r):
    title=r.get('title_original') or r.get('title') or '';author=r.get('author_original') or r.get('author') or ''
    strong=[]
    for qid in search_qids(title,author):
        try:e=entity(qid)
        except Exception:continue
        ts=max([sim(title,n) for n in names(e)] or [0])
        if ts<0.90:continue
        years=p577_years(e);aq=p50(e)
        if not years or not aq:continue
        asc,an=author_score(author,aq)
        if asc<0.88:continue
        y=min(years)
        if y in BOUND:continue
        strong.append((qid,y,t_of(y),ts,asc,an,years))
    if not strong:return dict(r,mad_status='REVIEW_NO_STRONG_WORK_AUTHOR_DATE')
    ts=sorted(set(x[2] for x in strong))
    if len(ts)!=1:return dict(r,mad_status='REVIEW_CANDIDATE_T_CONFLICT',mad_candidate_ts=';'.join(ts),mad_candidate_qids=';'.join(x[0] for x in strong))
    strong.sort(key=lambda x:(x[3]+x[4],-x[1]),reverse=True);b=strong[0]
    return dict(r,mad_status='SAFE_T_MISSING_AUTHOR_DATE_WORK',mad_proven_t=b[2],mad_year=str(b[1]),mad_qid=b[0],mad_title_score=f'{b[3]:.3f}',mad_author_match=b[5],mad_author_score=f'{b[4]:.3f}',mad_p577_years=';'.join(map(str,b[6])),mad_strong_candidate_count=str(len(strong)))
def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')));rows=[r for r in rows if r.get('residual_bucket')=='AUTHOR_DATE_MISSING']
    res=[]
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs={ex.submit(verify,r):r for r in rows}
        for i,f in enumerate(as_completed(futs),1):
            try:res.append(f.result())
            except Exception as e:res.append(dict(futs[f],mad_status='ERROR',mad_error=type(e).__name__))
            if i%20==0:print(i,flush=True)
    safe=[r for r in res if r.get('mad_status')=='SAFE_T_MISSING_AUTHOR_DATE_WORK'];review=[r for r in res if r.get('mad_status')!='SAFE_T_MISSING_AUTHOR_DATE_WORK']
    fields=[]
    for r in safe+review:
        for k in r:
            if k not in fields:fields.append(k)
    for p,data in [(SAFE,safe),(REVIEW,review)]:
        with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
    conflicts=sum(1 for r in review if r.get('mad_status')=='REVIEW_CANDIDATE_T_CONFLICT')
    REPORT.write_text('# P2 Missing-author-date Work Verification V1\n\n> Read-only. Scope: `AUTHOR_DATE_MISSING`. Author lifespan is not inferred; acceptance requires strong work-title match, strong P50 author match, and work-level P577. Candidate T conflicts are blocked.\n\n'+f'- Input AUTHOR_DATE_MISSING: **{len(rows)}**\n- SAFE_T_MISSING_AUTHOR_DATE_WORK: **{len(safe)}**\n- Candidate T conflicts blocked: **{conflicts}**\n- REVIEW: **{len(review)}**\n\nNo Work files were mutated.\n\n`P2_MISSING_AUTHOR_DATE_WORK_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8');MARKER.unlink();print({'input':len(rows),'safe':len(safe),'conflicts':conflicts,'review':len(review)})
if __name__=='__main__':main()
