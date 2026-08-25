from __future__ import annotations
import csv,json,re,time,unicodedata,urllib.parse,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
from difflib import SequenceMatcher
from pathlib import Path

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学/40 作品')
OUT=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis_completeness')
MARKER=OUT/'RUN_OPENLIBRARY_PRIORITY_V2'
BOUNDARIES={500,1500,1800,1890,1945,1980}
UA='worldForMe-bibliography-audit/2.0'
SPECIAL=re.compile(r'(全集|文集|选集|诗选|短篇小说集|故事集|传说|神话|史诗|往世书|歌谣|民谣|口传|作品集)')

def fm(t):
 m=re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',t,re.S);return m.group(1) if m else ''
def scalar(x,k):
 m=re.search(rf'(?m)^{re.escape(k)}:\s*(.*?)\s*$',x)
 if not m:return ''
 v=m.group(1).strip().strip('"\'');return '' if v.lower() in {'null','none','~'} else v
def lst(x,k):
 lines=x.splitlines()
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(k)}:\s*\[\s*\]\s*$',line):return []
  if re.match(rf'^{re.escape(k)}:\s*$',line):
   out=[]
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*(.*?)\s*$',n)
    if m:out.append(m.group(1).strip().strip('"\''));continue
    if re.match(r'^[A-Za-z0-9_\u4e00-\u9fff].*?:',n):break
    if n.strip() and not n.startswith((' ','\t')):break
   return out
 return []
def norm(s):
 s=unicodedata.normalize('NFKD',s or '').casefold();s=''.join(c for c in s if not unicodedata.combining(c));return ''.join(c for c in s if c.isalnum())
def sim(a,b):
 a,b=norm(a),norm(b)
 if not a or not b:return 0.0
 return 1.0 if a==b else SequenceMatcher(None,a,b).ratio()
def tyear(y):
 return 'T0' if y<500 else 'T1' if y<1500 else 'T2' if y<1800 else 'T3' if y<1890 else 'T4' if y<1945 else 'T5' if y<1980 else 'T6'
def has_cjk(s):return any('\u4e00'<=c<='\u9fff' for c in (s or ''))
def tier(x,title,author):
 special=bool(SPECIAL.search(title)) or author in {'佚名','匿名','民间','口传传统'} or bool(lst(x,'literary_traditions'))
 if special:return 'S_SPECIAL_TEXT'
 if scalar(x,'canon_id') or lst(x,'awards'):return 'P1_CANON_AWARD'
 if scalar(x,'author_original') and (scalar(x,'title_original') or not has_cjk(title)):return 'P2_EXTERNAL_MATCH_FRIENDLY'
 return 'P3_GENERAL_REVIEW'
def resolve(it):
 qtitle=it['title_original'] or it['title'];author=it['author_original'] or it['author']
 params=urllib.parse.urlencode({'title':qtitle,'author':author,'fields':'title,author_name,first_publish_year,key','limit':3})
 req=urllib.request.Request('https://openlibrary.org/search.json?'+params,headers={'User-Agent':UA})
 try:
  with urllib.request.urlopen(req,timeout=8) as r:data=json.load(r)
 except Exception as e:return {**it,'status':'LOOKUP_ERROR','candidate_year':'','suggested_t':'','confidence':'','ol_title':'','ol_authors':'','ol_key':'','title_similarity':'','author_similarity':'','reason':type(e).__name__}
 best=None;bs=-1
 for d in data.get('docs') or []:
  y=d.get('first_publish_year')
  if not isinstance(y,int):continue
  ts=max(sim(qtitle,d.get('title','')),sim(it['title'],d.get('title','')),sim(it['title_original'],d.get('title','')))
  aus=max([sim(author,a) for a in (d.get('author_name') or [])]+[0.0]);score=.65*ts+.35*aus
  if score>bs:bs=score;best=(d,y,ts,aus)
 if not best:return {**it,'status':'NO_MATCH','candidate_year':'','suggested_t':'','confidence':'','ol_title':'','ol_authors':'','ol_key':'','title_similarity':'','author_similarity':'','reason':'no result with first_publish_year'}
 d,y,ts,aus=best
 conf='HIGH' if ts>=.96 and aus>=.88 else 'MEDIUM' if ts>=.88 and aus>=.75 else 'LOW'
 return {**it,'status':'CANDIDATE_BOUNDARY' if y in BOUNDARIES else 'CANDIDATE','candidate_year':str(y),'suggested_t':tyear(y),'confidence':conf,'ol_title':d.get('title',''),'ol_authors':';'.join(d.get('author_name') or []),'ol_key':d.get('key',''),'title_similarity':f'{ts:.3f}','author_similarity':f'{aus:.3f}','reason':'Open Library first_publish_year candidate'}
def main():
 if not MARKER.exists():raise SystemExit('priority V2 marker missing')
 items=[]
 for p in sorted(ROOT.glob('*.md'),key=lambda p:p.name.casefold()):
  x=fm(p.read_text(encoding='utf-8-sig'))
  if not x or scalar(x,'type')!='work' or lst(x,'axis_t') or re.search(r'-?\d{1,4}',scalar(x,'year')):continue
  title=scalar(x,'title') or p.stem;author=scalar(x,'author');tr=tier(x,title,author)
  if tr not in {'P1_CANON_AWARD','P2_EXTERNAL_MATCH_FRIENDLY'}:continue
  items.append({'tier':tr,'file':p.name,'id':scalar(x,'id'),'title':title,'title_original':scalar(x,'title_original'),'author':author,'author_original':scalar(x,'author_original'),'canon_id':scalar(x,'canon_id'),'awards':';'.join(lst(x,'awards'))})
 rows=[]
 with ThreadPoolExecutor(max_workers=12) as ex:
  futs=[ex.submit(resolve,it) for it in items]
  for i,f in enumerate(as_completed(futs),1):
   rows.append(f.result())
   if i%100==0:print(i,len(items))
 rows.sort(key=lambda r:r['file'].casefold());fields=list(rows[0].keys()) if rows else []
 high=[r for r in rows if r['status']=='CANDIDATE' and r['confidence']=='HIGH'];review=[r for r in rows if r not in high]
 for name,subset in [('openlibrary_priority_v2.csv',rows),('openlibrary_priority_high_v2.csv',high),('openlibrary_priority_review_v2.csv',review)]:
  with (OUT/name).open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(subset)
 p1=[r for r in high if r['tier']=='P1_CANON_AWARD'];p2=[r for r in high if r['tier']=='P2_EXTERNAL_MATCH_FRIENDLY']
 md=['# Open Library Priority Missing-T Candidate Audit V2','',f'- Priority works queried: **{len(items)}**',f'- HIGH non-boundary candidates: **{len(high)}**',f'  - P1 canon/award: **{len(p1)}**',f'  - P2 external-match-friendly: **{len(p2)}**',f'- Review/unresolved: **{len(review)}**','','No Work mutation is performed. HIGH remains a candidate until special-case and plausibility gates pass.','','`OPENLIBRARY_PRIORITY_V2 = AUDITED_READ_ONLY`','']
 (OUT/'OPENLIBRARY_PRIORITY_V2.md').write_text('\n'.join(md),encoding='utf-8',newline='\n');MARKER.unlink();print(len(high),len(review))
if __name__=='__main__':main()
