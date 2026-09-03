---
id: WL-QX-FORMAL-ANNOTATION-011
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次011
code: QX-ANNOTATION-011
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 1Q84
  - 1988：我想和这个世界谈谈
  - 82年生的金智英
  - 24个比利
---

# QX Formal Annotation｜增量批次011

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。执行原则不变：只处理已读作品；作品之间不追求关系数均衡；抽象主题不得替代可感知对象；宁可少标，不为凑数降低 Admission Gate。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《1Q84》 | 3 | 月亮；首都高速公路紧急楼梯；空气蛹 |
| 《1988：我想和这个世界谈谈》 | 3 | 旅行车 / 1988；公路 / 国道；录音笔 |
| 《82年生的金智英》 | 1 | 声音 / 口吻 |
| 《24个比利》 | 2 | 意识大厅与聚光灯；身体 |

```text
BATCH_011_WORKS = 4
BATCH_011_FORMAL_RELATIONS = 9
FORMAL_QX_RELATIONS_BEFORE = 172
FORMAL_QX_RELATIONS_AFTER = 181
FORMAL_WORKS_WITH_QX_BEFORE = 44
FORMAL_WORKS_WITH_QX_AFTER = 48
```

---

## 02｜《1Q84》：用可见世界标志承载“现实偏移”

本批没有直接标注：

```text
平行世界
命运
爱情
宗教控制
```

这些仍属于 QH / QC 等解释层。

QX 保留的是作品把异常世界变得可感知的三个具体对象：

```text
两个月亮
首都高速公路紧急楼梯
空气蛹
```

其中：

- 两个月亮是反复可见的世界状态标志；
- 紧急楼梯是青豆从常规交通秩序中脱离并进入异常叙事阶段的阈限路径；
- 空气蛹使文本内部的超自然叙述进入人物现实，承担持续的世界规则与情节功能。

因此本批保持：

```text
ABSTRACT_ALTERNATE_WORLD = DROP_FROM_QX
PERCEPTIBLE_WORLD_MARKERS = KEEP
```

---

## 03｜《1988》：公路叙事必须落到移动载体与媒介

作品的“在路上”“成长”“寻找”没有直接作为 QX 对象。

正式保留：

```text
旅行车 / 1988
公路 / 国道
录音笔
```

旅行车与道路共同组织现实时间线：

```text
移动
→ 相遇与同行
→ 沿途场景
→ 记忆切换
```

而结尾的录音笔属于 `singular_pivotal` 型关系：娜娜遗留的声音在两年后重新进入当下，使已经离场的人物通过媒介形成关系回声。

这说明 QX17 的交通 / 道路对象与 QX16 的媒介对象可以在同一作品中承担不同层面的结构功能，无需把它们归并为泛化的“公路小说意象”。

---

## 04｜《82年生的金智英》：拒绝把日常家务物件批量意象化

本作只保留 1 条正式关系：

```text
声音 / 口吻
```

没有为了提高数量而标注：

```text
厨房
咖啡
家务用品
婴儿用品
普通家庭空间
```

这些对象虽然参与现实生活，但仅凭“能够体现女性处境”并不足以进入 QX。

“声音 / 口吻”通过 Admission Gate 的原因在于：

- 反复出现；
- 直接触发丈夫寻求心理咨询；
- 与金智英的人物状态稳定绑定；
- 作为小说开端及叙事展开的重要结构装置。

因此：

```text
GENDER_THEME = QH
BORROWED_VOICE_AS_PERCEPTIBLE_NARRATIVE_DEVICE = QX
```

---

## 05｜《24个比利》：人格主题必须落实为身体与内部空间

本批没有直接标注：

```text
多重人格
自我分裂
身份危机
精神疾病
```

正式保留：

```text
意识大厅与聚光灯
身体
```

“意识大厅与聚光灯”把人格切换转译成反复出现的内部空间模型：谁进入中央聚光灯，谁获得身体控制权。

“身体”则不是泛化的人体标签，而是：

```text
多个年龄 / 性别 / 能力不同的人格
→ 共享同一具现实身体
→ 轮流取得控制权
→ 产生行动与记忆断裂
```

因此两条关系分别承担：

- 内部心理结构的空间可视化；
- 人格进入现实行动的共同物质界面。

---

## 06｜对象粒度与延后治理

本批继续遵守“先建设完整 corpus、后做全量对象治理”的决定。

因此暂不处理以下潜在问题：

```text
月亮 vs 两个月亮
道路 vs 公路 vs 国道
声音 vs 音乐 vs 录音
身体 vs 具体身体部位
内部心理空间是否形成稳定 object family
```

这些仅作为后续 Full Corpus Audit 的候选问题，不在建设阶段提前改写对象本体。

```text
OBJECT_ONTOLOGY_REFACTOR = DEFERRED
SCHEMA_MIGRATION = NO
CURRENT_SCHEMA = QX_RELATION_SCHEMA_V1
```

---

## 07｜专题激活检查

本批没有出现足以直接触发新叶专题的同一 canonical object。

因此：

```text
ACTIVE_QX_LEAVES_BEFORE = 2
ACTIVE_QX_LEAVES_AFTER = 2
NEW_QX_LEAF = NO
```

现有正式叶节点继续为：

- `QX3.1 文学中的海`
- `QX16.1 文学中的书信`

本批出现的道路 / 交通、声音 / 媒介、身体 / 内部空间等，只积累实例，不提前建立专题。

---

## 08｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 181
FORMAL_WORKS_WITH_QX = 48
ACTIVE_QX_LEAVES = 2
NEW_TOPIC_THIS_BATCH = NONE
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次010]]
- [[QX3.1 文学中的海]]
- [[QX16.1 文学中的书信]]
