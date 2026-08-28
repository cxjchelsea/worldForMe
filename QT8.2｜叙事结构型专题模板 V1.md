# QT8.2｜叙事结构型专题模板 V1

> 对象类型：`plot_pattern`
>
> 状态：`QT8.2_PLOT_PATTERN_TEMPLATE_V1_FROZEN`
>
> Reference Pilot：预言→逃避→实现。

## 00｜对象主页

```yaml
type: qt82_component
component_type: plot_pattern
name: ""
primary_clusters: []
secondary_clusters: []
status: active
source_status: {}
core_slots: []
optional_slots: []
repeatable_slots: []
terminal_variants: []
causal_variants: []
```

主页必须用节点顺序表达对象，而不是主题词集合。

## 01｜定义、边界与准入

plot_pattern 必须是**关系 + 顺序**。

```text
S1 → S2 → S3 ...
```

冻结边界：

```text
slot sequence ≠ motif list
causal_variants ≠ core_slots
```

若只有几个 motif 共现而无稳定顺序，不构成 plot_pattern。

## 02｜来源实例

来源统一使用 `qt82_source_reference`，并记录实际节点序列、匹配程度与 source_status。

跨传统结构匹配不自动证明历史传播。

## 03｜槽位与变体

必须区分：

```text
core_slots
optional_slots
repeatable_slots
terminal_variants
causal_variants
```

只有多个实例都要求某一节点，才考虑升级为 core slot。

## 04｜结构功能

记录该结构在叙事中承担的功能，但功能相似不自动代表历史传播。

## 05｜文本证据与关键定型

区分 early_instance / defining_instance / canonical_reworking / later_structural_inheritance。

不要轻易声称某文本“发明”一个可能更早存在的结构。

## 06｜传播、结构继承与相似

严格区分：

```text
structural_inheritance
historical_transmission
structural_similarity
functional_similarity
```

冻结规则：

```text
high slot match ≠ structural_inheritance
```

只有稳定结构匹配而无独立继承证据时，使用 `structural_similarity`。

## 07｜与其他 QT8.2 对象关系

候选包括 contains_motif / typically_enacted_by_archetype / associated_with_symbol / variant_of_plot_pattern / inverts_plot_pattern。

正式边遵守 meaningful target gate。

## 08｜后世变形与反结构

追踪节点删减、倒置、增加、重复、循环化、开放结尾、结果提前揭示、结构反转与 causal variant 改变。

`motif_inversion ≠ plot_pattern_inversion`。

## 09｜作品实例

统一使用 `qt82_work_reference`，并允许 plot-pattern-specific optional fields：

```yaml
matched_slots: []
missing_slots: []
added_slots: []
```

这些字段不要求 motif / archetype / symbol 使用。

## 10｜阅读与研究

至少包含来源实例路线、跨传统压力测试、slot/causal variant 比较、后世 inheritance/similarity/inversion 与叙事学研究入口。

## 完成判定

- [ ] 最小节点序列明确
- [ ] core / optional / repeatable / terminal / causal 已区分
- [ ] motif 与 plot_pattern 未混淆
- [ ] structural_inheritance 与 structural_similarity 已区分
- [ ] 后世实例可按 matched / missing / added slots 比较
- [ ] relation/evidence 保持原子性

冻结结论：

```text
QT8.2_PLOT_PATTERN_TEMPLATE_V1 = FROZEN
```
