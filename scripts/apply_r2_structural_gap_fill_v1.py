from pathlib import Path
import re, csv, unicodedata
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'; AUDIT=ROOT/'_audit/r_axis_r2'; MATRIX=AUDIT/'r2_structural_slots_v1.csv'
R2='R2 东亚文学'
ITEMS=[
 {'title':'左传','orig':'Zuo Zhuan','author':'佚名','trad':'中国文学传统','role':'先秦历史叙事','priority':'◆','aliases':['春秋左氏传']},
 {'title':'世说新语','orig':'Shishuo Xinyu','author':'刘义庆','trad':'中国文学传统','role':'六朝志人笔记与名士文化','priority':'◆','aliases':[]},
 {'title':'漱玉词','orig':'Shuyu Ci','author':'李清照','trad':'中国文学传统','role':'宋词与女性词人传统','priority':'★','aliases':['李清照词集']},
 {'title':'古事记','orig':'Kojiki','author':'太安万侣编录','trad':'日本文学传统','role':'早期记纪神话与王权叙事','priority':'◆','aliases':[]},
 {'title':'处容歌','orig':'Cheoyongga','author':'佚名','trad':'朝鲜半岛文学传统','role':'新罗乡歌与仪式诗传统','priority':'◆','aliases':[]},
 {'title':'青山别曲','orig':'Cheongsan Byeolgok','author':'佚名','trad':'朝鲜半岛文学传统','role':'高丽歌谣传统','priority':'◆','aliases':[]},
 {'title':'龙飞御天歌','orig':'Yongbieocheonga','author':'郑麟趾等','trad':'朝鲜半岛文学传统','role':'训民正音初期书写与王朝颂歌','priority':'◆','aliases':[]},
 {'title':'青丘永言','orig':'Cheonggu Yeongeon','author':'金天泽编','trad':'朝鲜半岛文学传统','role':'时调经典选集与歌唱传统','priority':'★','aliases':[]},
 {'title':'洪吉童传','orig':'Hong Gildong jeon','author':'许筠','trad':'朝鲜半岛文学传统','role':'古典英雄小说与社会批判','priority':'★','aliases':['洪吉童傳']},
 {'title':'无情','orig':'Mujeong','author':'李光洙','trad':'朝鲜半岛文学传统','role':'近代启蒙与现代小说形成','priority':'★','aliases':['무정']},
 {'title':'杜鹃花','orig':'Jindallae-kkot','author':'金素月','trad':'朝鲜半岛文学传统','role':'殖民时期现代诗歌与民族抒情','priority':'◆','aliases':['진달래꽃']},
 {'title':'翅膀','orig':'Nalgae','author':'李箱','trad':'朝鲜半岛文学传统','role':'殖民时期现代主义小说','priority':'◆','aliases':['날개']},
 {'title':'矮子射上来的小球','orig':'Nanjangi-ga ssoaollin jageun gong','author':'赵世熙','trad':'朝鲜半岛文学传统','role':'工业化、阶级与都市批判','priority':'◆','aliases':['난장이가 쏘아올린 작은 공']},
]
def norm(s):
 s=unicodedata.normalize('NFKC',s or '').casefold(); return re.sub(r'[\s·・—_\-:：,，。.!！?？()（）《》〈〉“”"\'’]+','',s)
