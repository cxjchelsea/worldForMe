from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = LIT / "40 作品"
TOPIC_DIR = LIT / "30 专题" / "M3.2 先锋派"
TOPIC_ID = "WL-TOPIC-M3.2-AVANT-GARDE"

# title, author, movement, priority, mechanisms
SPECS = [
# Italian Futurism
("未来主义宣言","菲利波·托马索·马里内蒂","意大利未来主义","★",["宣言政治","速度与机器","反传统"]),
("未来主义文学技术宣言","菲利波·托马索·马里内蒂","意大利未来主义","★",["语言破坏","自由词语","排版实验"]),
("Zang Tumb Tuuum","菲利波·托马索·马里内蒂","意大利未来主义","★",["声音诗","排版实验","战争机器"]),
("未来主义者马法尔卡","菲利波·托马索·马里内蒂","意大利未来主义","◆",["未来人神话","反传统"]),
("想象力无线电与自由词语","菲利波·托马索·马里内蒂","意大利未来主义","◆",["媒介实验","自由词语"]),
("未来主义戏剧综合","马里内蒂、塞蒂梅利、科拉","意大利未来主义","◆",["戏剧革命","速度与压缩"]),
# Russian Futurism
("给公众趣味一记耳光","大卫·布尔柳克等","俄国未来主义","★",["宣言政治","反经典","诗人集体"]),
("裤中云","弗拉基米尔·马雅可夫斯基","俄国未来主义","★",["都市革命","夸张主体","语言实验"]),
("脊椎笛","弗拉基米尔·马雅可夫斯基","俄国未来主义","◆",["夸张主体","声音节奏"]),
("一亿五千万","弗拉基米尔·马雅可夫斯基","俄国未来主义","◆",["革命神话","大众政治"]),
("赞格齐","维利米尔·赫列勃尼科夫","俄国未来主义","★",["超理性语言","语言乌托邦"]),
("笑的咒语","维利米尔·赫列勃尼科夫","俄国未来主义","◆",["造词","声音诗"]),
("太阳的胜利","阿列克谢·克鲁乔内赫等","俄国未来主义","★",["跨媒介","超理性语言","反叙事"]),
("倒着的世界","阿列克谢·克鲁乔内赫、维利米尔·赫列勃尼科夫","俄国未来主义","◆",["超理性语言","书籍实验"]),
("词本身宣言","阿列克谢·克鲁乔内赫、维利米尔·赫列勃尼科夫","俄国未来主义","★",["宣言政治","语言自治","超理性语言"]),
# Expressionism
("人类的黄昏","库尔特·平图斯 编","德语表现主义","★",["表现主义诗歌","战争危机","都市焦虑"]),
("乞丐","莱因哈德·佐尔格","德语表现主义","★",["表现主义戏剧","代际冲突","精神救赎"]),
("儿子","瓦尔特·哈森克莱弗","德语表现主义","★",["表现主义戏剧","代际冲突"]),
("从早晨到午夜","格奥尔格·凯泽","德语表现主义","★",["表现主义戏剧","资本主义异化"]),
("煤气","格奥尔格·凯泽","德语表现主义","◆",["工业异化","群众社会"]),
("转变","恩斯特·托勒","德语表现主义","◆",["战争创伤","革命救赎"]),
("群众与人","恩斯特·托勒","德语表现主义","★",["革命伦理","群众政治"]),
("杀人者，女人们的希望","奥斯卡·柯克西卡","德语表现主义","★",["表现主义戏剧","性别暴力","原始冲动"]),
("加莱市民","格奥尔格·凯泽","德语表现主义","◆",["群体伦理","表现主义戏剧"]),
# Dada
("达达宣言 1918","特里斯坦·查拉","达达主义","★",["反艺术","宣言政治","偶然性"]),
("达达七篇宣言与杂灯","特里斯坦·查拉","达达主义","★",["反艺术","文本表演","偶然性"]),
("安提皮林先生的第一次天国冒险","特里斯坦·查拉","达达主义","◆",["文本表演","荒诞"]),
("卡拉瓦内","胡戈·巴尔","达达主义","★",["声音诗","语言归零","表演"]),
("达达年鉴","理查德·胡森贝克 编","达达主义","★",["运动网络","宣言政治","国际主义"]),
("前进，达达","理查德·胡森贝克","达达主义","◆",["反艺术","政治达达"]),
("最后的松弛","瓦尔特·塞尔纳","达达主义","◆",["虚无主义","反道德"]),
("致安娜·布鲁姆","库尔特·施维特斯","达达主义","★",["拼贴逻辑","荒诞","广告语言"]),
# Surrealism
("超现实主义宣言","安德烈·布勒东","超现实主义","★",["宣言政治","自动写作","梦与无意识"]),
("超现实主义第二宣言","安德烈·布勒东","超现实主义","◆",["运动纪律","政治介入"]),
("磁场","安德烈·布勒东、菲利普·苏波","超现实主义","★",["自动写作","共同创作"]),
("娜嘉","安德烈·布勒东","超现实主义","★",["都市漫游","偶然相遇","现实惊奇"]),
("疯爱","安德烈·布勒东","超现实主义","★",["欲望政治","客观偶然"]),
("可溶的鱼","安德烈·布勒东","超现实主义","◆",["自动写作","梦逻辑"]),
("巴黎的农民","路易·阿拉贡","超现实主义","★",["都市漫游","现代神话"]),
("自由或爱情","罗贝尔·德斯诺斯","超现实主义","★",["梦逻辑","欲望释放"]),
("无玷的受孕","安德烈·布勒东、保罗·艾吕雅","超现实主义","◆",["模拟精神状态","共同创作"]),
("痛苦之都","保罗·艾吕雅","超现实主义","★",["超现实主义诗歌","爱情与梦"]),
("交流的器皿","安德烈·布勒东","超现实主义","◆",["梦与现实","理论写作"]),
("百头女","马克斯·恩斯特","超现实主义","◆",["拼贴小说","跨媒介"]),
("返乡笔记","艾梅·塞泽尔","超现实主义","★",["殖民批判","黑人主体","超现实语言"]),
# Imagism / Vorticism
("意象派诗选","埃兹拉·庞德 编","意象主义与漩涡主义","★",["意象原则","诗歌压缩","跨国网络"]),
("意象派诗人集 1915","艾米·洛厄尔 编","意象主义与漩涡主义","★",["意象原则","运动网络"]),
("意象派诗人集 1916","艾米·洛厄尔 编","意象主义与漩涡主义","◆",["意象原则","运动网络"]),
("反击","埃兹拉·庞德","意象主义与漩涡主义","★",["诗歌压缩","现代都市"]),
("海园","H.D.","意象主义与漩涡主义","★",["意象原则","古典重写"]),
("BLAST 第1号","温德姆·刘易斯 编","意象主义与漩涡主义","★",["宣言政治","杂志媒介","跨艺术"]),
("塔尔","温德姆·刘易斯","意象主义与漩涡主义","◆",["漩涡主义小说","机械现代性"]),
# Constructivism / LEF / factography
("怎样做诗","弗拉基米尔·马雅可夫斯基","构成主义、LEF与事实文学","★",["生产主义","写作技术","大众传播"]),
("关于这个","弗拉基米尔·马雅可夫斯基","构成主义、LEF与事实文学","◆",["构成主义书籍","跨媒介"]),
("臭虫","弗拉基米尔·马雅可夫斯基","构成主义、LEF与事实文学","★",["讽刺剧场","革命日常"]),
("澡堂","弗拉基米尔·马雅可夫斯基","构成主义、LEF与事实文学","★",["讽刺剧场","官僚批判"]),
("事实文学","尼古拉·丘扎克等","构成主义、LEF与事实文学","★",["事实写作","反虚构","生产主义"]),
# Ibero-American avant-gardes
("非仆从","维森特·维多夫罗","伊比利亚与拉美先锋派","★",["创造主义","诗人造物","宣言政治"]),
("水镜","维森特·维多夫罗","伊比利亚与拉美先锋派","◆",["创造主义","意象实验"]),
("阿尔塔索尔","维森特·维多夫罗","伊比利亚与拉美先锋派","★",["语言解体","创造主义"]),
("特里尔塞","塞萨尔·巴列霍","伊比利亚与拉美先锋派","★",["语言实验","语法破坏","主体危机"]),
("二十首在电车上读的诗","奥利韦里奥·希龙多","伊比利亚与拉美先锋派","★",["都市感知","视觉诗学"]),
("贴花","奥利韦里奥·希龙多","伊比利亚与拉美先锋派","◆",["旅行现代性","视觉诗学"]),
("螺旋桨","吉列尔莫·德·托雷","伊比利亚与拉美先锋派","★",["极端主义","排版实验"]),
("内在脚手架","曼努埃尔·马普莱斯·阿尔塞","伊比利亚与拉美先锋派","★",["激进主义","都市机器"]),
("城市","曼努埃尔·马普莱斯·阿尔塞","伊比利亚与拉美先锋派","★",["激进主义","都市机器","革命现代性"]),
("巴西木诗集","奥斯瓦尔德·德·安德拉德","伊比利亚与拉美先锋派","★",["巴西现代主义","殖民语言重写"]),
("食人主义宣言","奥斯瓦尔德·德·安德拉德","伊比利亚与拉美先锋派","★",["文化食人","反殖民现代性","宣言政治"]),
]

