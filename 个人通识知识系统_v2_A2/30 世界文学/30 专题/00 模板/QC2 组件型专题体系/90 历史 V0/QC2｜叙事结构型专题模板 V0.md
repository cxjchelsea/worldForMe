# QC2｜叙事结构型专题模板 V0

> 对象类型：`plot_pattern`
>
> 状态：`V0_VALIDATED_BY_PROPHECY_REFERENCE_PLOT_PATTERN`
>
> 前置治理：[[QC2｜世界文化母题、原型与叙事结构模板总则 V0]] + [[QC2｜共享数据层规范 V0]]

---

# 00｜对象主页

主页必须用**节点顺序**表达对象，而不是一句主题描述。

建议 frontmatter：

```yaml
type: qc2_component
component_type: plot_pattern
name: ""
primary_clusters: []
secondary_clusters: []
status: PILOT | ACCEPTED_REFERENCE_PLOT_PATTERN_V0
source_status: {}
core_slots: []
optional_slots: []
repeatable_slots: []
terminal_variants: []
causal_variants: []
```

其中：

```text
core_slots
= 缺失后应重新判断是否仍属于同一 plot pattern 的最低顺序节点

optional_slots
= 高频但非必选的结构节点

repeatable_slots
= 可在结构中重复出现的节点／动作

terminal_variants
= 结尾如何完成、失败、反转或开放

causal_variants
= 相同 slot 顺序下，节点之间可能存在的不同因果组织方式
```

治理：

```text
causal_variants ≠ core_slots
slot sequence ≠ motif list
```

主页至少回答：

1. 最小节点序列是什么？
2. 哪些节点必选、可省略或可重复？
3. 是否存在不同 causal variants？
4. 来源于哪些 QC1.1 故事实例，各自 source_status 是什么？
5. 有哪些 terminal variants？
6. 与哪些 motif / archetype / symbol 共现？
7. 后世有哪些 structural inheritance、structural similarity 或 inversion？

---

# 01｜定义、边界与结构准入

plot_pattern 必须是**关系 + 顺序**，而不是一组 motif 标签。

```text
预言 → 规避 → 预言实现
= plot_pattern

预言、命运、自由意志
= motif / problem domain，不是 plot_pattern
```

最小结构统一用抽象槽位：

```text
S1 → S2 → S3 ...
```

并说明每个槽位功能。

结构准入必须检查前一槽位是否真正触发后一槽位，而不能只因为几个 motif 在同一个故事里共同出现就判为 plot pattern。

---

# 02｜来源实例

按 QC1.1 来源传统记录真实故事实例，并继承共享 `source_status`。

建议表：

| 来源传统 | 故事／人物 | 实际节点序列 | 匹配程度 | source_status |
|---|---|---|---|---|

匹配程度可分：

```text
full_match
strong_variant
partial_variant
weak_similarity
```

来源数据使用 `qc2_source_reference`。

跨传统结构匹配不自动证明历史传播。

---

# 03｜必选槽位、可变槽位与变体

必须区分：

```text
core_slots
optional_slots
repeatable_slots
terminal_variants
causal_variants
```

Pilot C 已验证：相同 core-slot 顺序可以具有不同因果机制。例如：

```text
fulfilled_despite_avoidance
= 尽管规避发生，结果仍实现

fulfilled_through_avoidance
= 规避行为本身进入结果实现的因果链
```

只有多个实例都要求某因果节点时，才考虑把它升级为 core slot。

---

# 04｜结构功能

分析该结构在叙事中承担的功能，例如：

- 制造反讽；
- 组织成长；
- 解释合法性；
- 建立循环感；
- 将私人危机转化为共同体秩序；
- 通过反复失败制造悲剧必然性。

功能相似不自动代表历史传播。

---

# 05｜文本证据与关键定型

至少区分：

```text
early_instance
defining_instance
canonical_reworking
later_structural_inheritance
```

不要声称某一文本“发明”一个可能更早存在的结构，除非证据充分。

---

# 06｜传播、结构继承与相似

严格区分：

```text
structural_inheritance
historical_transmission
structural_similarity
functional_similarity
```

Pilot C 固定：

```text
high slot match
≠ structural_inheritance
```

如果只证明后世作品稳定实例化同一结构，而没有独立继承／传播证据，使用：

```text
structural_similarity
```

`structural_inheritance` 必须另有文本、作者、改编史或传播链支持。

---

# 07｜与其他 QC2 对象关系

至少记录候选：

- `contains_motif`
- `typically_enacted_by_archetype`
- `associated_with_symbol`
- `variant_of_plot_pattern`
- `inverts_plot_pattern`

正式关系使用 `qc2_component_relation`，并遵守 target promotion gate。

---

# 08｜后世变形与反结构

追踪：

- 节点删减；
- 节点倒置；
- 节点增加；
- 节点重复；
- 循环化；
- 开放结尾；
- 结果提前揭示；
- 对经典结构的有意反转；
- causal variant 的改变。

`motif_inversion` 与 `plot_pattern_inversion` 必须区分。

---

# 09｜作品实例

使用共享 `qc2_work_reference`。

对于 `component_type: plot_pattern`，允许可选扩展：

```yaml
matched_slots: []
missing_slots: []
added_slots: []
```

并保留通用字段：

```yaml
retained_features: []
modified_features: []
relation_type: structural_inheritance | structural_similarity | plot_pattern_inversion | ...
evidence_level: documented | strongly_supported | probable | possible | similarity_only | unknown
source_evidence: []
```

只有结构匹配而无历史继承证据时，优先 `structural_similarity`。

---

# 10｜阅读与研究

至少包含：

- 来源实例路线；
- 跨传统压力测试；
- slot 与 causal variant 比较；
- 后世 inheritance / similarity / inversion 路线；
- 叙事学研究入口；
- KEEP / REVISE / ADD / REMOVE 模板反馈。

---

# 叙事结构型完成判定

- [ ] 可写出最小节点序列
- [ ] core / optional / repeatable / terminal slots 已区分
- [ ] causal variants 已检查
- [ ] 至少两个来源实例或明确单来源状态
- [ ] 至少一次跨传统来源压力测试，或明确为何暂不能做
- [ ] 每个来源具有 source_status
- [ ] 来源已进入 qc2_source_reference
- [ ] motif 与 plot_pattern 未混淆
- [ ] 主要变体已识别
- [ ] structural_inheritance 与 structural_similarity 已区分
- [ ] 后世实例可按 matched / missing / added slots 比较
- [ ] work reference 遵守 relation/evidence 原子性
- [ ] 至少一个 archetype / motif / symbol 关系已识别；target 未准入时允许保持 candidate

---

# V0 验证状态

Pilot C｜预言→逃避→实现 已正式通过 Acceptance Review：

```text
QC2_PLOT_PATTERN_TEMPLATE_V0
= VALIDATED_BY_ONE_REFERENCE_PLOT_PATTERN
```

该状态不等于 Template V1 Freeze；symbol Pilot 与四类型跨模板冲突检查仍未完成。