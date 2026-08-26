# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_ACCEPTED / PILOT_B1_CONTENT_PASS_A`
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

已验证：`required_invariants / optional_slots`、来源治理、relation 原子性、source / work reference 与共享 Base。

### Pilot B｜archetype｜abstract archetype 已通过

**受苦义人**（abstract_archetype）

状态：`ACCEPTED_REFERENCE_ARCHETYPE_V0`

已验证：

```text
abstract_archetype 准入
archetype vs theme
core_functions / variable_features
source_figure / archetype 分层
functional_similarity vs historical_transmission
source / work reference 跨类型复用
component relation target gate
```

Acceptance Review：[[QT8.2｜Pilot B 受苦义人 Acceptance Review]]

### Pilot B.1｜named archetype｜进行中

**所罗门王**（named_archetype pressure test）

当前状态：`CONTENT_PASS_A_COMPLETE / ACCEPTANCE_NOT_YET`

来源：

```text
QT8.1.1
→ 王权建立：扫罗—大卫—所罗门
→ 《列王纪》中的所罗门
```

Pass A 已建立：

```text
source figure Solomon
→ 智慧王／审判者／圣殿建造者
→ 智慧与知识权威
→ 晚期古代驱魔／魔法王接受
→ Quranic Sulayman
→ Solomonic magic 权威名字
```

当前初步支持：

```text
named_archetype 与 source figure 可分层
identity_anchor 是 named archetype 的专属字段候选
core_functions / variable_features 可继续复用
同一名字长期连续 ≠ 各传统叙事完全相同
```

当前数据：

```text
1 × qt82_source_reference
4 × qt82_work_reference
```

工作实例：

```text
Josephus, Antiquities 8.42–49
→ explicit_reference / documented

Testament of Solomon
→ character_or_name_borrowing / documented

Quranic Sulayman traditions
→ character_or_name_borrowing / documented

Key of Solomon / Clavicula Salomonis tradition
→ character_or_name_borrowing / documented
```

Pass A 暴露一个 relation schema 信号：

```text
figure_rewriting
```

named archetype 常出现“同一命名人物被系统重写”的关系，比 `character_or_name_borrowing` 更强，又不等于整部作品 `direct_adaptation`。当前仅记录为候选，不立即修改共享枚举。

下一步 Pass B：

1. 检查 `identity_anchor` 在 Jewish / Christian / Islamic / esoteric reception 中是否稳定；
2. 判断 `wise_king_and_judge / sacral_royal_authority / knowledge_authority` 哪些真正属于 core functions；
3. 检查 `builder_and_centralizer` 是否过度依赖来源层，应降为 variable feature；
4. 用真实记录判断 `figure_rewriting` 是否应加入 Shared Data Layer；
5. 做 named archetype Acceptance Review。

只有本压力测试通过，archetype 类型才算同时覆盖 abstract / named 两个子型。

### Pilot C｜plot_pattern

**预言 → 逃避 → 实现**

重点：core_slots / optional_slots / repeatable_slots / terminal_variants，以及 plot vs motif 边界。

### Pilot D｜symbol

第一对象：**巴别塔**。

重点：source object → symbol 准入、稳定意义与语义漂移、symbol_reuse 与普通视觉相似分离。

## 3. 验证矩阵

| 维度 | 洪水 motif | 受苦义人 abstract archetype | 所罗门王 named archetype | 预言结构 | 巴别塔 symbol |
|---|---:|---:|---:|---:|---:|
| 来源回指 QT8.1 | PASS | PASS | PASS_SO_FAR | 必须 | 必须 |
| 多来源／多接受比较 | PASS | PASS | PASS_SO_FAR | 强 | 初期较弱 |
| relation_type / evidence_level | PASS | PASS | SCHEMA_SIGNAL | 强 | 中 |
| 文本谱系 | PASS | PASS | PASS_SO_FAR | 强 | 强 |
| 对象边界压力 | PASS | PASS | PASS_SO_FAR | plot vs motif | symbol vs prop |
| 后世重写 | PASS | PASS | PASS_A | 强 | 强 |
| Shared Data Layer | PASS | SOURCE + WORK PASS | SOURCE + WORK PASS_SO_FAR | 复用 | 复用 |
| component relation 跨类型 | schema only | DEFERRED_BY_TARGET_GATE | DEFERRED_BY_TARGET_GATE | 复用 | 复用 |

## 4. Pilot 输出

每个 Pilot 完成后至少产出：对象主页、定义与准入、来源谱系、结构／变体、文本证据、关系记录、后世实例、阅读与研究、共享数据层记录，并记录 KEEP / REVISE / ADD / REMOVE。

## 5. Freeze Gate

只有当四类对象至少各完成一个 Pilot，并且四类边界无系统性冲突、Shared Data Layer 经跨类型复用、QT8.1 回指稳定、传播证据治理可执行、abstract / named archetype 均通过、symbol 与 plot_pattern 模型均通过，才允许：

`QT8.2_TEMPLATE_V1_FREEZE_REVIEW`

当前：

```text
QT8.2_PILOT_A = CLOSED_ACCEPTED
QT8.2_PILOT_B = CLOSED_ACCEPTED
QT8.2_PILOT_B1 = CONTENT_PASS_A_COMPLETE
QT8.2_ABSTRACT_ARCHETYPE_VALIDATION = PASS
QT8.2_NAMED_ARCHETYPE_VALIDATION = PASS_SO_FAR
QT8.2_IDENTITY_ANCHOR_MODEL = CANDIDATE_SUPPORTED
QT8.2_FIGURE_REWRITING_RELATION = CANDIDATE
QT8.2_SHARED_SOURCE_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_SHARED_WORK_SCHEMA_CROSS_TYPE_VALIDATION = PASS
QT8.2_COMPONENT_RELATION = DEFERRED_BY_TARGET_GATE
QT8.2_NEXT_STAGE = PILOT_B1_CONTENT_PASS_B
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```
