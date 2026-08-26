from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = LIT / "40 作品"
TOPIC_DIR = LIT / "30 专题" / "M1 早期现代思想与美学"
TOPIC_ID = "WL-TOPIC-M1-EARLY-MODERN"
LINK = "[[../30 专题/M1 早期现代思想与美学/00 早期现代思想与美学|M1 早期现代思想与美学]]"

# title, author, movement, priority, mechanisms
BIB = [
    # Humanism
    ("论人的尊严","乔瓦尼·皮科·德拉·米兰多拉","人文主义","★",["人的尊严","自由意志","古典复兴"]),
    ("愚人颂","伊拉斯谟","人文主义","★",["人文主义讽刺","教会批判","理性反思"]),
    ("乌托邦","托马斯·莫尔","人文主义","★",["理想社会","政治想象","古典对话体"]),
    ("君主论","尼科洛·马基雅维利","人文主义","★",["世俗政治","国家理性","现实主义政治观"]),
    ("廷臣论","巴尔达萨雷·卡斯蒂廖内","人文主义","◆",["宫廷文化","人格塑造","修辞与礼仪"]),
    ("随笔集","米歇尔·德·蒙田","人文主义","★",["自我书写","怀疑主义","主体形成"]),
    ("巨人传","弗朗索瓦·拉伯雷","人文主义","★",["身体与狂欢","人文主义讽刺","知识解放"]),
    ("七日谈","玛格丽特·德·纳瓦尔","人文主义","◆",["世俗叙事","性别与欲望","短篇框架"]),
    ("论学问的进步","弗朗西斯·培根","人文主义","◆",["知识秩序","经验主义前史","现代知识观"]),

    # Renaissance
    ("歌集","弗朗切斯科·彼特拉克","文艺复兴","★",["抒情主体","古典复兴","世俗爱情"]),
    ("十日谈","乔万尼·薄伽丘","文艺复兴","★",["世俗叙事","城市社会","短篇框架"]),
    ("疯狂的奥兰多","卢多维科·阿里奥斯托","文艺复兴","★",["骑士传统重写","反讽","古典与俗语"]),
    ("被解放的耶路撒冷","托尔夸托·塔索","文艺复兴","◆",["史诗重写","宗教与英雄","古典规范"]),
    ("仙后","埃德蒙·斯宾塞","文艺复兴","★",["寓言史诗","民族国家","古典与基督教"]),
    ("阿斯特洛菲尔与斯黛拉","菲利普·锡德尼","文艺复兴","◆",["十四行诗传统","宫廷爱情","自我反思"]),
    ("浮士德博士","克里斯托弗·马洛","文艺复兴","★",["知识欲望","现代主体","戏剧革命"]),
    ("哈姆雷特","威廉·莎士比亚","文艺复兴","★",["主体内省","复仇悲剧","戏剧革命"]),
    ("李尔王","威廉·莎士比亚","文艺复兴","★",["王权与家庭","悲剧主体","秩序危机"]),
    ("暴风雨","威廉·莎士比亚","文艺复兴","★",["知识与权力","殖民前史","戏剧幻术"]),
    ("莎士比亚十四行诗","威廉·莎士比亚","文艺复兴","◆",["抒情主体","时间与欲望","十四行诗传统"]),
    ("堂吉诃德","米格尔·德·塞万提斯","文艺复兴","★",["小说自反","骑士传统解构","现代主体"]),
    ("小癞子","佚名","文艺复兴","★",["流浪汉小说","社会阶层","反英雄"]),
    ("羊泉村","洛佩·德·维加","文艺复兴","◆",["民族戏剧","共同体","荣誉政治"]),
    ("塞莱斯蒂娜","费尔南多·德·罗哈斯","文艺复兴","◆",["中世纪向早期现代过渡","欲望与市场","对话体"]),
    ("嘉尔西拉索诗集","嘉尔西拉索·德·拉·维加","文艺复兴","◆",["意大利诗体传播","宫廷抒情","古典模仿"]),
    ("卢济塔尼亚人之歌","路易斯·德·卡蒙斯","文艺复兴","★",["帝国史诗","航海与扩张","古典史诗重写"]),

    # Baroque
    ("人生如梦","佩德罗·卡尔德隆·德·拉·巴尔卡","巴洛克","★",["现实与幻象","自由意志","巴洛克戏剧"]),
    ("孤独集","路易斯·德·贡戈拉","巴洛克","★",["华丽文体","隐喻密度","语言复杂化"]),
    ("梦集","弗朗西斯科·德·克维多","巴洛克","◆",["讽刺与幻象","社会批判","概念主义"]),
    ("批评家","巴尔塔萨尔·格拉西安","巴洛克","◆",["寓言人生","概念主义","世界剧场"]),
    ("第一梦","胡安娜·伊内斯·德·拉·克鲁斯","巴洛克","★",["殖民巴洛克","知识欲望","女性主体"]),
    ("答索尔·菲洛泰亚修女","胡安娜·伊内斯·德·拉·克鲁斯","巴洛克","★",["女性知识权","殖民巴洛克","自我辩护"]),
    ("失乐园","约翰·弥尔顿","巴洛克","★",["史诗重写","宗教政治","自由意志"]),
    ("神圣十四行诗","约翰·多恩","巴洛克","★",["玄学诗","信仰与身体","智性隐喻"]),
    ("歌与十四行诗","约翰·多恩","巴洛克","◆",["玄学诗","爱情与身体","智性隐喻"]),
    ("圣殿","乔治·赫伯特","巴洛克","◆",["宗教抒情","版面形式","信仰体验"]),
    ("西里西亚天使","安格鲁斯·西勒修斯","巴洛克","◆",["神秘主义","警句体","悖论"]),
    ("痴儿西木传","汉斯·雅各布·克里斯托弗·冯·格里梅尔斯豪森","巴洛克","★",["战争经验","流浪汉小说","德语巴洛克"]),

    # Classicism
    ("熙德","皮埃尔·高乃依","古典主义","★",["荣誉与情感","三一律争论","古典主义戏剧"]),
    ("贺拉斯","皮埃尔·高乃依","古典主义","◆",["国家与家庭","古典主义戏剧","义务伦理"]),
    ("安德洛玛刻","让·拉辛","古典主义","★",["激情与秩序","古典悲剧","心理集中"]),
    ("费德尔","让·拉辛","古典主义","★",["激情与罪","古典悲剧","心理集中"]),
    ("伪君子","莫里哀","古典主义","★",["喜剧规范","宗教伪善","社会观察"]),
    ("恨世者","莫里哀","古典主义","★",["宫廷社会","喜剧规范","个人与礼俗"]),
    ("寓言诗","让·德·拉封丹","古典主义","★",["寓言传统","社会讽喻","古典模仿"]),
    ("诗艺","尼古拉·布瓦洛","古典主义","★",["规则美学","模仿古典","文类秩序"]),
    ("人物志","让·德·拉布吕耶尔","古典主义","◆",["性格书写","宫廷社会","道德观察"]),
    ("克莱芙王妃","拉法耶特夫人","古典主义","★",["心理小说前史","宫廷秩序","欲望与自制"]),

    # Enlightenment
    ("鲁滨逊漂流记","丹尼尔·笛福","启蒙主义","★",["个人主义","劳动与财产","殖民现代性"]),
    ("格列佛游记","乔纳森·斯威夫特","启蒙主义","★",["理性批判","政治讽刺","旅行叙事"]),
    ("波斯人信札","孟德斯鸠","启蒙主义","★",["异域视角","制度批判","书信体"]),
    ("老实人","伏尔泰","启蒙主义","★",["理性批判","乐观主义批判","哲理小说"]),
    ("哲学通信","伏尔泰","启蒙主义","◆",["公共理性","比较文明","思想传播"]),
    ("百科全书","狄德罗、达朗贝尔等","启蒙主义","★",["知识分类","公共理性","出版公共领域"]),
    ("拉摩的侄儿","德尼·狄德罗","启蒙主义","★",["对话体","道德相对性","主体分裂"]),
    ("宿命论者雅克","德尼·狄德罗","启蒙主义","★",["叙事自反","决定论争论","小说实验"]),
    ("汤姆·琼斯","亨利·菲尔丁","启蒙主义","★",["社会全景","小说规范","道德判断"]),
    ("项狄传","劳伦斯·斯特恩","启蒙主义","★",["叙事自反","时间实验","小说形式"]),
    ("塞维利亚理发师","博马舍","启蒙主义","◆",["等级讽刺","公共剧场","社会流动"]),
    ("费加罗的婚礼","博马舍","启蒙主义","★",["等级批判","革命前夜","公共剧场"]),
    ("危险关系","肖德洛·德·拉克洛","启蒙主义","★",["书信体","欲望与权力","贵族秩序危机"]),
    ("智者纳坦","戈特霍尔德·埃弗拉伊姆·莱辛","启蒙主义","★",["宗教宽容","公共理性","启蒙戏剧"]),
    ("爱米丽雅·迦洛蒂","戈特霍尔德·埃弗拉伊姆·莱辛","启蒙主义","◆",["市民悲剧","权力批判","家庭伦理"]),
    ("汉堡剧评","戈特霍尔德·埃弗拉伊姆·莱辛","启蒙主义","◆",["戏剧美学","公共批评","反法式规范"]),
    ("社会契约论","让-雅克·卢梭","启蒙主义","★",["政治主体","人民主权","社会秩序"]),
    ("论科学与艺术","让-雅克·卢梭","启蒙主义","◆",["文明批判","反进步叙事","自然观"]),

    # Sentimentalism
    ("帕梅拉","塞缪尔·理查逊","感伤主义","★",["书信体","道德感情","内心书写"]),
    ("克拉丽莎","塞缪尔·理查逊","感伤主义","★",["书信体","道德感情","女性主体"]),
    ("新爱洛绮丝","让-雅克·卢梭","感伤主义","★",["自然与情感","书信体","感情共同体"]),
    ("感伤旅行","劳伦斯·斯特恩","感伤主义","★",["感受性","旅行叙事","主体情感"]),
    ("有感情的人","亨利·麦肯齐","感伤主义","◆",["感受性","道德同情","男性情感"]),
    ("少年维特的烦恼","约翰·沃尔夫冈·冯·歌德","感伤主义","★",["情感主体","书信体","向浪漫主义过渡"]),
    ("可怜的丽莎","尼古拉·卡拉姆津","感伤主义","★",["俄国感伤主义","阶级与情感","女性悲剧"]),
    ("保尔和维吉妮","雅克-亨利·贝尔纳丹·德·圣皮埃尔","感伤主义","◆",["自然与情感","殖民空间","纯真神话"]),
    ("威克菲尔德的牧师","奥利弗·哥尔德斯密斯","感伤主义","◆",["家庭伦理","感受性","市民道德"]),
    ("忏悔录","让-雅克·卢梭","感伤主义","★",["自我书写","真实性","现代主体"]),
]

