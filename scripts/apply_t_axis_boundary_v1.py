from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORLD = ROOT / "个人通识知识系统_v2_A2" / "30 世界文学"
WORKS = WORLD / "40 作品"
AUDIT = WORLD / "_audit" / "t_axis"
MARKER = AUDIT / "APPLY_T_AXIS_BOUNDARY_V1"
REPORT = AUDIT / "BOUNDARY_RESOLUTION_V1.md"
POLICY = AUDIT / "BOUNDARY_POLICY_V1.md"

T_LABELS = {
    "T0": "T0 文学源头与古代文学",
    "T1": "T1 中古多中心文学世界",
    "T2": "T2 早期现代文学",
    "T3": "T3 19世纪现代文学体系",
    "T4": "T4 全球现代主义时代",
    "T5": "T5 二战后多极文学",
    "T6": "T6 当代全球文学",
}

# All 26 items previously classified BOUNDARY in the manual screening.
# Exact boundary years follow a left-closed/right-open period policy.
# Broad/approximate ranges use primary textual fixation / first complete publication.
RESOLUTIONS = {
    # T0/T1 boundary around 500
    "脚镯记.md": ("T1", "约5—6世纪；主要文本形成跨入500后，主归T1"),
    # T2/T3 boundary around 1800
    "春香传.md": ("T2", "18—19世纪口传/盘索里传统跨界；现有实体保留T2，记录边界性"),
    # T3/T4 boundary at 1890
    "乌有乡消息.md": ("T4", "1890；按[1890,1945)归T4"),
    "四签名.md": ("T4", "1890；按[1890,1945)归T4"),
    "道林·格雷的画像.md": ("T4", "1890；按[1890,1945)归T4"),
    "饥饿.md": ("T4", "1890；按[1890,1945)归T4"),
    # T4/T5 boundary at 1945
    "往事.md": ("T5", "1945；按[1945,1980)归T5"),
    "德里纳河上的桥.md": ("T5", "1945；按[1945,1980)归T5"),
    "维吉尔之死.md": ("T5", "1945；按[1945,1980)归T5"),
    "黑夜有千只眼.md": ("T5", "1945；按[1945,1980)归T5"),
    "黑孩子.md": ("T5", "1945；按[1945,1980)归T5"),
    "动物农场.md": ("T5", "1945；当前归属已符合[1945,1980)"),
    # T5/T6 boundary at 1980
    "人世间（普拉姆迪亚）.md": ("T6", "1980；按[1980,+∞)归T6"),
    "十字架上的魔鬼.md": ("T6", "1980；按[1980,+∞)归T6"),
    "未完的传说.md": ("T6", "1980；按[1980,+∞)归T6"),
    "生活与命运.md": ("T6", "1980首次完整出版语境；按[1980,+∞)归T6"),
    "等待野蛮人.md": ("T6", "1980；按[1980,+∞)归T6"),
    "武士.md": ("T6", "1980；按[1980,+∞)归T6"),
    "马永贝.md": ("T6", "1980；按[1980,+∞)归T6"),
    "将军吟.md": ("T6", "约1980；当前T6保留"),
    "笨伯联盟.md": ("T6", "1980首次出版；按[1980,+∞)归T6"),
    "拷刑者之影.md": ("T6", "1980；按[1980,+∞)归T6"),
    "时代景观.md": ("T6", "1980；按[1980,+∞)归T6"),
    "迷雾.md": ("T6", "1980；按[1980,+∞)归T6"),
    "雪后.md": ("T6", "约1980；当前T6保留"),
    "龙蛋.md": ("T6", "1980；按[1980,+∞)归T6"),
}


def axis_values(text: str) -> list[str]:
    m = re.search(r"(?ms)^axis_t:\s*\n(?P<body>(?:[ \t]*-[^\n]*\n)+|[ \t]*\[\]\s*\n?)", text)
    if not m:
        raise RuntimeError("axis_t block not found")
    return [re.sub(r"^[ \t]*-\s*", "", line).strip() for line in m.group("body").splitlines() if line.strip().startswith("-")]


def replace_axis_t(text: str, target: str) -> str:
    pattern = re.compile(r"(?ms)^axis_t:\s*\n(?:[ \t]*-[^\n]*\n)+|^axis_t:\s*\n[ \t]*\[\]\s*\n?")
    replacement = f"axis_t:\n- {T_LABELS[target]}\n"
    out, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError("Could not replace exactly one axis_t block")
    return out


def main() -> None:
    if not MARKER.exists():
        print("T-axis boundary marker absent; nothing to apply.")
        return
    if len(RESOLUTIONS) != 26:
        raise RuntimeError(f"Expected 26 boundary resolutions, got {len(RESOLUTIONS)}")

    changed = []
    unchanged = []
    for filename, (target, reason) in RESOLUTIONS.items():
        path = WORKS / filename
        if not path.exists():
            raise FileNotFoundError(f"Boundary work not found: {path}")
        text = path.read_text(encoding="utf-8")
        values = axis_values(text)
        expected = [T_LABELS[target]]
        if values == expected:
            unchanged.append((filename, target, reason))
            continue
        # Boundary resolution may only change T, never R/M/G/Q or other fields.
        path.write_text(replace_axis_t(text, target), encoding="utf-8", newline="\n")
        changed.append((filename, target, reason))

    for filename, (target, _) in RESOLUTIONS.items():
        values = axis_values((WORKS / filename).read_text(encoding="utf-8"))
        if values != [T_LABELS[target]]:
            raise RuntimeError(f"Post-write verification failed for {filename}: {values}")

    POLICY.write_text(
        "# T-axis Boundary Policy V1\n\n"
        "## Canonical interval policy\n\n"
        "T 轴采用左闭右开断代：\n\n"
        "- T0: `< 500`\n"
        "- T1: `[500, 1500)`\n"
        "- T2: `[1500, 1800)`\n"
        "- T3: `[1800, 1890)`\n"
        "- T4: `[1890, 1945)`\n"
        "- T5: `[1945, 1980)`\n"
        "- T6: `[1980, +∞)`\n\n"
        "因此恰好落在 500、1500、1800、1890、1945、1980 的作品归入后一个时代。\n\n"
        "## Cross-boundary works\n\n"
        "若年代是范围、连载期或口传传统且跨越断点，不机械取中点。优先依据：作品主要文本定型时间，其次首次完整发表/出版时间。仍无法唯一裁决的实体应进入 REVIEW，而非凭故事时代或题材归类。\n\n"
        "## Scope\n\n"
        "本政策只约束 T 轴；不修改 R/M/G/Q，不处理异译名、重复实体或聚合选本。\n",
        encoding="utf-8",
        newline="\n",
    )

    lines = [
        "# T-axis Boundary Resolution V1",
        "",
        f"- Total boundary items resolved: **{len(RESOLUTIONS)}**",
        f"- axis_t changed: **{len(changed)}**",
        f"- already compliant / retained: **{len(unchanged)}**",
        "- REVIEW: unchanged",
        "- R/M/G/Q: unchanged",
        "",
        "## Resolutions",
        "",
    ]
    for filename, (target, reason) in RESOLUTIONS.items():
        state = "CHANGED" if any(x[0] == filename for x in changed) else "RETAINED"
        lines.append(f"- `{filename}` → **{target}** ({state})：{reason}")
    lines += ["", "`T_AXIS_BOUNDARY_V1 = RESOLVED_AND_VERIFIED`", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    MARKER.unlink()
    print(f"Resolved 26 T-axis boundary items: changed={len(changed)}, retained={len(unchanged)}")


if __name__ == "__main__":
    main()
