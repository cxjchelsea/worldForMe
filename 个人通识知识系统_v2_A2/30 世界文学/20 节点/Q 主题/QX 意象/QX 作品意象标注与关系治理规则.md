---
id: WL-QX-GOVERNANCE
type: literature_governance
name: QX 作品意象标注与关系治理规则
code: QX-GOVERNANCE
axis: Q
facet: QX
status: FROZEN_V1
source_version: 1.0
schema: QX_RELATION_SCHEMA_V1
pilot_basis: 10 works / 87 relations
---

# QX 作品意象标注与关系治理规则

> 本文件规定 QX 从作品层采集意象、建立 `作品 → QX 意象` 关系、维护关系属性，并由作品实例反向生长为跨作品专题的统一规则。
>
> 本规则基于两轮 Pilot、10 部作品、87 条关系完成审查后冻结为 `QX_RELATION_SCHEMA_V1`。
>
> 核心原则：**作品层保存事实与关系，QX 专题保存跨作品解释；先采集，后归纳；不为了分类完整而制造空节点。**

---

## 00｜QX 的定位

QX 不是与 QT / QH / QC 相同的“先验分类树”。

基本工作流：

```text
作品阅读
↓
识别值得跨作品比较的具体意象 / 场景 / 物件
↓
建立 作品 —[HAS_IMAGERY]→ QX 意象 关系
↓
记录该关系在当前作品中的属性
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
- **HAS_IMAGERY = 关系采集层**；
- **QX 叶节点 = 聚合分析层**；
- **QX 专题四层结构 = 归纳层**；
- **IMAGERY_CONSTELLATION 等 = 派生分析层**。

> **QT / QH / QC 更多是“用已有结构理解作品”，QX 更多是“从作品里发现可重复比较的结构”。**

---

## 01｜什么可以进入 QX

QX 记录作品中具有跨作品比较价值的**可感知对象、空间、场景、自然现象、身体要素、器物、媒介或社会仪式**。

典型对象包括：雨、雪、月亮、海、河、树、森林、鸟、蛇、房屋、门、窗、镜子、街道、火车、身体、血、颜色、光影、火、书、信、手稿、墓地、幽灵、宴会、舞会、葬礼等。

### 01.1 纳入判断

一个对象至少满足下列任一条件，才值得进入作品的 QX 记录：

1. 在作品中反复出现；
2. 出现在关键情节、关键人物或关键空间中；
3. 明显承担叙事功能，而不是普通背景；
4. 意义或作用随剧情发生变化；
5. 与人物身份、关系或命运形成稳定绑定；
6. 与主题、母题、历史环境或作品结构形成明显连接；
7. 去掉该对象后，会明显削弱作品的文学辨识度；
8. 虽只出现少数几次，但对结局、转折或整体解释具有高权重。

### 01.2 不纳入

默认不记录：

- 普通背景性出现；
- 单纯因为“文本中出现过”就打标签；
- 无法说明其叙事作用的偶发物件；
- 仅凭传统象征字典推断，但作品本身没有证据；
- 为了让作品“至少有几个 QX”而强行补齐；
- 仅因某对象属于一个 QX 一级类，就把整个一级类挂到作品上。

**作品允许 `QX = 0`。**

---

## 02｜数量与提取原则

### 02.1 不设硬性数量上限

QX 不规定每部作品必须标多少，也不设置固定上限。

唯一门槛是：

> **这个对象是否明确、可解释、有文本依据，并且值得未来跨作品比较。**

0 个、2 个、7 个、15 个都可以。数量越多，只意味着需要越严格检查是否混入普通背景元素。

### 02.2 阅读后提取五问

1. 有没有反复出现的具体物象？
2. 有没有在关键情节出现的天气、空间、身体、器物或场景？
3. 有没有随剧情发生作用或意义变化的对象？
4. 有没有与特定人物、家族、群体或地点强绑定的对象？
5. 有没有一个对象拿掉之后，会明显削弱这部作品的文学辨识度？

### 02.3 高数量作品复核

当一部作品产生大量 QX 关系时，只复核：

1. 是否把“出现过”误当成“有文学功能”；
2. 是否把同一个对象的不同具体形态错误拆成多个节点；
3. 是否把 QH 主题、QC 母题或 QT 类型误标成 QX 意象。

通过复核后，数量本身不是问题。

---

## 03｜核心关系模型

```text
作品 —[HAS_IMAGERY]→ QX 具体意象
```

关系不是无属性标签，而应保存该意象**在这部具体作品中如何被使用**。

```text
作品
 │
 │ HAS_IMAGERY
 ▼
