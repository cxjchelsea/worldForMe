from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / '个人通识知识系统_v2_A2' / '30 世界文学' / '40 作品'
M_PREFIXES = ('m1_', 'm2_', 'modernism_', 'm32_', 'm4_', 'm51_', 'm52_')


def split_two_frontmatters(text: str):
    if not text.startswith('---\n'):
        return None
    first_end = text.find('\n---\n', 4)
    if first_end < 0:
        return None
    rest = text[first_end + 5:]
    if not rest.startswith('---\n'):
        return None
    second_end = rest.find('\n---\n', 4)
    if second_end < 0:
        return None
    return text[4:first_end], rest[4:second_end], rest[second_end + 5:]


def field_blocks(fm: str):
    lines = fm.splitlines()
    out = []
    i = 0
    while i < len(lines):
        m = re.match(r'^([A-Za-z0-9_.-]+):', lines[i])
        if not m:
            i += 1
            continue
        key = m.group(1)
        block = [lines[i]]
        i += 1
        while i < len(lines) and not re.match(r'^([A-Za-z0-9_.-]+):', lines[i]):
            block.append(lines[i])
            i += 1
        out.append((key, block))
    return out


def list_items(block):
    items = []
    for line in block[1:]:
        m = re.match(r'^\s*-\s*(.*)$', line)
        if m:
            items.append(m.group(1))
    return items


def render_list(key, items):
    return [f'{key}:'] + [f'- {x}' for x in items]


def merge_frontmatter(first: str, second: str):
    fb = field_blocks(first)
    sb = field_blocks(second)
    first_map = {k: b for k, b in fb}
    second_map = {k: b for k, b in sb}

    # canonical second frontmatter remains authoritative except M-axis overlay fields.
    overlay_keys = {k for k in first_map if k.startswith(M_PREFIXES)}

    # merge shared multi-value cross-axis fields instead of replacing them.
    for key in ('topics', 'topic_links', 'axis_m'):
        vals = []
        for source in (second_map.get(key), first_map.get(key)):
            if source:
                for item in list_items(source):
                    if item not in vals:
                        vals.append(item)
        if vals:
            second_map[key] = render_list(key, vals)

    for key in overlay_keys:
        second_map[key] = first_map[key]

    # preserve original canonical field order; append newly introduced M fields at end.
    rendered = []
    seen = set()
    for key, _ in sb:
        if key in seen:
            continue
        seen.add(key)
        rendered.extend(second_map[key])
    for key, _ in fb:
        if key in seen or key in ('topics', 'topic_links', 'axis_m'):
            continue
        if key in overlay_keys:
            seen.add(key)
            rendered.extend(second_map[key])
    return '\n'.join(rendered).rstrip() + '\n'


repaired = []
for p in WORKS.glob('*.md'):
    text = p.read_text(encoding='utf-8', errors='strict')
    parts = split_two_frontmatters(text)
    if not parts:
        continue
    first, second, body = parts
    merged = merge_frontmatter(first, second)
    new_text = '---\n' + merged + '---\n' + body
    p.write_text(new_text, encoding='utf-8')
    repaired.append(p.name)

print('repaired_double_frontmatter_count', len(repaired))
for name in repaired[:50]:
    print('repaired', name)
