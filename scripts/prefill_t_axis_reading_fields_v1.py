from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORLD = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = WORLD / "40 作品"
AUDIT = WORLD / "_audit" / "t_axis"
REPORT = AUDIT / "T_AXIS_READING_PREFILL_V1.md"
DETAIL = AUDIT / "T_AXIS_READING_PREFILL_V1.csv"

CFG = {
    "T0": dict(label="T0 文学源头与古代文学", priority="t0_priority",
               history="t0_history_position", stage="t0_stage", role="t0_historical_role",
               mechanism="t0_role", context="t0_civilization",
               fallback="文字、书写与文本固定"),
    "T1": dict(label="T1 中古多中心文学世界", priority="t1_priority",
               history="t1_history_position", stage="t1_stage", role="t1_historical_role",
               mechanism="t1_role", context="t1_network",
               fallback="手稿、书写与区域性印刷"),
    "T2": dict(label="T2 早期现代文学", priority="t2_priority",
               history="t2_history_position", stage="t2_stage", role="t2_historical_role",
               mechanism="t2_mechanism", context="",
               fallback="印刷、书籍市场与读者扩大"),
    "T3": dict(label="T3 19世纪现代文学体系", priority="t3_priority",
               history="t3_history_position", stage="t3_stage", role="t3_historical_role",
               mechanism="t3_mechanism", context="",
               fallback="职业作者、版权与文学市场"),
    "T4": dict(label="T4 全球现代主义时代", priority="t4_priority",
               history="t4_history_position", stage="t4_stage", role="t4_historical_role",
               mechanism="t4_mechanism", context="",
               fallback="小杂志、翻译、流亡与跨国网络"),
    "T5": dict(label="T5 二战后多极文学", priority="postwar_priority",
               history="postwar_history_position", stage="postwar_stage", role="postwar_historical_role",
               mechanism="postwar_axes", context="",
               fallback="从欧洲中心到多中心世界文学"),
    "T6": dict(label="T6 当代全球文学", priority="t6_priority",
               history="t6_history_position", stage="t6_stage", role="t6_historical_role",
               mechanism="t6_mechanism", context="",
               fallback="全球市场、翻译与奖项"),
}

STAGES = {
    "T0": [
        "早期文明：口传、仪式与文字形成",
        "古典形成：史诗、经典与公共文学成熟",
        "帝国与经典化：传统整合及中古过渡",
    ],
    "T1": [
        "约500—1000：传统保存与多中心网络形成",
        "约1000—1250：宫廷、宗教与俗语文学扩展",
        "约1250—1500：跨区域传播、印刷与中古晚期转型",
    ],
    "T2": [
        "1500—1600：印刷扩张、宗教变革与俗语文学兴起",
        "1600—1700：宫廷、城市、巴洛克与全球接触",
        "1700—1800：公共领域、启蒙与现代文学市场成熟",
    ],
    "T3": [
        "1800—1830：革命余波、浪漫主义与民族文学兴起",
        "1830—1870：市场扩张、现实主义与现代小说成熟",
        "1870—1890：工业社会深化与世纪末转型",
    ],
    "T4": [
        "1890—1914：世纪末危机与现代主义酝酿",
        "1914—1918：战争断裂与先锋化",
        "1918—1930：高峰现代主义与全球扩展",
        "1930—1945：政治极化、反殖民与战时转型",
    ],
    "T5": [
        "1945—1955：废墟、罪责与重新开始",
        "1955—1965：世界真正多中心化",
        "1965—1975：文学爆炸与全球分叉",
        "1975—1980：革命激情退潮与后现代成熟",
    ],
    "T6": [
        "1980—1991：冷战晚期与全球文学重组",
        "1991—2008：全球化出版与离散写作扩张",
        "2008—2020：全球危机、平台化与类型融合",
        "2020—至今：疫情、气候与技术社会",
    ],
}

HISTORICAL_ROLES = {
    "奠基", "转折", "成熟", "高峰", "扩散", "反拨", "过渡", "遗产",
    "经典化", "形式突破", "边缘突破", "跨区域转译", "阶段性代表",
}


def frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)(.*)$", text, re.S)
    if not m:
        raise ValueError("missing frontmatter")
    return m.group(1), m.group(2)


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", fm)
    if not m:
        return ""
    value = m.group(1).strip().strip('"\'')
    return "" if value.lower() in {"null", "none", "~"} else value


