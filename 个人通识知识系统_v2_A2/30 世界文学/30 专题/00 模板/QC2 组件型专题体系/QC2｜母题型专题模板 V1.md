# QC2｜母题型专题模板 V1

> 对象类型：`motif`
>
> 状态：`QC2_MOTIF_TEMPLATE_V1_FROZEN`
>
> Reference Pilot：洪水与灾后重建。

## 00｜对象主页

建议 frontmatter：

```yaml
type: qc2_component
component_type: motif
name: ""
primary_clusters: []
secondary_clusters: []
status: active
source_status: {}
required_invariants: []
optional_slots: []
```

主页回答：这个 motif 是什么、最低辨识条件是什么、来自哪些来源传统、有哪些变体与后世重写。

## 01｜定义、边界与准入

`required_invariants` 是缺失后不再属于该 motif 的最低条件；`optional_slots` 是高频但非必选变体。

冻结边界：

```text
required_invariants
≠ optional_slots
≠ ordered plot slots
≠ theme labels
```

若一组槽位形成稳定顺序，应升级为 plot_pattern candidate，而不是继续扩张 motif 定义。

## 02｜来源谱系

按 QC1.1 来源传统组织，所有来源使用共享 `qc2_source_reference` 并记录 `source_status`。

允许多中心起源、独立同构、可能传播与未知关系；禁止因为多个文明存在相似 motif 就强行设定单一起源。

## 03｜内部结构与核心变体

至少记录：

- required_invariants
- optional_slots
- 可变角色
- 可变因果
- 可变结局
- 与其他 motif 的组合方式

## 04｜跨传统分布

区分：

```text
high structural match
partial shared structure
surface similarity
historical transmission supported
relationship unknown
```

固定：`cross_tradition_distribution ≠ transmission_history`。

## 05｜文本证据与定型

至少区分：

```text
early_witness
defining_text
defining_reworking
later_reworking
recommended_reading
```

并区分故事传统形成、文学版本形成与现存抄本年代。

## 06｜传播、借用与结构相似

共享治理：

```text
one relation record = one relation_type + one evidence_level
```

结构相似与历史传播必须拆分记录。

## 07｜与其他 QC2 对象关系

候选包括：

```text
co_occurs_with_motif
carried_by_archetype
organized_by_plot_pattern
represented_by_symbol
```

只有 target 已正式准入且关系具有解释价值时，才创建 `qc2_component_relation`。

## 08｜后世重写与文化化

区分 direct adaptation、explicit reference、structural inheritance、motif inversion、hybridization。

## 09｜作品实例

统一使用 `qc2_work_reference`。重点记录保留了哪些 invariants、修改了哪些 slots，以及 relation_type / evidence_level。

## 10｜阅读与研究

至少包含来源文本路线、跨传统比较路线、后世重写路线与研究入口。

## 完成判定

- [ ] 最小 motif 定义明确
- [ ] required_invariants / optional_slots 已分离
- [ ] 与 theme / plot_pattern 边界清楚
- [ ] 来源均有 source_status
- [ ] 传播与结构相似分离
- [ ] relation record 保持原子性
- [ ] 后世实例具有明确关系类型与证据等级

冻结结论：

```text
QC2_MOTIF_TEMPLATE_V1 = FROZEN
```
