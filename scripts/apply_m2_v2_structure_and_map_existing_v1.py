from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = LIT / "40 作品"
TOPIC_DIR = LIT / "30 专题" / "M2 19世纪文学思潮"
TOPIC_ID = "WL-TOPIC-M2-19C-MOVEMENTS"
LINK = "[[../30 专题/M2 19世纪文学思潮/00 19世纪文学思潮|19世纪文学思潮]]"

# title, author, movement, priority, mechanisms
BIB = [
("抒情歌谣集","威廉·华兹华斯、塞缪尔·泰勒·柯勒律治","浪漫主义","★",["自然与主体","想象力与情感"]),
("序曲","威廉·华兹华斯","浪漫主义","★",["自然与主体","自我形成"]),
("古舟子咏","塞缪尔·泰勒·柯勒律治","浪漫主义","★",["超自然","想象力与情感"]),
("天真与经验之歌","威廉·布莱克","浪漫主义","★",["想象力与情感","反工业现代性"]),
("恰尔德·哈洛尔德游记","拜伦","浪漫主义","◆",["浪漫主义英雄","个体反叛"]),
("唐璜","拜伦","浪漫主义","★",["个体反叛","反讽"]),
("解放了的普罗米修斯","珀西·比希·雪莱","浪漫主义","◆",["革命想象","神话重写"]),
("弗兰肯斯坦","玛丽·雪莱","浪漫主义","★",["科学与现代性","哥特与浪漫主义"]),
("艾凡赫","沃尔特·司各特","浪漫主义","★",["历史想象","民族与历史"]),
("巴黎圣母院","维克多·雨果","浪漫主义","★",["历史想象","崇高与怪诞"]),
("九三年","维克多·雨果","浪漫主义","◆",["革命想象","历史想象"]),
("勒内","夏多布里昂","浪漫主义","◆",["忧郁主体","自然与主体"]),
("一个世纪儿的忏悔","缪塞","浪漫主义","◆",["忧郁主体","历史断裂"]),
("欧那尼","维克多·雨果","浪漫主义","★",["反古典规范","浪漫主义戏剧"]),
("浮士德","歌德","浪漫主义","★",["知识与欲望","现代主体"]),
("夜颂","诺瓦利斯","浪漫主义","◆",["夜与超越","想象力与情感"]),
("沙人","E. T. A. 霍夫曼","浪漫主义","★",["超自然","不稳定主体"]),
("叶甫盖尼·奥涅金","普希金","浪漫主义","★",["浪漫主义英雄","向现实主义过渡"]),
("当代英雄","莱蒙托夫","浪漫主义","★",["浪漫主义英雄","向现实主义过渡"]),
("塔杜施先生","亚当·密茨凯维奇","浪漫主义","◆",["民族与历史","流亡与记忆"]),
("自然","拉尔夫·沃尔多·爱默生","超验主义","★",["自然与主体","精神自主"]),
("论自助","拉尔夫·沃尔多·爱默生","超验主义","★",["精神自主","个人主义"]),
("瓦尔登湖","亨利·戴维·梭罗","超验主义","★",["自然与主体","反工业现代性"]),
("论公民的不服从","亨利·戴维·梭罗","超验主义","★",["个人良知","政治抵抗"]),
("草叶集","沃尔特·惠特曼","超验主义","★",["民主主体","身体与自然"]),
("白鲸","赫尔曼·梅尔维尔","超验主义","★",["自然与主体","认识论危机"]),
("红字","纳撒尼尔·霍桑","超验主义","◆",["个人良知","宗教与社会"]),
("高老头","巴尔扎克","现实主义","★",["社会总体","阶级与金钱"]),
("幻灭","巴尔扎克","现实主义","★",["社会总体","资本与媒介"]),
("红与黑","司汤达","现实主义","★",["个人与社会","阶级流动"]),
("包法利夫人","福楼拜","现实主义","★",["日常生活","欲望与商品社会"]),
("情感教育","福楼拜","现实主义","★",["历史幻灭","日常生活"]),
("名利场","萨克雷","现实主义","★",["社会全景","讽刺"]),
("荒凉山庄","查尔斯·狄更斯","现实主义","★",["制度与城市","社会全景"]),
("远大前程","查尔斯·狄更斯","现实主义","★",["阶级流动","成长与社会"]),
("米德尔马契","乔治·艾略特","现实主义","★",["社会网络","伦理与日常"]),
("死魂灵","果戈理","现实主义","★",["官僚与社会","讽刺"]),
("父与子","屠格涅夫","现实主义","★",["代际冲突","思想与社会"]),
("奥勃洛莫夫","冈察洛夫","现实主义","◆",["社会类型","现代化迟滞"]),
("战争与和平","列夫·托尔斯泰","现实主义","★",["历史与个人","社会总体"]),
("安娜·卡列尼娜","列夫·托尔斯泰","现实主义","★",["家庭与社会","伦理与欲望"]),
("罪与罚","陀思妥耶夫斯基","现实主义","★",["都市贫困","心理现实主义"]),
("卡拉马佐夫兄弟","陀思妥耶夫斯基","现实主义","★",["伦理与信仰","心理现实主义"]),
("哈克贝利·费恩历险记","马克·吐温","现实主义","★",["方言与现实","种族与社会"]),
("一位女士的画像","亨利·詹姆斯","现实主义","★",["心理现实主义","跨大西洋社会"]),
("福尔图娜塔和哈辛塔","贝尼托·佩雷斯·加尔多斯","现实主义","◆",["城市社会","阶级与性别"]),
("马亚一家","埃萨·德·克罗兹","现实主义","◆",["家庭与社会","现代化批判"]),
("浮云","二叶亭四迷","现实主义","★",["语言改革","现代主体"]),
("萌芽","埃米尔·左拉","自然主义","★",["阶级与工业","环境决定"]),
("小酒店","埃米尔·左拉","自然主义","★",["环境决定","都市贫困"]),
("娜娜","埃米尔·左拉","自然主义","★",["身体与商品社会","环境决定"]),
("泰蕾丝·拉甘","埃米尔·左拉","自然主义","◆",["生理决定","实验小说"]),
("杰米妮·拉瑟都","龚古尔兄弟","自然主义","◆",["实验小说","社会病理"]),
("苔丝","托马斯·哈代","自然主义","★",["环境与命运","性别与社会"]),
("无名的裘德","托马斯·哈代","自然主义","★",["制度与个体","环境与命运"]),
("麦琪姑娘","斯蒂芬·克莱恩","自然主义","★",["都市贫困","环境决定"]),
("麦克梯格","弗兰克·诺里斯","自然主义","◆",["生理决定","资本与欲望"]),
("章鱼","弗兰克·诺里斯","自然主义","◆",["资本与环境","社会力量"]),
("嘉莉妹妹","西奥多·德莱塞","自然主义","★",["都市欲望","环境决定"]),
("织工","盖哈特·霍普特曼","自然主义","★",["阶级与工业","自然主义戏剧"]),
("朱莉小姐","奥古斯特·斯特林堡","自然主义","★",["性别与阶级","自然主义戏剧"]),
("恶之花","夏尔·波德莱尔","象征主义","★",["都市现代性","感官与象征"]),
("无言浪漫曲","保罗·魏尔伦","象征主义","★",["音乐性","暗示"]),
("彩画集","阿蒂尔·兰波","象征主义","★",["感官重组","语言实验"]),
("骰子一掷永远取消不了偶然","斯特凡·马拉美","象征主义","★",["语言实验","页面与形式"]),
("佩利亚斯与梅丽桑德","莫里斯·梅特林克","象征主义","★",["象征主义戏剧","暗示"]),
("阿克塞尔","维利耶·德·利尔-阿当","象征主义","◆",["象征主义戏剧","反现实主义"]),
("道林·格雷的画像","奥斯卡·王尔德","唯美主义","★",["艺术自主","审美与伦理"]),
("文艺复兴史研究","沃尔特·佩特","唯美主义","★",["艺术自主","感受主义"]),
("诗与歌谣","阿尔杰农·查尔斯·斯温伯恩","唯美主义","◆",["艺术自主","感官与形式"]),
("意图集","奥斯卡·王尔德","唯美主义","◆",["艺术自主","批评与悖论"]),
("逆流","若利斯-卡尔·于斯曼","颓废主义","★",["人工性","反自然与审美封闭"]),
("莎乐美","奥斯卡·王尔德","颓废主义","★",["欲望与死亡","人工性"]),
("维纳斯先生","拉希尔德","颓废主义","◆",["性别越界","人工性"]),
("恶魔们","巴贝·多尔维伊","颓废主义","◆",["罪与审美","反资产阶级道德"]),
("逸乐","加布里埃莱·邓南遮","颓废主义","★",["审美生活","欲望与人工性"]),
("蓝","鲁文·达里奥","拉美 Modernismo","★",["语言革新","跨大西洋现代性"]),
("世俗的圣歌及其他诗篇","鲁文·达里奥","拉美 Modernismo","★",["音乐性","艺术自主"]),
("生命与希望之歌","鲁文·达里奥","拉美 Modernismo","★",["拉美身份","现代性批判"]),
("伊斯梅利略","何塞·马蒂","拉美 Modernismo","◆",["语言革新","拉美身份"]),
("朴素的诗","何塞·马蒂","拉美 Modernismo","★",["拉美身份","抒情革新"]),
("雪","胡利安·德尔·卡萨尔","拉美 Modernismo","◆",["颓废审美","都市现代性"]),
("黑珍珠","阿马多·内尔沃","拉美 Modernismo","◆",["象征与音乐性","精神性"]),
("金山","莱奥波尔多·卢贡内斯","拉美 Modernismo","◆",["语言革新","向先锋过渡"]),
("阿里埃尔","何塞·恩里克·罗多","拉美 Modernismo","★",["拉美身份","现代性批判"]),
]


