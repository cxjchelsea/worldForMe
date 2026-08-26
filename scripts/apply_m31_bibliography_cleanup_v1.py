from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "40 作品"
TOPIC = "WL-TOPIC-M3-MODERNISM"
TOPIC_AXIS = "M3.1 现代主义 / Modernism"
TOPIC_LINK_MARKER = "M3.1 现代主义/00 现代主义文学"

CONTAMINATED = {
    "一九八六年.md", "世事如烟.md", "两地书.md", "二月.md", "俗世奇人.md",
    "十八岁出门远行.md", "古典爱情.md", "四月三日事件.md", "契诃夫短篇小说选.md",
    "往事与刑罚.md", "春桃.md", "朝花夕拾.md", "死亡叙述.md", "河边的错误.md",
    "现实一种.md", "红拂夜奔.md", "给樱桃以性别.md", "难逃劫数.md", "鲜血梅花.md",
    "悉达多.md",
}

TRADITION_NORMALIZE = {
    "德语—奥地利—中欧": "德语—奥地利—中欧现代主义",
    "俄罗斯与东欧": "俄罗斯与东欧现代主义",
    "伊比利亚与意大利": "伊比利亚与意大利现代主义",
    "拉丁美洲与Brazilian Modernismo": "拉丁美洲先锋与巴西Modernismo",
    "法语现代主义与存在主义前夜": "法国现代主义",
}

AUTHOR_FIXES = {
    "坎塔普拉.md": ("拉贾·拉奥", "Raja Rao", "Kanthapura", "1938"),
    "德里黄昏.md": ("艾哈迈德·阿里", "Ahmed Ali", "Twilight in Delhi", "1940"),
    "谢里.md": ("科莱特", "Colette", "Chéri", "1920"),
    "施疗室里.md": ("平林泰子", "Hirabayashi Taiko", "In the Charity Ward", "1927"),
}

