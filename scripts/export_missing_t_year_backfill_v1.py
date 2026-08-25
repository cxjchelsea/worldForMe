from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS = ROOT / '40 作品'
AUDIT = ROOT / '_audit/t_axis_year_backfill'
MARKER = AUDIT / 'RUN_MISSING_T_YEAR_BACKFILL_EXPORT_V1'
OUT = AUDIT / 'missing_t_year_backfill_v1.csv'
REPORT = AUDIT / 'README.md'

T_LABELS = {
    'T0': 'T0 文学源头与古代文学',
    'T1': 'T1 中古多中心文学世界',
    'T2': 'T2 早期现代文学',
    'T3': 'T3 19世纪现代文学体系',
    'T4': 'T4 全球现代主义时代',
    'T5': 'T5 二战后多极文学',
    'T6': 'T6 当代全球文学',
}
LABEL_TO_T = {v: k for k, v in T_LABELS.items()}


def frontmatter(text: str) -> str:
    if not text.startswith('---'):
        return ''
    m = re.match(r'^---\s*\n(.*?)\n---(?:\s*\n|$)', text, re.S)
    return m.group(1) if m else ''


def scalar(fm: str, key: str) -> str:
    m = re.search(rf'(?m)^{re.escape(key)}:\s*(.*?)\s*$', fm)
    if not m:
        return ''
    v = m.group(1).strip()
    if v.lower() in {'null','none','~'}:
        return ''
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v


def list_field(fm: str, key: str) -> list[str]:
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        inline = re.match(rf'^{re.escape(key)}:\s*\[(.*?)\]\s*$', line)
        if inline:
            raw = inline.group(1).strip()
            return [] if not raw else [x.strip().strip("\"'") for x in raw.split(',')]
        if re.match(rf'^{re.escape(key)}:\s*$', line):
            out = []
            for nxt in lines[i+1:]:
                m = re.match(r'^\s*-\s*(.*?)\s*$', nxt)
                if m:
                    out.append(m.group(1).strip().strip("\"'")); continue
                if nxt and not nxt.startswith((' ','\t')):
                    break
            return out
    return []


def main() -> None:
    if not MARKER.exists():
        raise SystemExit('authorization marker missing')
    AUDIT.mkdir(parents=True, exist_ok=True)
    rows = []
    for p in sorted(WORKS.glob('*.md'), key=lambda x: x.name.casefold()):
        text = p.read_text(encoding='utf-8-sig')
        fm = frontmatter(text)
        if not fm or scalar(fm, 'type') != 'work':
            continue
        axis_t = list_field(fm, 'axis_t')
        valid = [LABEL_TO_T[x] for x in axis_t if x in LABEL_TO_T]
        if valid:
            continue
        rows.append({
            'file': p.name,
            'id': scalar(fm,'id'),
            'title': scalar(fm,'title') or p.stem,
            'title_original': scalar(fm,'title_original'),
            'author': scalar(fm,'author'),
            'author_original': scalar(fm,'author_original'),
            'current_year': scalar(fm,'year'),
            'topics': ';'.join(list_field(fm,'topics')),
            'topic_links': ';'.join(list_field(fm,'topic_links')),
            'source_refs': ';'.join(list_field(fm,'source_refs')),
            'source_ref_keys': ';'.join(list_field(fm,'source_ref_keys')),
            'canon_id': scalar(fm,'canon_id'),
            'awards': ';'.join(list_field(fm,'awards')),
            'verification_status': scalar(fm,'verification_status'),
            'bibliography_status': scalar(fm,'bibliography_status'),
            'publication_year': '',
            'publication_year_type': '',
            'year_source_1': '',
            'year_source_2': '',
            'source_agreement': '',
            'confidence': '',
            'suggested_t': '',
            'review_status': 'UNRESEARCHED',
            'notes': '',
        })
    fields = list(rows[0].keys()) if rows else []
    with OUT.open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    REPORT.write_text(
        '# Missing-T Year Backfill V1\n\n'
        f'- Exported unresolved canonical Works: **{len(rows)}**\n'
        '- This export is read-only; no Work file was modified.\n'
        '- `publication_year` must represent work-level first publication / first appearance / defensible formation-completion year, not a modern reprint date.\n'
        '- Rows will be researched in batches and classified HIGH / MEDIUM / REVIEW before any canonical write-back.\n\n'
        '`MISSING_T_YEAR_BACKFILL_EXPORT_V1 = EXPORTED_READ_ONLY`\n',
        encoding='utf-8'
    )
    MARKER.unlink()
    print(f'EXPORTED={len(rows)}')

if __name__ == '__main__':
    main()
