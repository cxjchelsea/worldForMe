from __future__ import annotations
import re, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'
WORKS=LIT/'40 作品'
TOPIC=LIT/'30 专题'/'M5.2 权力、身份与世界批评'
NODE=LIT/'20 节点'/'M 思潮'/'M5.2 权力、身份与世界批评.md'
TOPIC_ID='WL-TOPIC-M5.2-POWER-IDENTITY-WORLD'
AXIS='M5.2 权力、身份与世界批评'

# title, author, framework, priority, role, axes
BIB=[
# 后殖民 14
('东方主义','爱德华·萨义德','后殖民','★','理论',['东方主义','表述权力']),
('文化与帝国主义','爱德华·萨义德','后殖民','★','理论',['帝国文化','经典重读']),
('黑皮肤，白面具','弗朗茨·法农','后殖民','★','理论',['殖民主体','种族化']),
('大地上的受苦者','弗朗茨·法农','后殖民','★','理论',['去殖民暴力','民族意识']),
('殖民者与被殖民者','阿尔贝·梅米','后殖民','◆','理论',['殖民关系','身份结构']),
('帝国反写','比尔·阿什克罗夫特、加雷斯·格里菲斯、海伦·蒂芬','后殖民','★','理论',['中心与边缘','语言反写']),
('瓦解','钦努阿·阿契贝','后殖民','★','文学',['殖民遭遇','本土叙事']),
('神箭','钦努阿·阿契贝','后殖民','◆','文学',['殖民制度','宗教权威']),
('一粒麦种','恩古吉·瓦·提安哥','后殖民','★','文学',['独立记忆','背叛与共同体']),
('印度之行','E.M.福斯特','后殖民','◆','文学',['殖民空间','跨文化误读']),
('午夜之子','萨尔曼·鲁西迪','后殖民','★','文学',['国家寓言','混杂身份']),
('微物之神','阿兰达蒂·洛伊','后殖民','★','文学',['种姓','后殖民家庭']),
('河湾','V.S.奈保尔','后殖民','◆','文学',['独立后国家','流动身份']),
('宠儿','托妮·莫里森','后殖民','★','文学',['奴隶制记忆','历史幽灵']),
# 去殖民 10
('去殖民化心灵','恩古吉·瓦·提安哥','去殖民','★','理论',['语言政治','文化去殖民']),
('去殖民化方法论','琳达·图希瓦伊·史密斯','去殖民','★','理论',['研究权力','原住民知识']),
('西方现代性的黑暗面','沃尔特·米格诺洛','去殖民','★','理论',['殖民性','边界思维']),
('地方历史／全球设计','沃尔特·米格诺洛','去殖民','◆','理论',['知识地缘政治','边界思维']),
('权力的殖民性、欧洲中心主义与拉丁美洲','阿尼瓦尔·基哈诺','去殖民','★','理论',['权力殖民性','欧洲中心主义']),
('1492：对他者的遮蔽','恩里克·杜塞尔','去殖民','★','理论',['现代性神话','征服']),
('南方认识论','博阿文图拉·德·索萨·桑托斯','去殖民','◆','理论',['认知正义','南方知识']),
('被压迫者教育学','保罗·弗莱雷','去殖民','★','理论',['解放教育','主体化']),
('世界的词语是森林','厄休拉·勒古恩','去殖民','◆','文学',['殖民暴力','生态帝国主义']),
('羚羊与秧鸡','玛格丽特·阿特伍德','去殖民','◆','文学',['生物资本','知识权力']),
# 女性主义 14
('第二性','西蒙娜·德·波伏瓦','女性主义','★','理论',['他者化','女性主体']),
('一间自己的房间','弗吉尼亚·伍尔夫','女性主义','★','理论',['写作空间','文学制度']),
('性政治','凯特·米利特','女性主义','★','理论',['父权制','文学批评']),
('女性的奥秘','贝蒂·弗里丹','女性主义','◆','理论',['家庭意识形态','第二波女性主义']),
('女性、种族与阶级','安吉拉·戴维斯','女性主义','★','理论',['交叉性前史','种族与阶级']),
('女性主义理论：从边缘到中心','贝尔·胡克斯','女性主义','★','理论',['边缘主体','交叉权力']),
('黑人女性主义思想','帕特里夏·希尔·柯林斯','女性主义','◆','理论',['黑人女性主义','知识生产']),
('姐妹，局外人','奥德丽·洛德','女性主义','★','理论',['差异政治','黑人女性主体']),
('黄色墙纸','夏洛特·珀金斯·吉尔曼','女性主义','★','文学',['医学父权','禁闭空间']),
('她们眼望上苍','佐拉·尼尔·赫斯顿','女性主义','★','文学',['黑人女性主体','声音']),
('紫色','艾丽斯·沃克','女性主义','★','文学',['黑人女性主义','书信主体']),
('女战士','汤亭亭','女性主义','◆','文学',['移民女性','母女叙事']),
('使女的故事','玛格丽特·阿特伍德','女性主义','★','文学',['生殖政治','父权国家']),
('宠儿','托妮·莫里森','女性主义','★','文学',['母职','黑人女性记忆']),
# 酷儿 12
('性史第一卷：认知的意志','米歇尔·福柯','酷儿','★','理论',['性话语','规训权力']),
('性别麻烦','朱迪斯·巴特勒','酷儿','★','理论',['性别表演','异性恋矩阵']),
('身体之重','朱迪斯·巴特勒','酷儿','◆','理论',['身体物质化','规范性']),
('壁橱认识论','伊芙·科索夫斯基·塞奇威克','酷儿','★','理论',['壁橱结构','同性／异性知识']),
('男性之间','伊芙·科索夫斯基·塞奇威克','酷儿','◆','理论',['同性社会欲望','三角关系']),
('酷儿理论导论','安娜玛丽·雅各斯','酷儿','◆','理论',['酷儿谱系','反规范']),
('奥兰多','弗吉尼亚·伍尔夫','酷儿','★','文学',['性别流动','时间与身份']),
('乔瓦尼的房间','詹姆斯·鲍德温','酷儿','★','文学',['同性欲望','羞耻与身份']),
('盐的代价','帕特里夏·海史密斯','酷儿','★','文学',['女同性恋欲望','逃离规范']),
('酷儿','威廉·巴勒斯','酷儿','◆','文学',['同性欲望','边缘生活']),
('阿尔戈号','玛吉·尼尔森','酷儿','★','文学',['酷儿亲密','家庭重构']),
('快乐之家','艾莉森·贝克德尔','酷儿','★','文学',['酷儿自传','父女关系']),
# 生态批评 10
('寂静的春天','蕾切尔·卡森','生态批评','★','理论',['环境毒性','现代性批判']),
('沙乡年鉴','奥尔多·利奥波德','生态批评','★','理论',['土地伦理','生态共同体']),
('瓦尔登湖','亨利·戴维·梭罗','生态批评','◆','理论',['自然书写','反工业生活']),
('环境想象','劳伦斯·布尔','生态批评','★','理论',['环境文本','自然表述']),
('生态批评','格雷格·加勒德','生态批评','★','理论',['生态批评谱系','荒野与污染']),
('无自然的生态学','蒂莫西·莫顿','生态批评','★','理论',['自然概念批判','环境美学']),
('黑暗生态学','蒂莫西·莫顿','生态批评','◆','理论',['共存','非人世界']),
('慢暴力与穷人的环境主义','罗布·尼克松','生态批评','★','理论',['慢暴力','环境正义']),
('与麻烦共处','唐娜·哈拉维','生态批评','★','理论',['多物种共生','世代责任']),
('我们从未现代过','布鲁诺·拉图尔','生态批评','◆','理论',['自然文化','现代性批判']),
# 生态文学 14
('海风下','蕾切尔·卡森','生态文学','◆','文学',['海洋生态','非人视角']),
('白鲸','赫尔曼·梅尔维尔','生态文学','◆','文学',['海洋世界','人类中心主义']),
('世界的词语是森林','厄休拉·勒古恩','生态文学','★','文学',['森林世界','生态殖民主义']),
('播种者寓言','奥克塔维娅·巴特勒','生态文学','★','文学',['气候崩溃','社区韧性']),
('天赋寓言','奥克塔维娅·巴特勒','生态文学','◆','文学',['生态危机','宗教与政治']),
('淹没的世界','J.G.巴拉德','生态文学','★','文学',['气候灾变','深时']),
('路','科马克·麦卡锡','生态文学','★','文学',['生态末日','父子伦理']),
('第五季','N.K.杰米辛','生态文学','★','文学',['地质灾变','环境正义']),
('纽约2140','金·斯坦利·罗宾逊','生态文学','◆','文学',['海平面上升','气候城市']),
('飞行行为','芭芭拉·金索沃','生态文学','★','文学',['气候变化','地方社会']),
('毒木圣经','芭芭拉·金索沃','生态文学','◆','文学',['殖民生态','家庭与土地']),
('洪水之年','玛格丽特·阿特伍德','生态文学','★','文学',['生态宗教','生物灾难']),
('疯癫亚当','玛格丽特·阿特伍德','生态文学','◆','文学',['物种重构','后人类']),
('羚羊与秧鸡','玛格丽特·阿特伍德','生态文学','★','文学',['生物工程','物种伦理']),
]

