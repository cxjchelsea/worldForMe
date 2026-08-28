---
id: WL-TEMPLATE-QC2-COMPONENT-V1
type: literature_topic_template
name: QC2 组件型专题地图模板 V1
status: FROZEN_V1
validated_by:
  - 洪水与灾后重建 (motif)
  - 受苦义人 (abstract archetype)
  - 所罗门王 (named archetype)
  - 预言→逃避→实现 (plot_pattern)
  - 巴别塔 (symbol)
---
# QC2 组件型专题地图模板 V1

> 适用范围：QC2 的正式 `motif / archetype / plot_pattern / symbol` 组件。QC2 不套用 QC1 的传统型模板：QC1 回答“从哪套传统来”，QC2 回答“跨传统反复出现了什么叙事组件”。

## 1. 固定产品壳

```text
00 <组件名>.md
01 <组件名>.canvas
02 <组件名>结构.base
03 <组件名>证据关系.base
10 核心结构/
11 来源与证据/
12 跨传统关系/
13 后世重写与阅读/
20 数据层/
```

`20 数据层` 是证据与关系记录层，不是正常阅读导航，也不替代中央 `40 作品`。

## 2. 四类组件本体

- `motif`：可复用的最小叙事单元；必须定义 required invariants 与 optional slots。
- `archetype`：可复用角色/人物模型；进一步区分 `abstract_archetype / named_archetype`。
- `plot_pattern`：具有稳定关系与顺序约束的叙事结构；slot sequence 不等于 motif 列表。
- `symbol`：已形成稳定、可复用文化含义的意象/物件/地点/形象；“故事里出现过”不足以准入。

`theme` 不作为 QC2 核心对象，仍主要属于 QH。

## 3. Cluster 与组件关系

- `QC2.1–QC2.20` 是一级问题域 / 导航 cluster，不是 component。
- 每个 component 只有一个主要主页，但可以关联多个 cluster。
- 不为矩阵整齐强迫每个 cluster 同时拥有四类 component。
- 不因对象著名就准入；必须满足对应本体的结构性准入条件。

## 4. Structure Base

正式结构节点必须显式维护：

```yaml
topic_id: WL-TOPIC-...
type: qc2_component_structure
structure_type_zh: 核心结构 | 来源与证据 | 跨传统关系 | 后世重写与阅读
sequence: <integer>
```

Base 按 `structure_type_zh` 进行语义分组，不使用 sequence 区间冒充模块。

## 5. Evidence Base 与共享数据层

固定区分：`qc2_source_reference / qc2_work_reference / qc2_component_relation`。

Evidence Base 必须以 `component_id` 过滤，并至少提供“全部证据与实例 / 来源证据 / 作品实例 / 组件关系”四类视图。真实文学作品仍来自中央 `40 作品`；不得把手稿、译本、见证材料或证据记录伪装成作品实体，不得仅凭同名标题做 canonical work 匹配。

## 6. 跨传统证据等级

至少区分：

- `weak_similarity / structural_similarity / functional_similarity`
- `possible_transmission / historical_transmission`
- `explicit_reference / direct_adaptation`
- `character_or_name_borrowing / structural_inheritance / motif_inversion`

结构相似不能自动升级为传播、借用或直接影响；跨传统边必须能回到证据记录。

## 7. Canvas

推荐稳定拓扑：`主页 → 核心结构 / 来源与证据 / 跨传统关系 / 后世重写与阅读`。Canvas 是导航和认知入口，不承担尚未被证据层支持的历史传播断言。

## 8. 内容层职责

- `10 核心结构`：定义、边界、准入、不变量/槽位或类型专属核心结构。
- `11 来源与证据`：来源谱系、文本证据、关键定型与证据等级。
- `12 跨传统关系`：跨传统分布、相似/传播区分、与其他 QC2 对象关系。
- `13 后世重写与阅读`：后世重写、作品实例、跨媒介使用、阅读与研究入口。
- `20 数据层`：原子证据/关系记录与索引。

## 9. 正式准入门槛

1. `component_type` 明确且通过对应类型准入；
2. 有真实来源/文本证据；
3. 产品壳 00/01/02/03 + 10/11/12/13 + 20 完整；
4. Structure Base 与 Evidence Base 可实际查询；
5. 跨传统关系使用证据等级；
6. 与中央 `40 作品` 对齐时完成同名消歧；
7. 不制造“全球完整清单”或虚构覆盖率。

## 10. 冻结结论

```text
QC2_COMPONENT_TOPIC_TEMPLATE_V1 = FROZEN
SHELL_REUSE_FOR_QC2.1_TO_QC2.20 = AUTHORIZED_AFTER_PER_COMPONENT_CONTENT_REVIEW
CONTENT_BLIND_COPY = NOT_AUTHORIZED
EVIDENCE_BLIND_COPY = NOT_AUTHORIZED
TITLE_ONLY_CANONICAL_MATCH = NOT_AUTHORIZED
QT8.3_MIGRATION = OUT_OF_SCOPE
```
