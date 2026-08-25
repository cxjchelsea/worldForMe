from __future__ import annotations

import csv, json, re, time, unicodedata, urllib.parse, urllib.request, urllib.error
from difflib import SequenceMatcher
from pathlib import Path

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
AUDIT=ROOT/'_audit/t_axis_completeness'
TRIAGE=AUDIT/'missing_t_triage_v1.csv'
OUT=AUDIT/'p2_wikidata_serial_v2.csv'
SAFE=AUDIT/'p2_wikidata_serial_safe_v2.csv'
REVIEW=AUDIT/'p2_wikidata_serial_review_v2.csv'
REPORT=AUDIT/'P2_WIKIDATA_SERIAL_V2.md'
UA='worldForMe-literature-audit/2.0 contact:github.com/cxjchelsea/worldForMe'
BOUNDARIES={500,1500,1800,1890,1945,1980}
LANGS=['en','es','pt','fr','de','it','ru','ja']

def norm(s):
    s=unicodedata.normalize('NFKD',s or '')
    s=''.join(c for c in s if not unicodedata.combining(c)).casefold()
    s=re.sub(r'[^0-9a-z\u4e00-\u9fff]+',' ',s)
    return re.sub(r'\s+',' ',s).strip()

def sim(a,b):
    a,b=norm(a),norm(b)
    if not a or not b:return 0.0
    if a==b:return 1.0
    return SequenceMatcher(None,a,b).ratio()

def t_for(y):
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'

def api(params,retries=5):
    url='https://www.wikidata.org/w/api.php?'+urllib.parse.urlencode({**params,'format':'json','formatversion':'2'})
    for attempt in range(retries):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
            with urllib.request.urlopen(req,timeout=20) as r:
                data=json.load(r)
            time.sleep(0.18)
            return data
        except urllib.error.HTTPError as e:
            if e.code in (429,500,502,503,504):
                time.sleep(1.5*(attempt+1));continue
            raise
        except Exception:
            if attempt==retries-1:raise
            time.sleep(1.0*(attempt+1))
    raise RuntimeError('api retries exhausted')

def years(ent):
    out=[]
    for c in ent.get('claims',{}).get('P577',[]):
        try:
            v=c['mainsnak']['datavalue']['value']['time']
            m=re.match(r'[+-](\d+)-',v)
            if m: out.append(int(m.group(1)))
        except:pass
    return sorted(set(y for y in out if 1<=y<=2026))

def author_qids(ent):
    out=[]
    for c in ent.get('claims',{}).get('P50',[]):
        try:out.append(c['mainsnak']['datavalue']['value']['id'])
        except:pass
    return out

def get_labels(qids):
    if not qids:return {}
    d=api({'action':'wbgetentities','ids':'|'.join(qids[:50]),'props':'labels','languages':'en|zh|es|pt|fr|de|it|ru|ja'})
    out={}
    for e in d.get('entities',[]):
        vals=[v['value'] for v in e.get('labels',{}).values() if v.get('value')]
        out[e['id']]=' / '.join(dict.fromkeys(vals))
    return out

def search_ids(title):
    ids=[]
    for lang in LANGS:
        try:d=api({'action':'wbsearchentities','search':title,'language':lang,'uselang':'en','type':'item','limit':'10'})
        except:continue
        ids += [x['id'] for x in d.get('search',[]) if x.get('id')]
        if len(set(ids))>=10:break
    return list(dict.fromkeys(ids))[:20]

