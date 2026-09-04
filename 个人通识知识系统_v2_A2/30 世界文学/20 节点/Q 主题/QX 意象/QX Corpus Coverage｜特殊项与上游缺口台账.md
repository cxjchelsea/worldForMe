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

> 目的：记录“没有进入 Work-level 正式 QX”的非普通原因。这里的项目不得自动计为 QX=0。

## 01｜状态定义

```text
FORMAL_QX = Work 已核实为实际阅读单元，且至少一条关系通过 Admission Gate
ZERO_QX = Work 已核实为实际阅读单元，也完成 QX 审查，但当前没有对象通过 Gate
DEFER_STORY_LEVEL = 阅读事实对应短篇集 / 多独立叙事，需要篇章级处理
DEFER_SERIES_GRANULARITY = 阅读记录是系列总称或卷级边界尚无法稳定映射
DEFER_EDITORIAL_COLLECTION = 编辑型选集 / 精选，目录依版本变化
ONE_TO_MANY_RECONCILIATION = 一条读书记录实际映射多个 Work
UPSTREAM_WORK_BUILD_GAP = 已读覆盖层要求创建中央 Work，但当前没有可复用 Work
```

## 02｜系列 / 全集粒度

| 读书记录 | 状态 | 当前结论 / QX 下一步 |
|---|---|---|
| 福尔摩斯探案全集 | ONE_TO_MANY_RECONCILIATION | 已完成 4 长篇 +《历险记》12篇 +《回忆录》11篇 +《归来记》13篇，共 40/60；剩余 20 短篇 |
| 哈利·波特 | ONE_TO_MANY_RECONCILIATION | 七册中央 Work 均为已读，7 Work / 21 formal QX；系列粒度闭环 |
| 龙族 | DEFER_SERIES_GRANULARITY | 全集阅读事实已确认，但版本 / 卷级边界仍需恢复 |

## 03｜QX 阶段额外发现的篇章级项目

| 中央 Work / 阅读记录 | 状态 |
|---|---|
| 夜晚的潜水艇 | DEFER_STORY_LEVEL |
| 机器人短篇全集 | DEFER_STORY_LEVEL |
| 草 | DEFER_STORY_LEVEL |
| 人类的群星闪耀时 | DEFER_STORY_LEVEL |
| 哑舍 | DEFER_STORY_LEVEL |
| 台北人 | DEFER_STORY_LEVEL |
| 燃烧的原野 | DEFER_STORY_LEVEL |
| 彷徨 | DEFER_STORY_LEVEL |
| 呐喊 | DEFER_STORY_LEVEL |
| 俗世奇人（足本） | DEFER_STORY_LEVEL |

## 04｜一对多阅读记录

### 《哈利·波特》

```text
7 child Works
7 FORMAL_QX
21 formal relations
HARRY_POTTER_GRANULARITY = CLOSED
```

### 《福尔摩斯探案全集》

```text
4 novels + 56 short stories = 60 independent narrative units
```

已完成：

```text
4 novels → 4 FORMAL_QX / 12 relations
The Adventures of Sherlock Holmes → 12 FORMAL_QX / 19 relations
The Memoirs of Sherlock Holmes → 10 FORMAL_QX + 1 ZERO_QX / 13 relations
The Return of Sherlock Holmes → 12 FORMAL_QX + 1 ZERO_QX / 20 relations
```

ZERO_QX：

```text
住院的病人
失踪的中卫
```

当前：

```text
SHERLOCK_CANON_UNITS = 60
SHERLOCK_UNITS_REVIEWED = 40
SHERLOCK_SHORT_STORIES_REVIEWED = 36
SHERLOCK_SHORT_STORIES_REMAINING = 20
SHERLOCK_FORMAL_QX_WORKS = 38
SHERLOCK_ZERO_QX_WORKS = 2
SHERLOCK_FORMAL_RELATIONS_CURRENT = 64
```

## 05｜上游 Work 建库缺口

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_FORMAL_QX = 7
UPSTREAM_ZERO_QX = 3
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 06｜已纠正的粒度错误

```text
《麦琪的礼物》3 formal relations = REVERTED
reason = COLLECTION_TITLE ≠ VERIFIED_STORY_READ_FACT
```

同名 Work 消歧：

```text
驼背人.md = 保罗·费瓦尔长篇
驼背人（福尔摩斯）.md = 柯南·道尔短篇
```

## 07｜后续处理顺序

```text
1. UPSTREAM_WORK_BUILD_GAP → CLOSED
2. SERIES / VOLUME GRANULARITY
   - 哈利·波特 → CLOSED
   - 福尔摩斯探案全集 → CURRENT / 40 OF 60 REVIEWED
     - 四部长篇 → CLOSED
     - 福尔摩斯历险记 → CLOSED
     - 福尔摩斯回忆录 → CLOSED
     - 福尔摩斯归来记 → CLOSED
     - 最后致意 → NEXT
     - 福尔摩斯案件簿 → PENDING
   - 龙族 → DEFER_VERSION_BOUNDARY
3. 稳定作者短篇集 story-level reading map
4. 编辑型选集版本目录 / 实际读篇
5. story-level QX
6. 重新计算 corpus coverage
```

## 08｜当前正式 QX 基线

```text
FORMAL_WORKS_WITH_QX = 169
FORMAL_QX_RELATIONS = 453
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
```

> ZERO_QX 已完成审查但不进入 FORMAL_WORKS_WITH_QX；系列父记录也不作为独立 QX Work 计数。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次028]]
- [[QX Formal Annotation｜增量批次029]]
- [[QX Formal Annotation｜增量批次030]]
