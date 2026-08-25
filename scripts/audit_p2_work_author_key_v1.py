from pathlib import Path
import csv,json,re,time,urllib.request
from datetime import date

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
AUDIT=ROOT/'_audit/t_axis_completeness'
IN=AUDIT/'p2_residual_review_v1.csv'
OUT_SAFE=AUDIT/'p2_work_author_key_safe_v1.csv'
OUT_REVIEW=AUDIT/'p2_work_author_key_review_v1.csv'
REPORT=AUDIT/'P2_WORK_AUTHOR_KEY_V1.md'
MARKER=AUDIT/'RUN_P2_WORK_AUTHOR_KEY_V1'
UA={'User-Agent':'worldForMe-literature-audit/1.0'}
YEAR_RE=re.compile(r'(1[0-9]{3}|20[0-2][0-9])')
CURRENT_YEAR=date.today().year

def t_of(y):
    if y<500:return 'T0'
    if y<1500:return 'T1'
    if y<1800:return 'T2'
    if y<1890:return 'T3'
    if y<1945:return 'T4'
    if y<1980:return 'T5'
    return 'T6'

def year(s):
    m=YEAR_RE.search(str(s or '')); return int(m.group(1)) if m else None

def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=12) as r:return json.loads(r.read().decode('utf-8'))

def author_keys_from_work(key):
    if not key or not key.startswith('/works/'):return []
    try:d=get('https://openlibrary.org'+key+'.json')
    except Exception:return []
    out=[]
    for a in d.get('authors') or []:
        ak=(a.get('author') or {}).get('key') if isinstance(a,dict) else None
        if ak:out.append(ak)
    return out

def classify(r):
    key=r.get('deep_key','')
    aks=author_keys_from_work(key)
    if len(aks)!=1:return None,'NO_SINGLE_WORK_AUTHOR_KEY'
    try:a=get('https://openlibrary.org'+aks[0]+'.json')
    except Exception as e:return None,'AUTHOR_FETCH_ERROR:'+type(e).__name__
    by=year(a.get('birth_date'));dy=year(a.get('death_date'))
    if not by:return None,'AUTHOR_BIRTH_MISSING'
    start=by+15;end=dy or CURRENT_YEAR
    st,et=t_of(start),t_of(end)
    if st!=et:return None,f'AUTHOR_RANGE_SPANS_T:{start}-{end}:{st}-{et}'
    return {'proven_t':st,'author_key_direct':aks[0],'author_name_direct':a.get('name',''),'birth':by,'death':dy or '','active_start':start,'active_end':end},'SAFE_T_DIRECT_WORK_AUTHOR'

rows=list(csv.DictReader(IN.open(encoding='utf-8-sig',newline='')))
# Only rows with a reliable matched work key can benefit from this audit.
rows=[r for r in rows if (r.get('deep_key') or '').startswith('/works/')]
safe=[];review=[]
for i,r in enumerate(rows,1):
    info,status=classify(r);x=dict(r);x['work_author_key_status']=status
    if info:
        x.update(info);safe.append(x)
    else:review.append(x)
    if i%25==0:print(i,len(safe),len(review),flush=True)
    time.sleep(0.04)
fields=[]
for r in safe+review:
    for k in r:
        if k not in fields:fields.append(k)
for p,data in [(OUT_SAFE,safe),(OUT_REVIEW,review)]:
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
REPORT.write_text('# P2 Direct Work→Author Audit V1\n\n> Read-only. Uses the already matched Open Library Work key to follow its explicit author entity, avoiding a second fuzzy author-name search. T is accepted only when that author\'s possible composition interval lies wholly within one frozen T interval.\n\n'+f'- Residual rows with matched Work key inspected: **{len(rows)}**\n- SAFE_T_DIRECT_WORK_AUTHOR: **{len(safe)}**\n- REVIEW: **{len(review)}**\n\nNo Work files were mutated.\n\n`P2_WORK_AUTHOR_KEY_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8')
MARKER.unlink()
print({'inspected':len(rows),'safe':len(safe),'review':len(review)})
