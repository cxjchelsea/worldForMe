from __future__ import annotations

import csv,json,re,unicodedata,urllib.parse,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
from difflib import SequenceMatcher
from pathlib import Path

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); AUDIT=ROOT/'_audit/t_axis_year_backfill'
IN=AUDIT/'missing_t_year_backfill_v1.csv'; BASE=AUDIT/'missing_t_year_research_v1.csv'
OUT=AUDIT/'missing_t_year_wikipedia_v2.csv'; SAFE=AUDIT/'missing_t_year_wikipedia_safe_v2.csv'; REPORT=AUDIT/'WIKIPEDIA_RESEARCH_V2.md'; MARKER=AUDIT/'RUN_MISSING_T_YEAR_WIKIPEDIA_V2'
UA={'User-Agent':'worldForMe-literature-audit/1.0'}; BOUND={500,1500,1800,1890,1945,1980}

def norm(s):
 s=unicodedata.normalize('NFKD',str(s or '')).casefold();return ''.join(c for c in s if c.isalnum())
def sim(a,b):
 a,b=norm(a),norm(b)
 if not a or not b:return 0.0
 return 1.0 if a==b else SequenceMatcher(None,a,b).ratio()
def get(url):
 req=urllib.request.Request(url,headers=UA)
 with urllib.request.urlopen(req,timeout=12) as r:return json.loads(r.read().decode('utf-8'))
def t_of(y):
 if y<500:return'T0'
 if y<1500:return'T1'
 if y<1800:return'T2'
 if y<1890:return'T3'
 if y<1945:return'T4'
 if y<1980:return'T5'
 return'T6'
def search_pages(title,author):
 queries=[f'"{title}" "{author}"',f'"{title}" {author}',title]
 out=[]
 for sq in queries:
  q=urllib.parse.urlencode({'action':'query','format':'json','list':'search','srsearch':sq,'srlimit':5})
  try:d=get('https://en.wikipedia.org/w/api.php?'+q)
  except:continue
  for x in d.get('query',{}).get('search',[]):
   tup=(x.get('title',''),x.get('pageid'))
   if tup[1] and tup not in out:out.append(tup)
 return out[:8]
def text_page(pid):
 q=urllib.parse.urlencode({'action':'query','format':'json','pageids':str(pid),'prop':'revisions|extracts','rvprop':'content','rvslots':'main','explaintext':1,'exintro':0,'formatversion':'2'})
 d=get('https://en.wikipedia.org/w/api.php?'+q);p=(d.get('query',{}).get('pages') or [{}])[0]
 wt=((((p.get('revisions') or [{}])[0].get('slots') or {}).get('main') or {}).get('content') or '')
 ex=p.get('extract','') or ''
 return wt,ex
def clean(s):
 s=re.sub(r'<ref[^>]*>.*?</ref>',' ',s,flags=re.S|re.I);s=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]+)\]\]',r'\1',s);s=re.sub(r'\{\{[^{}]*\}\}',' ',s);s=re.sub(r'<[^>]+>',' ',s);return re.sub(r'\s+',' ',s)
def field(wt,names):
 for n in names:
  m=re.search(rf'(?im)^\s*\|\s*{re.escape(n)}\s*=\s*(.+)$',wt)
  if m:return clean(m.group(1)).strip()
 return''
def years_from(s):
 return [int(x) for x in re.findall(r'(?<!\d)(1[5-9]\d{2}|20\d{2})(?!\d)',s)]
