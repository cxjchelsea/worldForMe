# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_READY_FOR_ACCEPTANCE`
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

### Pilot B｜archetype｜验收准备完成

第一对象：**受苦义人**（abstract_archetype）

当前状态：`CONTENT_PASS_A_COMPLETE / CONTENT_PASS_B_COMPLETE / READY_FOR_ACCEPTANCE`

来源：

```text
QT8.1.1
→ 约伯／《约伯记》

古代美索不达米亚（QT8.1 待建）
→ Šubši-mēšrê-Šakkan／Ludlul bēl nēmeqi
```

当前已支持：

```text
abstract_archetype 准入
archetype vs theme
core_functions / variable_features
source_figure / archetype 分层
functional_similarity vs historical_transmission
Shared Data Layer 的 source_status / qt82_source_reference 跨类型复用
Shared Data Layer 的 qt82_work_reference 跨类型复用
```

当前已建立：

```text
2 × qt82_source_reference
3 × qt82_work_reference
```

后世作品核证：

```text
Joseph Roth, Job
→ direct_adaptation / documented

Archibald MacLeish, J.B.
→ direct_adaptation / documented

Muriel Spark, The Only Problem
→ explicit_reference / documented
```

当前未建立正式 `qt82_component_relation`。原因不是 schema 失败，而是 target gate 生效：相邻 motif / plot_pattern / symbol 尚未完成自身正式准入，不由本 Pilot 提前升级。

下一步：

1. 做 **Pilot B Acceptance Review**；
2. 判断 `受苦义人` 是否可冻结为 `ACCEPTED_REFERENCE_ARCHETYPE_V0`；
3. 记录 KEEP / REVISE / ADD / REMOVE；
4. 若通过，再启动**所罗门王** `named_archetype` 压力测试。

第二候选：**所罗门王**（named_archetype_candidate）

用于验证命名型原型是否能与 QT8.1 来源人物彻底分层；只在受苦义人 Pilot B 验收后启动。

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

| 维度 | 洪水 motif | 受苦义人 archetype | 预言结构 | 巴别塔 symbol |
|---|---:|---:|---:|---:|
| 来源回指 QT8.1 | PASS | PASS | 必须 | 必须 |
| 多来源比较 | PASS | PASS | 强 | 初期较弱 |
| relation_type / evidence_level | PASS | PASS | 强 | 中 |
| 文本谱系 | PASS | PASS | 强 | 强 |
| 对象边界压力 | PASS | PASS | plot vs motif | symbol vs prop |
| 后世重写 | PASS | PASS | 强 | 强 |
| Shared Data Layer | PASS 首轮 | SOURCE + WORK PASS | 复用 | 复用 |
| component relation 跨类型 | schema only | DEFERRED_BY_TARGET_GATE | 复用 | 复用 |

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
QT8.2_PILOT_B_CONTENT_PASS_A = COMPLETE
QT8.2_PILOT_B_CONTENT_PASS_B = COMPLETE
QT8.2_ARCHETYPE_TEMPLATE_V0 = REVISED_AFTER_PILOT_B_PASS_A
QT8.2_SHARED_SOURCE_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_SHARED_WORK_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_COMPONENT_RELATION = DEFERRED_BY_TARGET_GATE
QT8.2_PILOT_B_ACCEPTANCE = READY_FOR_REVIEW
QT8.2_NEXT_STAGE = PILOT_B_ACCEPTANCE_REVIEW
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```
