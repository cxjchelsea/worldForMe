from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORLD = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = WORLD / "40 作品"
TOPICS = WORLD / "30 专题"
AUDIT = WORLD / "_audit" / "r_axis"
REPORT = AUDIT / "R_AXIS_READING_PREFILL_V1.md"
DETAIL = AUDIT / "R_AXIS_READING_PREFILL_V1.csv"

CFG = {
    "R1": ("R1 西亚—地中海古老传统", "西亚—地中海综合—具体内部传统待读后校准"),
    "R2": ("R2 东亚文学", "东亚文学综合—具体内部传统待读后校准"),
    "R3": ("R3 南亚文学", "南亚文学综合—具体内部传统待读后校准"),
    "R4": ("R4 欧洲文学", "欧洲文学综合—具体内部传统待读后校准"),
    "R5": ("R5 北美文学", "北美文学综合—具体内部传统待读后校准"),
    "R6": ("R6 拉丁美洲与加勒比", "拉丁美洲与加勒比综合—具体内部传统待读后校准"),
    "R7": ("R7 非洲文学", "非洲文学综合—具体内部传统待读后校准"),
    "R8": ("R8 东南亚文学", "东南亚文学综合—具体内部传统待读后校准"),
    "R9": ("R9 大洋洲与太平洋", "大洋洲与太平洋综合—具体内部传统待读后校准"),
    "R10": ("R10 跨区域文学传统", "跨区域综合—具体传统待读后校准"),
}

T_VALUES = {
    "T0": "T0 文学源头与古代文学", "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学", "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代", "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}

REGION_PROCESS = {
    "R1": {"T0": "古代文字、史诗与经典传统形成", "T1": "宗教经典、帝国网络与翻译传承", "T2": "手稿—印刷转换与多语传统延续", "T3": "现代文类输入与民族文学转型", "T4": "帝国危机、现代主义与语言革新", "T5": "战后国家建构、流亡与现代转型", "T6": "当代冲突、迁徙与全球传播"},
    "R2": {"T0": "古代经典、史传与诗歌传统奠基", "T1": "宗教传播、宫廷文化与区域交流", "T2": "印刷扩展、通俗文类与文人传统成熟", "T3": "晚期传统、翻译输入与现代转折", "T4": "殖民现代性、新文学与形式实验", "T5": "战争革命、国家文学与社会重构", "T6": "都市经验、媒介转型与跨国传播"},
    "R3": {"T0": "吠陀、史诗与古典语言传统奠基", "T1": "宗教、宫廷与多语文学网络扩展", "T2": "波斯语—地方语互动与早期印刷转型", "T3": "殖民教育、语言公共领域与民族文学形成", "T4": "反殖民、现代主义与多语文学革新", "T5": "独立分治、国家文学与离散书写", "T6": "全球南亚、英语写作与地方传统重组"},
    "R4": {"T0": "希腊罗马古典传统奠基", "T1": "基督教、宫廷与俗语文学形成", "T2": "文艺复兴、宗教改革与印刷公共领域", "T3": "浪漫主义、现实主义与民族文学体系", "T4": "战争危机、现代主义与先锋实验", "T5": "战后重建、记忆政治与后现代转型", "T6": "欧洲一体化、迁徙经验与当代重组"},
    "R5": {"T0": "原住民口传与古老叙事传统", "T1": "原住民传承与殖民前文化网络", "T2": "殖民定居、宗教书写与印刷起步", "T3": "国家文学、奴隶制回应与大众出版", "T4": "现代主义、哈莱姆复兴与类型扩张", "T5": "战后反文化、族裔文学与媒介繁荣", "T6": "多元身份、数字媒介与全球传播"},
    "R6": {"T0": "前哥伦布口传、神话与文字传统", "T1": "原住民文明、口传网络与早期接触", "T2": "殖民编年、巴洛克与混合文化形成", "T3": "独立建国、浪漫主义与国家文学", "T4": "Modernismo、先锋派与本土现代性", "T5": "革命经验、文学爆炸与独裁回应", "T6": "后独裁记忆、迁徙与跨国文学重组"},
    "R7": {"T0": "古代书写、神话与口传传统奠基", "T1": "口传延续、宗教传播与跨撒哈拉网络", "T2": "海洋交流、殖民接触与文字转译", "T3": "殖民教育、语言选择与早期现代文学", "T4": "反殖民意识、现代主义与民族表达", "T5": "独立、去殖民化与国家文学建构", "T6": "后殖民批判、城市经验与全球离散"},
    "R8": {"T0": "古代口传、神话与碑铭传统", "T1": "印度化、伊斯兰化与区域海洋网络", "T2": "宫廷文学、殖民接触与印刷起步", "T3": "殖民公共领域与民族语言文学形成", "T4": "民族主义、现代主义与反殖民写作", "T5": "独立战争、国家建构与政治创伤", "T6": "城市化、跨语写作与东南亚离散"},
    "R9": {"T0": "原住民口传、神话与谱系传统", "T1": "岛屿口传网络与仪式文化延续", "T2": "航海接触、传教书写与殖民记录", "T3": "定居殖民、民族文学与原住民回应", "T4": "战争经验、现代主义与区域认同", "T5": "去殖民化、原住民复兴与太平洋意识", "T6": "生态危机、移民社会与跨太平洋传播"},
    "R10": {"T0": "古代跨区域叙事母题与经典流动", "T1": "宗教、商路与翻译网络中的文本迁移", "T2": "印刷、帝国与海洋网络扩展", "T3": "世界市场、殖民体系与跨国文类形成", "T4": "流亡、现代主义与国际文学网络", "T5": "去殖民化、离散共同体与世界文学重组", "T6": "全球迁徙、数字传播与跨语文学网络"},
}

G = {"poetry": "G1 诗歌", "drama": "G2 戏剧", "novel": "G3 小说", "essay": "G4 散文与随笔", "life": "G5 生命书写", "nonfiction": "G6 纪实与文学非虚构"}
VALID_PRIORITY = {"★", "◆", "△"}


def frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)(.*)$", text, re.S)
    if not m:
        raise ValueError("missing frontmatter")
    return m.group(1), m.group(2)


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", fm)
    if not m:
        return ""
    value = m.group(1).strip().strip("\"'")
    return "" if value.lower() in {"null", "none", "~"} else value


