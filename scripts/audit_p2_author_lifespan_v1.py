from pathlib import Path
import csv,re,time,json,urllib.parse,urllib.request
from datetime import date

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_openlibrary_deep_safe_v1.csv'
OUT_SAFE=AUDIT/'p2_author_lifespan_safe_v1.csv'
OUT_REVIEW=AUDIT/'p2_author_lifespan_review_v1.csv'
REPORT=AUDIT/'P2_AUTHOR_LIFESPAN_V1.md'
UA={'User-Agent':'worldForMe-literature-audit/1.0'}
YEAR_RE=re.compile(r'(1[0-9]{3}|20[0-2][0-9])')
CURRENT_YEAR=date.today().year


def t_of(y:int):
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'


def get_json(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=12) as r:
        return json.loads(r.read().decode('utf-8'))


def year_from_date(s):
    if not s:return None
    m=YEAR_RE.search(str(s))
    return int(m.group(1)) if m else None


def classify(row):
    title=row.get('deep_title') or row.get('title') or ''
    author=row.get('author_original') or row.get('author') or ''
    candidate_t=row.get('chosen_t') or ''
    q=urllib.parse.urlencode({'title':title,'author':author,'limit':5,'fields':'title,author_name,author_key,first_publish_year'})
    try:
        data=get_json('https://openlibrary.org/search.json?'+q)
    except Exception as e:
        return 'REVIEW_API', '', '', '', str(e)
    best=None
    for d in data.get('docs',[]):
        if d.get('author_key'):
            best=d; break
    if not best:
        return 'REVIEW_NO_AUTHOR_KEY','','','', ''
    deaths=[]; births=[]
    for ak in best.get('author_key',[])[:3]:
        try:
            a=get_json(f'https://openlibrary.org/authors/{ak}.json')
            by=year_from_date(a.get('birth_date')); dy=year_from_date(a.get('death_date'))
            if by: births.append(by)
            if dy: deaths.append(dy)
            time.sleep(0.03)
        except Exception:
            pass
    birth=min(births) if births else None
    death=max(deaths) if deaths else None
    if not birth:
        return 'REVIEW_NO_BIRTH', '', str(death or ''), '', 'author birth year unavailable'
    active_start=birth+15
    active_end=death if death else CURRENT_YEAR
    start_t=t_of(active_start); end_t=t_of(active_end)
    if start_t==end_t and start_t==candidate_t:
        return 'SAFE_T_LIFESPAN_RANGE',str(birth),str(death or ''),start_t,'author possible composition interval lies wholly inside candidate T'
    return 'REVIEW_LIFESPAN_SPANS_T',str(birth),str(death or ''),'',f'possible composition interval {active_start}-{active_end} spans {start_t}..{end_t}'


rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
safe=[]; review=[]
for i,r in enumerate(rows,1):
    status,birth,death,proven_t,reason=classify(r)
    x=dict(r); x.update({'lifespan_status':status,'author_birth_year':birth,'author_death_year':death,'lifespan_proven_t':proven_t,'lifespan_reason':reason})
    (safe if status=='SAFE_T_LIFESPAN_RANGE' else review).append(x)
    if i%25==0: print(i,len(safe),len(review),flush=True)
    time.sleep(0.04)
fields=list((safe or review or [{}])[0].keys())
for path,data in [(OUT_SAFE,safe),(OUT_REVIEW,review)]:
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(data)
REPORT.write_text('# P2 Author Lifespan T-Interval Gate V1\n\n> Read-only. This audit does not infer an exact publication year. It only accepts a T coordinate when the author\'s possible composition interval (birth+15 through death/current year) lies wholly within one frozen T interval, and that interval agrees with the deep bibliographic candidate.\n\n'+f'- Input deep-safe candidates: **{len(rows)}**\n- SAFE_T_LIFESPAN_RANGE: **{len(safe)}**\n- REVIEW: **{len(review)}**\n\nNo Work files were mutated.\n\n`P2_AUTHOR_LIFESPAN_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8')
print({'safe_t':len(safe),'review':len(review)})
