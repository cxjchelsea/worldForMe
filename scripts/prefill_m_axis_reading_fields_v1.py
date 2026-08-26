from __future__ import annotations

import csv
import importlib.util
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HELPER_PATH = ROOT / "scripts" / "prefill_t_axis_reading_fields_v1.py"
spec = importlib.util.spec_from_file_location("t_prefill", HELPER_PATH)
h = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(h)

AUDIT = h.WORLD / "_audit" / "m_axis"
REPORT = AUDIT / "M_AXIS_READING_PREFILL_V1.md"
DETAIL = AUDIT / "M_AXIS_READING_PREFILL_V1.csv"

CFG = {
    "M1": dict(priority="m1_priority", cluster="m1_movement_cluster",
               history="m1_history_position", role="m1_topic_role", axes="m1_axes",
               axis="M1 早期现代思想与美学", expected=76),
    "M2": dict(priority="m2_priority", cluster="m2_movement_cluster",
               history="m2_history_position", role="m2_topic_role", axes="m2_axes",
               axis="M2 19世纪文学思潮", expected=85),
    "M3.1": dict(priority="modernism_priority", cluster="modernism_tradition_cluster",
                 history="modernism_history_position", role="modernism_topic_role", axes="modernism_axes",
                 axis="M3.1 现代主义 / Modernism", expected=149),
    "M3.2": dict(priority="m32_priority", cluster="m32_movement_cluster",
                 history="m32_history_position", role="m32_topic_role", axes="m32_axes",
                 axis="M3.2 先锋派", expected=68),
    "M4": dict(priority="m4_priority", cluster="m4_movement_cluster",
               history="m4_history_position", role="m4_topic_role", axes="m4_axes",
               axis="M4 集体文学运动与文化政治", expected=90),
    "M5.1": dict(priority="m51_priority", cluster="m51_movement_cluster",
                 history="m51_history_position", role="m51_topic_role", axes="m51_axes",
                 axis="M5.1 战后思想与美学范式", expected=80),
    "M5.2": dict(priority="m52_priority", cluster="m52_framework_cluster",
                 history="m52_history_position", role="m52_topic_role", axes="m52_axes",
                 axis="M5.2 权力、身份与世界批评", expected=74),
}

