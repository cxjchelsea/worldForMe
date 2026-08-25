from pathlib import Path
import csv

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis')
for t in ['T0','T1','T2','T3','T4','T5','T6']:
    src = ROOT / f'semantic_stage1_{t}.csv'
    with src.open('r', encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    out = []
    for i, r in enumerate(rows, 1):
        out.append({
            'n': i,
            'file': r['file'],
            'title': r['title'],
            'author': r['author'],
            'current_t': r['current_t'],
        })
    with (ROOT / f'compact_{t}.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['n','file','title','author','current_t'])
        w.writeheader(); w.writerows(out)
    print(t, len(out))
