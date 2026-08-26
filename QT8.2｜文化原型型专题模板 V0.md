# QT8.2｜文化原型型专题模板 V0

> 对象类型：`archetype`
>
> 状态：`V0_REVISED_AFTER_SOLOMON_NAMED_ARCHETYPE_PASS_B`
>
> 前置治理：[[QT8.2｜世界文化母题、原型与叙事结构模板总则 V0]] + [[QT8.2｜共享数据层规范 V0]]

---

# 00｜对象主页

首先标记：

```yaml
type: qt82_component
component_type: archetype
archetype_kind: abstract_archetype | named_archetype
name: ""
primary_clusters: []
secondary_clusters: []
status: PILOT
source_status: {}
core_functions: []
variable_features: []
```

对于 `named_archetype`，额外使用：

```yaml
required_identity_anchors: []
supporting_identity_anchors: []
```

其中：

```text
core_functions
= 跨来源／接受实例仍必须保留的稳定角色功能

variable_features
= 高频但非必选的情节实现、人格特征、结局或社会位置

required_identity_anchors
= 保证命名人物仍被识别为“同一个文化人物”的最低身份连续

supporting_identity_anchors
= 高辨识度且长期稳定，但不等于纯身份同一性的最低条件
```

治理：

```text
core_functions
≠ ordered plot slots
≠ personality traits
≠ theme labels

identity anchors
≠ core functions
```

主页至少回答：

1. 这是抽象角色原型还是命名型文化原型？
2. 它与来源人物是什么关系？
3. 它承担哪些 `core_functions`？
4. 哪些只是 `variable_features`？
5. 若为 named archetype，哪些是 `required_identity_anchors`，哪些只是 supporting anchors？
6. 来自哪些 QT8.1 传统／文本，各自 `source_status` 是什么？
7. 何时开始超出单一来源身份？
8. 被后世怎样反复调用、改写或反转？
9. 它承载哪些 motif、plot_pattern、symbol？

---

# 01｜定义、边界与原型准入

## 抽象原型

必须描述的是稳定角色功能，而不是人格形容词或抽象问题。

例如：

```text
Trickster = archetype
“聪明” = trait，不是 archetype
“欺骗与规则” = theme / motif problem domain，不是 archetype 本身
```

Pilot B 规则：

> 抽象原型至少要能用一组 `core_functions` 跨两个实例进行核证；如果只能依赖某一具体人物的情节细节，说明抽象层次可能仍然过低。

## 命名型原型

具体人物必须满足：

- 超出单一来源文本；
- 跨时代持续被调用；
- 具有可追踪的 `required_identity_anchors`；
- 角色功能出现相对稳定抽象；
- 能在新语境中经过较大重写仍被识别；
- 有足够文本／媒介证据支持原型化。

“著名人物”不自动升级。

Pilot B.1 所罗门王进一步固定：

```text
named archetype continuity
= identity continuity
+ stable role-function continuity
+ reception-specific transformation
```

只有名字、没有稳定人物功能，可能只是 `character_or_name_borrowing`；只有相似功能、没有命名人物身份，则只能先做 abstract archetype / functional similarity。

---

# 02｜来源人物与来源谱系

必须显式区分：

```text
source_figure（QT8.1）
        ↓ archetypalization / functional abstraction
archetype（QT8.2）
```

所有来源必须继承共享 `source_status`：

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

对于抽象原型，可有多个来源人物实例；对于命名型原型，至少追踪：

- 来源人物；
- 来源故事；
- 早期文本；
- 关键定型文本；
- 早期再解释；
- 身份锚点何时被保持、改变或弱化。

来源数据使用 `qt82_source_reference`，不在说明页复制成另一套数据 schema。

---

# 03｜角色功能与内部结构

文化原型型专题必须正式区分：

```text
core_functions
+
variable_features
```

named archetype 再额外区分：

```text
required_identity_anchors
+
supporting_identity_anchors
```

建议同时观察：

- 常见行动模式；
- 与秩序的关系；
- 与权威／共同体的关系；
- 正向／负向／双重面向；
- 可被替换的角色槽位；
- 来源层高重要特征是否真的能跨接受史保留。

Pilot B.1 提醒：

> `source-figure defining feature` 不自动等于 `named-archetype core function`。

例如来源层的“圣殿建造者”可以极其重要，却未必在后世每次所罗门重写中保持核心。

