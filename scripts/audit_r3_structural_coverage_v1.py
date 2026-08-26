from pathlib import Path
import re, unicodedata

ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'
OUT=ROOT/'_audit'/'r_axis_r3'
R3='R3 南亚文学'

SLOTS=[
('梵语—吠陀与古典文学传统','吠陀赞歌','梨俱吠陀|Rigveda','P0'),
('梵语—吠陀与古典文学传统','奥义书','奥义书|Upanishads','P1'),
('梵语—吠陀与古典文学传统','摩诃婆罗多史诗','摩诃婆罗多|Mahabharata','P0'),
('梵语—吠陀与古典文学传统','罗摩衍那史诗','罗摩衍那|Ramayana','P0'),
('梵语—吠陀与古典文学传统','薄伽梵歌','薄伽梵歌|Bhagavad Gita','P1'),
('梵语—吠陀与古典文学传统','古典梵语戏剧','沙恭达罗|Abhijnanasakuntalam','P0'),
('梵语—吠陀与古典文学传统','古典抒情与kavya','云使|Meghaduta','P1'),
('梵语—吠陀与古典文学传统','寓言与故事集','五卷书|Panchatantra','P1'),
('梵语—吠陀与古典文学传统','大型故事叙事','故事海|Kathasaritsagara','P1'),
('梵语—吠陀与古典文学传统','戏剧诗学理论','舞论|戏剧论|Natyashastra','P1'),
('巴利—普拉克里特与佛教耆那文学传统','巴利佛教偈颂','法句经|Dhammapada','P0'),
('巴利—普拉克里特与佛教耆那文学传统','本生故事','本生经|Jataka','P0'),
('巴利—普拉克里特与佛教耆那文学传统','早期僧侣诗歌','长老偈|Theragatha','P1'),
('巴利—普拉克里特与佛教耆那文学传统','早期女性宗教诗歌','长老尼偈|Therigatha','P1'),
('巴利—普拉克里特与佛教耆那文学传统','耆那经典叙事','卡尔帕经|Kalpasutra','P1'),
('巴利—普拉克里特与佛教耆那文学传统','普拉克里特世俗诗歌','七百咏|Gaha Sattasai|Gathasaptasati','P1'),
('泰米尔与南印度文学传统','桑伽姆爱情诗','古鲁恩托盖|Kuruntokai','P0'),
('泰米尔与南印度文学传统','桑伽姆公共诗','普拉南努鲁|Purananuru','P0'),
('泰米尔与南印度文学传统','泰米尔史诗','西拉巴提伽拉姆|脚镯记|Silappatikaram','P0'),
('泰米尔与南印度文学传统','泰米尔Bhakti女性诗','安达尔诗歌|Andal','P1'),
('泰米尔与南印度文学传统','泰卢固古典文学','摩诃婆罗多（泰卢固）|Andhra Mahabharatam','P1'),
('泰米尔与南印度文学传统','卡纳达古典文学','维克拉玛尔朱那胜利记|Vikramarjuna Vijaya','P1'),
('泰米尔与南印度文学传统','马拉雅拉姆现代小说','Chemmeen|虾','P1'),
('泰米尔与南印度文学传统','现代南印度小说','Samskara|葬礼','P1'),
('北印度俗语—Bhakti与印地文学传统','卡比尔诗歌','卡比尔诗选|Kabir','P0'),
('北印度俗语—Bhakti与印地文学传统','克里希纳Bhakti诗','苏尔达斯诗选|Sursagar','P1'),
('北印度俗语—Bhakti与印地文学传统','罗摩Bhakti史诗','罗摩功行录|Ramcharitmanas','P0'),
('北印度俗语—Bhakti与印地文学传统','女性Bhakti诗','米拉拜诗选|Mirabai','P1'),
('北印度俗语—Bhakti与印地文学传统','现代印地小说形成','戈丹|Godaan','P0'),
('北印度俗语—Bhakti与印地文学传统','印地短篇现实主义','棋手|两个公牛','P1'),
('北印度俗语—Bhakti与印地文学传统','现代印地诗歌','卡马亚尼|Kamayani','P1'),
('波斯语—Hindavi—乌尔都文学传统','南亚波斯/Hindavi诗','阿米尔·霍斯陆诗选|Amir Khusrau','P1'),
('波斯语—Hindavi—乌尔都文学传统','古典乌尔都ghazal','米尔诗选|Mir Taqi Mir','P0'),
('波斯语—Hindavi—乌尔都文学传统','加利卜','加利卜诗选|Diwan-e-Ghalib','P0'),
('波斯语—Hindavi—乌尔都文学传统','伊克巴尔现代诗','伊克巴尔诗选|Bal-e-Jibril|Bang-e-Dara','P1'),
('波斯语—Hindavi—乌尔都文学传统','dastan长篇叙事','阿米尔·哈姆扎传奇|Dastan-e-Amir Hamza','P1'),
('波斯语—Hindavi—乌尔都文学传统','分治短篇','托巴·泰克·辛格|Toba Tek Singh','P0'),
('波斯语—Hindavi—乌尔都文学传统','女性现代乌尔都小说','被子|Lihaaf','P1'),
('波斯语—Hindavi—乌尔都文学传统','现代乌尔都长篇','火河|Aag Ka Darya|River of Fire','P0'),
('孟加拉与东部语言文学传统','早期孟加拉佛教诗','查尔亚歌|Charyapada','P1'),
('孟加拉与东部语言文学传统','孟加拉小说形成','阿难陀寺|Anandamath','P1'),
('孟加拉与东部语言文学传统','泰戈尔诗歌','吉檀迦利|Gitanjali','P0'),
('孟加拉与东部语言文学传统','泰戈尔小说','家庭与世界|Ghare-Baire|戈拉','P1'),
('孟加拉与东部语言文学传统','孟加拉现实主义小说','道路之歌|Pather Panchali','P1'),
('孟加拉与东部语言文学传统','纳兹鲁尔','反叛者|Bidrohi','P1'),
('孟加拉与东部语言文学传统','孟加拉现代诗','博纳罗塔·森|Banalata Sen','P1'),
('旁遮普—信德与西北文学传统','锡克经典诗歌','古鲁·格兰特·萨希卜|Guru Granth Sahib','P0'),
('旁遮普—信德与西北文学传统','旁遮普苏菲诗','布莱·沙阿诗选|Bulleh Shah','P1'),
('旁遮普—信德与西北文学传统','qissa爱情叙事','希尔·兰贾|Heer Ranjha','P0'),
('旁遮普—信德与西北文学传统','信德苏菲诗','沙阿·阿卜杜勒·拉蒂夫诗选|Shah Jo Risalo','P1'),
('旁遮普—信德与西北文学传统','旁遮普分治文学','Pinjar|骨笼','P1'),
('僧伽罗—斯里兰卡文学传统','巴利编年史','大史|Mahavamsa','P0'),
('僧伽罗—斯里兰卡文学传统','古典僧伽罗诗文','鸽使诗|Selalihini Sandesaya','P1'),
('僧伽罗—斯里兰卡文学传统','现代僧伽罗小说','Gamperaliya|变迁的村庄','P0'),
('僧伽罗—斯里兰卡文学传统','斯里兰卡英语/战争文学','安尼尔的鬼魂|Anil’s Ghost|Anils Ghost','P1'),
('尼泊尔—喜马拉雅文学传统','尼泊尔语罗摩衍那','巴努巴克塔罗摩衍那|Bhanubhakta Ramayana','P0'),
('尼泊尔—喜马拉雅文学传统','尼泊尔现代长诗','牟那·马丹|Muna Madan','P0'),
('尼泊尔—喜马拉雅文学传统','尼泊尔现代小说','蓝色含羞草|Shirish Ko Phool','P1'),
('南亚英语文学传统','殖民时期印度英语小说','不可接触者|Untouchable','P0'),
('南亚英语文学传统','印度英语地方小说','斯瓦米和朋友|Swami and Friends','P1'),
('南亚英语文学传统','后殖民英语小说','午夜之子|Midnight’s Children|Midnights Children','P0'),
('南亚英语文学传统','当代印度英语小说','微物之神|The God of Small Things','P0'),
('南亚英语文学传统','跨国历史小说','玻璃宫|The Glass Palace','P1'),
]

