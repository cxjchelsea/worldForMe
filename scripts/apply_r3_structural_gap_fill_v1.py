from pathlib import Path
import re, unicodedata
from audit_r3_structural_coverage_v1 import SLOTS

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
OUT=ROOT/'_audit'/'r_axis_r3'
R3='R3 南亚文学'

META={
'奥义书':('Upanishads','佚名',None),
'五卷书':('Panchatantra','传 Vishnu Sharma',None),
'故事海':('Kathasaritsagara','苏摩提婆',None),
'舞论':('Natyashastra','传婆罗多牟尼',None),
'法句经':('Dhammapada','佚名',None),
'长老偈':('Theragatha','多人',None),
'长老尼偈':('Therigatha','多人',None),
'卡尔帕经':('Kalpasutra','传跋陀罗巴胡',None),
'七百咏':('Gathasaptasati','传哈拉',None),
'古鲁恩托盖':('Kuruntokai','多人',None),
'普拉南努鲁':('Purananuru','多人',None),
'安达尔诗歌':('Andal poems','安达尔',None),
'摩诃婆罗多（泰卢固）':('Andhra Mahabharatam','Nannaya、Tikkana、Errana',None),
'维克拉玛尔朱那胜利记':('Vikramarjuna Vijaya','Pampa',None),
'Chemmeen':('Chemmeen','Thakazhi Sivasankara Pillai',1956),
'Samskara':('Samskara','U. R. Ananthamurthy',1965),
'卡比尔诗选':('Kabir poems','卡比尔',None),
'苏尔达斯诗选':('Sursagar','苏尔达斯',None),
'米拉拜诗选':('Mirabai poems','米拉拜',None),
'棋手':('Shatranj Ke Khiladi','普列姆昌德',1924),
'卡马亚尼':('Kamayani','贾亚辛格尔·普拉萨德',1936),
'阿米尔·霍斯陆诗选':('Amir Khusrau poems','阿米尔·霍斯陆',None),
'米尔诗选':('Mir Taqi Mir poems','米尔·塔基·米尔',None),
'加利卜诗选':('Diwan-e-Ghalib','米尔扎·加利卜',None),
'伊克巴尔诗选':('Selected poems of Muhammad Iqbal','穆罕默德·伊克巴尔',None),
'阿米尔·哈姆扎传奇':('Dastan-e-Amir Hamza','多人',None),
'托巴·泰克·辛格':('Toba Tek Singh','萨达特·哈桑·曼托',1955),
'查尔亚歌':('Charyapada','多人',None),
'阿难陀寺':('Anandamath','班金·钱德拉·查特吉',1882),
'道路之歌':('Pather Panchali','比布提布尚·班纳吉',1929),
'反叛者':('Bidrohi','卡齐·纳兹鲁尔·伊斯拉姆',1922),
'古鲁·格兰特·萨希卜':('Guru Granth Sahib','多人',1604),
'布莱·沙阿诗选':('Bulleh Shah poems','布莱·沙阿',None),
'希尔·兰贾':('Heer Ranjha','瓦里斯·沙阿',1766),
'沙阿·阿卜杜勒·拉蒂夫诗选':('Shah Jo Risalo','沙阿·阿卜杜勒·拉蒂夫·比泰',None),
'Pinjar':('Pinjar','阿姆丽塔·普里塔姆',1950),
'大史':('Mahavamsa','佚名',None),
'鸽使诗':('Selalihini Sandesaya','Sri Rahula Thera',None),
'Gamperaliya':('Gamperaliya','Martin Wickramasinghe',1944),
'安尼尔的鬼魂':("Anil's Ghost",'Michael Ondaatje',2000),
'巴努巴克塔罗摩衍那':('Bhanubhakta Ramayana','Bhanubhakta Acharya',None),
'牟那·马丹':('Muna Madan','Laxmi Prasad Devkota',1936),
'蓝色含羞草':('Shirish Ko Phool','Parijat',1965),
'斯瓦米和朋友':('Swami and Friends','R. K. Narayan',1935),
'玻璃宫':('The Glass Palace','Amitav Ghosh',2000),
}

T_BY_YEAR=lambda y: ('T0 文学源头与古代文学' if y is not None and y<500 else 'T1 中古多中心文学世界' if y is not None and y<1500 else 'T2 早期现代文学' if y is not None and y<1800 else 'T3 19世纪现代文学体系' if y is not None and y<1890 else 'T4 全球现代主义时代' if y is not None and y<1945 else 'T5 二战后多极文学' if y is not None and y<1980 else 'T6 当代全球文学' if y is not None else None)

