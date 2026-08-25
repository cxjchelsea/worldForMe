from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKS_DIR = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "40 作品"
AUDIT_DIR = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "_audit" / "t_axis"
MARKER = AUDIT_DIR / "APPLY_T_AXIS_REVIEW_RESOLUTION_V1"
REPORT = AUDIT_DIR / "REVIEW_RESOLUTION_V1.md"

T_LABELS = {
    "T0": "T0 文学源头与古代文学",
    "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学",
    "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代",
    "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}

# 18 review relationships correspond to 17 unique work entities because
# 契诃夫短篇小说选 appeared in both the historical T3 and T4 review lists.
RESOLUTIONS = {
    "Darangen.md": ("T1", None, None, "口传史诗明确早于14世纪菲律宾伊斯兰化，但无可靠证据支持公元500年前定型；按可证实传统形成期归T1"),
    "Diné Bahaneʼ：纳瓦霍创世故事.md": ("T6", "Diné Bahaneʼ: The Navajo Creation Story", 1984, "当前实体题名对应Paul G. Zolbrod 1984年整理/英译本；按具体文本实体归T6，而非按神话内容归古代"),
    "Ozidi Saga.md": ("T5", "The Ozidi Saga", 1977, "当前可识别文本为J. P. Clark整理、翻译并于1977年出版的口传史诗文本，按文本实体归T5"),
    "太阳传说.md": ("T2", "Leyenda de los Soles", 1558, "按纳瓦特尔《太阳传说》/Manuscript of 1558处理；殖民时期1558年前后成文记录，归T2"),
    "姆温多史诗.md": ("T5", "The Mwindo Epic from the Banyanga", 1969, "当前可识别文本为Biebuyck与Kahombo整理、翻译的1969年出版文本，按记录文本归T5"),
    "巴里公主.md": ("T4", None, 1937, "韩国巫歌口传传统年代复杂；本库采用最早有明确录音/记录信息并出版的1937年文本作为操作性文本锚点，归T4"),
    "斯里拉玛传.md": ("T1", "Hikayat Seri Rama", None, "按马来文学《Hikayat Seri Rama》处理；现存文学传统通常定型于13—15世纪，归T1"),
    "毗湿奴往世书.md": ("T0", "Vishnu Purana", None, "成书年代学界存在较大争议；早期核心常被置于公元3—5世纪。当前T0可保留，但保留年代争议说明"),
    "未来世界.md": ("T4", "The Shape of Things to Come", 1933, "结合作者H. G. Wells及科幻书单语境，消歧为1933年The Shape of Things to Come，归T4"),
    "福尔摩斯探案集.md": ("T4", None, 1927, "作为福尔摩斯完整作品聚合实体处理；作品群形成跨度1887—1927，按完整语料闭合时间1927归T4，而非按首篇1887归T3"),
    "契诃夫短篇小说选.md": ("T4", None, None, "现代聚合选本，所收作品横跨1890；本库作为契诃夫短篇创作整体入口，按成熟/完整作品群主要形成至1904的口径保留T4"),
    "细雪.md": ("T5", "細雪", 1948, "1943开始连载但战时中断，战后三卷陆续出版并于1948完成；按主要文本完成时间归T5"),
    "四世同堂.md": ("T5", "四世同堂", 1948, "1944起写/刊行，完整写作在1948完成；按主要文本完成时间优先于首部连载时间，归T5"),
    "真田太平记.md": ("T6", "真田太平記", 1982, "1974—1982连载，跨越1980断点；按完整文本形成/连载完成时间1982归T6"),
    "武士的一分.md": ("T5", "盲目剣谺返し", 1978, "当前题名是2006年电影通行名，藤泽周平原作为短篇《盲目剣谺返し》，1978年发表；按原作文本归T5"),
    "惶然录.md": ("T6", "Livro do Desassossego", 1982, "主体写于20世纪前期，但作者未形成定稿书本；1982年首次作为编辑建构的独立作品出版。按当前书籍实体归T6"),
    "天才寓言.md": ("T6", "Parable of the Talents", 1998, "结合作者Octavia E. Butler、星云奖与反乌托邦语境，消歧为Parable of the Talents（1998），归T6"),
}


def replace_scalar(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    replacement = f"{key}: {value}"
    new_text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"Missing scalar field {key}")
    return new_text


def axis_values(text: str) -> list[str]:
    m = re.search(r"(?ms)^axis_t:\s*\n(?P<body>(?:[ \t]*-[^\n]*\n)+|[ \t]*\[\]\s*\n?)", text)
    if not m:
        raise RuntimeError("axis_t block not found")
    return [re.sub(r"^[ \t]*-\s*", "", line).strip() for line in m.group("body").splitlines() if line.strip().startswith("-")]


def replace_axis_t(text: str, target: str) -> str:
    pattern = re.compile(r"(?ms)^axis_t:\s*\n(?:[ \t]*-[^\n]*\n)+|^axis_t:\s*\n[ \t]*\[\]\s*\n?")
    replacement = f"axis_t:\n- {T_LABELS[target]}\n"
    new_text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError("Could not replace exactly one axis_t block")
    return new_text


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def main() -> None:
    if not MARKER.exists():
        print("T-axis review-resolution marker absent; nothing to apply.")
        return

    changed_axis = 0
    retained_axis = 0
    metadata_changed = 0
    report_rows: list[str] = []

    for filename, (target, original_title, year, note) in RESOLUTIONS.items():
        path = WORKS_DIR / filename
        if not path.exists():
            raise FileNotFoundError(path)
        text = path.read_text(encoding="utf-8")
        before_axis = axis_values(text)
        target_label = T_LABELS[target]

        if before_axis != [target_label]:
            text = replace_axis_t(text, target)
            changed_axis += 1
            axis_state = "CHANGED"
        else:
            retained_axis += 1
            axis_state = "RETAINED"

        md_changed = False
        if original_title is not None:
            desired = yaml_quote(original_title)
            m = re.search(r"(?m)^title_original:\s*(.*)$", text)
            if not m:
                raise RuntimeError(f"title_original missing in {filename}")
            if m.group(1).strip() != desired:
                text = replace_scalar(text, "title_original", desired)
                md_changed = True

        if year is not None:
            m = re.search(r"(?m)^year:\s*(.*)$", text)
            if not m:
                raise RuntimeError(f"year missing in {filename}")
            if m.group(1).strip() != str(year):
                text = replace_scalar(text, "year", str(year))
                md_changed = True

        quoted_note = yaml_quote("T-axis REVIEW V1：" + note)
        if re.search(r"(?m)^review_note:", text):
            current = re.search(r"(?m)^review_note:\s*(.*)$", text).group(1).strip()
            if current != quoted_note:
                text = replace_scalar(text, "review_note", quoted_note)
                md_changed = True
        else:
            # Insert review_note immediately after verification_status when absent.
            pat = re.compile(r"(?m)^(verification_status:\s*.*)$")
            text, n = pat.subn(r"\1\nreview_note: " + quoted_note, text, count=1)
            if n != 1:
                raise RuntimeError(f"Cannot insert review_note in {filename}")
            md_changed = True

        if md_changed:
            metadata_changed += 1

        path.write_text(text, encoding="utf-8", newline="\n")
        report_rows.append(f"- `{filename}` → **{target}** ({axis_state})：{note}")

    for filename, (target, _, _, _) in RESOLUTIONS.items():
        values = axis_values((WORKS_DIR / filename).read_text(encoding="utf-8"))
        if values != [T_LABELS[target]]:
            raise RuntimeError(f"Post-write verification failed for {filename}: {values}")

    report = [
        "# T-axis REVIEW Resolution V1",
        "",
        "## Scope",
        "",
        "- Historical REVIEW relationships: **18**",
        f"- Unique work entities resolved: **{len(RESOLUTIONS)}**",
        f"- axis_t changed: **{changed_axis}**",
        f"- axis_t retained: **{retained_axis}**",
        f"- entities with disambiguation metadata/review note updated: **{metadata_changed}**",
        "- BOUNDARY policy: unchanged",
        "- R/M/G/Q: unchanged",
        "",
        "## Governing rule",
        "",
        "Prefer the work's principal text formation/completion time; use first complete publication when the work did not exist as a stable book/text before editorial publication. Oral traditions are not assigned to T0 merely because their subject matter is ancient; use the earliest defensible textual/recorded form for the concrete entity in this repository.",
        "",
        "## Resolutions",
        "",
        *report_rows,
        "",
        "`T_AXIS_REVIEW_V1 = RESOLVED_AND_VERIFIED`",
        "",
    ]
    REPORT.write_text("\n".join(report), encoding="utf-8", newline="\n")
    MARKER.unlink()
    print(f"Resolved REVIEW V1: unique={len(RESOLUTIONS)}, axis_changed={changed_axis}, retained={retained_axis}, metadata={metadata_changed}")


if __name__ == "__main__":
    main()