MOVEMENTS = ["意大利未来主义","俄国未来主义","德语表现主义","达达主义","超现实主义","意象主义与漩涡主义","构成主义、LEF与事实文学","伊比利亚与拉美先锋派"]


def fm_match(text: str):
    return re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)

def norm(s: str) -> str:
    return re.sub(r"[\s·・:：,，.。!！?？'\"“”‘’《》<>（）()\-—_]+", "", s).lower()

def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    return m.group(1).strip().strip("'\"") if m else ""

def list_value(fm: str, key: str) -> list[str]:
    lines=fm.splitlines(); out=[]
    for i,line in enumerate(lines):
        if line.startswith(key+":"):
            inline=line.split(":",1)[1].strip()
            if inline.startswith("[") and inline.endswith("]"):
                return [x.strip().strip("'\"") for x in inline[1:-1].split(",") if x.strip()]
            for nxt in lines[i+1:]:
                if re.match(r"^[A-Za-z0-9_]+:",nxt): break
                m=re.match(r"^\s*-\s+(.*)$",nxt)
                if m: out.append(m.group(1).strip().strip("'\""))
            break
    return out

def remove_field(fm: str, key: str) -> str:
    fm=re.sub(rf"(?ms)^{re.escape(key)}:\s*\n(?:\s*-.*\n?)*", "", fm)
    fm=re.sub(rf"(?m)^{re.escape(key)}:\s*.*\n?", "", fm)
    return fm.rstrip()