QX 具体意象
 │
 ├─ object               归一化对象
 ├─ manifestation        当前作品中的具体呈现形态
 ├─ salience             重要程度
 ├─ function             文学 / 叙事功能
 ├─ meaning              当前作品中的意义
 ├─ perceptual_channel   感知通道
 ├─ mode                 存在 / 运作方式
 ├─ phase                结构位置 / 出现阶段
 ├─ scope                作用对象 / 范围
 ├─ evidence             文本证据
 ├─ qx_id                正式节点编号（条件必填）
 ├─ primary_group        一级导航归属
 └─ note                 补充说明
```

- QX 节点回答：**“是什么意象？”**
- HAS_IMAGERY 属性回答：**“这个意象在这部作品里具体怎么出现、怎么工作？”**

---

## 04｜QX_RELATION_SCHEMA_V1

### 04.1 三层字段结构

#### A｜核心关系层：正式记录必填

```text
object
salience
function
evidence
```

这是 **Minimum Viable QX Relation**。

#### B｜解释增强层：按实际需要填写

```text
manifestation
meaning
perceptual_channel
mode
phase
scope
```

禁止为了填表而硬填。

#### C｜系统管理层

```text
qx_id
primary_group
note
```

### 04.2 字段总表

| 字段 | 含义 | 类型 | V1 要求 | 控制方式 |
|---|---|---|---|---|
| `object` | 归一化的人可读对象名 | string | **必填** | 尽量复用既有名称 |
| `salience` | 在作品中的重要程度 | enum | **必填** | 严格受控 |
| `function` | 该对象承担什么文学 / 叙事功能 | list | **必填** | 半受控词表 |
| `evidence` | 支撑判断的具体文本位置 / 场景 | list | **必填** | 文本事实 |
| `manifestation` | 该对象在本作中的具体形态 | string/list | 建议填写 | 开放、描述性 |
| `meaning` | 当前作品赋予或强化的意义 | list | 可选 | 开放但优先复用 |
| `perceptual_channel` | 主要感知通道 | list | 可选 | 受控词表 |
| `mode` | 该对象以什么方式存在 / 运作 | list | 可选 | 半受控词表 |
| `phase` | 主要出现在哪个结构阶段 | list/string | 可选 | 开放 |
| `scope` | 主要作用于谁 / 什么层面 | list | 可选 | 开放 |
| `qx_id` | 对应正式 QX 叶节点 | string/null | **节点激活后必填** | 唯一编号 |
| `primary_group` | 一级导航主归属 | string | 候选阶段建议填写 | QX1–QX20 |
| `note` | 无法结构化但值得保留的说明 | string | 可选 | 开放 |

### 04.3 统一记录结构

候选对象和正式对象使用同一 schema，不长期维护两套数据模型。

```yaml
qx:
  - qx_id: null
    object: 栗树
    primary_group: QX4
    manifestation: 家宅庭院中与家族始祖长期绑定的栗树
    salience: core
    function:
      - 人物塑造
      - 空间塑造
      - 记忆触发
    meaning:
      - 孤独
      - 家族记忆
    perceptual_channel:
      - visual
    mode:
      - recurrent
      - character_bound
      - spatial_bound
    phase:
      - 中后期
    scope:
      - 家族始祖
      - 家宅
    evidence:
      - 人物长期被系于栗树旁，树成为其晚年与家族起源记忆的固定空间锚点
    note:
