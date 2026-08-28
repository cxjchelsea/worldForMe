# QC2｜世界文化母题、原型与叙事结构模板总则 V1

> 状态：`QC2_TEMPLATE_V1_FROZEN`
>
> 适用范围：QC2 横向抽象层中的 motif / archetype / plot_pattern / symbol 专题。
>
> 验证依据：Pilot A / B / B.1 / C / D + Four-Type Cross-Template Conflict and Shared Data Review。

---

# 一、QC2 的职责

QC2 研究不同来源传统中反复出现、能够跨文本与跨文化比较的叙事组件，回答它们如何被定义、形成、传播、重写、组合并持续获得新意义。

固定主链：

```text
QC1.1 来源人物／故事／文本
        ↓ 抽取
QC2 叙事组件
├─ motif
├─ archetype
├─ plot_pattern
└─ symbol
        ↓
关系网络／文本谱系／跨文化比较／后世重写
```

QC2 是横向抽象层，不负责重建单一文明的完整来源史，不把 theme 纳入核心对象，不把结构相似自动解释为历史传播。

---

# 二、两层架构

```text
QC2.1～QC2.20
= 一级母题簇／问题域导航容器

具体 component
= 真正的重型专题叶节点
```

一级母题簇不是本体学唯一归属。一个 component 只能有一个主要归属地，但可以通过标签与正式关系连接多个问题域。

Pilot A / B / B.1 / C / D 仅表示模板验证顺序，不等于 QC2.x 的建设顺序。

---

# 三、四类对象的冻结定义

## motif

回答：**故事反复在发生什么基本叙事单元或关系？**

冻结字段：

```text
required_invariants
optional_slots
```

治理：`required_invariants ≠ ordered plot slots`。

## archetype

回答：**谁成为可反复调用的文化角色模型？**

冻结字段：

```text
archetype_kind: abstract_archetype | named_archetype
core_functions
variable_features
```

named archetype 额外使用：

```text
required_identity_anchors
supporting_identity_anchors
```

治理：`core_functions ≠ personality traits ≠ ordered plot slots`；identity anchors 与 core functions 分离。

## plot_pattern

回答：**故事怎样以稳定关系和顺序展开？**

冻结字段：

```text
core_slots
optional_slots
repeatable_slots
terminal_variants
causal_variants
```

治理：`plot_pattern = relation + sequence`，不是 motif 列表。

## symbol

回答：**什么对象、空间或意象获得了跨文本、时代与媒介可识别的文化意义？**

冻结字段：

```text
admission_evidence
stable_meanings
meaning_shifts
```

治理：

```text
source object / source-story function ≠ later symbol
symbol continuity ≠ literal object continuity ≠ visual-form continuity
```

---

# 四、共享专题职责骨架

所有类型至少覆盖以下职责：

```text
00 对象主页
01 定义、边界与准入
02 来源谱系
03 类型专属内部结构
04 分布／形成／结构功能
05 文本与关键定型证据
06 传播、借用、继承与相似
07 与其他 QC2 对象关系
08 后世重写／变形／文化化
09 作品实例与跨媒介证据
10 阅读与研究
20 数据层
```

职责冻结，不强制每项都是独立文件；二级组织可按类型适配。

---

# 五、来源治理

每个 component 应尽可能回指 QC1.1，并保存 `source_status`：

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

固定：

```text
QC2 已核证来源实例
≠ QC1.1 对应来源专题已完成
```

禁止把后世成熟解释倒灌成来源文本唯一含义。

---

# 六、Shared Data Layer

V1 固定三类共享实体：

```text
qc2_source_reference
qc2_component_relation
qc2_work_reference
```

完整规范：[[QC2｜共享数据层规范 V1]]。

解释层与数据层保持分离；共享 Base：[[QC2｜共享数据.base]]。

冻结原子性规则：

```text
one relation record
= one relation_type
+ one evidence_level
```

---

# 七、关系与证据治理

必须区分：

```text
relation_type ≠ evidence_level
structural_similarity ≠ structural_inheritance
functional_similarity ≠ historical_transmission
symbol_reuse ≠ historical_transmission
visual similarity ≠ iconographic_inheritance
character_or_name_borrowing ≠ figure_rewriting ≠ direct_adaptation
motif_inversion ≠ plot_pattern_inversion
```

`iconographic_inheritance` 不进入 V1 冻结 vocabulary；只有 documented visual chain 出现后才允许 amendment review。

---

# 八、类型专属字段隔离

类型字段必须保持 `component_type` 语境：

```text
motif → required_invariants / optional_slots
archetype → core_functions / variable_features / identity anchors
plot_pattern → core/optional/repeatable slots / terminal/causal variants
symbol → admission_evidence / stable_meanings / meaning_shifts
```

同名字段不自动拥有跨类型统一语义。例如 motif.optional_slots 与 plot_pattern.optional_slots 必须由各自模板解释。

---

# 九、component relation promotion gate

正式 `qc2_component_relation` 只有在：

1. source 与 target 均已完成自身 component 准入；
2. 关系具有独立解释价值；
3. 证据等级可明确；
4. 不是为了填 schema 或 checklist 强制造边；

时才创建。

V1 冻结时真实记录仍为 `0 × qc2_component_relation`。该缺口被接受为：

```text
DEFERRED_BY_MEANINGFUL_TARGET_GATE
```

未来首次自然产生的真实跨类型 component relation，应先验证其与 V1 vocabulary 的兼容性；如需新增 relation type，走 Governance Amendment，不静默修改 V1。

---

# 十、与其他层职责边界

```text
QC1.1 = 来源传统、人物、故事、文本形成
QC2 = motif / archetype / plot_pattern / symbol
QT8.3 = 历史化文化传统
QH = 抽象主题
T = 历史阶段中的接受
R = 地域／语言传播与改写
M = 思潮／美学中的重组
G / 其他 QT = 文学类型
40 作品 = 单一作品主节点
```

---

# 十一、V1 Reference Pilots

```text
Pilot A｜洪水与灾后重建
→ motif
→ ACCEPTED_REFERENCE_MOTIF_V0

Pilot B｜受苦义人
→ abstract_archetype
→ ACCEPTED_REFERENCE_ARCHETYPE_V0

Pilot B.1｜所罗门王
→ named_archetype
→ ACCEPTED_REFERENCE_NAMED_ARCHETYPE_V0

Pilot C｜预言→逃避→实现
→ plot_pattern
→ ACCEPTED_REFERENCE_PLOT_PATTERN_V0

Pilot D｜巴别塔
→ symbol
→ ACCEPTED_REFERENCE_SYMBOL_V0
```

这些对象是模板验证参考，不是未来内容建设的固定顺序。

---

# 十二、Freeze 后变更规则

可持续增补而无需模板升级：

- 新 component；
- 新来源与 work reference；
- 新研究书目；
- 已有 component 的内容证据；
- 在不改变一级职责的前提下适配二级页面；
- Shared Base 的非破坏性辅助视图。

以下变化需要 `V1.x / V2` 或 Governance Amendment：

- 四类 component 的对象边界；
- 类型核心字段语义；
- 三类 Shared Data 实体；
- relation atomicity；
- source_status 核心治理；
- promotion gate；
- relation vocabulary 的新增／删除／语义改变；
- 类型专属 optional extension 的跨类型提升。
