# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_ACCEPTED / READY_FOR_NAMED_ARCHETYPE_PRESSURE_TEST`
>
> 前置：QT8.1.1 与 QT8.1.2 已作为两个差异显著的来源 Reference Topic；QT8.2 四类模板 V0 已建立；Shared Data Layer V0 已由 motif Pilot A 首轮验证，并由 archetype Pilot B 完成 source / work 两类实体的跨类型复用验证。

## 1. 目标

本轮不是批量建设 20 个母题簇，而是验证四类对象模板是否真的能从 QT8.1 来源材料中抽取稳定对象，并形成可复用的跨传统关系网络。

共享数据层固定复用：

```text
qt82_source_reference
qt82_component_relation
qt82_work_reference
QT8.2｜共享数据.base
```

后续 Pilot 不重新设计来源／作品关系 schema，只验证是否需要非破坏性扩展。

## 2. Pilot 顺序

### Pilot A｜motif｜已通过

**洪水与灾后重建**

状态：`ACCEPTED_REFERENCE_MOTIF_V0`

已验证：

- `required_invariants / optional_slots`；
- motif 与 plot_pattern / archetype / symbol 的边界；
- `source_status`；
- relation record 原子性；
- `qt82_source_reference`；
- `qt82_work_reference`；
- 共享 Base。

`qt82_component_relation` 已建立 schema，但正式跨类型记录等待相关对象完成自身准入。

### Pilot B｜archetype｜abstract archetype 已通过

第一对象：**受苦义人**（abstract_archetype）

状态：`ACCEPTED_REFERENCE_ARCHETYPE_V0`

来源：

```text
QT8.1.1
→ 约伯／《约伯记》

古代美索不达米亚（QT8.1 待建）
→ Šubši-mēšrê-Šakkan／Ludlul bēl nēmeqi
```

已验证：

```text
abstract_archetype 准入
archetype vs theme
core_functions / variable_features
source_figure / archetype 分层
functional_similarity vs historical_transmission
Shared Data Layer 的 source_status / qt82_source_reference 跨类型复用
Shared Data Layer 的 qt82_work_reference 跨类型复用
component relation target gate
```

正式数据：

```text
2 × qt82_source_reference
3 × qt82_work_reference
```

后世作品：

```text
Joseph Roth, Job
→ direct_adaptation / documented

Archibald MacLeish, J.B.
→ direct_adaptation / documented

Muriel Spark, The Only Problem
→ explicit_reference / documented
```

Acceptance：

```text
QT8.2_PILOT_B_CONTENT_ACCEPTANCE = PASS
QT8.2_PILOT_B_OBJECT_BOUNDARY_ACCEPTANCE = PASS
QT8.2_PILOT_B_CORE_FUNCTION_MODEL = PASS
QT8.2_PILOT_B_SOURCE_GOVERNANCE = PASS
QT8.2_PILOT_B_RELATION_GOVERNANCE = PASS
QT8.2_PILOT_B_WORK_REFERENCE_ACCEPTANCE = PASS
QT8.2_PILOT_B_COMPONENT_RELATION_GATE = PASS_BY_DEFERRED_GATE
```

Acceptance Review：[[QT8.2｜Pilot B 受苦义人 Acceptance Review]]

### Pilot B.1｜named archetype｜下一阶段

**所罗门王**（named_archetype pressure test）

目的不是证明“所罗门很有名”，而是验证：

```text
QT8.1 来源人物
→ 后世特征选择／放大／删减
→ 跨文本、跨时代、跨媒介持续调用
→ named_archetype
```

重点检查：

- `source_figure` 与 `named_archetype` 是否彻底分层；
- 哪些身份特征必须保留才能继续被识别为“所罗门型”；
- 智慧王、裁判者、圣王、魔法王等功能是否应被拆成可复用身份特征，而不是全塞进一个标签；
- named archetype 是否需要专属字段；
- character/name borrowing 与真正 archetypalization 的边界；
- 是否可建立首批正式 `qt82_component_relation`。

只有本压力测试通过，archetype 类型才算同时覆盖 abstract / named 两个子型。

### Pilot C｜plot_pattern

**预言 → 逃避 → 实现**

重点：

- core_slots / optional_slots / repeatable_slots / terminal_variants；
- 命运／预言 motif 与结构顺序分离；
- structural_inheritance 与 structural_similarity 区分。

### Pilot D｜symbol

第一对象：**巴别塔**

重点：

- source object → symbol 的准入；
- 稳定意义与语义漂移；
- symbol_reuse 与普通视觉相似分离。

第二候选：**迷宫**，用于跨媒介压力测试。

## 3. 验证矩阵

| 维度 | 洪水 motif | 受苦义人 abstract archetype | 所罗门王 named archetype | 预言结构 | 巴别塔 symbol |
|---|---:|---:|---:|---:|---:|
| 来源回指 QT8.1 | PASS | PASS | 必须 | 必须 | 必须 |
| 多来源／多接受比较 | PASS | PASS | 强 | 强 | 初期较弱 |
| relation_type / evidence_level | PASS | PASS | 强 | 强 | 中 |
| 文本谱系 | PASS | PASS | 强 | 强 | 强 |
| 对象边界压力 | PASS | PASS | named vs source figure | plot vs motif | symbol vs prop |
| 后世重写 | PASS | PASS | 核心 | 强 | 强 |
| Shared Data Layer | PASS | SOURCE + WORK PASS | 复用 | 复用 | 复用 |
| component relation 跨类型 | schema only | DEFERRED_BY_TARGET_GATE | 候选首轮 | 复用 | 复用 |

## 4. Pilot 输出

每个 Pilot 完成后至少产出：

```text
00 对象主页
对象定义与准入
来源谱系
结构／变体
文本证据
关系记录
后世实例
阅读与研究
共享数据层记录
```

并记录：

```text
KEEP
REVISE
ADD
REMOVE
```

## 5. Freeze Gate

只有当四类对象至少各完成一个 Pilot，并且：

- 四类边界无系统性冲突；
- Shared Data Layer 经跨类型复用验证；
- QT8.1 回指稳定；
- 传播证据治理可执行；
- abstract archetype 与 named archetype 均通过压力测试；
- symbol 准入与语义漂移模型通过；
- plot_pattern slot 模型通过；

才允许：

`QT8.2_TEMPLATE_V1_FREEZE_REVIEW`

当前：

```text
QT8.2_PILOT_A = CLOSED_ACCEPTED
QT8.2_PILOT_B = CLOSED_ACCEPTED
QT8.2_PILOT_B_REFERENCE_STATUS = ACCEPTED_REFERENCE_ARCHETYPE_V0
QT8.2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ONE_ABSTRACT_ARCHETYPE
QT8.2_SHARED_SOURCE_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_SHARED_WORK_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_COMPONENT_RELATION = DEFERRED_BY_TARGET_GATE
QT8.2_NAMED_ARCHETYPE_VALIDATION = NOT_YET
QT8.2_NEXT_STAGE = PILOT_B1_SOLOMON_NAMED_ARCHETYPE
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```
