---
id: WL-QX-FORMAL-ANNOTATION-025
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次025
code: QX-ANNOTATION-025
axis: Q
facet: QX
status: COMPLETE_NO_NEW_RELATIONS
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次025

> 本批进入 corpus 尾部特殊项清理。目标不是继续提高关系数量，而是把无法直接按 Work-level QX 处理的已读记录分型，避免后续误把系列、选集、合集或缺失 Work 当成 QX=0。

## 01｜本批结果

```text
BATCH_025_FORMAL_RELATIONS = 0
FORMAL_QX_RELATIONS_BEFORE = 354
FORMAL_QX_RELATIONS_AFTER = 354
FORMAL_WORKS_WITH_QX_BEFORE = 115
FORMAL_WORKS_WITH_QX_AFTER = 115
```

## 02｜系列总称：不做整系列 QX

### 《龙族》

当前中央 Work 存在且 `read_status: 已读`，但历史已读审计将其标为系列总称，具体已读卷缺乏稳定粒度。

```text
DECISION = DEFER_SERIES_GRANULARITY
```

原因：

- 不同卷存在不同主要空间、器物和角色绑定；
- 直接给“龙族”总称挂 QX 会制造“读过全部系列”的假事实；
- 后续应先恢复卷级阅读事实，再按卷或明确的长篇单元标注。

同类：

```text
哈利·波特
福尔摩斯探案全集
```

其中后两者当前分支按系列 / 全集标题未解析为单一中央 Work，本身也不应为了 QX 临时创建总实体。

## 03｜多独立叙事 / 选集 / 文集：延期到篇章级

已经确认进入篇章级待审队列：

```text
夜晚的潜水艇
机器人短篇全集
草
人类的群星闪耀时
哑舍
台北人
```

以及已读审计中的编辑型或多篇集合候选：

```text
福尔摩斯探案全集
欧·亨利短篇小说选 / 精选
莫泊桑短篇小说精选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
彷徨
呐喊
俗世奇人（足本）
```

这些记录后续应区分：

```text
稳定作者文集
编辑型选集
短篇小说集
系列总称
单篇作品
```

再决定是否建立 collection / story-level QX。

## 04｜中央 Work 缺失 / 路径未解析

截至本批，已读审计中明确属于文学地图、但当前 `feat/qx-literary-imagery` 无法按标准化标题取得 Work 的候选包括：

```text
盗墓笔记：七星鲁王宫
临界·爵迹I
我的一个世纪
你当像鸟飞往你的山
看见
天才在左，疯子在右
盐镇
鱼翅与花椒
```

```text
DECISION = CENTRAL_WORK_MISSING_OR_PATH_UNRESOLVED
QX_DECISION = NOT_YET_EVALUATED
```

注意：这类作品不能计入 QX=0。

## 05｜为什么尾部批次允许 0 新关系

到这一阶段，继续强行追求“每批新增关系”会产生三个风险：

1. 把系列总称误当单一作品；
2. 把短篇合集中的单篇意象提升成整本对象；
3. 因中央 Work 路径缺失而重复创建实体。

因此 corpus coverage 的完成度必须同时记录：

```text
FORMAL_QX
ZERO_QX
DEFERRED_COLLECTION_OR_SERIES
CENTRAL_WORK_UNRESOLVED
```

而不能只看 `FORMAL_WORKS_WITH_QX`。

## 06｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 354
FORMAL_WORKS_WITH_QX = 115
CORPUS_TAIL_TRIAGE = ACTIVE
FULL_CORPUS_AUDIT = DEFERRED
NEXT_STEP = RESOLVE_UNREVIEWED_SINGLE_WORKS + SPECIAL_ITEM_LEDGER
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次024]]
