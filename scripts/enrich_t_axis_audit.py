from __future__ import annotations

import csv
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学/40 作品")
OUT = Path("个人通识知识系统_v2_A2/30 世界文学/_audit/t_axis")
MASTER_FILES = [
    Path("世界文学经典母库_V1.csv"),
    Path("世界文学经典母库_V2_增量_CANON-196-300.csv"),
]

T_LABELS = {
    "T0": "T0 文学源头与古代文学",
    "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学",
    "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代",
    "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}
LABEL_TO_T = {v: k for k, v in T_LABELS.items()}
BOUNDARIES = {500, 1500, 1800, 1890, 1945, 1980}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").lower()
    s = re.sub(r"[《》〈〉「」『』\[\]()（）{}【】'\"“”‘’·・:：;；,，.。!?！？/\\\-—–_\s]", "", s)
    return s


def frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return ""
    m = re.match(r"^---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    return m.group(1) if m else ""


def scalar(fm: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*?)\s*$", fm)
    if not m:
        return ""
    value = m.group(1).strip()
    if value.lower() in {"null", "none", "~"}:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]
    return value


def list_field(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:\s*\[\s*\]\s*$", line):
            return []
        inline = re.match(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", line)
        if inline:
            raw = inline.group(1).strip()
            return [] if not raw else [x.strip().strip('"\'') for x in raw.split(",")]
        if re.match(rf"^{re.escape(key)}:\s*$", line):
            out: list[str] = []
            for nxt in lines[i + 1 :]:
                m = re.match(r"^\s*-\s*(.*?)\s*$", nxt)
                if m:
                    out.append(m.group(1).strip().strip('"\''))
                    continue
                if re.match(r"^[A-Za-z0-9_\u4e00-\u9fff].*?:", nxt):
                    break
                if nxt.strip() and not nxt.startswith((" ", "\t")):
                    break
            return out
    return []


def parse_note_year(fm: str) -> int | None:
    raw = scalar(fm, "year")
    if not raw:
        return None
    m = re.search(r"-?\d{1,4}", raw)
    return int(m.group(0)) if m else None


def t_for_year(year: int) -> str | None:
    if year in BOUNDARIES:
        return None
    if year < 500:
        return "T0"
    if year < 1500:
        return "T1"
    if year < 1800:
        return "T2"
    if year < 1890:
        return "T3"
    if year < 1945:
        return "T4"
    if year < 1980:
        return "T5"
    return "T6"


def years_from_text(text: str) -> list[int]:
    if not text:
        return []
    s = unicodedata.normalize("NFKC", text)
    years: list[int] = []

    # BCE explicit years, e.g. 前458 / 公元前458
    for m in re.finditer(r"(?:公元)?前\s*(\d{1,4})", s):
        years.append(-int(m.group(1)))
    s_no_bce = re.sub(r"(?:公元)?前\s*\d{1,4}", " ", s)

    # BCE centuries, e.g. 前8世纪 -> representative midpoint -750
    for m in re.finditer(r"(?:公元)?前\s*(\d{1,2})\s*世纪", s):
        c = int(m.group(1))
        years.append(-(c * 100 - 50))
    s_no_bce = re.sub(r"(?:公元)?前\s*\d{1,2}\s*世纪", " ", s_no_bce)

    # CE centuries, representative midpoint.
    for m in re.finditer(r"(?<!前)(\d{1,2})\s*世纪", s_no_bce):
        c = int(m.group(1))
        years.append((c - 1) * 100 + 50)
    s_no_cent = re.sub(r"\d{1,2}\s*世纪", " ", s_no_bce)

    # Explicit CE years. Avoid small numbers that are usually volume/count markers.
    for m in re.finditer(r"(?<!\d)(\d{3,4})(?!\d)", s_no_cent):
        years.append(int(m.group(1)))

    return sorted(set(years))


def evidence_t_from_time_text(text: str) -> tuple[str, str]:
    years = years_from_text(text)
    if not years:
        return "", "NO_PARSEABLE_DATE"
    if any(y in BOUNDARIES for y in years):
        return "", "BOUNDARY_DATE"
    ts = {t_for_year(y) for y in years}
    ts.discard(None)
    if len(ts) == 1:
        return next(iter(ts)), "SINGLE_PERIOD"
    return "", "CROSSES_PERIODS"


def load_master_index() -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in MASTER_FILES:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                rec = {
                    "id": row.get("ID", ""),
                    "cn_title": row.get("作品中文常用名", ""),
                    "orig_title": row.get("Original_or_English_Title", ""),
                    "cn_author": row.get("作者中文名", ""),
                    "author": row.get("Author", ""),
                    "time": row.get("首次成书_出版时间", ""),
                    "era": row.get("时代", ""),
                    "source": path.name,
                }
                for title in [rec["cn_title"], rec["orig_title"]]:
                    n = norm(title)
                    if n:
                        index[n].append(rec)
    return index


def choose_master(note_titles: list[str], note_authors: list[str], index: dict[str, list[dict[str, str]]]) -> dict[str, str] | None:
    candidates: list[dict[str, str]] = []
    seen = set()
    for title in note_titles:
        for rec in index.get(norm(title), []):
            key = (rec["id"], rec["source"])
            if key not in seen:
                candidates.append(rec)
                seen.add(key)
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    author_norms = {norm(a) for a in note_authors if norm(a)}
    for rec in candidates:
        if norm(rec["cn_author"]) in author_norms or norm(rec["author"]) in author_norms:
            return rec
    return None


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    master = load_master_index()
    rows: list[dict[str, str]] = []

    for path in sorted(ROOT.glob("*.md"), key=lambda p: p.name.casefold()):
        fm = frontmatter(path.read_text(encoding="utf-8"))
        if not fm:
            continue
        axis_t = list_field(fm, "axis_t")
        current = [LABEL_TO_T[x] for x in axis_t if x in LABEL_TO_T]
        if not current:
            continue

        title = scalar(fm, "title") or path.stem
        title_original = scalar(fm, "title_original")
        author = scalar(fm, "author")
        author_original = scalar(fm, "author_original")
        aliases = list_field(fm, "aliases")
        note_year = parse_note_year(fm)

        master_rec = choose_master(
            [title, title_original, path.stem, *aliases],
            [author, author_original],
            master,
        )
        master_time = master_rec["time"] if master_rec else ""
        master_t, master_date_status = evidence_t_from_time_text(master_time)

        current_one = current[0] if len(current) == 1 else ""
        suggested = ""
        status = "REVIEW"
        evidence = ""
        confidence = ""

        if len(current) > 1:
            status = "REVIEW"
            evidence = "MULTI_T"
        elif note_year is not None:
            if note_year in BOUNDARIES:
                status = "BOUNDARY"
                evidence = f"note.year={note_year}"
                confidence = "HIGH"
            else:
                suggested = t_for_year(note_year) or ""
                status = "PASS" if suggested == current_one else "MOVE_CANDIDATE"
                evidence = f"note.year={note_year}"
                confidence = "HIGH"
        elif master_rec and master_t:
            suggested = master_t
            status = "PASS" if suggested == current_one else "MOVE_CANDIDATE"
            evidence = f"{master_rec['id']} 首次成书_出版时间={master_time}"
            confidence = "HIGH"
        elif master_rec and master_date_status in {"BOUNDARY_DATE", "CROSSES_PERIODS"}:
            status = "BOUNDARY" if master_date_status == "BOUNDARY_DATE" else "REVIEW"
            evidence = f"{master_rec['id']} 首次成书_出版时间={master_time} ({master_date_status})"
            confidence = "HIGH"
        else:
            status = "REVIEW"
            evidence = "缺少可靠年代证据"

        rows.append({
            "file": path.name,
            "title": title,
            "author": author,
            "current_t": ";".join(current),
            "note_year": "" if note_year is None else str(note_year),
            "master_id": master_rec["id"] if master_rec else "",
            "master_time": master_time,
            "suggested_t": suggested,
            "status": status,
            "confidence": confidence,
            "evidence": evidence,
            "verification_status": scalar(fm, "verification_status"),
            "id": scalar(fm, "id"),
        })

    fields = [
        "file", "title", "author", "current_t", "note_year", "master_id", "master_time",
        "suggested_t", "status", "confidence", "evidence", "verification_status", "id",
    ]
    with (OUT / "semantic_stage1_all.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

    by_t = defaultdict(list)
    for r in rows:
        for t in r["current_t"].split(";"):
            if t:
                by_t[t].append(r)
    for t in T_LABELS:
        with (OUT / f"semantic_stage1_{t}.csv").open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader(); w.writerows(by_t[t])

    anomalies = [r for r in rows if r["status"] in {"MOVE_CANDIDATE", "BOUNDARY", "REVIEW"}]
    with (OUT / "semantic_stage1_anomalies.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(anomalies)

    counts = Counter(r["status"] for r in rows)
    matched = sum(1 for r in rows if r["master_id"])
    lines = [
        "# T 轴全量语义筛查 Stage 1",
        "",
        "> Stage 1 使用作品笔记 `year` 与两份世界文学经典母库的 `首次成书_出版时间`。不修改任何作品。",
        "",
        f"- T0–T6 作品总数：**{len(rows)}**",
        f"- 匹配经典母库：**{matched}**",
        f"- PASS：**{counts['PASS']}**",
        f"- MOVE_CANDIDATE：**{counts['MOVE_CANDIDATE']}**",
        f"- BOUNDARY：**{counts['BOUNDARY']}**",
        f"- REVIEW：**{counts['REVIEW']}**",
        "",
        "下一阶段应人工核验 MOVE_CANDIDATE / BOUNDARY，并继续为 REVIEW 引入其他可靠年代证据。",
    ]
    (OUT / "SEMANTIC_STAGE1.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"works={len(rows)} master_matched={matched}")
    print(" ".join(f"{k}={counts[k]}" for k in ["PASS", "MOVE_CANDIDATE", "BOUNDARY", "REVIEW"]))


if __name__ == "__main__":
    main()