MOVEMENTS = ["人文主义","文艺复兴","巴洛克","古典主义","启蒙主义","感伤主义"]


def norm(s: str) -> str:
    return re.sub(r"[\s·・\-—_（）()《》〈〉:：,，.。'\"“”‘’]", "", (s or "").lower())


def split_doc(text: str):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end], text[end+5:]
    return "", text


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*[\"']?(.*?)[\"']?\s*$", fm)
    return m.group(1).strip().strip("\"'") if m else ""


def list_field(fm: str, key: str):
    lines = fm.splitlines()
    out=[]
    for i,line in enumerate(lines):
        if line.startswith(key+":"):
            tail=line.split(":",1)[1].strip()
            if tail.startswith("[") and tail.endswith("]"):
                inner=tail[1:-1].strip()
                return [x.strip().strip("\"'") for x in inner.split(",") if x.strip()]
            j=i+1
            while j < len(lines) and lines[j].startswith("-"):
                out.append(lines[j][1:].strip().strip("\"'"))
                j+=1
            return out
    return out


def set_list(fm: str, key: str, vals):
    vals=list(dict.fromkeys(vals))
    lines=fm.splitlines()
    start=None; end=None
    for i,line in enumerate(lines):
        if line.startswith(key+":"):
            start=i; end=i+1
            while end < len(lines) and lines[end].startswith("-"):
                end+=1
            break
    block=[key+":"]+[f"- {v}" for v in vals]
    if start is None:
        if lines and lines[-1].strip(): lines.append("")
        lines.extend(block)
    else:
        lines=lines[:start]+block+lines[end:]
    return "\n".join(lines).strip()+"\n"


