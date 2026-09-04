---
id: WL-QX-FORMAL-ANNOTATION-027
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次027
code: QX-ANNOTATION-027
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次027

> 本批继续以 `R3.5_已读映射收口.xlsx` 为 source of truth，反向核对中央 Work。期间发现并纠正 Batch026 中《麦琪的礼物》阅读粒度误判，因此本批所有累计数均按纠正后的基线重新计算。

## 01｜正式新增

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《人生海海》 | 1 | 下腹刺字 / 纹身 |

```text
BATCH_027_FORMAL_RELATIONS = 1
FORMAL_QX_RELATIONS_BEFORE = 355
FORMAL_QX_RELATIONS_AFTER = 356
FORMAL_WORKS_WITH_QX_BEFORE = 116
FORMAL_WORKS_WITH_QX_AFTER = 117
```

## 02｜《人生海海》：身体秘密作为叙事结构

正式对象：

```text
下腹刺字 / 纹身
```

它满足：

```text
recurrent
character_bound
structural role
stable identity binding
transformative
```

传闻、窥探、遮蔽、批斗暴露与晚年改绘都持续围绕同一身体痕迹展开；因此这里记录的是具体可见身体对象，而不是“创伤”“秘密”“羞耻”等抽象主题。

## 03｜鲁尔福三部曲的一对多阅读记录

R3.5 明确将一条《燃烧的原野：鲁尔福三部曲》阅读记录映射为：

```text
佩德罗·巴拉莫
燃烧的原野
金鸡
```

当前状态：

```text
佩德罗·巴拉莫 = 已有正式 QX
燃烧的原野 = 中央 Work 存在、read_status=已读，但为短篇集，DEFER_STORY_LEVEL
金鸡 = R3.5要求新建 Work，但当前分支未找到，UPSTREAM_WORK_BUILD_GAP
```

不能因为《佩德罗·巴拉莫》已完成就把整套阅读记录视为全部完成。

## 04｜Batch026 粒度纠错

尾部复核确认个人阅读记录实际是：

```text
《麦琪的礼物：欧·亨利短篇小说经典》
```

而非已核实单独阅读短篇《麦琪的礼物》。R3.5 将其判为：

```text
特殊项待确认
编辑型 / 版本型短篇选集
```

因此 Batch026 原写入中央 `麦琪的礼物.md` 的 3 条单篇 QX 已撤回，Batch026 已同步更正为：

```text
116 works / 355 relations
```

本批《人生海海》加入后，当前正式累计为：

```text
117 works / 356 relations
```

## 05｜重新扫描结果

本批重新检查了 R3.5 中段与后段的大量文学记录。已核到的正常单书基本都落入三种状态：

```text
此前已正式标注
此前已明确 QX=0
当前中央 Work 缺失
```

本轮新发现、且满足“中央 Work 已存在 + read_status已读 + 未进入此前批次”的高置信单书只有《人生海海》。这说明 corpus 尾部已经从“批量漏标”逐渐转向“特殊项与上游数据缺口”。

## 06｜当前上游 Work 缺口

已确认至少包括：

```text
盗墓笔记 : 七星鲁王宫
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

统一状态：

```text
UPSTREAM_WORK_BUILD_GAP = TRUE
QX_DECISION = NOT_YET_EVALUATED
```

## 07｜篇章 / 系列级待审队列

当前至少包括：

```text
夜晚的潜水艇
机器人短篇全集
草
人类的群星闪耀时
哑舍
台北人
燃烧的原野
龙族
哈利·波特
福尔摩斯探案全集
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
彷徨
呐喊
俗世奇人（足本）
```

这些不能与 QX=0 混淆。

## 08｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 356
FORMAL_WORKS_WITH_QX = 117
CORPUS_TAIL_RECONCILIATION = ACTIVE
UPSTREAM_WORK_BUILD_GAP_TRACKING = ACTIVE
SPECIAL_ITEM_LEDGER = NEXT
FULL_CORPUS_AUDIT = DEFERRED
NEXT_BATCH = 028
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次026]]