def resolve(row):
    titles=[x for x in [row.get('title_original',''),row.get('title','')] if x]
    author=row.get('author_original') or row.get('author') or ''
    if not titles:return {'wd2_status':'NO_TITLE'}
    ids=[]
    for title in titles:
        ids += search_ids(title)
        if len(set(ids))>=12:break
    ids=list(dict.fromkeys(ids))[:20]
    if not ids:return {'wd2_status':'NO_MATCH'}
    try:d=api({'action':'wbgetentities','ids':'|'.join(ids),'props':'labels|aliases|claims','languages':'en|zh|es|pt|fr|de|it|ru|ja'})
    except Exception as e:return {'wd2_status':'ERROR','wd2_error':type(e).__name__}
    ents={e['id']:e for e in d.get('entities',[])}
    aq=[]
    for e in ents.values():aq += author_qids(e)
    try:alabel=get_labels(list(dict.fromkeys(aq)))
    except:alabel={}
    cand=[]
    for qid in ids:
        e=ents.get(qid,{})
        ys=years(e)
        if not ys:continue
        names=[v['value'] for v in e.get('labels',{}).values() if v.get('value')]
        for arr in e.get('aliases',{}).values():names += [v['value'] for v in arr if v.get('value')]
        ts=max((sim(t,n) for t in titles for n in names),default=0)
        atext=' / '.join(alabel.get(q,'') for q in author_qids(e) if alabel.get(q,''))
        aus=sim(author,atext) if author else 0
        if ts>=0.90 and aus>=0.72:
            y=min(ys)
            cand.append((ts+aus,-y,qid,y,ts,aus,names[0] if names else '',atext,','.join(map(str,ys))))
    if not cand:return {'wd2_status':'NO_RELIABLE_WORK_MATCH'}
    cand.sort(reverse=True);_,_,qid,y,ts,aus,label,atext,all_y=cand[0]
    return {'wd2_status':'MATCH','wd2_qid':qid,'wd2_year':str(y),'wd2_t':t_for(y),'wd2_label':label,'wd2_authors':atext,'wd2_title_similarity':f'{ts:.3f}','wd2_author_similarity':f'{aus:.3f}','wd2_all_p577':all_y}

def main():
    with TRIAGE.open(encoding='utf-8-sig',newline='') as f:rows=[r for r in csv.DictReader(f) if r.get('tier')=='P2_EXTERNAL_MATCH_FRIENDLY']
    out=[];safe=[];review=[]
    for i,r in enumerate(rows,1):
        try:wd=resolve(r)
        except Exception as e:wd={'wd2_status':'ERROR','wd2_error':type(e).__name__}
        merged=dict(r);merged.update(wd)
        y=int(wd['wd2_year']) if wd.get('wd2_status')=='MATCH' and wd.get('wd2_year','').isdigit() else None
        if y is not None and y not in BOUNDARIES:
            merged['resolution_status']='SAFE_WIKIDATA_WORK'
            merged['chosen_t']=wd['wd2_t'];merged['canonical_year_candidate']=str(y)
            merged['resolution_reason']='Wikidata 强标题匹配 + P50 作者匹配 + 作品级 P577'
            safe.append(merged)
        else:
            merged['resolution_status']='REVIEW';merged['chosen_t']='';merged['canonical_year_candidate']=''
            merged['resolution_reason']='缺少可靠作品级 P577/P50 组合或边界年'
            review.append(merged)
        out.append(merged)
        if i%25==0:print(f'wd_serial={i}/{len(rows)} safe={len(safe)}',flush=True)
    fields=list(dict.fromkeys(k for r in out for k in r))
    for p,rr in [(OUT,out),(SAFE,safe),(REVIEW,review)]:
        with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rr)
    REPORT.write_text('\n'.join(['# P2 Wikidata Serial Verification V2','',f'- P2 population: **{len(rows)}**',f'- SAFE_WIKIDATA_WORK: **{len(safe)}**',f'- REVIEW: **{len(review)}**','','Serial, retrying access is used to avoid rate-limit artifacts. Accepted rows require title + P50 author + P577 publication-date evidence.','','`P2_WIKIDATA_SERIAL_V2 = AUDITED_READ_ONLY`','']),encoding='utf-8')
    print(f'p2={len(rows)} safe={len(safe)} review={len(review)}')
if __name__=='__main__':main()
