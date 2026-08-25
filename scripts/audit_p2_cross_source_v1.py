from __future__ import annotations

import csv
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path("个人通识知识系统_v2_A2/30 世界文学")
AUDIT = ROOT / "_audit/t_axis_completeness"
TRIAGE = AUDIT / "missing_t_triage_v1.csv"
OL = AUDIT / "openlibrary_priority_v2.csv"
OUT = AUDIT / "p2_cross_source_v1.csv"
SAFE = AUDIT / "p2_cross_source_safe_v1.csv"
REVIEW = AUDIT / "p2_cross_source_review_v1.csv"
REPORT = AUDIT / "P2_CROSS_SOURCE_V1.md"

BOUNDARIES = {500, 1500, 1800, 1890, 1945, 1980}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.casefold().replace("／", "/")
    s = re.sub(r"[^0-9a-z\u4e00-\u9fff]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def sim(a: str, b: str) -> float:
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    if a == b:
        return 1.0
    return SequenceMatcher(None, a, b).ratio()


def t_for_year(year: int | None) -> str:
    if year is None:
        return ""
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


def parse_year(raw: str) -> int | None:
    m = re.search(r"(?<!\d)(1\d{3}|20\d{2}|[5-9]\d{2})(?!\d)", raw or "")
    return int(m.group(1)) if m else None


def google_query(row: dict[str, str]) -> dict[str, str]:
    title = row.get("title_original") or row.get("title") or ""
    author = row.get("author_original") or row.get("author") or ""
    q = f'intitle:"{title}"'
    if author:
        q += f' inauthor:"{author}"'
    url = "https://www.googleapis.com/books/v1/volumes?" + urllib.parse.urlencode({"q": q, "maxResults": 10, "printType": "books"})
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "worldForMe-t-axis-audit/1.0"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.load(resp)
    except Exception as e:
        return {"gb_status": "ERROR", "gb_error": type(e).__name__}

    candidates = []
    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        gt = info.get("title", "")
        ga = "; ".join(info.get("authors") or [])
        gy = parse_year(info.get("publishedDate", ""))
        ts = max(sim(title, gt), sim(row.get("title", ""), gt))
        auths = [x.strip() for x in re.split(r"[;/]", author) if x.strip()]
        if auths:
            aus = max((sim(a, ga) for a in auths), default=0.0)
        else:
            aus = 0.0
        if ts >= 0.88 and aus >= 0.72 and gy is not None:
            candidates.append((gy, ts, aus, gt, ga, item.get("id", "")))

    if not candidates:
        return {"gb_status": "NO_RELIABLE_MATCH"}

    # Prefer the earliest bibliographic year among strongly matching editions,
    # then strongest title/author match. This reduces modern-reprint bias.
    candidates.sort(key=lambda x: (x[0], -(x[1] + x[2])))
    gy, ts, aus, gt, ga, gid = candidates[0]
    return {
        "gb_status": "MATCH",
        "gb_year": str(gy),
        "gb_t": t_for_year(gy),
        "gb_title": gt,
        "gb_authors": ga,
        "gb_id": gid,
        "gb_title_similarity": f"{ts:.3f}",
        "gb_author_similarity": f"{aus:.3f}",
    }


def main() -> None:
    with TRIAGE.open(encoding="utf-8-sig", newline="") as f:
        triage = [r for r in csv.DictReader(f) if r.get("tier") == "P2_EXTERNAL_MATCH_FRIENDLY"]
    with OL.open(encoding="utf-8-sig", newline="") as f:
        ol_rows = {r.get("id", ""): r for r in csv.DictReader(f) if r.get("tier") == "P2_EXTERNAL_MATCH_FRIENDLY"}

    # P1 was completed after TRIAGE_V1; P2 remains the same 421-entity population.
    results: dict[str, dict[str, str]] = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(google_query, r): r for r in triage}
        for i, fut in enumerate(as_completed(futs), 1):
            row = futs[fut]
            try:
                results[row["id"]] = fut.result()
            except Exception as e:
                results[row["id"]] = {"gb_status": "ERROR", "gb_error": type(e).__name__}
            if i % 50 == 0:
                print(f"google_books_done={i}/{len(triage)}", flush=True)

    out_rows = []
    safe_rows = []
    review_rows = []
    for r in triage:
        ol = ol_rows.get(r.get("id", ""), {})
        gb = results.get(r.get("id", ""), {})
        ol_year = parse_year(ol.get("candidate_year", ""))
        ol_t = ol.get("suggested_t", "") if ol.get("confidence") == "HIGH" else ""
        gb_year = parse_year(gb.get("gb_year", ""))
        gb_t = gb.get("gb_t", "")

        status = "REVIEW"
        reason = ""
        chosen_t = ""
        canonical_year_candidate = ""
        year_action = "LEAVE_BLANK"

        if gb.get("gb_status") != "MATCH":
            reason = "Google Books 无可靠标题+作者+年份匹配"
        elif not ol_t or ol_year is None:
            reason = "Open Library 未提供 HIGH 候选，缺少双来源交叉验证"
        elif ol_year in BOUNDARIES or gb_year in BOUNDARIES:
            reason = "至少一个来源落在冻结边界年，禁止自动处理"
        elif ol_t != gb_t:
            reason = f"跨来源 T 区间冲突：OL={ol_year}/{ol_t}, GB={gb_year}/{gb_t}"
        else:
            chosen_t = ol_t
            gap = abs(ol_year - gb_year)
            status = "SAFE_T"
            reason = f"双来源落在同一 {chosen_t}；年份差 {gap} 年"
            # Only fill canonical year when the two sources essentially agree.
            if gap <= 2:
                canonical_year_candidate = str(min(ol_year, gb_year))
                year_action = "FILL_YEAR"
            else:
                year_action = "T_ONLY_YEAR_REVIEW"

        merged = dict(r)
        merged.update({
            "ol_status": ol.get("status", ""),
            "ol_year": "" if ol_year is None else str(ol_year),
            "ol_t": ol_t,
            "ol_title": ol.get("ol_title", ""),
            "ol_authors": ol.get("ol_authors", ""),
            "ol_title_similarity": ol.get("title_similarity", ""),
            "ol_author_similarity": ol.get("author_similarity", ""),
            **gb,
            "cross_source_status": status,
            "chosen_t": chosen_t,
            "canonical_year_candidate": canonical_year_candidate,
            "year_action": year_action,
            "cross_source_reason": reason,
        })
        out_rows.append(merged)
        (safe_rows if status == "SAFE_T" else review_rows).append(merged)

    fields = list(dict.fromkeys(k for row in out_rows for k in row.keys()))
    for path, rows in [(OUT, out_rows), (SAFE, safe_rows), (REVIEW, review_rows)]:
        with path.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader(); w.writerows(rows)

    fill_year = sum(r["year_action"] == "FILL_YEAR" for r in safe_rows)
    t_only = sum(r["year_action"] == "T_ONLY_YEAR_REVIEW" for r in safe_rows)
    lines = [
        "# P2 Cross-Source T-axis Audit V1", "",
        "> Read-only. Google Books is used only as a second bibliographic signal; no Work mutation occurs in this audit.", "",
        f"- P2 population queried: **{len(triage)}**",
        f"- SAFE_T (Open Library + Google Books agree on T interval): **{len(safe_rows)}**",
        f"  - FILL_YEAR (source years within 2 years): **{fill_year}**",
        f"  - T_ONLY_YEAR_REVIEW (same T but larger year gap): **{t_only}**",
        f"- REVIEW: **{len(review_rows)}**", "",
        "## Safety gates", "",
        "- title/author matching is required on Google Books.",
        "- Open Library must already be HIGH.",
        "- exact frozen boundary years are never auto-applied.",
        "- the two sources must land in the same T interval.",
        "- canonical `year` is proposed only when source years differ by <=2; otherwise only T is considered safe.", "",
        "`P2_CROSS_SOURCE_V1 = AUDITED_READ_ONLY`", "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"p2={len(triage)} safe_t={len(safe_rows)} fill_year={fill_year} t_only={t_only} review={len(review_rows)}")


if __name__ == "__main__":
    main()