def norm(s): return re.sub(r'[\s·・\-—_.（）()《》“”"\'：:，,/／]','',s or '').lower()
def fm_parts(text):
    if not text.startswith('---\n'): return None
    end=text.find('\n---\n',4)
    return (text[4:end],text[end+5:]) if end!=-1 else None
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm)
    return m.group(1).strip() if m else ''
def list_values(fm,key):
    lines=fm.splitlines(); out=[]
    for i,line in enumerate(lines):
        if line.startswith(key+':'):
            inline=line.split(':',1)[1].strip()
            if inline.startswith('['): return [x.strip().strip('"\'') for x in inline.strip('[]').split(',') if x.strip()]
            j=i+1
            while j<len(lines) and re.match(r'^\s*- ',lines[j]): out.append(lines[j].split('-',1)[1].strip().strip('"\'')); j+=1
            return out
    return out
def set_list(fm,key,vals):
    vals=list(dict.fromkeys(vals)); lines=fm.splitlines(); i=next((i for i,x in enumerate(lines) if x.startswith(key+':')),None)
    block=[key+':']+[f'- "{v}"' for v in vals]
    if i is None: return fm+'\n'+'\n'.join(block)
    j=i+1
    while j<len(lines) and re.match(r'^\s*- ',lines[j]): j+=1
    lines[i:j]=block; return '\n'.join(lines)