AXES = {
    "地下室手记.md": ["意识与内在世界"],
    "饥饿.md": ["意识与内在世界"],
    "一个青年艺术家的画像.md": ["意识与内在世界", "意识流"],
    "尤利西斯.md": ["意识流", "时间重构", "都市现代性", "神话方法", "语言危机"],
    "达洛维夫人.md": ["意识流", "时间重构", "都市现代性", "性别与女性现代主义", "战争与文明危机"],
    "到灯塔去.md": ["意识流", "时间重构", "性别与女性现代主义"],
    "海浪.md": ["意识与内在世界", "语言危机", "性别与女性现代主义"],
    "朝圣.md": ["意识流", "性别与女性现代主义"],
    "古斯特少尉.md": ["意识流", "意识与内在世界"],
    "泽诺的意识.md": ["意识与内在世界", "不可靠叙述"],
    "喧哗与骚动.md": ["意识流", "时间重构", "不可靠叙述"],
    "我弥留之际.md": ["多视角", "时间重构", "不可靠叙述"],
    "押沙龙，押沙龙！.md": ["多视角", "时间重构", "历史与记忆"],
    "靠近野心的心.md": ["意识与内在世界", "性别与女性现代主义", "语言危机"],
    "去斯万家那边.md": ["时间重构", "记忆"],
    "重现的时光.md": ["时间重构", "记忆"],
    "魔山.md": ["时间重构", "战争与文明危机"],
    "虚构集.md": ["时间重构", "元小说", "碎片化与拼贴"],
    "骰子一掷永远取消不了偶然.md": ["碎片化与拼贴", "语言危机"],
    "荒原.md": ["碎片化与拼贴", "神话方法", "战争与文明危机", "都市现代性"],
    "诗章.md": ["碎片化与拼贴", "神话方法", "跨文化翻译"],
    "曼哈顿中转站.md": ["蒙太奇与新媒体", "都市现代性", "碎片化与拼贴", "大众文化与现代主义"],
    "柏林亚历山大广场.md": ["蒙太奇与新媒体", "都市现代性", "碎片化与拼贴", "大众文化与现代主义"],
    "图像诗.md": ["蒙太奇与新媒体", "语言危机"],
    "西伯利亚大铁路和小让娜的法兰西散文诗.md": ["蒙太奇与新媒体", "都市现代性"],
    "上海.md": ["蒙太奇与新媒体", "都市现代性", "大众文化与现代主义", "帝国与殖民现代性"],
    "机械.md": ["蒙太奇与新媒体", "都市现代性", "感知革命"],
    "战争.md": ["蒙太奇与新媒体", "战争与文明危机"],
    "浅草红团.md": ["都市现代性", "大众文化与现代主义", "蒙太奇与新媒体"],
    "夜总会里的五个人.md": ["都市现代性", "大众文化与现代主义", "蒙太奇与新媒体"],
    "梅雨之夕.md": ["都市现代性", "心理现代主义"],
    "都市风景线.md": ["都市现代性", "大众文化与现代主义", "蒙太奇与新媒体"],
    "恶之花.md": ["都市现代性", "感知革命"],
    "黑暗的心.md": ["帝国与殖民现代性", "不可靠叙述"],
    "印度之行.md": ["帝国与殖民现代性"],
    "家庭与世界.md": ["帝国与殖民现代性", "民族主义与现代性"],
    "不可接触者.md": ["帝国与殖民现代性", "社会现实与现代性"],
    "苦力.md": ["帝国与殖民现代性", "都市现代性", "社会现实与现代性"],
    "坎塔普拉.md": ["帝国与殖民现代性", "民族主义与现代性", "口述形式实验"],
    "德里黄昏.md": ["帝国与殖民现代性", "都市现代性", "文化转型"],
    "早安，午夜.md": ["帝国与殖民现代性", "都市现代性", "性别与女性现代主义"],
    "Minty Alley.md": ["帝国与殖民现代性", "都市现代性", "黑人现代性"],
    "一间自己的房间.md": ["性别与女性现代主义", "文学制度"],
    "花园茶会.md": ["性别与女性现代主义", "现代主义短篇"],
    "海园.md": ["性别与女性现代主义", "语言危机"],
    "夜林.md": ["性别与女性现代主义", "都市现代性", "身份与欲望"],
    "他们眼望上苍.md": ["种族与黑人现代主义", "性别与女性现代主义", "语言政治"],
    "甘蔗.md": ["种族与黑人现代主义", "碎片化与拼贴", "现代主义短篇"],
    "哈莱姆之家.md": ["种族与黑人现代主义", "都市现代性", "大众文化与现代主义"],
    "疲倦的布鲁斯.md": ["种族与黑人现代主义", "爵士与大众文化"],
    "The New Negro.md": ["种族与黑人现代主义", "文化运动与宣言"],
    "土生子.md": ["种族与黑人现代主义", "都市现代性"],
    "Color.md": ["种族与黑人现代主义"],
    "The Conjure-Man Dies.md": ["种族与黑人现代主义", "都市现代性", "犯罪叙事"],
    "钱多斯勋爵的信.md": ["语言危机"],
    "温柔的纽扣.md": ["语言危机", "碎片化与拼贴"],
    "特里尔塞.md": ["语言危机", "碎片化与拼贴"],
    "华夏集.md": ["跨文化翻译", "语言危机"],
    "野草.md": ["语言危机", "意识与内在世界"],
    "呐喊.md": ["现代主义短篇", "国民性批判", "语言政治"],
    "都柏林人.md": ["现代主义短篇", "都市现代性"],
    "齿轮.md": ["意识与内在世界", "语言危机"],
    "金锁记.md": ["性别与女性现代主义", "都市现代性", "家庭与权力"],
    "倾城之恋.md": ["性别与女性现代主义", "都市现代性", "战争与文明危机"],
    "六个寻找作者的剧中人.md": ["现代主义戏剧", "元戏剧", "再现危机"],
    "毛猿.md": ["现代主义戏剧", "都市现代性", "异化"],
    "血婚.md": ["现代主义戏剧", "神话方法"],
    "波希米亚之光.md": ["现代主义戏剧", "都市现代性", "再现危机"],
    "海鸥.md": ["现代主义戏剧", "再现危机"],
    "朱莉小姐.md": ["现代主义戏剧", "性别与权力"],
    "盲枭.md": ["意识与内在世界", "不可靠叙述", "语言危机"],
    "变形记（卡夫卡）.md": ["异化", "荒诞", "官僚与现代性"],
    "审判.md": ["异化", "荒诞", "官僚与现代性"],
    "城堡.md": ["异化", "荒诞", "官僚与现代性"],
    "没有个性的人.md": ["主体危机", "社会系统与现代性"],
    "梦游者.md": ["碎片化与拼贴", "文明危机"],
    "彼得堡.md": ["都市现代性", "碎片化与拼贴"],
    "我们.md": ["技术现代性", "异化", "政治现代性"],
    "马库纳伊玛.md": ["神话方法", "民族文化与现代性", "语言实验"],
    "食人宣言.md": ["文化运动与宣言", "帝国与殖民现代性", "跨文化翻译"],
    "阿尔塔索尔.md": ["语言危机", "先锋形式实验"],
    "大地上的居所.md": ["语言危机", "主体危机"],
    "雾.md": ["元小说", "主体危机"],
    "惶然录.md": ["主体危机", "碎片化与拼贴"],
    "局外人.md": ["荒诞", "异化", "战后转向"],
}