def fm_bounds(text):
    if not text.startswith("---\n"): return None
    i=text.find("\n---",4)
    return (4,i) if i!=-1 else None

def set_scalar(fm,key,value):
    pat=rf"(?m)^{re.escape(key)}:\s*.*$"; line=f"{key}: {value}"
    return re.sub(pat,line,fm) if re.search(pat,fm) else fm.rstrip()+"\n"+line+"\n"
def list_value(fm,key):
    lines=fm.splitlines(); vals=[]
    for i,line in enumerate(lines):
        if line.startswith(key+":"):
            for nxt in lines[i+1:]:
                if re.match(r"^[A-Za-z0-9_]+:",nxt): break
                m=re.match(r"^\s*-\s+(.*)$",nxt)
                if m: vals.append(m.group(1).strip().strip("'\""))
            break
    return vals
def set_list(fm,key,vals):
    lines=fm.splitlines(); out=[]; i=0; replaced=False
    while i<len(lines):
        if lines[i].startswith(key+":"):
            out.append(key+":"); out.extend("- "+str(v) for v in vals); replaced=True; i+=1
            while i<len(lines) and not re.match(r"^[A-Za-z0-9_]+:",lines[i]): i+=1
        else: out.append(lines[i]); i+=1
    if not replaced: out.extend([key+":"]+["- "+str(v) for v in vals])
    return "\n".join(out)+"\n"
