---
id: WL-QX-CORPUS-COVERAGE-LEDGER
type: literature_qx_governance
name: QX Corpus Coverage｜特殊项与上游缺口台账
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
---

# QX Corpus Coverage｜特殊项与上游缺口台账

> 目的：记录个人已读书目在 QX 中的完成状态。QX 完成性是“每条已读记录都已判断是否值得进入意象系统”，而不是“所有短篇都必须逐篇抽取”。

## 01｜已读覆盖最终底数

```text
DEDUP_READ_RECORDS_TOTAL = 190
LITERARY_READ_RECORDS = 173
NON_LITERARY_READ_RECORDS = 17
```

```text
LITERARY_READ_RECORDS_QX_DISPOSITIONED = 173
LITERARY_READ_RECORD_COVERAGE = 173 / 173 = 100%
ACTIONABLE_READ_CORPUS_QX_GAPS = 0
```

17 条非文学 / 知识类记录属于个人通识阅读史，不进入世界文学 QX：

```text
NON_LITERARY_QX_REQUIRED = 0
```

## 02｜完成状态定义

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

以下均属于完成状态：

```text
FORMAL_QX
ZERO_QX
FORMAL_QX_SERIES_SCOPE
FORMAL_QX_SCOPE_INVARIANT
REVIEWED_NO_QX_REQUIRED
```

## 03｜系列 / 全集粒度

| 读书记录 | 最终状态 | 当前结论 |
|---|---|---|
| 福尔摩斯探案全集 | CLOSED | 60 units；58 FORMAL_QX + 2 ZERO_QX / 91 relations |
| 哈利·波特 | CLOSED | 7 child Works / 21 relations |
| 龙族 | FORMAL_QX_SERIES_SCOPE | 全集已读；黄金瞳、卡塞尔学院、尼伯龙根 3 条跨卷稳定关系 |
| 哑舍 | FORMAL_QX_SCOPE_INVARIANT | 卷级范围未知；仅保留“哑舍古董店”1条范围无关关系 |

```text
SERIES_RECONCILIATION = CLOSED_FOR_QX
```

## 04｜已完成的稳定短篇集

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

## 05｜已审查但无需继续拆分的已读记录

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

若未来其中某个独立短篇因个人阅读重要性或强意象进入专题，可单篇追加，不影响当前已读覆盖完成性。

## 06｜短篇选择性规则

```text
SHORT_FORM_DEFAULT = SELECTIVE_REVIEW
SHORT_STORY ≠ MANDATORY_QX_UNIT
EDITORIAL_COLLECTION ≠ MANDATORY_STORY_MAP
ZERO_QX_SHORT_STORY ≠ COVERAGE_GAP
```

短篇优先进入 QX 的条件：

```text
1. 存在 dominant / core 级高辨识物象
2. 具体物象明显承担结构作用
3. 具有跨作品比较价值
4. 本身是个人阅读中的重要独立作品
```

## 07｜上游 Work 建库缺口

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 08｜当前正式 QX 数据规模

```text
FORMAL_WORKS_WITH_QX = 259
FORMAL_QX_RELATIONS = 571
```

注意：

```text
259 ≠ 173
```

259 是正式拥有 QX 的 Work 数，包含从系列、短篇集拆出的独立叙事 Work；173 才是个人文学已读记录的覆盖分母。

## 09｜最终结论

```text
UNRESOLVED_NORMAL_SINGLE_WORK = 0
UNRESOLVED_UPSTREAM_WORK_GAP = 0
UNRESOLVED_MANDATORY_SHORT_FORM = 0
UNRESOLVED_MANDATORY_SERIES_QX = 0
ACTIONABLE_READ_CORPUS_QX_GAPS = 0
```

> **个人 173 条文学已读记录已经全部完成 QX 层处置：需要抽取的已经抽取；没有对象达到 Gate 的记录允许 ZERO_QX；不值得为 QX 继续拆分的短篇 / 选集已明确归为 REVIEWED_NO_QX_REQUIRED。**

后续不再以“补已读覆盖”为目标，而转入：

```text
normalized object 去重
→ 叶节点激活
→ 跨作品意象专题
→ imagery constellation / work distance
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次030]]
- [[QX Formal Annotation｜增量批次031]]
- [[QX Version Reconciliation｜版本阻塞项证据台账]]
- [[QX Final Audit｜已读书目全量收口]]
