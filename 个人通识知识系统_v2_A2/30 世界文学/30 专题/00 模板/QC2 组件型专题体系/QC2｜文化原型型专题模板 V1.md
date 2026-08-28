# QC2｜文化原型型专题模板 V1

> 对象类型：`archetype`
>
> 状态：`QC2_ARCHETYPE_TEMPLATE_V1_FROZEN`
>
> Reference Pilots：受苦义人（abstract）+ 所罗门王（named）。

## 00｜对象主页

```yaml
type: qc2_component
component_type: archetype
archetype_kind: abstract_archetype | named_archetype
name: ""
primary_clusters: []
secondary_clusters: []
status: active
source_status: {}
core_functions: []
variable_features: []
```

named archetype 额外使用：

```yaml
required_identity_anchors: []
supporting_identity_anchors: []
```

## 01｜定义、边界与准入

abstract archetype 描述稳定角色功能，不是人格形容词或主题标签；named archetype 必须证明人物跨文本／时代持续被调用并保留最低身份锚点。

冻结边界：

```text
core_functions ≠ personality traits ≠ theme labels ≠ ordered plot slots
identity anchors ≠ core functions
```

只有名字而无稳定人物功能，可能只是 `character_or_name_borrowing`；只有相似功能而无身份连续，优先 abstract archetype / functional similarity。

## 02｜来源人物与来源谱系

必须区分：

```text
source_figure（QC1.1）
↓ archetypalization / functional abstraction
archetype（QC2）
```

来源统一使用 `qc2_source_reference` 与 `source_status`。

## 03｜角色功能与内部结构

冻结字段：

```text
core_functions
variable_features
required_identity_anchors（named only）
supporting_identity_anchors（named only）
```

来源人物的重要特征不自动成为后世 archetype 的 core function。

## 04｜原型化过程

至少追踪：

```text
来源人物／实例
→ 早期定型
→ 特征选择
→ 核心功能抽象
→ 特征放大／删减
→ 跨文本复制或比较
→ 跨媒介再编码
→ 稳定文化模型
```

named archetype 必须额外说明什么保证“仍然是这个人”。

## 05｜文本证据与关键定型

区分 source_text / early_instance / defining_text / defining_reworking / later_reinterpretation。

若原型化证据不足，保持 candidate，不因人物著名自动升级。

## 06｜跨传统对应与关系置信度

必须区分：

```text
character_or_name_borrowing
figure_rewriting
direct_adaptation
functional_similarity
historical_transmission
```

其中 figure_rewriting 要求可识别身份锚点仍存在，同时角色功能或叙事结构被系统重写。

## 07｜与其他 QC2 对象关系

候选包括 carries_motif / enacts_plot_pattern / associated_with_symbol / overlaps_archetype / contrasts_with_archetype。

正式边遵守 meaningful target gate。

## 08｜后世重写与身份漂移

观察 identity anchors、core functions、variable features 如何被保留、削弱、反转或新增。

## 09｜作品实例

统一使用 `qc2_work_reference`。同一作品若构成多种关系，拆成多条原子记录。

## 10｜阅读与研究

至少包含来源人物／文本路线、原型化节点、跨传统比较、后世重写与研究入口。

## 完成判定

- [ ] abstract / named 类型确定
- [ ] 来源人物与 archetype 层分离
- [ ] core_functions / variable_features 明确
- [ ] named archetype 的 identity anchors 明确
- [ ] figure rewriting / name borrowing / adaptation 已区分
- [ ] functional similarity 与 historical transmission 已分离
- [ ] 后世实例可解释身份与功能如何变化

冻结结论：

```text
QC2_ARCHETYPE_TEMPLATE_V1 = FROZEN
```
