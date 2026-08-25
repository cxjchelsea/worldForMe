from pathlib import Path
import re

ROOT = Path('个人通识知识系统_v2_A2/30 世界文学')
WORKS = ROOT / '40 作品'
AUDIT = ROOT / '_audit' / 'entity_dedup'
MARKER = AUDIT / 'APPLY_ENTITY_DEDUP_V1'
REPORT = AUDIT / 'ENTITY_DEDUP_V1.md'

GROUPS = [
    {
        'canonical': '卡特里奥娜.md', 'duplicate': '卡特丽奥娜.md',
        'canonical_id': 'WL-WORK-2469', 'duplicate_id': 'WL-WORK-0614',
        'canonical_title': '卡特里奥娜', 'duplicate_title': '卡特丽奥娜',
        'content': '''---
id: WL-WORK-2469
type: work
title: 卡特里奥娜
title_original: Catriona
aliases:
- Catriona
- 卡特丽奥娜
author: 罗伯特·路易斯·史蒂文森
author_original: Robert Louis Stevenson
author_source: heading
year: 1893
literary_traditions: []
read_status: 未读
axis_t:
- T4 全球现代主义时代
axis_r:
- R4 欧洲文学
axis_m:
- M2 19世纪文学思潮
axis_g:
- G3 小说
axis_q:
- QT5 冒险与探索叙事
- QT8 英雄、边疆与法外者文化传统
- QT8.4 欧洲剑客
axis_source: inferred
topics:
- WL-TOPIC-G45-ADVENTURE
- WL-TOPIC-Q15
- WL-TOPIC-Q15-SWASHBUCKLER
topic_links:
- '[[../30 专题/QT5 冒险与探索叙事/00 冒险文学|冒险文学]]'
- '[[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|世界武人、边疆与法外英雄文学]]'
- '[[../30 专题/QT8.4 欧洲剑客/00 欧洲剑客文学|欧洲剑客文学]]'
adventure_priority: ★
adventure_history_cluster: 科学冒险、Stevenson与Treasure Hunt
adventure_axes: []
martial_systems:
- 欧洲剑客／Swashbuckler
q15_core_compare: false
swashbuckler_priority: ★
swashbuckler_history_stage: 英国Historical Adventure
swashbuckler_axes: []
verification_status: 人工核验
bibliography_status: verified
review_note: '实体去重：卡特丽奥娜与卡特里奥娜均对应 Robert Louis Stevenson 的 Catriona（1893），合并为本唯一 Work。'
batch1_source_refs:
- 冒险书单.md:718
batch6_source_refs:
- 剑客书单.md:645
---
# 卡特里奥娜

## 基本信息

- 原题：Catriona
- 作者：Robert Louis Stevenson
- 首次出版年：1893
- 阅读状态：未读

## 专题位置

- [[../30 专题/QT5 冒险与探索叙事/00 冒险文学|冒险文学]]
- [[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|Q15 世界武人英雄体系]]
- [[../30 专题/QT8.4 欧洲剑客/00 欧洲剑客文学|欧洲剑客文学]]

## 数据说明

> 本文件是中央作品库中的唯一 Work；“卡特丽奥娜”作为异译名保留在 aliases，不再维护第二个作品实体。
'''
    },
    {
        'canonical': '世界尽头的井.md', 'duplicate': "The Well at the World's End.md",
        'canonical_id': 'WL-WORK-0564', 'duplicate_id': 'WL-WORK-2418',
        'canonical_title': '世界尽头的井', 'duplicate_title': "The Well at the World's End",
        'content': '''---
id: WL-WORK-0564
type: work
title: 世界尽头的井
title_original: The Well at the World's End
aliases:
- The Well at the World's End
author: 威廉·莫里斯
author_original: William Morris
author_source: title_map
year: 1896
literary_traditions: []
read_status: 未读
axis_t:
- T4 全球现代主义时代
axis_r:
- R4 欧洲文学
axis_m:
- M2 19世纪文学思潮
axis_g:
- G3 小说
axis_q:
- QT3 奇幻
- QT8 英雄、边疆与法外者文化传统
- QT8.2 欧洲骑士
axis_source: inferred
topics:
- WL-TOPIC-G45-FANTASY
- WL-TOPIC-Q15
- WL-TOPIC-Q15-KNIGHT
topic_links:
- '[[../30 专题/QT3 奇幻/00 奇幻文学|奇幻文学]]'
- '[[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|世界武人、边疆与法外英雄文学]]'
- '[[../30 专题/QT8.2 欧洲骑士/00 欧洲骑士文学|欧洲骑士文学]]'
fantasy_priority: ★
fantasy_history_cluster: 19世纪现代奇幻形成
fantasy_subgenres: []
fantasy_region: []
martial_systems:
- 欧洲骑士
q15_core_compare: false
knight_priority: ★
knight_history_stage: 19世纪中世纪复兴
knight_axes: []
verification_status: 人工核验
bibliography_status: verified
review_note: "实体去重：英文题 The Well at the World's End 与中文《世界尽头的井》为同一 William Morris 1896 年小说，合并为本唯一 Work。"
batch1_source_refs:
- 奇幻书单.md:1860
- 奇幻书单.md:202
batch6_source_refs:
- 骑士书单.md:1194
---
# 世界尽头的井

## 基本信息

- 原题：The Well at the World's End
- 作者：William Morris
- 首次出版年：1896
- 阅读状态：未读

## 专题位置

- [[../30 专题/QT3 奇幻/00 奇幻文学|奇幻文学]]
- [[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|Q15 世界武人英雄体系]]
- [[../30 专题/QT8.2 欧洲骑士/00 欧洲骑士文学|欧洲骑士文学]]

## 数据说明

> 本文件是中央作品库中的唯一 Work；英文题作为 title_original / alias 保留。
'''
    },
    {
        'canonical': '世界彼端的森林.md', 'duplicate': 'The Wood Beyond the World.md',
        'canonical_id': 'WL-WORK-0565', 'duplicate_id': 'WL-WORK-2420',
        'canonical_title': '世界彼端的森林', 'duplicate_title': 'The Wood Beyond the World',
        'content': '''---
id: WL-WORK-0565
type: work
title: 世界彼端的森林
title_original: The Wood Beyond the World
aliases:
- The Wood Beyond the World
author: 威廉·莫里斯
author_original: William Morris
author_source: heading
year: 1894
literary_traditions: []
read_status: 未读
axis_t:
- T4 全球现代主义时代
axis_r:
- R4 欧洲文学
axis_m:
- M2 19世纪文学思潮
axis_g:
- G3 小说
axis_q:
- QT3 奇幻
- QT8 英雄、边疆与法外者文化传统
- QT8.2 欧洲骑士
axis_source: inferred
topics:
- WL-TOPIC-G45-FANTASY
- WL-TOPIC-Q15
- WL-TOPIC-Q15-KNIGHT
topic_links:
- '[[../30 专题/QT3 奇幻/00 奇幻文学|奇幻文学]]'
- '[[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|世界武人、边疆与法外英雄文学]]'
- '[[../30 专题/QT8.2 欧洲骑士/00 欧洲骑士文学|欧洲骑士文学]]'
fantasy_priority: ★
fantasy_history_cluster: 19世纪现代奇幻形成
fantasy_subgenres: []
fantasy_region: []
martial_systems:
- 欧洲骑士
q15_core_compare: false
knight_priority: ★
knight_history_stage: 19世纪中世纪复兴
knight_axes: []
verification_status: 人工核验
bibliography_status: verified
review_note: '实体去重：The Wood Beyond the World 与《世界彼端的森林》为同一 William Morris 1894 年小说，合并为本唯一 Work。'
batch1_source_refs:
- 奇幻书单.md:203
batch6_source_refs:
- 骑士书单.md:1192
---
# 世界彼端的森林

## 基本信息

- 原题：The Wood Beyond the World
- 作者：William Morris
- 首次出版年：1894
- 阅读状态：未读

## 专题位置

- [[../30 专题/QT3 奇幻/00 奇幻文学|奇幻文学]]
- [[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|Q15 世界武人英雄体系]]
- [[../30 专题/QT8.2 欧洲骑士/00 欧洲骑士文学|欧洲骑士文学]]

## 数据说明

> 本文件是中央作品库中的唯一 Work；英文题作为 title_original / alias 保留。
'''
    },
    {
        'canonical': '南方.md', 'duplicate': 'El Sur ／ 南方.md',
        'canonical_id': 'WL-WORK-2468', 'duplicate_id': 'WL-WORK-2213',
        'canonical_title': '南方', 'duplicate_title': 'El Sur / 南方',
        'content': '''---
id: WL-WORK-2468
type: work
title: 南方
title_original: El Sur
aliases:
- El Sur
- El Sur / 南方
author: 博尔赫斯
author_original: Jorge Luis Borges
author_source: title_map
year: 1953
literary_traditions: []
read_status: 未读
axis_t:
- T5 二战后多极文学
axis_r:
- R6 拉丁美洲与加勒比
axis_m:
- M3 现代主义与先锋派
axis_g:
- G3 小说
axis_q:
- QT8 英雄、边疆与法外者文化传统
- QT8.6 Gaucho
- QT8.7 侠盗
axis_source: inferred
topics:
- WL-TOPIC-Q15
- WL-TOPIC-Q15-GAUCHO
- WL-TOPIC-Q15-OUTLAW
topic_links:
- '[[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|世界武人、边疆与法外英雄文学]]'
- '[[../30 专题/QT8.6 Gaucho/00 Gaucho文学|Gaucho文学]]'
- '[[../30 专题/QT8.7 侠盗/00 侠盗文学|侠盗文学]]'
martial_systems:
- Gaucho
- 侠盗／Outlaw Hero
q15_core_compare: false
gaucho_priority: ★
gaucho_history_stage: Borges：重写民族神话
gaucho_axes: []
outlaw_priority: ★
outlaw_tradition_cluster: 阿根廷Gaucho Outlaw
outlaw_axes: []
verification_status: 人工核验
bibliography_status: verified
review_note: '实体去重：El Sur / 南方 与《南方》均对应 Jorge Luis Borges 的 El Sur（1953），合并 Gaucho 与 Outlaw 两套专题属性。'
batch6_source_refs:
- Gaucho书单.md:1749
- Gaucho书单.md:819
- 侠盗书单.md:1151
---
# 南方

## 基本信息

- 原题：El Sur
- 作者：Jorge Luis Borges
- 首次出版年：1953
- 阅读状态：未读

## Q15位置

- [[../30 专题/QT8.6 Gaucho/00 Gaucho文学|Gaucho文学]]
- [[../30 专题/QT8.7 侠盗/00 侠盗文学|侠盗文学]]

## 数据说明

> 本文件是中央作品库中的唯一 Work；Gaucho 与侠盗专题共用本实体。
'''
    },
    {
        'canonical': '结局.md', 'duplicate': 'El fin ／ 结局.md',
        'canonical_id': 'WL-WORK-2597', 'duplicate_id': 'WL-WORK-2204',
        'canonical_title': '结局', 'duplicate_title': 'El fin / 结局',
        'content': '''---
id: WL-WORK-2597
type: work
title: 结局
title_original: El fin
aliases:
- El fin
- El fin / 结局
author: 博尔赫斯
author_original: Jorge Luis Borges
author_source: title_map
year: 1953
literary_traditions: []
read_status: 未读
axis_t:
- T5 二战后多极文学
axis_r:
- R6 拉丁美洲与加勒比
axis_m:
- M3 现代主义与先锋派
axis_g:
- G3 小说
axis_q:
- QT8 英雄、边疆与法外者文化传统
- QT8.6 Gaucho
- QT8.7 侠盗
axis_source: inferred
topics:
- WL-TOPIC-Q15
- WL-TOPIC-Q15-GAUCHO
- WL-TOPIC-Q15-OUTLAW
topic_links:
- '[[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|世界武人、边疆与法外英雄文学]]'
- '[[../30 专题/QT8.6 Gaucho/00 Gaucho文学|Gaucho文学]]'
- '[[../30 专题/QT8.7 侠盗/00 侠盗文学|侠盗文学]]'
martial_systems:
- Gaucho
- 侠盗／Outlaw Hero
q15_core_compare: false
gaucho_priority: ★
gaucho_history_stage: Borges：重写民族神话
gaucho_axes: []
outlaw_priority: ★
outlaw_tradition_cluster: 阿根廷Gaucho Outlaw
outlaw_axes: []
verification_status: 人工核验
bibliography_status: verified
review_note: '实体去重：El fin / 结局 与《结局》均对应 Jorge Luis Borges 的 El fin（1953），合并 Gaucho 与 Outlaw 两套专题属性。'
batch6_source_refs:
- Gaucho书单.md:1748
- Gaucho书单.md:805
- 侠盗书单.md:1145
- 侠盗书单.md:2042
---
# 结局

## 基本信息

- 原题：El fin
- 作者：Jorge Luis Borges
- 首次出版年：1953
- 阅读状态：未读

## Q15位置

- [[../30 专题/QT8.6 Gaucho/00 Gaucho文学|Gaucho文学]]
- [[../30 专题/QT8.7 侠盗/00 侠盗文学|侠盗文学]]

## 数据说明

> 本文件是中央作品库中的唯一 Work；Gaucho 与侠盗专题共用本实体。
'''
    },
    {
        'canonical': 'Tadeo Isidoro Cruz小传.md', 'duplicate': 'Biografía de Tadeo Isidoro Cruz.md',
        'canonical_id': 'WL-WORK-2351', 'duplicate_id': 'WL-WORK-2172',
        'canonical_title': 'Tadeo Isidoro Cruz小传', 'duplicate_title': 'Biografía de Tadeo Isidoro Cruz',
        'content': '''---
id: WL-WORK-2351
type: work
title: Tadeo Isidoro Cruz小传
title_original: Biografía de Tadeo Isidoro Cruz
aliases:
- Biografía de Tadeo Isidoro Cruz
author: 博尔赫斯
author_original: Jorge Luis Borges
author_source: title_map
year: 1949
literary_traditions: []
read_status: 未读
axis_t:
- T5 二战后多极文学
axis_r:
- R6 拉丁美洲与加勒比
axis_m:
- M3 现代主义与先锋派
axis_g:
- G3 小说
axis_q:
- QT8 英雄、边疆与法外者文化传统
- QT8.6 Gaucho
- QT8.7 侠盗
axis_source: inferred
topics:
- WL-TOPIC-Q15
- WL-TOPIC-Q15-GAUCHO
- WL-TOPIC-Q15-OUTLAW
topic_links:
- '[[../30 专题/QT8 英雄、边疆与法外者文化传统/00 世界武人、边疆与法外英雄文学|世界武人、边疆与法外英雄文学]]'
- '[[../30 专题/QT8.6 Gaucho/00 Gaucho文学|Gaucho文学]]'
- '[[../30 专题/QT8.7 侠盗/00 侠盗文学|侠盗文学]]'
martial_systems:
- Gaucho
- 侠盗／Outlaw Hero
q15_core_compare: false
gaucho_priority: ★
gaucho_history_stage: Borges：重写民族神话
gaucho_axes: []
outlaw_priority: ★
outlaw_tradition_cluster: 阿根廷Gaucho Outlaw
outlaw_axes: []
verification_status: 人工核验
bibliography_status: verified
review_note: '实体去重：Biografía de Tadeo Isidoro Cruz 与 Tadeo Isidoro Cruz小传为同一 Jorge Luis Borges 1949 年短篇，合并 Gaucho 与 Outlaw 两套专题属性。'
batch6_source_refs:
- Gaucho书单.md:1747
- Gaucho书单.md:789
- 侠盗书单.md:1141
- 侠盗书单.md:2041
---
# Tadeo Isidoro Cruz小传

## 基本信息

- 原题：Biografía de Tadeo Isidoro Cruz
- 作者：Jorge Luis Borges
- 首次出版年：1949
- 阅读状态：未读

## Q15位置

- [[../30 专题/QT8.6 Gaucho/00 Gaucho文学|Gaucho文学]]
- [[../30 专题/QT8.7 侠盗/00 侠盗文学|侠盗文学]]

## 数据说明

> 本文件是中央作品库中的唯一 Work；西语原题作为 title_original / alias 保留。
'''
    },
]

