---
id: WL-QC-GOV-V2
type: literature_governance
name: QC 总体架构与建设规范 V2
axis: Q
scope: QC
status: ACTIVE
version: "2.0"
---

# QC 总体架构与建设规范 V2

> 本文件定义 QC 的长期职责、三层架构、对象模型、关系与证据规则、跨轴边界，以及专题准入、建设、冻结与重开机制。它是 QC 后续扩展的治理依据，不承担具体知识内容。

## 0. QC 的总定义

**QC｜世界叙事资源、母题谱系与文化传统**：研究故事从何而来，哪些叙事组件在不同文本与文化中反复出现、传播和变形，以及这些资源与组件如何进入具体历史社会，形成稳定的文化角色、叙事世界与文学传统。

QC 不以穷尽神话、母题或文化符号为目标，而以建立一个能够解释经典文学、民间叙事及现代再创作的高复用叙事资源网络为目标。

QC 的三个核心问题：

```text
QC1｜叙事资源与来源传统
人类曾经讲过什么故事？这些故事从哪里来、如何保存、定型与传播？

QC2｜母题、叙事组件与文本谱系
这些故事由哪些可重复的叙事组件构成？这些组件如何跨文本、跨传统迁移、组合和变形？

QC3｜历史化文化叙事传统
这些资源与组件进入具体历史社会后，如何与制度、伦理、空间和社会经验结合，形成稳定的文化角色世界与叙事传统？
```

三层不是按“具体 → 抽象 → 更抽象”排列，而是回答三个不同维度的问题：**来源、组件、历史化组织**。

---

# 1. 总体架构

```text
QC｜世界叙事资源、母题谱系与文化传统
│
├─ QC1｜世界叙事资源与来源传统
│   ├─ 来源传统 hubs
│   └─ Narrative Resource Entities
│
├─ QC2｜世界文化母题、原型与叙事结构
│   ├─ 稳定问题域 / 母题簇
│   └─ Component Network
│
└─ QC3｜历史化文化叙事传统
    ├─ 文化传统比较簇
    └─ Historical Cultural Narrative Traditions
```

基本流向：

```text
QC1 叙事资源
      ↓ supplies / attests
QC2 叙事组件
      ↓ combines_with
历史制度 + 社会结构 + 伦理系统 + 空间经验 + 政治合法性
      ↓ historicalizes
QC3 历史化文化叙事传统
      ↓ connects_to
QT 类型 / QH 主题 / R 区域文学 / T 时期 / 40 作品
```

注意：该图表示解释关系，不表示所有对象必须经历同一条单线演化路径。

---

# 2. QC1｜世界叙事资源与来源传统

## 2.1 职责

QC1 回答：**一个叙事资源从哪里来，它如何形成、保存、文本化、经典化、传播和被后世重写。**

QC1 的核心不是“文明百科”，而是建立可追踪的叙事资源谱系。

现有按文明／传统组织的 QC1.1 叶节点继续保留，作为来源传统 hub 和导航入口；不因新故事增加而无限追加 taxonomy 层级。

## 2.2 QC1 的资源对象

QC1 允许至少以下资源类型：

| resource_type | 定义 | 例子 |
|---|---|---|
| tradition | 一个较稳定的来源传统或叙事文化系统 | 希腊—罗马神话传统、北欧神话传统 |
| cycle | 围绕共同人物、事件或世界形成的故事循环 | 特洛伊循环、亚瑟王循环 |
| story | 可识别的具体故事单元 | 普罗米修斯盗火、大洪水 |
| figure_tradition | 围绕命名人物长期形成的叙事传统 | 浮士德、罗宾汉、唐璜、孙悟空传统 |
| tale_tradition | 具有较稳定整体结构、存在多个变体的故事传统 | 灰姑娘型故事等 |

资源对象原则上进入专题数据层或实体层，不要求全部升格为正式 QC 编号。

## 2.3 QC1 专题的最低解释结构

一个成熟的来源传统专题应逐步回答：

```text
1. 定义与边界
2. 时间、地域、语言与材料范围
3. 形成环境：宗教、仪式、社会结构、表演与口传机制
4. 叙事世界：宇宙观、人物系统、空间与秩序
5. 核心叙事群：cycles / stories / figure traditions
6. 载体演化：口传 → 仪式 → 史诗／戏剧／编纂 → 后世文类
7. 文本谱系：早期见证 → 定型文本 → 关键重写
8. 内部变体：地域、时期、作者／群体差异
9. 跨文化传播与接触
10. QC2 组件映射
11. 后世接受、再创作与现代生命
12. 阅读路线与核心书目
```

