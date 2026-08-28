# QC2.1｜世界父母分离结构 Component Acceptance Review

> Component：`WL-TOPIC-QC21-WORLD-PARENTS-SEPARATION`
>
> component_type：`plot_pattern`
>
> Baseline：`QC2_PLOT_PATTERN_TEMPLATE_V1_FROZEN`

---

## 1. Acceptance summary

本组件通过 QC2 V1 冻结后的正式 component acceptance。

```text
QC2.1_P1_COMPONENT_ACCEPTANCE = PASS
QC2.1_P1_COMPONENT_TYPE = plot_pattern
QC2.1_P1_STATUS = ACTIVE_V1_COMPONENT
QC2_TEMPLATE_REOPEN_REQUIRED = NO
```

## 2. Plot-pattern object check

核心序列明确：

```text
S1 world_parents_joined
→ S2 offspring_constrained
→ S3 separation_action
→ S4 cosmic_space_opened
```

该对象具有稳定的关系 + 顺序，不是 motif 列表。

```text
RELATION_PLUS_SEQUENCE = PASS
CORE_SLOT_MODEL = PASS
```

## 3. 与 M2「天地分离」边界

```text
M2 天地分离
= motif
= 未分／贴合 → 分离 → 世界空间形成

P1 世界父母分离结构
= plot_pattern
= world parents + offspring constraint + ordered separation sequence
```

盘古式实例可满足 M2 而不满足 P1，因此 P1 不等于 M2 的重命名。

```text
MOTIF_VS_PLOT_PATTERN_BOUNDARY = PASS
```

## 4. Source pressure test

当前：

```text
Māori Rangi / Papa = FULL_MATCH
Egyptian Nut / Geb / Shu = FULL_OR_NEAR_FULL_MATCH
Greek Gaia / Ouranos / Kronos = STRONG_VARIANT
```

跨传统差异通过 causal / terminal variants 表达，没有为了统一而抹平来源差异。

```text
CROSS_TRADITION_SOURCE_PRESSURE = PASS
SOURCE_STATUS_GOVERNANCE = PASS
```

## 5. Slot taxonomy

已区分：

```text
core_slots
optional_slots
repeatable_slots
terminal_variants
causal_variants
```

`repeatable_slots` 当前为空是合法状态，不为模板完整度强造重复节点。

```text
SLOT_TAXONOMY = PASS
```

## 6. Transmission governance

```text
high slot match ≠ structural_inheritance
structural_similarity ≠ historical_transmission
```

当前未创建跨传统传播关系。

```text
TRANSMISSION_GOVERNANCE = PASS
```

## 7. Shared Data Layer

Acceptance 时数据：

```text
3 × qc2_source_reference
0 × qc2_component_relation
0 × qc2_work_reference
```

source schema 复用正常；work reference 暂缺不构成阻塞。

## 8. First real component relation gate

P1 与已经正式 accepted 的 M2 存在自然且具有解释价值的关系：

```text
P1 世界父母分离结构
→ carries_motif
→ M2 天地分离
```

检查：

```text
source_component formally accepted = YES
target_component formally accepted = YES
relation has independent explanatory value = YES
existing V1 vocabulary sufficient = YES
new relation type required = NO
```

建议：

```text
relation_type = carries_motif
evidence_level = strongly_supported
```

`strongly_supported` 而非 `documented`，因为该 relation 是由两个 component 的冻结定义与多来源实例共同支持的结构判断，而不是某一外部文献直接命名的本体关系。

```text
QC2_FIRST_REAL_COMPONENT_RELATION_GATE = PASS
QC2_SHARED_DATA_V1_AMENDMENT_REQUIRED = NO
```

## 9. Final decision

```text
QC2.1_P1_COMPONENT_ACCEPTANCE = PASS
QC2.1_P1_STATUS = ACTIVE_V1_COMPONENT
QC2.1_ACTIVE_COMPONENT_COUNT_AFTER_P1 = 2

QC2_FIRST_REAL_CROSS_TYPE_COMPONENT_RELATION = AUTHORIZED_TO_CREATE
QC2_TEMPLATE_V1_REOPEN = NO
```

下一步：创建 P1 → M2 `carries_motif` 原子关系记录，并同步专题主页、数据索引与 QC2.1 问题域状态。