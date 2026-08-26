from __future__ import annotations
import hashlib,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
WORKS=LIT/'40 作品'
TOPIC=LIT/'30 专题'/'M4 集体文学运动与文化政治'
NODE=LIT/'20 节点'/'M 思潮'/'M4 政治、民族与文化运动.md'
TOPIC_ID='WL-TOPIC-M4-COLLECTIVE-MOVEMENTS'
AXIS='M4 集体文学运动与文化政治'
BIB=[
('潘塔德乌什','亚当·密茨凯维奇','民族主义文学','★',['民族史诗','波兰民族想象']),('先人祭','亚当·密茨凯维奇','民族主义文学','★',['民族记忆','浪漫民族主义']),('婚约','亚历山德罗·曼佐尼','民族主义文学','★',['语言统一','民族历史']),('卡勒瓦拉','埃利亚斯·伦罗特','民族主义文学','★',['民间传统','民族史诗']),('民族之歌','裴多菲·山陀尔','民族主义文学','★',['革命民族主义','公共诗歌']),('凯尔特曙光','W.B.叶芝','民族主义文学','◆',['文化复兴','凯尔特传统']),('胡里痕的凯瑟琳','W.B.叶芝','民族主义文学','◆',['民族寓言','戏剧动员']),('阿难陀寺','班金·钱德拉·查特吉','民族主义文学','★',['反殖民民族主义','宗教共同体']),('戈拉','拉宾德拉纳特·泰戈尔','民族主义文学','★',['民族身份','宗教与国家']),('家庭与世界','拉宾德拉纳特·泰戈尔','民族主义文学','★',['民族主义反思','家庭与政治']),
('母亲','马克西姆·高尔基','无产阶级文学','★',['阶级觉醒','革命主体']),('蟹工船','小林多喜二','无产阶级文学','★',['劳动剥削','集体行动']),('党生活者','小林多喜二','无产阶级文学','◆',['组织生活','地下政治']),('没有钱的犹太人','迈克·戈尔德','无产阶级文学','★',['工人阶级','移民城市']),('大地之女','艾格尼丝·史沫特莱','无产阶级文学','◆',['女性劳动','阶级流动']),('被剥夺的人们','杰克·康罗伊','无产阶级文学','◆',['失业','工人共同体']),('屠场','厄普顿·辛克莱','无产阶级文学','★',['工业资本','劳动条件']),('石油！','厄普顿·辛克莱','无产阶级文学','◆',['资本与劳动','产业政治']),('丰收之歌','艾拉·沃尔夫特','无产阶级文学','◆',['劳动组织','阶级叙事']),('矿井','夏目漱石','无产阶级文学','◆',['劳动空间','现代异化']),
('咆哮了的土地','蒋光慈','革命文学','★',['左翼文学','农民革命']),('短裤党','蒋光慈','革命文学','◆',['革命青年','阶级斗争']),('一九三〇年春上海','丁玲','革命文学','★',['左翼都市','革命主体']),('二月','柔石','革命文学','★',['知识分子革命','伦理冲突']),('为奴隶的母亲','柔石','革命文学','★',['阶级压迫','女性劳动']),('包身工','夏衍','革命文学','★',['劳动剥削','报告文学']),('子夜','茅盾','革命文学','★',['左翼现实主义','资本主义都市']),('春蚕','茅盾','革命文学','◆',['农村经济','阶级结构']),('毁灭','巴金','革命文学','◆',['革命青年','无政府主义']),('新儿女英雄传','袁静、孔厥','革命文学','◆',['抗战动员','群众叙事']),
('钢铁是怎样炼成的','尼古拉·奥斯特洛夫斯基','社会主义现实主义','★',['新人塑造','革命伦理']),('水泥','费奥多尔·格拉德科夫','社会主义现实主义','★',['工业建设','革命后社会']),('恰巴耶夫','德米特里·富尔曼诺夫','社会主义现实主义','★',['革命英雄','红军叙事']),('毁灭（法捷耶夫）','亚历山大·法捷耶夫','社会主义现实主义','★',['革命集体','内战']),('被开垦的处女地','米哈伊尔·肖洛霍夫','社会主义现实主义','★',['集体化','农村改造']),('青年近卫军','亚历山大·法捷耶夫','社会主义现实主义','★',['英雄集体','战争动员']),('太阳照在桑干河上','丁玲','社会主义现实主义','★',['土地改革','农村阶级']),('暴风骤雨','周立波','社会主义现实主义','★',['土地改革','群众叙事']),('林海雪原','曲波','社会主义现实主义','◆',['革命英雄','通俗叙事']),('红岩','罗广斌、杨益言','社会主义现实主义','◆',['革命记忆','烈士叙事']),
('甘蔗','让·图默','哈莱姆文艺复兴','★',['黑人现代主义','南北迁徙']),('疲惫的布鲁斯','兰斯顿·休斯','哈莱姆文艺复兴','★',['爵士诗学','黑人公共文化']),('哈莱姆之家','克劳德·麦凯','哈莱姆文艺复兴','★',['都市黑人生活','侨民经验']),('越界','内拉·拉森','哈莱姆文艺复兴','★',['种族身份','表演性']),('流沙','内拉·拉森','哈莱姆文艺复兴','★',['黑人女性主体','跨大西洋']),('他们眼望上苍','佐拉·尼尔·赫斯顿','哈莱姆文艺复兴','★',['黑人女性主体','口语传统']),('黑莓','华莱士·瑟曼','哈莱姆文艺复兴','◆',['肤色政治','都市文化']),('并非没有笑声','兰斯顿·休斯','哈莱姆文艺复兴','◆',['黑人家庭','阶级']),('梅子包','杰西·雷德蒙·福塞特','哈莱姆文艺复兴','◆',['黑人中产','性别']),('上帝的长号','詹姆斯·韦尔登·约翰逊','哈莱姆文艺复兴','◆',['布道传统','黑人宗教文化']),
('返乡笔记','艾梅·塞泽尔','Négritude','★',['黑人主体','殖民异化']),('颜料','莱昂-贡特朗·达马斯','Négritude','★',['殖民语言','黑人身体']),('黑色祭品','莱奥波德·塞达尔·桑戈尔','Négritude','★',['黑人文化','战争经验']),('阴影之歌','莱奥波德·塞达尔·桑戈尔','Négritude','★',['非洲文化','抒情共同体']),('埃塞俄比亚颂','莱奥波德·塞达尔·桑戈尔','Négritude','◆',['非洲文明','文化认同']),('黑色标签','莱昂-贡特朗·达马斯','Négritude','◆',['种族暴力','殖民现代性']),('巴黎蜃景','奥斯曼·索塞','Négritude','◆',['殖民都市','非洲侨民']),('克林比耶','贝尔纳·达迪耶','Négritude','◆',['殖民教育','身份形成']),
('瓦解','钦努阿·阿契贝','反殖民文学运动','★',['殖民冲突','本土社会']),('神箭','钦努阿·阿契贝','反殖民文学运动','★',['殖民制度','宗教权威']),('人民公仆','钦努阿·阿契贝','反殖民文学运动','◆',['独立后政治','腐败']),('一粒麦种','恩古吉·瓦·提安哥','反殖民文学运动','★',['民族解放','背叛与共同体']),('孩子，你别哭','恩古吉·瓦·提安哥','反殖民文学运动','★',['殖民教育','土地']),('血色花瓣','恩古吉·瓦·提安哥','反殖民文学运动','◆',['新殖民主义','阶级']),('神的木片','奥斯曼·森贝纳','反殖民文学运动','★',['铁路罢工','集体行动']),('穷人的基督','蒙戈·贝蒂','反殖民文学运动','★',['传教殖民','文化冲突']),('家丁','费迪南·奥约诺','反殖民文学运动','◆',['殖民行政','讽刺']),('回归故里','塔伊布·萨利赫','反殖民文学运动','★',['殖民凝视','返乡']),('河湾','V.S.奈保尔','反殖民文学运动','◆',['后殖民国家','历史断裂']),('印度之行','E.M.福斯特','反殖民文学运动','◆',['帝国关系','殖民司法']),
('在路上','杰克·凯鲁亚克','垮掉的一代','★',['流动生活','反文化']),('达摩流浪者','杰克·凯鲁亚克','垮掉的一代','★',['禅宗想象','反消费']),('大瑟尔','杰克·凯鲁亚克','垮掉的一代','◆',['反文化疲惫','自我神话']),('嚎叫','艾伦·金斯堡','垮掉的一代','★',['公共朗诵','反规范']),('卡迪什','艾伦·金斯堡','垮掉的一代','◆',['家庭创伤','长诗']),('裸体午餐','威廉·S.巴勒斯','垮掉的一代','★',['拼贴','毒品文化']),('瘾君子','威廉·S.巴勒斯','垮掉的一代','◆',['地下文化','成瘾']),('酷儿','威廉·S.巴勒斯','垮掉的一代','◆',['同性欲望','边缘身份']),('康尼岛的心灵','劳伦斯·费林盖蒂','垮掉的一代','★',['城市诗歌','公共文化']),('汽油','格雷戈里·科索','垮掉的一代','◆',['即兴诗学','青年反叛']),
('跳房子','胡里奥·科塔萨尔','拉丁美洲Boom','★',['跨国作家网络','形式实验']),('百年孤独','加西亚·马尔克斯','拉丁美洲Boom','★',['全球出版','家族与国家']),('阿尔特米奥·克罗斯之死','卡洛斯·富恩特斯','拉丁美洲Boom','★',['革命记忆','国家历史']),('城市与狗','马里奥·巴尔加斯·略萨','拉丁美洲Boom','★',['军事制度','形式实验']),('酒吧长谈','马里奥·巴尔加斯·略萨','拉丁美洲Boom','★',['独裁社会','多声部']),('绿房子','马里奥·巴尔加斯·略萨','拉丁美洲Boom','◆',['多线叙事','边疆现代性']),('夜鸟','何塞·多诺索','拉丁美洲Boom','◆',['怪诞','家族权力']),('三只忧伤的老虎','吉列尔莫·卡夫雷拉·因凡特','拉丁美洲Boom','◆',['古巴都市','语言游戏']),('天堂','何塞·莱萨马·利马','拉丁美洲Boom','◆',['巴洛克语言','文化谱系']),('大教堂爆炸','阿莱霍·卡彭铁尔','拉丁美洲Boom','★',['革命历史','跨大西洋'])]