```

正式节点激活后只需回填：

```yaml
qx_id: QX4.x
```

---

## 05｜object 与 manifestation

### 05.1 object

`object` 回答：**跨作品比较时，我们把它视为什么对象？**

例如：雨、太阳、镜子、海、火车、房屋、玫瑰。

### 05.2 manifestation

`manifestation` 回答：**同一个归一化对象，在这部作品中具体长什么样？**

```yaml
object: 雨
manifestation: 持续数年的连绵长雨
```

```yaml
object: 太阳
manifestation: 正午刺眼、灼热并伴随强烈反光的阳光
```

默认使用：

```text
object + manifestation
```

而不是因为“春雨 / 秋雨 / 暴雨 / 细雨 / 长雨”制造大量近义叶节点。

只有当某一变体形成独立、稳定、值得长期追踪的文学传统时，才考虑拆节点。

---

## 06｜salience：重要程度

只允许：

```text
significant
core
dominant
```

- `significant`：承担明确文学功能，值得比较，但不是作品核心识别结构；
- `core`：与人物、结构、主题、世界状态或结局高度绑定；
- `dominant`：极少使用，对象几乎组织作品主要感知世界或意义网络。

规则：

- 不设置 `low / incidental`；普通出现直接不进入 QX；
- `dominant` 必须谨慎；
- 同一作品可以有多个 `core`，但每个必须有独立证据。

---

## 07｜function：文学 / 叙事功能

`function` 回答：**这个对象在作品运行过程中具体做了什么？**

function 是 QX V1 最重要的可计算属性之一。

### 07.1 半受控词表

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

### 07.2 多值规则

一个意象允许多个 function，但不要机械穷举。若数量过多，应检查是否把 `meaning`、`mode` 或普通后果混入 function。

### 07.3 function 与 meaning

```text
雨
function = 情绪外化
meaning = 悲伤 / 压抑
```

- function 描述**怎么工作**；
- meaning 描述**表达什么**。

---

## 08｜meaning：作品内意义

V1 状态：**OPTIONAL**。

部分意象首先是强物质条件、空间条件、技术条件或身体条件，不必承担稳定象征意义。

合法示例：

```yaml
object: 冰层
function:
  - 阻碍
  - 人物行动条件
meaning: []
```

meaning 开放但优先复用已有词；禁止使用固定象征字典自动推断。

没有明确意义时，**宁缺毋滥**。

---

## 09｜perceptual_channel：感知通道

V1 不新增 `QX21 感官` 一级分类，而把感官作为关系属性处理。

### 09.1 受控值

```text
visual
auditory
olfactory
gustatory
tactile
thermal
bodily
```

### 09.2 示例

```yaml
object: 太阳
primary_group: QX2
perceptual_channel:
  - visual
  - thermal
  - bodily
```

```yaml
object: 香气
perceptual_channel:
  - olfactory
```

规则：

- 描述体验方式，不决定对象主归属；
- 一个对象可有多个通道；
- 只有感官维度有解释价值时再记录。

---

## 10｜mode：存在 / 运作方式

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

定义：

- `recurrent`：反复出现；
- `climactic`：集中于高潮或重大转折；
- `character_bound`：与特定人物稳定绑定；
- `relation_bound`：与特定人物关系绑定；
- `spatial_bound`：与特定空间绑定；
- `period_bound`：与作品某一阶段绑定；
- `transformative`：作用或意义随剧情变化；
- `contrastive`：通过前后、人物或空间对照运作；
- `ritualized`：以仪式、重复动作或习惯化场景出现；
- `singular_pivotal`：出现次数少，但承担决定性转折。

允许多值。

### 10.1 title_bound 不进入 V1

题名关系描述的是作品命名层显著性，不属于意象在叙事内部如何运作。如重要，可通过 `salience + note + evidence` 记录。

---

## 11｜phase 与 scope

### phase

可使用自然语言，例如：开篇、战争阶段、家族繁盛期、身份转换后、结尾、回忆层、梦境层、某一叙事线。

没有解释价值可以省略。

### scope

回答：**这个意象主要作用于谁、什么关系或什么尺度？**

可使用：人物、人物关系、家族、房屋 / 场所、城镇、群体、阶层、制度、社会、文明 / 世界，或具体名称。

---

## 12｜evidence：证据

V1 状态：**REQUIRED**。

`evidence` 是正式 QX 关系的必填字段，是防止过度阐释和保证未来可复核性的核心质量门。

证据可以是：

- 具体章节 / 回目；
- 关键场景；
- 反复发生的事件；
- 与人物绑定的动作；
- 开头与结尾的结构呼应；
- 可定位的文本描述。

不要求逐字摘录。

```yaml
evidence:
  - 连续降雨覆盖马孔多后期生活并伴随城镇衰败
  - 雨停之后空间和生活秩序已无法恢复到原状