---

# 04｜原型化过程

这是 archetype 专题区别于人物百科的核心。

至少追踪：

```text
来源人物／来源实例
→ 早期定型
→ 特征选择
→ 核心功能抽象
→ 特征放大／删减
→ 跨文本复制或跨来源比较
→ 跨文化／跨媒介再编码
→ 形成稳定文化模型
```

对于 `abstract_archetype`，重点是多个实例如何支持共同角色功能。

对于 `named_archetype`，必须额外回答：

```text
什么保证人物仍然是“这个人”？
哪些 identity anchors 始终存在？
哪些 source features 被后世抛弃？
哪些新功能后来反而成为高辨识特征？
```

---

# 05｜文本证据与关键定型

分层记录：

- source_text
- early_instance
- early_reworking
- defining_text
- defining_reworking
- archetypalizing_text
- later_reinterpretation

若没有足够证据证明命名型人物已经“原型化”，状态应保留为 `named_archetype_candidate`。

同时区分：

```text
角色问题域形成
≠ 某一文学版本形成
≠ 现存抄本／泥版年代
≠ 现代学术抽象与命名
```

---

# 06｜跨传统对应与关系置信度

抽象原型可跨文明比较，但不得把功能相似误作同一历史来源。

named archetype 还需要区分：

```text
character_or_name_borrowing
figure_rewriting
direct_adaptation
```

其中：

```text
character_or_name_borrowing
= 主要借人物／名字

figure_rewriting
= 同一可识别人物继续存在，但角色功能、故事环境或身份结构被系统重写

direct_adaptation
= 明确以某一来源故事／文本为主要整体改编对象
```

共享原子性规则：

```text
one relation record
=
one source
+
one target
+
one relation_type
+
one evidence_level
```

---

# 07｜与其他 QT8.2 对象关系

至少记录候选：

- `carries_motif`
- `enacts_plot_pattern`
- `associated_with_symbol`
- `overlaps_archetype`
- `contrasts_with_archetype`

正式关系使用 `qt82_component_relation`，但只有 target 已通过自身 QT8.2 准入后才能创建；candidate 不能因本专题发现而自动升级。

---

# 08｜后世重写与身份漂移

重点观察：

- 哪些 `required_identity_anchors` 被保留；
- 哪些 `supporting_identity_anchors` 被放大或弱化；
- 哪些 `core_functions` 被保留；
- 哪些 `variable_features` 被删除、替换或新增；
- 是否从宗教人物变成文学人物；
- 是否从历史／传说人物变成抽象文化标签；
- 是否进入政治修辞、心理学、流行文化或游戏角色系统。

---

# 09｜作品实例

只收录能证明 archetype 被明确调用或稳定重组的代表作品。

使用共享 `qt82_work_reference`，至少记录：

```yaml
work: ...
component_id: ...
retained_features: []
modified_features: []
relation_type: ...
evidence_level: ...
source_evidence: []
```

若同一作品同时构成两种关系，建立两条 work reference，不合并 relation_type。

---

# 10｜阅读与研究

至少提供：

- 来源人物／文本路线；
- 原型化关键节点路线；
- 跨传统比较路线；
- 后世重写路线；
- 研究书目；
- KEEP / REVISE / ADD / REMOVE 模板反馈。

---

# 文化原型型完成判定

- [ ] abstract / named 类型已确定
- [ ] 来源人物与原型层已分离
- [ ] `core_functions` 已明确
- [ ] `variable_features` 已明确
- [ ] archetype 与 theme / trait / plot_pattern 未混淆
- [ ] 至少两个来源实例已核证，或明确单来源状态
- [ ] 每个来源具有 `source_status`
- [ ] 来源已进入 `qt82_source_reference`
- [ ] 原型化／功能抽象过程有证据链
- [ ] 命名型原型不是因为“著名”而建立
- [ ] named archetype 已建立 `required_identity_anchors`
- [ ] named archetype 已区分 supporting anchors、core functions 与 variable features
- [ ] `character_or_name_borrowing / figure_rewriting / direct_adaptation` 已按证据区分
- [ ] 至少一个 motif / plot_pattern / symbol 关系已识别；正式 target 未准入时允许保持 candidate
- [ ] 跨传统 functional similarity 与 historical transmission 已区分
- [ ] relation record 遵守原子性
- [ ] 后世实例能说明 identity / core / variable features 如何变化
