---
id: WL-QX-GOVERNANCE
type: literature_governance
name: QX 作品意象标注与关系治理规则
code: QX-GOVERNANCE
axis: Q
facet: QX
status: FROZEN_V1
source_version: 1.1
schema: QX_RELATION_SCHEMA_V1
pilot_basis: 10 works / 87 high-recall candidate relations
precision_policy: ADMISSION_GATE_V1
---

# QX 作品意象标注与关系治理规则

> 本文件规定 QX 从作品层采集意象、建立 `作品 → QX 意象` 关系、维护关系属性，并由作品实例反向生长为跨作品专题的统一规则。
>
> `QX_RELATION_SCHEMA_V1` 的字段结构已冻结；本次 V1.1 不修改字段 schema，只提高**正式入库准入精度**。
>
> 两轮 Pilot 的 87 条关系应视为 **high-recall candidate set（高召回候选集）**，不是 87 条自动成立的正式关系。正式迁移前必须经过 Precision Review。
>
> 核心原则：**作品层保存事实与关系，QX 专题保存跨作品解释；先采集，后归纳；可解释不等于应入库；宁可少而明确，不为完整性制造噪声。**

---

## 00｜QX 的定位

QX 不是与 QT / QH / QC 相同的先验分类树。

```text
作品阅读
↓
发现可能值得比较的具体意象 / 场景 / 物件
↓
候选采集（允许高召回）
↓
Admission Gate 精度审查
↓
建立正式 作品 —[HAS_IMAGERY]→ QX 意象 关系
↓
记录关系属性
↓
同类意象跨作品聚合
↓
达到门槛后激活 QX 叶节点专题
↓
从实例中归纳文学功能、意义谱系与跨作品模式
↓
派生意象簇、作品距离等上层结构
```

因此：

- **作品层 = 数据源**；
- **候选采集 = 高召回层**；
- **Admission Gate = 精度控制层**；
- **HAS_IMAGERY = 正式关系层**；
- **QX 叶节点 = 聚合分析层**；
- **IMAGERY_CONSTELLATION 等 = 派生分析层**。

> **QT / QH / QC 更多是“用已有结构理解作品”，QX 更多是“从作品里发现可重复比较的结构”。**

---

# 01｜QX 的对象边界

QX 记录作品中具有跨作品比较价值的**具体可感知对象、空间、场景、自然现象、身体要素、器物、媒介或社会仪式**。

例如：雨、雪、月亮、海、河、树、森林、鸟、蛇、房屋、门、窗、镜子、街道、火车、血、颜色、光影、火、书、信、手稿、墓地、幽灵、宴会、舞会、葬礼等。

但必须区分三层：

```text
文本中出现的物象
↓
可以进行文学解释的意象
↓
值得进入 QX 的显著 / 核心意象
```

**QX 只记录第三层。**

因此：

> **可进行文学解释 ≠ 应进入 QX。**

文学作品中几乎任何物象都可能被解释，但 QX 是结构化跨作品数据层，不是“所有可分析物象”的全集。

作品完全允许：

```text
QX = 0
```

这表示“没有达到 QX 正式准入门槛的显著意象”，不表示“作品没有任何文学意象”。

---

# 02｜Formal Admission Gate：正式准入门槛

## 02.1 常规准入：四项至少满足两项

一个候选对象只有在以下四个信号中**至少满足两项**，才进入正式 QX 关系：

### A. recurrence｜重复性

对象在作品中反复出现，且重复本身承担文学或结构作用，而非简单背景重复。

有效例：

- 某对象反复与同一人物、状态或阶段共同出现；
- 重复形成前后回声；
- 重复过程中意义或作用发生变化。

仅仅“出现很多次”不自动满足本项。

### B. structural｜结构性

对象参与作品的重要结构：

- 开头 / 结尾；
- 关键转折；
- 人物命运节点；
- 世界状态变化；
- 重要叙事阶段切换；
- 关键伏笔、闭环或前后呼应。

### C. binding｜稳定绑定性

对象与以下至少一种对象形成稳定绑定：

- 特定人物；
- 人物关系；
- 家族 / 群体；
- 特定空间；
- 特定历史阶段；
- 某种持续身份或生活秩序。

### D. distinctiveness｜作品辨识度

该对象明显参与作品的文学辨识度：

- 提及该对象容易联想到该作品；
- 拿掉它会明显削弱作品的感知特征、结构特征或人物识别；
- 它不是该类作品都可以随意替换的普通背景元素。

## 02.2 例外准入：singular_pivotal

出现次数少甚至只有一次的对象，可以不满足“两项规则”，但必须同时满足：

```text
singular_pivotal = true
AND
evidence = clear
```

即：它虽然不反复，但对关键转折、结局、人物命运或作品解释具有决定性作用。