def norm(s): return re.sub(r'[\s·・\-—_.（）()《》“”"\'：:，,！!？?]','',s).lower()
def fm_parts(text):
    if not text.startswith('---\n'): return None
    end=text.find('\n---\n',4)
    return (text[4:end],text[end+5:]) if end!=-1 else None
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm); return m.group(1).strip() if m else ''
def union_list(fm,key,vals):
    lines=fm.splitlines(); i=next((i for i,x in enumerate(lines) if re.match(rf'^{re.escape(key)}:',x)),None)
    if i is None: return fm+'\n'+key+':\n'+'\n'.join(f'- {v}' for v in vals)
    old=[]; j=i+1; inline=lines[i].split(':',1)[1].strip()
    if inline.startswith('['): old=[x.strip(' "\'') for x in inline.strip('[]').split(',') if x.strip()]
    else:
        while j<len(lines) and re.match(r'^\s*- ',lines[j]): old.append(lines[j].split('-',1)[1].strip().strip('"\'')); j+=1
    new=old+[v for v in vals if v not in old]
    lines[i:j]=[key+':']+[f'- {v}' for v in new]; return '\n'.join(lines)
def set_scalar(fm,key,val):
    line=f'{key}: "{val}"'; pat=rf'(?m)^{re.escape(key)}:.*$'
    return re.sub(pat,line,fm,count=1) if re.search(pat,fm) else fm+'\n'+line

