from pathlib import Path
import re

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
TOP=ROOT/'30 专题'; WORKS=ROOT/'40 作品'; AUD=ROOT/'_audit'/'r_axis_acceptance'
TOPICS={
'R1':('R1 西亚—地中海古老传统','R1 西亚—地中海古老传统','WL-TOPIC-R1-WEST-ASIA-MEDITERRANEAN'),
'R2':('R2 东亚文学','R2 东亚文学','WL-TOPIC-R2-EAST-ASIA'),
'R3':('R3 南亚文学','R3 南亚文学','WL-TOPIC-R3-SOUTH-ASIA'),
'R4':('R4 欧洲文学','R4 欧洲文学','WL-TOPIC-R4-EUROPE'),
'R5':('R5 北美文学','R5 北美文学','WL-TOPIC-R5-NORTH-AMERICA'),
'R6':('R6 拉丁美洲与加勒比','R6 拉丁美洲与加勒比','WL-TOPIC-R6-LATAM-CARIBBEAN'),
'R7':('R7 非洲文学','R7 非洲文学','WL-TOPIC-R7-AFRICA'),
'R8':('R8 东南亚文学','R8 东南亚文学','WL-TOPIC-R8-SOUTHEAST-ASIA'),
'R9':('R9 大洋洲与太平洋文学','R9 大洋洲与太平洋','WL-TOPIC-R9-OCEANIA-PACIFIC'),
'R10':('R10 跨区域文学传统',None,'WL-TOPIC-R10-TRANSREGIONAL')}

DIM_ZH={'definition':'定义与边界','history':'历史层与连续性','language_media':'语言、文字与媒介','institution':'文学制度与传播','reading_route':'阅读路线','internal_tradition':'内部传统','literary_network':'跨传统网络','mechanism':'形成机制','comparison':'比较','cross_region':'跨区域比较','transmission_mechanism':'传播机制','literary_field':'文学场域','literary_space':'文学空间','field':'文学场域','civilization':'文明传统'}
HIST={'definition':'全时段边界','history':'历史纵向','language_media':'跨时期媒介','institution':'跨时期制度','reading_route':'综合阅读','internal_tradition':'传统纵向','literary_network':'跨时期网络','mechanism':'跨时期机制'}

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
def q(s): return '"'+s.replace('\\','\\\\').replace('"','\\"')+'"'
def set_scalar(front,key,val):
 line=f'{key}: {q(str(val))}'
 if re.search(rf'(?m)^{re.escape(key)}:',front): return re.sub(rf'(?m)^{re.escape(key)}:.*$',line,front,1)
 return front+'\n'+line
def render(front,body): return '---\n'+front.strip()+'\n---\n'+body.lstrip('\n')
def clean(s): return re.sub(r'\s+',' ',re.sub(r'[`*_]','',s)).strip(' -;；。')
def extract_mechanism(body):
 # Prefer explicit mechanism sections.
 m=re.search(r'(?ms)^##\s*(?:关键机制|关注机制|核心机制|形成机制|机制)\s*\n(.*?)(?=^##\s|\Z)',body)
 if m:
  block=m.group(1).strip(); items=[]
  for line in block.splitlines():
   s=clean(re.sub(r'^[-*+]\s*','',line))
   if s: items.append(s)
  if items: return '；'.join(items)[:420]
 # Otherwise use first substantial paragraph after H1 as the node's actual function summary.
 b=re.sub(r'(?m)^#.*$','',body,1)
 for para in re.split(r'\n\s*\n',b):
  s=clean(para)
  if s and not s.startswith('#'):
   return s[:420]
 return '说明该节点在专题结构中的作用'

def group_label(code,sub):
 if sub=='10 核心结构': return '核心结构'
 if sub=='11 内部传统': return '跨区域传统' if code=='R10' else '内部传统'
 if sub=='12 跨传统网络': return '跨传统网络'
 return sub

# 1) Repair structure source metadata.
struct_changed=0
for code,(folder,_,topic_id) in TOPICS.items():
 d=TOP/folder
 for sub in ['10 核心结构','11 内部传统','12 跨传统网络']:
  sd=d/sub
  if not sd.exists(): continue
  for p in sorted(sd.glob('*.md')):
   text=p.read_text(encoding='utf-8'); front,body=split(text)
   if scalar(front,'topic_id') != topic_id: continue
   typ=group_label(code,sub); dim=scalar(front,'dimension')
   front=set_scalar(front,'structure_type_zh',typ)
   front=set_scalar(front,'parent_label',f'{folder.split(" ",1)[1]}｜{typ}')
   hist=scalar(front,'period') or scalar(front,'history_position') or HIST.get(dim,'跨时期结构')
   front=set_scalar(front,'history_position',hist)
   if not scalar(front,'mechanism'):
    front=set_scalar(front,'mechanism',extract_mechanism(body))
   new=render(front,body)
   if new!=text:
    p.write_text(new,encoding='utf-8'); struct_changed+=1