def set_scalar(fm: str, key: str, val: str):
    lines=fm.splitlines()
    for i,line in enumerate(lines):
        if line.startswith(key+":"):
            lines[i]=f'{key}: "{val}"' if isinstance(val,str) else f"{key}: {val}"
            return "\n".join(lines).strip()+"\n"
    lines.append(f'{key}: "{val}"' if isinstance(val,str) else f"{key}: {val}")
    return "\n".join(lines).strip()+"\n"


def author_match(a: str,b: str)->bool:
    na,nb=norm(a),norm(b)
    return bool(na and nb and (na in nb or nb in na))


def safe_filename(title: str, author: str):
    base=re.sub(r"[\\/:*?\"<>|]","_",title)
    p=WORKS/(base+".md")
    if not p.exists(): return p
    suffix=re.sub(r"[\\/:*?\"<>|]","_",author.split("·")[-1][:12])
    return WORKS/f"{base}（{suffix}）.md"


def write_topic_structure():
    TOPIC_DIR.mkdir(parents=True,exist_ok=True)
    files={
"00 早期现代思想与美学.md":'''---\nid: WL-TOPIC-M1-EARLY-MODERN\ntype: literature_topic\naxis: M\nnode: M1\nstatus: m-axis-v2\n---\n# M1 早期现代思想与美学\n\n> 核心问题：欧洲从中世纪共同体进入早期现代世界时，“人、知识、自然、国家、古典传统与情感”如何被重新定义，并改变文学？\n\n## 认知主线\n古典文本再发现与人文主义 → 文艺复兴的主体、世俗生活与文类重造 → 宗教改革、国家形成与帝国扩张带来的秩序危机 → 巴洛克的幻象与复杂化 → 古典主义的规则、节制与公共规范 → 启蒙主义的理性、公共领域与制度批判 → 感伤主义对理性主义的情感修正，并向 M2 浪漫主义过渡。\n\n## 边界\nM1 不是“1400—1800年的所有文学”。这里的人文主义、文艺复兴、巴洛克、古典主义、启蒙主义、感伤主义主要是欧洲—大西洋文学史范畴；非欧洲同期文学不因年代相同而强行套入这些标签。\n\n## 数据入口\n- [[02 早期现代思想与美学结构.base|结构 Base]]\n- [[03 早期现代思想与美学作品.base|作品 Base]]\n- [[04 早期现代思想与美学书目覆盖审计|书目覆盖审计]]\n''',
"10 核心结构/01 定义与边界.md":'''---\nid: WL-TOPIC-M1-BOUNDARY\ntype: literature_topic_structure\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 定义与边界\n\nM1 研究的不是一个统一主义，而是一系列共同推动早期现代文学制度形成的思想与美学变化：人的尊严与主体性、古典传统的重新发现、世俗政治、宗教分裂、印刷公共性、国家与帝国、规范美学、理性批判和感受性。\n\n不把中国、日本、南亚等同期文学自动归为“文艺复兴/巴洛克/启蒙主义”；比较必须基于具体传播或可论证的结构相似，而不是年代同步。\n''',
"10 核心结构/02 历史条件与问题意识.md":'''---\nid: WL-TOPIC-M1-CONTEXT\ntype: literature_topic_structure\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 历史条件与问题意识\n\n关键条件包括：古典手稿复兴与人文学科、印刷术扩散、宗教改革与宗派冲突、宫廷与城市公共生活、民族国家形成、海外扩张与殖民接触、科学革命与经验知识增长、沙龙/期刊/剧场等公共文化空间。\n''',
"10 核心结构/03 思想谱系与内部结构.md":'''---\nid: WL-TOPIC-M1-GENEALOGY\ntype: literature_topic_structure\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 思想谱系与内部结构\n\n人文主义提供“人—古典传统—教育”的新框架；文艺复兴将其落实为新的主体、世俗生活和文类实践；巴洛克把宗教、战争、帝国与认知不稳定转成幻象、悖论和语言复杂化；古典主义以规则、秩序与公共规范回应失序；启蒙主义扩大理性批判与公共领域；感伤主义则重新强调情感、同情与真实性，并向浪漫主义过渡。\n''',
"10 核心结构/04 美学主张与文学机制.md":'''---\nid: WL-TOPIC-M1-MECHANISMS\ntype: literature_topic_structure\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 美学主张与文学机制\n\n跨板块机制：古典模仿与重写、俗语文学、现代主体与自我书写、宫廷与公共礼仪、戏剧公共性、规则美学、寓言与讽刺、书信体与公共理性、小说自反、感受性与道德同情、现实/幻象、殖民与帝国想象。\n''',
"10 核心结构/05 传播、地域与非同步性.md":'''---\nid: WL-TOPIC-M1-TRANSMISSION\ntype: literature_topic_structure\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 传播、地域与非同步性\n\nM1 重点覆盖意大利、伊比利亚、法国、英格兰、德语世界以及大西洋殖民空间。传播依赖翻译、印刷、宫廷、大学、教会、剧场、沙龙和殖民网络。各地进入早期现代性的节奏不同，因此不建立统一硬年代。\n''',
"10 核心结构/06 与T2、M2的边界.md":'''---\nid: WL-TOPIC-M1-ADJACENCY\ntype: literature_topic_structure\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 与 T2、M2 的边界\n\nT2 主要回答早期现代文学世界“发生了什么、在哪些传统中发生”；M1 回答这些变化背后的文学观念与美学逻辑。M1 到 M2 的关键转折不是 1800 年这个数字本身，而是革命、工业化、民族主义和现代社会结构使“个人—自然—社会”矛盾成为新的核心问题。\n''',
"10 核心结构/07 阅读路线.md":'''---\nid: WL-TOPIC-M1-ROUTE\ntype: literature_topic_structure\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 阅读路线\n\n建议先读 ★ 骨架，依次抓住：人文主义的“人” → 文艺复兴的主体与文类 → 巴洛克的世界不稳定 → 古典主义的秩序 → 启蒙的理性与公共性 → 感伤主义的情感转向。再用 ◆ 扩展地域、文类与机制。\n''',
"11 主要思潮/00 主要思潮索引.md":'''---\nid: WL-TOPIC-M1-MOVEMENTS\ntype: literature_topic_index\ntopic_id: WL-TOPIC-M1-EARLY-MODERN\n---\n# 主要思潮\n\n- [[01 人文主义]]\n- [[02 文艺复兴]]\n- [[03 巴洛克]]\n- [[04 古典主义]]\n- [[05 启蒙主义]]\n- [[06 感伤主义]]\n''',
"11 主要思潮/01 人文主义.md":"# 人文主义\n\n核心：人的尊严、古典教育、修辞、世俗知识与自我塑造。它首先是一种知识和教育结构，不应等同于所有文艺复兴文学。\n",
"11 主要思潮/02 文艺复兴.md":"# 文艺复兴\n\n核心：古典复兴进入戏剧、史诗、抒情与新兴小说；主体、自我、世俗欲望、国家和帝国经验被重新组织。\n",
"11 主要思潮/03 巴洛克.md":"# 巴洛克\n\n核心：宗教分裂、战争、帝国和认识不稳定转化为幻象、悖论、华丽语言、世界剧场与复杂形式。殖民巴洛克是本节点的重要变体。\n",
"11 主要思潮/04 古典主义.md":"# 古典主义\n\n核心：规则、节制、文类秩序、模仿古典和公共规范；尤其以17世纪法国戏剧与批评制度为中心。\n",
"11 主要思潮/05 启蒙主义.md":"# 启蒙主义\n\n核心：公共理性、制度批判、知识分类、宗教宽容、社会契约、讽刺与哲理叙事，并依赖出版和公共领域。\n",
"11 主要思潮/06 感伤主义.md":"# 感伤主义\n\n核心：感受性、同情、真实性、书信体和内心书写；既属于18世纪文化，也构成浪漫主义的重要过渡。\n",
"12 核心矛盾/00 核心矛盾索引.md":'''# 核心矛盾\n\n- 人的尊严 vs 宗教/等级秩序\n- 古典模仿 vs 俗语与现代经验\n- 自由意志 vs 神意/决定论\n- 秩序与规则 vs 激情与幻象\n- 理性与进步 vs 文明批判\n- 公共规范 vs 私人情感与真实性\n- 欧洲自我建构 vs 帝国/殖民他者\n''',
"13 转型/00 转型关系索引.md":'''# 转型关系\n\n人文主义 → 文艺复兴：从知识/教育计划进入文学形式与主体实践。\n\n文艺复兴 → 巴洛克：稳定的人文主义世界图景受到宗教、战争、帝国与认知危机冲击。\n\n巴洛克 ↔ 古典主义：复杂、幻象与失序同规则、秩序和规范并存而竞争。\n\n古典主义 → 启蒙主义：规范美学扩展为公共理性、批评制度与社会政治问题。\n\n启蒙主义 → 感伤主义：理性框架内部出现对感受性、同情和真实性的补充与反拨。\n\n感伤主义 → M2 浪漫主义：情感主体、自然和真实性逐渐成为19世纪的新中心。\n''',
"02 早期现代思想与美学结构.base":'''filters:\n  and:\n    - file.hasTag("#literature_topic_structure") || file.path.contains("M1 早期现代思想与美学")\nviews:\n  - type: table\n    name: M1 结构\n    order:\n      - file.name\n''',
"03 早期现代思想与美学作品.base":f'''filters:\n  and:\n    - topics.contains("{TOPIC_ID}")\nviews:\n  - type: table\n    name: M1 作品\n    order:\n      - m1_priority\n      - m1_movement_cluster\n      - file.name\n''',
"01 早期现代思想与美学.canvas":'''{"nodes":[{"id":"root","type":"file","file":"00 早期现代思想与美学.md","x":0,"y":0,"width":420,"height":240},{"id":"context","type":"file","file":"10 核心结构/02 历史条件与问题意识.md","x":0,"y":-360,"width":360,"height":200},{"id":"humanism","type":"file","file":"11 主要思潮/01 人文主义.md","x":-900,"y":220,"width":320,"height":180},{"id":"renaissance","type":"file","file":"11 主要思潮/02 文艺复兴.md","x":-540,"y":220,"width":320,"height":180},{"id":"baroque","type":"file","file":"11 主要思潮/03 巴洛克.md","x":-180,"y":220,"width":320,"height":180},{"id":"classicism","type":"file","file":"11 主要思潮/04 古典主义.md","x":180,"y":220,"width":320,"height":180},{"id":"enlightenment","type":"file","file":"11 主要思潮/05 启蒙主义.md","x":540,"y":220,"width":320,"height":180},{"id":"sentimentalism","type":"file","file":"11 主要思潮/06 感伤主义.md","x":900,"y":220,"width":320,"height":180},{"id":"mechanisms","type":"file","file":"10 核心结构/04 美学主张与文学机制.md","x":0,"y":520,"width":380,"height":200},{"id":"route","type":"file","file":"10 核心结构/07 阅读路线.md","x":0,"y":820,"width":360,"height":180}],"edges":[{"id":"e1","fromNode":"context","toNode":"root"},{"id":"e2","fromNode":"root","toNode":"humanism"},{"id":"e3","fromNode":"humanism","toNode":"renaissance"},{"id":"e4","fromNode":"renaissance","toNode":"baroque"},{"id":"e5","fromNode":"baroque","toNode":"classicism"},{"id":"e6","fromNode":"classicism","toNode":"enlightenment"},{"id":"e7","fromNode":"enlightenment","toNode":"sentimentalism"},{"id":"e8","fromNode":"baroque","toNode":"mechanisms"},{"id":"e9","fromNode":"classicism","toNode":"mechanisms"},{"id":"e10","fromNode":"enlightenment","toNode":"mechanisms"},{"id":"e11","fromNode":"mechanisms","toNode":"route"}]}'''
    }
    for rel,content in files.items():
        p=TOPIC_DIR/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding="utf-8")


