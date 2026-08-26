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

AUDIT = h.WORLD / "_audit" / "t_axis"
REPORT = AUDIT / "FIVE_AXIS_PRIORITY_PREFILL_V1.md"
DETAIL = AUDIT / "FIVE_AXIS_PRIORITY_PREFILL_V1.csv"

R_VALUES = {
    1: "R1 西亚—地中海古老传统", 2: "R2 东亚文学", 3: "R3 南亚文学",
    4: "R4 欧洲文学", 5: "R5 北美文学", 6: "R6 拉丁美洲与加勒比",
    7: "R7 非洲文学", 8: "R8 东南亚文学", 9: "R9 大洋洲与太平洋",
    10: "R10 跨区域文学传统",
}
G_VALUES = {
    "poetry": "G1 诗歌", "drama": "G2 戏剧", "novel": "G3 小说",
    "essay": "G4 散文与随笔", "life": "G5 生命书写", "nonfiction": "G6 纪实与文学非虚构",
}
M_FALLBACK = {
    "T2": "M1 早期现代思想与美学", "T3": "M2 19世纪文学思潮",
    "T4": "M3 现代主义与先锋派", "T5": "M5 战后与当代美学范式",
    "T6": "M5 战后与当代美学范式",
}
R_FALLBACK = {"T0": R_VALUES[1], "T1": R_VALUES[4], "T2": R_VALUES[4],
              "T3": R_VALUES[4], "T4": R_VALUES[4], "T5": R_VALUES[5], "T6": R_VALUES[5]}
Q_FALLBACK = {
    "T0": "QH8 信仰、伦理与超越", "T1": "QH8 信仰、伦理与超越",
    "T2": "QH5 权力、制度与秩序", "T3": "QH4 社会、阶级与劳动",
    "T4": "QH1 自我、存在与生命", "T5": "QH6 战争、暴力与创伤",
    "T6": "QH3 身份、身体与归属",
}
Q_DIRECT = [
    (re.compile(r"CRIME|MYSTERY|DETECT", re.I), "QT1 推理与犯罪叙事"),
    (re.compile(r"(?:^|-)SF(?:-|$)|SCIENCE", re.I), "QT2 科幻"),
    (re.compile(r"FANTASY", re.I), "QT3 奇幻"),
    (re.compile(r"HORROR|GOTHIC", re.I), "QT4 恐怖与哥特"),
    (re.compile(r"DYSTOP|UTOP", re.I), "QT6 乌托邦、反乌托邦与社会想象"),
    (re.compile(r"HISTOR", re.I), "QT7 历史叙事"),
    (re.compile(r"MYTH|FOLK|FAIRY", re.I), "QT9 神话、传说与民间叙事"),
    (re.compile(r"THRILL", re.I), "QT10 惊悚与悬疑叙事"),
    (re.compile(r"LOVE|ROMANCE", re.I), "QT11 爱情与浪漫叙事"),
    (re.compile(r"APOCAL|DISASTER", re.I), "QT12 灾变、末世与后末日叙事"),
    (re.compile(r"SATIR", re.I), "QT13 讽刺叙事"),
    (re.compile(r"TRAVEL", re.I), "QT14 旅行与游记"),
    (re.compile(r"FAMILY", re.I), "QH2.3 家庭与家族"),
    (re.compile(r"BILDUNGS|GROWTH", re.I), "QH2.5 童年与成长"),
    (re.compile(r"MEMORY", re.I), "QH7 历史、记忆与时间"),
    (re.compile(r"WAR|TRAUMA", re.I), "QH6 战争、暴力与创伤"),
]


def valid_q(value: str) -> bool:
    code = value.split(" ", 1)[0]
    if re.fullmatch(r"QH[1-3](?:\.\d+)?", code): return True
    if re.fullmatch(r"QH[4-8]", code): return True
    if re.fullmatch(r"QT(?:[1-9]|1[0-4])", code): return True
    if re.fullmatch(r"QT8\.\d+", code): return True
    return False


def work_rows():
    rows = []
    for path in sorted(h.WORKS.glob("*.md")):
        try: fm, body = h.frontmatter(path.read_text(encoding="utf-8-sig"))
        except ValueError: continue
        if h.scalar(fm, "type") == "work": rows.append((path, fm, body))
    return rows


def build_models(rows):
    topic_model = {axis: defaultdict(Counter) for axis in ["axis_r", "axis_m", "axis_g", "axis_q"]}
    author_r = defaultdict(Counter)
    for _, fm, _ in rows:
        topics = h.list_field(fm, "topics")
        for axis in topic_model:
            for topic in topics:
                topic_model[axis][topic].update(h.list_field(fm, axis))
        author = h.scalar(fm, "author")
        if author: author_r[author].update(h.list_field(fm, "axis_r"))
    return topic_model, author_r


def direct_r(topics: list[str]) -> str:
    for topic in topics:
        m = re.search(r"WL-TOPIC-R(10|[1-9])(?:-|$)", topic)
        if m: return R_VALUES[int(m.group(1))]
    return ""