QC1 不以罗列“有哪些神、人物、故事”为完成标准。

---

# 3. QC2｜母题、叙事组件与文本谱系

## 3.1 职责

QC2 回答：**哪些叙事组件被反复使用，它们如何组合、传播、反转、重写，以及哪些相似只是独立同构。**

现有 QC2.1—QC2.20 继续作为相对稳定的问题域／母题簇，不要求每个具体对象都成为新的 taxonomy 节点。

## 3.2 QC2 正式对象类型

QC2 的核心对象分为六类：

| component_type | 核心问题 | 说明 |
|---|---|---|
| motif | 故事中反复出现的最小或较小叙事单元是什么？ | 兄弟相残、禁忌知识、冥界之旅 |
| tale_type | 哪些故事在整体事件组合与关系上形成可识别的故事类型？ | 用于民间叙事等存在稳定多变体结构的对象 |
| character_type | 哪类角色功能或文化角色模型被反复使用？ | Trickster、导师、法外英雄 |
| named_archetype | 哪些命名人物已超出单一文本身份，成为长期可调用的文化模型？ | 亚瑟王、浮士德、孙悟空 |
| plot_pattern | 事件通常按何种关系、顺序或因果结构展开？ | 预言 → 逃避 → 实现；离乡 → 试炼 → 归乡 |
| symbol | 哪些物件、形象或空间意象形成较稳定的文化含义？ | 圣杯、世界树、禁果 |

### 关于 archetype 的限制

`archetype` 不作为无条件的“跨文化万能解释词”。

- 一般角色模型优先使用 `character_type`；
- 具体人物经长期重写成为文化模型时使用 `named_archetype`；
- 若使用荣格、弗莱、坎贝尔等理论意义上的 archetype，必须注明理论框架与证据来源；
- 结构相似不能自动推出“集体无意识原型”或共同历史来源。

### theme 不属于 QC2 核心对象

`theme` 回答“作品在讨论什么抽象问题”，继续主要由 QH 承担。QC2 可与 QH 建立关系，但不重复建设主题 taxonomy。

## 3.3 Component 建设标准

QC2.1 已验证的 component 机制推广为 QC2 通用标准。一个正式 component 至少需要：

```text
component_type
明确名称与定义
positive boundary / negative boundary
required invariants
来源传统或文本见证
至少一个可核查的 source_reference
与相邻 component 的区分
必要时记录 work_reference
关系类型与证据等级
```

不是所有候选都应建成重型专题。

标准流程：

```text
Problem Domain
→ Component Inventory
→ Candidate Triage
→ Source Readiness
→ Component Admission / Acceptance
→ Topic Build
→ Coverage Review
→ Stage Freeze
→ Evidence-based Reopen only
```

---

# 4. QC3｜历史化文化叙事传统

## 4.1 定义

QC3 研究：**叙事资源和组件如何在具体历史社会中，与制度、阶层、伦理、政治合法性、空间经验和媒介传统结合，形成持续被重写的文化角色、社会想象和叙事世界。**

QC3 不是“某国文化概论”，也不是文学类型目录。

典型对象包括但不限于：

- 侠／江湖传统
- 欧洲骑士传统
- 日本武士／剑豪传统
- 美国西部／cowboy／outlaw 传统
- 罗宾汉／social bandit 传统
- 剑客／swashbuckler 传统
- 海盗／海洋法外者传统
- Gaucho 等具有明确历史—文化基底的叙事传统

## 4.2 QC3 的形成模型

```text
QC1 来源叙事与历史材料
        +
QC2 母题 / character types / plot patterns / symbols
        +
社会制度
        +
阶层结构
        +
伦理系统
        +
政治合法性
        +
空间经验
        +
媒介与文学生产机制
        ↓
历史化文化叙事传统
```

QC3 的核心是“历史化组织”，不是寻找所有传统背后的单一原型。

## 4.3 QC3 专题的最低解释结构

```text
1. 定义与边界
2. 本土概念与术语体系
3. 历史社会基底
4. 制度与阶层结构
5. 伦理与价值体系
6. 角色生态
7. 空间结构
8. QC2 母题／组件星座
9. 文本与媒介定型过程
10. 历史现实与文化神话之间的距离
11. 后世重构：reinvention / nationalization / commercialization / globalization
12. 与 QT 类型、QH 主题、R 区域文学及具体作品的关系
13. 跨文化比较
14. 阅读路线与支撑书目
```

