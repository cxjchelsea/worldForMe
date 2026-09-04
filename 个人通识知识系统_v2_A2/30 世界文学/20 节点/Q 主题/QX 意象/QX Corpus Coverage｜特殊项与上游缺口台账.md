---
id: WL-QX-CORPUS-COVERAGE-LEDGER
type: literature_qx_governance
name: QX Corpus Coverage｜特殊项与上游缺口台账
axis: Q
facet: QX
status: ACTIVE
schema: QX_RELATION_SCHEMA_V1
---

# QX Corpus Coverage｜特殊项与上游缺口台账

> 目的：记录没有直接进入 Work-level 正式 QX 的特殊粒度、版本与上游原因，并维护当前审查断点。

## 01｜系列 / 全集粒度

| 读书记录 | 状态 | 当前结论 |
|---|---|---|
| 福尔摩斯探案全集 | CLOSED | 60 units；58 FORMAL_QX + 2 ZERO_QX / 91 relations |
| 哈利·波特 | CLOSED | 7 child Works / 21 relations |
| 龙族 | DEFER_VERSION_BOUNDARY | 系列已读事实保留；版本 / 卷级边界不足；NON-BLOCKING |
| 哑舍 | DEFER_SERIES_GRANULARITY | 中央记录只有系列父名，没有具体卷；禁止给系列父节点挂跨卷 QX |

## 02｜稳定作者短篇集 / 文集

| 父级阅读记录 | 当前状态 | story-level 结果 |
|---|---|---|
| 呐喊 | CLOSED | 14 = 12 FORMAL + 2 ZERO / 21 relations |
| 彷徨 | CLOSED | 11 = 7 FORMAL + 4 ZERO / 10 relations |
| 台北人 | CLOSED | 14 = 10 FORMAL + 4 ZERO / 11 relations |
| 燃烧的原野 | CLOSED | 17 = 10 FORMAL + 7 ZERO / 13 relations |
| 夜晚的潜水艇 | CLOSED | 9 = 7 FORMAL + 2 ZERO / 8 relations |
| 机器人短篇全集 | CLOSED | 32 = 22 FORMAL + 10 ZERO / 24 relations |

## 03｜版本 / 结构延期项

| 阅读记录 | 状态 | 原因 |
|---|---|---|
| 人类的群星闪耀时 | DEFER_COLLECTION_VERSION | 历史上存在5 / 12 / 14篇等不同版本；个人记录无出版社 / ISBN / 目录 |
| 草 | DEFER_EXCERPT_COLLECTION | 实为从《一座城池》《光荣日》《他的国》《杂的文》摘取片段的精选集，不是独立短篇集 |
| 俗世奇人 / 俗世奇人（足本） | DEFER_COLLECTION_VERSION | 中央父名与已读覆盖层版本名不一致；旧版、足本、新增本篇目边界不同 |
| 龙族 | DEFER_VERSION_BOUNDARY | 网文、单行本、修订与重写边界不稳定 |
| 哑舍 | DEFER_SERIES_GRANULARITY | 具体卷级阅读事实缺失 |

```text
DEFERRED_ITEMS_ARE_REVIEWED_FOR_GRANULARITY = TRUE
DEFERRED_ITEMS_DO_NOT_BLOCK_STABLE_CORPUS = TRUE
```

## 04｜编辑型选集：仍需版本目录

```text
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
```

统一状态：`DEFER_EDITORIAL_COLLECTION`。

## 05｜上游 Work 建库缺口

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 06｜当前处理顺序

```text
1. SERIES / VOLUME GRANULARITY
   - 哈利·波特 → CLOSED
   - 福尔摩斯探案全集 → CLOSED
   - 龙族 → DEFER_VERSION_BOUNDARY / NON-BLOCKING
   - 哑舍 → DEFER_SERIES_GRANULARITY / NON-BLOCKING
2. STORY-LEVEL READING MAP
   - 呐喊 → CLOSED
   - 彷徨 → CLOSED
   - 台北人 → CLOSED
   - 燃烧的原野 → CLOSED
   - 夜晚的潜水艇 → CLOSED
   - 机器人短篇全集 → CLOSED
3. VERSION / TOC RECONCILIATION
   - 人类的群星闪耀时
   - 草
   - 俗世奇人（足本）
4. EDITORIAL COLLECTION RECONCILIATION
5. FINAL CORPUS COVERAGE RECOUNT
```

## 07｜当前正式 QX 基线

截至 Batch031《机器人短篇全集》收口：

```text
FORMAL_WORKS_WITH_QX = 257
FORMAL_QX_RELATIONS = 567
STORY_LEVEL_UNITS_REVIEWED_BATCH031 = 97
STORY_LEVEL_FORMAL_QX_WORKS_BATCH031 = 68
STORY_LEVEL_ZERO_QX_BATCH031 = 29
STORY_LEVEL_NEW_RELATIONS_BATCH031 = 87
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
```

> ZERO_QX 已完成审查但不进入 FORMAL_WORKS_WITH_QX；父级 collection / series 也不作为独立 QX Work 计数；DEFERRED 表示粒度审查已完成但版本事实不足。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次030]]
- [[QX Formal Annotation｜增量批次031]]