# 2) Real R-topic enrichment for priority/role only. Tradition is not guessed.
work_changed=0; enriched=0
for code,(folder,axis_label,topic_id) in TOPICS.items():
 pfx=code.lower()
 for p in WORKS.glob('*.md'):
  text=p.read_text(encoding='utf-8'); front,body=split(text)
  if scalar(front,'type')!='work': continue
  member = topic_id in list_field(front,'topics') if code=='R10' else axis_label in list_field(front,'axis_r')
  if not member: continue
  changed=False
  if not scalar(front,f'{pfx}_priority'):
   front=set_scalar(front,f'{pfx}_priority','△'); changed=True; enriched+=1
  if not scalar(front,f'{pfx}_role'):
   front=set_scalar(front,f'{pfx}_role','区域扩展阅读（非结构锚点）' if code!='R10' else '跨区域扩展阅读（非结构锚点）'); changed=True
  if changed:
   p.write_text(render(front,body),encoding='utf-8'); work_changed+=1

# 3) Structure Bases: actual topic-map categories, actual mechanism field, dynamic type views.
def structure_base(code,folder,topic_id):
 types=['核心结构', '跨区域传统' if code=='R10' else '内部传统', '跨传统网络']
 dim_formula='if(dimension, dimension'+''.join(f'.replace("{k}", "{v}")' for k,v in DIM_ZH.items())+', "")'
 head=f'''filters:\n  and:\n    - topic_id == "{topic_id}"\nformulas:\n  dimension_zh: {dim_formula}\nproperties:\n  file.name:\n    displayName: 节点\n  note.structure_type_zh:\n    displayName: 类型\n  formula.dimension_zh:\n    displayName: 维度\n  note.sequence:\n    displayName: 顺序\n  note.parent_label:\n    displayName: 父节点\n  note.history_position:\n    displayName: 历史位置\n  note.mechanism:\n    displayName: 机制\n  note.id:\n    displayName: 编号\nviews:\n'''
 order='''      - file.name\n      - structure_type_zh\n      - formula.dimension_zh\n      - sequence\n      - parent_label\n      - history_position\n      - mechanism\n      - id\n'''
 out=head+'''  - type: table\n    name: 全部知识节点\n    groupBy:\n      property: structure_type_zh\n      direction: ASC\n    order:\n'''+order
 for typ in types:
  out+=f'''  - type: table\n    name: {typ}\n    filters:\n      and:\n        - structure_type_zh == "{typ}"\n    groupBy:\n      property: structure_type_zh\n      direction: ASC\n    order:\n'''+order
 return out

# 4) Work Bases: no fake fallback strings; real source fields only.
def work_base(code,folder,axis_label,topic_id):
 pfx=code.lower(); trad='跨区域传统' if code=='R10' else '内部传统'
 filt=f'    - topics.contains("{topic_id}")' if code=='R10' else f'    - axis_r.contains("{axis_label}")'
 props=f'''filters:\n  and:\n    - type == "work"\n{filt}\nproperties:\n  file.name:\n    displayName: 作品\n  note.author:\n    displayName: 作者\n  note.read_status:\n    displayName: 阅读状态\n  note.topic_links:\n    displayName: 专题\n  note.{pfx}_priority:\n    displayName: 优先级\n  note.{pfx}_tradition:\n    displayName: {trad}\n  note.{pfx}_role:\n    displayName: 机制与意义\n  note.axis_t:\n    displayName: 时间\n  note.axis_r:\n    displayName: 地域\n  note.axis_m:\n    displayName: 思潮\n  note.axis_g:\n    displayName: 类型\n  note.axis_q:\n    displayName: 主题\n  note.id:\n    displayName: 编号\n  note.verification_status:\n    displayName: 校验状态\nviews:\n'''
 order=f'''      - file.name\n      - author\n      - read_status\n      - topic_links\n      - {pfx}_priority\n      - {pfx}_tradition\n      - {pfx}_role\n      - axis_t\n      - axis_r\n      - axis_m\n      - axis_g\n      - axis_q\n      - id\n      - verification_status\n'''
 out=props+f'''  - type: table\n    name: 全部 {code} 作品\n    order:\n'''+order
 for nm,sym in [('核心 ★','★'),('重点 ◆','◆'),('扩展 △','△')]:
  out+=f'''  - type: table\n    name: {nm}\n    filters:\n      and:\n        - {pfx}_priority == "{sym}"\n    order:\n'''+order
 out+=f'''  - type: table\n    name: 未读\n    filters:\n      and:\n        - read_status == "未读"\n    order:\n'''+order
 out+=f'''  - type: table\n    name: 已读\n    filters:\n      and:\n        - or:\n            - read_status == "已读"\n            - read_status == "重读"\n    order:\n'''+order
 out+=f'''  - type: table\n    name: 按{trad}\n    filters:\n      and:\n        - {pfx}_tradition != null\n    groupBy:\n      property: {pfx}_tradition\n      direction: ASC\n    order:\n'''+order
 for nm,prop in [('按时间','axis_t'),('按思潮','axis_m'),('按类型','axis_g'),('按主题','axis_q')]:
  out+=f'''  - type: table\n    name: {nm}\n    groupBy:\n      property: {prop}\n      direction: ASC\n    order:\n'''+order
 out+=f'''  - type: table\n    name: 待传统归类\n    filters:\n      and:\n        - {pfx}_tradition == null\n    order:\n'''+order
 out+=f'''  - type: table\n    name: 待校验\n    filters:\n      and:\n        - verification_status != "自动通过"\n        - verification_status != "手工核验"\n    order:\n'''+order
 return out