def list_field(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        inline = re.match(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", line)
        if inline:
            return [x.strip().strip('"\'') for x in inline.group(1).split(",") if x.strip()]
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            out = []
            for nxt in lines[i + 1:]:
                m = re.match(r"^\s*-\s*(.*?)\s*$", nxt)
                if m:
                    out.append(m.group(1).strip().strip('"\''))
                elif re.match(r"^\S.*?:", nxt):
                    break
            return out
    return []


def yaml_value(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def upsert_scalar(fm: str, key: str, value: str, before: str) -> str:
    line = f"{key}: {yaml_value(value)}"
    pat = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    if pat.search(fm):
        return pat.sub(line, fm, count=1)
    marker = re.search(rf"(?m)^{re.escape(before)}:", fm)
    if marker:
        return fm[:marker.start()] + line + "\n" + fm[marker.start():]
    return fm.rstrip() + "\n" + line


def upsert_list(fm: str, key: str, values: list[str]) -> str:
    if list_field(fm, key):
        return fm
    block = key + ":\n" + "\n".join(f"- {yaml_value(v)}" for v in values)
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:\s*(?:\[\s*\])?\s*$", line):
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                j += 1
            return "\n".join(lines[:i] + block.splitlines() + lines[j:])
    return fm.rstrip() + "\n" + block


def numeric_year(fm: str) -> int | None:
    raw = scalar(fm, "year")
    m = re.fullmatch(r"-?\d{1,4}", raw)
    return int(raw) if m else None


def stage_by_year(t: str, year: int) -> str | None:
    limits = {
        "T1": [(1000, 0), (1250, 1), (1501, 2)],
        "T2": [(1600, 0), (1700, 1), (1801, 2)],
        "T3": [(1830, 0), (1870, 1), (1891, 2)],
        "T4": [(1914, 0), (1918, 1), (1930, 2), (1946, 3)],
        "T5": [(1955, 0), (1965, 1), (1975, 2), (1981, 3)],
        "T6": [(1991, 0), (2008, 1), (2020, 2), (9999, 3)],
    }
    for upper, index in limits.get(t, []):
        if year < upper:
            return STAGES[t][index]
    return None


def infer_stage(t: str, fm: str, old_history: str, mechanisms: list[str]) -> tuple[str, str]:
    existing = scalar(fm, CFG[t]["stage"])
    if existing in STAGES[t]:
        return existing, "existing"
    year = numeric_year(fm)
    if year is not None:
        by_year = stage_by_year(t, year)
        if by_year:
            return by_year, "year"
    blob = " ".join([old_history, *mechanisms])
    if t == "T0":
        context = scalar(fm, CFG[t]["context"])
        if any(x in context for x in ["两河", "埃及", "口传传统"]):
            return STAGES[t][0], "context"
        if "罗马" in context or "经典化" in blob:
            return STAGES[t][2], "context"
        return STAGES[t][1], "context"
    if t == "T1":
        if "保存与再经典化" in blob:
            return STAGES[t][0], "keyword"
        if "印刷" in blob or "旅行文学" in blob:
            return STAGES[t][2], "keyword"
        return STAGES[t][1], "default"
    keyword_rules = {
        "T2": [(0, ["文艺复兴", "宗教改革", "早期", "前哥伦布"]),
               (2, ["启蒙", "感伤", "清代", "成熟读者"]),
               (1, ["巴洛克", "晚明", "江户", "骑士罗曼司解构"]),],
        "T3": [(0, ["浪漫", "早期", "革命余波"]),
               (2, ["自然主义", "象征主义", "唯美", "颓废", "世纪末", "晚期"]),
               (1, ["现实主义", "市场", "连载", "成熟"]),],
        "T4": [(0, ["世纪末", "酝酿", "前史"]),
               (1, ["1914—1918", "战争断裂"]),
               (3, ["政治极化", "反殖民", "战时", "后期"]),
               (2, ["高峰现代主义", "意识流", "先锋派"]),],
        "T5": [(0, ["废墟", "罪责", "大屠杀", "战败"]),
               (1, ["去殖民", "民族国家"]),
               (3, ["后现代成熟", "退潮"]),
               (2, ["Boom", "文学爆炸", "全球分叉"]),],
        "T6": [(0, ["冷战晚期"]),
               (3, ["疫情", "AI", "人工智能"]),
               (2, ["数字平台", "气候", "技术社会", "当代全球类型"]),
               (1, ["离散", "全球化", "全球市场"]),],
    }
    for index, words in keyword_rules[t]:
        if any(word in blob for word in words):
            return STAGES[t][index], "keyword"
    defaults = {"T2": 1, "T3": 1, "T4": 2, "T5": 2, "T6": 1}
    return STAGES[t][defaults[t]], "default"


def infer_role(t: str, old_history: str, mechanisms: list[str], stage: str) -> tuple[str, str]:
    # A generated history repeats the prior inferred role, so it must not become
    # evidence for the next run. Specific pre-existing history remains primary.
    history_text = "" if "（读前预判）" in old_history else old_history
    rules = [
        ("奠基", ["奠基", "源头", "开创"]),
        ("高峰", ["高峰"]),
        ("成熟", ["成熟"]),
        ("转折", ["转折", "断裂", "解构", "革命"]),
        ("形式突破", ["意识流", "叙事视角", "语言实验", "文类融合", "先锋"]),
        ("过渡", ["过渡", "转型", "晚期"]),
    ]
    for role, words in rules:
        if any(word in history_text for word in words):
            return role, "keyword"
    mechanism_text = " ".join(mechanisms)
    direct_mechanism_rules = {
        "T0": [("经典化", ["经典化"]), ("转折", ["历史记录向文学叙事"])],
        "T1": [("跨区域转译", ["翻译与改写"]), ("经典化", ["再经典化"])],
        "T2": [("转折", ["宗教改革"]), ("跨区域转译", ["俗语化、翻译"])],
        "T3": [("跨区域转译", ["翻译、帝国与跨洋市场"])],
        "T4": [("形式突破", ["心理、主体与叙事视角"]),
               ("转折", ["世界大战、革命与政治极化"]),
               ("边缘突破", ["帝国、殖民、反殖民与文化翻译"])],
        "T5": [("边缘突破", ["去殖民、民族国家与后殖民转向"])],
        "T6": [("边缘突破", ["身份、性别与代表权"]),
               ("形式突破", ["类型全球化与文类融合"]),
               ("反拨", ["记忆、创伤与历史重写"])],
    }
    for role, words in direct_mechanism_rules[t]:
        if any(word in mechanism_text for word in words):
            return role, "mechanism"
    stage_roles = {
        "T0": ["奠基", "成熟", "过渡"],
        "T1": ["奠基", "成熟", "过渡"],
        "T2": ["奠基", "成熟", "过渡"],
        "T3": ["奠基", "成熟", "过渡"],
        "T4": ["转折", "转折", "高峰", "过渡"],
        "T5": ["转折", "扩散", "高峰", "过渡"],
        "T6": ["转折", "扩散", "形式突破", "转折"],
    }
    return stage_roles[t][STAGES[t].index(stage)], "stage"


def generic_history(value: str) -> bool:
    return (not value or " · " in value or "时期归属已确认" in value
            or "（读前预判）" in value)


def generated_history(t: str, fm: str, stage: str, role: str, mechanisms: list[str]) -> str:
    stage_name = stage.split("：", 1)[-1]
    mechanism = mechanisms[0]
    context = scalar(fm, CFG[t]["context"]) if CFG[t]["context"] else ""
    where = f"的{context}传统中" if t == "T0" and context else ""
    if t == "T1" and context:
        where = f"的{context}中"
    return f"{stage_name}{where}，以“{mechanism}”为主要路径的{role}节点（读前预判）"


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    stats: dict[str, Counter] = defaultdict(Counter)
    detail_rows = []
    changed_files = set()

    for path in sorted(WORKS.glob("*.md")):
        original = path.read_text(encoding="utf-8-sig")
        try:
            fm, body = frontmatter(original)
        except ValueError:
            continue
        if scalar(fm, "type") != "work":
            continue
        axes = set(list_field(fm, "axis_t"))
        fm2 = fm
        for t, cfg in CFG.items():
            if cfg["label"] not in axes:
                continue
            stats[t]["works"] += 1
            mechanisms = list_field(fm2, cfg["mechanism"])
            if not mechanisms:
                mechanisms = [cfg["fallback"]]
                fm2 = upsert_list(fm2, cfg["mechanism"], mechanisms)
                mech_source = "fallback"
            else:
                mech_source = "existing"
            old_history = scalar(fm2, cfg["history"])
            stage, stage_source = infer_stage(t, fm2, old_history, mechanisms)
            existing_role = scalar(fm2, cfg["role"])
            if existing_role and "（读前预判）" not in old_history:
                role, role_source = existing_role, "existing"
            else:
                role, role_source = infer_role(t, old_history, mechanisms, stage)
            if generic_history(old_history):
                history = generated_history(t, fm2, stage, role, mechanisms)
                history_source = "generated_from_generic" if old_history else "generated_missing"
            else:
                history, history_source = old_history, "existing_specific"

            fm2 = upsert_scalar(fm2, cfg["history"], history, cfg["mechanism"])
            fm2 = upsert_scalar(fm2, cfg["stage"], stage, cfg["mechanism"])
            fm2 = upsert_scalar(fm2, cfg["role"], role, cfg["mechanism"])
            stats[t][f"history:{history_source}"] += 1
            stats[t][f"stage:{stage_source}"] += 1
            stats[t][f"role:{role_source}"] += 1
            stats[t][f"mechanism:{mech_source}"] += 1
            stats[t][f"stage_value:{stage}"] += 1
            stats[t][f"role_value:{role}"] += 1
            detail_rows.append({
                "work": path.name, "id": scalar(fm2, "id"), "t": t,
                "history_position": history, "stage": stage, "historical_role": role,
                "mechanisms": " | ".join(mechanisms), "history_source": history_source,
                "stage_source": stage_source, "role_source": role_source,
                "mechanism_source": mech_source,
                "needs_reading_calibration": "yes" if "（读前预判）" in history else "no",
            })
        if fm2 != fm:
            path.write_text("---\n" + fm2 + "\n---\n" + body.lstrip("\n"), encoding="utf-8", newline="\n")
            changed_files.add(path)

    # Strict postconditions: every T membership has all four non-empty fields.
    failures = []
    for path in sorted(WORKS.glob("*.md")):
        text = path.read_text(encoding="utf-8-sig")
        try:
            fm, _ = frontmatter(text)
        except ValueError:
            continue
        axes = set(list_field(fm, "axis_t"))
        for t, cfg in CFG.items():
            if cfg["label"] not in axes:
                continue
            if not scalar(fm, cfg["history"]): failures.append((path.name, t, "history"))
            stage_value = scalar(fm, cfg["stage"])
            role_value = scalar(fm, cfg["role"])
            if stage_value not in STAGES[t]: failures.append((path.name, t, "stage"))
            if role_value not in HISTORICAL_ROLES: failures.append((path.name, t, "role"))
            if not list_field(fm, cfg["mechanism"]): failures.append((path.name, t, "mechanism"))
    if failures:
        raise SystemExit(f"postcondition failures: {failures[:20]} (total={len(failures)})")

    with DETAIL.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(detail_rows[0]))
        writer.writeheader()
        writer.writerows(detail_rows)

    lines = [
        "# T轴作品读前预填 V1", "",
        f"- 初次读前预填范围：**{len(detail_rows)}**", f"- 当前覆盖的 T轴作品：**{len(detail_rows)}**",
        f"- 本次复核执行产生变更：**{len(changed_files)}**",
        "- 原则：保留已有具体判断；替换‘文学场·文类’类通用占位；缺失值按年份、关键词和中段默认依次预填。", "",
        "## 覆盖与历史位置", "",
        "| T | works | 读前预判位置 | 保留的具体位置 |",
        "|---|---:|---:|---:|",
    ]
    for t in CFG:
        s = stats[t]
        generated = s["history:generated_missing"] + s["history:generated_from_generic"]
        lines.append(f"| {t} | {s['works']} | {generated} | {s['history:existing_specific']} |")
    lines += ["", "## 内部分期分布", ""]
    for t in CFG:
        values = [(k.removeprefix("stage_value:"), v) for k, v in stats[t].items()
                  if k.startswith("stage_value:")]
        lines.append(f"- **{t}**：" + "；".join(f"{name} {count}" for name, count in sorted(values, key=lambda x: -x[1])))
    lines += ["", "## 历史角色分布", ""]
    for t in CFG:
        values = [(k.removeprefix("role_value:"), v) for k, v in stats[t].items()
                  if k.startswith("role_value:")]
        lines.append(f"- **{t}**：" + "；".join(f"{name} {count}" for name, count in sorted(values, key=lambda x: -x[1])))
    lines += [
        "", "## 校准说明", "",
        "- 自动生成的历史位置带有‘（读前预判）’，应在阅读后重写。",
        "- 本批数据应整体视为读前导航，不视为读后文学史结论。",
        "- 详细值与 `needs_reading_calibration` 标记见 `T_AXIS_READING_PREFILL_V1.csv`。", "",
        "`T_AXIS_READING_PREFILL_V1 = APPLIED_AND_VERIFIED`", "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"CHANGED_FILES={len(changed_files)}")
    print(f"T_MEMBERSHIPS={len(detail_rows)}")
    print(f"POSTCONDITION_FAILURES={len(failures)}")


if __name__ == "__main__":
    main()