def existing_index():
    out={}
    for p in WORKS.glob('*.md'):
        t=p.read_text(encoding='utf-8'); parts=fm_parts(t)
        if not parts: continue
        fm,_=parts; title=scalar(fm,'title') or p.stem; author=scalar(fm,'author')
        out.setdefault(norm(title),[]).append((p,author,t))
    return out

def update_existing(p,text,movement,priority,axes):
    fm,body=fm_parts(text); fm=union_list(fm,'axis_m',[AXIS]); fm=union_list(fm,'topics',[TOPIC_ID])
    fm=set_scalar(fm,'m4_priority',priority); fm=set_scalar(fm,'m4_movement_cluster',movement); fm=union_list(fm,'m4_axes',axes)
    p.write_text('---\n'+fm+'\n---\n'+body,encoding='utf-8')

def create_work(title,author,movement,priority,axes):
    stem=title; p=WORKS/(stem+'.md'); n=2
    while p.exists(): p=WORKS/(f'{stem}（{author}）.md' if n==2 else f'{stem}（{author}{n}）.md'); n+=1
    hid=hashlib.sha1((title+'|'+author).encode()).hexdigest()[:8]
    fm=f'''id: WL-WORK-M4-{hid}\ntype: work\ntitle: "{title}"\naliases: []\nauthor: "{author}"\nyear: null\nread_status: 未读\naxis_t: []\naxis_r: []\naxis_m:\n- {AXIS}\naxis_g: []\naxis_q: []\naxis_source: manual_m4_structural_gap_fill_v1\ntopics:\n- {TOPIC_ID}\ntopic_links: []\nm4_priority: "{priority}"\nm4_movement_cluster: "{movement}"\nm4_axes:\n'''+''.join(f'- {x}\n' for x in axes)+'''verification_status: 手工核验\nbibliography_status: structural_anchor_metadata_pending'''
    body=f'''# {title}\n\n## M4 专题角色\n\n- 运动：{movement}\n- 专题优先级：{priority}\n- 机制：{' / '.join(axes)}\n\n> M4 Structural Gap Fill V1：用于补齐集体文学运动与文化政治的结构槽位；年份、原文题名等通用书目字段留待中央作品库统一校验。\n'''
    p.write_text('---\n'+fm+'\n---\n'+body,encoding='utf-8')

