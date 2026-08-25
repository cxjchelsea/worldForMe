import csv
from pathlib import Path

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis')
SRC = ROOT / 'semantic_stage1_all.csv'

with SRC.open('r', encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))

for status, name in [('MOVE_CANDIDATE', 'semantic_stage1_move.csv'), ('BOUNDARY', 'semantic_stage1_boundary.csv')]:
    subset = [r for r in rows if r.get('status') == status]
    fields = list(rows[0].keys()) if rows else []
    with (ROOT / name).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(subset)
    print(status, len(subset))
