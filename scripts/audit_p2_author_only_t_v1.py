from pathlib import Path
import csv,re,time,json,urllib.parse,urllib.request,unicodedata
from difflib import SequenceMatcher
from datetime import date

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
AUDIT=ROOT/'_audit/t_axis_completeness'
SAFE_IN=AUDIT/'p2_openlibrary_deep_safe_v1.csv'
REVIEW_IN=AUDIT/'p2_openlibrary_deep_review_v1.csv'
OUT_SAFE=AUDIT/'p2_author_only_t_safe_v1.csv'
OUT_REVIEW=AUDIT/'p2_author_only_t_review_v1.csv'
REPORT=AUDIT/'P2_AUTHOR_ONLY_T_V1.md'
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


def norm(s):
    s=unicodedata.normalize('NFKD',str(s or '')).casefold()
    return ''.join(ch for ch in s if ch.isalnum())


def sim(a,b):
    a=norm(a); b=norm(b)
    if not a or not b:return 0.0
    if a==b:return 1.0
    return SequenceMatcher(None,a,b).ratio()


def year_from_date(s):
    if not s:return None
    m=YEAR_RE.search(str(s))
    return int(m.group(1)) if m else None


def get_json(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=12) as r:
        return json.loads(r.read().decode('utf-8'))


def resolve_author(name):
    # Multiple-author/collective strings are deliberately excluded.
    if not name or any(sep in name for sep in [' / ',';',' & ',' and ']):
        return None,'MULTI_OR_EMPTY'
    q=urllib.parse.urlencode({'q':name,'limit':5})
    try:
        data=get_json('https://openlibrary.org/search/authors.json?'+q)
    except Exception as e:
        return None,'API:'+type(e).__name__
    best=None; best_score=0.0
    for d in data.get('docs',[]):
        names=[d.get('name','')]+list(d.get('alternate_names') or [])
        score=max([sim(name,n) for n in names] or [0])
        if score>best_score:
            best_score=score;best=d
    if not best or best_score<0.92:
        return None,f'NO_STRONG_MATCH:{best_score:.3f}'
    birth=year_from_date(best.get('birth_date'))
    death=year_from_date(best.get('death_date'))
    return {'matched_name':best.get('name',''),'score':best_score,'birth':birth,'death':death,'key':best.get('key','')},'OK'


def classify(r):
    author=r.get('author_original') or r.get('author') or ''
    a,status=resolve_author(author)
    if not a:
        return None,status
    if not a['birth']:
        return None,'NO_BIRTH'
    start=a['birth']+15
    end=a['death'] if a['death'] else CURRENT_YEAR
    st=t_of(start); et=t_of(end)
    if st!=et:
        return None,f'ACTIVE_RANGE_SPANS_T:{start}-{end}:{st}-{et}'
    return {'proven_t':st,'active_start':start,'active_end':end,**a},'SAFE_T_AUTHOR_RANGE'

rows=[]
for p in [SAFE_IN,REVIEW_IN]:
    if p.exists():
        with p.open(encoding='utf-8-sig',newline='') as f: rows.extend(csv.DictReader(f))
# de-duplicate by canonical Work id/file
uniq={}
for r in rows: uniq[(r.get('id',''),r.get('file',''))]=dict(r)
rows=list(uniq.values())

safe=[];review=[]
for i,r in enumerate(rows,1):
    info,status=classify(r)
    x=dict(r);x['author_only_status']=status
    if info:
        x.update({
            'author_only_proven_t':info['proven_t'],'author_active_start':info['active_start'],'author_active_end':info['active_end'],
            'author_match_name':info['matched_name'],'author_match_score':f"{info['score']:.3f}",'author_birth_year':info['birth'] or '',
            'author_death_year':info['death'] or '','author_key':info['key']})
        safe.append(x)
    else:
        review.append(x)
    if i%25==0: print(i,len(safe),len(review),flush=True)
    time.sleep(0.04)
fields=[]
for r in safe+review:
    for k in r:
        if k not in fields: fields.append(k)
for path,data in [(OUT_SAFE,safe),(OUT_REVIEW,review)]:
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
REPORT.write_text('# P2 Author-only T Inference V1\n\n> Read-only. A T coordinate is accepted only when a strongly matched author identity has a possible composition interval (birth+15 through death/current year) wholly inside one frozen T interval. No publication year is inferred.\n\n'+f'- P2 population inspected: **{len(rows)}**\n- SAFE_T_AUTHOR_RANGE: **{len(safe)}**\n- REVIEW: **{len(review)}**\n\nNo Work files were mutated.\n\n`P2_AUTHOR_ONLY_T_V1 = AUDITED_READ_ONLY`\n',encoding='utf-8')
print({'population':len(rows),'safe_t':len(safe),'review':len(review)})