## 02.3 单项不足

以下情况**单独存在时不够进入 QX**：

- “它出现过”；
- “它出现很多次”；
- “它可以象征某种东西”；
- “它营造了气氛”；
- “它符合传统象征字典”；
- “它和主题有一点关系”；
- “我觉得这个意象很美 / 很有印象”。

这些都只能进入候选层，除非同时满足 Admission Gate 的其他信号。

---

# 03｜明确排除与降级规则

默认 DROP：

- 普通背景性出现；
- 单纯因为“文本中出现过”就打标签；
- 只有泛化氛围功能、没有独立结构价值的对象；
- 无法提供作品内 evidence 的对象；
- 仅凭传统象征字典推断的意义；
- 为了让作品至少有几个 QX 而补齐的对象；
- 仅因属于某 QX 一级类就挂入作品的对象。

优先 REFRAME 而不是直接 KEEP：

```text
过粗对象：
服饰
身体
灯光
植物
食物
建筑
```

如果真正有价值的是具体对象，应改写为更明确粒度，例如：

```text
“服饰” → 某件反复出现且身份绑定的服饰 / 饰物
“身体” → 眼睛 / 伤口 / 血 / 手 / 疤痕等明确对象
“灯光” → 某种稳定灯火场景或特定光源
```

如果无法具体化，则 DROP。

---

# 04｜候选层与正式层

## 04.1 候选采集允许高召回

阅读或 Pilot 阶段可以先记录较宽的候选对象，以免遗漏。

候选记录可以包含：

```yaml
qx:
  - qx_id: null
    object: 候选对象
    primary_group: QXx
    admission_status: candidate
    reason: 初步发现理由
```

候选状态**不代表正式 HAS_IMAGERY 已成立**。

## 04.2 正式关系必须通过 Admission Gate

正式关系要求：

```text
ADMISSION_GATE = PASS
```

并满足 V1 核心字段：

```text
object
salience
function
evidence
```

## 04.3 Precision Review 决策枚举

现有 Pilot 或未来批量候选审查统一使用：

```text
KEEP
DROP
MERGE
REFRAME
```

- `KEEP`：满足准入门槛，可转正式关系；
- `DROP`：可解释，但不够显著 / 稳定，不进入 QX；
- `MERGE`：与同一对象重复或只是 manifestation 差异，应合并；
- `REFRAME`：对象粒度或概念不对，需要改成更准确对象后重审。

---

# 05｜数量原则

QX 不设置硬性数量上限。

但正式 QX 的数量由 Admission Gate 自然控制。

因此：

- 0 个可以；
- 1–3 个很正常；
- 5–10 个也可能合理；
- 高密度经典作品可以更多；
- 数量多本身不是错误，但每一条都必须独立通过 Admission Gate。

不应因为“经典作品很复杂”就默认多标，也不应因为“这本书有很多可解释物象”就全部入库。

---

# 06｜QX_RELATION_SCHEMA_V1

字段 schema 不因本次精度修订改变。

## 06.1 A｜核心关系层：正式记录必填

```text
object
salience
function
evidence
```

## 06.2 B｜解释增强层：按实际需要填写

```text
manifestation
meaning
perceptual_channel
mode
phase
scope
```

## 06.3 C｜系统管理层

```text
qx_id
primary_group
note
```

### 字段总表

| 字段 | 含义 | V1 要求 |
|---|---|---|
| `object` | 归一化对象名 | **必填** |
| `salience` | 在作品中的重要程度 | **必填** |
| `function` | 对象怎样参与作品运行 | **必填** |
| `evidence` | 支撑关系的作品内事实 | **必填** |
| `manifestation` | 本作中的具体呈现形态 | 建议填写 |
| `meaning` | 当前作品中的意义 | 可选 |
| `perceptual_channel` | 感知通道 | 可选 |
| `mode` | 存在 / 运作方式 | 可选 |
| `phase` | 主要结构阶段 | 可选 |
| `scope` | 作用对象 / 尺度 | 可选 |
| `qx_id` | 正式叶节点编号 | 节点激活后必填 |
| `primary_group` | QX1–QX20 主归属 | 候选阶段建议填写 |
| `note` | 补充说明 | 可选 |

---

# 07｜object 与 manifestation

`object` 回答：

> 跨作品比较时，我们把它视为什么对象？

`manifestation` 回答：

> 同一个对象在这部作品里具体长什么样？

例如：

```yaml
object: 雨
manifestation: 持续数年的连绵长雨
```

默认不要因为：

```text
春雨 / 秋雨 / 暴雨 / 细雨 / 长雨
```

就建立多个 QX 节点，而应由 manifestation 表达具体形态。

---

# 08｜salience：正式关系内部的重要程度

受控值：

