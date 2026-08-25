from __future__ import annotations

import csv
import json
import re
import unicodedata
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学")
AUDIT = ROOT / "_audit/t_axis_completeness"
TRIAGE = AUDIT / "missing_t_triage_v1.csv"
OUT = AUDIT / "p2_openlibrary_deep_v1.csv"
SAFE = AUDIT / "p2_openlibrary_deep_safe_v1.csv"
REVIEW = AUDIT / "p2_openlibrary_deep_review_v1.csv"
REPORT = AUDIT / "P2_OPENLIBRARY_DEEP_V1.md"
BOUNDARIES = {500,1500,1800,1890,1945,1980}
UA = "worldForMe-literature-audit/1.0"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.casefold().replace("／", "/")
    s = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def sim(a,b):
    a,b=norm(a),norm(b)
    if not a or not b:return 0.0
    if a==b:return 1.0
    return SequenceMatcher(None,a,b).ratio()


def t_for_year(y:int|None)->str:
    if y is None:return ""
    if y<500:return "T0"
    if y<1500:return "T1"
    if y<1800:return "T2"
    if y<1890:return "T3"
    if y<1945:return "T4"
    if y<1980:return "T5"
    return "T6"


def query(row):
    title=row.get("title_original") or row.get("title") or ""
    author=row.get("author_original") or row.get("author") or ""
    params={"title":title,"author":author,"limit":20,"fields":"key,title,author_name,first_publish_year,publish_year,edition_count"}
    url="https://openlibrary.org/search.json?"+urllib.parse.urlencode(params)
    try:
        req=urllib.request.Request(url,headers={"User-Agent":UA})
        with urllib.request.urlopen(req,timeout=15) as resp:data=json.load(resp)
    except Exception as e:
        return {"deep_status":"ERROR","deep_error":type(e).__name__}
    matches=[]
    for d in data.get("docs",[]):
        dt=d.get("title","")
        da="; ".join(d.get("author_name") or [])
        ts=max(sim(title,dt),sim(row.get("title",""),dt))
        aus=sim(author,da) if author else 0.0
        if ts<0.90 or aus<0.78:continue
        years=[]
        for y in d.get("publish_year") or []:
            try:
                yi=int(y)
                if 500 <= yi <= 2026: years.append(yi)
            except: pass
        try:
            fp=int(d.get("first_publish_year")) if d.get("first_publish_year") is not None else None
        except: fp=None
        if fp and 500<=fp<=2026: years.append(fp)
        if not years:continue
        earliest=min(years)
        matches.append((ts+aus, earliest, fp or earliest, dt, da, d.get("key",""), len(set(years)), min(years), max(years)))
    if not matches:return {"deep_status":"NO_RELIABLE_MATCH"}
    # strongest title+author match, then earliest bibliographic evidence
    matches.sort(key=lambda x:(-x[0],x[1]))
    score, earliest, fp, dt, da, key, ny, ymin, ymax=matches[0]
    et=t_for_year(earliest); ft=t_for_year(fp)
    status="STABLE_T" if et==ft and earliest not in BOUNDARIES and fp not in BOUNDARIES else "INTERNAL_CONFLICT"
    return {
        "deep_status":status,"deep_earliest_year":str(earliest),"deep_earliest_t":et,
        "deep_first_publish_year":str(fp),"deep_first_publish_t":ft,
        "deep_title":dt,"deep_authors":da,"deep_key":key,
        "deep_year_count":str(ny),"deep_year_min":str(ymin),"deep_year_max":str(ymax),
        "deep_match_score":f"{score:.3f}",
    }


def main():
    with TRIAGE.open(encoding="utf-8-sig",newline="") as f:
        rows=[r for r in csv.DictReader(f) if r.get("tier")=="P2_EXTERNAL_MATCH_FRIENDLY"]
    m={}
    with ThreadPoolExecutor(max_workers=8) as ex:
        fs={ex.submit(query,r):r for r in rows}
        for i,fu in enumerate(as_completed(fs),1):
            r=fs[fu]
            try:m[r["id"]]=fu.result()
            except Exception as e:m[r["id"]]={"deep_status":"ERROR","deep_error":type(e).__name__}
            if i%50==0:print(f"deep_done={i}/{len(rows)}",flush=True)
    out=[];safe=[];review=[]
    for r in rows:
        d=m.get(r["id"],{})
        status="SAFE_T" if d.get("deep_status")=="STABLE_T" else "REVIEW"
        merged=dict(r);merged.update(d);merged["resolution_status"]=status
        merged["chosen_t"]=d.get("deep_earliest_t","") if status=="SAFE_T" else ""
        merged["canonical_year_candidate"]=d.get("deep_earliest_year","") if status=="SAFE_T" else ""
        if status=="SAFE_T":
            merged["resolution_reason"]="强标题+作者匹配；最早版次年份与 first_publish_year 落在同一 T"
            safe.append(merged)
        else:
            merged["resolution_reason"]="无可靠深层匹配或版次年份与 first_publish_year 的 T 区间不稳定"
            review.append(merged)
        out.append(merged)
    fields=list(dict.fromkeys(k for r in out for k in r.keys()))
    for p,rr in [(OUT,out),(SAFE,safe),(REVIEW,review)]:
        with p.open("w",encoding="utf-8-sig",newline="") as f:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rr)
    lines=["# P2 Open Library Deep Edition-Year Audit V1","",
           "> Read-only. Uses exact title/author matching plus edition-year evidence within Open Library; no Work mutation occurs here.","",
           f"- P2 population: **{len(rows)}**",f"- SAFE_T: **{len(safe)}**",f"- REVIEW: **{len(review)}**","",
           "## Safe rule","",
           "A row is SAFE only when title+author match is strong and the earliest observed edition year and `first_publish_year` fall in the same frozen T interval. Exact boundary years are blocked.","",
           "`P2_OPENLIBRARY_DEEP_V1 = AUDITED_READ_ONLY`",""]
    REPORT.write_text("\n".join(lines),encoding="utf-8")
    print(f"p2={len(rows)} safe={len(safe)} review={len(review)}")

if __name__=="__main__":main()
