---
id: WL-QX-FORMAL-ANNOTATION-029
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次029
code: QX-ANNOTATION-029
axis: Q
facet: QX
status: PARTIAL_UPSTREAM_RECONCILIATION
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次029

> 本批开始执行 Batch028 指定的 `UPSTREAM RECONCILIATION`：先恢复 R3.5 已确认已读、但中央 `40 作品` 缺失的独立 Work，再按现行 Admission Gate 做 QX。不上推其他轴的推断元数据。

## 01｜本组正式计数

```text
BATCH_029_GROUP1_RECOVERED_WORKS = 2
BATCH_029_GROUP1_FORMAL_RELATIONS = 4
FORMAL_QX_RELATIONS_BEFORE = 356
FORMAL_QX_RELATIONS_AFTER = 360
FORMAL_WORKS_WITH_QX_BEFORE = 117
FORMAL_WORKS_WITH_QX_AFTER = 119
```

## 02｜恢复：《你当像鸟飞往你的山》

中央 Work：

```text
40 作品/你当像鸟飞往你的山.md
read_status = 已读
bibliography_status = qx_recovered_minimal
verification_status = 需复核
```

正式 QX：

### 巴克峰 / 山

```text
primary_group = QX6
salience = dominant
Gate = PASS
basis = recurrence + structural/spatial + identity/family binding + distinctiveness
```

巴克峰不是一般自然背景，而是童年家庭世界的固定空间中心；离家求学后，对山的回望继续连接故乡、家庭身份与“是否归返”。

### 废料场

```text
primary_group = QX8
salience = core
Gate = PASS
basis = recurrence + family/labor binding + bodily-risk structure
```

废料场长期组织童年劳动、父权关系与身体风险，因此不是一次性场景。

## 03｜恢复：《苏菲的世界》

中央 Work：

```text
40 作品/苏菲的世界.md
read_status = 已读
bibliography_status = qx_recovered_minimal
verification_status = 需复核
```

正式 QX：

### 书信 / 明信片

```text
qx_id = QX16.1
primary_group = QX16
salience = dominant
Gate = PASS
basis = recurrence + plot/structure + cross-world binding
```

匿名哲学问题信件启动小说，给希尔德的明信片持续制造叙事层级之间的渗透，是结构装置而非普通媒介。

### 书 / 书稿

```text
primary_group = QX16
salience = dominant
Gate = PASS
basis = structural + singular_pivotal + world-state transformation
```

苏菲与艾伯特发现自己存在于希尔德父亲写给女儿的书中；书稿直接改变人物对自身存在层级的理解。

## 04｜上游恢复策略

本批明确采用：

```text
READ FACT
→ 只继承 R3.5 / corpus ledger 已确认的“已读”

BIBLIOGRAPHY
→ 只补可高置信确认的题名、作者、原题、年份

OTHER AXES
→ 不因 QX 修复而顺手推断 T/R/M/QH
→ 无上游证据则留空

QX
→ 必须独立通过 ADMISSION_GATE_V1
```

因此新建 Work 的 `verification_status = 需复核` 不影响 QX 关系本身的 Gate 判断；它表示中央作品库其他维度仍待后续上游治理。

## 05｜剩余 UPSTREAM_WORK_BUILD_GAP

```text
盗墓笔记：七星鲁王宫
临界·爵迹I
我的一个世纪（增订版）
看见
天才在左，疯子在右
盐镇
鱼翅与花椒
金鸡
```

当前剩余：

```text
UPSTREAM_WORK_BUILD_GAP_REMAINING = 8
```

这些项目仍保持：

```text
QX_DECISION = NOT_YET_EVALUATED
DO_NOT_COUNT_AS_ZERO_QX
```

## 06｜下一步

继续 Batch029 第二组，优先处理：

```text
鱼翅与花椒
看见
我的一个世纪（增订版）
天才在左，疯子在右
```

其中若某作品没有对象通过 Gate，应正式落为 `ZERO_QX`，而不是为了完成率强行制造关系。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次028]]
