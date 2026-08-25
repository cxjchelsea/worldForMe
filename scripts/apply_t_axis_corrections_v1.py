from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKS_DIR = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "40 作品"
AUDIT_DIR = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学" / "_audit" / "t_axis"
MARKER = AUDIT_DIR / "APPLY_T_AXIS_CORRECTIONS_V1"
MANUAL_T0_T2 = AUDIT_DIR / "manual_T0_T2_all.csv"
MANUAL_T3_T6 = AUDIT_DIR / "MANUAL_T3_T6.md"
REPORT = AUDIT_DIR / "CORRECTION_V1.md"

T_LABELS = {
    "T0": "T0 文学源头与古代文学",
    "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学",
    "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代",
    "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}

EXPECTED_MOVE_COUNT = 149
DOUBLE_HANG_FIXES = {
    "82年生的金智英.md": "T6",
    "夜晚的潜水艇.md": "T6",
}


def parse_t0_t2_moves() -> list[tuple[str, str, str]]:
    moves: list[tuple[str, str, str]] = []
    with MANUAL_T0_T2.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if (row.get("manual_status") or "").strip() != "MOVE":
                continue
            filename = (row.get("file") or "").strip()
            source = (row.get("current_t") or "").strip()
            target = (row.get("manual_suggested_t") or "").strip()
            if not filename or source not in T_LABELS or target not in T_LABELS:
                raise RuntimeError(f"Invalid manual T0-T2 MOVE row: {row}")
            moves.append((filename, source, target))
    return moves


def resolve_review_filename(stem: str) -> str:
    """Resolve a reviewed display title to the existing canonical Markdown filename.

    Audit prose uses ordinary '/' in display titles, while repository filenames sanitize
    that character to the full-width '／'. No fuzzy title matching is permitted here.
    """
    candidates = [f"{stem}.md"]
    if "/" in stem:
        candidates.append(f"{stem.replace('/', '／')}.md")

    existing = [name for name in candidates if (WORKS_DIR / name).exists()]
    if len(existing) == 1:
        return existing[0]
    if len(existing) > 1:
        raise RuntimeError(f"Ambiguous reviewed filename for {stem!r}: {existing}")
    # Return the literal candidate so the later existence check produces a precise failure.
    return candidates[0]


def parse_t3_t6_moves() -> list[tuple[str, str, str]]:
    text = MANUAL_T3_T6.read_text(encoding="utf-8")
    moves: list[tuple[str, str, str]] = []
    source: str | None = None
    target: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        m_source = re.match(r"^#\s+(T[3-6])\b", line)
        if m_source:
            source = m_source.group(1)
            target = None
            continue

        m_target = re.match(r"^##\s+MOVE\s+→\s+(T[0-6])\b", line)
        if m_target:
            target = m_target.group(1)
            continue

        if line.startswith("## ") and not line.startswith("## MOVE"):
            target = None
            continue

        if source and target and line.startswith("- "):
            item = line[2:].strip()
            # Audit bullets use: - 《title》——year or - `title`——year.
            title_part = item.split("——", 1)[0].strip()
            if title_part.startswith("`") and title_part.endswith("`"):
                stem = title_part[1:-1]
            elif title_part.startswith("《") and title_part.endswith("》"):
                stem = title_part[1:-1]
            else:
                raise RuntimeError(f"Unrecognized MOVE bullet: {raw_line}")
            moves.append((resolve_review_filename(stem), source, target))

    return moves


def axis_values(text: str) -> list[str]:
    m = re.search(r"(?ms)^axis_t:\s*\n(?P<body>(?:[ \t]*-[^\n]*\n)+|[ \t]*\[\]\s*\n?)", text)
    if not m:
        raise RuntimeError("axis_t block not found")
    return [
        re.sub(r"^[ \t]*-\s*", "", line).strip()
        for line in m.group("body").splitlines()
        if line.strip().startswith("-")
    ]


def replace_axis_t(text: str, target: str) -> str:
    label = T_LABELS[target]
    pattern = re.compile(
        r"(?ms)^axis_t:\s*\n(?:[ \t]*-[^\n]*\n)+|^axis_t:\s*\n[ \t]*\[\]\s*\n?"
    )
    replacement = f"axis_t:\n- {label}\n"
    new_text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError("Could not replace exactly one axis_t block")
    return new_text


def main() -> None:
    if not MARKER.exists():
        print("T-axis correction marker absent; nothing to apply.")
        return

    moves = parse_t0_t2_moves() + parse_t3_t6_moves()
    if len(moves) != EXPECTED_MOVE_COUNT:
        raise RuntimeError(
            f"Refusing mutation: expected {EXPECTED_MOVE_COUNT} reviewed MOVE rows, got {len(moves)}"
        )

    seen: dict[str, tuple[str, str]] = {}
    for filename, source, target in moves:
        prior = seen.get(filename)
        if prior and prior != (source, target):
            raise RuntimeError(f"Conflicting MOVE decisions for {filename}: {prior} vs {(source, target)}")
        seen[filename] = (source, target)

    changed_moves = 0
    already_correct = 0
    corrected: list[str] = []

    for filename, source, target in moves:
        path = WORKS_DIR / filename
        if not path.exists():
            raise FileNotFoundError(f"Reviewed MOVE target not found: {path}")
        text = path.read_text(encoding="utf-8")
        values = axis_values(text)
        target_label = T_LABELS[target]
        source_prefix = f"{source} "

        if values == [target_label]:
            already_correct += 1
            continue

        if not any(v == source or v.startswith(source_prefix) for v in values):
            raise RuntimeError(
                f"Refusing unexpected mutation for {filename}: audit source={source}, current axis_t={values}"
            )

        path.write_text(replace_axis_t(text, target), encoding="utf-8", newline="\n")
        changed_moves += 1
        corrected.append(f"- `{filename}`: {source} → {target}")

    double_hang_changes = 0
    for filename, target in DOUBLE_HANG_FIXES.items():
        path = WORKS_DIR / filename
        if not path.exists():
            raise FileNotFoundError(f"Double-hang target not found: {path}")
        text = path.read_text(encoding="utf-8")
        values = axis_values(text)
        target_label = T_LABELS[target]
        if values == [target_label]:
            continue
        if not any(v.startswith("T5 ") for v in values) or not any(v.startswith("T6 ") for v in values):
            raise RuntimeError(f"Unexpected double-hang state for {filename}: {values}")
        path.write_text(replace_axis_t(text, target), encoding="utf-8", newline="\n")
        double_hang_changes += 1

    for filename, _, target in moves:
        values = axis_values((WORKS_DIR / filename).read_text(encoding="utf-8"))
        if values != [T_LABELS[target]]:
            raise RuntimeError(f"Post-write verification failed for {filename}: {values}")

    for filename, target in DOUBLE_HANG_FIXES.items():
        values = axis_values((WORKS_DIR / filename).read_text(encoding="utf-8"))
        if values != [T_LABELS[target]]:
            raise RuntimeError(f"Double-hang verification failed for {filename}: {values}")

    report_lines = [
        "# T-axis Correction V1",
        "",
        "## Scope",
        "",
        f"- Reviewed MOVE decisions: **{len(moves)}**",
        f"- MOVE files changed in this run: **{changed_moves}**",
        f"- MOVE files already correct: **{already_correct}**",
        f"- T5/T6 double-hang fixes changed: **{double_hang_changes}**",
        "- BOUNDARY: unchanged",
        "- REVIEW: unchanged",
        "- R/M/G/Q: unchanged",
        "",
        "## Source of truth",
        "",
        "- T0–T2: `manual_T0_T2_all.csv` rows with `manual_status=MOVE`",
        "- T3–T6: `MANUAL_T3_T6.md` sections `MOVE → Tx`",
        "- Explicit double-hang cleanup: `82年生的金智英.md`, `夜晚的潜水艇.md` → T6 only",
        "",
        "## Applied MOVE entries",
        "",
        *corrected,
        "",
        "`T_AXIS_CORRECTION_V1 = APPLIED_AND_VERIFIED`",
        "",
    ]
    REPORT.write_text("\n".join(report_lines), encoding="utf-8", newline="\n")

    MARKER.unlink()
    print(
        f"Applied T-axis correction V1: moves={len(moves)}, changed={changed_moves}, "
        f"already_correct={already_correct}, double_hang_changes={double_hang_changes}"
    )


if __name__ == "__main__":
    main()
