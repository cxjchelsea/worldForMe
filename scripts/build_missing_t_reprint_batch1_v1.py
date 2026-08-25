from pathlib import Path
import csv

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis_year_backfill')
SRC = ROOT / 'missing_t_year_research_v1.csv'
OUT = ROOT / 'REPRINT_BATCH1_V1.csv'
REPORT = ROOT / 'REPRINT_BATCH1_V1.md'

rows = []
with SRC.open('r', encoding='utf-8-sig', newline='') as f:
    for r in csv.DictReader(f):
        if (r.get('review_status') or '').strip() == 'REPRINT_RISK_REVIEW':
            rows.append(r)

batch = rows[:50]
fields = [
    'file','id','title','title_original','author','author_original',
    'ol_year','ol_title','ol_author','ol_key','suggested_t',
    'publication_year','year_source_1','confidence','review_status','notes'
]
with OUT.open('w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for r in batch:
        w.writerow({k:r.get(k,'') for k in fields})

REPORT.write_text(
    '# Missing-T Reprint Risk Batch 1 V1\n\n'
    f'- Total REPRINT_RISK_REVIEW population: **{len(rows)}**\n'
    f'- Frozen batch size: **{len(batch)}**\n'
    '- Selection: first 50 rows in the stable research CSV order.\n'
    '- Read-only freeze; no Work file modified.\n\n'
    '`MISSING_T_REPRINT_BATCH1_V1 = FROZEN_READ_ONLY`\n',
    encoding='utf-8'
)
print({'total_reprint_risk': len(rows), 'batch1': len(batch)})