def set_scalar(fm,key,val):
    line=f'{key}: "{val}"'; pat=rf'(?m)^{re.escape(key)}:.*$'
    return re.sub(pat,line,fm,count=1) if re.search(pat,fm) else fm+'\n'+line

def indexes():
    by_title={}; maxid=0
    for p in WORKS.glob('*.md'):
        t=p.read_text(encoding='utf-8'); parts=fm_parts(t)
        if not parts: continue
        fm,_=parts; title=scalar(fm,'title') or p.stem; author=scalar(fm,'author')
        by_title.setdefault(norm(title),[]).append((p,author))
        m=re.search(r'WL-WORK-(\d+)',scalar(fm,'id'))
        if m: maxid=max(maxid,int(m.group(1)))
    return by_title,maxid

def author_compatible(a,b):
    a,b=norm(a),norm(b)
    return bool(a and b and (a==b or a in b or b in a))

def work_text(wid,title,author,framework,priority,role,axes):
    q=lambda s: json.dumps(s,ensure_ascii=False)
    return f'''---\nid: "WL-WORK-{wid:04d}"\ntype: "work"\ntitle: {q(title)}\nauthor: {q(author)}\ntopics:\n- "{TOPIC_ID}"\naxis_m: "{AXIS}"\nm52_priority: {q(priority)}\nm52_framework_cluster: {q(framework)}\nm52_role: {q(role)}\nm52_axes:\n'''+''.join(f'- {q(x)}\n' for x in axes)+'''verification_status: "metadata_pending"\nsource_note: "M5.2 V2 structural bibliography"\n---\n\n# '''+title+'\n'

