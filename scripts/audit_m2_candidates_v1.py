from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "40 作品"
OUT = ROOT / "reports"
MOVEMENTS = ["浪漫主义", "超验主义", "现实主义", "自然主义", "象征主义", "唯美主义", "颓废主义", "Modernismo"]


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    if not m:
        return ""
    v = m.group(1).strip()
    if v in {"null", "''", '""'}:
        return ""
    return v.strip("'\"")


def list_value(fm: str, key: str) -> list[str]:
    lines = fm.splitlines(); values=[]
    for i, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            inline=line.split(":",1)[1].strip()
            if inline.startswith("[") and inline.endswith("]"):
                return [x.strip().strip("'\"") for x in inline[1:-1].split(",") if x.strip()]
            for nxt in lines[i+1:]:
                if re.match(r"^[A-Za-z0-9_]+:", nxt): break
                m=re.match(r"^\s*-\s+(.*)$", nxt)
                if m: values.append(m.group(1).strip().strip("'\""))
            break
    return values

records=[]
for path in sorted(WORKS.glob("*.md")):
    fm=frontmatter(path.read_text(encoding="utf-8"))
    if not fm: continue
    axis_m=list_value(fm,"axis_m")
    joined=" | ".join(axis_m)
    hits=[m for m in MOVEMENTS if m.lower() in joined.lower()]
    year=scalar(fm,"year")
    try: yi=int(year)
    except: yi=None
    if hits or (yi is not None and 1780 <= yi <= 1905):
        records.append({
            "file": path.name,
            "title": scalar(fm,"title") or path.stem,
            "author": scalar(fm,"author"),
            "year": yi,
            "axis_m": axis_m,
            "movement_hits": hits,
            "topics": list_value(fm,"topics"),
            "axis_r": list_value(fm,"axis_r"),
            "axis_g": list_value(fm,"axis_g"),
        })

movement_counts=Counter(h for r in records for h in r["movement_hits"])
explicit=[r for r in records if r["movement_hits"]]
date_only=[r for r in records if not r["movement_hits"]]
payload={"candidate_count":len(records),"explicit_movement_count":len(explicit),"date_only_count":len(date_only),"movement_counts":dict(movement_counts),"records":records}
OUT.mkdir(exist_ok=True)
(OUT/"m2_candidate_audit.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding="utf-8")
lines=["# M2 候选作品审计","",f"- candidates: **{len(records)}**",f"- explicit movement mapping: **{len(explicit)}**",f"- date-only candidates: **{len(date_only)}**","","## 已有思潮标注","","| movement | works |","|---|---:|"]
for m in MOVEMENTS: lines.append(f"| {m} | {movement_counts.get(m,0)} |")
lines += ["","## 明确已有 M2 思潮标注的作品",""]
for r in explicit: lines.append(f"- {r['title']}｜{r['author']}｜{r['year'] or ''}｜{', '.join(r['movement_hits'])}")
lines += ["","## 仅因年代进入候选池（需人工/结构审计，不能自动归 M2）",""]
for r in date_only: lines.append(f"- {r['title']}｜{r['author']}｜{r['year'] or ''}")
report="\n".join(lines)+"\n"
(OUT/"m2_candidate_audit.md").write_text(report,encoding="utf-8")
print(report)
