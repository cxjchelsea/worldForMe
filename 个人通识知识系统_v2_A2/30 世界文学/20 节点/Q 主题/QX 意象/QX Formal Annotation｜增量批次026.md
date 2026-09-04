---
id: WL-QX-FORMAL-ANNOTATION-026
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次026
code: QX-ANNOTATION-026
axis: Q
facet: QX
status: COMPLETE_CORRECTED
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次026

> 本批重新对照 `R3.5_已读映射收口.xlsx` 寻找此前循环遗漏的单一作品。后续尾部复核发现《麦琪的礼物：欧·亨利短篇小说经典》属于编辑型选集，原将其主打篇《麦琪的礼物》当作单篇阅读事实的 3 条 QX 已撤回；以下为更正后的正式状态。

## 01｜更正后的批次结果

| 作品 / 读书记录 | 正式 QX 关系数 | 结论 |
|---|---:|---|
| 《牛虻》 | 1 | 面部伤疤 / 身体残损 |
| 《最后一颗子弹留给我》 | 0 | 军装、枪械、训练场属于军旅通用背景；标题“子弹”不绕过 Gate |
| 《麦琪的礼物：欧·亨利短篇小说经典》 | deferred | 编辑型短篇选集；不能据主打篇名推定《麦琪的礼物》单篇已读 |

```text
BATCH_026_REVIEWED_EXISTING_WORKS = 3
BATCH_026_WORKS_WITH_FORMAL_QX = 1
BATCH_026_ZERO_QX_WORKS = 1
BATCH_026_DEFERRED_COLLECTION = 1
BATCH_026_FORMAL_RELATIONS = 1
FORMAL_QX_RELATIONS_BEFORE = 354
FORMAL_QX_RELATIONS_AFTER = 355
FORMAL_WORKS_WITH_QX_BEFORE = 115
FORMAL_WORKS_WITH_QX_AFTER = 116
```

## 02｜《牛虻》：标题不是 object

没有把“牛虻”这一题名直接建立为动物意象。

正式准入的是：

```text
面部伤疤 / 身体残损
```

因为流亡后的身体改变稳定参与身份遮蔽、身份识别、人物前后变化与旧关系重认。

## 03｜《麦琪的礼物》撤回说明

尾部复核 R3.5 时确认，个人已读记录实际为：

```text
《麦琪的礼物：欧·亨利短篇小说经典》
```

R3.5 的正式结论为：

```text
特殊项待确认
编辑型 / 版本型短篇选集
不等同于单一作者原始作品
```

因此此前挂在中央 `麦琪的礼物.md` 上的：

```text
德拉的长发
吉姆的金表
发梳 / 表链
```

虽然对短篇《麦琪的礼物》本身是合理 QX，但无法由当前个人阅读事实证明该单篇被实际阅读，故全部撤回。

```text
GOOD_QX_FOR_STORY ≠ VERIFIED_READ_RELATION
COLLECTION_TITLE ≠ STORY_READ_FACT
```

## 04｜《最后一颗子弹留给我》与《狼牙》保持同一标准

本轮不采用子弹、枪械、军装、训练场作为正式 QX。它们虽然大量出现，但目前不足以证明某一对象具有作品特有的稳定结构作用。

## 05｜上游 Work 建库缺口

当前已确认至少包括：

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
```

这些统一记为：

```text
UPSTREAM_WORK_BUILD_GAP = TRUE
QX_DECISION = NOT_YET_EVALUATED
```

不得计入 QX=0，也不在 QX 阶段临时创建重复 Work。

## 06｜当前状态（Batch026结束时）

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 355
FORMAL_WORKS_WITH_QX = 116
CORPUS_TAIL_RECONCILIATION = ACTIVE
FULL_CORPUS_AUDIT = DEFERRED
NEXT_BATCH = 027
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次025]]
