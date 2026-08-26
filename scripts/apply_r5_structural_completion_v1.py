from pathlib import Path
import re, unicodedata
ROOT=Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS=ROOT/'40 作品'; OUT=ROOT/'_audit'/'r_axis_r5'; R5='R5 北美文学'
SLOTS=[
('北美原住民文学传统','现代原住民小说奠基','黎明之屋|House Made of Dawn','N. Scott Momaday','P0'),('北美原住民文学传统','仪式与土地叙事','仪式|Ceremony','Leslie Marmon Silko','P0'),('北美原住民文学传统','口述—自传混合书写','通往雨山的路|The Way to Rainy Mountain','N. Scott Momaday','P1'),('北美原住民文学传统','部落共同体与现代性','爱药|Love Medicine','Louise Erdrich','P1'),('北美原住民文学传统','加拿大原住民反讽小说','绿草，流水|Green Grass, Running Water','Thomas King','P1'),('北美原住民文学传统','原住民女性与北太平洋','猴滩|Monkey Beach','Eden Robinson','P1'),('北美原住民文学传统','植物知识与回归叙事','编织甜草|Braiding Sweetgrass','Robin Wall Kimmerer','P1'),('北美原住民文学传统','当代都市原住民','在那里那里|There There','Tommy Orange','P1'),
('殖民地—清教徒与早期共和国文学传统','殖民见证','普利茅斯种植园史|Of Plymouth Plantation','William Bradford','P1'),('殖民地—清教徒与早期共和国文学传统','清教徒女性诗歌','安妮·布拉德斯特里特诗选|Anne Bradstreet Poems','Anne Bradstreet','P1'),('殖民地—清教徒与早期共和国文学传统','俘虏叙事','玛丽·罗兰森被俘记|The Sovereignty and Goodness of God','Mary Rowlandson','P1'),('殖民地—清教徒与早期共和国文学传统','大觉醒布道','落在愤怒之神手中的罪人|Sinners in the Hands of an Angry God','Jonathan Edwards','P1'),('殖民地—清教徒与早期共和国文学传统','共和国自我塑造','富兰克林自传|The Autobiography of Benjamin Franklin','Benjamin Franklin','P0'),('殖民地—清教徒与早期共和国文学传统','革命政治文体','常识|Common Sense','Thomas Paine','P0'),('殖民地—清教徒与早期共和国文学传统','早期美国小说','威兰|Wieland','Charles Brockden Brown','P1'),
('十九世纪—现代美国文学传统','浪漫主义与罪恶寓言','红字|The Scarlet Letter','Nathaniel Hawthorne','P0'),('十九世纪—现代美国文学传统','海洋史诗与现代性','白鲸|Moby-Dick','Herman Melville','P0'),('十九世纪—现代美国文学传统','超验主义散文','瓦尔登湖|Walden','Henry David Thoreau','P0'),('十九世纪—现代美国文学传统','民主诗学','草叶集|Leaves of Grass','Walt Whitman','P0'),('十九世纪—现代美国文学传统','抒情现代性','狄金森诗选|Emily Dickinson Poems','Emily Dickinson','P1'),('十九世纪—现代美国文学传统','方言与国家反讽','哈克贝利·费恩历险记|Adventures of Huckleberry Finn','Mark Twain','P0'),('十九世纪—现代美国文学传统','国际主题小说','一位女士的画像|The Portrait of a Lady','Henry James','P1'),('十九世纪—现代美国文学传统','女性主体与自然主义转型','觉醒|The Awakening','Kate Chopin','P1'),('十九世纪—现代美国文学传统','都市自然主义','嘉莉妹妹|Sister Carrie','Theodore Dreiser','P1'),('十九世纪—现代美国文学传统','爵士时代','了不起的盖茨比|The Great Gatsby','F. Scott Fitzgerald','P0'),('十九世纪—现代美国文学传统','南方现代主义','喧哗与骚动|The Sound and the Fury','William Faulkner','P0'),('十九世纪—现代美国文学传统','大萧条与迁徙','愤怒的葡萄|The Grapes of Wrath','John Steinbeck','P0'),('十九世纪—现代美国文学传统','战争荒诞小说','第二十二条军规|Catch-22','Joseph Heller','P1'),('十九世纪—现代美国文学传统','反西部史诗','血色子午线|Blood Meridian','Cormac McCarthy','P1'),
('非裔美国文学传统','奴隶叙事经典','弗雷德里克·道格拉斯自传|Narrative of the Life of Frederick Douglass','Frederick Douglass','P0'),('非裔美国文学传统','黑人女性奴隶叙事','一个奴隶女孩生活中的事件|Incidents in the Life of a Slave Girl','Harriet Jacobs','P1'),('非裔美国文学传统','双重意识与思想散文','黑人的灵魂|The Souls of Black Folk','W. E. B. Du Bois','P0'),('非裔美国文学传统','哈莱姆实验小说','甘蔗|Cane','Jean Toomer','P1'),('非裔美国文学传统','黑人女性与民间传统','他们眼望上苍|Their Eyes Were Watching God','Zora Neale Hurston','P0'),('非裔美国文学传统','都市种族现实主义','土生子|Native Son','Richard Wright','P0'),('非裔美国文学传统','身份与不可见性','看不见的人|Invisible Man','Ralph Ellison','P0'),('非裔美国文学传统','宗教—家庭—民权前夜','向苍天呼吁|Go Tell It on the Mountain','James Baldwin','P1'),('非裔美国文学传统','奴隶制记忆与后现代叙事','宠儿|Beloved','Toni Morrison','P0'),('非裔美国文学传统','黑人女性主义','紫色|The Color Purple','Alice Walker','P1'),
('犹太裔美国文学传统','移民都市小说','叫它睡眠|Call It Sleep','Henry Roth','P0'),('犹太裔美国文学传统','战后伦理与贫困','店员|The Assistant','Bernard Malamud','P1'),('犹太裔美国文学传统','知识分子身份小说','赫索格|Herzog','Saul Bellow','P0'),('犹太裔美国文学传统','同化与性政治','波特诺伊的怨诉|Portnoy’s Complaint','Philip Roth','P1'),('犹太裔美国文学传统','浩劫记忆与图像叙事','鼠族|Maus','Art Spiegelman','P0'),('犹太裔美国文学传统','移民—漫画—战争记忆','卡瓦利与克雷的神奇冒险|The Amazing Adventures of Kavalier & Clay','Michael Chabon','P1'),
('亚裔美国文学传统','日裔拘禁后身份','拒绝者|No-No Boy','John Okada','P0'),('亚裔美国文学传统','华裔女性自传混合体','女勇士|The Woman Warrior','Maxine Hong Kingston','P0'),('亚裔美国文学传统','华裔母女与代际','喜福会|The Joy Luck Club','Amy Tan','P1'),('亚裔美国文学传统','韩裔美国都市身份','母语者|Native Speaker','Chang-rae Lee','P1'),('亚裔美国文学传统','南亚裔美国短篇','疾病解说者|Interpreter of Maladies','Jhumpa Lahiri','P0'),('亚裔美国文学传统','亚裔刻板印象与元小说','内景唐人街|Interior Chinatown','Charles Yu','P1'),('亚裔美国文学传统','越裔美国战争记忆','同情者|The Sympathizer','Viet Thanh Nguyen','P0'),
('拉美裔—奇卡诺美国文学传统','奇卡诺成长小说','祝福我，乌尔蒂玛|Bless Me, Ultima','Rudolfo Anaya','P0'),('拉美裔—奇卡诺美国文学传统','奇卡娜都市成长','芒果街上的小屋|The House on Mango Street','Sandra Cisneros','P0'),('拉美裔—奇卡诺美国文学传统','边境理论与混合文体','边境之地/拉弗龙特拉|Borderlands/La Frontera','Gloria Anzaldúa','P0'),('拉美裔—奇卡诺美国文学传统','古巴裔美国离散','梦见古巴|Dreaming in Cuban','Cristina García','P1'),('拉美裔—奇卡诺美国文学传统','多米尼加裔美国跨国小说','奥斯卡·瓦奥短暂而奇妙的一生|The Brief Wondrous Life of Oscar Wao','Junot Díaz','P0'),('拉美裔—奇卡诺美国文学传统','波多黎各移民回忆','我曾是波多黎各人|When I Was Puerto Rican','Esmeralda Santiago','P1'),('拉美裔—奇卡诺美国文学传统','边境工人女性叙事','汤姆ás·里维拉作品集|...y no se lo tragó la tierra','Tomás Rivera','P1'),
('英语加拿大文学传统','加拿大小镇与成长','绿山墙的安妮|Anne of Green Gables','L. M. Montgomery','P0'),('英语加拿大文学传统','小镇讽刺','小镇艳阳录|Sunshine Sketches of a Little Town','Stephen Leacock','P1'),('英语加拿大文学传统','草原女性与现代性','石天使|The Stone Angel','Margaret Laurence','P0'),('英语加拿大文学传统','历史与身份三部曲入口','第五件事|Fifth Business','Robertson Davies','P1'),('英语加拿大文学传统','加拿大女性主义与荒野','浮现|Surfacing','Margaret Atwood','P1'),('英语加拿大文学传统','反乌托邦与全球经典','使女的故事|The Handmaid’s Tale','Margaret Atwood','P0'),('英语加拿大文学传统','移民都市与历史','狮皮之下|In the Skin of a Lion','Michael Ondaatje','P1'),('英语加拿大文学传统','当代多元文化短篇','逃离|Runaway','Alice Munro','P0'),
('法语加拿大—魁北克文学传统','乡土小说传统','玛丽亚·夏普德兰|Maria Chapdelaine','Louis Hémon','P0'),('法语加拿大—魁北克文学传统','都市工人阶级现实主义','锡笛|Bonheur d’occasion','Gabrielle Roy','P0'),('法语加拿大—魁北克文学传统','静默革命戏剧','嫂子们|Les Belles-Sœurs','Michel Tremblay','P0'),('法语加拿大—魁北克文学传统','历史女性小说','卡穆拉斯卡|Kamouraska','Anne Hébert','P1'),('法语加拿大—魁北克文学传统','反传统现代小说','吞噬者|L’Avalée des avalés','Réjean Ducharme','P1'),('法语加拿大—魁北克文学传统','当代移民魁北克','Ru|小溪','Kim Thúy','P1')]

