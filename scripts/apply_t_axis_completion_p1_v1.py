from __future__ import annotations

import re
from pathlib import Path

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS = ROOT / '40 作品'
AUDIT = ROOT / '_audit' / 't_axis_completeness'
MARKER = AUDIT / 'APPLY_T_AXIS_COMPLETION_P1_V1'
REPORT = AUDIT / 'T_AXIS_COMPLETION_P1_V1.md'

T_LABELS = {
    'T0': 'T0 文学源头与古代文学',
    'T1': 'T1 中古多中心文学世界',
    'T2': 'T2 早期现代文学',
    'T3': 'T3 19世纪现代文学体系',
    'T4': 'T4 全球现代主义时代',
    'T5': 'T5 二战后多极文学',
    'T6': 'T6 当代全球文学',
}

# Explicitly reviewed P1 canon/award works. For multi-volume works, year follows
# the frozen T-axis policy: principal text completion / first complete publication.
ROWS = [
    ('Dance Hall of the Dead.md', 'WL-WORK-2195', 1973, 'T5', 'single-work first publication'),
    ('House Made of Dawn.md', 'WL-WORK-2243', 1968, 'T5', 'single-work first publication'),
    ('Nervous Conditions.md', 'WL-WORK-0936', 1988, 'T6', 'single-work first publication'),
    ('一千英亩.md', 'WL-WORK-0962', 1991, 'T6', 'A Thousand Acres first publication'),
    ('中性.md', 'WL-WORK-0970', 2002, 'T6', 'Middlesex first publication'),
    ('乔纳森·斯特兰奇与诺雷尔先生.md', 'WL-WORK-0572', 2004, 'T6', 'first publication'),
    ('凯恩舰哗变.md', 'WL-WORK-2025', 1951, 'T5', 'The Caine Mutiny first publication'),
    ('北上.md', 'WL-WORK-1007', 2018, 'T6', '北京十月文艺出版社 2018'),
    ('占有.md', 'WL-WORK-1012', 1990, 'T6', 'Possession first publication'),
    ('同情者.md', 'WL-WORK-2034', 2015, 'T6', 'The Sympathizer first publication'),
    ('如此漫长的信.md', 'WL-WORK-2051', 1979, 'T5', 'Une si longue lettre first publication'),
    ('安息角.md', 'WL-WORK-2503', 1971, 'T5', 'Angle of Repose first publication'),
    ('所有我们看不见的光.md', 'WL-WORK-1121', 2014, 'T6', 'All the Light We Cannot See first publication'),
    ('杀戮天使.md', 'WL-WORK-1153', 1974, 'T5', 'The Killer Angels first publication'),
    ('李自成.md', 'WL-WORK-1156', 1999, 'T6', 'five-volume work completed/fully published in 1999'),
    ('狼厅.md', 'WL-WORK-1211', 2009, 'T6', 'Wolf Hall first publication'),
    ('白门柳.md', 'WL-WORK-1223', 1997, 'T6', 'three-part work completed with third part in 1997'),
    ('纯真年代.md', 'WL-WORK-2116', 1920, 'T4', 'The Age of Innocence first publication'),
    ('西行之路.md', 'WL-WORK-2616', 1949, 'T5', 'The Way West first publication'),
    ('飘.md', 'WL-WORK-1330', 1936, 'T4', 'Gone with the Wind first publication'),
]


def frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)(.*)$', text, re.S)
    if not m:
        raise ValueError('missing frontmatter')
    return m.group(1), m.group(2)


def scalar(fm: str, key: str) -> str:
    m = re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$', fm)
    if not m:
        return ''
    v = m.group(1).strip().strip('"\'')
    return '' if v.lower() in {'null', 'none', '~'} else v


