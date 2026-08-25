from __future__ import annotations

import csv, json, re, time, unicodedata, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
AUDIT = ROOT / '_audit/t_axis_year_backfill'
IN = AUDIT / 'missing_t_year_backfill_v1.csv'
OUT = AUDIT / 'missing_t_year_research_v1.csv'
HIGH = AUDIT / 'missing_t_year_high_confidence_v1.csv'
REVIEW = AUDIT / 'missing_t_year_review_v1.csv'
REPORT = AUDIT / 'RESEARCH_V1.md'
MARKER = AUDIT / 'RUN_MISSING_T_YEAR_RESEARCH_V1'
UA = {'User-Agent':'worldForMe-literature-audit/1.0 (bibliographic research)'}
YEAR_RE = re.compile(r'(?<!\d)(-?\d{1,4})(?!\d)')
BOUND = {500,1500,1800,1890,1945,1980}


def norm(s):
    s = unicodedata.normalize('NFKD', str(s or '')).casefold()
    return ''.join(c for c in s if c.isalnum())

def sim(a,b):
    a,b=norm(a),norm(b)
    if not a or not b:return 0.0
    return 1.0 if a==b else SequenceMatcher(None,a,b).ratio()

def get(url, timeout=15):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return json.loads(r.read().decode('utf-8'))

def t_of(y):
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'

def entity(qid):
    return get(f'https://www.wikidata.org/wiki/Special:EntityData/{qid}.json')['entities'][qid]

def names(e):
    vals=[]
    for obj in (e.get('labels') or {}).values(): vals.append(obj.get('value',''))
    for arr in (e.get('aliases') or {}).values(): vals += [x.get('value','') for x in arr]
    return [x for x in vals if x]

def p50(e):
    out=[]
    for c in (e.get('claims') or {}).get('P50',[]):
        v=((c.get('mainsnak') or {}).get('datavalue') or {}).get('value')
        if isinstance(v,dict) and v.get('id'): out.append(v['id'])
    return out

def p577(e):
    out=[]
    for c in (e.get('claims') or {}).get('P577',[]):
        v=((c.get('mainsnak') or {}).get('datavalue') or {}).get('value')
        if isinstance(v,dict):
            m=re.search(r'([+-]\d{4,})-',str(v.get('time','')))
            if m:
                try: out.append(int(m.group(1)))
                except: pass
    return sorted(set(out))

def best_ol(title,author):
    q=urllib.parse.urlencode({'title':title,'author':author,'limit':8,'fields':'key,title,author_name,first_publish_year,publish_year'})
    try: data=get('https://openlibrary.org/search.json?'+q)
    except Exception as e: return None, type(e).__name__
    best=None
    for d in data.get('docs',[]):
        ts=sim(title,d.get('title',''))
        ascore=max([sim(author,x) for x in d.get('author_name',[]) ] or [0])
        if ts<0.90 or ascore<0.86: continue
        years=[]
        for y in d.get('publish_year',[]) or []:
            try: years.append(int(y))
            except: pass
        fpy=d.get('first_publish_year')
        try: fpy=int(fpy) if fpy is not None else None
        except: fpy=None
        score=ts+ascore
        cand={'score':score,'title':d.get('title',''),'author':' ; '.join(d.get('author_name',[]) or []),'key':d.get('key',''),'fpy':fpy,'years':sorted(set(years)),'ts':ts,'as':ascore}
        if best is None or cand['score']>best['score']: best=cand
    return best,''

def wikidata_candidates(title):
    q=urllib.parse.urlencode({'action':'wbsearchentities','format':'json','language':'en','uselang':'en','type':'item','limit':8,'search':title})
    try: data=get('https://www.wikidata.org/w/api.php?'+q)
    except Exception: return []
    return [x.get('id') for x in data.get('search',[]) if x.get('id')]

def wikipedia_candidates(title):
    q=urllib.parse.urlencode({'action':'query','format':'json','generator':'search','gsrsearch':f'intitle:"{title}"','gsrlimit':5,'prop':'pageprops','ppprop':'wikibase_item','redirects':1})
    try: data=get('https://en.wikipedia.org/w/api.php?'+q)
    except Exception: return []
    out=[]
    for p in (data.get('query') or {}).get('pages',{}).values():
        qid=(p.get('pageprops') or {}).get('wikibase_item')
        if qid: out.append(qid)
    return out

def best_wd(title,author):
    qids=[]
    for qid in wikipedia_candidates(title)+wikidata_candidates(title):
        if qid not in qids:qids.append(qid)
    best=None
    for qid in qids[:10]:
        try:e=entity(qid)
        except:continue
        ts=max([sim(title,n) for n in names(e)] or [0])
        if ts<0.92:continue
        years=p577(e); authors=p50(e)
        if not years or not authors:continue
        ascore=0.0;matched=''
        for aq in authors[:5]:
            try:ae=entity(aq)
            except:continue
            for n in names(ae):
                s=sim(author,n)
                if s>ascore:ascore=s;matched=n
        if ascore<0.88:continue
        y=min(years)
        score=ts+ascore
        cand={'qid':qid,'year':y,'years':years,'ts':ts,'as':ascore,'author':matched,'score':score}
        if best is None or cand['score']>best['score']:best=cand
    return best

