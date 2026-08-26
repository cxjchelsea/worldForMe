# QT8.2｜世界文化母题、原型与叙事结构模板总则 V0

> 状态：`TEMPLATE_V0_REVISED_AFTER_ARCHETYPE_PILOT_B_PASS_A`
>
> 适用范围：QT8.2 横向抽象层中的 motif / archetype / plot_pattern / symbol 专题。
>
> 设计依据：QT8.1.1 希伯来—圣经叙事传统与 QT8.1.2 希腊—罗马神话传统两个已验收来源专题；由“洪水与灾后重建” motif Pilot A、Shared Data Layer Pass，以及“受苦义人” archetype Pilot B Content Pass A 持续反向修订。

---

# 一、QT8.2 的职责

QT8.2 不再研究“某一文明内部有什么故事”，而研究：

> **不同来源传统中反复出现、能够跨文本和跨文化比较的叙事组件，如何被定义、形成、传播、重写、组合，并在后世持续获得新意义。**

固定主链：

```text
QT8.1 来源人物／故事／文本
        ↓ 抽取
QT8.2 叙事组件
├─ motif
├─ archetype
├─ plot_pattern
└─ symbol
        ↓ 建立关系网络
文本谱系／跨文化比较／后世重写
        ↓
具体作品、历史时期、地域与媒介
```

QT8.2 是**横向抽象与关系网络层**。

它不负责：

- 重建某一来源传统的完整历史；
- 把结构相似自动解释成传播；
- 把 theme 混入 QT8.2 核心对象；
- 把文化人物写成人物百科；
- 把所有故事道具都升级成 symbol；
- 让一级母题簇承担重型内容。

---

# 二、两层架构

QT8.2 固定采用：

```text
一级母题簇
= 导航／问题域容器

具体叙事组件实体
= 真正的重型专题叶节点
```

现有 20 个一级母题簇保持相对稳定，但它们不是本体学唯一归属。一个对象可多标签关联多个簇。

---

# 三、四类对象的最小定义

## 3.1 motif｜母题

反复出现的基本叙事单元或关系。回答：**故事反复在发生什么？**

motif Pilot A 已支持：

```text
required_invariants
= 缺少后不再属于该 motif 的最低条件

optional_slots
= 高频但非必选的变体槽位
```

## 3.2 archetype｜文化原型

可被反复调用的角色／人物模型。

- `abstract_archetype`
- `named_archetype`

回答：**谁成为可重复调用的文化角色模型？**

archetype Pilot B Content Pass A 新增稳定候选：

```text
core_functions
= 跨来源实例仍保留的稳定角色功能

variable_features
= 高频但非必选的情节实现、人格特征、结局或社会位置
```

治理底线：

```text
archetype core_functions
≠ theme labels
≠ personality traits
≠ ordered plot slots
```

## 3.3 plot_pattern｜叙事结构

多个叙事节点之间稳定、可复用的顺序与关系。回答：**故事通常怎样展开？**

## 3.4 symbol｜文化意象／符号

超出单一情节道具功能，并在多个文本、时代或媒介中形成稳定可识别意义的物件、空间或意象。回答：**什么形象获得了可持续复用的文化含义？**

---

# 四、共享专题骨架

```text
00 对象主页
01 定义、边界与准入
02 来源谱系
03 内部结构与核心变体
04 跨传统分布
05 文本证据与定型
06 传播、借用与结构相似
07 与其他 QT8.2 对象的关系
08 后世重写与文化化
09 作品实例与跨媒介使用
10 阅读与研究
```

这十项是职责，不强制十个独立文件。

---

# 五、来源谱系治理

每个 QT8.2 对象必须尽可能回指 QT8.1，并显式保存 `source_status`。

至少允许：

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

因此：

```text
QT8.2 已核证一个来源实例
≠ QT8.1 已完成该来源传统
```

这允许 QT8.2 先发现跨文化组件，又不会反向冒充来源层已经建成。

至少记录：

```text
source_traditions
source_status
source_figures_or_stories
source_texts
early_witnesses
defining_texts
later_reworkings
```

Pilot B 已证明 `source_status + qt82_source_reference` 可以从 motif 复用到 archetype，而无需重造来源 schema。

---

# 六、关系模型

## 6.1 relation_type

- `direct_adaptation`
- `explicit_reference`
- `character_or_name_borrowing`
- `structural_inheritance`
- `motif_inversion`
- `symbol_reuse`
- `historical_transmission`
- `structural_similarity`
- `functional_similarity`

## 6.2 evidence_level

- `documented`
- `strongly_supported`
- `probable`
- `possible`
- `similarity_only`
- `unknown`

## 6.3 relation record 原子性

稳定规则：

> **一条 relation record 只表达一个 relation_type，并配一个 evidence_level。**

例如同一对对象既存在文本结构相似，又可能存在历史传播时，应拆成两条记录。

Pilot B 进一步强调：抽象 archetype 的 `functional_similarity` 不自动提升为 `historical_transmission`。

治理底线：

```text
relation_type ≠ evidence_level
结构相似 ≠ 历史传播
功能相似 ≠ 历史传播
高相似度 ≠ 高传播置信度
```

---

# 七、共享数据层