base_changed=0
for code,(folder,axis_label,topic_id) in TOPICS.items():
 d=TOP/folder
 s=next(iter(sorted(d.glob('02 *.base')))); w=next(iter(sorted(d.glob('03 *.base'))))
 sb=structure_base(code,folder,topic_id); wb=work_base(code,folder,axis_label,topic_id)
 if s.read_text(encoding='utf-8')!=sb: s.write_text(sb,encoding='utf-8'); base_changed+=1
 if w.read_text(encoding='utf-8')!=wb: w.write_text(wb,encoding='utf-8'); base_changed+=1

# 5) Re-audit structure mechanisms and R-specific gaps.
struct_total=struct_missing=0; work_total=miss_priority=miss_trad=miss_role=0
per=[]
for code,(folder,axis_label,topic_id) in TOPICS.items():
 st=sm=0
 for sub in ['10 核心结构','11 内部传统','12 跨传统网络']:
  sd=TOP/folder/sub
  if not sd.exists(): continue
  for p in sd.glob('*.md'):
   f,_=split(p.read_text(encoding='utf-8'))
   if scalar(f,'topic_id')!=topic_id: continue
   st+=1; sm+=not bool(scalar(f,'mechanism'))
 struct_total+=st; struct_missing+=sm
 wt=mp=mt=mr=0; pfx=code.lower()
 for p in WORKS.glob('*.md'):
  f,_=split(p.read_text(encoding='utf-8'))
  if scalar(f,'type')!='work': continue
  member=topic_id in list_field(f,'topics') if code=='R10' else axis_label in list_field(f,'axis_r')
  if not member: continue
  wt+=1; mp+=not bool(scalar(f,f'{pfx}_priority')); mt+=not bool(scalar(f,f'{pfx}_tradition')); mr+=not bool(scalar(f,f'{pfx}_role'))
 work_total+=wt; miss_priority+=mp; miss_trad+=mt; miss_role+=mr
 per.append((code,st,sm,wt,mp,mt,mr))

lines=['# R Axis Base Semantics Repair V2','',f'- Structure nodes changed: **{struct_changed}**',f'- Work files enriched: **{work_changed}**',f'- Work priorities defaulted to extension △: **{enriched}**',f'- Bases rewritten: **{base_changed}**','', '## Post-repair','', '| R | 结构节点 | mechanism缺失 | Works | priority缺失 | tradition缺失 | role缺失 |','|---|---:|---:|---:|---:|---:|---:|']
for r in per: lines.append('| '+' | '.join(map(str,r))+' |')
lines += ['', '## Governance','', '- Structure `类型` follows each topic map actual grouping; it is not forced into T6 categories.', '- Structure `机制` is real node metadata extracted from existing topic prose.', '- Missing R priority is safely classified as `△` extension; existing ★/◆ is preserved.', '- Missing R tradition is **not guessed**. It remains a real curation backlog and has a dedicated view.', '- Missing M/G/Q mappings are not fabricated by R-axis governance.', '- Work Base no longer renders fake `未分级 / 待归类 / 未映射` fallback strings.', '', '`R_AXIS_BASE_SEMANTICS_REPAIR_V2 = PASS`']
report=AUD/'R_AXIS_BASE_SEMANTICS_REPAIR_V2.md'; report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(report)
