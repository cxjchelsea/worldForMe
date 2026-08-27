# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_ACCEPTED / PILOT_B1_ACCEPTED / READY_FOR_PILOT_C`
>
> 前置：QT8.1.1 与 QT8.1.2 已作为两个差异显著的来源 Reference Topic；QT8.2 四类模板 V0 已建立；Shared Data Layer V0 已由 motif Pilot A 首轮验证，并由 archetype Pilot B / B.1 完成 abstract / named archetype 双子型压力测试。

## 1. 目标

本轮不是批量建设 20 个母题簇，而是验证四类对象模板是否真的能从 QT8.1 来源材料中抽取稳定对象，并形成可复用的跨传统关系网络。

共享数据层固定复用：

```text
qt82_source_reference
qt82_component_relation
qt82_work_reference
QT8.2｜共享数据.base
```

## 2. Pilot 顺序

### Pilot A｜motif｜已通过

**洪水与灾后重建** → `ACCEPTED_REFERENCE_MOTIF_V0`

### Pilot B｜archetype｜abstract archetype 已通过

**受苦义人** → `ACCEPTED_REFERENCE_ARCHETYPE_V0`

已验证 abstract archetype、archetype vs theme、`core_functions / variable_features`、source figure 分层、source/work schema 与 target gate。

Acceptance Review：[[QT8.2｜Pilot B 受苦义人 Acceptance Review]]

### Pilot B.1｜named archetype｜已通过

**所罗门王** → `ACCEPTED_REFERENCE_NAMED_ARCHETYPE_V0`

Pass B + Acceptance 已确认：

```text
required_identity_anchors / supporting_identity_anchors
= ACCEPTED named-archetype model

builder_and_centralizer
→ temple_builder_and_centralizer / variable_feature

core_functions
- wise_king_and_judge
- divinely_authorized_kingship
- extraordinary_knowledge_authority

figure_rewriting
= ACTIVE shared work relation
```

关系边界：

```text
character_or_name_borrowing
= 主要借人物／名字

figure_rewriting
= 同一人物持续可识别，但角色功能／故事系统被系统重写

direct_adaptation
= 以某一来源故事／文本为主要整体改编对象
```

Acceptance Review：[[个人通识知识系统_v2_A2/30 世界文学/30 专题/QT8.2.8 王权、合法性与秩序更替/所罗门王/QT8.2｜Pilot B.1 所罗门王 Acceptance Review]]

Archetype template 状态：

```text
QT8.2_ARCHETYPE_TEMPLATE_ABSTRACT_VALIDATION = PASS
QT8.2_ARCHETYPE_TEMPLATE_NAMED_VALIDATION = PASS
QT8.2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
```

### Pilot C｜plot_pattern｜下一阶段

**预言 → 逃避 → 实现**

目标不是建立“预言”主题专题，而是验证具有严格关系和顺序的叙事结构：

```text
预言／宣告
→ 规避、逃避或干预
→ 行动反而参与条件形成
→ 预言实现或等价实现
```

重点验证：

```text
core_slots
optional_slots
repeatable_slots
terminal_variants
```

并回答：

- plot_pattern 与“命运／预言” motif 的边界；
- 顺序变化到什么程度仍是同一结构；
- `structural_inheritance` 与 `structural_similarity` 的边界；
- 是否第一次产生可正式建立的 `qt82_component_relation` target。

建议优先使用已经建成的 QT8.1.2 希腊—罗马材料，例如俄狄浦斯传统，同时再寻找至少一个不同来源传统做压力测试。

### Pilot D｜symbol

**巴别塔**

重点：source object → symbol 准入、稳定意义、语义漂移与 symbol_reuse。

## 3. 验证矩阵

| 维度 | 洪水 motif | 受苦义人 abstract archetype | 所罗门王 named archetype | 预言结构 | 巴别塔 symbol |
|---|---:|---:|---:|---:|---:|
| 来源回指 QT8.1 | PASS | PASS | PASS | 必须 | 必须 |
| 多来源／多接受比较 | PASS | PASS | PASS | 强 | 初期较弱 |
| relation_type / evidence_level | PASS | PASS | PASS_AFTER_REVISION | 强 | 中 |
| 文本谱系 | PASS | PASS | PASS | 强 | 强 |
| 对象边界压力 | PASS | PASS | PASS | plot vs motif | symbol vs prop |
| 后世重写 | PASS | PASS | PASS | 强 | 强 |
| Shared Data Layer | PASS | SOURCE + WORK PASS | SOURCE + WORK PASS | 复用 | 复用 |
| component relation 跨类型 | schema only | DEFERRED_BY_TARGET_GATE | DEFERRED_BY_TARGET_GATE | 复用／候选首条正式边 | 复用 |

## 4. Freeze Gate

只有当四类对象至少各完成一个 Pilot，并且四类边界无系统性冲突、Shared Data Layer 经跨类型复用、QT8.1 回指稳定、传播证据治理可执行、abstract / named archetype 均通过、symbol 与 plot_pattern 模型均通过，才允许：

`QT8.2_TEMPLATE_V1_FREEZE_REVIEW`

当前：

```text
QT8.2_PILOT_A = CLOSED_ACCEPTED
QT8.2_PILOT_B = CLOSED_ACCEPTED
QT8.2_PILOT_B1 = CLOSED_ACCEPTED
QT8.2_ABSTRACT_ARCHETYPE_VALIDATION = PASS
QT8.2_NAMED_ARCHETYPE_VALIDATION = PASS
QT8.2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
QT8.2_IDENTITY_ANCHOR_MODEL = ACCEPTED_FOR_NAMED_ARCHETYPE_V0
QT8.2_FIGURE_REWRITING_RELATION = ACTIVE
QT8.2_SHARED_SOURCE_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_SHARED_WORK_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_COMPONENT_RELATION = DEFERRED_BY_TARGET_GATE
QT8.2_NEXT_STAGE = PILOT_C_PROPHECY_ESCAPE_FULFILLMENT
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```
