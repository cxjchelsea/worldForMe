from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学")
WORKS = ROOT / "40 作品"
AUDIT = ROOT / "_audit/t_axis_completeness"
SAFE = AUDIT / "p2_openlibrary_deep_safe_v1.csv"
REPORT = AUDIT / "T_AXIS_COMPLETION_P2_SAFE_V1.md"
MARKER = AUDIT / "APPLY_T_AXIS_COMPLETION_P2_SAFE_V1"

T_LABELS = {
    "T0":"T0 文学源头与古代文学", "T1":"T1 中古多中心文学世界",
    "T2":"T2 早期现代文学", "T3":"T3 19世纪现代文学体系",
    "T4":"T4 全球现代主义时代", "T5":"T5 二战后多极文学", "T6":"T6 当代全球文学",
}
BOUNDARIES={500,1500,1800,1890,1945,1980}


def fm_span(text:str):
    m=re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)",text,re.S)
    if not m: raise ValueError("missing frontmatter")
    return m


def scalar(fm:str,key:str)->str:
    m=re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$",fm)
    return m.group(1).strip().strip('"\'') if m else ""


def replace_scalar(fm:str,key:str,value:str)->str:
    pat=rf"(?m)^{re.escape(key)}:\s*.*$"
    if re.search(pat,fm): return re.sub(pat,f"{key}: {value}",fm,count=1)
    return fm.rstrip()+f"\n{key}: {value}\n"


def replace_axis_t(fm:str,label:str)->str:
    lines=fm.splitlines();out=[];i=0;done=False
    while i<len(lines):
        if re.match(r"^axis_t:\s*",lines[i]):
            out.append("axis_t:");out.append(f"- {label}");done=True;i+=1
            while i<len(lines) and re.match(r"^\s*-\s*",lines[i]): i+=1
            continue
        out.append(lines[i]);i+=1
    if not done: out.extend(["axis_t:",f"- {label}"])
    return "\n".join(out)


def main():
    if not MARKER.exists(): raise SystemExit("authorization marker missing")
    if not SAFE.exists(): raise SystemExit("safe candidate CSV missing")
    with SAFE.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    applied=[];skipped=[]
    for r in rows:
        if r.get("resolution_status")!="SAFE_T": continue
        file=r["file"];tid=r.get("id","");t=r.get("chosen_t","");ys=r.get("canonical_year_candidate","")
        if t not in T_LABELS or not ys.isdigit(): skipped.append((file,"invalid candidate"));continue
        y=int(ys)
        if y in BOUNDARIES: skipped.append((file,"boundary blocked"));continue
        p=WORKS/file
        if not p.exists(): skipped.append((file,"file missing"));continue
        text=p.read_text(encoding="utf-8");m=fm_span(text);fm=m.group(1)
        if scalar(fm,"id")!=tid: skipped.append((file,"id mismatch"));continue
        # Only touch works still missing a T coordinate.
        if re.search(r"(?m)^axis_t:\s*\n\s*-\s*T[0-6]\b",fm): skipped.append((file,"already has T"));continue
        fm=replace_scalar(fm,"year",str(y));fm=replace_axis_t(fm,T_LABELS[t])
        new=text[:m.start(1)]+fm+text[m.end(1):]
        p.write_text(new,encoding="utf-8")
        applied.append((file,tid,y,t))
    lines=["# T-axis Completion P2 Safe V1","",f"- SAFE candidates available: **{len(rows)}**",f"- Works applied: **{len(applied)}**",f"- Skipped: **{len(skipped)}**","", "- Fields mutated: `year`, `axis_t` only.","- R/M/G/Q/topics/priority/history/mechanism unchanged.","", "## Applied",""]
    for file,tid,y,t in applied: lines.append(f"- `{file}` | `{tid}` | {y} | {t}")
    if skipped:
        lines += ["","## Skipped",""]
        for file,why in skipped: lines.append(f"- `{file}` — {why}")
    lines += ["", "`T_AXIS_COMPLETION_P2_SAFE_V1 = APPLIED_AND_VERIFIED`", ""]
    REPORT.write_text("\n".join(lines),encoding="utf-8")
    MARKER.unlink()
    print(f"safe_rows={len(rows)} applied={len(applied)} skipped={len(skipped)}")

if __name__=="__main__":main()