VALID_PRIORITY = {"★", "◆", "△"}
T_VALUES = {
    "T0": "T0 文学源头与古代文学", "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学", "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代", "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}
R_VALUES = {
    1: "R1 西亚—地中海古老传统", 2: "R2 东亚文学", 3: "R3 南亚文学",
    4: "R4 欧洲文学", 5: "R5 北美文学", 6: "R6 拉丁美洲与加勒比",
    7: "R7 非洲文学", 8: "R8 东南亚文学", 9: "R9 大洋洲与太平洋",
    10: "R10 跨区域文学传统",
}
G_VALUES = {
    "poetry": "G1 诗歌", "drama": "G2 戏剧", "novel": "G3 小说",
    "essay": "G4 散文与随笔", "life": "G5 生命书写",
    "nonfiction": "G6 纪实与文学非虚构",
}

M31_CONTEXT = {
    "19世纪前史": "世纪末现代主义前史与形式酝酿",
    "英国—爱尔兰现代主义": "英爱高峰现代主义与形式革新",
    "德语—奥地利—中欧现代主义": "中欧帝国危机与现代主义形成",
    "法国现代主义": "法国都市现代性与文学实验",
    "美国与Harlem Renaissance": "美国现代主义与黑人文化复兴",
    "日本与中国现代主义": "东亚现代性与新文学转型",
    "伊比利亚与意大利现代主义": "南欧现代主义与先锋互动",
    "俄罗斯与东欧现代主义": "革命、帝国解体与东欧现代主义",
    "拉丁美洲先锋与巴西Modernismo": "拉美先锋与本土现代主义形成",
    "南亚、波斯与阿拉伯现代主义": "殖民现代性与多语言文学转型",
    "殖民与跨国现代主义": "全球现代主义的跨国流动与殖民经验",
}


def unique(values: list[str]) -> list[str]:
    out = []
    for value in values:
        if value and value not in out:
            out.append(value)
    return out


def set_list(fm: str, key: str, values: list[str]) -> str:
    values = unique(values)
    block = key + ":\n" + "\n".join(f"- {h.yaml_value(v)}" for v in values)
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:\s*(?:\[.*\])?\s*$", line):
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                j += 1
            return "\n".join(lines[:i] + block.splitlines() + lines[j:])
    return fm.rstrip() + "\n" + block


def work_rows() -> list[tuple[Path, str, str]]:
    rows = []
    for path in sorted(h.WORKS.glob("*.md")):
        try:
            fm, body = h.frontmatter(path.read_text(encoding="utf-8-sig"))
        except ValueError:
            continue
        if h.scalar(fm, "type") == "work":
            rows.append((path, fm, body))
    return rows


def memberships(fm: str) -> list[str]:
    return [code for code, cfg in CFG.items()
            if h.scalar(fm, cfg["priority"]) in VALID_PRIORITY or h.scalar(fm, cfg["cluster"])]


def model_value(model: dict[str, Counter], key: str, allowed_prefix: str) -> str:
    for value, _ in model.get(key, Counter()).most_common():
        if value.startswith(allowed_prefix):
            return value
    return ""


def direct_region(topics: list[str]) -> str:
    for topic in topics:
        m = re.search(r"WL-TOPIC-R(10|[1-9])(?:-|$)", topic)
        if m:
            return R_VALUES[int(m.group(1))]
    return ""


def t_by_year(year: int | None) -> str:
    if year is None:
        return ""
    if year < 500: return T_VALUES["T0"]
    if year < 1500: return T_VALUES["T1"]
    if year < 1800: return T_VALUES["T2"]
    if year < 1890: return T_VALUES["T3"]
    if year < 1945: return T_VALUES["T4"]
    if year < 1980: return T_VALUES["T5"]
    return T_VALUES["T6"]


def infer_t(code: str, cluster: str) -> str:
    if code == "M1": return T_VALUES["T2"]
    if code == "M2": return T_VALUES["T3"]
    if code in {"M3.1", "M3.2"}: return T_VALUES["T4"]
    if code == "M5.1": return T_VALUES["T5"]
    if code == "M4":
        if cluster == "民族主义文学": return T_VALUES["T3"]
        if cluster in {"反殖民文学运动", "拉丁美洲Boom", "垮掉的一代"}: return T_VALUES["T5"]
        return T_VALUES["T4"]
    if code == "M5.2":
        if cluster in {"后殖民", "去殖民", "女性主义"}: return T_VALUES["T5"]
        return T_VALUES["T6"]
    raise KeyError(code)


def infer_r(code: str, cluster: str) -> str:
    if code == "M1": return R_VALUES[4]
    if code == "M2":
        if "拉美" in cluster: return R_VALUES[6]
        if cluster == "超验主义": return R_VALUES[5]
        return R_VALUES[4]
    if code == "M3.1":
        rules = [
            (("日本", "中国"), R_VALUES[2]), (("南亚", "波斯", "阿拉伯"), R_VALUES[3]),
            (("美国", "Harlem"), R_VALUES[5]), (("拉丁美洲", "巴西"), R_VALUES[6]),
            (("殖民", "跨国"), R_VALUES[10]),
        ]
        for words, value in rules:
            if any(word in cluster for word in words): return value
        return R_VALUES[4]
    if code == "M3.2":
        return R_VALUES[6] if any(x in cluster for x in ["伊比利亚", "拉美"]) else R_VALUES[4]
    if code == "M4":
        mapping = {
            "拉丁美洲Boom": R_VALUES[6], "哈莱姆文艺复兴": R_VALUES[5],
            "垮掉的一代": R_VALUES[5], "Négritude": R_VALUES[10],
            "反殖民文学运动": R_VALUES[10],
        }
        return mapping.get(cluster, R_VALUES[10])
    if code == "M5.1":
        return R_VALUES[6] if cluster == "魔幻现实主义" else R_VALUES[4]
    return R_VALUES[10]


def infer_genre(title: str, mechanisms: list[str], author: str,
                author_g: dict[str, Counter], topics: list[str], topic_g: dict[str, Counter]) -> tuple[str, str]:
    text = " ".join([title, *mechanisms])
    rules = [
        (r"戏剧|剧本|悲剧|喜剧|剧场", G_VALUES["drama"], "title_or_tag"),
        (r"诗集|诗选|诗歌|长诗|十四行诗|声音诗|视觉诗|诗学|诗篇", G_VALUES["poetry"], "title_or_tag"),
        (r"自传|回忆录|日记|书信|传记", G_VALUES["life"], "title_or_tag"),
        (r"纪实|报告文学|事实文学|文献|访谈", G_VALUES["nonfiction"], "title_or_tag"),
        (r"宣言|理论|批评|评论|随笔|散文|文集|纲领|论文|讲演", G_VALUES["essay"], "title_or_tag"),
        (r"小说|叙事|元小说", G_VALUES["novel"], "title_or_tag"),
    ]
    for pattern, value, source in rules:
        if re.search(pattern, text): return value, source
    for topic in topics:
        if "WL-TOPIC-G" in topic:
            value = model_value(topic_g, topic, "G")
            if value in G_VALUES.values(): return value, "genre_topic_model"
    value = model_value(author_g, author, "G")
    if value in G_VALUES.values(): return value, "author_model"
    return G_VALUES["novel"], "conservative_default"


def infer_q(code: str, cluster: str, title: str, mechanisms: list[str],
            topics: list[str], topic_q: dict[str, Counter]) -> tuple[list[str], str]:
    for topic in topics:
        if "WL-TOPIC-Q" in topic:
            values = [v for v, _ in topic_q.get(topic, Counter()).most_common(2) if v.startswith("Q")]
            if values: return values, "q_topic_model"
    text = " ".join([cluster, title, *mechanisms])
    rules = [
        (r"战争|暴力|创伤|大屠杀|灾难", "QH6 战争、暴力与创伤"),
        (r"记忆|历史|时间|档案|过去", "QH7 历史、记忆与时间"),
        (r"性别|女性|酷儿|同性|种族|身份|身体|离散|殖民", "QH3 身份、身体与归属"),
        (r"阶级|劳动|贫困|工业|社会|群众|共同体", "QH4 社会、阶级与劳动"),
        (r"权力|制度|国家|革命|帝国|政治|规训|正义", "QH5 权力、制度与秩序"),
        (r"宗教|信仰|伦理|救赎|超越|生态|环境|自然", "QH8 信仰、伦理与超越"),
        (r"爱情|欲望|情欲", "QH2.1 爱情与欲望"),
        (r"家庭|家族|母职|父职", "QH2.3 家庭与家族"),
        (r"童年|成长|教育", "QH2.5 童年与成长"),
        (r"主体|存在|心理|意识|语言|自由|荒诞|梦", "QH1 自我、存在与生命"),
    ]
    values = unique([value for pattern, value in rules if re.search(pattern, text)])[:2]
    if values: return values, "topic_tags"
    fallback = {
        "M1": "QH5 权力、制度与秩序", "M2": "QH4 社会、阶级与劳动",
        "M3.1": "QH1 自我、存在与生命", "M3.2": "QH1 自我、存在与生命",
        "M4": "QH4 社会、阶级与劳动", "M5.1": "QH1 自我、存在与生命",
        "M5.2": "QH3 身份、身体与归属",
    }
    return [fallback[code]], "topic_default"


def infer_role(priority: str, mechanisms: list[str], cross_topic: bool) -> tuple[str, str]:
    text = " ".join(mechanisms)
    rules = [
        ("理论阐释与范式建构", ["理论", "宣言", "批评", "诗学", "纲领", "文论", "概念"]),
        ("文学动员与共同体建构", ["运动", "革命", "集体", "组织", "群众", "共同体", "民族"]),
        ("传播扩散与跨地域连接", ["传播", "翻译", "杂志", "出版", "流亡", "网络", "跨国", "跨大西洋"]),
        ("批判反拨与范式转型", ["解构", "反艺术", "反拨", "颠覆", "反思", "批判", "否定"]),
    ]
    for role, words in rules:
        if any(word in text for word in words): return role, "mechanism_tag"
    if cross_topic: return "跨专题连接与范式转译", "cross_membership"
    if priority == "★": return "核心典范与形式确立", "priority_core"
    if priority == "◆": return "专题扩展与变体生成", "priority_focus"
    return "延伸阅读与影响观察", "priority_expand"


def genealogy_context(code: str, cluster: str, old: str) -> str:
    if code == "M3.1" and cluster in M31_CONTEXT:
        return M31_CONTEXT[cluster]
    context = old.split(" · ", 1)[0].strip()
    return context or cluster


def genealogy_value(context: str, role: str) -> str:
    suffix = {
        "理论阐释与范式建构": "理论化与范式确立",
        "文学动员与共同体建构": "组织化与集体扩展",
        "传播扩散与跨地域连接": "传播扩散与跨地域转译",
        "批判反拨与范式转型": "反拨、转型与再阐释",
        "跨专题连接与范式转译": "跨专题连接与转型",
        "核心典范与形式确立": "核心形成与典范确立",
        "专题扩展与变体生成": "扩展、变体与后续发展",
        "延伸阅读与影响观察": "影响延伸与历史遗产",
    }[role]
    return f"{context} · {suffix}"


def build_models(rows: list[tuple[Path, str, str]]):
    author_r, author_g = defaultdict(Counter), defaultdict(Counter)
    topic_g, topic_q = defaultdict(Counter), defaultdict(Counter)
    for _, fm, _ in rows:
        author = h.scalar(fm, "author")
        author_r[author].update(unique(h.list_field(fm, "axis_r")))
        author_g[author].update(unique(h.list_field(fm, "axis_g")))
        for topic in h.list_field(fm, "topics"):
            topic_g[topic].update(unique(h.list_field(fm, "axis_g")))
            topic_q[topic].update(unique(h.list_field(fm, "axis_q")))
    return author_r, author_g, topic_g, topic_q


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    rows = work_rows()
    author_r, author_g, topic_g, topic_q = build_models(rows)
    changed, details, stats = set(), [], Counter()
    frozen = Counter()

    for path, fm, body in rows:
        member_codes = memberships(fm)
        if not member_codes:
            continue
        fm2 = fm
        topics = h.list_field(fm2, "topics")
        author = h.scalar(fm2, "author")
        title = h.scalar(fm2, "title") or path.stem
        all_mechanisms = unique([value for code in member_codes for value in h.list_field(fm2, CFG[code]["axes"])])
        cross_topic = len(member_codes) > 1

        for code in member_codes:
            cfg = CFG[code]
            frozen[code] += 1
            priority = h.scalar(fm2, cfg["priority"])
            if priority not in VALID_PRIORITY:
                priority = "◆"
                fm2 = h.upsert_scalar(fm2, cfg["priority"], priority, cfg["cluster"])
                stats["priority_auto"] += 1
            cluster = h.scalar(fm2, cfg["cluster"])
            mechanisms = h.list_field(fm2, cfg["axes"])
            role, role_source = infer_role(priority, mechanisms, cross_topic)
            old_history = h.scalar(fm2, cfg["history"])
            genealogy = genealogy_value(genealogy_context(code, cluster, old_history), role)
            fm2 = h.upsert_scalar(fm2, cfg["history"], genealogy, cfg["axes"])
            fm2 = h.upsert_scalar(fm2, cfg["role"], role, cfg["axes"])
            stats[f"role:{role_source}"] += 1
            details.append({
                "work": path.name, "id": h.scalar(fm2, "id"), "topic": code,
                "priority": priority, "topic_affiliation": cluster,
                "genealogy_position": genealogy, "topic_role": role,
                "role_source": role_source,
            })

        axis_m = unique(h.list_field(fm2, "axis_m") + [CFG[code]["axis"] for code in member_codes])
        fm2 = set_list(fm2, "axis_m", axis_m)

        if not h.list_field(fm2, "axis_t"):
            year_value = t_by_year(h.numeric_year(fm2))
            candidates = [year_value] if year_value else [infer_t(code, h.scalar(fm2, CFG[code]["cluster"])) for code in member_codes]
            axis_t = Counter(candidates).most_common(1)[0][0]
            fm2 = set_list(fm2, "axis_t", [axis_t])
            stats["axis_t_auto"] += 1
        else:
            fm2 = set_list(fm2, "axis_t", h.list_field(fm2, "axis_t"))

        if not h.list_field(fm2, "axis_r"):
            region = direct_region(topics)
            source = "region_topic"
            if not region:
                region = model_value(author_r, author, "R")
                source = "author_model"
            if not region:
                region = infer_r(member_codes[0], h.scalar(fm2, CFG[member_codes[0]]["cluster"]))
                source = "topic_default"
            fm2 = set_list(fm2, "axis_r", [region])
            stats[f"axis_r:{source}"] += 1
        else:
            fm2 = set_list(fm2, "axis_r", h.list_field(fm2, "axis_r"))

        if not h.list_field(fm2, "axis_g"):
            genre, source = infer_genre(title, all_mechanisms, author, author_g, topics, topic_g)
            fm2 = set_list(fm2, "axis_g", [genre])
            stats[f"axis_g:{source}"] += 1
        else:
            existing_g = [G_VALUES["drama"] if value == "G5 戏剧" else value
                          for value in h.list_field(fm2, "axis_g")]
            fm2 = set_list(fm2, "axis_g", existing_g)

        if not h.list_field(fm2, "axis_q"):
            code = member_codes[0]
            q_values, source = infer_q(code, h.scalar(fm2, CFG[code]["cluster"]), title,
                                       all_mechanisms, topics, topic_q)
            fm2 = set_list(fm2, "axis_q", q_values)
            stats[f"axis_q:{source}"] += 1
        else:
            fm2 = set_list(fm2, "axis_q", h.list_field(fm2, "axis_q"))

        if fm2 != fm:
            path.write_text("---\n" + fm2 + "\n---\n" + body.lstrip("\n"), encoding="utf-8", newline="\n")
            changed.add(path)

    failures = []
    rows2 = work_rows()
    for path, fm, _ in rows2:
        member_codes = memberships(fm)
        if not member_codes:
            continue
        for axis in ["axis_t", "axis_r", "axis_m", "axis_g", "axis_q"]:
            if not h.list_field(fm, axis): failures.append(f"{path.name}:{axis}")
        for code in member_codes:
            cfg = CFG[code]
            for field in [cfg["priority"], cfg["cluster"], cfg["history"], cfg["role"]]:
                if not h.scalar(fm, field): failures.append(f"{path.name}:{field}")
    for code, cfg in CFG.items():
        if frozen[code] != cfg["expected"]:
            failures.append(f"{code}:membership={frozen[code]} expected={cfg['expected']}")
    if failures:
        raise SystemExit(f"postcondition failures={failures[:30]} total={len(failures)}")

    if not changed and REPORT.exists() and DETAIL.exists():
        print("CHANGED_FILES=0")
        print(f"MEMBERSHIPS={len(details)}")
        print("FAILURES=0")
        return

    with DETAIL.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(details[0]))
        writer.writeheader()
        writer.writerows(details)

    lines = [
        "# M轴文学作品读前预填 V1", "",
        f"- 专题成员关系：**{len(details)}**",
        f"- 唯一作品文件：**{len({row['work'] for row in details})}**",
        f"- 本次修改文件：**{len(changed)}**",
        "- 原有非空五轴坐标不覆盖；仅补空值并去除完全重复项。", "",
        "## 专题覆盖", "", "| 专题 | 数量 |", "|---|---:|",
    ]
    for code in CFG:
        lines.append(f"| {code} | {frozen[code]} |")
    lines += ["", "## 自动补值", ""]
    for key, value in sorted(stats.items()):
        lines.append(f"- `{key}`：{value}")
    lines += [
        "", "## 校准说明", "",
        "1. 谱系位置由专题历史语境与作品角色组合生成。",
        "2. 专题角色优先依据原专题标签，其次依据跨专题关系与优先级。",
        "3. 缺失五轴依次使用年代、专题、作者模型、标题及原专题标签推断。",
        "4. 逐项结果见 `M_AXIS_READING_PREFILL_V1.csv`。", "",
        "`M_AXIS_READING_PREFILL_V1 = APPLIED_AND_VERIFIED`", "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"CHANGED_FILES={len(changed)}")
    print(f"UNIQUE_WORKS={len({row['work'] for row in details})}")
    print(f"MEMBERSHIPS={len(details)}")
    print("FAILURES=0")


if __name__ == "__main__":
    main()