def norm(s): return re.sub(r'[^0-9a-z\u4e00-\u9fff]+','',unicodedata.normalize('NFKC',s).casefold())
def fm_span(text): return re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
def scalar(front,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',front); return m.group(1).strip(' "\'') if m else ''
def list_field(front,key):
 lines=front.splitlines(); out=[]
 for i,line in enumerate(lines):
  inline=re.match(rf'^{re.escape(key)}:\s*\[(.*?)\]\s*$',line)
  if inline:
   raw=inline.group(1).strip(); return [] if not raw else [x.strip().strip('"\'') for x in raw.split(',')]
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if m: out.append(m.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []
def set_list(front,key,vals):
 lines=front.splitlines(); start=None; end=None
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:',line):
   start=i; end=i+1
   if line.strip().endswith(':'):
    while end<len(lines) and re.match(r'^\s*-\s+',lines[end]): end+=1
   break
 block=[f'{key}:']+[f'- {v}' for v in vals] if vals else [f'{key}: []']
 if start is None: return front+'\n'+'\n'.join(block)
 return '\n'.join(lines[:start]+block+lines[end:])
def set_scalar(front,key,val):
 pat=rf'(?m)^{re.escape(key)}:\s*.*$'
 line=f'{key}: {val}'
 return re.sub(pat,line,front,count=1) if re.search(pat,front) else front+'\n'+line

def index():
 out=[]
 for p in WORKS.glob('*.md'):
  text=p.read_text(encoding='utf-8-sig'); m=fm_span(text)
  if not m: continue
  front=m.group(1)
  if scalar(front,'type')!='work': continue
  vals=[scalar(front,'title'),scalar(front,'title_original'),p.stem]+list_field(front,'aliases')
  out.append([p,text,m,front,{norm(x) for x in vals if x}])
 return out

def create_work(title,orig,author,year,trad,slot,prio):
 safe=title.replace('/','／')
 p=WORKS/f'{safe}.md'
 i=2
 while p.exists(): p=WORKS/f'{safe} ({i}).md'; i+=1
 t=T_BY_YEAR(year)
 lines=['---',f'id: WL-WORK-R3-{abs(hash((title,orig)))%100000000:08d}','type: work',f'title: "{title}"',f'title_original: "{orig}"','aliases: []',f'author: "{author}"',f'year: {year if year is not None else "null"}','read_status: 未读','axis_t:']
 if t: lines.append(f'- {t}')
 else: lines[-1]='axis_t: []'
 lines += ['axis_r:',f'- {R3}','axis_m: []','axis_g: []','axis_q: []','axis_source: r3_structural_gap_fill','topics: []','topic_links: []',f'r3_priority: {"★" if prio=="P0" else "◆"}',f'r3_tradition: "{trad}"','r3_role:',f'- "{slot}"','verification_status: 手工核验','bibliography_status: metadata_pending','---',f'# {title}','','## R3 结构位置','',f'- 内部传统：{trad}',f'- 结构角色：{slot}','', '> 本作品由 R3 Structural Gap Fill V1 补入中央作品库；专题不维护重复书单。','']
 p.write_text('\n'.join(lines),encoding='utf-8')
 return p.name

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 idx=index(); created=[]; reused=[]; enriched=[]
 for trad,slot,cands,prio in SLOTS:
  found=None
  for cand in cands.split('|'):
   nc=norm(cand)
   for item in idx:
    if nc and nc in item[4]: found=item; break
   if found: break
  if not found:
   title=cands.split('|')[0]
   orig,author,year=META.get(title,('', '佚名', None))
   fn=create_work(title,orig,author,year,trad,slot,prio); created.append(fn)
   idx=index(); continue
  p,text,m,front,names=found
  reused.append(p.name)
  changed=False
  ar=list_field(front,'axis_r')
  if R3 not in ar: ar.append(R3); front=set_list(front,'axis_r',ar); changed=True
  existing=scalar(front,'r3_tradition')
  if not existing: front=set_scalar(front,'r3_tradition',f'"{trad}"'); changed=True
  roles=list_field(front,'r3_role')
  if not roles: roles=[]
  if slot not in roles: roles.append(slot); front=set_list(front,'r3_role',[f'"{x}"' for x in roles]); changed=True
  if not scalar(front,'r3_priority'): front=set_scalar(front,'r3_priority','★' if prio=='P0' else '◆'); changed=True
  if changed:
   p.write_text(text[:m.start(1)]+front+text[m.end(1):],encoding='utf-8'); enriched.append(p.name)
 lines=['# R3 Structural Gap Fill V1','',f'- Structural slots processed: **{len(SLOTS)}**',f'- Existing anchors reused: **{len(set(reused))}**',f'- Existing Works enriched for R3: **{len(set(enriched))}**',f'- Newly created canonical Works: **{len(created)}**','','## Created','']
 lines += [f'- {x}' for x in created] or ['- None']
 lines += ['','`R3_STRUCTURAL_GAP_FILL_V1 = APPLIED`','']
 (OUT/'R3_STRUCTURAL_GAP_FILL_V1.md').write_text('\n'.join(lines),encoding='utf-8')
 print(f'created={len(created)} enriched={len(set(enriched))}')
if __name__=='__main__': main()
