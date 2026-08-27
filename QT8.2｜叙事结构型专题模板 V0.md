# QT8.2｜叙事结构型专题模板 V0

> 对象类型：`plot_pattern`
>
> 状态：`V0_REVISED_AFTER_PROPHECY_PILOT_PASS_A`
>
> 前置治理：[[QT8.2｜世界文化母题、原型与叙事结构模板总则 V0]] + [[QT8.2｜共享数据层规范 V0]]

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
source_status: {}
core_slots: []
optional_slots: []
repeatable_slots: []
terminal_variants: []
```

主页至少回答：

1. 该结构的最小节点序列是什么？
2. 哪些节点是必选，哪些可省略？
3. 哪些节点允许重复？
4. 有哪些 terminal variants？
5. 哪些角色槽位可替换？
6. 来源于哪些 QT8.1 故事实例，各自 `source_status` 是什么？
7. 与哪些 motif / archetype 经常共现？
8. 后世有哪些结构继承或反转？

---

# 01｜定义、边界与结构准入

plot_pattern 必须是**关系 + 顺序**，而不是一组 motif 标签。

例如：

```text
预言 → 规避 → 预言实现
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

Pilot C 新增工作规则：

> 结构准入必须检查前一槽位是否真正触发后一槽位，而不能只因为几个 motif 在同一个故事里共同出现就判为 plot pattern。

---

# 02｜来源实例

按 QT8.1 来源传统记录真实故事实例，并继承共享 `source_status`。

建议表：

| 来源传统 | 故事／人物 | 实际节点序列 | 匹配程度 | source_status |
|---|---|---|---|---|

匹配程度可分：

- full_match
- strong_variant
- partial_variant
- weak_similarity

不要求所有实例完全同构。

来源数据使用共享 `qt82_source_reference`，不重新设计 plot-pattern 专属来源 schema。

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

Pilot C Pass A 进一步暴露一个候选维度：

```text
causal_variants
```

它用于回答不同实例中槽位之间的因果强度，例如：

```text
fulfilled_despite_avoidance
vs
fulfilled_through_avoidance
```

当前仅为候选，不在单一 Pass A 中固定为模板必选字段；留给 Pass B 压力测试。

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

Pilot C 工作门槛：正式 `structural_inheritance` 至少需要核心槽位可识别、节点顺序保持，并有足够证据支持结构继承／重组；否则保留为 similarity。

---

# 07｜与其他 QT8.2 对象关系

至少记录候选：

- `contains_motif`
- `typically_enacted_by_archetype`
- `associated_with_symbol`
- `variant_of_plot_pattern`
- `inverts_plot_pattern`

正式关系使用共享 `qt82_component_relation`，只有 target 已完成自身准入且关系有实际解释价值时才建立。

```text
candidate relation
≠ formal component relation
```

---

# 08｜后世变形与反结构

追踪：

- 节点删减；
- 节点倒置；
- 节点重复；
- 循环化；
- 开放结尾；
- 将结果提前揭示；
- 对经典结构的有意反转。

`motif_inversion` 与 `plot_pattern_inversion` 要区分。

---

# 09｜作品实例

每个作品实例至少需要能够说明：

```text
matched_slots
missing_slots
added_slots
relation_type
evidence_level
```

Shared Data Layer 的正式实体仍使用 `qt82_work_reference`。

Pilot C Pass A 暴露出一个 schema 候选：plot-pattern 的 work reference 可能需要允许：

```yaml
matched_slots: []
missing_slots: []
added_slots: []
```

当前不修改共享 schema；Pass B 用真实后世作品验证后再决定是否作为类型专属扩展字段。

---

# 10｜阅读与研究

至少包含：

- 来源实例路线；
- 结构变体路线；
- 后世继承／反转路线；
- 叙事学研究入口；
- KEEP / REVISE / ADD / REMOVE 模板反馈。

---

# 叙事结构型完成判定

- [ ] 可写出最小节点序列
- [ ] `core_slots / optional_slots / repeatable_slots / terminal_variants` 已区分
- [ ] 至少两个来源实例或明确单来源状态
- [ ] 每个来源具有 `source_status`
- [ ] 来源已进入 `qt82_source_reference`
- [ ] motif 与 plot_pattern 未混淆
- [ ] 主要变体已识别
- [ ] structural_inheritance 与 similarity 已区分
- [ ] 至少识别一个 archetype / motif 关系；正式 target 未准入或价值不足时允许保持 candidate
- [ ] 后世实例可按节点级比较
- [ ] relation record 遵守原子性