```

需要时可内部区分：

- `direct`
- `strong_inference`
- `speculative`

`speculative` 不进入正式结构化关系，最多留在 note。

---

## 13｜qx_id 与专题激活

### 13.1 qx_id 条件必填

- 尚未激活正式叶节点：`qx_id: null`；
- 正式 QX 叶节点创建后：必须回填 `qx_id`；
- 禁止伪造编号。

### 13.2 候选与正式关系使用同一 schema

候选对象仍使用正式关系结构，只是：

```yaml
qx_id: null
primary_group: QX4
```

这样节点激活后只需回填编号。

### 13.3 专题激活门槛

原则上，同一对象需：

- 至少出现于 **3 部可比较作品**；
- 且至少存在两种有意义的使用方式、语义或功能变体；

才激活正式 QX 叶节点专题。

文学史价值极强或明确希望长期追踪的对象，可提前建立 `CANDIDATE` 专题，但不得假装已有跨作品结论。

---

## 14｜作品粒度：最小独立叙事单元原则

默认：

> **QX 标注到最小的独立叙事 Work。**

若一个意象只属于小说集中的某一短篇，应建立：

```text
短篇 A —HAS_IMAGERY→ 意象
```

而不是：

```text
整本小说集 —HAS_IMAGERY→ 意象
```

否则会制造不同篇章之间的假共现。

只有存在明确 collection-level evidence，例如对象贯穿多篇、作为全书框架意象、参与集子整体结构，才允许集子层关系。

```text
WORK_GRANULARITY_DEFAULT = SMALLEST_INDEPENDENT_NARRATIVE_UNIT
COLLECTION_LEVEL_RELATION = REQUIRES_COLLECTION_LEVEL_EVIDENCE
```

---

## 15｜QX 专题四层结构

正式叶节点按作品数据反向归纳：

1. **对象本体**：我们究竟在观察什么；
2. **文学功能**：它在不同作品里如何工作；
3. **作品实例**：在哪些作品里实际做了什么；
4. **跨作品模式**：积累足够实例后，能归纳出哪些重复使用模式。

跨作品模式必须从作品实例长出来，不预设固定分类。

---

## 16｜与 QT / QH / QC 的边界

- **QT**：这是什么类型的故事？
- **QH**：作品究竟在思考什么？
- **QC**：哪些母题、原型和叙事模式跨文化反复出现？
- **QX**：哪些具体可感知对象值得跨作品比较，它们如何运作？

示例：

```text
洪水（QX：可感知的水灾 / 场景）
        ↓ 可连接
洪水毁灭—重生母题（QC）
```

QX 的 `meaning` 可以连接 QH，但不能自动替代 QH。

---

## 17｜对象粒度与归属治理

### 17.1 不要过粗

“水 / 动物 / 植物 / 建筑 / 颜色”更适合作为导航类，而不是具体叶节点。

### 17.2 不要过细

同一对象的形态差异优先由 `manifestation` 表达。

### 17.3 同义词

统一主名称，例如：

```text
铁路列车 / 火车 → 火车
```

原文具体说法进入 manifestation 或 evidence。

### 17.4 主归属 + 交叉连接

每个对象只设一个 `primary_group`，但允许连接其他 QX 类。分类主归属用于导航，不代表语义互斥。

---

## 18｜感官问题的最终治理

V1 **不新增 QX21 感官与感觉**。

统一使用 `perceptual_channel` 表达视觉、听觉、嗅觉、味觉、触觉、温度与身体体验。

若未来大规模数据证明纯感官对象无法稳定归入 QX1–QX20，再重新评估导航分类，但 V1 不扩轴。

---

## 19｜IMAGERY_CONSTELLATION：意象簇

`IMAGERY_CONSTELLATION` 表示多个 QX 对象在同一作品中形成的稳定组合或共同感知世界。

例如未来可能从数据中发现：

```text
夜 + 银河 + 星光 + 列车 + 河流
→ 夜间宇宙旅程意象簇
```

V1 状态：

```text
IMAGERY_CONSTELLATION.type = derived_structure
IMAGERY_CONSTELLATION.manual_annotation = PROHIBITED
```

即：不作为作品级必填字段，不要求人工直接命名，应从多条 `HAS_IMAGERY` 关系中计算、聚类或归纳产生。人工可以审阅、命名和解释派生结果。

---

## 20｜作品距离中的 QX 使用原则

QX 可以参与未来作品距离计算，但不得只按“共有对象”计算。

潜在特征可包括：

```text
对象相似度
+ manifestation 相似度
+ function 相似度
+ meaning 相似度（有值时）
+ perceptual_channel 相似度
+ mode 相似度
+ phase / scope 结构相似度
```

例如：

```text
作品 A：雨 → 衰败 → 世界状态
作品 B：雪 → 衰败 → 世界状态
```

即使对象不同，也可能具有很高的功能结构相似性。

> **function 是 QX 距离计算中的核心特征；meaning 是增强特征，不应因缺失而惩罚作品。**

---

## 21｜正式标注质量检查

### 对象检查

- [ ] 是否是具体可感知对象 / 空间 / 场景 / 媒介 / 身体要素？
- [ ] 是否值得跨作品比较，而不是普通背景？
- [ ] 是否与已有 object 重复或仅是 manifestation 差异？

### 关系检查

- [ ] `salience` 是否符合三级定义？
- [ ] `function` 是否描述“怎么工作”而不是“表达什么”？
- [ ] `evidence` 是否足以让未来的自己复核？
- [ ] `meaning` 若填写，是否有作品内证据？
- [ ] 可选字段是否真的增加解释力，而不是为了填表？

### 边界检查

- [ ] 是否误把 QH 主题当成 QX？
- [ ] 是否误把 QC 母题 / 原型 / plot pattern 当成 QX？
- [ ] 是否误把 QT 类型当成 QX？
- [ ] 小说集是否错误在 Collection 层制造了单篇之间的假共现？

### 节点治理检查

- [ ] 没有正式叶节点时是否保持 `qx_id: null`？
- [ ] 是否填写了合理 `primary_group`？
- [ ] 是否避免仅因一个作品出现就创建正式 QX 叶节点？

---

## 22｜V1 完整示例

```yaml
qx:
  - qx_id: QX1.1
    object: 雨
    primary_group: QX1
    manifestation: 持续数年的连绵长雨
    salience: dominant
    function:
      - 世界状态
      - 时间标记
      - 空间塑造
      - 结构标记
    meaning:
      - 衰败
      - 停滞
      - 历史断裂
    perceptual_channel:
      - visual
      - auditory
      - tactile
    mode:
      - recurrent
      - period_bound
      - transformative
    phase:
      - 后期
    scope:
      - 马孔多
      - 布恩迪亚家族
    evidence:
      - 持续降雨覆盖马孔多后期生活并伴随城镇秩序崩解
      - 雨停后原有生活世界没有恢复
    note:
