# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_ACCEPTED / PILOT_B1_READY_FOR_ACCEPTANCE`
>
> 前置：QT8.1.1 与 QT8.1.2 已作为两个差异显著的来源 Reference Topic；QT8.2 四类模板 V0 已建立；Shared Data Layer V0 已由 motif Pilot A 首轮验证，并由 archetype Pilot B / B.1 继续做跨类型与 named archetype 压力测试。

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

### Pilot B.1｜named archetype｜验收准备完成

**所罗门王**

当前：`CONTENT_PASS_A_COMPLETE / CONTENT_PASS_B_COMPLETE / READY_FOR_ACCEPTANCE`

Pass B 已回答三个决定性问题：

```text
1. identity_anchor
→ SUPPORTED
→ 拆为 required_identity_anchors / supporting_identity_anchors

2. builder_and_centralizer
→ NOT_CORE
→ temple_builder_and_centralizer / variable_feature

3. figure_rewriting
→ SUPPORTED
→ 已加入 Shared Data Layer work relation vocabulary
```

当前 named archetype 模型：

```text
required identity continuity
+
supporting identity anchors
+
stable core-function bundle
+
reception-specific variable features
=
named archetype continuity
```

当前所罗门 core functions：

```text
wise_king_and_judge
divinely_authorized_kingship
extraordinary_knowledge_authority
```

关系治理：

```text
character_or_name_borrowing
= 主要借人物／名字

figure_rewriting
= 同一人物持续可识别，但角色功能／故事系统被系统重写

direct_adaptation
= 以某一来源故事／文本为主要整体改编对象
```

真实数据调整：

```text
Testament of Solomon
→ figure_rewriting / documented

Quranic Sulayman traditions
→ figure_rewriting / documented

Key of Solomon
→ character_or_name_borrowing / documented

Josephus Antiquities 8.42–49
→ explicit_reference / documented
```

下一步：**Pilot B.1 Acceptance Review**。

只有该验收通过，archetype 类型才算同时覆盖 abstract / named 两个子型。

### Pilot C｜plot_pattern

**预言 → 逃避 → 实现**

重点：`core_slots / optional_slots / repeatable_slots / terminal_variants` 与 plot vs motif 边界。

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
| 对象边界压力 | PASS | PASS | PASS_SO_FAR | plot vs motif | symbol vs prop |
| 后世重写 | PASS | PASS | PASS | 强 | 强 |
| Shared Data Layer | PASS | SOURCE + WORK PASS | SOURCE + WORK PASS | 复用 | 复用 |
| component relation 跨类型 | schema only | DEFERRED_BY_TARGET_GATE | DEFERRED_BY_TARGET_GATE | 复用 | 复用 |

## 4. Freeze Gate

只有当四类对象至少各完成一个 Pilot，并且四类边界无系统性冲突、Shared Data Layer 经跨类型复用、QT8.1 回指稳定、传播证据治理可执行、abstract / named archetype 均通过、symbol 与 plot_pattern 模型均通过，才允许：

`QT8.2_TEMPLATE_V1_FREEZE_REVIEW`

当前：

```text
QT8.2_PILOT_A = CLOSED_ACCEPTED
QT8.2_PILOT_B = CLOSED_ACCEPTED
QT8.2_PILOT_B1_CONTENT_PASS_A = COMPLETE
QT8.2_PILOT_B1_CONTENT_PASS_B = COMPLETE
QT8.2_ABSTRACT_ARCHETYPE_VALIDATION = PASS
QT8.2_NAMED_ARCHETYPE_VALIDATION = READY_FOR_ACCEPTANCE
QT8.2_IDENTITY_ANCHOR_MODEL = SUPPORTED
QT8.2_FIGURE_REWRITING_RELATION = ACTIVE
QT8.2_SHARED_SOURCE_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_SHARED_WORK_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_COMPONENT_RELATION = DEFERRED_BY_TARGET_GATE
QT8.2_NEXT_STAGE = PILOT_B1_ACCEPTANCE_REVIEW
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```
