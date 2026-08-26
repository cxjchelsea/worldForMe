from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WORKS = ROOT / '个人通识知识系统_v2_A2' / '30 世界文学' / '40 作品'
M_PREFIXES = ('m1_', 'm2_', 'modernism_', 'm32_', 'm4_', 'm51_', 'm52_')


def split_damaged_frontmatter(text: str):
    """Return (overlay_fm, canonical_fm, body) for the damaged pattern.

    Supported forms after the first valid frontmatter:
      ---\n<canonical yaml>\n---\n<body>
    or the observed broken form:
      ---\n<canonical yaml to EOF>
    The second segment is accepted only when it clearly looks like a work entity.
    """
    norm = text.replace('\r\n', '\n').replace('\r', '\n')
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', norm, flags=re.S)
    if not m:
        return None
    first = m.group(1)
    rest = m.group(2)
    if not re.match(r'^---\s*\n', rest):
        return None
    rest = re.sub(r'^---\s*\n', '', rest, count=1)

    # Prefer a proper closing delimiter when present; otherwise treat the rest as
    # displaced canonical YAML only if it clearly contains a canonical work header.
    m2 = re.match(r'^(.*?)\n---\s*\n(.*)$', rest, flags=re.S)
    if m2:
        second, body = m2.group(1), m2.group(2)
    else:
        second, body = rest, ''

    if not re.search(r'(?m)^type:\s*["\']?work["\']?\s*$', second):
        return None
    if not re.search(r'(?m)^id:\s*WL-WORK-', second):
        return None
    return first, second.rstrip('\n'), body


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
    if not block:
        return []
    # support both multiline YAML lists and simple inline lists
    head = block[0].split(':', 1)[1].strip()
    if head.startswith('[') and head.endswith(']'):
        return [x.strip() for x in head[1:-1].split(',') if x.strip()]
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
    overlay_keys = {k for k in first_map if k.startswith(M_PREFIXES)}

    # Cross-axis lists must be unioned so M repair never drops T/R/G/Q or other topics.
    for key in ('topics', 'topic_links', 'axis_m'):
        vals = []
        for source in (second_map.get(key), first_map.get(key)):
            for item in list_items(source):
                if item not in vals:
                    vals.append(item)
        if vals:
            second_map[key] = render_list(key, vals)

    # The overlay block contains the most recent M-axis-specific metadata.
    for key in overlay_keys:
        second_map[key] = first_map[key]

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


scanned = 0
repaired = []
for p in WORKS.glob('*.md'):
    text = p.read_text(encoding='utf-8', errors='strict')
    parts = split_damaged_frontmatter(text)
    if not parts:
        continue
    scanned += 1
    first, second, body = parts
    merged = merge_frontmatter(first, second)
    new_text = '---\n' + merged + '---\n'
    if body:
        new_text += body
    p.write_text(new_text, encoding='utf-8')
    repaired.append(p.name)

print('damaged_frontmatter_matches', scanned)
print('repaired_frontmatter_count', len(repaired))
for name in repaired[:100]:
    print('repaired', name)
