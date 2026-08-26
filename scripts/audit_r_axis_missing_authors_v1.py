from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
AUD=ROOT/'_audit'/'r_axis_acceptance'/'R_AXIS_MISSING_AUTHORS_V1.md'

TOPICS={
'R1':'R1 西亚—地中海古老传统',
'R2':'R2 东亚文学',
'R3':'R3 南亚文学',
'R4':'R4 欧洲文学',
'R5':'R5 北美文学',
'R6':'R6 拉丁美洲与加勒比',
'R7':'R7 非洲文学',
'R8':'R8 东南亚文学',
'R9':'R9 大洋洲与太平洋',
}

def split(text):
 m=re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$',text,re.S)
 return (m.group(1),m.group(2)) if m else ('',text)
def scalar(front,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',front)
 return m.group(1).strip(' "\'') if m else ''
def list_field(front,key):
 lines=front.splitlines(); out=[]
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*\[\]\s*$',line): return []
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   for n in lines[i+1:]:
    mm=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if mm: out.append(mm.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []

rows=[]
for p in sorted(WORKS.glob('*.md')):
 text=p.read_text(encoding='utf-8'); f,_=split(text)
 if scalar(f,'type')!='work': continue
 author=scalar(f,'author')
 if author: continue
 axes=list_field(f,'axis_r'); topics=list_field(f,'topics')
 rs=[code for code,label in TOPICS.items() if label in axes]
 if 'WL-TOPIC-R10-TRANSREGIONAL' in topics: rs.append('R10')
 if not rs: continue
 rows.append((p.name, scalar(f,'title') or p.stem, '、'.join(rs), scalar(f,'year') or '', scalar(f,'title_original') or '', scalar(f,'verification_status') or ''))

lines=['# R Axis Missing Authors V1','',f'- Unique works with missing author in R1–R10: **{len(rows)}**','', '| 文件 | 作品 | R专题 | 年份 | 原题 | 校验状态 |','|---|---|---|---|---|---|']
for r in rows:
 lines.append('| ' + ' | '.join(x.replace('|','\\|') for x in r) + ' |')
AUD.parent.mkdir(parents=True,exist_ok=True)
AUD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(len(rows))
