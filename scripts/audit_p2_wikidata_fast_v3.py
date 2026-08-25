from __future__ import annotations
import csv,json,re,time,unicodedata,urllib.parse,urllib.request,urllib.error
from concurrent.futures import ThreadPoolExecutor,as_completed
from difflib import SequenceMatcher
from pathlib import Path
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); AUDIT=ROOT/'_audit/t_axis_completeness'; TRIAGE=AUDIT/'missing_t_triage_v1.csv'
OUT=AUDIT/'p2_wikidata_fast_v3.csv'; SAFE=AUDIT/'p2_wikidata_fast_safe_v3.csv'; REVIEW=AUDIT/'p2_wikidata_fast_review_v3.csv'; REPORT=AUDIT/'P2_WIKIDATA_FAST_V3.md'
UA='worldForMe-literature-audit/3.0'; B={500,1500,1800,1890,1945,1980}
def norm(s):
 s=unicodedata.normalize('NFKD',s or '');s=''.join(c for c in s if not unicodedata.combining(c)).casefold();s=re.sub(r'[^0-9a-z\u4e00-\u9fff]+',' ',s);return re.sub(r'\s+',' ',s).strip()
def sim(a,b):
 a,b=norm(a),norm(b);return 0 if not a or not b else (1.0 if a==b else SequenceMatcher(None,a,b).ratio())
def tf(y):
 return 'T0' if y<500 else 'T1' if y<1500 else 'T2' if y<1800 else 'T3' if y<1890 else 'T4' if y<1945 else 'T5' if y<1980 else 'T6'
def api(p):
 url='https://www.wikidata.org/w/api.php?'+urllib.parse.urlencode({**p,'format':'json','formatversion':'2'})
 for n in range(4):
  try:
   req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'application/json'});return json.load(urllib.request.urlopen(req,timeout=15))
  except urllib.error.HTTPError as e:
   if e.code in (429,500,502,503,504):time.sleep(0.8*(n+1));continue
   raise
  except Exception:
   if n==3:raise
   time.sleep(0.5*(n+1))
 raise RuntimeError()
def yrs(e):
 z=[]
 for c in e.get('claims',{}).get('P577',[]):
  try:
   m=re.match(r'[+-](\d+)-',c['mainsnak']['datavalue']['value']['time']);
   if m:z.append(int(m.group(1)))
  except:pass
 return sorted(set(y for y in z if 1<=y<=2026))
def aq(e):
 z=[]
 for c in e.get('claims',{}).get('P50',[]):
  try:z.append(c['mainsnak']['datavalue']['value']['id'])
  except:pass
 return z
def resolve(r):
 title=r.get('title_original') or r.get('title') or ''; author=r.get('author_original') or r.get('author') or ''
 try:s=api({'action':'wbsearchentities','search':title,'language':'en','uselang':'en','type':'item','limit':'12'})
 except Exception as e:return {'wd3_status':'ERROR','wd3_error':type(e).__name__}
 ids=[x['id'] for x in s.get('search',[]) if x.get('id')]
 if not ids:return {'wd3_status':'NO_MATCH'}
 try:d=api({'action':'wbgetentities','ids':'|'.join(ids),'props':'labels|aliases|claims','languages':'en|zh|es|pt|fr|de|it|ru|ja'})
 except Exception as e:return {'wd3_status':'ERROR','wd3_error':type(e).__name__}
 ents={e['id']:e for e in d.get('entities',[])}; aids=list(dict.fromkeys(q for e in ents.values() for q in aq(e))); amap={}
 if aids:
  try:
   ad=api({'action':'wbgetentities','ids':'|'.join(aids[:50]),'props':'labels','languages':'en|zh|es|pt|fr|de|it|ru|ja'})
   for e in ad.get('entities',[]):amap[e['id']]=' / '.join(v['value'] for v in e.get('labels',{}).values() if v.get('value'))
  except:pass
 cand=[]
 for qid in ids:
  e=ents.get(qid,{});ys=yrs(e)
  if not ys:continue
  names=[v['value'] for v in e.get('labels',{}).values() if v.get('value')]
  for arr in e.get('aliases',{}).values():names += [v['value'] for v in arr if v.get('value')]
  ts=max((sim(title,n) for n in names),default=0); at=' / '.join(amap.get(q,'') for q in aq(e) if amap.get(q)); au=sim(author,at)
  if ts>=.9 and au>=.72:cand.append((ts+au,-min(ys),qid,min(ys),ts,au,names[0] if names else '',at,','.join(map(str,ys))))
 if not cand:return {'wd3_status':'NO_RELIABLE'}
 cand.sort(reverse=True);_,_,qid,y,ts,au,lab,at,ally=cand[0]
 return {'wd3_status':'MATCH','wd3_qid':qid,'wd3_year':str(y),'wd3_t':tf(y),'wd3_label':lab,'wd3_authors':at,'wd3_title_similarity':f'{ts:.3f}','wd3_author_similarity':f'{au:.3f}','wd3_all_p577':ally}
def main():
 with TRIAGE.open(encoding='utf-8-sig',newline='') as f:rows=[r for r in csv.DictReader(f) if r.get('tier')=='P2_EXTERNAL_MATCH_FRIENDLY']
 mm={}
 with ThreadPoolExecutor(max_workers=2) as ex:
  fs={ex.submit(resolve,r):r for r in rows}
  for i,fu in enumerate(as_completed(fs),1):
   r=fs[fu]
   try:mm[r['id']]=fu.result()
   except Exception as e:mm[r['id']]={'wd3_status':'ERROR','wd3_error':type(e).__name__}
   if i%50==0:print(f'wd3={i}/{len(rows)}',flush=True)
 out=[];safe=[];review=[]
 for r in rows:
  d=mm.get(r['id'],{});m=dict(r);m.update(d); y=int(d['wd3_year']) if d.get('wd3_status')=='MATCH' and d.get('wd3_year','').isdigit() else None
  if y is not None and y not in B:
   m.update(resolution_status='SAFE_WIKIDATA_WORK',chosen_t=d['wd3_t'],canonical_year_candidate=str(y),resolution_reason='title+P50+P577') ;safe.append(m)
  else:m.update(resolution_status='REVIEW',chosen_t='',canonical_year_candidate='',resolution_reason='no reliable work-level evidence or boundary');review.append(m)
  out.append(m)
 fields=list(dict.fromkeys(k for r in out for k in r))
 for p,rr in [(OUT,out),(SAFE,safe),(REVIEW,review)]:
  with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rr)
 REPORT.write_text(f'# P2 Wikidata Fast Verification V3\n\n- P2 population: **{len(rows)}**\n- SAFE_WIKIDATA_WORK: **{len(safe)}**\n- REVIEW: **{len(review)}**\n\n`P2_WIKIDATA_FAST_V3 = AUDITED_READ_ONLY`\n',encoding='utf-8')
 print(f'p2={len(rows)} safe={len(safe)} review={len(review)}')
if __name__=='__main__':main()
