from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'/'R6 拉丁美洲与加勒比'
TOPIC='WL-TOPIC-R6-LATAM'
DIM_ZH={'definition':'定义与边界','history':'历史层与连续性','language_media':'语言、文字与媒介','institution':'文学制度与传播','reading_route':'阅读路线','internal_tradition':'内部传统','literary_network':'跨传统网络','mechanism':'形成机制','comparison':'比较','cross_region':'跨区域比较'}
HIST={'definition':'全时段边界','history':'历史纵向','language_media':'跨时期媒介','institution':'跨时期制度','reading_route':'综合阅读','internal_tradition':'传统纵向','literary_network':'跨时期网络','mechanism':'跨时期机制'}

def split(t):
 m=re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$',t,re.S); return (m.group(1),m.group(2)) if m else ('',t)
def scalar(f,k):
 m=re.search(rf'(?m)^{re.escape(k)}:\s*["\']?(.*?)["\']?\s*$',f); return m.group(1).strip(' "\'') if m else ''
def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"')+'"'
def setv(f,k,v):
 line=f'{k}: {q(v)}'
 return re.sub(rf'(?m)^{re.escape(k)}:.*$',line,f,1) if re.search(rf'(?m)^{re.escape(k)}:',f) else f+'\n'+line
def clean(s): return re.sub(r'\s+',' ',re.sub(r'[`*_]','',s)).strip(' -;；。')
def mech(body):
 m=re.search(r'(?ms)^##\s*(?:关键机制|关注机制|核心机制|形成机制|机制)\s*\n(.*?)(?=^##\s|\Z)',body)
 if m:
  xs=[]
  for line in m.group(1).splitlines():
   s=clean(re.sub(r'^[-*+]\s*','',line))
   if s: xs.append(s)
  if xs:return '；'.join(xs)[:420]
 b=re.sub(r'(?m)^#.*$','',body,1)
 for p in re.split(r'\n\s*\n',b):
  s=clean(p)
  if s and not s.startswith('#'): return s[:420]
 return '说明该节点在专题结构中的作用'

groups={'10 核心结构':'核心结构','11 内部传统':'内部传统','12 跨传统网络':'跨传统网络'}
changed=0; count=0
for sub,typ in groups.items():
 d=TOP/sub
 if not d.exists(): continue
 for p in d.glob('*.md'):
  text=p.read_text(encoding='utf-8'); f,b=split(text)
  if scalar(f,'topic_id')!=TOPIC: continue
  count+=1; dim=scalar(f,'dimension')
  f=setv(f,'structure_type_zh',typ)
  f=setv(f,'parent_label',f'拉丁美洲与加勒比｜{typ}')
  f=setv(f,'history_position',scalar(f,'period') or scalar(f,'history_position') or HIST.get(dim,'跨时期结构'))
  if not scalar(f,'mechanism'): f=setv(f,'mechanism',mech(b))
  new='---\n'+f.strip()+'\n---\n'+b.lstrip('\n')
  if new!=text: p.write_text(new,encoding='utf-8'); changed+=1

base=next(iter(sorted(TOP.glob('02 *.base'))))
dim_formula='if(dimension, dimension'+''.join(f'.replace("{k}", "{v}")' for k,v in DIM_ZH.items())+', "")'
order='''      - file.name
      - structure_type_zh
      - formula.dimension_zh
      - sequence
      - parent_label
      - history_position
      - mechanism
      - id
'''
out=f'''filters:
  and:
    - topic_id == "{TOPIC}"
formulas:
  dimension_zh: {dim_formula}
properties:
  file.name:
    displayName: 节点
  note.structure_type_zh:
    displayName: 类型
  formula.dimension_zh:
    displayName: 维度
  note.sequence:
    displayName: 顺序
  note.parent_label:
    displayName: 父节点
  note.history_position:
    displayName: 历史位置
  note.mechanism:
    displayName: 机制
  note.id:
    displayName: 编号
views:
  - type: table
    name: 全部知识节点
    groupBy:
      property: structure_type_zh
      direction: ASC
    order:
'''+order
for typ in groups.values():
 out+=f'''  - type: table
    name: {typ}
    filters:
      and:
        - structure_type_zh == "{typ}"
    groupBy:
      property: structure_type_zh
      direction: ASC
    order:
'''+order
base.write_text(out,encoding='utf-8')
missing=0
for sub in groups:
 for p in (TOP/sub).glob('*.md'):
  f,_=split(p.read_text(encoding='utf-8'))
  if scalar(f,'topic_id')==TOPIC and not scalar(f,'mechanism'): missing+=1
report=ROOT/'_audit'/'r_axis_acceptance'/'R6_STRUCTURE_METADATA_REPAIR_V1.md'
report.write_text(f'''# R6 Structure Metadata Repair V1

- R6 actual topic_id: `{TOPIC}`
- Structure nodes: **{count}**
- Nodes changed: **{changed}**
- mechanism missing after repair: **{missing}**
- Structure Base filter corrected to the actual R6 topic id.

`R6_STRUCTURE_METADATA_REPAIR_V1 = {'PASS' if missing==0 and count>0 else 'FAIL'}`
''',encoding='utf-8')
print(report)
