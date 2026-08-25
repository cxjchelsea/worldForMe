from pathlib import Path
import csv,re,time,json,urllib.parse,urllib.request

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_openlibrary_deep_safe_v1.csv'
OUT_SAFE=AUDIT/'p2_author_lifespan_safe_v1.csv'
OUT_REVIEW=AUDIT/'p2_author_lifespan_review_v1.csv'
REPORT=AUDIT/'P2_AUTHOR_LIFESPAN_V1.md'
UA={'User-Agent':'worldForMe-literature-audit/1.0'}
YEAR_RE=re.compile(r'(1[0-9]{3}|20[0-2][0-9])')

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
    y=int(row['canonical_year_candidate'])
    q=urllib.parse.urlencode({'title':title,'author':author,'limit':5,'fields':'title,author_name,author_key,first_publish_year'})
    try:
        data=get_json('https://openlibrary.org/search.json?'+q)
    except Exception as e:
        return 'REVIEW_API', '', '', str(e)
    best=None
    for d in data.get('docs',[]):
        if d.get('author_key'):
            best=d; break
    if not best:
        return 'REVIEW_NO_AUTHOR_KEY','','',''
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
    if birth and y < birth-10:
        return 'REVIEW_PRE_BIRTH',str(birth),str(death or ''),'candidate predates author birth implausibly'
    if death and y > death+15:
        return 'REVIEW_POST_DEATH',str(birth or ''),str(death),'candidate likely late reprint/edition'
    return 'SAFE_LIFESPAN',str(birth or ''),str(death or ''),'no lifespan contradiction'

rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
safe=[]; review=[]
for i,r in enumerate(rows,1):
    status,birth,death,reason=classify(r)
    x=dict(r); x.update({'lifespan_status':status,'author_birth_year':birth,'author_death_year':death,'lifespan_reason':reason})
    (safe if status=='SAFE_LIFESPAN' else review).append(x)
    if i%25==0: print(i,len(safe),len(review),flush=True)
    time.sleep(0.04)
fields=list((safe or review or [{}])[0].keys())
for path,data in [(OUT_SAFE,safe),(OUT_REVIEW,review)]:
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(data)
REPORT.write_text('# P2 Author Lifespan Sanity Gate V1\n\n> Read-only. This gate only rejects bibliographic years that conflict strongly with author lifespan; it never invents a publication year.\n\n'+f'- Input deep-safe candidates: **{len(rows)}**\n- SAFE_LIFESPAN: **{len(safe)}**\n- REVIEW: **{len(review)}**\n\n`P2_AUTHOR_LIFESPAN_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8')
print({'safe':len(safe),'review':len(review)})