def patch_work(path,movement,priority,axes):
    text=path.read_text(encoding="utf-8"); b=fm_bounds(text)
    if not b: return False
    a,z=b; fm=text[a:z]
    topics=list_value(fm,"topics");
    if TOPIC_ID not in topics: topics.append(TOPIC_ID)
    fm=set_list(fm,"topics",topics)
    links=list_value(fm,"topic_links");
    if LINK not in links: links.append("'"+LINK+"'")
    fm=set_list(fm,"topic_links",links)
    axis_m=list_value(fm,"axis_m"); label=f"M2 19世纪文学思潮 / {movement}"
    if label not in axis_m: axis_m.append(label)
    fm=set_list(fm,"axis_m",axis_m)
    fm=set_scalar(fm,"m2_priority",priority)
    fm=set_scalar(fm,"m2_movement_cluster",movement)
    fm=set_list(fm,"m2_axes",axes)
    path.write_text("---\n"+fm.rstrip()+"\n---"+text[z+4:],encoding="utf-8")
    return True

# Core package
TOPIC_DIR.mkdir(parents=True,exist_ok=True)
for sub in ["10 核心结构","11 主要思潮","12 核心矛盾","13 转型","_source"]: (TOPIC_DIR/sub).mkdir(exist_ok=True)

home='''---\nid: WL-TOPIC-M2-19C-MOVEMENTS\ntype: literature_topic\naxis: M\nnode: M2\nstatus: m-axis-v2\n---\n# M2 19世纪文学思潮\n\n> 核心问题：法国革命、工业化、资本主义、民族国家、城市社会与现代科学改变世界之后，文学如何重新理解个人、自然、社会与现实？\n\n## 认知主线\n启蒙/革命遗产 → 浪漫主义的主体与自然 → 现实主义的社会再现 → 自然主义的决定论实验；另一支由浪漫主义与世纪末危机走向象征主义、唯美主义、颓废主义，并在拉美形成自身的 Modernismo，最终向现代主义与先锋派过渡。\n\n## 三层地图\n- [[10 核心结构/03 19世纪思潮谱系|历史与思想谱系]]\n- [[11 主要思潮/00 主要思潮索引|八个主要思潮]]\n- [[12 核心矛盾/00 核心矛盾索引|跨思潮核心矛盾]]\n- [[13 转型/00 转型关系索引|思潮之间的转型关系]]\n\n## 数据入口\n- [[02 19世纪文学思潮结构.base|结构 Base]]\n- [[03 19世纪文学思潮作品.base|作品 Base]]\n\n## 边界\nM2 不是“所有19世纪文学”。作品只有在理解某一思潮、思潮间转换或现代性回应时具有结构意义，才进入本专题。象征主义、唯美主义、颓废主义作为 M3.1 的重要前史仍归 M2；西语美洲 Modernismo 不等于英语语境 Modernism。\n'''
(TOPIC_DIR/"00 19世纪文学思潮.md").write_text(home,encoding="utf-8")
canvas='''{"nodes":[{"id":"context","type":"text","text":"革命 · 工业化 · 城市化 · 资本主义 · 民族国家 · 科学","x":0,"y":0,"width":360,"height":120},{"id":"question","type":"text","text":"文学如何重新理解个人、自然、社会与现实？","x":0,"y":180,"width":360,"height":100},{"id":"rom","type":"text","text":"浪漫主义 / 超验主义\\n主体 · 自然 · 想象力","x":-420,"y":360,"width":300,"height":120},{"id":"real","type":"text","text":"现实主义 → 自然主义\\n社会再现 · 制度 · 决定论","x":0,"y":360,"width":300,"height":120},{"id":"fin","type":"text","text":"象征主义 / 唯美主义 / 颓废主义\\n语言 · 感知 · 艺术自主","x":420,"y":360,"width":320,"height":120},{"id":"latam","type":"text","text":"拉美 Modernismo\\n语言革新 · 跨大西洋现代性","x":420,"y":560,"width":320,"height":110},{"id":"m31","type":"text","text":"→ M3.1 现代主义 / M3.2 先锋派","x":0,"y":720,"width":360,"height":100}],"edges":[{"id":"e1","fromNode":"context","toNode":"question"},{"id":"e2","fromNode":"question","toNode":"rom"},{"id":"e3","fromNode":"question","toNode":"real"},{"id":"e4","fromNode":"question","toNode":"fin"},{"id":"e5","fromNode":"fin","toNode":"latam"},{"id":"e6","fromNode":"rom","toNode":"m31"},{"id":"e7","fromNode":"real","toNode":"m31"},{"id":"e8","fromNode":"latam","toNode":"m31"}]}'''
(TOPIC_DIR/"01 19世纪文学思潮.canvas").write_text(canvas,encoding="utf-8")
base='''filters:\n  and:\n    - type == "work"\n    - topics.contains("WL-TOPIC-M2-19C-MOVEMENTS")\nproperties:\n  file.name:\n    displayName: 作品\n  note.author:\n    displayName: 作者\n  note.read_status:\n    displayName: 阅读状态\n  note.m2_priority:\n    displayName: 优先级\n  note.m2_movement_cluster:\n    displayName: 思潮\n  note.m2_axes:\n    displayName: 机制\nviews:\n  - type: table\n    name: 全部作品\n    order: [file.name, author, read_status, m2_priority, m2_movement_cluster, m2_axes]\n  - type: table\n    name: 核心骨架 ★\n    filters:\n      and:\n        - m2_priority == "★"\n    order: [file.name, author, m2_movement_cluster, m2_axes]\n  - type: table\n    name: 按思潮\n    groupBy:\n      property: m2_movement_cluster\n      direction: ASC\n    order: [file.name, author, m2_priority, m2_axes]\n'''
(TOPIC_DIR/"03 19世纪文学思潮作品.base").write_text(base,encoding="utf-8")
structure='''filters:\n  and:\n    - file.inFolder("个人通识知识系统_v2_A2/30 世界文学/30 专题/M2 19世纪文学思潮")\n    - file.ext == "md"\nviews:\n  - type: table\n    name: 专题结构\n    order: [file.name]\n'''
(TOPIC_DIR/"02 19世纪文学思潮结构.base").write_text(structure,encoding="utf-8")