```text
significant
core
dominant
```

注意：**salience 只在对象通过 Admission Gate 之后使用。**

它不是准入评分。

### significant

已经通过正式准入门槛，具有稳定、明确、值得跨作品比较的独立作用，但不是作品核心识别结构。

> V1.1 对 `significant` 的门槛高于 Pilot 阶段。

### core

与人物、结构、主题、世界状态或结局高度绑定，是理解作品的重要入口。

### dominant

极少使用；对象几乎组织作品主要感知世界或意义网络。

不设置 `incidental / low`。达不到 significant 的对象直接不进入正式 QX。

---

# 09｜function：QX 的核心可计算属性

`function` 回答：

> **这个对象在作品运行过程中具体做了什么？**

半受控词表：

环境与世界：

- `氛围塑造`
- `空间塑造`
- `世界状态`
- `时间标记`
- `场景转换`

人物与关系：

- `情绪外化`
- `人物塑造`
- `身份标识`
- `关系映射`
- `权力标识`

情节与结构：

- `人物行动条件`
- `情节推动`
- `情节转折`
- `伏笔 / 预示`
- `结构标记`
- `前后回声`
- `记忆触发`

空间与边界：

- `隔离`
- `连接`
- `遮蔽`
- `暴露`
- `阻碍`
- `边界 / 阈限`

意义强化：

- `主题承载`
- `象征强化`
- `对照 / 反讽`
- `仪式化`

一个对象允许多个 function，但不要机械穷举。

特别注意：

> **单独只有 `氛围塑造` 通常不足以通过 Admission Gate。**

它需要同时具备重复、结构、绑定或辨识度等更强证据。

---

# 10｜meaning：OPTIONAL

`meaning` 回答：

> 当前作品语境中，这个对象承载、唤起或强化什么？

meaning 不是必填。

对象可以首先是物质条件、空间条件、技术条件或身体条件，而没有稳定象征意义。

禁止固定象征字典：

```text
雨 ≠ 自动等于洗涤
蛇 ≠ 自动等于邪恶
白 ≠ 自动等于纯洁
```

没有明确作品内证据时，宁缺毋滥。

---

# 11｜perceptual_channel

V1 不新增 `QX21 感官`。

受控值：

```text
visual
auditory
olfactory
gustatory
tactile
thermal
bodily
```

它描述体验方式，不决定对象主归属。

---

# 12｜mode

V1 词表：

```text
recurrent
climactic
character_bound
relation_bound
spatial_bound
period_bound
transformative
contrastive
ritualized
singular_pivotal
```

其中 `singular_pivotal` 可以触发 Admission Gate 的例外路径，但必须有明确 evidence。

`title_bound` 不进入 V1。

---

# 13｜phase 与 scope

`phase` 可使用：开篇、前期、战争阶段、繁盛期、身份转换后、结尾、回忆层、梦境层等自然语言。

`scope` 回答对象主要作用于谁 / 什么尺度，可写：人物、关系、家族、房屋、城镇、群体、制度、社会、世界或具体名称。

两者均为可选。

---

# 14｜evidence：REQUIRED

`evidence` 是正式 QX 关系的必填字段，也是 Admission Gate 的基础。

证据可以是：

- 关键场景；
- 反复发生的事件；
- 与人物绑定的动作；
- 开头 / 结尾呼应；
- 结构转折；
- 可定位文本事实。

不要求逐字摘录。

证据等级可内部区分：

```text
direct
strong_inference
speculative
```

`speculative` 不进入正式结构化关系，最多进入 note。

---

# 15｜qx_id 与专题激活

- 未激活正式叶节点：`qx_id: null`；
- 正式叶节点创建后：必须回填 `qx_id`；
- 禁止伪造编号。

专题原则上要求：

- 同一对象至少出现于 3 部**已经通过 Admission Gate 的正式作品关系**；
- 且至少存在两种有意义的使用方式 / 功能 / 语义变体。

Pilot 候选数量不计入激活门槛，只有 Precision Review 后的 KEEP 才计入。

---

# 16｜作品粒度

默认：

```text
WORK_GRANULARITY_DEFAULT = SMALLEST_INDEPENDENT_NARRATIVE_UNIT
```

小说集 / 短篇集应优先标到具体单篇 Work。

只有存在明确 collection-level evidence，才允许集子层 HAS_IMAGERY。

---

# 17｜与 QT / QH / QC 的边界

- **QT**：这是什么类型的故事？
- **QH**：作品究竟在思考什么？
- **QC**：哪些母题、原型和叙事模式跨文化反复出现？
- **QX**：哪些具体可感知对象达到显著性门槛，它们如何运作？

```text
洪水（QX：具体水灾 / 场景）
↓
洪水毁灭—重生（QC：母题）
```

