from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
R2=ROOT/'30 专题'/'R2 东亚文学'/'00 东亚文学.md'

# 1. Finalize R2 home status without changing content structure.
t=R2.read_text(encoding='utf-8')
t=re.sub(r'(?m)^structure_status:\s*active\s*$', 'structure_status: complete', t)
if 'R2_TOPIC_MAP_V1 = COMPLETE_USABLE' not in t:
    t=t.rstrip()+"\n\n## 状态\n`R2_TOPIC_MAP_STRUCTURE = COMPLETE`\n\n`R2_WORK_SUPPORT = COMPLETE`\n\n`R2_TOPIC_MAP_V1 = COMPLETE_USABLE`\n"
R2.write_text(t,encoding='utf-8')

# 2. Remove the obsolete synthetic R10 axis coordinate only.
changed=[]
for p in WORKS.glob('*.md'):
    txt=p.read_text(encoding='utf-8',errors='ignore')
    new=re.sub(r'(?m)^\s*-\s*R10 跨区域文学传统\s*\n?', '', txt)
    if new!=txt:
        p.write_text(new,encoding='utf-8')
        changed.append(p.name)
print(f'R2 finalized; removed illegal R10 axis coordinate from {len(changed)} Works')
for x in changed: print(x)