## 4.4 QC3 准入门槛

一个对象进入 QC3，原则上至少满足以下四项：

1. 有可识别的真实历史、社会或制度基底；
2. 已形成相对稳定的角色、伦理或空间结构；
3. 存在跨时期持续的叙事、文本或媒介传统；
4. 不能仅由单一 motif、单一人物或单一 genre 充分解释。

因此：

```text
兄弟相残 → QC2
复仇 → QC2
侦探小说 → QT
浮士德 → QC1 + QC2，通常不单独进入 QC3
骑士传统 → QC3 候选
侠／江湖传统 → QC3 候选，并与 QT 武侠类型建立映射
```

---

# 5. 三层共享实体，不复制内容

QC1、QC2、QC3 必须通过关系共享同一批故事、人物、文本和作品，不允许为了满足三个专题模板而复制三份事实。

示例：

```text
普罗米修斯故事
QC1 → 希腊来源、早期见证、文本定型
QC2 → 盗火、越界获取知识、神罚、named_archetype
QH  → 知识、自由、责任、权力
40   → 《被缚的普罗米修斯》《弗兰肯斯坦》等具体作品
```

每层只保存自己需要解释的关系。

---

# 6. 关系模型

## 6.1 QC1 内部常用关系

```text
belongs_to_tradition
contains_cycle
contains_story
contains_figure_tradition
early_attested_in
canonicalized_in
rewritten_in
translated_into
transmitted_to
variant_of
```

## 6.2 QC1 → QC2

```text
attests_component
contains_motif
contains_character_type
contains_plot_pattern
contains_symbol
source_for_named_archetype
```

## 6.3 QC2 内部

```text
carries_motif
co_occurs_with
requires
variant_of
inverts
structurally_parallels
historically_derives_from
borrows_from
```

## 6.4 QC2 → QC3

```text
component_of_tradition
forms_motif_constellation_of
character_model_of
symbolic_resource_of
plot_resource_of
```

## 6.5 QC3 → 其他轴

```text
historically_realized_in_region → R
historically_realized_in_period → T
generates_or_shapes_genre → QT
engages_theme → QH
instantiated_or_reworked_in → 40 作品
```

关系词表可以扩充，但必须保持“来源关系、结构关系、历史传播关系、解释关系”彼此可区分。

---

# 7. 历史传播与相似性证据等级

QC 的最重要治理原则之一：**相似不等于传播。**

所有涉及跨文本、跨文化的谱系或影响判断，至少区分以下等级：

| level | 类型 | 定义 |
|---|---|---|
| GEN-1 | documented_transmission | 有明确文本、翻译、改写、接触或传播链证据 |
| GEN-2 | probable_transmission | 时间、地域、文本接触条件支持，但传播链不完整 |
| GEN-3 | common_source | 两个对象可追溯至共同的更早来源 |
| GEN-4 | independent_parallel | 结构或功能相似，但目前无传播证据，按独立平行处理 |
| GEN-5 | weak_analogy | 仅存在有限比较价值，不主张谱系或强结构同一 |
| GEN-U | unknown | 现有材料不足以判断 |

每条重要关系宜同时记录：

```yaml
relation_type: structural_parallel
transmission_claim: independent_parallel
confidence: medium
evidence:
  - source A
  - source B
note: 不主张直接历史影响
```

不得从 GEN-4 / GEN-5 自动升级为 GEN-1 / GEN-2。

---

# 8. 与其他轴的边界

| 系统 | 核心问题 | QC 不应重复的内容 |
|---|---|---|
| QC1 | 这个故事从哪里来、怎样形成与传播？ | 不写区域文学通史 |
| QC2 | 哪些叙事组件反复出现、怎样变形？ | 不把抽象主题重新做成母题 |
| QC3 | 组件如何在历史社会中形成文化叙事传统？ | 不把文化传统等同于文学类型 |
| QH | 作品讨论什么主题／观念问题？ | QC 只建立关联 |
| QT | 文学类型如何形成、运作并产生惯例？ | QC3 不复制 genre history |
| R | 某地区文学如何历史发展？ | QC1/3 只取与叙事传统有关部分 |
| T | 某时期文学如何变化？ | QC 不承担完整时期史 |
| 40 作品 | 具体作品是什么、怎样阅读？ | QC 保存关系，不复制作品实体 |