Shared Data Layer Pass 后，QT8.2 正式固定三种最小数据实体：

```text
qt82_source_reference
qt82_component_relation
qt82_work_reference
```

完整 schema：[[QT8.2｜共享数据层规范 V0]]

共享聚合入口：[[QT8.2｜共享数据.base]]

## 7.1 qt82_source_reference

回答：

> 这个组件从哪个 QT8.1 来源传统／故事／文本中抽取？

至少保存：

```text
component_id
component_type
source_tradition
source_story
source_text
source_status
tradition_role
canonical_work
```

Pilot A 已用 motif 验证；Pilot B Content Pass A 已用两条 archetype 来源记录完成首次跨类型复用。

## 7.2 qt82_component_relation

回答：

> 两个正式 QT8.2 component 之间存在什么语义关系？

只有 target 已经通过对应类型准入、成为正式 QT8.2 component 后，才创建正式 relation entity。候选 archetype / plot_pattern / symbol 不因另一个 Pilot 的发现而提前升级。

当前 schema 已建立，真实跨类型 relation 仍等待后续正式 target。

## 7.3 qt82_work_reference

回答：

> 某个后世作品怎样调用、改编、继承或反转这个组件？

同一作品若同时存在多个关系，应拆成多条原子 work reference。

Pilot A 已验证；archetype 类型的 work reference 留给 Pilot B Content Pass B 验证。

## 7.4 解释层 ≠ 数据层

```text
00–10 专题页面
= 解释、论证、结构化阅读

共享数据实体
= 已确认的来源／关系／作品记录
```

Base 只聚合数据实体，不把说明页伪装成关系记录。

---

# 八、文本谱系

每个 QT8.2 专题至少区分：

- 来源／早期见证
- 关键定型文本
- 重要后世重写
- 推荐阅读文本

还必须区分：

```text
故事／角色问题域形成时间
≠ 文学版本形成时间
≠ 现存抄本／泥版年代
≠ 现代研究中的抽象与命名
```

文本完整作品信息仍由唯一作品主节点承担。

---

# 九、与其他轴的职责边界

```text
QT8.1 = 来源传统、人物、故事、文本形成
QT8.2 = motif / archetype / plot_pattern / symbol
QT8.3 = 历史化文化传统
QH = 抽象主题
T = 历史阶段中的接受
R = 地域／语言中的传播与改写
M = 思潮／美学中的重组
G / 其他 QT = 具体文学类型
40 作品 = 单一作品主节点
```

---

# 十、四类模板的差异重点

| 类型 | 最重要的问题 |
|---|---|
| motif | required invariants、optional slots、变体、功能、组合方式 |
| archetype | archetype kind、core functions、variable features、来源人物、原型化过程 |
| plot_pattern | 节点顺序、必选槽位、可变槽位、结构变体 |
| symbol | 来源物象、symbol 准入、稳定意义、语义漂移、跨媒介复用 |

对应：

- [[QT8.2｜母题型专题模板 V0]]
- [[QT8.2｜文化原型型专题模板 V0]]
- [[QT8.2｜叙事结构型专题模板 V0]]
- [[QT8.2｜文化符号型专题模板 V0]]

共享数据字段不覆盖类型专属字段：

```text
motif
→ required_invariants / optional_slots

archetype
→ archetype_kind / core_functions / variable_features

plot_pattern
→ core_slots / optional_slots / repeatable_slots / terminal_variants

symbol
→ admission_evidence / stable_meanings / meaning_shifts
```

---

# 十一、Pilot 策略

V0 不批量建设 20 个母题簇，而用真实对象逐类验证。

```text
Pilot A motif
→ 洪水与灾后重建
→ CLOSED_ACCEPTED

Pilot B archetype
→ 受苦义人
→ CONTENT_PASS_A_COMPLETE
→ 下一步 Content Pass B
→ 之后所罗门王 named archetype 压力测试

Pilot C plot_pattern
→ 预言 → 逃避 → 实现

Pilot D symbol
→ 巴别塔
```

Pilot B 当前不直接进入 Acceptance：仍需后世 `qt82_work_reference` 验证，并在适当时机验证正式跨类型 `qt82_component_relation`。

---

# 十二、V0 验收条件

- [ ] 四类对象边界可实际区分
- [ ] 一个来源故事可同时映射多类对象而不冲突
- [ ] 一级母题簇可以作为多标签导航
- [ ] 来源谱系可以稳定回指 QT8.1
- [ ] `source_status` 可处理不完整来源层
- [ ] relation_type 与 evidence_level 能分离
- [ ] relation record 可保持单一关系类型
- [x] `qt82_source_reference` 已跨 motif / archetype 两类复用
- [ ] `qt82_component_relation` 完成真实跨类型复用
- [ ] `qt82_work_reference` 跨 motif / archetype 两类复用
- [ ] 文本谱系不会复制作品主节点
- [ ] abstract archetype 准入稳定
- [ ] named_archetype 不会退化成人物百科
- [ ] symbol 准入规则能挡住普通道具
- [ ] plot_pattern 不会被写成 motif 列表
- [ ] 后世作品实例只承担证据和出口
- [ ] 四种模板能够共用一套 Base / relation 数据模型

四类 Pilot 完成前：

`QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN`
