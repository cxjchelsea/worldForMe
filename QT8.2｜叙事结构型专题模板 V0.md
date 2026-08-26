# QT8.2｜叙事结构型专题模板 V0

> 对象类型：`plot_pattern`
>
> 前置治理：[[QT8.2｜世界文化母题、原型与叙事结构模板总则 V0]]

---

# 00｜对象主页

主页必须用**节点顺序**表达对象，而不是一句主题描述。

建议 frontmatter：

```yaml
type: qt82_component
component_type: plot_pattern
name: ""
primary_clusters: []
secondary_clusters: []
status: PILOT
```

主页至少回答：

1. 该结构的最小节点序列是什么？
2. 哪些节点是必选，哪些可省略？
3. 哪些角色槽位可替换？
4. 来源于哪些 QT8.1 故事实例？
5. 有哪些稳定变体？
6. 与哪些 motif / archetype 经常共现？
7. 后世有哪些结构继承或反转？

---

# 01｜定义、边界与结构准入

plot_pattern 必须是**关系 + 顺序**，而不是一组 motif 标签。

例如：

```text
预言 → 逃避 → 反而促成预言实现
```

是 plot_pattern；

```text
预言、命运、自由意志
```

不是。

## 最小结构

用抽象槽位表达：

```text
S1 → S2 → S3 ...
```

并说明每个槽位的功能。

---

# 02｜来源实例

按 QT8.1 来源传统记录真实故事实例。

建议表：

| 来源传统 | 故事／人物 | 实际节点序列 | 匹配程度 |
|---|---|---|---|

匹配程度可分：

- full_match
- strong_variant
- partial_variant
- weak_similarity

不要求所有实例完全同构。

---

# 03｜必选槽位、可变槽位与变体

至少区分：

```text
core_slots
optional_slots
repeatable_slots
terminal_variants
```

例如“离乡—试炼—归乡”可能具有：

```text
离开原空间（core）
边界穿越（optional）
多次试炼（repeatable）
返回／失败归返／拒绝归返（terminal variants）
```

这一步是 plot_pattern 模板的核心。

---

# 04｜结构功能

分析该结构在叙事中常承担什么功能，例如：

- 制造反讽；
- 组织成长；
- 解释合法性；
- 建立循环感；
- 将私人危机转化为共同体秩序；
- 通过反复失败制造悲剧必然性。

功能相似不自动代表历史传播。

---

# 05｜文本证据与关键定型

记录哪些文本使这种结构获得高可识别形态。

至少区分：

- early_instance
- defining_instance
- canonical_reworking
- later_structural_inheritance

不要声称某一文本“发明”一个可能更早存在的叙事结构，除非证据足够。

---

# 06｜传播、结构继承与相似

特别区分：

```text
structural_inheritance
historical_transmission
structural_similarity
functional_similarity
```

后世作品若只共享几个节点，不应自动标为 structural_inheritance。

---

# 07｜与其他 QT8.2 对象关系

至少记录：

- `contains_motif`
- `typically_enacted_by_archetype`
- `associated_with_symbol`
- `variant_of_plot_pattern`
- `inverts_plot_pattern`

例如：

```text
预言→逃避→实现
├─ motif：预言、命运冲突
├─ archetype：被预言者、悲剧英雄
└─ 可与“弑父／篡位”等 motif 组合，但两者不是同一对象
```

---

# 08｜后世变形与反结构

追踪：

- 节点删减；
- 节点倒置；
- 循环化；
- 开放结尾；
- 将结果提前揭示；
- 对经典结构的有意反转。

`motif_inversion` 与 `plot_pattern_inversion` 要区分。

---

# 09｜作品实例

每个作品实例至少记录：

```text
matched_slots
missing_slots
added_slots
relation_type
evidence_level
```

作品只是验证结构的证据，不在这里重做完整作品分析。

---

# 10｜阅读与研究

至少包含：

- 来源实例路线；
- 结构变体路线；
- 后世继承／反转路线；
- 叙事学研究入口。

---

# 叙事结构型完成判定

- [ ] 可写出最小节点序列
- [ ] core / optional / repeatable 槽位已区分
- [ ] 至少两个来源实例或明确单来源状态
- [ ] motif 与 plot_pattern 未混淆
- [ ] 主要变体已识别
- [ ] structural_inheritance 与 similarity 已区分
- [ ] 至少建立一个 archetype / motif 关系
- [ ] 后世实例可按节点级比较