def fm_span(text): return re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)',text,re.S)
def scalar(f,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$',f)
 if not m:return ''
 return m.group(1).strip().strip('"\'')
def list_field(f,key):
 lines=f.splitlines()
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   out=[]
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*(.*?)\s*$',n)
    if m:out.append(m.group(1).strip().strip('"\''));continue
    if n.strip() and not n.startswith((' ','\t')):break
   return out
 return []
def set_scalar(f,key,val):
 pat=rf'(?m)^{re.escape(key)}:\s*.*$'
 if re.search(pat,f):return re.sub(pat,f'{key}: {val}',f,count=1)
 return f+f'\n{key}: {val}'
def set_list(f,key,vals):
 lines=f.splitlines(); start=None; end=None
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*(?:\[.*\])?\s*$',line):
   start=i; end=i+1
   while end<len(lines) and re.match(r'^\s*-\s+',lines[end]):end+=1
   break
 block=[f'{key}:']+[f'- {v}' for v in vals]
 if start is None:return f+'\n'+'\n'.join(block)
 return '\n'.join(lines[:start]+block+lines[end:])
def main():
 index={}
 files=[]
 for p in WORKS.glob('*.md'):
  text=p.read_text(encoding='utf-8-sig'); m=fm_span(text)
  if not m:continue
  f=m.group(1)
  if scalar(f,'type')!='work':continue
  vals={scalar(f,'title') or p.stem, scalar(f,'title_original'), p.stem}; vals.update(list_field(f,'aliases'))
  rec=(p,text,m,f)
  for v in vals:
   if v:index.setdefault(norm(v),[]).append(rec)
 reused=[]; created=[]
 for i,it in enumerate(ITEMS,1):
  hit=None
  for v in [it['title'],it['orig'],*it['aliases']]:
   if index.get(norm(v)): hit=index[norm(v)][0]; break
  if hit:
   p,text,m,f=hit
   ar=list_field(f,'axis_r')
   if R2 not in ar: ar.append(R2); f=set_list(f,'axis_r',ar)
   f=set_scalar(f,'r2_tradition',it['trad']); f=set_scalar(f,'r2_priority',it['priority']); f=set_list(f,'r2_role',[it['role']])
   p.write_text(text[:m.start(1)]+f+text[m.end(1):],encoding='utf-8'); reused.append(it['title'])
  else:
   safe=it['title'].replace('/','／')+'.md'; p=WORKS/safe
   aliases='aliases: []' if not it['aliases'] else 'aliases:\n'+'\n'.join(f'- {a}' for a in it['aliases'])
   text=f'''---\nid: WL-WORK-R2-GAP-{i:02d}\ntype: work\ntitle: {it['title']}\ntitle_original: {it['orig']}\n{aliases}\nauthor: {it['author']}\nyear: null\nread_status: 未读\naxis_t: []\naxis_r:\n- {R2}\naxis_m: []\naxis_g: []\naxis_q: []\naxis_source: reviewed_r2_structural_gap_fill\nr2_priority: {it['priority']}\nr2_tradition: {it['trad']}\nr2_role:\n- {it['role']}\nverification_status: 手工核验\nbibliography_status: metadata_pending\n---\n# {it['title']}\n\nR2 结构角色：{it['role']}。\n'''
   p.write_text(text,encoding='utf-8'); created.append(it['title'])
 # promote matching matrix rows by role/candidate intent
 rows=list(csv.DictReader(MATRIX.open(encoding='utf-8-sig')))
 role_to_title={it['role']:it['title'] for it in ITEMS}
 slot_map={
 '先秦历史叙事':'左传','六朝志怪与笔记':'世说新语','宋词':'漱玉词','早期记纪神话':'古事记','乡歌传统':'处容歌','高丽歌谣':'青山别曲','朝鲜王朝汉文与训民正音转型':'龙飞御天歌','时调':'青丘永言','古典英雄小说':'洪吉童传','近代启蒙小说':'无情','殖民时期现代诗歌':'杜鹃花','殖民时期现代小说':'翅膀','工业化与民主化文学':'矮子射上来的小球'}
 out=[]
 for r in rows:
  if r['slot'] in slot_map: r['candidates']=slot_map[r['slot']]
  out.append(r)
 with MATRIX.open('w',encoding='utf-8-sig',newline='') as fh:
  w=csv.DictWriter(fh,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(out)
 report=['# R2 Structural Gap Fill V1','',f'- Reused canonical Works: **{len(reused)}**',f'- Newly created canonical Works: **{len(created)}**','','## Reused','']+[f'- {x}' for x in reused]+['','## Created','']+[f'- {x}' for x in created]+['','`R2_STRUCTURAL_GAP_FILL_V1 = APPLIED`','']
 (AUDIT/'R2_STRUCTURAL_GAP_FILL_V1.md').write_text('\n'.join(report),encoding='utf-8')
 print(f'REUSED={len(reused)} CREATED={len(created)}')
if __name__=='__main__':main()