### QC3 与 QT 的硬边界

```text
QC3 问：为什么一个社会形成“侠、骑士、武士、cowboy”等文化角色与叙事世界？
QT 问：武侠小说、西部片／西部小说等作为文学／媒介类型如何运作？
```

二者可以双向映射，但不可合并。

---

# 9. Taxonomy 与实体层的分工

QC 不追求通过编号树表达全部知识。

## Taxonomy 负责

- 稳定入口
- 问题域
- 来源传统 hub
- 比较簇
- 导航

## 实体／Base／专题数据层负责

- story / cycle / figure tradition
- component
- 文本见证
- 作品关系
- 跨文化映射
- 关系证据
- 变体与传播记录

原则：**树负责找路，网络负责表达知识。**

只有当一个对象长期稳定、具有独立解释价值，并需要单独导航时，才考虑升格为 taxonomy 节点。

---

# 10. 专题建设治理

## 10.1 不按编号顺序机械施工

禁止默认：

```text
QC2.1 完成 → QC2.2 全量完成 → ... → QC2.20
```

推荐由真实阅读与研究需求触发：

```text
阅读／研究出现反复问题
→ 判断归属 QC1 / QC2 / QC3
→ 建立候选或最小记录
→ 累积足够来源
→ 通过准入
→ 深建专题
→ Coverage Review
→ Stage Freeze
```

## 10.2 深建触发条件

满足任一条件可提升优先级：

- 阅读经典时反复出现；
- 能连接多个来源传统或作品；
- 现有结构无法解释一个持续出现的学习问题；
- 对其他轴具有明显桥接价值；
- 有足够可靠来源支持深入；
- 能显著提高已有专题的解释密度，而非仅增加名词数量。

## 10.3 Stage Freeze

一个专题达到当前学习目标后应允许冻结。

冻结意味着：

```text
不再因为“还有候选”而自动扩建
允许 source enrichment
允许 work-reference backfill
允许 reading-route refinement
允许 relation evidence refinement
```

重开必须由新证据或真实学习缺口触发。

---

# 11. 推荐的第一阶段实施顺序

```text
Phase 1｜冻结本治理规范与 QC 顶层三层定义

Phase 2｜从 QC2.1 提炼并正式固化 Component 模板

Phase 3｜以“希腊—罗马神话传统”重构一个 QC1 深建样板

Phase 4｜建立 QC3 Pilot：英雄、武人、边疆与法外者文化传统
         首批比较：侠 / 骑士 / 武士 / 西部

Phase 5｜建立跨层矩阵与 Base
         来源 × component
         component × cultural tradition
         cultural tradition × genre / work
```

第一阶段不要求同时补全所有 QC1 来源传统，也不要求依次完成 QC2.2—QC2.20。

---

# 12. QC3 Pilot 建议

首个 QC3 比较簇建议定义为：

```text
QC3.1 英雄、武人、边疆与法外者文化传统
```

第一批只验证四个差异足够大的传统：

```text
侠／江湖
欧洲骑士
日本武士／剑豪
美国西部／cowboy／outlaw
```

共同研究问题不是“它们是否属于同一种英雄”，而是：

> 不同社会如何把武力、荣誉、忠诚、法律、边疆、国家与个人正义组织成不同的文化英雄模型？

比较变量至少包括：

```text
与国家关系
武力合法性
忠诚对象
荣誉体系
社会阶层
核心空间
法律关系
家庭与性别结构
共同体结构
典型冲突
典型结局
历史现实与后世神话之间的距离
```

---

# 13. QC 的完成标准

QC 的完成不以“收录多少神话、多少母题、多少人物”衡量，而以以下能力衡量：

1. 能追踪一个重要叙事资源从来源到定型与后世重写；
2. 能把重复出现的现象拆解为 motif / tale_type / character_type / named_archetype / plot_pattern / symbol；
3. 能区分历史传播、共同来源、独立平行与弱类比；
4. 能解释某些组件如何在具体历史社会中形成稳定文化叙事传统；
5. 能与 QH、QT、R、T、40 作品连接而不复制它们的职责；
6. 能在阅读新作品时快速回答“它调用了哪些旧资源、怎样改写、为什么在这个文化语境中这样改写”。

最终目标不是一个更大的分类树，而是一个具有来源、结构、历史和作品解释能力的**世界叙事谱系网络**。