def research(r):
 title=r.get('title_original') or r.get('title') or '';author=r.get('author_original') or r.get('author') or ''
 rr=dict(r);rr.update({'wiki2_status':'REVIEW','wiki2_page':'','wiki2_year':'','wiki2_title_score':'','wiki2_author_evidence':'','wiki2_date_evidence':''})
 if not title or not author or '/' in author or author in {'佚名','匿名','民间','口传传统'}:return rr
 na=norm(author);nt=norm(title);best=None
 for pt,pid in search_pages(title,author):
  try:wt,ex=text_page(pid)
  except:continue
  blob=clean(wt[:15000]+' '+ex[:5000]);nb=norm(blob)
  ts=sim(title,pt)
  title_ok=ts>=0.72 or (nt and nt in nb)
  author_field=field(wt,['author','authors','writer','written_by']);author_ok=(sim(author,author_field)>=0.72) if author_field else (na and na in nb)
  if not title_ok or not author_ok:continue
  date_fields=[]
  for n in ['published','publication_date','pub_date','release_date','first_published','publication']:
   v=field(wt,[n])
   if v:date_fields.append(v)
  years=[];evidence=''
  for v in date_fields:
   ys=years_from(v)
   if ys:years+=ys;evidence+='FIELD:'+v+';'
  patterns=[r'first published(?:[^.]{0,80})\b(1[5-9]\d{2}|20\d{2})\b',r'originally published(?:[^.]{0,80})\b(1[5-9]\d{2}|20\d{2})\b',r'published(?:[^.]{0,50})\bin\s+(1[5-9]\d{2}|20\d{2})\b',r'published(?:[^.]{0,50})\b(1[5-9]\d{2}|20\d{2})\b']
  for pat in patterns:
   for m in re.finditer(pat,ex,flags=re.I):years.append(int(m.group(1)));evidence+='PROSE:'+m.group(0)[:100]+';'
  if not years:continue
  y=min(years);score=(1 if nt in nb else ts)+(1 if na in nb else sim(author,author_field))
  cand=(score,y,pt,ts,author_field or author,evidence)
  if best is None or cand[0]>best[0]:best=cand
 if not best:return rr
 _,y,pt,ts,ae,de=best;rr.update({'wiki2_status':'WORK_PAGE_YEAR','wiki2_page':pt,'wiki2_year':str(y),'wiki2_title_score':f'{ts:.3f}','wiki2_author_evidence':ae,'wiki2_date_evidence':de,'suggested_t':t_of(y)});return rr

def main():
 if not MARKER.exists():raise SystemExit('authorization marker missing')
 rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')));base={r.get('id'):r for r in csv.DictReader(BASE.open(encoding='utf-8-sig',newline=''))}
 out=[]
 with ThreadPoolExecutor(max_workers=5) as ex:
  futs={ex.submit(research,r):r for r in rows}
  for i,f in enumerate(as_completed(futs),1):
   try:out.append(f.result())
   except:out.append(dict(futs[f],wiki2_status='ERROR'))
   if i%50==0:print(i,flush=True)
 order={r.get('id'):i for i,r in enumerate(rows)};out.sort(key=lambda r:order.get(r.get('id'),10**9));safe=[]
 for r in out:
  if r.get('wiki2_status')!='WORK_PAGE_YEAR':continue
  b=base.get(r.get('id'),{})
  try:wy=int(r.get('wiki2_year',''));oy=int(b.get('ol_year','')) if b.get('ol_year') else None
  except:continue
  if oy is None or wy in BOUND or oy in BOUND:continue
  if t_of(wy)!=t_of(oy) or abs(wy-oy)>1:continue
  x=dict(r);x.update({'publication_year':str(min(wy,oy)),'confidence':'HIGH','review_status':'READY_FOR_WRITEBACK','year_source_1':'Wikipedia:'+r.get('wiki2_page',''),'year_source_2':'OpenLibrary:'+b.get('ol_key',''),'source_agreement':'WIKI2_PLUS_OL_EXACT_OR_1Y','suggested_t':t_of(wy)});safe.append(x)
 fields=[]
 for r in out+safe:
  for k in r:
   if k not in fields:fields.append(k)
 for p,data in [(OUT,out),(SAFE,safe)]:
  with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
 REPORT.write_text('# Missing-T Wikipedia Work-page Research V2\n\n'+f'- Input: **{len(rows)}**\n- Work-page year candidates: **{sum(1 for r in out if r.get("wiki2_status")=="WORK_PAGE_YEAR")}**\n- HIGH after Open Library cross-check: **{len(safe)}**\n\nNo Work file was modified.\n\n`MISSING_T_WIKIPEDIA_RESEARCH_V2 = COMPLETE_READ_ONLY`\n',encoding='utf-8');MARKER.unlink();print({'safe':len(safe)},flush=True)
if __name__=='__main__':main()