def write_topic_files():
    TOPIC.mkdir(parents=True,exist_ok=True)
    (TOPIC/'10 核心结构').mkdir(exist_ok=True); (TOPIC/'11 主要运动').mkdir(exist_ok=True); (TOPIC/'12 集体机制').mkdir(exist_ok=True); (TOPIC/'13 边界与转型').mkdir(exist_ok=True)
    home='''---\nid: WL-TOPIC-M4-COLLECTIVE-MOVEMENTS\ntype: literature_topic\ncode: M4\nname: 集体文学运动与文化政治\naxis: M\nstructure_status: m-axis-v2\ntemplate_version: literature-topic-m-axis-v2\n---\n# M4 集体文学运动与文化政治\n\n> 核心问题：**文学如何从个人美学选择变成群体身份、政治行动、文化解放与跨国文学网络？**\n\n## 三大结构\n\n1. **政治与阶级文学**：民族主义文学、无产阶级文学、革命文学、社会主义现实主义。\n2. **身份与文化解放运动**：哈莱姆文艺复兴、Négritude、反殖民文学运动。\n3. **文学群体与跨国网络**：垮掉的一代、拉丁美洲 Boom。\n\nM4 不等于“所有政治文学”。作品只有在真实运动、共同体、组织纲领或跨国网络中具有结构意义时才进入。Boom 是文学网络与出版现象，魔幻现实主义归 M5.1；后殖民/去殖民作为批评框架归 M5.2。\n'''
    (TOPIC/'00 集体文学运动与文化政治.md').write_text(home,encoding='utf-8')
    canvas='{"nodes":[{"id":"q","type":"text","text":"文学如何成为集体历史行动？","x":0,"y":0,"width":320,"height":80},{"id":"p","type":"text","text":"政治与阶级文学","x":-420,"y":180,"width":260,"height":70},{"id":"i","type":"text","text":"身份与文化解放","x":0,"y":180,"width":260,"height":70},{"id":"n","type":"text","text":"文学群体与跨国网络","x":420,"y":180,"width":280,"height":70}],"edges":[{"id":"e1","fromNode":"q","toNode":"p"},{"id":"e2","fromNode":"q","toNode":"i"},{"id":"e3","fromNode":"q","toNode":"n"}]}'
    (TOPIC/'01 集体文学运动与文化政治.canvas').write_text(canvas,encoding='utf-8')
    (TOPIC/'02 集体文学运动与文化政治结构.base').write_text('filters:\n  and:\n    - file.inFolder("10 核心结构") || file.inFolder("11 主要运动") || file.inFolder("12 集体机制") || file.inFolder("13 边界与转型")\nviews:\n  - type: table\n    name: 结构\n',encoding='utf-8')
    (TOPIC/'03 集体文学运动与文化政治作品.base').write_text(f'filters:\n  and:\n    - type == "work"\n    - topics.contains("{TOPIC_ID}")\nviews:\n  - type: table\n    name: 全部作品\n    order: [file.name, m4_priority, m4_movement_cluster, m4_axes]\n',encoding='utf-8')
    cores={
    '01 定义与边界.md':'M4 研究真实发生的集体文学运动、文化共同体、政治纲领与跨国网络，而不是把所有政治主题作品都收入。',
    '02 历史条件与问题意识.md':'民族国家、工业资本、阶级政治、殖民主义、种族秩序、革命与全球出版市场共同塑造集体文学行动。',
    '03 运动谱系与内部结构.md':'政治与阶级文学 / 身份与文化解放 / 文学群体与跨国网络三组并行，并允许跨组连接。',
    '04 集体机制与文学行动.md':'重点观察宣言、组织、杂志、朗诵、出版社、作家网络、群众动员、文化复兴与制度化规范。',
    '05 传播、地域与非同步性.md':'同一运动在不同地区并不同步；跨国传播必须通过翻译、出版、流亡、殖民网络与政治组织来解释。',
    '06 与M3、M5.1、M5.2的边界.md':'M3 看形式与先锋制度挑战；M4 看集体行动；M5.1 看战后美学范式；M5.2 看权力与知识批评框架。',
    '07 阅读路线.md':'先读每个运动的 ★ 骨架，再按“阶级 / 种族 / 殖民 / 反文化 / 出版网络”等机制跨运动比较。'}
    for fn,txt in cores.items(): (TOPIC/'10 核心结构'/fn).write_text('# '+fn[3:-3]+'\n\n'+txt+'\n',encoding='utf-8')
    groups=['民族主义文学','无产阶级文学','革命文学','社会主义现实主义','哈莱姆文艺复兴','Négritude','反殖民文学运动','垮掉的一代','拉丁美洲Boom']
    (TOPIC/'11 主要运动'/'00 主要运动索引.md').write_text('# 主要运动索引\n\n'+'\n'.join(f'- [[{i+1:02d} {g}|{g}]]' for i,g in enumerate(groups))+'\n',encoding='utf-8')
    for i,g in enumerate(groups): (TOPIC/'11 主要运动'/f'{i+1:02d} {g}.md').write_text(f'# {g}\n\n> 通过 M4 作品 Base 查看该运动的 ★ / ◆ 作品与机制。\n',encoding='utf-8')
    (TOPIC/'12 集体机制'/'00 集体机制索引.md').write_text('# 集体机制索引\n\n- 组织与宣言\n- 群众动员\n- 民族与语言建构\n- 阶级共同体\n- 种族文化复兴\n- 反殖民文化行动\n- 朗诵、杂志与小型出版社\n- 国际出版与作家网络\n',encoding='utf-8')
    (TOPIC/'13 边界与转型'/'00 边界与转型索引.md').write_text('# 边界与转型索引\n\n- 民族主义文学 ↔ M2 浪漫主义/现实主义\n- 无产阶级与革命文学 ↔ M3.2 先锋派\n- Harlem / Négritude / 反殖民 ↔ M5.2\n- Boom ↔ M5.1 魔幻现实主义\n',encoding='utf-8')