def update_existing(p,framework,priority,role,axes):
    text=p.read_text(encoding='utf-8'); fm,body=fm_parts(text)
    fm=set_list(fm,'topics',list_values(fm,'topics')+[TOPIC_ID])
    fm=set_scalar(fm,'m52_priority',priority); fm=set_scalar(fm,'m52_framework_cluster',framework); fm=set_scalar(fm,'m52_role',role)
    fm=set_list(fm,'m52_axes',list_values(fm,'m52_axes')+axes)
    # Preserve an existing primary M-axis coordinate for legal multi-topic projections.
    if not scalar(fm,'axis_m'): fm=set_scalar(fm,'axis_m',AXIS)
    p.write_text('---\n'+fm+'\n---\n'+body,encoding='utf-8')

def build_topic():
    files={
'00 权力、身份与世界批评.md':'''---\nid: WL-TOPIC-M5.2-POWER-IDENTITY-WORLD\ntype: literature_topic\nnode: WL-M5.2\nstructure_status: m-axis-v2\ntemplate_version: literature-topic-m-axis-v2\n---\n# M5.2 权力、身份与世界批评\n\n> 核心问题：**谁有权定义主体、文明、性别、知识、文学与世界？被排除的声音如何改变文学的解释框架？**\n\nM5.2 不以共享形式技巧为中心，而研究文学与权力、身份、知识生产和非人世界的关系。\n\n## 三大板块\n1. 殖民与知识权力：后殖民 / 去殖民\n2. 性别、身体与身份：女性主义 / 酷儿\n3. 人类与非人世界：生态批评 / 生态文学\n\n## 边界\n- M4 研究真实发生的集体运动与文学网络；M5.2 研究批评框架与知识权力。\n- M5.1 研究战后文学内部的主体、现实、叙事与文本权威；M5.2 追问谁有资格定义这些概念。\n- “写到女性、殖民或自然”不足以自动进入 M5.2。\n''',
'02 权力、身份与世界批评结构.base':'''filters:\n  and:\n    - file.inFolder("个人通识知识系统_v2_A2/30 世界文学/30 专题/M5.2 权力、身份与世界批评")\nviews:\n  - type: table\n    name: 核心结构\n    order: [file.name]\n''',
'03 权力、身份与世界批评作品.base':f'''filters:\n  and:\n    - type == "work"\n    - topics.contains("{TOPIC_ID}")\nviews:\n  - type: table\n    name: 全部作品\n    order: [m52_priority, m52_framework_cluster, m52_role, author, file.name]\n  - type: table\n    name: ★ 核心\n    filters: m52_priority == "★"\n    order: [m52_framework_cluster, m52_role, author]\n''',
'04 权力、身份与世界批评书目覆盖审计.md':'# M5.2 权力、身份与世界批评书目覆盖审计\n\n> 状态：待独立审计。\n',
'10 核心结构/01 定义与边界.md':'# 定义与边界\n\nM5.2 研究文学解释框架如何重审帝国、父权、性规范、知识制度与人类中心主义。\n',
'10 核心结构/02 历史条件与问题意识.md':'# 历史条件与问题意识\n\n去殖民化、民权运动、第二波女性主义、性解放、环境危机与知识制度反思共同改变了文学批评。\n',
'10 核心结构/03 批评谱系与内部结构.md':'# 批评谱系与内部结构\n\n殖民与知识权力 / 性别身体与身份 / 人类与非人世界构成三条主线。\n',
'10 核心结构/04 权力机制与文学重读.md':'# 权力机制与文学重读\n\n关注表述权、他者化、规范性、交叉权力、知识殖民性、环境正义与多物种关系。\n',
'10 核心结构/05 传播、地域与非同步性.md':'# 传播、地域与非同步性\n\n这些框架在不同地区出现时间、政治背景与理论语言并不同步，禁止把单一路径全球化。\n',
'10 核心结构/06 与M4、M5.1的边界.md':'# 与 M4、M5.1 的边界\n\nM4=运动/共同体/网络；M5.1=战后美学与叙事范式；M5.2=权力、身份与知识批评框架。\n',
'10 核心结构/07 阅读路线.md':'# 阅读路线\n\n建议先读框架奠基文本，再以文学作品验证框架如何改变“谁能说话、谁被看见、世界如何被定义”。\n',
'11 主要框架/00 主要框架索引.md':'# 主要框架索引\n\n- 后殖民\n- 去殖民\n- 女性主义\n- 酷儿\n- 生态批评\n- 生态文学\n',
'12 权力机制/00 权力机制索引.md':'# 权力机制索引\n\n表述权 / 殖民性 / 他者化 / 父权制 / 性别表演 / 交叉性 / 环境正义 / 人类中心主义 / 多物种共生。\n',
'13 边界与转型/00 边界与转型索引.md':'# 边界与转型索引\n\nM4 的历史运动可被 M5.2 的后殖民、女性主义与酷儿框架重新解释；生态批评则把权力问题扩展到非人世界。\n',
}
    for i,name in enumerate(['后殖民','去殖民','女性主义','酷儿','生态批评','生态文学'],1):
        files[f'11 主要框架/{i:02d} {name}.md']=f'# {name}\n\n本页用于组织 {name} 的核心问题、理论文本、文学实践与边界。\n'
    canvas={"nodes":[
        {"id":"q","type":"text","text":"谁有权定义主体、文明、性别、知识与世界？","x":0,"y":0,"width":360,"height":100},
        {"id":"c","type":"text","text":"殖民与知识权力\n后殖民 / 去殖民","x":-420,"y":180,"width":280,"height":120},
        {"id":"g","type":"text","text":"性别、身体与身份\n女性主义 / 酷儿","x":0,"y":180,"width":280,"height":120},
        {"id":"e","type":"text","text":"人类与非人世界\n生态批评 / 生态文学","x":420,"y":180,"width":280,"height":120}],
        "edges":[{"id":"e1","fromNode":"q","toNode":"c"},{"id":"e2","fromNode":"q","toNode":"g"},{"id":"e3","fromNode":"q","toNode":"e"}]}
    files['01 权力、身份与世界批评.canvas']=json.dumps(canvas,ensure_ascii=False,indent=2)
    for rel,content in files.items():
        p=TOPIC/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding='utf-8')

