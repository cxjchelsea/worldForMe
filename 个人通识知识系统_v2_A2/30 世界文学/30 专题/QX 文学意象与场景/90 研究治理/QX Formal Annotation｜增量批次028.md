---
id: WL-QX-FORMAL-ANNOTATION-028
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次028
code: QX-ANNOTATION-028
axis: Q
facet: QX
status: COMPLETE_NO_NEW_RELATIONS
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次028

> 本批不新增正式关系，完成 corpus 尾部特殊项与上游 Work 缺口的治理性收口，并创建长期台账 [[QX Corpus Coverage｜特殊项与上游缺口台账]]。

## 01｜本批正式计数

```text
BATCH_028_FORMAL_RELATIONS = 0
FORMAL_QX_RELATIONS_BEFORE = 356
FORMAL_QX_RELATIONS_AFTER = 356
FORMAL_WORKS_WITH_QX_BEFORE = 117
FORMAL_WORKS_WITH_QX_AFTER = 117
```

## 02｜R3.5 特殊待确认 8 条全部进入台账

分为：

```text
SERIES / COMPLETE-CORPUS GRANULARITY = 3
EDITORIAL COLLECTION = 5
```

系列 / 全集：

```text
福尔摩斯探案全集
哈利·波特
龙族
```

编辑型短篇选集：

```text
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
```

这些均不得计入 QX=0。

## 03｜QX 阶段额外形成 story-level queue

当前至少包括：

```text
夜晚的潜水艇
机器人短篇全集
草
人类的群星闪耀时
哑舍
台北人
燃烧的原野
彷徨
呐喊
俗世奇人（足本）
```

后续必须先建立或恢复独立篇章阅读事实，再标 QX。

## 04｜上游 Work 缺口

当前至少确认：

```text
盗墓笔记：七星鲁王宫
临界·爵迹I
我的一个世纪（增订版）
你当像鸟飞往你的山
看见
天才在左，疯子在右
盐镇
鱼翅与花椒
苏菲的世界
金鸡
```

这些作品在已读审计中存在，但当前分支没有可复用中央 Work。

```text
QX_DECISION = NOT_YET_EVALUATED
```

## 05｜本轮 corpus reconciliation 的重要纠错

此前错误：

```text
《麦琪的礼物：欧·亨利短篇小说经典》
→ 被误当成单篇《麦琪的礼物》
→ 写入 3 条 QX
```

现已撤销，并将 Batch026 和后续累计全部重新计算。

当前正确基线：

```text
FORMAL_WORKS_WITH_QX = 117
FORMAL_QX_RELATIONS = 356
```

## 06｜当前阶段判断

经过 Batch014—028 的连续循环，普通的：

```text
中央 Work 已存在
read_status = 已读
单一作品粒度
尚未进入 QX 审查
```

这类漏项已经显著减少，尾部剩余主要由：

```text
collection / anthology
series granularity
one-to-many reading record
upstream Work build gap
```

构成。

因此继续“只扫描 40 作品目录”已经不是高收益路径。

## 07｜下一阶段入口

```text
Stage 1: 修复 UPSTREAM_WORK_BUILD_GAP
Stage 2: 恢复 series / anthology / collection 阅读粒度
Stage 3: story-level / volume-level QX
Stage 4: 重新计算 173 条文学阅读记录的覆盖状态
Stage 5: 全量 Object / Function / Topic audit
```

这仍然属于“先完成 corpus coverage，再做 ontology 全审计”的原定战略，并不改变 QX schema。

## 08｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 356
FORMAL_WORKS_WITH_QX = 117
NORMAL_SINGLE_WORK_LOOP = NEAR_EXHAUSTED
SPECIAL_ITEM_LEDGER = ACTIVE
UPSTREAM_WORK_BUILD_GAP_TRACKING = ACTIVE
FULL_CORPUS_AUDIT = DEFERRED
NEXT_BATCH = 029 / UPSTREAM RECONCILIATION
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次027]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
