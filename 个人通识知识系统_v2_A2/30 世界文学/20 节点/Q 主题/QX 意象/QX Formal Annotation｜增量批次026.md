---
id: WL-QX-FORMAL-ANNOTATION-026
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次026
code: QX-ANNOTATION-026
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次026

> 本批不再只按目录寻找候选，而是重新对照 `R3.5_已读映射收口.xlsx`，专门寻找此前循环遗漏、但当前中央 Work 已经真实存在的单一作品。

## 01｜正式结果

| 作品 | 正式 QX 关系数 | 结论 |
|---|---:|---|
| 《牛虻》 | 1 | 面部伤疤 / 身体残损 |
| 《麦琪的礼物》 | 3 | 德拉的长发；吉姆的金表；发梳 / 表链 |
| 《最后一颗子弹留给我》 | 0 | 军装、枪械、训练场属于军旅通用背景；标题“子弹”不绕过 Gate |

```text
BATCH_026_REVIEWED_EXISTING_WORKS = 3
BATCH_026_WORKS_WITH_FORMAL_QX = 2
BATCH_026_ZERO_QX_WORKS = 1
BATCH_026_FORMAL_RELATIONS = 4
FORMAL_QX_RELATIONS_BEFORE = 354
FORMAL_QX_RELATIONS_AFTER = 358
FORMAL_WORKS_WITH_QX_BEFORE = 115
FORMAL_WORKS_WITH_QX_AFTER = 117
```

## 02｜《牛虻》：标题不是 object

没有把“牛虻”这一题名直接建立为动物意象。

正式准入的是：

```text
面部伤疤 / 身体残损
```

因为流亡后的身体改变稳定参与：

```text
身份遮蔽
身份识别
人物前后变化
旧关系重新认出亚瑟
```

这比由书名反推昆虫象征更符合 QX 的作品内证据要求。

## 03｜《麦琪的礼物》：singular pivotal 可以形成高密度短篇 QX

本篇虽然短，但三个物质对象形成严密结构：

```text
长发 → 被出售
金表 → 被出售
发梳 / 表链 → 因上述出售而暂时失去用途
```

其物质交换直接构成结尾反转，因此无需因为篇幅短而压低 QX 密度。

## 04｜《最后一颗子弹留给我》与《狼牙》保持同一标准

本轮不采用：

```text
子弹
枪械
军装
训练场
```

作为正式 QX。

理由与此前《狼牙》一致：这些元素虽然大量出现，但目前不足以证明某一个具体对象具有作品特有的稳定结构作用。

```text
MILITARY_BACKGROUND ≠ AUTOMATIC_QX
TITLE_BULLET ≠ FORMAL_QX
```

## 05｜上游 Work 建库缺口继续独立登记

重新核对 R3.5 后确认，部分作品当时的明确动作是：

```text
R4创建新Work并标记已读
```

但当前 `feat/qx-literary-imagery` 中仍无法找到对应中央 Work。

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
```

这些项目统一记为：

```text
UPSTREAM_WORK_BUILD_GAP = TRUE
QX_DECISION = NOT_YET_EVALUATED
```

不得计入 QX=0，也不在 QX 阶段临时创建重复 Work。

## 06｜为什么要重新扫审计表

R3.5 明确记录：

```text
文学记录 = 173
确认复用 = 59
新建Work = 105
一对多映射 = 1
特殊项待确认 = 8
```

因此“当前中央 Work 找不到”可能来自 R4 回写不完整，而不是作品未读。

本批发现《牛虻》《麦琪的礼物》就是这种尾部复核价值的反例：它们中央 Work 实际存在，只是此前 QX 连续批次漏过。

## 07｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 358
FORMAL_WORKS_WITH_QX = 117
CORPUS_TAIL_RECONCILIATION = ACTIVE
UPSTREAM_WORK_BUILD_GAP_TRACKING = ACTIVE
FULL_CORPUS_AUDIT = DEFERRED
NEXT_BATCH = 027
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次025]]
