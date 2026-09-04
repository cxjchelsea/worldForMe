---
id: WL-QX-FORMAL-ANNOTATION-009
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次009
code: QX-ANNOTATION-009
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 无人生还
  - 灿烂千阳
  - 我与地坛
  - 悉达多
---

# QX Formal Annotation｜增量批次009

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`，不设数量目标，不为专题激活反向补标。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《无人生还》 | 3 | 士兵岛；十个小兵人偶；童谣 |
| 《灿烂千阳》 | 3 | 喀布尔城；布卡；房屋与庭院 |
| 《我与地坛》 | 3 | 地坛；轮椅；古园中的树木与荒草 |
| 《悉达多》 | 3 | 河流；渡船；河声 |

```text
BATCH_009_WORKS = 4
BATCH_009_FORMAL_RELATIONS = 12
FORMAL_QX_RELATIONS_BEFORE = 147
FORMAL_QX_RELATIONS_AFTER = 159
FORMAL_WORKS_WITH_QX_BEFORE = 36
FORMAL_WORKS_WITH_QX_AFTER = 40
```

## 02｜《无人生还》：结构装置可以形成高密度小型意象链

```text
士兵岛
→ 隔离条件

童谣
→ 死亡脚本

小兵人偶
→ 可见计数器
```

三者分别属于空间、文本媒介和器物，不能手工合并成一个 object；未来可由共现关系派生为作品内部结构簇。

## 03｜《灿烂千阳》：抽象权力必须物质化后才能进入 QX

本批没有直接录入：

- 战争；
- 父权；
- 宗教规训；
- 女性压迫。

而是保留它们在文本中的具体承载物：

```text
喀布尔城
布卡
家庭住宅
```

因此继续保持：

```text
ABSTRACT_THEME → QH
MATERIAL / SPATIAL MANIFESTATION → QX
```

## 04｜《我与地坛》：QX 同样适用于散文与生命书写

“地坛”不是小说式情节装置，但仍具备：

- recurrence；
- structural；
- binding；
- distinctiveness。

因此 QX 并不依赖虚构叙事，只要对象在文本经验中具有稳定、可比较的文学功能即可。

## 05｜《悉达多》：河流专题暂不激活

“河流”在本作中达到 dominant，并同时具有视觉和听觉 manifestation。

但专题激活按 object-level 计算。当前正式数据中尚未出现至少另外两部能够直接 normalization 为：

```text
object: 河流
```

的作品实例。

因此：

```text
QX3.RIVER_CANDIDATE = ACTIVE_CANDIDATE
NEW_QX_TOPIC_ACTIVATED = 0
```

“银河的河流感”等近似结构不因语义相似而强行计入同一 object。

## 06｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 159
FORMAL_WORKS_WITH_QX = 40
ACTIVE_QX_LEAVES = 2
QX3.1_ACTIVATION_WORKS = 5
QX16.1_ACTIVATION_WORKS = 4
NEW_TOPIC_THIS_BATCH = NONE
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次008]]
- [[QX3.1 文学中的海]]
- [[QX16.1 文学中的书信]]