core={
"01 定义与边界.md":"# 定义与边界\n\nM2 研究的是19世纪文学思潮对现代社会条件的系统回应，而非以公元年份圈定的全部文学。思潮之间允许重叠、竞争与过渡。\n",
"02 革命、工业化与现代社会.md":"# 革命、工业化与现代社会\n\n关键压力包括法国革命及其政治遗产、工业化与资本关系、都市化、民族国家、帝国扩张、现代科学与大众出版。它们改变文学的读者、对象、媒介与现实观。\n",
"03 19世纪思潮谱系.md":"# 19世纪思潮谱系\n\n启蒙/革命遗产 → 浪漫主义；浪漫主义内部的主体与自然问题在美国形成超验主义。工业资本主义与城市社会推动现实主义，科学主义与决定论将其激进化为自然主义。另一条路线由浪漫主义和世纪末危机进入象征主义、唯美主义、颓废主义，并向现代主义过渡。\n",
"04 美学回应与文学机制.md":"# 美学回应与文学机制\n\n本专题不把“主义”当标签，而把它们理解为不同现实观：浪漫主义强调想象与主体，现实主义强调社会关系与可观察现实，自然主义强调环境/遗传/社会力量，象征主义转向暗示与语言，唯美主义强调艺术自主，颓废主义将人工性和危机体验推到极端。\n",
"05 跨地域传播与变体.md":"# 跨地域传播与变体\n\n思潮通过翻译、期刊、教育、旅行、帝国与跨大西洋网络传播，但不同地区不是简单复制中心范式。美国超验主义与西语美洲 Modernismo 都必须作为主动改写而不是外围模仿理解。\n",
"06 与M1、M3.1的边界.md":"# 与 M1、M3.1 的边界\n\nM1 提供启蒙、感伤主义等前提；M2 处理19世纪思潮的分化与竞争；M3.1 处理约1890—1945现代主义对再现、主体、语言和形式的进一步重构。象征/唯美/颓废是桥梁，但主归 M2。\n",
"07 阅读路线.md":"# 阅读路线\n\n第一轮读 ★，要求至少跨越浪漫主义、现实主义、自然主义、世纪末审美与拉美 Modernismo；第二轮用 ◆ 补足地域与边界案例。阅读顺序优先按问题链而非年代机械推进。\n"}
for name,text in core.items(): (TOPIC_DIR/"10 核心结构"/name).write_text(text,encoding="utf-8")
movements=["浪漫主义","超验主义","现实主义","自然主义","象征主义","唯美主义","颓废主义","拉美 Modernismo"]
(TOPIC_DIR/"11 主要思潮"/"00 主要思潮索引.md").write_text("# 主要思潮索引\n\n"+"\n".join(f"- [[{i+1:02d} {m}|{m}]]" for i,m in enumerate(movements))+"\n",encoding="utf-8")
for i,m in enumerate(movements,1):
    (TOPIC_DIR/"11 主要思潮"/f"{i:02d} {m}.md").write_text(f"# {m}\n\n## 它回应什么问题\n\n## 核心文学观\n\n## 主要形式与机制\n\n## 地域变体\n\n## 与相邻思潮的关系\n\n## 代表作品\n",encoding="utf-8")