def update_node():
    text=NODE.read_text(encoding='utf-8')
    text=text.replace('topic_map: null','topic_map: "../../30 专题/M5.2 权力、身份与世界批评/00 权力、身份与世界批评.md"')
    text=text.replace('> 暂未接入。','> 已接入：[[../../30 专题/M5.2 权力、身份与世界批评/00 权力、身份与世界批评|M5.2 权力、身份与世界批评专题地图]]。')
    NODE.write_text(text,encoding='utf-8')

def main():
    build_topic(); update_node(); by_title,maxid=indexes(); reused=created=0; collisions=[]
    for title,author,framework,priority,role,axes in BIB:
        candidates=by_title.get(norm(title),[]); match=next((p for p,a in candidates if author_compatible(a,author)),None)
        if match:
            update_existing(match,framework,priority,role,axes); reused+=1
        else:
            if candidates: collisions.append((title,author,[a for _,a in candidates]))
            maxid+=1; name=title+'.md'
            if candidates or (WORKS/name).exists(): name=f'{title}（{author}）.md'
            p=WORKS/name; p.write_text(work_text(maxid,title,author,framework,priority,role,axes),encoding='utf-8'); created+=1
            by_title.setdefault(norm(title),[]).append((p,author))
    print(f'target={len(BIB)} reused={reused} created={created}')
    print(Counter(x[2] for x in BIB)); print('collisions=',collisions)

if __name__=='__main__': main()