def update_node():
    text=NODE.read_text(encoding='utf-8'); text=text.replace('topic_map: null','topic_map: "[[../../30 专题/M4 集体文学运动与文化政治/00 集体文学运动与文化政治|M4 集体文学运动与文化政治]]"')
    text=text.replace('> 暂未接入。后续专题内部建议按“政治与阶级文学 / 身份与文化解放运动 / 文学群体与跨国网络”三组展开。','[[../../30 专题/M4 集体文学运动与文化政治/00 集体文学运动与文化政治|进入 M4 专题地图]]')
    NODE.write_text(text,encoding='utf-8')

def main():
    write_topic_files(); update_node(); idx=existing_index(); reused=created=0; collisions=[]
    for title,author,movement,priority,axes in BIB:
        candidates=idx.get(norm(title),[]); matched=None
        for p,a,t in candidates:
            if not a or norm(author) in norm(a) or norm(a) in norm(author): matched=(p,t); break
        if matched:
            update_existing(matched[0],matched[1],movement,priority,axes); reused+=1
        else:
            if candidates: collisions.append((title,author,[a for _,a,_ in candidates]))
            create_work(title,author,movement,priority,axes); created+=1
    print(f'target={len(BIB)} reused={reused} created={created}')
    print(Counter(x[2] for x in BIB)); print('collisions=',collisions)
if __name__=='__main__': main()
