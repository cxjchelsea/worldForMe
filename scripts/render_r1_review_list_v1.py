from pathlib import Path
import csv

SRC=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_r1/r1_works_v1.csv')
OUT=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_r1/R1_REVIEW_LIST_V1.md')
rows=list(csv.DictReader(SRC.open(encoding='utf-8-sig')))
lines=['# R1 Existing Works Semantic Review List V1','',f'- Population: **{len(rows)}**','']
for i,r in enumerate(rows,1):
    lines.append(f"{i}. `{r['id']}` | **{r['title']}** | {r['author']} | year={r['year'] or '—'} | T={r['axis_t'] or '—'} | canon={r['canon_id'] or '—'} | verify={r['verification_status'] or '—'}")
OUT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(f'RENDERED={len(rows)}')
