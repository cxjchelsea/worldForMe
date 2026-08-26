from __future__ import annotations
import hashlib,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LIT=ROOT/'个人通识知识系统_v2_A2'/'30 世界文学'; WORKS=LIT/'40 作品'; TOPIC=LIT/'30 专题'/'M5.1 战后思想与美学范式'
TOPIC_ID='WL-TOPIC-M5.1-POSTWAR-AESTHETICS'; AXIS='M5.1 战后思想与美学范式'
BIB=[
('恶心','让-保罗·萨特','存在主义','★',['存在危机','偶然性']),('墙','让-保罗·萨特','存在主义','◆',['自由选择','死亡']),('禁闭','让-保罗·萨特','存在主义','★',['他人凝视','自由选择']),('肮脏的手','让-保罗·萨特','存在主义','◆',['政治责任','自由选择']),('自由之路','让-保罗·萨特','存在主义','◆',['自由选择','历史处境']),('局外人','阿尔贝·加缪','存在主义','★',['荒诞意识','疏离']),('西西弗神话','阿尔贝·加缪','存在主义','★',['荒诞意识','反抗']),('鼠疫','阿尔贝·加缪','存在主义','★',['共同体伦理','反抗']),('堕落','阿尔贝·加缪','存在主义','★',['罪责','自我审判']),('女宾','西蒙娜·德·波伏瓦','存在主义','◆',['自由选择','女性主体']),('名士风流','西蒙娜·德·波伏瓦','存在主义','★',['知识分子','战后政治']),('人都是要死的','西蒙娜·德·波伏瓦','存在主义','◆',['时间','有限性']),('人的境况','安德烈·马尔罗','存在主义','◆',['行动','历史处境']),('他人的血','西蒙娜·德·波伏瓦','存在主义','◆',['责任','抵抗']),
('等待戈多','塞缪尔·贝克特','荒诞','★',['等待','语言失效']),('终局','塞缪尔·贝克特','荒诞','★',['封闭空间','语言失效']),('克拉普的最后一盘磁带','塞缪尔·贝克特','荒诞','◆',['记忆','媒介']),('快乐时光','塞缪尔·贝克特','荒诞','◆',['身体困境','重复']),('秃头歌女','欧仁·尤内斯库','荒诞','★',['语言失效','日常异化']),('上课','欧仁·尤内斯库','荒诞','◆',['权力','语言暴力']),('犀牛','欧仁·尤内斯库','荒诞','★',['从众','政治寓言']),('椅子','欧仁·尤内斯库','荒诞','◆',['空缺','交流失败']),('动物园故事','爱德华·阿尔比','荒诞','◆',['都市疏离','交流失败']),('罗森格兰兹与吉尔登斯吞死了','汤姆·斯托帕德','荒诞','★',['元戏剧','偶然性']),('生日晚会','哈罗德·品特','荒诞','◆',['威胁','身份不稳']),('送菜升降机','哈罗德·品特','荒诞','◆',['权力','等待']),
('嫉妒','阿兰·罗伯-格里耶','法国新小说','★',['物的凝视','去心理化']),('橡皮','阿兰·罗伯-格里耶','法国新小说','★',['侦探解构','循环叙事']),('窥视者','阿兰·罗伯-格里耶','法国新小说','◆',['物的凝视','不可靠感知']),('在迷宫中','阿兰·罗伯-格里耶','法国新小说','◆',['空间迷宫','叙事不确定']),('向性','娜塔莉·萨洛特','法国新小说','★',['前意识','微观心理']),('马特罗','娜塔莉·萨洛特','法国新小说','◆',['去人物化','话语张力']),('天象馆','娜塔莉·萨洛特','法国新小说','◆',['话语张力','社会感知']),('变','米歇尔·布托尔','法国新小说','★',['第二人称','时间结构']),('弗兰德公路','克洛德·西蒙','法国新小说','★',['记忆碎片','战争经验']),('宫殿','克洛德·西蒙','法国新小说','◆',['历史碎片','感知重组']),
('人间王国','阿莱霍·卡彭铁尔','魔幻现实主义','★',['神奇现实','殖民历史']),('玉米人','米格尔·安赫尔·阿斯图里亚斯','魔幻现实主义','★',['神话现实','原住民世界']),('佩德罗·巴拉莫','胡安·鲁尔福','魔幻现实主义','★',['亡灵叙事','乡土现代性']),('百年孤独','加西亚·马尔克斯','魔幻现实主义','★',['循环时间','家族历史']),('族长的秋天','加西亚·马尔克斯','魔幻现实主义','★',['独裁寓言','循环句法']),('幽灵之家','伊莎贝尔·阿连德','魔幻现实主义','★',['家族记忆','政治暴力']),('恰似水之于巧克力','劳拉·埃斯基韦尔','魔幻现实主义','◆',['日常魔幻','女性经验']),('午夜之子','萨尔曼·鲁西迪','魔幻现实主义','★',['国家寓言','历史与身体']),('羞耻','萨尔曼·鲁西迪','魔幻现实主义','◆',['国家寓言','政治神话']),('宠儿','托妮·莫里森','魔幻现实主义','★',['幽灵叙事','奴隶制记忆']),('所罗门之歌','托妮·莫里森','魔幻现实主义','★',['神话谱系','黑人记忆']),('铁皮鼓','君特·格拉斯','魔幻现实主义','★',['怪诞历史','战争记忆']),('大师与玛格丽特','米哈伊尔·布尔加科夫','魔幻现实主义','★',['魔鬼叙事','现实层级']),('马戏团之夜','安吉拉·卡特','魔幻现实主义','◆',['身体奇观','女性主义重写']),('饥饿之路','本·奥克里','魔幻现实主义','★',['灵界现实','后殖民城市']),('梦游之地','米亚·科托','魔幻现实主义','★',['战争创伤','口述神话']),('红高粱家族','莫言','魔幻现实主义','★',['民间叙事','暴力与生命']),('莫雷尔的发明','阿道夫·比奥伊·卡萨雷斯','魔幻现实主义','◆',['现实层级','技术幻象']),('消逝的足迹','阿莱霍·卡彭铁尔','魔幻现实主义','◆',['神奇现实','文明时间']),
('虚构集','豪尔赫·路易斯·博尔赫斯','后现代主义','★',['元小说','无限文本']),('阿莱夫','豪尔赫·路易斯·博尔赫斯','后现代主义','★',['无限空间','文本迷宫']),('跳房子','胡里奥·科塔萨尔','后现代主义','★',['开放结构','读者参与']),('微暗的火','弗拉基米尔·纳博科夫','后现代主义','★',['伪注释','不可靠文本']),('V.','托马斯·品钦','后现代主义','◆',['熵','阴谋叙事']),('拍卖第四十九批','托马斯·品钦','后现代主义','★',['阴谋叙事','符号过载']),('万有引力之虹','托马斯·品钦','后现代主义','★',['系统小说','熵']),('迷失在游乐园','约翰·巴思','后现代主义','★',['元小说','叙事自反']),('烟草经纪人','约翰·巴思','后现代主义','◆',['历史戏仿','互文']),('白雪公主','唐纳德·巴塞尔姆','后现代主义','◆',['拼贴','童话重写']),('美国通用棒球协会','罗伯特·库弗','后现代主义','◆',['游戏结构','虚构世界']),('第五号屠宰场','库尔特·冯内古特','后现代主义','★',['时间跳跃','战争反叙事']),('寒冬夜行人','伊塔洛·卡尔维诺','后现代主义','★',['读者参与','元小说']),('宇宙奇趣','伊塔洛·卡尔维诺','后现代主义','◆',['科学寓言','形式游戏']),('玫瑰的名字','翁贝托·埃科','后现代主义','★',['历史戏仿','符号学']),('傅科摆','翁贝托·埃科','后现代主义','◆',['阴谋叙事','符号过载']),('人生拼图版','乔治·佩雷克','后现代主义','★',['约束写作','空间结构']),('纽约三部曲','保罗·奥斯特','后现代主义','★',['侦探解构','身份迷失']),('白噪音','唐·德里罗','后现代主义','★',['媒介社会','消费文化']),('地下世界','唐·德里罗','后现代主义','◆',['系统小说','冷战记忆']),('芒博琼博','伊什梅尔·里德','后现代主义','◆',['黑人后现代','文化拼贴']),('高中生的血与勇气','凯西·阿克','后现代主义','◆',['挪用写作','身体政治']),('叶之屋','马克·Z. 丹尼尔斯基','后现代主义','★',['版面实验','嵌套文本']),('无尽的玩笑','大卫·福斯特·华莱士','后现代主义','★',['媒介成瘾','系统小说']),('法国中尉的女人','约翰·福尔斯','后现代主义','★',['元历史','多重结局'])]