NEW_WORKS = [
    {
        "file": "Passing.md", "title": "Passing", "title_original": "Passing",
        "author": "内拉·拉森", "author_original": "Nella Larsen", "year": 1929,
        "axis_r": "R5 北美文学", "axis_g": "G3 小说", "priority": "★",
        "tradition": "美国与Harlem Renaissance",
        "axes": ["种族与黑人现代主义", "性别与女性现代主义", "都市现代性", "身份与表演"],
        "history": "哈莱姆文艺复兴与黑人现代主义",
    },
    {
        "file": "Quicksand.md", "title": "Quicksand", "title_original": "Quicksand",
        "author": "内拉·拉森", "author_original": "Nella Larsen", "year": 1928,
        "axis_r": "R5 北美文学", "axis_g": "G3 小说", "priority": "◆",
        "tradition": "美国与Harlem Renaissance",
        "axes": ["种族与黑人现代主义", "性别与女性现代主义", "都市现代性", "跨国身份"],
        "history": "哈莱姆文艺复兴与黑人现代主义",
    },
    {
        "file": "The Girl Who Killed to Save.md", "title": "The Girl Who Killed to Save",
        "title_original": "The Girl Who Killed to Save", "author": "H. I. E. Dhlomo",
        "author_original": "H. I. E. Dhlomo", "year": 1935,
        "axis_r": "R7 非洲文学", "axis_g": "G5 戏剧", "priority": "★",
        "tradition": "殖民与跨国现代主义",
        "axes": ["帝国与殖民现代性", "现代主义戏剧", "非洲现代主义", "民族主义与现代性"],
        "history": "南非黑人现代主义与全球现代主义扩展",
    },
]


def split_doc(text: str):
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", text
    return text[4:end], text[end + 4:]


def field_span(lines: list[str], key: str):
    for i, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            j = i + 1
            while j < len(lines) and not re.match(r"^[A-Za-z0-9_]+:", lines[j]):
                j += 1
            return i, j
    return None


def get_scalar(lines: list[str], key: str):
    span = field_span(lines, key)
    if not span:
        return ""
    i, _ = span
    return lines[i].split(":", 1)[1].strip().strip("'\"")


def get_list(lines: list[str], key: str):
    span = field_span(lines, key)
    if not span:
        return []
    i, j = span
    inline = lines[i].split(":", 1)[1].strip()
    if inline == "[]":
        return []
    vals = []
    for line in lines[i + 1:j]:
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m:
            vals.append(m.group(1).strip().strip("'\""))
    return vals


def set_scalar(lines: list[str], key: str, value: str):
    span = field_span(lines, key)
    line = f"{key}: {value}"
    if span:
        i, j = span
        lines[i:j] = [line]
    else:
        lines.append(line)


def set_list(lines: list[str], key: str, values: list[str]):
    span = field_span(lines, key)
    block = [f"{key}: []"] if not values else [f"{key}:"] + [f"- {v}" for v in values]
    if span:
        i, j = span
        lines[i:j] = block
    else:
        lines.extend(block)


def remove_field(lines: list[str], key: str):
    span = field_span(lines, key)
    if span:
        i, j = span
        del lines[i:j]


def write_lines(path: Path, lines: list[str], body: str):
    path.write_text("---\n" + "\n".join(lines).rstrip() + "\n---" + body, encoding="utf-8")