QX 的 meaning 可以连接 QH，但不能自动替代 QH。

---

# 18｜对象粒度与归属

### 不要过粗

```text
水 / 动物 / 植物 / 建筑 / 颜色
```

通常只适合导航类。

### 不要过细

同一对象不同形态优先由 manifestation 表达。

### 同义词

统一主名称：

```text
铁路列车 / 火车 → 火车
```

### 主归属 + 交叉连接

每个对象设一个 `primary_group`，但允许连接其他 QX 类。

---

# 19｜QX 专题四层结构

正式叶节点按通过精度审查的作品数据反向归纳：

1. **对象本体**；
2. **文学功能**；
3. **正式作品实例**；
4. **跨作品模式**。

跨作品模式必须从 KEEP 后的正式关系长出来，不从高召回 Pilot 候选直接归纳。

---

# 20｜IMAGERY_CONSTELLATION

```text
IMAGERY_CONSTELLATION.type = derived_structure
IMAGERY_CONSTELLATION.manual_annotation = PROHIBITED
```

意象簇由多条正式 HAS_IMAGERY 关系计算 / 聚类 / 归纳产生，不作为人工底层标签。

---

# 21｜作品距离中的 QX

QX 可以参与作品距离，但不得只按共有 object 计算。

可使用：

```text
object similarity
+ manifestation similarity
+ function similarity
+ meaning similarity（有值时）
+ perceptual_channel similarity
+ mode similarity
+ phase / scope similarity
```

其中：

> **function 是核心特征；meaning 是增强特征；DROP 的候选关系不得进入距离计算。**

提高 Admission Gate 精度也是为了避免“雨 / 房屋 / 门 / 路 / 夜”等高频普通对象变成低信息 hub，污染作品距离。

---

# 22｜正式标注质量检查

## A. Admission Gate

- [ ] 是否满足 recurrence / structural / binding / distinctiveness 中至少两项？
- [ ] 若不满足两项，是否属于有明确证据的 `singular_pivotal`？
- [ ] 是否只是“可解释”，但还不够显著？若是，DROP。

## B. 对象

- [ ] 是否为具体可感知对象 / 空间 / 场景 / 媒介 / 身体要素？
- [ ] 是否过粗，需要 REFRAME？
- [ ] 是否与已有 object 重复，只是 manifestation 不同，需要 MERGE？

## C. 关系

- [ ] salience 是否在通过准入后才赋值？
- [ ] function 是否描述“怎么工作”？
- [ ] evidence 是否足够未来复核？
- [ ] meaning 若填写，是否有作品内证据？
- [ ] 可选字段是否真的增加解释力？

## D. 边界

- [ ] 是否误把 QH / QC / QT 当成 QX？
- [ ] 小说集是否错误制造单篇间假共现？

## E. 节点治理

- [ ] 没有正式叶节点时是否保持 `qx_id: null`？
- [ ] 是否填写合理 primary_group？
- [ ] 专题激活统计是否只使用 Precision Review 后 KEEP 的关系？

---

# 23｜Pilot Precision Review 规则

两轮 Pilot：

```text
TOTAL_PILOT_WORKS = 10
TOTAL_PILOT_RELATIONS = 87
PILOT_RELATION_STATUS = HIGH_RECALL_CANDIDATE_SET
```

因此这 87 条不得直接迁入正式作品库。

下一步必须逐条执行：

```text
KEEP / DROP / MERGE / REFRAME
```

正式迁移只允许：

```text
KEEP
+ REFRAME 后重新 PASS
+ MERGE 后保留的统一关系
```

目标不是维持某个数量，而是提高 precision。

预期允许出现：

- 某作品保留 8–10 条；
- 某作品只保留 2–3 条；
- 某作品最终为 0 条。

这都是正常结果。

---

# 24｜V1.1 状态

字段 schema：

```text
QX_RELATION_SCHEMA_V1 = FROZEN
SCHEMA_FIELDS_CHANGED = NO
```

准入治理：

```text
ADMISSION_GATE_V1 = ACTIVE
PRECISION_FIRST = TRUE
QUANTITY_CAP = NONE
QX_ZERO_ALLOWED = TRUE
```

Pilot：

```text
PILOT_001 = HIGH_RECALL_INPUT
PILOT_002 = HIGH_RECALL_INPUT
PRECISION_REVIEW = REQUIRED_BEFORE_MIGRATION
```

正式大规模标注：

```text
MASS_ANNOTATION = AUTHORIZED_ONLY_UNDER_ADMISSION_GATE_V1
```

---

## 返回

- [[QX 文学意象与场景]]
- [[QX 专题模板]]
- [[QX Pilot｜五部经典作品意象试标]]
- [[QX Pilot｜第二批五部作品意象试标]]