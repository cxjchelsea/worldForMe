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
| 龙族 | DEFER_VERSION_BOUNDARY | 系列已读事实保留；个人材料不足以确定网文 / 单行本 / 修订重写卷级边界；NON-BLOCKING |

## 02｜稳定作者短篇集 / 文集

| 父级阅读记录 | 当前状态 | story-level 结果 |
|---|---|---|
| 呐喊 | CLOSED | 14 = 12 FORMAL + 2 ZERO / 21 relations |
| 彷徨 | CLOSED | 11 = 7 FORMAL + 4 ZERO / 10 relations |
| 台北人 | CLOSED | 14 = 10 FORMAL + 4 ZERO / 11 relations |
| 燃烧的原野 | CLOSED | 17 = 10 FORMAL + 7 ZERO / 13 relations |
| 夜晚的潜水艇 | CLOSED | 9 = 7 FORMAL + 2 ZERO / 8 relations |
| 人类的群星闪耀时 | CURRENT | 多独立历史叙事，待 story-level map |
| 机器人短篇全集 | PENDING | 需先稳定具体篇目边界 |
| 草 | PENDING | 文集粒度待恢复 |
| 哑舍 | PENDING | 连缀式器物故事 |
| 俗世奇人（足本） | PENDING | 多人物独立故事 |

## 03｜已闭环的一对多记录

```text
哈利·波特 = CLOSED
福尔摩斯探案全集 = CLOSED
呐喊 = CLOSED
彷徨 = CLOSED
台北人 = CLOSED
燃烧的原野 = CLOSED
夜晚的潜水艇 = CLOSED
```

## 04｜上游 Work 建库缺口

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 05｜编辑型选集：仍需版本目录

```text
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
```

统一状态：`DEFER_EDITORIAL_COLLECTION`。

## 06｜当前处理顺序

```text
1. SERIES / VOLUME GRANULARITY
   - 哈利·波特 → CLOSED
   - 福尔摩斯探案全集 → CLOSED
   - 龙族 → DEFER_VERSION_BOUNDARY / NON-BLOCKING
2. STORY-LEVEL READING MAP
   - 呐喊 → CLOSED
   - 彷徨 → CLOSED
   - 台北人 → CLOSED
   - 燃烧的原野 → CLOSED
   - 夜晚的潜水艇 → CLOSED
   - 人类的群星闪耀时 → CURRENT
3. 其余稳定 / 半稳定文集逐项恢复
4. 编辑型选集版本目录 / 实际读篇
5. 最终 corpus coverage recount
```

## 07｜当前正式 QX 基线

截至 Batch031《夜晚的潜水艇》收口：

```text
FORMAL_WORKS_WITH_QX = 235
FORMAL_QX_RELATIONS = 543
STORY_LEVEL_UNITS_REVIEWED_BATCH031 = 65
STORY_LEVEL_FORMAL_QX_WORKS_BATCH031 = 46
STORY_LEVEL_ZERO_QX_BATCH031 = 19
STORY_LEVEL_NEW_RELATIONS_BATCH031 = 63
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
```

> ZERO_QX 已完成审查但不进入 FORMAL_WORKS_WITH_QX；父级 collection 和 series 也不作为独立 QX Work 计数。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次030]]
- [[QX Formal Annotation｜增量批次031]]
