# QT8.2｜文化原型型专题模板 V0

> 对象类型：`archetype`
>
> 状态：`V0_REVISED_AFTER_SUFFERING_RIGHTEOUS_PILOT_PASS_A`
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

其中：

```text
core_functions
= 跨来源实例仍必须保留的稳定角色功能；缺失后应重新判断是否仍属于该 archetype

variable_features
= 高频但非必选的情节实现、人格特征、结局或社会位置
```

治理：

```text
core_functions
≠ ordered plot slots
≠ personality traits
≠ theme labels
```

主页至少回答：

1. 这是抽象角色原型还是命名型文化原型？
2. 它与来源人物是什么关系？
3. 它承担哪些 `core_functions`？
4. 哪些只是 `variable_features`？
5. 来自哪些 QT8.1 传统／文本，各自 `source_status` 是什么？
6. 何时开始超出单一来源身份？
7. 被后世怎样反复调用、改写或反转？
8. 它承载哪些 motif、plot_pattern、symbol？

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

Pilot B 新增工作规则：

> 抽象原型至少要能用一组 `core_functions` 跨两个实例进行核证；如果只能依赖某一具体人物的情节细节，说明抽象层次可能仍然过低。

## 命名型原型

具体人物必须满足：

- 超出单一来源文本；
- 跨时代持续被调用；
- 角色功能出现相对稳定抽象；
- 能在新语境中脱离原始故事继续被识别；
- 有足够文本／媒介证据支持原型化。

“著名人物”不自动升级。

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
- 早期再解释。

来源数据使用 `qt82_source_reference`，不在说明页复制成另一套数据 schema。

---

# 03｜角色功能与内部结构

文化原型型专题必须正式区分：

```text
core_functions
+
variable_features
```

建议同时观察：

- 常见行动模式；
- 与秩序的关系；
- 与权威／共同体的关系；
- 正向／负向／双重面向；
- 可被替换的角色槽位。

例如“智慧王”不能只写“有智慧”，而要研究：

```text
统治合法性
+ 判断／裁决
+ 知识权威
+ 神圣或超自然知识
+ 王权风险与反转
```

而王冠、具体宫廷事件或某一版本结局通常只是具体实现。

Pilot B 的“受苦义人”进一步证明：

```text
稳定角色功能
≠ 某一经典人物的完整剧情模板
```

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

对于 `abstract_archetype`，重点是多个实例如何支持共同角色功能；对于 `named_archetype`，必须回答具体人物“何时、如何变成原型”。

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

例如：

```text
智慧王 A
智慧王 B
```

可以是：

```yaml
relation_type: functional_similarity
evidence_level: documented
```

但不因此自动建立：

```text
historical_transmission
```

若存在传播证据，应另建独立 relation record。

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

命名型原型尤其适合建立对象网络，而不是单标签归类。

---

# 08｜后世重写与身份漂移

重点观察：

- 哪些 `core_functions` 被保留；
- 哪些 `variable_features` 被删除或替换；
- 哪些特征被反转；
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
- [ ] 至少一个 motif / plot_pattern / symbol 关系已识别；正式 target 未准入时允许保持 candidate
- [ ] 跨传统 functional similarity 与 historical transmission 已区分
- [ ] relation record 遵守原子性
- [ ] 后世实例能说明 core / variable features 如何变化
