from pathlib import Path
import csv
SRC=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_r1/r1_works_v1.csv')
OUT=Path('个人通识知识系统_v2_A2/30 世界文学/_audit/r_axis_r1')
rows=list(csv.DictReader(SRC.open(encoding='utf-8-sig')))
for n,(a,b) in enumerate(((0,40),(40,81)),1):
    lines=[f'# R1 Review Chunk {n}','']
    for i,r in enumerate(rows[a:b],a+1):
        lines.append(f"{i}. {r['id']} | {r['title']} | {r['title_original'] or '-'} | {r['author']} | {r['author_original'] or '-'} | {r['year'] or '-'} | {r['axis_t'] or '-'} | {r['canon_id'] or '-'}")
    (OUT/f'R1_REVIEW_CHUNK_{n}.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('DONE')