changed = []
for path in sorted(WORKS.glob("*.md")):
    text = path.read_text(encoding="utf-8")
    fm, body = split_doc(text)
    if not fm:
        continue
    lines = fm.splitlines()
    topics = get_list(lines, "topics")
    if TOPIC not in topics:
        continue

    before = "\n".join(lines)

    if path.name in CONTAMINATED or get_scalar(lines, "modernism_priority") == "补录":
        set_list(lines, "topics", [x for x in topics if x != TOPIC])
        set_list(lines, "axis_m", [x for x in get_list(lines, "axis_m") if x != TOPIC_AXIS])
        set_list(lines, "topic_links", [x for x in get_list(lines, "topic_links") if TOPIC_LINK_MARKER not in x])
        remove_field(lines, "modernism_priority")
        remove_field(lines, "modernism_tradition_cluster")
        remove_field(lines, "modernism_axes")
    else:
        trad = get_scalar(lines, "modernism_tradition_cluster")
        if trad in TRADITION_NORMALIZE:
            set_scalar(lines, "modernism_tradition_cluster", TRADITION_NORMALIZE[trad])

        if path.name in AUTHOR_FIXES:
            author, author_original, title_original, year = AUTHOR_FIXES[path.name]
            set_scalar(lines, "author", author)
            set_scalar(lines, "author_original", author_original)
            set_scalar(lines, "title_original", title_original)
            set_scalar(lines, "year", year)
            set_scalar(lines, "verification_status", "手工核验")

        if path.name in AXES:
            merged = []
            for item in get_list(lines, "modernism_axes") + AXES[path.name]:
                if item and item not in merged:
                    merged.append(item)
            set_list(lines, "modernism_axes", merged)

    after = "\n".join(lines)
    if after != before:
        write_lines(path, lines, body)
        changed.append(path.name)

# allocate new numeric work IDs deterministically from current max
max_id = 0
for path in WORKS.glob("*.md"):
    fm, _ = split_doc(path.read_text(encoding="utf-8"))
    m = re.search(r"(?m)^id:\s*WL-WORK-(\d+)\s*$", fm)
    if m:
        max_id = max(max_id, int(m.group(1)))

for spec in NEW_WORKS:
    path = WORKS / spec["file"]
    if path.exists():
        continue
    max_id += 1
    axes = "\n".join(f"- {x}" for x in spec["axes"])
    content = f'''---
id: WL-WORK-{max_id:04d}
type: work
title: {spec['title']}
title_original: {spec['title_original']}
aliases: []
author: {spec['author']}
author_original: {spec['author_original']}
year: {spec['year']}
literary_traditions: []
read_status: 未读
axis_t:
- T4 全球现代主义时代
axis_r:
- {spec['axis_r']}
axis_m:
- M3.1 现代主义 / Modernism
axis_g:
- {spec['axis_g']}
axis_q: []
axis_source: curated_m31_v2
topics:
- WL-TOPIC-M3-MODERNISM
topic_links:
- '[[../30 专题/M3.1 现代主义/00 现代主义文学|现代主义文学]]'
modernism_priority: {spec['priority']}
modernism_tradition_cluster: {spec['tradition']}
modernism_axes:
{axes}
t4_priority: {spec['priority']}
t4_history_position: {spec['history']}
t4_mechanism:
- 帝国、殖民、反殖民与文化翻译
- 小杂志、翻译、流亡与跨国网络
verification_status: 手工核验
bibliography_status: curated
---
# {spec['title']}

## 基本信息

- 作者：{spec['author_original']}
- 首次出版年：{spec['year']}
- 阅读状态：未读

## 专题位置

- [[../30 专题/M3.1 现代主义/00 现代主义文学|现代主义文学]]
  - 专题优先级：{spec['priority']}
  - 传统入口：{spec['tradition']}
  - 机制：{'；'.join(spec['axes'])}

## 数据说明

> 本文件是中央作品库的唯一 Work 实体。此次作为 M3.1 V2 覆盖缺口补录。
'''
    path.write_text(content, encoding="utf-8")
    changed.append(path.name)

print(f"changed_files={len(changed)}")
for name in changed:
    print(name)
