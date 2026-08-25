from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT=Path("个人通识知识系统_v2_A2/30 世界文学/40 作品")
OUT=Path("个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis_completeness")
MARKER=OUT/"RUN_MISSING_T_TRIAGE_V1"
SPECIAL=re.compile(r"(全集|文集|选集|诗选|短篇小说集|故事集|传说|神话|史诗|往世书|歌谣|民谣|口传|作品集)")


def fm(text):
    m=re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)",text,re.S); return m.group(1) if m else ""
def scalar(x,k):
    m=re.search(rf"(?m)^{re.escape(k)}:\s*(.*?)\s*$",x)
    if not m:return ""
    v=m.group(1).strip().strip("\"'")
    return "" if v.lower() in {"null","none","~"} else v
def lst(x,k):
    lines=x.splitlines()
    for i,line in enumerate(lines):
        if re.match(rf"^{re.escape(k)}:\s*\[\s*\]\s*$",line):return []
        if re.match(rf"^{re.escape(k)}:\s*$",line):
            out=[]
            for n in lines[i+1:]:
                m=re.match(r"^\s*-\s*(.*?)\s*$",n)
                if m:out.append(m.group(1).strip().strip("\"'"));continue
                if re.match(r"^[A-Za-z0-9_\u4e00-\u9fff].*?:",n):break
                if n.strip() and not n.startswith((" ","\t")):break
            return out
    return []
def source_keys(x):return [m.group(1) for m in re.finditer(r"(?m)^([A-Za-z0-9_]+_source_refs):\s*$",x)]

def main():
    if not MARKER.exists():raise SystemExit("triage marker missing")
    rows=[]; counts=Counter(); src=Counter()
    for p in sorted(ROOT.glob("*.md"),key=lambda p:p.name.casefold()):
        x=fm(p.read_text(encoding="utf-8-sig"))
        if not x or scalar(x,"type")!="work" or lst(x,"axis_t"):continue
        title=scalar(x,"title") or p.stem; author=scalar(x,"author")
        special=bool(SPECIAL.search(title)) or author in {"佚名","匿名","民间","口传传统"} or bool(lst(x,"literary_traditions"))
        canon=bool(scalar(x,"canon_id")); awards=lst(x,"awards")
        if special: tier="S_SPECIAL_TEXT"
        elif canon or awards: tier="P1_CANON_AWARD"
        elif scalar(x,"author_original") and (scalar(x,"title_original") or not any('\u4e00'<=c<='\u9fff' for c in title)): tier="P2_EXTERNAL_MATCH_FRIENDLY"
        else: tier="P3_GENERAL_REVIEW"
        counts[tier]+=1
        for k in source_keys(x):src[k]+=1
        rows.append({"tier":tier,"file":p.name,"id":scalar(x,"id"),"title":title,"title_original":scalar(x,"title_original"),"author":author,"author_original":scalar(x,"author_original"),"canon_id":scalar(x,"canon_id"),"awards":";".join(awards),"source_ref_keys":";".join(source_keys(x)),"topics":";".join(lst(x,"topics"))})
    fields=list(rows[0].keys()) if rows else []
    with (OUT/"missing_t_triage_v1.csv").open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    md=["# Missing-T Triage V1","",f"- Total missing-T works: **{len(rows)}**",""]
    for k in ["P1_CANON_AWARD","P2_EXTERNAL_MATCH_FRIENDLY","P3_GENERAL_REVIEW","S_SPECIAL_TEXT"]:md.append(f"- {k}: **{counts[k]}**")
    md += ["","## Source batches",""]+[f"- {k}: **{v}**" for k,v in src.most_common()]
    md += ["","`MISSING_T_TRIAGE_V1 = COMPLETE_READ_ONLY`",""]
    (OUT/"TRIAGE_V1.md").write_text("\n".join(md),encoding="utf-8",newline="\n")
    MARKER.unlink()
    print(dict(counts))
if __name__=="__main__":main()