def norm(s): return re.sub(r'[^0-9a-z\u4e00-\u9fff]+','',unicodedata.normalize('NFKC',s).casefold())

def fm(text):
 m=re.match(r'^---\s*\n(.*?)\n---',text,re.S); return m.group(1) if m else ''
def scalar(front,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',front); return m.group(1).strip(' "\'') if m else ''
def list_field(front,key):
 lines=front.splitlines(); out=[]
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*\[\]\s*$',line): return []
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if m: out.append(m.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 idx=[]; r3count=0; total=0
 for p in WORKS.glob('*.md'):
  text=p.read_text(encoding='utf-8-sig'); front=fm(text)
  if scalar(front,'type')!='work': continue
  total+=1
  vals=[scalar(front,'title'),scalar(front,'title_original'),p.stem]+list_field(front,'aliases')
  idx.append((p,front,{norm(x) for x in vals if x}))
  if R3 in list_field(front,'axis_r'): r3count+=1
 rows=[]; covered=0
 for trad,slot,cands,prio in SLOTS:
  found=None
  for cand in cands.split('|'):
   nc=norm(cand)
   for p,front,names in idx:
    if nc and nc in names:
     found=scalar(front,'title') or p.stem; break
   if found: break
  status='COVERED' if found else 'MISSING'; covered += status=='COVERED'
  rows.append((trad,slot,status,found or '—',prio,cands))
 lines=['# R3 Structural Coverage Audit V1','',f'- Total canonical Works: **{total}**',f'- Works currently mapped to R3: **{r3count}**',f'- Structural slots: **{len(rows)}**',f'- Covered: **{covered}**',f'- Missing: **{len(rows)-covered}**',f'- Coverage: **{covered/len(rows)*100:.1f}%**','','| Tradition | Slot | Status | Anchor | Priority |','|---|---|---|---|---|']
 for r in rows: lines.append('| '+' | '.join(r[:5])+' |')
 lines += ['','## Missing P0/P1','']
 for pr in ('P0','P1'):
  lines += [f'### {pr}','']
  miss=[r for r in rows if r[4]==pr and r[2]=='MISSING']
  lines += [f'- {r[0]} / {r[1]} → {r[5]}' for r in miss] or ['- None']
  lines.append('')
 lines += ['`R3_STRUCTURAL_COVERAGE_V1 = AUDITED_READ_ONLY`','']
 (OUT/'R3_STRUCTURAL_COVERAGE_V1.md').write_text('\n'.join(lines),encoding='utf-8')
 print(f'R3={r3count} slots={len(rows)} covered={covered} missing={len(rows)-covered}')
if __name__=='__main__': main()
