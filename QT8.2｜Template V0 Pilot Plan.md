# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_ACCEPTED / PILOT_B1_ACCEPTED / PILOT_C_CONTENT_PASS_A`
>
> 前置：QT8.1.1 与 QT8.1.2 已作为来源 Reference Topic；QT8.2 四类模板 V0 已建立；motif 与 archetype 已完成 reference Pilot，当前进入 plot_pattern 压力测试。

## 1. 共享数据层

固定复用：

```text
qt82_source_reference
qt82_component_relation
qt82_work_reference
QT8.2｜共享数据.base
```

## 2. Pilot 状态

### Pilot A｜motif｜已通过

**洪水与灾后重建** → `ACCEPTED_REFERENCE_MOTIF_V0`

### Pilot B｜abstract archetype｜已通过

**受苦义人** → `ACCEPTED_REFERENCE_ARCHETYPE_V0`

### Pilot B.1｜named archetype｜已通过

**所罗门王** → `ACCEPTED_REFERENCE_NAMED_ARCHETYPE_V0`

Archetype template：

```text
QT8.2_ARCHETYPE_TEMPLATE_V0
= VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
```

### Pilot C｜plot_pattern｜进行中

**预言 → 逃避 → 实现**

当前状态：`CONTENT_PASS_A_COMPLETE / ACCEPTANCE_NOT_YET`

第一轮来源全部来自已建 QT8.1.2，用于先隔离验证结构抽取：

```text
Cronus / Zeus
→ 《Theogony》
→ full_match

Laius / Oedipus
→ Sophocles《Oedipus Tyrannus》
→ full_match

Acrisius / Perseus
→ Apollodorus《Library》2.4
→ full_match
```

当前最小结构：

```text
S1 authoritative_prediction
→ S2 avoidance_action
→ S3 predicted_outcome_fulfilled
```

已支持：

```text
core_slots
optional_slots
repeatable_slots
terminal_variants
plot_pattern vs motif 边界
source_status / qt82_source_reference 在 plot_pattern 类型上的复用
structural_inheritance / structural_similarity / historical_transmission 分离
```

当前已建立：

```text
3 × qt82_source_reference
0 × qt82_work_reference（Pass B 再建）
0 × qt82_component_relation（meaningful target gate）
```

Pass A 暴露两个非破坏性 schema 信号：

```text
causal_variants
= 用于区分 fulfilled_despite_avoidance / fulfilled_through_avoidance

matched_slots / missing_slots / added_slots
= plot-pattern work reference 的节点级比较字段候选
```

Plot template 已进行 Pass A 非破坏性修订，正式继承 `source_status` 与 Shared Data Layer，但上述两个字段暂不冻结。

下一步 Content Pass B：

1. 加入至少一个不同 QT8.1 来源传统／外部已核证传统，检查该结构是否只是在希腊材料内部成立；
2. 核证 2–3 个后世作品，建立 `qt82_work_reference`；
3. 用真实作品判断 `matched_slots / missing_slots / added_slots` 是否值得成为 plot-pattern work reference 类型扩展；
4. 判断 `causal_variants` 是否应从候选升级为稳定字段；
5. 再做 Pilot C Acceptance Review。

### Pilot D｜symbol｜待开始

**巴别塔**

重点：source object → symbol 准入、稳定意义、语义漂移与 symbol_reuse。

## 3. 验证矩阵

| 维度 | 洪水 motif | 受苦义人 abstract archetype | 所罗门王 named archetype | 预言结构 | 巴别塔 symbol |
|---|---:|---:|---:|---:|---:|
| 来源回指 QT8.1 | PASS | PASS | PASS | PASS_SO_FAR | 必须 |
| 多来源／多接受比较 | PASS | PASS | PASS | SAME_TRADITION_PASS_A / CROSS_TRADITION_PENDING | 初期较弱 |
| relation_type / evidence_level | PASS | PASS | PASS_AFTER_REVISION | PASS_SO_FAR | 中 |
| 文本谱系 | PASS | PASS | PASS | PASS_SO_FAR | 强 |
| 对象边界压力 | PASS | PASS | PASS | PASS_SO_FAR | symbol vs prop |
| 后世重写 | PASS | PASS | PASS | PENDING_PASS_B | 强 |
| Shared Data Layer | PASS | SOURCE + WORK PASS | SOURCE + WORK PASS | SOURCE PASS | 复用 |
| component relation 跨类型 | schema only | DEFERRED_BY_TARGET_GATE | DEFERRED_BY_TARGET_GATE | DEFERRED_BY_MEANINGFUL_TARGET_GATE | 复用 |

## 4. Freeze Gate

只有当四类对象至少各完成一个 Pilot，并且四类边界无系统性冲突、Shared Data Layer 经跨类型复用、QT8.1 回指稳定、传播证据治理可执行、abstract / named archetype 均通过、symbol 与 plot_pattern 模型均通过，才允许：

`QT8.2_TEMPLATE_V1_FREEZE_REVIEW`

当前：

```text
QT8.2_PILOT_A = CLOSED_ACCEPTED
QT8.2_PILOT_B = CLOSED_ACCEPTED
QT8.2_PILOT_B1 = CLOSED_ACCEPTED
QT8.2_PILOT_C_CONTENT_PASS_A = COMPLETE
QT8.2_PLOT_PATTERN_BOUNDARY = SUPPORTED_SO_FAR
QT8.2_PLOT_PATTERN_SLOT_MODEL = PASS_SO_FAR
QT8.2_PLOT_PATTERN_SOURCE_SCHEMA_REUSE = PASS_SO_FAR
QT8.2_PLOT_PATTERN_CAUSAL_VARIANT_FIELD = CANDIDATE
QT8.2_PLOT_PATTERN_SLOT_LEVEL_WORK_FIELDS = CANDIDATE
QT8.2_PILOT_C_ACCEPTANCE = NOT_YET
QT8.2_NEXT_STAGE = PILOT_C_CONTENT_PASS_B
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```