def norm(s): return re.sub(r'[^0-9a-z\u4e00-\u9fff]+','',unicodedata.normalize('NFKC',s).casefold())
def front(text):
 m=re.match(r'^---\s*\n(.*?)\n---\s*\n?',text,re.S); return (m.group(1),m.end()) if m else ('',0)
def scalar(f,key):
 m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',f); return m.group(1).strip(' "\'') if m else ''
def list_field(f,key):
 lines=f.splitlines(); out=[]
 for i,line in enumerate(lines):
  if re.match(rf'^{re.escape(key)}:\s*$',line):
   for n in lines[i+1:]:
    m=re.match(r'^\s*-\s*["\']?(.*?)["\']?\s*$',n)
    if m: out.append(m.group(1)); continue
    if n.strip() and not n.startswith((' ','\t')): break
   return out
 return []
def set_scalar(f,key,val):
 line=f'{key}: "{val}"'
 if re.search(rf'(?m)^{re.escape(key)}:',f): return re.sub(rf'(?m)^{re.escape(key)}:.*$',line,f)
 return f+'\n'+line
def set_list(f,key,vals):
 pat=rf'(?ms)^{re.escape(key)}:\s*\n(?:\s+-.*\n?)*'
 block=key+':\n'+''.join(f'  - "{x}"\n' for x in vals)
 if re.search(pat,f): return re.sub(pat,block,f)
 return f+'\n'+block.rstrip()