def norm(s): return re.sub(r'[\s·・\-—_.（）()《》“”"\'：:，,]','',s).lower()
def fm_parts(text):
    if not text.startswith('---\n'): return None
    end=text.find('\n---\n',4)
    return (text[4:end],text[end+5:]) if end!=-1 else None
def scalar(fm,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$',fm); return m.group(1).strip() if m else ''
def union_list(fm,key,vals):
    lines=fm.splitlines(); i=next((i for i,x in enumerate(lines) if re.match(rf'^{re.escape(key)}:',x)),None)
    if i is None: return fm+'\n'+key+':\n'+'\n'.join(f'- {v}' for v in vals)
    old=[]; j=i+1
    inline=lines[i].split(':',1)[1].strip()
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

def create_work(title,author,mov,pri,axes):
    sid=hashlib.sha1((title+'|'+author).encode()).hexdigest()[:10]
    p=WORKS/f'{title}.md'
    if p.exists(): p=WORKS/f'{title}（{author}）.md'
    body=f'''---\nid: WL-WORK-M51-{sid}\ntype: work\ntitle: "{title}"\naliases: []\nauthor: "{author}"\nyear: null\nread_status: 未读\naxis_t: []\naxis_r: []\naxis_m:\n- {AXIS}\naxis_g: []\naxis_q: []\naxis_source: manual_m51_structural_gap_fill_v1\ntopics:\n- {TOPIC_ID}\ntopic_links: []\nm51_priority: "{pri}"\nm51_movement_cluster: "{mov}"\nm51_axes:\n'''+''.join(f'- {a}\n' for a in axes)+'''verification_status: 手工核验\nbibliography_status: structural_anchor_metadata_pending\n---\n# '''+title+'''\n\n## M5.1 专题角色\n\n- 范式：'''+mov+'''\n- 优先级：'''+pri+'''\n- 机制：'''+ ' / '.join(axes)+'''\n'''
    p.write_text(body,encoding='utf-8')

def map_existing(p,text,mov,pri,axes):
    fm,body=fm_parts(text); fm=union_list(fm,'axis_m',[AXIS]); fm=union_list(fm,'topics',[TOPIC_ID]); fm=set_scalar(fm,'m51_priority',pri); fm=set_scalar(fm,'m51_movement_cluster',mov); fm=union_list(fm,'m51_axes',axes); p.write_text('---\n'+fm+'\n---\n'+body,encoding='utf-8')

def write_topic():
    TOPIC.mkdir(parents=True,exist_ok=True)
    (TOPIC/'00 战后思想与美学范式.md').write_text('''---\nid: WL-TOPIC-M5.1-POSTWAR-AESTHETICS\ntype: literature_topic_index\nname: 战后思想与美学范式\nstructure_status: m-axis-v2\ntemplate_version: literature-topic-m-axis-v2\n---\n# M5.1 战后思想与美学范式\n\n> 核心问题：二战以后，当主体、意义、现实与语言的稳定性受到怀疑时，文学如何重新组织现实、经验与叙事？\n\n## 五个板块\n\n[[11 主要范式/01 存在主义|存在主义]] · [[11 主要范式/02 荒诞|荒诞]] · [[11 主要范式/03 法国新小说|法国新小说]] · [[11 主要范式/04 魔幻现实主义|魔幻现实主义]] · [[11 主要范式/05 后现代主义|后现代主义]]\n\n## 认知主线\n\n战争与意义危机 → 存在主义 / 荒诞 → 再现危机 → 新小说 → 现实层级与文本权威不稳定 → 魔幻现实主义 / 后现代主义。\n\n## 边界\n\n- 不是所有战后文学。\n- Boom 是 M4 的文学网络；魔幻现实主义是 M5.1 的美学模式。\n- 后殖民、女性主义、酷儿、去殖民作为批评框架时归 M5.2。\n- 允许作品与 M3.1、M4、M5.2 合法多专题投影。\n''',encoding='utf-8')
    (TOPIC/'01 战后思想与美学范式.canvas').write_text('{"nodes":[],"edges":[]}',encoding='utf-8')
    (TOPIC/'02 战后思想与美学范式结构.base').write_text('filters:\n  and:\n    - file.folder.startsWith("个人通识知识系统_v2_A2/30 世界文学/30 专题/M5.1 战后思想与美学范式")\nviews:\n  - type: table\n    name: 结构\n',encoding='utf-8')
    (TOPIC/'03 战后思想与美学范式作品.base').write_text('filters:\n  and:\n    - file.folder == "个人通识知识系统_v2_A2/30 世界文学/40 作品"\n    - topics.contains("WL-TOPIC-M5.1-POSTWAR-AESTHETICS")\nviews:\n  - type: table\n    name: 作品\n    groupBy:\n      property: m51_movement_cluster\n',encoding='utf-8')
    (TOPIC/'04 战后思想与美学范式书目覆盖审计.md').write_text('# M5.1 战后思想与美学范式书目覆盖审计\n\n待独立审计冻结。\n',encoding='utf-8')
    core={'01 定义与边界':'M5.1 不是所有战后文学；以主体、意义、现实、语言与文本权威的危机为准入标准。','02 历史条件与问题意识':'二战、大屠杀、冷战、去殖民、消费社会与媒介扩张共同改变文学的问题意识。','03 范式谱系与内部结构':'存在主义、荒诞、新小说、魔幻现实主义、后现代主义不是线性替代，而是部分重叠的不同回应。','04 美学机制与叙事重组':'关注疏离、荒诞、去心理化、物的凝视、现实层级、元小说、拼贴、互文、系统小说等机制。','05 传播、地域与非同步性':'战后范式跨法国、拉美、英语世界、非洲、南亚与东亚传播，但不假设同步发展。','06 与M3.1、M4、M5.2的边界':'M3.1偏现代主义形式革命；M4偏集体运动与网络；M5.2偏权力与批评框架。','07 阅读路线':'先存在主义/荒诞理解意义危机，再读新小说的再现危机，最后比较魔幻现实主义与后现代主义。'}
    d=TOPIC/'10 核心结构'; d.mkdir(exist_ok=True)
    for n,c in core.items(): (d/(n+'.md')).write_text('# '+n[3:]+'\n\n'+c+'\n',encoding='utf-8')
    d=TOPIC/'11 主要范式'; d.mkdir(exist_ok=True); names=['存在主义','荒诞','法国新小说','魔幻现实主义','后现代主义']; (d/'00 主要范式索引.md').write_text('# 主要范式索引\n\n'+'\n'.join(f'- [[{i+1:02d} {n}|{n}]]' for i,n in enumerate(names))+'\n',encoding='utf-8')
    for i,n in enumerate(names): (d/f'{i+1:02d} {n}.md').write_text(f'# {n}\n\n> 作为 M5.1 内部分析板块，不升格为全局 M 子坐标。\n',encoding='utf-8')
    for sub,title,content in [('12 核心矛盾','核心矛盾索引','意义/荒诞；主体/他者；现实/再现；历史/记忆；文本/权威。'),('13 转型','转型关系索引','M3.1 → M5.1；Boom ↔ 魔幻现实主义；M5.1 ↔ M5.2。')]:
        q=TOPIC/sub; q.mkdir(exist_ok=True); (q/('00 '+title+'.md')).write_text('# '+title+'\n\n'+content+'\n',encoding='utf-8')

def main():
    write_topic(); idx=existing_index(); reused=created=0; collisions=[]
    for title,author,mov,pri,axes in BIB:
        cands=idx.get(norm(title),[]); match=None
        for p,a,t in cands:
            if norm(author)==norm(a) or norm(author) in norm(a) or norm(a) in norm(author): match=(p,t); break
        if match: map_existing(match[0],match[1],mov,pri,axes); reused+=1
        else:
            if cands: collisions.append((title,author,[a for _,a,_ in cands]))
            create_work(title,author,mov,pri,axes); created+=1
    print(f'target={len(BIB)} reused={reused} created={created}'); print(Counter(x[2] for x in BIB)); print('collisions=',collisions)
if __name__=='__main__': main()
