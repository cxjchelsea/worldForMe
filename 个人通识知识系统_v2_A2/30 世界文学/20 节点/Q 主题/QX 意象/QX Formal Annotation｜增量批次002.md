---
id: WL-QX-FORMAL-ANNOTATION-002
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次002
code: QX-ANNOTATION-002
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 双城记
  - 老人与海
  - 动物农场
  - 追风筝的人
---

# QX Formal Annotation｜增量批次002

> 本批次不再执行 Pilot。四部作品均为中央作品库中的已读 Work，直接按冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1` 进行正式标注。
>
> 原则仍然是：**不设数量配额；可解释不等于应进入 QX；允许作品最终 `QX = 0`。**

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《双城记》 | 4 | 红酒；编织；巴士底狱；断头台 |
| 《老人与海》 | 4 | 海；马林鱼；鲨鱼；狮子 |
| 《动物农场》 | 3 | 风车；七诫；农舍 |
| 《追风筝的人》 | 3 | 风筝；石榴树；弹弓 |

```text
BATCH_002_WORKS = 4
BATCH_002_FORMAL_RELATIONS = 14
FORMAL_QX_RELATIONS_BEFORE = 55
FORMAL_QX_RELATIONS_AFTER = 69
```

---

## 02｜为什么这一批不需要 Pilot

此前两轮 Pilot、Precision Review 与首批正式迁移已经完成：

```text
QX_RELATION_SCHEMA_V1 = FROZEN
ADMISSION_GATE_V1 = ACTIVE
```

因此本批次采用正式工作流：

```text
已读 Work
↓
候选对象
↓
Admission Gate
↓
正式 qx:
```

没有为了形成“漂亮数量”而补齐对象，也没有把作品中的所有可解释细节录入。

---

## 03｜角色与 QX 边界再次验证

### 《动物农场》

没有因为猪、马、驴等角色具有强烈寓言意义，就把它们直接作为 QX5 动物意象录入。

原因：

> 它们首先是完整人物 / 角色单位，其主要文学价值来自行动、语言、社会位置与寓言角色功能，而不是“动物对象本身如何作为可感知意象运作”。

正式保留的是：

- 风车：劳动、宣传与权力合法化装置；
- 七诫：公共记忆被权力持续改写的书写媒介；
- 农舍：权力阶层逐渐复制旧统治者生活方式的空间装置。

这一结果继续支持：

```text
IMPORTANT_CHARACTER ≠ QX_OBJECT
```

### 《老人与海》

大鱼、鲨鱼、狮子虽然属于动物对象，但与完整人格角色的情况不同：

- 大鱼稳定构成行动核心和人与非人世界的关系对象；
- 鲨鱼直接改变搏斗成果和结局的物质结果；
- 狮子以反复梦境形态形成青春、力量记忆与首尾回声。

因此可通过 Admission Gate。

---

## 04｜QX3.1 文学中的海增量

《老人与海》的“海”直接复用已有正式节点：

```yaml
qx_id: QX3.1
object: 海
```

`QX3.1` 当前作品实例从 3 部增至 4 部：

1. 《基督山伯爵》：跨越 / 逃亡 / 身份转换；
2. 《局外人》：身体经验与关系反差；
3. 《海底两万里》：世界本体与探索空间；
4. 《老人与海》：劳动、生存与搏斗空间。

这进一步说明 QX 专题比较的是：

```text
同一 object
× 不同 function
× 不同 manifestation
× 不同 scope
```

而不是建立“海 = 固定象征”的词典。

---

## 05｜本批 Object Normalization 检查

新增 14 条关系中：

- `海` 已存在 `QX3.1`，直接复用；
- 红酒、编织、巴士底狱、断头台、马林鱼、鲨鱼、狮子、风车、七诫、农舍、风筝、石榴树、弹弓均未因本批数据达到“至少 3 部可比较作品 + 至少两种稳定使用方式”的专题激活门槛。

因此：

```text
NEW_QX_TOPIC_ACTIVATED = 0
EXISTING_QX_TOPIC_EXPANDED = QX3.1
```

特别注意：名称或概念相近不自动归一。例如：

- “农舍”不与“大观园 / 梁宅 / 楼上房间”强行归成同一 object；
- “风筝”不因与“列车”等都属于移动物就合并；
- 这些跨对象的结构相似应留给 function / mode / scope 派生分析。

---

## 06｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 69
FORMAL_WORKS_WITH_QX = 13
QX3.1_ACTIVATION_WORKS = 4
NEW_TOPIC_THIS_BATCH = NONE
```

《夜晚的潜水艇》仍按最小独立叙事单元原则保持 collection-level QX = 0，等待未来建立具体短篇 Work 后再标注。

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Migration｜首批十部作品]]
- [[QX Object Normalization｜首批55条正式关系]]
- [[QX3.1 文学中的海]]
