---
id: WL-QX-CORPUS-COVERAGE-LEDGER
type: literature_qx_governance
name: QX Corpus Coverage｜特殊项与上游缺口台账
axis: Q
facet: QX
status: FINAL_AUDIT_READY
schema: QX_RELATION_SCHEMA_V1
---

# QX Corpus Coverage｜特殊项与上游缺口台账

> 目的：记录个人已读书目在 QX 中的完成状态。QX 完成性是“每条已读记录都已判断是否值得进入意象系统”，而不是“所有短篇都必须逐篇抽取”。

## 01｜完成状态定义

```text
FORMAL_QX
= 需要 QX，且至少一个对象通过 Admission Gate

ZERO_QX
= 需要作品级审查，但没有对象达到正式门槛

FORMAL_QX_SERIES_SCOPE
= 全系列阅读事实明确，但分卷边界不稳定；只记录跨卷稳定意象

FORMAL_QX_SCOPE_INVARIANT
= 具体阅读范围不完整；只记录对任何已知阅读范围都稳定成立的核心意象

REVIEWED_NO_QX_REQUIRED
= 已判断该阅读记录不值得为了 QX 完整性继续拆篇 / 恢复版本目录
```

以下不再视为覆盖缺口：

```text
ZERO_QX
REVIEWED_NO_QX_REQUIRED
```

## 02｜系列 / 全集粒度

| 读书记录 | 最终状态 | 当前结论 |
|---|---|---|
| 福尔摩斯探案全集 | CLOSED | 60 units；58 FORMAL_QX + 2 ZERO_QX / 91 relations |
| 哈利·波特 | CLOSED | 7 child Works / 21 relations |
| 龙族 | FORMAL_QX_SERIES_SCOPE | 全集已读；仅保留黄金瞳、卡塞尔学院、尼伯龙根 3 条跨卷稳定关系 |
| 哑舍 | FORMAL_QX_SCOPE_INVARIANT | 卷级范围未知；仅保留范围无关的“哑舍古董店”1条关系 |

```text
SERIES_RECONCILIATION = CLOSED_FOR_QX
```

## 03｜已完成的稳定短篇集

| 父级阅读记录 | 结果 |
|---|---|
| 呐喊 | 14 = 12 FORMAL + 2 ZERO / 21 relations |
| 彷徨 | 11 = 7 FORMAL + 4 ZERO / 10 relations |
| 台北人 | 14 = 10 FORMAL + 4 ZERO / 11 relations |
| 燃烧的原野 | 17 = 10 FORMAL + 7 ZERO / 13 relations |
| 夜晚的潜水艇 | 9 = 7 FORMAL + 2 ZERO / 8 relations |
| 机器人短篇全集 | 32 = 22 FORMAL + 10 ZERO / 24 relations |

```text
STORY_UNITS_REVIEWED = 97
STORY_FORMAL_QX_WORKS = 68
STORY_ZERO_QX_WORKS = 29
STORY_FORMAL_RELATIONS = 87
```

## 04｜已审查但无需继续拆分的已读记录

### 历史小品 / 摘录 / 多人物短篇集合

```text
人类的群星闪耀时
→ REVIEWED_NO_QX_REQUIRED_COLLECTION

草
→ REVIEWED_NO_QX_REQUIRED_EXCERPT_COLLECTION

俗世奇人（足本）
→ REVIEWED_NO_QX_REQUIRED_SHORT_FORM_COLLECTION
```

### 编辑型外国短篇选集

```text
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
```

统一状态：

```text
REVIEWED_NO_QX_REQUIRED_EDITORIAL_COLLECTION
```

理由：这些书的价值不在于为 QX 恢复每个版本的完整目录；若未来某篇独立短篇因个人阅读重要性或强意象进入专题，可单篇追加，不影响当前已读覆盖完成性。

## 05｜上游建库缺口

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 06｜短篇选择性规则

```text
SHORT_FORM_DEFAULT = SELECTIVE_REVIEW
SHORT_STORY ≠ MANDATORY_QX_UNIT
EDITORIAL_COLLECTION ≠ MANDATORY_STORY_MAP
ZERO_QX_SHORT_STORY ≠ COVERAGE_GAP
```

短篇只有在以下情况下优先独立进入 QX：

```text
1. 存在 dominant / core 级高辨识物象
2. 具体物象明显承担结构作用
3. 具有跨作品比较价值
4. 本身是个人阅读中的重要独立作品
```

## 07｜当前正式 QX 基线

截至 Batch031 关闭：

```text
FORMAL_WORKS_WITH_QX = 259
FORMAL_QX_RELATIONS = 571
STORY_LEVEL_UNITS_REVIEWED_BATCH031 = 97
STORY_LEVEL_FORMAL_QX_WORKS_BATCH031 = 68
STORY_LEVEL_ZERO_QX_BATCH031 = 29
STORY_LEVEL_NEW_RELATIONS_BATCH031 = 87
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
```

## 08｜当前缺口判断

```text
UNRESOLVED_NORMAL_SINGLE_WORK = 0
UNRESOLVED_UPSTREAM_WORK_GAP = 0
UNRESOLVED_MANDATORY_SHORT_FORM = 0
UNRESOLVED_MANDATORY_SERIES_QX = 0
```

因此：

```text
READ_CORPUS_QX_REVIEW = READY_FOR_FINAL_RECOUNT
```

下一步只做最终全量审计：确认个人已读记录中不存在遗漏的普通单本 Work，并检查所有特殊项都已落入上述完成状态之一。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次030]]
- [[QX Formal Annotation｜增量批次031]]
- [[QX Version Reconciliation｜版本阻塞项证据台账]]
