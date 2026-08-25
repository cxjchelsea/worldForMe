from pathlib import Path
import csv
p=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis_year_backfill/REPRINT_BATCH1_V1.csv')
out=p.with_suffix('.list.md')
rows=list(csv.DictReader(p.open('r',encoding='utf-8-sig',newline='')))
lines=['# Reprint Batch 1 Research List','']
for i,r in enumerate(rows,1):
    lines.append(f"{i}. `{r['file']}` | `{r['id']}` | **{r['title']}** | {r['author_original'] or r['author']} | OL={r['ol_year']} | candidate {r['suggested_t']}")
out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(len(rows))