def set_scalar(fm,key,value): return remove_field(fm,key)+f"\n{key}: {value}"
def set_list(fm,key,values):
    fm=remove_field(fm,key)
    return fm+"\n"+key+":\n"+"\n".join(f"- {v}" for v in values) if values else fm+f"\n{key}: []"

def update_existing(path: Path, spec):
    title,author,movement,priority,axes=spec
    text=path.read_text(encoding="utf-8-sig"); m=fm_match(text)
    if not m: raise RuntimeError(f"frontmatter missing: {path}")
    fm=m.group(1)
    topics=list_value(fm,"topics"); axis_m=list_value(fm,"axis_m")
    if TOPIC_ID not in topics: topics.append(TOPIC_ID)
    if "M3.2 先锋派" not in axis_m: axis_m.append("M3.2 先锋派")
    fm=set_list(fm,"topics",topics)
    fm=set_list(fm,"axis_m",axis_m)
    fm=set_scalar(fm,"m32_priority",priority)
    fm=set_scalar(fm,"m32_movement_cluster",movement)
    fm=set_list(fm,"m32_axes",axes)
    new=text[:m.start(1)]+fm+text[m.end(1):]
    path.write_text(new,encoding="utf-8")

def new_work(spec):
    title,author,movement,priority,axes=spec
    wid="WL-WORK-M32-"+re.sub(r"[^A-Za-z0-9]+","-",title.encode("unicode_escape").decode()).strip("-")[:72]
    axes_block="\n".join(f"- {x}" for x in axes)
    return f'''---\nid: {wid}\ntype: work\ntitle: {title}\naliases: []\nauthor: {author}\nyear: null\nread_status: 未读\naxis_t: []\naxis_r: []\naxis_m:\n- M3.2 先锋派\naxis_g: []\naxis_q: []\naxis_source: manual_m32_structural_gap_fill_v1\ntopics:\n- {TOPIC_ID}\ntopic_links: []\nm32_priority: {priority}\nm32_movement_cluster: {movement}\nm32_axes:\n{axes_block}\nverification_status: 手工核验\nbibliography_status: structural_anchor_metadata_pending\n---\n# {title}\n\n## M3.2 专题角色\n\n- 先锋派运动：{movement}\n- 专题优先级：{priority}\n- 机制：{' / '.join(axes)}\n\n> M3.2 Structural Gap Fill V1：用于补齐先锋派运动与机制槽位；年份、原文题名等通用书目字段留待中央作品库统一校验。\n'''