def list_field(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        inline = re.match(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", line)
        if inline:
            return [x.strip().strip("\"'") for x in inline.group(1).split(",") if x.strip()]
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            out = []
            for nxt in lines[i + 1:]:
                m = re.match(r"^\s*-\s*(.*?)\s*$", nxt)
                if m:
                    out.append(m.group(1).strip().strip("\"'"))
                elif re.match(r"^\S.*?:", nxt):
                    break
            return out
    return []


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def upsert_scalar(fm: str, key: str, value: str, before: str) -> str:
    line = f"{key}: {q(value)}"
    pat = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    if pat.search(fm):
        return pat.sub(line, fm, count=1)
    marker = re.search(rf"(?m)^{re.escape(before)}:", fm)
    if marker:
        return fm[:marker.start()] + line + "\n" + fm[marker.start():]
    return fm.rstrip() + "\n" + line


def unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(v for v in values if v))


def set_list(fm: str, key: str, values: list[str]) -> str:
    values = unique(values)
    block = key + ":\n" + "\n".join(f"- {q(v)}" for v in values)
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:\s*(?:\[.*\]|null|~)?\s*$", line):
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                j += 1
            return "\n".join(lines[:i] + block.splitlines() + lines[j:])
    return fm.rstrip() + "\n" + block


def numeric_year(fm: str) -> int | None:
    m = re.fullmatch(r"-?\d{1,4}", scalar(fm, "year"))
    return int(m.group()) if m else None


def memberships(fm: str) -> list[str]:
    axes, topics = list_field(fm, "axis_r"), list_field(fm, "topics")
    out = [code for code in CFG if code != "R10" and CFG[code][0] in axes]
    if "WL-TOPIC-R10-TRANSREGIONAL" in topics:
        out.append("R10")
    return out


def t_from_year(year: int | None) -> str:
    if year is None: return ""
    if year < 500: return T_VALUES["T0"]
    if year < 1500: return T_VALUES["T1"]
    if year < 1800: return T_VALUES["T2"]
    if year < 1890: return T_VALUES["T3"]
    if year < 1945: return T_VALUES["T4"]
    if year < 1980: return T_VALUES["T5"]
    return T_VALUES["T6"]


def infer_t(fm: str) -> tuple[str, str]:
    by_year = t_from_year(numeric_year(fm))
    if by_year:
        return by_year, "year"
    blob = " ".join([scalar(fm, k) for k in ["knight_history_stage", "sf_history_cluster", "swashbuckler_history_stage", "fantasy_history_cluster", "war_history_stage"]])
    rules = [
        (r"古代|上古|古典|史诗|神话时代", T_VALUES["T0"]),
        (r"中古|中世纪|骑士|武士|封建", T_VALUES["T1"]),
        (r"文艺复兴|早期现代|16世纪|17世纪|18世纪", T_VALUES["T2"]),
        (r"19世纪|浪漫主义|现实主义|工业革命", T_VALUES["T3"]),
        (r"现代主义|先锋派|一战|二战|世纪之交", T_VALUES["T4"]),
        (r"战后|冷战|去殖民|文学爆炸|1960|1970", T_VALUES["T5"]),
    ]
    for pattern, value in rules:
        if re.search(pattern, blob):
            return value, "history_tag"
    return T_VALUES["T6"], "provisional_contemporary"


def t_code(axis_t: list[str]) -> str:
    for value in axis_t:
        m = re.match(r"^(T[0-6])\b", value)
        if m:
            return m.group(1)
    return "T6"


def infer_genre(blob: str) -> str:
    rules = [
        (r"戏剧|剧本|悲剧|喜剧|剧场", G["drama"]),
        (r"诗集|诗选|诗歌|长诗|十四行诗|诗学|诗篇", G["poetry"]),
        (r"自传|回忆录|日记|书信|传记", G["life"]),
        (r"纪实|报告文学|访谈|文献", G["nonfiction"]),
        (r"宣言|理论|批评|评论|随笔|散文|文集|论文|演讲", G["essay"]),
    ]
    for pattern, value in rules:
        if re.search(pattern, blob):
            return value
    return G["novel"]


def normalize_axes(values: list[str], axis: str) -> list[str]:
    replacements = {
        "G1 诗歌与韵文": G["poetry"], "G5 戏剧": G["drama"],
        "QH9 殖民、迁徙与身份": "QH3 身份、身体与归属",
    }
    out = [replacements.get(v, v) for v in values]
    return unique([v for v in out if v.startswith(axis)])


def infer_q(blob: str, cross: bool) -> list[str]:
    rules = [
        (r"战争|暴力|创伤|屠杀|灾难", "QH6 战争、暴力与创伤"),
        (r"记忆|历史|时间|档案|过去", "QH7 历史、记忆与时间"),
        (r"性别|女性|酷儿|同性|种族|身份|身体|离散|殖民|迁徙|流亡", "QH3 身份、身体与归属"),
        (r"阶级|劳动|贫困|工业|社会|群众|共同体", "QH4 社会、阶级与劳动"),
        (r"权力|制度|国家|革命|帝国|政治|规训|正义", "QH5 权力、制度与秩序"),
        (r"宗教|信仰|伦理|救赎|超越|生态|环境|自然", "QH8 信仰、伦理与超越"),
        (r"爱情|欲望|情欲", "QH2.1 爱情与欲望"),
        (r"家庭|家族|母职|父职", "QH2.3 家庭与家族"),
        (r"童年|成长|教育", "QH2.5 童年与成长"),
        (r"主体|存在|心理|意识|语言|自由|荒诞|梦", "QH1 自我、存在与生命"),
    ]
    values = unique([value for pattern, value in rules if re.search(pattern, blob)])
    return values[:2] or ["QH3 身份、身体与归属" if cross else "QH5 权力、制度与秩序"]


def infer_role(priority: str, blob: str, cross: bool, axis_r: list[str]) -> str:
    if cross or re.search(r"离散|迁徙|流亡|跨国|跨区域|难民", blob):
        return "离散迁徙与跨区域连接"
    if re.search(r"翻译|转译|译介|跨传统|传播网络", blob) or len(axis_r) > 1:
        return "翻译与跨传统连接"
    if re.search(r"文字|书写|印刷|语言|方言|媒介", blob):
        return "语言、书写与媒介转型"
    if re.search(r"殖民|反殖民|民族|独立|革命|国家建构", blob):
        return "殖民回应与民族文学建构"
    if re.search(r"史诗|经典|神话|口传|仪式|宗教", blob):
        return "源头与经典奠基"
    if re.search(r"文类|小说|诗歌|戏剧|类型|范式", blob):
        return "文类形成与区域典范"
    return {"★": "核心经典与传统确立", "◆": "传统转型与区域扩展", "△": "区域扩展阅读"}[priority]


def infer_m(t: str) -> list[str]:
    return {
        "T2": ["M1 早期现代思想与美学"],
        "T3": ["M2 19世纪文学思潮"],
        "T4": ["M3 现代主义与先锋派"],
        "T5": ["M5 战后与当代美学范式"],
        "T6": ["M5 战后与当代美学范式"],
    }.get(t, [])


def main() -> None:
    rows = []
    for path in sorted(WORKS.glob("*.md")):
        try:
            fm, body = frontmatter(path.read_text(encoding="utf-8-sig"))
        except ValueError:
            continue
        if scalar(fm, "type") == "work" and memberships(fm):
            rows.append([path, fm, body])

    author_model: dict[str, dict[str, Counter]] = defaultdict(lambda: defaultdict(Counter))
    for _, fm, _ in rows:
        author = scalar(fm, "author")
        for code in memberships(fm):
            value = scalar(fm, f"{code.lower()}_tradition")
            if author and value and "待校准" not in value:
                author_model[code][author][value] += 1

    changed = 0
    details = []
    source_counts = Counter()
    for path, original, body in rows:
        fm = original
        codes = memberships(fm)
        axes_t = normalize_axes(list_field(fm, "axis_t"), "T")
        if not axes_t:
            value, source = infer_t(fm)
            axes_t = [value]
            source_counts[f"axis_t:{source}"] += 1
        fm = set_list(fm, "axis_t", axes_t)
        tc = t_code(axes_t)

        axes_r = normalize_axes(list_field(fm, "axis_r"), "R")
        for code in codes:
            if code != "R10" and CFG[code][0] not in axes_r:
                axes_r.append(CFG[code][0])
        if "R10" in codes and not axes_r:
            axes_r.append(CFG["R10"][0])
        fm = set_list(fm, "axis_r", axes_r)

        axes_m = normalize_axes(list_field(fm, "axis_m"), "M")
        if not axes_m:
            axes_m = infer_m(tc)
            if axes_m: source_counts["axis_m:time_default"] += 1
        fm = set_list(fm, "axis_m", axes_m)

        old_role_blob = " ".join(scalar(fm, f"{c.lower()}_role") for c in codes)
        blob = " ".join([path.stem, scalar(fm, "title"), old_role_blob, " ".join(list_field(fm, "topics"))] + [scalar(fm, k) for k in ["knight_history_stage", "sf_history_cluster", "swashbuckler_history_stage", "fantasy_history_cluster", "war_history_stage"]])
        axes_g = normalize_axes(list_field(fm, "axis_g"), "G")
        if not axes_g:
            axes_g = [infer_genre(blob)]
            source_counts["axis_g:content_rule"] += 1
        fm = set_list(fm, "axis_g", axes_g)

        axes_q = normalize_axes(list_field(fm, "axis_q"), "Q")
        if not axes_q:
            axes_q = infer_q(blob, "R10" in codes)
            source_counts["axis_q:content_rule"] += 1
        fm = set_list(fm, "axis_q", axes_q)

        for code in codes:
            prefix = code.lower()
            priority = scalar(fm, f"{prefix}_priority")
            if priority not in VALID_PRIORITY:
                priority = "△"
                source_counts["priority:default"] += 1
            fm = upsert_scalar(fm, f"{prefix}_priority", priority, f"{prefix}_tradition")

            tradition = scalar(fm, f"{prefix}_tradition")
            tradition_source = "existing"
            if not tradition:
                author = scalar(fm, "author")
                choices = author_model[code].get(author, Counter())
                if choices:
                    tradition = choices.most_common(1)[0][0]
                    tradition_source = "author_model"
                else:
                    tradition = CFG[code][1]
                    tradition_source = "provisional_region"
                source_counts[f"tradition:{tradition_source}"] += 1
            fm = upsert_scalar(fm, f"{prefix}_tradition", tradition, f"{prefix}_tradition_stage")

            stage = f"{T_VALUES[tc]} · {REGION_PROCESS[code][tc]}"
            fm = upsert_scalar(fm, f"{prefix}_tradition_stage", stage, f"{prefix}_role")
            role = infer_role(priority, blob + " " + tradition, code == "R10", axes_r)
            fm = upsert_scalar(fm, f"{prefix}_role", role, "axis_t")
            details.append({"file": path.name, "code": code, "priority": priority, "tradition": tradition, "tradition_source": tradition_source, "stage": stage, "role": role, "axis_t": " | ".join(axes_t), "axis_r": " | ".join(axes_r), "axis_m": " | ".join(axes_m), "axis_g": " | ".join(axes_g), "axis_q": " | ".join(axes_q)})

        if fm != original:
            path.write_text("---\n" + fm + "\n---\n" + body, encoding="utf-8")
            changed += 1

    # Keep provisional records visible in the review view after they cease to be null.
    base_changed = 0
    for directory in sorted(TOPICS.glob("R*")):
        for base in directory.glob("*.base"):
            text = base.read_text(encoding="utf-8-sig")
            if "待传统归类" not in text:
                continue
            new = re.sub(
                r"(?m)^(\s*)and:\n\1  - (r(?:10|[1-9])_tradition) == null$",
                r'\1or:\n\1  - \2 == null\n\1  - \2.contains("待校准")', text,
            )
            if new != text:
                base.write_text(new, encoding="utf-8")
                base_changed += 1

    AUDIT.mkdir(parents=True, exist_ok=True)
    with DETAIL.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(details[0]))
        writer.writeheader(); writer.writerows(details)

    counts = Counter(d["code"] for d in details)
    provisional = Counter(d["code"] for d in details if "待校准" in d["tradition"])
    lines = ["# R 轴文学作品预填报告 V1", "", f"- 唯一作品：{len(rows)}", f"- 专题成员记录：{len(details)}", f"- 本次改写作品文件：{changed}", f"- 更新 Base 待校准视图：{base_changed}", "", "## 各专题", "", "| 专题 | 成员 | 暂定传统（待读后校准） |", "|---|---:|---:|"]
    for code in CFG:
        lines.append(f"| {code} | {counts[code]} | {provisional[code]} |")
    lines += ["", "## 推断来源", ""] + [f"- {k}: {v}" for k, v in sorted(source_counts.items())]
    lines += ["", "## 口径", "", "- 已有优先级与传统归属保留；缺失优先级暂定为 △。", "- 传统归属优先沿用同作者在本专题中的既有归属；无法可靠细分时使用带“待读后校准”的区域暂定值。", "- 传统阶段以作品的 T 轴坐标为时间骨架，并写成该区域内部的文学史过程。", "- 传统角色使用受控功能词，不沿用文类或一般性说明。", "- T0/T1 作品允许 M 轴为空；其余缺失 M 坐标按时间阶段预填。", "- 本报告为阅读前导航，不替代读后判断。", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    # Postcondition checks.
    failures = []
    for path in sorted(WORKS.glob("*.md")):
        try: fm, _ = frontmatter(path.read_text(encoding="utf-8-sig"))
        except ValueError: continue
        if scalar(fm, "type") != "work":
            continue
        for code in memberships(fm):
            p = code.lower()
            for key in [f"{p}_priority", f"{p}_tradition", f"{p}_tradition_stage", f"{p}_role"]:
                if not scalar(fm, key): failures.append(f"{path.name}:{key}")
        axes_t = list_field(fm, "axis_t")
        if memberships(fm) and (not axes_t or not list_field(fm, "axis_r") or not list_field(fm, "axis_g") or not list_field(fm, "axis_q")):
            failures.append(f"{path.name}:required_axes")
        if memberships(fm) and t_code(axes_t) not in {"T0", "T1"} and not list_field(fm, "axis_m"):
            failures.append(f"{path.name}:axis_m")
    if failures:
        raise SystemExit("POSTCHECK_FAILED\n" + "\n".join(failures[:30]))
    print(f"WORKS={len(rows)} MEMBERSHIPS={len(details)} CHANGED_FILES={changed} BASES_CHANGED={base_changed} POSTCHECK=PASS")


if __name__ == "__main__":
    main()