def main():
    write_topic_structure()
    WORKS.mkdir(parents=True,exist_ok=True)
    index=[]
    for p in WORKS.glob("*.md"):
        text=p.read_text(encoding="utf-8",errors="ignore")
        fm,_=split_doc(text)
        if not fm: continue
        title=scalar(fm,"title") or p.stem
        author=scalar(fm,"author")
        aliases=list_field(fm,"aliases")
        index.append((p,text,fm,title,author,aliases))

    reused=0; created=0; collisions=[]
    counts=Counter()
    for title,author,movement,priority,axes in BIB:
        title_norms={norm(title)}
        matches=[]
        for item in index:
            p,text,fm,t,a,aliases=item
            if norm(t) in title_norms or any(norm(x) in title_norms for x in aliases):
                if author_match(author,a): matches.append(item)
        if len(matches)==1:
            p,text,fm,t,a,aliases=matches[0]
            body=split_doc(text)[1]
            fm=set_list(fm,"axis_m",list_field(fm,"axis_m")+["M1 早期现代思想与美学"])
            fm=set_list(fm,"topics",list_field(fm,"topics")+[TOPIC_ID])
            fm=set_scalar(fm,"m1_priority",priority)
            fm=set_scalar(fm,"m1_movement_cluster",movement)
            fm=set_list(fm,"m1_axes",axes)
            p.write_text("---\n"+fm+"---\n"+body.lstrip("\n"),encoding="utf-8")
            reused+=1
        else:
            # If same title exists but author does not match, never overwrite: create a disambiguated canonical entity.
            same_title=[x for x in index if norm(x[3])==norm(title) or any(norm(y)==norm(title) for y in x[5])]
            if same_title: collisions.append((title,author,[x[4] for x in same_title]))
            p=safe_filename(title,author)
            entity=f'''---\nid: WL-WORK-M1-{abs(hash((title,author))) % 100000000:08d}\ntype: work\ntitle: "{title}"\naliases: []\nauthor: "{author}"\nyear: null\nread_status: 未读\naxis_t: []\naxis_r: []\naxis_m:\n- M1 早期现代思想与美学\naxis_g: []\naxis_q: []\naxis_source: manual_m1_structural_gap_fill_v1\ntopics:\n- {TOPIC_ID}\ntopic_links: []\nm1_priority: "{priority}"\nm1_movement_cluster: "{movement}"\nm1_axes:\n''' + ''.join(f'- {x}\n' for x in axes) + '''verification_status: 手工核验\nbibliography_status: structural_anchor_metadata_pending\n---\n# '''+title+'''\n\n## M1 专题角色\n\n- 思潮：'''+movement+'''\n- 专题优先级：'''+priority+'''\n- 机制：'''+" / ".join(axes)+'''\n\n> M1 Structural Gap Fill V1：用于补齐早期现代思想与美学的结构槽位；年份、原文题名等通用书目字段留待中央作品库统一校验。\n'''
            p.write_text(entity,encoding="utf-8")
            created+=1
        counts[movement]+=1

    audit=TOPIC_DIR/"04 早期现代思想与美学书目覆盖审计.md"
    audit.write_text("# M1 早期现代思想与美学书目覆盖审计\n\n- target bibliography: **%d**\n- reused canonical works: **%d**\n- newly created canonical works: **%d**\n\n## 六个板块\n\n%s\n\n## 同名但作者不一致的安全分流\n\n%s\n\n待独立审计冻结最终 PASS 状态。\n"%(len(BIB),reused,created,"\n".join(f"- {k}: {counts[k]}" for k in MOVEMENTS),"\n".join(f"- {t} / {a}；既有作者：{old}" for t,a,old in collisions) or "- 无"),encoding="utf-8")
    print(f"target={len(BIB)} reused={reused} created={created}")
    for k in MOVEMENTS: print(f"{k}: {counts[k]}")
    if collisions:
        print("collisions:")
        for c in collisions: print(c)

if __name__ == "__main__":
    main()