def safe_name(s): return re.sub(r'[\\/:*?"<>|]','-',s).strip()

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 idx=[]; before=0
 for p in WORKS.glob('*.md'):
  text=p.read_text(encoding='utf-8-sig'); f,end=front(text)
  if scalar(f,'type')!='work': continue
  names=[scalar(f,'title'),scalar(f,'title_original'),p.stem]+list_field(f,'aliases')
  idx.append([p,text,f,end,{norm(x) for x in names if x}])
  if R5 in list_field(f,'axis_r'): before+=1
 created=[]; reused=[]
 for trad,role,cands,author,prio in SLOTS:
  hit=None
  for cand in cands.split('|'):
   nc=norm(cand)
   for rec in idx:
    if nc and nc in rec[4]: hit=rec; break
   if hit: break
  if hit:
   p,text,f,end,names=hit
   axes=list_field(f,'axis_r')
   if R5 not in axes: axes.append(R5)
   f=set_list(f,'axis_r',axes); f=set_scalar(f,'r5_tradition',trad); f=set_scalar(f,'r5_role',role); f=set_scalar(f,'r5_priority','★' if prio=='P0' else '◆')
   p.write_text('---\n'+f.strip()+'\n---\n'+text[end:].lstrip('\n'),encoding='utf-8'); reused.append(p.stem)
  else:
   title=cands.split('|')[0]; aliases=cands.split('|')[1:]
   p=WORKS/(safe_name(title)+'.md'); n=2
   while p.exists(): p=WORKS/(safe_name(title)+f' ({n}).md'); n+=1
   alias_block='aliases:\n'+''.join(f'  - "{a}"\n' for a in aliases) if aliases else 'aliases: []\n'
   content=f'''---\nid: "WL-WORK-R5-{len(created)+1:03d}"\ntype: work\ntitle: "{title}"\n{alias_block}author: "{author}"\nyear: null\naxis_r:\n  - "{R5}"\nr5_tradition: "{trad}"\nr5_role: "{role}"\nr5_priority: "{'★' if prio=='P0' else '◆'}"\nread_status: "未读"\nverification_status: "结构补全待书目核验"\n---\n\n# {title}\n'''
   p.write_text(content,encoding='utf-8'); created.append(p.name)
   f2,end2=front(content); idx.append([p,content,f2,end2,{norm(title)}|{norm(x) for x in aliases}])
 after=0
 for p in WORKS.glob('*.md'):
  f,_=front(p.read_text(encoding='utf-8-sig'))
  if scalar(f,'type')=='work' and R5 in list_field(f,'axis_r'): after+=1
 by={}
 for trad,_,_,_,_ in SLOTS: by.setdefault(trad,0); by[trad]+=1
 report=['# R5 Structural Completion V1','',f'- Structural slots: **{len(SLOTS)}**',f'- Existing anchors reused/enriched: **{len(reused)}**',f'- Newly created canonical Works: **{len(created)}**',f'- R5 Works before: **{before}**',f'- R5 Works after: **{after}**','','## By tradition']
 for k,v in by.items(): report.append(f'- {k}: **{v}/{v} COVERED**')
 report += ['','## Created']+[f'- {x}' for x in created]+['','## Governance','- Mexico remains R6; U.S. Latino/Chicano works are R5 with R6 interface.','- African American works remain R5 and may also connect R10.2 when diaspora is the primary frame.','- Indigenous North American literature is not partitioned solely by U.S./Canada borders.','- New anchors leave `year: null` pending global bibliographic/T-axis governance.','','`R5_STRUCTURAL_COVERAGE_V1 = 100_PERCENT_COMPLETE`','`R5_TOPIC_MAP_V1 = COMPLETE_USABLE`']
 (OUT/'R5_STRUCTURAL_COMPLETION_V1.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
 home=ROOT/'30 专题'/'R5 北美文学'/'00 北美文学.md'
 if home.exists():
  t=home.read_text(encoding='utf-8'); t=t.replace('structure_status: active','structure_status: complete').replace('`R5_TOPIC_MAP_STRUCTURE = ACTIVE`','`R5_TOPIC_MAP_STRUCTURE = COMPLETE`\n\n`R5_WORK_SUPPORT = COMPLETE`\n\n`R5_TOPIC_MAP_V1 = COMPLETE_USABLE`'); home.write_text(t,encoding='utf-8')
 print('slots',len(SLOTS),'reused',len(reused),'created',len(created),'R5',before,'->',after)
if __name__=='__main__': main()