TEXT_SUFFIXES = {'.md', '.canvas', '.base', '.csv', '.json', '.yaml', '.yml'}


def validate_group(g):
    cp = WORKS / g['canonical']
    dp = WORKS / g['duplicate']
    if not cp.exists() or not dp.exists():
        raise SystemExit(f'missing group file: {cp} or {dp}')
    c = cp.read_text(encoding='utf-8-sig')
    d = dp.read_text(encoding='utf-8-sig')
    if g['canonical_id'] not in c:
        raise SystemExit(f'canonical id mismatch: {cp}')
    if g['duplicate_id'] not in d:
        raise SystemExit(f'duplicate id mismatch: {dp}')


def active_files():
    for p in ROOT.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = p.relative_to(ROOT)
        parts = set(rel.parts)
        if '_source' in parts or '_audit' in parts or p.parent == WORKS:
            continue
        yield p


def replace_references(g):
    changed = 0
    for p in active_files():
        try:
            text = p.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError:
            continue
        new = text.replace(g['duplicate_id'], g['canonical_id'])
        new = new.replace(g['duplicate_title'], g['canonical_title'])
        # Windows-safe filename may use full-width slash while display title uses ASCII slash.
        new = new.replace(Path(g['duplicate']).stem, Path(g['canonical']).stem)
        if new != text:
            p.write_text(new, encoding='utf-8', newline='\n')
            changed += 1
    return changed