def list_field(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if re.match(rf'^{re.escape(key)}:\s*\[\s*\]\s*$', line):
            return []
        if re.match(rf'^{re.escape(key)}:\s*$', line):
            out = []
            for nxt in lines[i + 1:]:
                m = re.match(r'^\s*-\s*(.*?)\s*$', nxt)
                if m:
                    out.append(m.group(1).strip().strip('"\'')); continue
                if re.match(r'^[A-Za-z0-9_\u4e00-\u9fff].*?:', nxt): break
                if nxt.strip() and not nxt.startswith((' ', '\t')): break
            return out
    return []


def replace_scalar(fm: str, key: str, value: str) -> str:
    pat = re.compile(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$')
    if not pat.search(fm):
        raise ValueError(f'missing scalar key {key}')
    return pat.sub(f'{key}: {value}', fm, count=1)


def replace_list(fm: str, key: str, values: list[str]) -> str:
    lines = fm.splitlines()
    start = None
    end = None
    for i, line in enumerate(lines):
        if re.match(rf'^{re.escape(key)}:\s*(?:\[\s*\])?\s*$', line):
            start = i
            end = i + 1
            if line.rstrip().endswith('[]'):
                break
            j = i + 1
            while j < len(lines) and re.match(r'^\s*-\s+', lines[j]):
                j += 1
            end = j
            break
    if start is None:
        raise ValueError(f'missing list key {key}')
    block = [f'{key}:'] + [f'- {v}' for v in values]
    return '\n'.join(lines[:start] + block + lines[end:])


def main() -> None:
    if not MARKER.exists():
        raise SystemExit('P1 completion authorization marker missing')
    AUDIT.mkdir(parents=True, exist_ok=True)

    changed = []
    for filename, expected_id, year, t, rationale in ROWS:
        p = WORKS / filename
        if not p.exists():
            raise SystemExit(f'missing Work: {filename}')
        text = p.read_text(encoding='utf-8-sig')
        fm, body = frontmatter(text)
        if scalar(fm, 'id') != expected_id:
            raise SystemExit(f'id mismatch: {filename}')
        if scalar(fm, 'type') != 'work':
            raise SystemExit(f'not Work: {filename}')
        if scalar(fm, 'year'):
            raise SystemExit(f'year already populated unexpectedly: {filename}')
        if list_field(fm, 'axis_t'):
            raise SystemExit(f'axis_t already populated unexpectedly: {filename}')

        fm2 = replace_scalar(fm, 'year', str(year))
        fm2 = replace_list(fm2, 'axis_t', [T_LABELS[t]])
        p.write_text('---\n' + fm2 + '\n---\n' + body.lstrip('\n'), encoding='utf-8', newline='\n')
        changed.append((filename, expected_id, year, t, rationale))

    # Postconditions.
    for filename, expected_id, year, t, _ in changed:
        fm, _ = frontmatter((WORKS / filename).read_text(encoding='utf-8-sig'))
        if scalar(fm, 'id') != expected_id or scalar(fm, 'year') != str(year):
            raise SystemExit(f'postcondition scalar failure: {filename}')
        if list_field(fm, 'axis_t') != [T_LABELS[t]]:
            raise SystemExit(f'postcondition T failure: {filename}')

    md = [
        '# T-axis Completion P1 V1', '',
        '- Scope: canon/award priority works only',
        f'- Works completed: **{len(changed)}**',
        '- Fields mutated: `year`, `axis_t` only',
        '- R/M/G/Q/topics/priority/history/mechanism: unchanged', '',
        '## Resolutions', '',
        '| Work | ID | canonical year | T | rationale |',
        '|---|---|---:|---|---|',
    ]
    for filename, wid, year, t, rationale in changed:
        md.append(f'| `{filename}` | `{wid}` | {year} | {t} | {rationale} |')
    md += [
        '', '## Policy', '',
        '- Ordinary single works use first publication year.',
        '- Multi-volume/serial works follow the frozen T-axis policy: principal text completion / first complete publication where necessary.',
        '- Exact boundary years would go to the later T period; none of this batch falls on a frozen boundary year.',
        '', '`T_AXIS_COMPLETION_P1_V1 = APPLIED_AND_VERIFIED`', ''
    ]
    REPORT.write_text('\n'.join(md), encoding='utf-8', newline='\n')
    MARKER.unlink()
    print(f'P1_COMPLETED={len(changed)}')


if __name__ == '__main__':
    main()
