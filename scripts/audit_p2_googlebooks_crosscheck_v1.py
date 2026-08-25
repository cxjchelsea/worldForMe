from pathlib import Path
import csv,json,re,unicodedata,urllib.parse,urllib.request
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor,as_completed

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学'); AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_residual_review_v1.csv'; SAFE=AUDIT/'p2_googlebooks_crosscheck_safe_v1.csv'; REVIEW=AUDIT/'p2_googlebooks_crosscheck_review_v1.csv'; REPORT=AUDIT/'P2_GOOGLEBOOKS_CROSSCHECK_V1.md'; MARKER=AUDIT/'RUN_P2_GOOGLEBOOKS_CROSSCHECK_V1'
UA={'User-Agent':'worldForMe-literature-audit/2.2 (bibliographic verification)'}
YEAR_RE=re.compile(r'([12][0-9]{3})'); ACTIVE_RE=re.compile(r'ACTIVE_RANGE_SPANS_T:(\d{3,4})-(\d{3,4}):')
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
    if a==b:return 1.0
    return SequenceMatcher(None,a,b).ratio()
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=15) as r:return json.loads(r.read().decode('utf-8'))
def active_range(r):
    m=ACTIVE_RE.search(r.get('author_only_reason',''))
    return (int(m.group(1)),int(m.group(2))) if m else (None,None)
def verify(r):
    title=r.get('title_original') or r.get('title') or '';author=r.get('author_original') or r.get('author') or ''
    ol_t=r.get('chosen_t') or r.get('deep_earliest_t') or ''
    lo,hi=active_range(r)
    if not lo or not hi or not ol_t:return dict(r,gb_status='REVIEW_MISSING_GATE_INPUT')
    q=urllib.parse.urlencode({'q':f'intitle:"{title}" inauthor:"{author}"','maxResults':20,'printType':'books','projection':'lite'})
    try:data=get('https://www.googleapis.com/books/v1/volumes?'+q)
    except Exception as e:return dict(r,gb_status='API_ERROR',gb_error=type(e).__name__)
    matches=[]
    for item in data.get('items',[]) or []:
        info=item.get('volumeInfo') or {};gt=info.get('title','');authors=info.get('authors') or []
        ts=sim(title,gt);asc=max([sim(author,a) for a in authors] or [0])
        if ts<0.90 or asc<0.88:continue
        m=YEAR_RE.search(str(info.get('publishedDate','')))
        if not m:continue
        y=int(m.group(1));matches.append((y,ts,asc,gt,';'.join(authors),item.get('id','')))
    if not matches:return dict(r,gb_status='REVIEW_NO_STRONG_GOOGLEBOOK_MATCH')
    years=sorted(set(x[0] for x in matches));earliest=years[0];gt=t_of(earliest)
    if earliest in BOUND:return dict(r,gb_status='REVIEW_BOUNDARY_YEAR',gb_earliest_year=str(earliest))
    if earliest<lo or earliest>hi:return dict(r,gb_status='REVIEW_DATE_OUTSIDE_AUTHOR_RANGE',gb_earliest_year=str(earliest),gb_author_active=f'{lo}-{hi}')
    if gt!=ol_t:return dict(r,gb_status='REVIEW_CROSS_SOURCE_T_DISAGREE',gb_earliest_year=str(earliest),gb_proven_t=gt,gb_ol_t=ol_t,gb_years=';'.join(map(str,years)))
    # Require at least one exact or near-exact title+author hit; choose strongest row for audit trail.
    matches.sort(key=lambda x:(x[1]+x[2],-x[0]),reverse=True);best=matches[0]
    return dict(r,gb_status='SAFE_T_GOOGLEBOOKS_CROSSCHECK',gb_proven_t=gt,gb_earliest_year=str(earliest),gb_years=';'.join(map(str,years)),gb_title_match=best[3],gb_authors=best[4],gb_title_score=f'{best[1]:.3f}',gb_author_score=f'{best[2]:.3f}',gb_volume_id=best[5],gb_author_active=f'{lo}-{hi}',gb_ol_t=ol_t)
def main():
    if not MARKER.exists():raise SystemExit('authorization marker missing')
    rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')));rows=[r for r in rows if r.get('residual_bucket')=='AUTHOR_RANGE_SPANS_T']
    res=[]
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs={ex.submit(verify,r):r for r in rows}
        for i,f in enumerate(as_completed(futs),1):
            try:res.append(f.result())
            except Exception as e:res.append(dict(futs[f],gb_status='ERROR',gb_error=type(e).__name__))
            if i%20==0:print(i,flush=True)
    safe=[r for r in res if r.get('gb_status')=='SAFE_T_GOOGLEBOOKS_CROSSCHECK'];review=[r for r in res if r.get('gb_status')!='SAFE_T_GOOGLEBOOKS_CROSSCHECK']
    fields=[]
    for r in safe+review:
        for k in r:
            if k not in fields:fields.append(k)
    for p,data in [(SAFE,safe),(REVIEW,review)]:
        with p.open('w',encoding='utf-8-sig',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
    disag=sum(1 for r in review if r.get('gb_status')=='REVIEW_CROSS_SOURCE_T_DISAGREE')
    REPORT.write_text('# P2 Google Books Cross-check V1\n\n> Read-only. Scope: residual `AUTHOR_RANGE_SPANS_T`. A T is accepted only when a strong Google Books title+author match has an earliest publication year inside the author possible composition interval and its T agrees with the already matched Open Library deep candidate T.\n\n'+f'- Input AUTHOR_RANGE_SPANS_T: **{len(rows)}**\n- SAFE_T_GOOGLEBOOKS_CROSSCHECK: **{len(safe)}**\n- Cross-source T disagreements blocked: **{disag}**\n- REVIEW: **{len(review)}**\n\nNo Work files were mutated.\n\n`P2_GOOGLEBOOKS_CROSSCHECK_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8');MARKER.unlink();print({'input':len(rows),'safe':len(safe),'disagree':disag,'review':len(review)})
if __name__=='__main__':main()