contrasts=["理性 vs 情感","个体 vs 社会","自然 vs 工业文明","理想 vs 现实","艺术自主 vs 社会功能","再现现实 vs 重构感知"]
(TOPIC_DIR/"12 核心矛盾"/"00 核心矛盾索引.md").write_text("# 核心矛盾索引\n\n"+"\n".join(f"- {x}" for x in contrasts)+"\n",encoding="utf-8")
trans=["浪漫主义 → 现实主义","现实主义 → 自然主义","浪漫主义 → 象征主义","象征主义／唯美主义／颓废主义 → 现代主义"]
(TOPIC_DIR/"13 转型"/"00 转型关系索引.md").write_text("# 转型关系索引\n\n"+"\n".join(f"- {x}" for x in trans)+"\n",encoding="utf-8")

matched=[]; missing=[]; counts=Counter()
for title,author,movement,priority,axes in BIB:
    path=WORKS/(title+".md")
    if path.exists():
        if patch_work(path,movement,priority,axes):
            matched.append(title); counts[movement]+=1
    else: missing.append((title,author,movement,priority,axes))

source=["# M2 书目映射候选 v1","",f"目标节点：{len(BIB)}",f"已匹配中央作品：{len(matched)}",f"缺失：{len(missing)}","","## 已匹配"]+[f"- {x}" for x in matched]+["","## 缺失（本阶段不自动新建）"]+[f"- {t}｜{a}｜{m}｜{p}" for t,a,m,p,_ in missing]
(TOPIC_DIR/"_source"/"M2书目映射候选_v1.md").write_text("\n".join(source)+"\n",encoding="utf-8")
print(f"target={len(BIB)} matched={len(matched)} missing={len(missing)}")
for m in movements: print(f"{m}: {counts[m]}")
print("MISSING:")
for t,a,m,p,_ in missing: print(f"{t}|{a}|{m}|{p}")
