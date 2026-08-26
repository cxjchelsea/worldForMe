# QT8.2｜文化原型型专题模板 V0

> 对象类型：`archetype`
>
> 前置治理：[[QT8.2｜世界文化母题、原型与叙事结构模板总则 V0]]

---

# 00｜对象主页

首先标记：

```yaml
component_type: archetype
archetype_kind: abstract_archetype | named_archetype
```

主页至少回答：

1. 这是抽象角色原型还是命名型文化原型？
2. 它与来源人物是什么关系？
3. 它承担哪些稳定角色功能？
4. 来自哪些 QT8.1 传统／文本？
5. 何时开始超出单一来源身份？
6. 被后世怎样反复调用、改写或反转？
7. 它承载哪些 motif、plot_pattern、symbol？

---

# 01｜定义、边界与原型准入

## 抽象原型

必须描述的是稳定角色功能，而不是人格形容词。

例如：

```text
Trickster = archetype
“聪明” = trait，不是 archetype
```

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
        ↓ archetypalization
archetype（QT8.2）
```

对于抽象原型，可有多个来源人物实例；对于命名型原型，至少追踪：

- 来源人物；
- 来源故事；
- 早期文本；
- 关键定型文本；
- 早期再解释。

---

# 03｜角色功能与内部结构

建议拆成：

- 核心功能；
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

---

# 04｜原型化过程

这是 archetype 专题区别于人物百科的核心。

至少追踪：

```text
来源人物
→ 早期定型
→ 特征选择
→ 特征放大／删减
→ 跨文本复制
→ 跨文化／跨媒介再编码
→ 形成稳定文化模型
```

命名型原型必须回答“何时、如何变成原型”。

---

# 05｜文本证据与关键定型

分层记录：

- source_text
- early_reworking
- defining_reworking
- archetypalizing_text
- later_reinterpretation

若没有足够证据证明“原型化”，状态应保留为 `named_archetype_candidate`。

---

# 06｜跨传统对应与关系置信度

抽象原型可跨文明比较，但不得把功能相似误作同一历史来源。

例如：

```text
智慧王 A
智慧王 B
```

可以是 `functional_similarity`，不必是 `historical_transmission`。

---

# 07｜与其他 QT8.2 对象关系

至少记录：

- `carries_motif`
- `enacts_plot_pattern`
- `associated_with_symbol`
- `overlaps_archetype`
- `contrasts_with_archetype`

命名型原型尤其适合建立对象网络，而不是单标签归类。

---

# 08｜后世重写与身份漂移

重点观察：

- 哪些特征被保留；
- 哪些被删除；
- 哪些被反转；
- 是否从宗教人物变成文学人物；
- 是否从历史／传说人物变成抽象文化标签；
- 是否进入政治修辞、心理学、流行文化或游戏角色系统。

---

# 09｜作品实例

只收录能证明 archetype 被明确调用或稳定重组的代表作品。

每个实例标记：

```text
relation_type
evidence_level
preserved_features
modified_features
new_function
```

---

# 10｜阅读与研究

至少提供：

- 来源人物／文本路线；
- 原型化关键节点路线；
- 跨传统比较路线；
- 后世重写路线；
- 研究书目。

---

# 文化原型型完成判定

- [ ] abstract / named 类型已确定
- [ ] 来源人物与原型层已分离
- [ ] 核心角色功能可定义
- [ ] 原型化过程有证据链
- [ ] 命名型原型不是因为“著名”而建立
- [ ] 至少一个 motif / plot_pattern / symbol 关系已建立
- [ ] 跨传统相似与传播已区分
- [ ] 后世实例能说明特征如何变化