def direct_m(topics: list[str]) -> str:
    joined = " ".join(topics).upper()
    rules = [
        ("M5.2", "M5.2 权力、身份与世界批评"),
        ("M5.1", "M5.1 战后思想与美学范式"),
        ("M3.2", "M3.2 先锋派"), ("M3-MODERNISM", "M3.1 现代主义 / Modernism"),
        ("M3.1", "M3.1 现代主义 / Modernism"),
        ("M4", "M4 集体文学运动与文化政治"),
        ("M2", "M2 19世纪文学思潮"),
        ("M1", "M1 早期现代思想与美学"),
    ]
    for needle, value in rules:
        if needle in joined: return value
    return ""


def model_pick(model, topics: list[str], allowed=None) -> str:
    scores = Counter()
    for topic in topics:
        for value, count in model.get(topic, {}).items():
            if allowed is None or value in allowed: scores[value] += count
    return scores.most_common(1)[0][0] if scores else ""


def infer_g(title: str, topics: list[str], model) -> tuple[str, str]:
    picked = model_pick(model, [x for x in topics if "WL-TOPIC-G" in x], set(G_VALUES.values()))
    if picked: return picked, "topic_model"
    if re.search(r"诗集|诗选|诗歌|长诗|十四行诗|叙事诗", title): return G_VALUES["poetry"], "title"
    if re.search(r"戏剧|剧本|悲剧|喜剧", title): return G_VALUES["drama"], "title"
    if re.search(r"自传|回忆录|日记|传记|书信", title): return G_VALUES["life"], "title"
    if re.search(r"随笔|散文|文集|评论", title): return G_VALUES["essay"], "title"
    if re.search(r"游记|纪实|报告文学|访谈", title): return G_VALUES["nonfiction"], "title"
    return G_VALUES["novel"], "t_default"


def infer_q(fm: str, t: str, topics: list[str], model, mechanisms: list[str]) -> tuple[list[str], str]:
    direct = []
    for topic in topics:
        for pat, value in Q_DIRECT:
            if pat.search(topic) and value not in direct: direct.append(value)
    if direct: return direct[:2], "topic_direct"
    scores = Counter()
    for topic in topics:
        if "WL-TOPIC-Q" not in topic and "WL-TOPIC-G4" not in topic and "WL-TOPIC-G5" not in topic:
            continue
        for value, count in model.get(topic, {}).items():
            if valid_q(value): scores[value] += count
    if scores: return [x for x, _ in scores.most_common(2)], "topic_model"
    text = " ".join(mechanisms)
    rules = [
        (["神话", "传说", "民间"], "QT9 神话、传说与民间叙事"),
        (["战争", "暴力", "创伤", "冷战"], "QH6 战争、暴力与创伤"),
        (["记忆", "历史重写"], "QH7 历史、记忆与时间"),
        (["身份", "性别", "离散", "迁徙"], "QH3 身份、身体与归属"),
        (["宗教", "信仰", "仪式"], "QH8 信仰、伦理与超越"),
        (["阶级", "工业城市", "劳动"], "QH4 社会、阶级与劳动"),
        (["帝国", "殖民", "制度", "秩序"], "QH5 权力、制度与秩序"),
        (["心理", "主体", "感知"], "QH1 自我、存在与生命"),
    ]
    for needles, value in rules:
        if any(x in text for x in needles): return [value], "mechanism"
    return [Q_FALLBACK[t]], "t_default"


