# QT8.2｜文化符号型专题模板 V0

> 对象类型：`symbol`
>
> 前置治理：[[QT8.2｜世界文化母题、原型与叙事结构模板总则 V0]]

---

# 00｜对象主页

主页首先回答：

1. 这个对象为什么已经是 symbol，而不只是故事道具？
2. 它最早／较早出现在哪些来源传统与文本？
3. 它获得稳定文化意义的关键节点是什么？
4. 它有哪些核心意义与语义变体？
5. 它和哪些 motif / archetype / plot_pattern 稳定关联？
6. 后世如何跨文本、跨媒介持续复用？

建议 frontmatter：

```yaml
type: qt82_component
component_type: symbol
name: ""
primary_clusters: []
secondary_clusters: []
status: PILOT
```

---

# 01｜定义、边界与 symbol 准入

必须通过以下准入：

- 超出单一情节功能；
- 在多个文本、版本、时代或媒介中重复调用；
- 形成相对稳定、可识别的文化意义；
- 可以追踪来源、关键定型或后世变体。

若只满足“故事里出现过”，保持为 source object，不进入 QT8.2 symbol。

## 边界问题

必须区分：

```text
物件／地点／形象本身
≠ 它在某一文本中的具体功能
≠ 后世形成的文化符号意义
```

---

# 02｜来源物象与来源谱系

按 QT8.1 记录：

- source_tradition
- source_story
- source_figure
- early_textual_witness
- early_visual_or_ritual_witness（若适用）

不要把后世已经成熟的符号义反投射到最早文本。

---

# 03｜符号化过程

这是 symbol 专题的核心。

至少追踪：

```text
情节对象／空间／意象
→ 重复出现
→ 与特定叙事关系绑定
→ 脱离单一情节仍可识别
→ 获得稳定文化意义
→ 跨媒介复用
```

例如巴别塔若进入 symbol 层，需要证明它后来不仅是《创世记》中的建筑，还持续表示语言分裂、统一工程、文明野心或知识秩序等可识别意义。

---

# 04｜核心意义与语义漂移

不要写成“这个符号代表 X”单一答案。

至少区分：

- early_meaning
- defining_meaning
- later_meanings
- inverted_meanings
- contested_meanings

并标记不同意义出现的时代、文本与媒介。

---

# 05｜文本／视觉／仪式证据

symbol 的证据不限文学文本，可记录：

- textual_witness
- visual_witness
- ritual_use
- material_culture
- later_media_reuse

但不同证据类型必须分层，不得互相替代。

---

# 06｜传播、借用与符号复用

至少区分：

```text
explicit_reference
symbol_reuse
iconographic_inheritance
historical_transmission
structural_similarity
independent_or_unknown
```

两个文化都有“树”不意味着同一个文化符号。

---

# 07｜与其他 QT8.2 对象关系

至少记录：

- `represents_motif`
- `associated_with_archetype`
- `appears_in_plot_pattern`
- `contrasts_with_symbol`
- `transforms_into_symbol`

symbol 通常是关系网络中的高复用接口，而不是独立意义容器。

---

# 08｜后世重写与跨媒介复用

重点追踪：

- 文学；
- 戏剧；
- 绘画／雕塑；
- 建筑；
- 电影／电视剧；
- 漫画／动画；
- 游戏；
- 政治／公共修辞（若确有稳定使用）。

只记录能证明稳定符号义的代表性实例。

---

# 09｜作品实例

每个实例至少标记：

```text
source_or_reference
symbolic_meaning
meaning_shift
relation_type
evidence_level
```

避免“只要画面里有这个东西就算引用”。

---

# 10｜阅读与研究

至少提供：

- 来源物象路线；
- 符号化关键节点路线；
- 语义漂移路线；
- 跨媒介路线；
- 图像学／符号研究入口。

---

# 文化符号型完成判定

- [ ] 已证明超出单一故事道具功能
- [ ] 来源物象与后世符号义已分离
- [ ] 符号化过程可追踪
- [ ] 至少两次跨文本／时代／媒介复用证据，或明确候选状态
- [ ] 核心意义与语义漂移已区分
- [ ] 与 motif / archetype / plot_pattern 至少建立一个关系
- [ ] symbol_reuse 与普通视觉相似已区分
- [ ] 后世实例具有明确证据等级