def research(r):
    title=r.get('title_original') or r.get('title') or ''
    author=r.get('author_original') or r.get('author') or ''
    rr=dict(r)
    rr.update({'ol_year':'','ol_title':'','ol_author':'','ol_key':'','ol_title_score':'','ol_author_score':'','wd_year':'','wd_qid':'','wd_title_score':'','wd_author_match':'','wd_author_score':'','research_error':''})
    if not title or not author or '/' in author or author in {'佚名','匿名','民间','口传传统'}:
        rr.update({'confidence':'REVIEW','review_status':'SPECIAL_OR_INSUFFICIENT_IDENTITY','notes':'missing/special/multi author identity'})
        return rr
    ol,err=best_ol(title,author)
    if ol:
        rr.update({'ol_year':str(ol['fpy'] or ''),'ol_title':ol['title'],'ol_author':ol['author'],'ol_key':ol['key'],'ol_title_score':f"{ol['ts']:.3f}",'ol_author_score':f"{ol['as']:.3f}"})
    elif err: rr['research_error']=err
    wd=best_wd(title,author)
    if wd:
        rr.update({'wd_year':str(wd['year']),'wd_qid':wd['qid'],'wd_title_score':f"{wd['ts']:.3f}",'wd_author_match':wd['author'],'wd_author_score':f"{wd['as']:.3f}"})
    years=[]
    if ol and ol['fpy'] is not None: years.append(('OpenLibrary',ol['fpy']))
    if wd: years.append(('Wikidata',wd['year']))
    # HIGH: strong Wikidata work-level P577 + strong OL identity and same exact year, or within 1 year and same T.
    if wd and ol and ol['fpy'] is not None:
        oy,wy=ol['fpy'],wd['year']
        same_t=t_of(oy)==t_of(wy)
        if same_t and abs(oy-wy)<=1 and oy not in BOUND and wy not in BOUND:
            y=min(oy,wy)
            rr.update({'publication_year':str(y),'publication_year_type':'first_publication_or_first_appearance','year_source_1':f'Wikidata:{wd["qid"]}','year_source_2':f'OpenLibrary:{ol["key"]}','source_agreement':'EXACT_OR_1Y_SAME_T','confidence':'HIGH','suggested_t':t_of(y),'review_status':'READY_FOR_WRITEBACK','notes':'strong title+author match in both sources'})
            return rr
        if same_t:
            rr.update({'source_agreement':'SAME_T_DIFFERENT_YEAR','confidence':'MEDIUM','suggested_t':t_of(wy),'review_status':'YEAR_REVIEW','notes':f'OL={oy}; WD={wy}; same T but year differs'})
            return rr
        rr.update({'source_agreement':'CROSS_T_CONFLICT','confidence':'REVIEW','review_status':'CONFLICT_REVIEW','notes':f'OL={oy}/{t_of(oy)}; WD={wy}/{t_of(wy)}'})
        return rr
    if wd:
        rr.update({'publication_year':str(wd['year']),'publication_year_type':'work_level_P577','year_source_1':f'Wikidata:{wd["qid"]}','confidence':'MEDIUM','suggested_t':t_of(wd['year']),'review_status':'SECOND_SOURCE_NEEDED','notes':'strong work-level Wikidata match; second source unavailable'})
        return rr
    if ol and ol['fpy'] is not None:
        rr.update({'publication_year':str(ol['fpy']),'publication_year_type':'catalog_first_publish_year_candidate','year_source_1':f'OpenLibrary:{ol["key"]}','confidence':'REVIEW','suggested_t':t_of(ol['fpy']),'review_status':'REPRINT_RISK_REVIEW','notes':'OpenLibrary only; reprint contamination risk'})
        return rr
    rr.update({'confidence':'REVIEW','review_status':'NO_STRONG_MATCH','notes':'no strong work-level year match'})
    return rr

def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
    out=[]
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs={ex.submit(research,r):r for r in rows}
        for i,f in enumerate(as_completed(futs),1):
            try:out.append(f.result())
            except Exception as e:
                r=dict(futs[f]);r.update({'confidence':'REVIEW','review_status':'ERROR','research_error':type(e).__name__});out.append(r)
            if i%50==0:print(f'{i}/{len(rows)}',flush=True)
    order={r.get('id'):i for i,r in enumerate(rows)}
    out.sort(key=lambda r:order.get(r.get('id'),10**9))
    fields=[]
    for r in out:
        for k in r:
            if k not in fields:fields.append(k)
    for p,data in [(OUT,out),(HIGH,[r for r in out if r.get('confidence')=='HIGH']),(REVIEW,[r for r in out if r.get('confidence')!='HIGH'])]:
        with p.open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
    from collections import Counter
    c=Counter(r.get('confidence','') for r in out); s=Counter(r.get('review_status','') for r in out)
    REPORT.write_text('# Missing-T Publication Year Research V1\n\n> Full-population read-only research. No Work file is modified.\n\n'+f'- Input: **{len(rows)}**\n- HIGH: **{c["HIGH"]}**\n- MEDIUM: **{c["MEDIUM"]}**\n- REVIEW: **{c["REVIEW"]}**\n\n## Status\n\n'+'\n'.join(f'- {k}: **{v}**' for k,v in sorted(s.items()))+'\n\n`MISSING_T_YEAR_RESEARCH_V1 = COMPLETE_READ_ONLY`\n',encoding='utf-8')
    MARKER.unlink();print(dict(c),flush=True)

if __name__=='__main__':main()
