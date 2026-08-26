from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]; LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'; W=LIT/'40 作品'
AX='M5.1 战后思想与美学范式'; TOP='WL-TOPIC-M5.1-POSTWAR-AESTHETICS'
PAIRS=[
('等待戈多.md','等待戈多（塞缪尔·贝克特）.md','荒诞','★',['等待','语言失效']),
('恰似水之于巧克力.md','恰似水之于巧克力（劳拉·埃斯基韦尔）.md','魔幻现实主义','◆',['日常魔幻','女性经验']),
('午夜之子.md','午夜之子（萨尔曼·鲁西迪）.md','魔幻现实主义','★',['国家寓言','历史与身体']),
('叶之屋.md','叶之屋（马克·Z. 丹尼尔斯基）.md','后现代主义','★',['版面实验','嵌套文本'])]
def parts(t):
 e=t.find('\n---\n',4); return t[4:e],t[e+5:]
def union(fm,key,vals):
 ls=fm.splitlines(); i=next((i for i,x in enumerate(ls) if x.startswith(key+':')),None)
 if i is None:return fm+'\n'+key+':\n'+'\n'.join('- '+v for v in vals)
 old=[]; j=i+1; inline=ls[i].split(':',1)[1].strip()
 if inline.startswith('['): old=[x.strip(" '\"") for x in inline.strip('[]').split(',') if x.strip()]
 else:
  while j<len(ls) and re.match(r'^\s*- ',ls[j]): old.append(ls[j].split('-',1)[1].strip().strip("'\"")); j+=1
 new=old+[v for v in vals if v not in old]; ls[i:j]=[key+':']+['- '+v for v in new]; return '\n'.join(ls)
def scalar(fm,key,val):
 pat=rf'(?m)^{re.escape(key)}:.*$'; line=f'{key}: "{val}"'; return re.sub(pat,line,fm,count=1) if re.search(pat,fm) else fm+'\n'+line
for orig,dup,mov,pri,axes in PAIRS:
 p=W/orig; t=p.read_text(encoding='utf-8'); fm,body=parts(t); fm=union(fm,'axis_m',[AX]); fm=union(fm,'topics',[TOP]); fm=scalar(fm,'m51_priority',pri); fm=scalar(fm,'m51_movement_cluster',mov); fm=union(fm,'m51_axes',axes); p.write_text('---\n'+fm+'\n---\n'+body,encoding='utf-8'); d=W/dup
 if d.exists(): d.unlink()
node=LIT/'20 节点'/'M 思潮'/'M5.1 战后思想与美学范式.md'; t=node.read_text(encoding='utf-8'); t=t.replace('topic_map: null','topic_map: "[[../../30 专题/M5.1 战后思想与美学范式/00 战后思想与美学范式|M5.1 战后思想与美学范式]]"'); t=t.replace('> 暂未接入。','- [[../../30 专题/M5.1 战后思想与美学范式/00 战后思想与美学范式|M5.1 战后思想与美学范式]]'); node.write_text(t,encoding='utf-8')
print('cleaned',len(PAIRS))