def main():
    if not MARKER.exists():
        raise SystemExit('authorization marker missing')
    AUDIT.mkdir(parents=True, exist_ok=True)
    rows = []
    for g in GROUPS:
        validate_group(g)
    for g in GROUPS:
        changed_refs = replace_references(g)
        canonical_path = WORKS / g['canonical']
        canonical_path.write_text(g['content'], encoding='utf-8', newline='\n')
        duplicate_path = WORKS / g['duplicate']
        duplicate_path.unlink()
        rows.append((g['duplicate'], g['canonical'], g['duplicate_id'], g['canonical_id'], changed_refs))

    # Postconditions: duplicate files/IDs must be absent from active repository data.
    leftovers = []
    for g in GROUPS:
        if (WORKS / g['duplicate']).exists():
            leftovers.append(g['duplicate'])
        for p in active_files():
            try:
                text = p.read_text(encoding='utf-8-sig')
            except UnicodeDecodeError:
                continue
            if g['duplicate_id'] in text or Path(g['duplicate']).stem in text:
                leftovers.append(f'{p}: {g["duplicate"]}')
                break
    if leftovers:
        raise SystemExit('unresolved active references: ' + '; '.join(leftovers))

    lines = [
        '# Canonical Work Entity Dedup V1', '',
        '- Confirmed duplicate groups merged: **6**',
        '- Duplicate Work files removed: **6**',
        '- Canonical Work files retained: **6**',
        '- Raw `_source` provenance: unchanged',
        '- Historical `_audit` evidence: unchanged', '',
        '## Merges', '',
        '| Removed duplicate | Canonical Work | ID redirect | Active files rewritten |',
        '|---|---|---|---:|',
    ]
    for dup, can, did, cid, n in rows:
        lines.append(f'| `{dup}` | `{can}` | `{did}` → `{cid}` | {n} |')
    lines += ['', '## Policy', '',
              'Canonicalization is only applied to high-confidence same-work duplicates. Topic-specific metadata is unioned into the surviving Work; alternate translations/original-language titles become aliases/title_original rather than separate Works. Raw source lists remain immutable provenance.', '',
              '`CANONICAL_WORK_ENTITY_DEDUP_V1 = APPLIED_AND_VERIFIED`', '']
    REPORT.write_text('\n'.join(lines), encoding='utf-8', newline='\n')
    MARKER.unlink()


if __name__ == '__main__':
    main()