```

最低正式关系：

```yaml
qx:
  - qx_id: null
    object: 某意象
    primary_group: QXx
    salience: significant
    function:
      - 某一明确功能
    evidence:
      - 可复核的关键场景或结构事实
```

---

## 23｜Schema 冻结状态

两轮 Pilot：

```text
TOTAL_PILOT_WORKS = 10
TOTAL_PILOT_RELATIONS = 87
```

V1 Review 决议：

```text
object = KEEP / REQUIRED
salience = KEEP / REQUIRED
function = KEEP / REQUIRED
evidence = KEEP / REQUIRED
manifestation = ADD / OPTIONAL_RECOMMENDED
meaning = KEEP / OPTIONAL
perceptual_channel = ADD / OPTIONAL
mode = KEEP / OPTIONAL
phase = KEEP / OPTIONAL
scope = KEEP / OPTIONAL
qx_id = KEEP / CONDITIONAL_REQUIRED
primary_group = KEEP / MANAGEMENT_FIELD
note = KEEP / OPTIONAL
title_bound = REJECTED_FROM_MODE
quantity_cap = NONE
```

作品粒度：

```text
WORK_GRANULARITY_DEFAULT = SMALLEST_INDEPENDENT_NARRATIVE_UNIT
COLLECTION_LEVEL_RELATION = REQUIRES_COLLECTION_LEVEL_EVIDENCE
```

派生结构：

```text
IMAGERY_CONSTELLATION = DERIVED_ONLY
MANUAL_ANNOTATION = PROHIBITED
```

最终状态：

```text
QX_RELATION_SCHEMA_V1 = FROZEN
QX_TOPIC_GROWTH_MODEL = ACTIVE
MASS_ANNOTATION = AUTHORIZED_UNDER_V1
```

V1 冻结意味着：

- 可以开始正式作品标注；
- 可以把 Pilot 数据逐步迁入作品库；
- 新作品不得随意增加底层必填字段；
- 若未来出现真实缺口，应以 V1.x 变更记录修订，而不是在单个作品中私自扩展 schema；
- QX1–QX20 导航分类仍可按实际材料轻量维护，不等于关系 schema 永久不可演化。

---

## 返回

- [[QX 文学意象与场景]]
- [[QX 专题模板]]
- [[QX Pilot｜五部经典作品意象试标]]
- [[QX Pilot｜第二批五部作品意象试标]]
