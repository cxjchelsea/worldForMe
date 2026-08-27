# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_ACCEPTED / PILOT_B1_ACCEPTED / PILOT_C_ACCEPTED / PILOT_D_CONTENT_PASS_B_COMPLETE`

## Pilot A｜motif
**洪水与灾后重建** → `ACCEPTED_REFERENCE_MOTIF_V0`

## Pilot B｜abstract archetype
**受苦义人** → `ACCEPTED_REFERENCE_ARCHETYPE_V0`

## Pilot B.1｜named archetype
**所罗门王** → `ACCEPTED_REFERENCE_NAMED_ARCHETYPE_V0`

## Pilot C｜plot_pattern｜已通过

**预言 → 逃避 → 实现** → `ACCEPTED_REFERENCE_PLOT_PATTERN_V0`

已验证：

```text
core_slots / optional_slots / repeatable_slots / terminal_variants
causal_variants
matched_slots / missing_slots / added_slots
structural_similarity as work relation
```

Plot-pattern template：

```text
QT8.2_PLOT_PATTERN_TEMPLATE_V0
= VALIDATED_BY_ONE_REFERENCE_PLOT_PATTERN
```

## Pilot D｜symbol｜待 Acceptance Review

**巴别塔**

当前状态：`CONTENT_PASS_A_COMPLETE / CONTENT_PASS_B_COMPLETE / ACCEPTANCE_NOT_YET`

### 来源

```text
QT8.1.1 希伯来—圣经叙事传统
→ D｜巴别塔：统一、越界与语言分散
→ 《创世记》11:1–9
→ source_status: reference_topic
```

Pass A 已明确分离：

```text
source object / source episode
≠ source-story function
≠ later cultural symbol
```

### 符号化与跨媒介压力测试

```text
《创世记》11
→ defining source episode

Pieter Bruegel the Elder《The Tower of Babel》(1563)
→ symbol_reuse / documented
→ evidence_medium: visual
→ visual reuse / iconographic stabilization

Jorge Luis Borges《The Library of Babel》(1941)
→ explicit_reference / documented
→ evidence_medium: textual
→ Babel 从 literal tower 漂移到语言、知识总体性与信息秩序

Alejandro González Iñárritu《Babel》(2006)
→ explicit_reference / documented
→ evidence_medium: media
→ literal tower absent
→ communication / incommunicability 成为现代语义重心
```

Pass A + Pass B 当前支持：

```text
admission_evidence
stable_meanings
meaning_shifts
source object vs symbol boundary
explicit_reference vs symbol_reuse
ordinary visual similarity ≠ symbol reuse
symbol continuity ≠ literal object continuity ≠ visual-form continuity
source/work schema 在 symbol 类型上的复用
```

当前工作层 stable meanings：

```text
language confusion and fragmentation
collective human / universalizing ambition
failed or interrupted totalizing project
```

当前 meaning shifts：

```text
knowledge totality / information overload
monumental civilizational project
communication failure
```

“human pride / hubris”保留为重要接受史解释，但不倒灌为《创世记》11 唯一、穷尽性的原始意义。

### 当前数据

```text
1 × qt82_source_reference
3 × qt82_work_reference
0 × qt82_component_relation
```

`qt82_component_relation` 继续执行 meaningful target gate，不为 Pilot 强造 motif / plot-pattern target。

### Pass B schema 决策

symbol work reference 正式允许以下可选字段：

```yaml
symbolic_meaning: []
meaning_shift: []
evidence_medium: textual | visual | material | ritual | media
```

状态：

```text
QT8.2_SYMBOL_WORK_MEANING_FIELDS
= ACTIVE_OPTIONAL_EXTENSION
```

`iconographic_inheritance` 本轮不进入共享 relation vocabulary。当前只有 Bruegel 的视觉定型证据，不足以推出独立、可核证的后世图像继承链。

```text
QT8.2_ICONOGRAPHIC_INHERITANCE_RELATION
= NOT_PROMOTED / REQUIRES_DOCUMENTED_VISUAL_CHAIN
```

### 下一步

进行 `PILOT_D_ACCEPTANCE_REVIEW`，集中检查：

1. symbol 准入边界是否稳定；
2. `admission_evidence / stable_meanings / meaning_shifts` 是否足以支撑正式 symbol component；
3. symbol-specific optional work fields 是否与共享 schema 保持正交；
4. `explicit_reference / symbol_reuse / structural_similarity / historical_transmission` 边界是否清楚；
5. `iconographic_inheritance` 不升级是否符合证据门槛；
6. 数据层、节点页、专题页、模板与总计划状态是否一致。

## Freeze Gate

只有四类 component 至少各有一个通过 Pilot，并完成跨类型冲突检查与 Shared Data Layer 总复核后，才允许：

`QT8.2_TEMPLATE_V1_FREEZE_REVIEW`

当前：

```text
QT8.2_PILOT_A = CLOSED_ACCEPTED
QT8.2_PILOT_B = CLOSED_ACCEPTED
QT8.2_PILOT_B1 = CLOSED_ACCEPTED
QT8.2_PILOT_C = CLOSED_ACCEPTED
QT8.2_PILOT_D_CONTENT_PASS_A = COMPLETE
QT8.2_PILOT_D_CONTENT_PASS_B = COMPLETE
QT8.2_PILOT_D_ACCEPTANCE = NOT_YET

QT8.2_MOTIF_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_MOTIF
QT8.2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
QT8.2_PLOT_PATTERN_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_PLOT_PATTERN
QT8.2_SYMBOL_TEMPLATE_V0 = REVISED_AFTER_BABEL_PASS_B / NOT_YET_ACCEPTED

QT8.2_SYMBOL_BOUNDARY = SUPPORTED
QT8.2_SYMBOL_ADMISSION_MODEL = SUPPORTED
QT8.2_SYMBOL_SOURCE_WORK_SCHEMA_REUSE = PASS
QT8.2_SYMBOL_WORK_MEANING_FIELDS = ACTIVE_OPTIONAL_EXTENSION
QT8.2_ICONOGRAPHIC_INHERITANCE_RELATION = NOT_PROMOTED / REQUIRES_DOCUMENTED_VISUAL_CHAIN

QT8.2_NEXT_STAGE = PILOT_D_ACCEPTANCE_REVIEW
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```
