---
id: WL-QT8.2.1
type: literature_node
name: "创世、宇宙与世界秩序"
code: QT8.2.1
axis: Q
parent: WL-QT8.2
level: 4
coverage_priority: Interest
node_kind: problem_domain
anchorable: true
topic_map: null
source_version: "2.15-qt82-v1-p1-admitted"
---
 
# QT8.2.1 创世、宇宙与世界秩序

> 路径：Q轴 → QT8 → QT8.2 世界文化母题与原型 → **QT8.2.1 创世、宇宙与世界秩序**

本节点是 **QT8.2 一级母题簇／问题域导航容器**，不是 motif 专题本身。

依据冻结后的 QT8.2 Template V1：

```text
QT8.2.1～QT8.2.20
= 一级母题簇 / 问题域导航容器

motif / archetype / plot_pattern / symbol
= 真正的 component 专题实体
```

因此，本节点不要求四种 component 齐全，也不承担完整来源史或重型专题内容。

## 问题域边界

本域主要研究：

> 世界如何从尚未成形、尚未分化或尚未定序的状态，进入具有天地、空间、方向、秩序和可居住结构的宇宙。

重点包括：

- 原初状态与宇宙分化；
- 天地／空间的形成；
- 世界秩序的建立；
- 宇宙中心、垂直层级与方向结构；
- 创世材料如何形成 motif / archetype / plot_pattern / symbol；
- 不同来源传统之间的独立同构、可能传播与后世重写。

主动分流：

```text
造人／造物试错
→ 优先 QT8.2.4 造物、创造与失控

毁灭后重生
→ 优先 QT8.2.2 毁灭、灾变与世界重生

王权合法性
→ 优先 QT8.2.8 王权、合法性与秩序更替

神战／文明冲突本身
→ 优先 QT8.2.18 战争、围城、复仇与文明冲突
```

## Component Inventory

第一轮 inventory：[[QT8.2.1 Component Inventory V1]]

## M2｜天地分离

Admission Research：[[QT8.2.1 M2 天地分离 Admission Research]]

```text
QT8.2.1_M2_ADMISSION_RESEARCH = PASS
QT8.2.1_M2_COMPONENT_TYPE = motif
```

### 已正式建立

```text
component_type: motif
status: ACTIVE_V1_COMPONENT
component_acceptance: PASS
```

专题：[[../../../../30 专题/QT8.2.1 创世、宇宙与世界秩序/天地分离/00 天地分离|天地分离]]

Acceptance Review：[[../../../../30 专题/QT8.2.1 创世、宇宙与世界秩序/天地分离/QT8.2.1｜天地分离 Component Acceptance Review]]

首批数据：

```text
3 × qt82_source_reference
0 × qt82_component_relation
0 × qt82_work_reference
```

最低辨识条件：

```text
primordial_non_separation
+
cosmological_separation
+
world_space_result
```

## P1｜世界父母分离结构

Admission Research：[[QT8.2.1 P1 世界父母分离结构 Admission Research]]

已通过：

```text
QT8.2.1_P1_ADMISSION_RESEARCH = PASS
QT8.2.1_P1_COMPONENT_TYPE = plot_pattern
QT8.2.1_P1_PROMOTE_TO_TOPIC_BUILD_QUEUE = YES
```

候选 core slots：

```text
S1 WORLD_PARENTS_JOINED
→ S2 OFFSPRING_CONSTRAINED
→ S3 SEPARATION_ACTION
→ S4 COSMIC_SPACE_OPENED
```

跨传统压力测试：

```text
Māori Rangi / Papa = FULL_MATCH
Egyptian Nut / Geb / Shu = FULL_MATCH / STRONG_VARIANT
Greek Gaia / Ouranos / Kronos = STRONG_VARIANT
```

与 M2 的边界：

```text
P1 full match
→ 通常实例化 M2

M2 instance
→ 不一定满足 P1
```

P1 当前仅为 `ADMITTED_FOR_BUILD`，尚未创建正式 component relation；必须待 P1 专题通过 component acceptance 后再审查第一条自然跨类型关系。

## 下一阶段

```text
QT8.2.1_COMPONENT_INVENTORY_FIRST_PASS = COMPLETE
QT8.2.1_ACTIVE_V1_COMPONENT_COUNT = 1
QT8.2.1_SKY_EARTH_SEPARATION = ACTIVE_V1_COMPONENT
QT8.2.1_P1_ADMISSION_RESEARCH = PASS
QT8.2.1_TEMPLATE_REOPEN_REQUIRED = NO

QT8.2.1_NEXT_STAGE
= P1_WORLD_PARENTS_SEPARATION_TOPIC_BUILD

S1_ADMISSION_RESEARCH = NOT_STARTED
```

下一步建立 P1 正式 plot_pattern 专题包；通过前仍不创建与“天地分离”的正式 component relation。