def build_topic_files(counts, reused, created):
    TOPIC_DIR.mkdir(parents=True,exist_ok=True)
    home='''---\nid: WL-TOPIC-M3.2-AVANT-GARDE\ntype: literature_topic\naxis: M\nnode: M3.2\nstatus: m-axis-v2\n---\n# M3.2 先锋派\n\n> 核心问题：当“形式创新”仍不足以回应现代性危机时，文学为什么开始以宣言、集体行动、媒介破坏和政治介入去攻击“艺术制度”本身？\n\n## 专题定位\nM3.2 研究20世纪前半叶的历史先锋派。它与 M3.1 现代主义高度重叠，但观察单位不同：M3.1 更关注作品如何重造时间、意识、叙事与语言；M3.2 更关注运动如何通过宣言、团体、杂志、表演、拼贴、声音、排版与政治行动，把文学变成一种集体实验。\n\n## 认知主线\n世纪末形式危机 → 未来主义的速度/机器与断裂 → 表现主义的危机呼喊 → 达达的反艺术 → 超现实主义的梦、欲望与革命；同时意象主义/漩涡主义、俄国构成主义与 LEF、伊比利亚—拉美先锋派形成不同的跨媒介与反制度路径。\n\n## 四层地图\n- [[10 核心结构/03 先锋派谱系|历史与运动谱系]]\n- [[11 主要运动/00 主要运动索引|八个主要运动群]]\n- [[12 先锋机制/00 先锋机制索引|跨运动机制]]\n- [[13 边界与转型/00 边界与转型索引|与 M2、M3.1、战后实验的关系]]\n\n## 数据入口\n- [[02 先锋派结构.base|结构 Base]]\n- [[03 先锋派作品.base|作品 Base]]\n\n## 边界\nM3.2 ≠ 所有形式激进的现代主义作品，也 ≠ 20世纪所有实验文学。作品进入本专题，应能解释某个先锋运动、宣言/团体机制、反艺术制度、跨媒介实验或艺术—生活/政治合流。\n'''
    (TOPIC_DIR/"00 先锋派.md").write_text(home,encoding="utf-8")
    canvas={"nodes":[
      {"id":"c","type":"text","text":"M3.2 先锋派\n攻击艺术制度本身","x":0,"y":0,"width":300,"height":120},
      {"id":"m","type":"text","text":"运动/宣言\n集体与杂志","x":-420,"y":220,"width":260,"height":100},
      {"id":"mec","type":"text","text":"媒介破坏\n声音·排版·拼贴·表演","x":0,"y":220,"width":300,"height":100},
      {"id":"p","type":"text","text":"艺术—生活—政治\n重新连接","x":420,"y":220,"width":280,"height":100},
      {"id":"b","type":"text","text":"M3.1 现代主义\n形式/感知革命","x":-250,"y":430,"width":260,"height":100},
      {"id":"a","type":"text","text":"历史先锋派\n制度/行动革命","x":250,"y":430,"width":260,"height":100}],
      "edges":[{"id":"e1","fromNode":"c","toNode":"m"},{"id":"e2","fromNode":"c","toNode":"mec"},{"id":"e3","fromNode":"c","toNode":"p"},{"id":"e4","fromNode":"mec","toNode":"b"},{"id":"e5","fromNode":"mec","toNode":"a"}]}
    (TOPIC_DIR/"01 先锋派.canvas").write_text(json.dumps(canvas,ensure_ascii=False,indent=2),encoding="utf-8")
    base='''filters:\n  and:\n    - file.path.startsWith("个人通识知识系统_v2_A2/30 世界文学/30 专题/M3.2 先锋派/")\nviews:\n  - type: table\n    name: M3.2 结构\n    order:\n      - file.name\n'''
    (TOPIC_DIR/"02 先锋派结构.base").write_text(base,encoding="utf-8")
    works='''filters:\n  and:\n    - file.path.startsWith("个人通识知识系统_v2_A2/30 世界文学/40 作品/")\n    - topics.contains("WL-TOPIC-M3.2-AVANT-GARDE")\nviews:\n  - type: table\n    name: M3.2 作品\n    order:\n      - m32_priority\n      - m32_movement_cluster\n      - author\n      - year\n      - file.name\n'''
    (TOPIC_DIR/"03 先锋派作品.base").write_text(works,encoding="utf-8")
    core=TOPIC_DIR/"10 核心结构"; core.mkdir(exist_ok=True)
    docs={
      "01 定义与边界.md":"# 定义与边界\n\n先锋派不是“创新程度更高的现代主义”这么简单。历史先锋派通常具有集体自我命名、宣言、杂志/团体、公开挑衅、跨媒介行动，以及改变艺术与社会关系的企图。\n\nM3.1 的核心对象偏向作品与美学机制；M3.2 的核心对象偏向运动、制度行动与媒介策略。二者允许大量作品重叠。\n",
      "02 历史条件与先锋姿态.md":"# 历史条件与先锋姿态\n\n工业城市、群众媒体、战争、革命、帝国危机与新技术共同制造了先锋派。先锋姿态常表现为：宣布旧艺术死亡、制造公众冲突、组织团体、占领杂志与剧场、把新媒介直接纳入文学。\n",
      "03 先锋派谱系.md":"# 先锋派谱系\n\n世纪末象征主义/颓废主义 → 未来主义与表现主义 → 达达 → 超现实主义；并行网络包括意象主义/漩涡主义、俄国未来主义—构成主义—LEF，以及伊比利亚与拉美 vanguardias。谱系不是单线继承，而是宣言、杂志、翻译、城市网络与政治事件构成的交叉传播。\n",
      "04 宣言、团体与杂志.md":"# 宣言、团体与杂志\n\n宣言不是作品旁边的说明书，而是先锋派最关键的文学形式之一：它创造“我们”、制造敌人、规定动作、争夺公共空间。杂志、咖啡馆、剧场、朗诵会和小型出版社则是运动能够存在的基础设施。\n",
      "05 媒介实验与语言破坏.md":"# 媒介实验与语言破坏\n\n核心机制包括自由词语、zaum/超理性语言、声音诗、排版、拼贴、自动写作、偶然程序、杂志设计、表演以及图文混合。先锋派把“书页”从透明容器变成可被直接操作的物质。\n",
      "06 艺术、生活与政治.md":"# 艺术、生活与政治\n\n先锋派不断试图突破作品自治：未来主义拥抱技术与行动，达达攻击资产阶级艺术制度，超现实主义连接欲望解放与革命，构成主义/LEF强调生产与社会功能。不同运动的政治方向并不相同，甚至彼此冲突。\n",
      "07 阅读路线.md":"# 阅读路线\n\n## 骨架路线\n先读各运动的★宣言/纲领，再读每个运动1—2部★代表作品，优先建立“运动机制”而不是作者史。\n\n## 深化路线\n按机制横读：宣言政治 → 语言破坏 → 声音/排版 → 偶然/自动写作 → 跨媒介 → 艺术生活化 → 政治介入。\n\n## 边界路线\n最后把同一作品同时放回 M3.1，比较“作为现代主义作品”和“作为先锋派行动”时解释发生什么变化。\n"}
    for n,c in docs.items(): (core/n).write_text(c,encoding="utf-8")
    mov=TOPIC_DIR/"11 主要运动"; mov.mkdir(exist_ok=True)
    (mov/"00 主要运动索引.md").write_text("# 主要运动索引\n\n"+"\n".join(f"- [[{i+1:02d} {m}|{m}]]：{counts.get(m,0)} 部作品" for i,m in enumerate(MOVEMENTS))+"\n",encoding="utf-8")
    for i,m in enumerate(MOVEMENTS):
        (mov/f"{i+1:02d} {m}.md").write_text(f"# {m}\n\n- 当前 canonical works：**{counts.get(m,0)}**\n- 阅读时关注：该运动如何组织集体、制造断裂、操作媒介，并重新定义文学与社会的关系。\n",encoding="utf-8")
    mech=TOPIC_DIR/"12 先锋机制"; mech.mkdir(exist_ok=True)
    (mech/"00 先锋机制索引.md").write_text("# 先锋机制索引\n\n- 宣言政治与集体自我命名\n- 反经典与反艺术制度\n- 语言破坏、造词与超理性语言\n- 声音诗、朗诵与表演\n- 排版、拼贴与书籍物质性\n- 自动写作、梦与偶然程序\n- 杂志、城市与跨国运动网络\n- 艺术—生活合流\n- 革命、民族与反殖民政治\n",encoding="utf-8")
    edge=TOPIC_DIR/"13 边界与转型"; edge.mkdir(exist_ok=True)
    (edge/"00 边界与转型索引.md").write_text("# 边界与转型索引\n\n## M2 → M3.2\n象征主义、唯美主义、颓废主义提供语言自治、艺术自主与反资产阶级姿态；先锋派把这种危机进一步组织为宣言、团体与公共行动。\n\n## M3.1 ↔ M3.2\n现代主义与先锋派不是上下级。前者是更广的美学—历史结构，后者是其中更具运动性、制度攻击性与集体行动性的区域。\n\n## M3.2 → 战后实验\n达达/超现实主义/构成主义等机制继续进入具体诗、实验戏剧、情境主义、Oulipo、行为/观念艺术及战后跨媒介文学。\n",encoding="utf-8")
    src=TOPIC_DIR/"_source"; src.mkdir(exist_ok=True)
    lines=["# M3.2 结构书目映射 v1","",f"- target: **{len(SPECS)}**",f"- reused canonical works: **{len(reused)}**",f"- created canonical works: **{len(created)}**","","## 运动覆盖","","| movement | works |","|---|---:|"]
    for m in MOVEMENTS: lines.append(f"| {m} | {counts.get(m,0)} |")
    lines += ["","## 治理边界","","- 不按年代批量吸收所有 20 世纪前半叶作品。","- 允许同一 canonical Work 同时属于 M3.1 与 M3.2。","- 新增作品只进入 `40 作品/`；专题 Base 动态投影。","- 新增实体的 year / 原文题名等通用 metadata 不在本阶段猜填。"]
    (src/"M3.2书目映射_v1.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    audit=["# M3.2 先锋派书目覆盖审计","",f"- target bibliography: **{len(SPECS)}**",f"- reused canonical works: **{len(reused)}**",f"- newly created canonical works: **{len(created)}**","","待独立审计冻结最终 PASS 状态。"]
    (TOPIC_DIR/"04 先锋派书目覆盖审计.md").write_text("\n".join(audit)+"\n",encoding="utf-8")

def main():
    index={}
    for p in WORKS.glob("*.md"):
        text=p.read_text(encoding="utf-8-sig"); m=fm_match(text)
        names=[p.stem]
        if m:
            fm=m.group(1); t=scalar(fm,"title")
            if t: names.append(t)
            names += list_value(fm,"aliases")
        for name in names: index.setdefault(norm(name),p)
    reused=[]; created=[]; counts=Counter()
    for spec in SPECS:
        title,author,movement,priority,axes=spec; counts[movement]+=1
        p=index.get(norm(title))
        if p:
            update_existing(p,spec); reused.append(title)
        else:
            p=WORKS/f"{title}.md"
            if p.exists(): raise RuntimeError(f"identity collision: {p}")
            p.write_text(new_work(spec),encoding="utf-8"); created.append(title); index[norm(title)]=p
    build_topic_files(counts,reused,created)
    print(f"target={len(SPECS)} reused={len(reused)} created={len(created)}")
    for m in MOVEMENTS: print(f"{m}: {counts[m]}")

if __name__ == "__main__": main()