def infer_priority(fm: str, current_key: str) -> tuple[str, str]:
    if h.scalar(fm, "canon_level").lower() == "core": return "★", "canon_core"
    if h.scalar(fm, "canon_id"): return "◆", "canon"
    if h.list_field(fm, "awards"): return "◆", "award"
    other = []
    for key, value in re.findall(r"(?m)^([A-Za-z0-9_.]+_priority):\s*[\"']?(★|◆|△)[\"']?\s*$", fm):
        if key != current_key: other.append(value)
    if "★" in other or "◆" in other: return "◆", "other_topic"
    return "△", "conservative_default"


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    rows = work_rows()
    topic_model, author_r = build_models(rows)
    stats = defaultdict(Counter)
    details, changed = [], set()

    for path, fm, body in rows:
        memberships = [t for t, cfg in h.CFG.items() if cfg["label"] in h.list_field(fm, "axis_t")]
        if not memberships: continue
        fm2 = fm
        t = memberships[0]
        topics = h.list_field(fm2, "topics")
        mechanisms = h.list_field(fm2, h.CFG[t]["mechanism"])
        sources = {"axis_t": "existing"}

        if not h.list_field(fm2, "axis_r"):
            value = direct_r(topics)
            source = "topic_direct" if value else ""
            if not value:
                author = h.scalar(fm2, "author")
                if author and author_r[author]: value, source = author_r[author].most_common(1)[0][0], "author_model"
            if not value: value, source = R_FALLBACK[t], "t_default"
            fm2 = h.upsert_list(fm2, "axis_r", [value]); sources["axis_r"] = source
        else: sources["axis_r"] = "existing"

        if not h.list_field(fm2, "axis_m"):
            if t in {"T0", "T1"}:
                sources["axis_m"] = "not_applicable_pre_modern"
            else:
                value = direct_m(topics)
                source = "topic_direct" if value else ""
                if not value:
                    value = model_pick(topic_model["axis_m"], [x for x in topics if "WL-TOPIC-M" in x])
                    source = "topic_model" if value else ""
                if not value: value, source = M_FALLBACK[t], "t_default"
                fm2 = h.upsert_list(fm2, "axis_m", [value]); sources["axis_m"] = source
        else: sources["axis_m"] = "existing"

        if not h.list_field(fm2, "axis_g"):
            value, source = infer_g(h.scalar(fm2, "title") or path.stem, topics, topic_model["axis_g"])
            fm2 = h.upsert_list(fm2, "axis_g", [value]); sources["axis_g"] = source
        else: sources["axis_g"] = "existing"

        if not h.list_field(fm2, "axis_q"):
            values, source = infer_q(fm2, t, topics, topic_model["axis_q"], mechanisms)
            fm2 = h.upsert_list(fm2, "axis_q", values); sources["axis_q"] = source
        else: sources["axis_q"] = "existing"

        priority_key = h.CFG[t]["priority"]
        if not h.scalar(fm2, priority_key):
            value, source = infer_priority(fm2, priority_key)
            fm2 = h.upsert_scalar(fm2, priority_key, value, h.CFG[t]["history"])
            sources["priority"] = source
        else: sources["priority"] = "existing"

        for field, source in sources.items(): stats[t][f"{field}:{source}"] += 1
        details.append({"work": path.name, "id": h.scalar(fm2, "id"), "t": t,
                        "axis_t": " | ".join(h.list_field(fm2, "axis_t")),
                        "axis_r": " | ".join(h.list_field(fm2, "axis_r")),
                        "axis_m": " | ".join(h.list_field(fm2, "axis_m")),
                        "axis_g": " | ".join(h.list_field(fm2, "axis_g")),
                        "axis_q": " | ".join(h.list_field(fm2, "axis_q")),
                        "priority": h.scalar(fm2, priority_key), **{f"{k}_source": v for k, v in sources.items()}})
        if fm2 != fm:
            path.write_text("---\n" + fm2 + "\n---\n" + body.lstrip("\n"), encoding="utf-8", newline="\n")
            changed.add(path)

    failures = []
    for path, fm, _ in work_rows():
        memberships = [t for t, cfg in h.CFG.items() if cfg["label"] in h.list_field(fm, "axis_t")]
        if not memberships: continue
        t = memberships[0]
        for axis in ["axis_t", "axis_r", "axis_g", "axis_q"]:
            if not h.list_field(fm, axis): failures.append((path.name, axis))
        if t not in {"T0", "T1"} and not h.list_field(fm, "axis_m"): failures.append((path.name, "axis_m"))
        if not h.scalar(fm, h.CFG[t]["priority"]): failures.append((path.name, "priority"))
    if failures: raise SystemExit(f"postcondition failures={failures[:20]} total={len(failures)}")

    # An idempotency verification run must not erase the provenance captured by
    # the initial mutating run.
    if not changed and REPORT.exists() and DETAIL.exists():
        print("CHANGED_FILES=0"); print(f"WORKS={len(details)}"); print("FAILURES=0")
        return

    with DETAIL.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(details[0])); writer.writeheader(); writer.writerows(details)
    lines = ["# 五轴坐标与 T专题优先级读前预填 V1", "",
             f"- T轴作品：**{len(details)}**", f"- 本次修改文件：**{len(changed)}**",
             "- T0/T1 的 M轴按现行 taxonomy 记为不适用；未创建伪 M0，也未强制归入 M1。", "",
             "## 自动补值来源", "",
             "| T | R auto | M auto | M N/A | G auto | Q auto | priority auto |", "|---|---:|---:|---:|---:|---:|---:|"]
    for t in h.CFG:
        s = stats[t]
        auto = lambda field: sum(v for k, v in s.items() if k.startswith(field + ":") and not k.endswith(":existing") and "not_applicable" not in k)
        lines.append(f"| {t} | {auto('axis_r')} | {auto('axis_m')} | {s['axis_m:not_applicable_pre_modern']} | {auto('axis_g')} | {auto('axis_q')} | {auto('priority')} |")
    lines += ["", "## 校准优先级", "",
              "1. `*_source=t_default` 是时代众数回退，最先复核。",
              "2. `topic_model` 和 `author_model` 是基于已有坐标的读前推断。",
              "3. `existing` 值本次未改写，不代表已经读后确认。",
              "4. 逐作品值与来源见 `FIVE_AXIS_PRIORITY_PREFILL_V1.csv`。", "",
              "`FIVE_AXIS_PRIORITY_PREFILL_V1 = APPLIED_AND_VERIFIED`", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"CHANGED_FILES={len(changed)}"); print(f"WORKS={len(details)}"); print(f"FAILURES={len(failures)}")


if __name__ == "__main__": main()
