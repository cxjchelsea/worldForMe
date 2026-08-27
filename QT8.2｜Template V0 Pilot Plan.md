# QT8.2｜Template V0 Pilot Plan

> 状态：`PILOT_A_ACCEPTED / PILOT_B_ACCEPTED / PILOT_B1_ACCEPTED / PILOT_C_ACCEPTED / PILOT_D_ACCEPTED`

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

## Pilot D｜symbol｜已通过

**巴别塔** → `ACCEPTED_REFERENCE_SYMBOL_V0`

Acceptance Review：[[个人通识知识系统_v2_A2/30 世界文学/30 专题/QT8.2.3 神、人边界与禁忌越界/巴别塔/QT8.2｜Pilot D 巴别塔 Acceptance Review]]

### 来源

```text
QT8.1.1 希伯来—圣经叙事传统
→ D｜巴别塔：统一、越界与语言分散
→ 《创世记》11:1–9
→ source_status: reference_topic
```

已验证：

```text
source object / source episode
≠ source-story function
≠ later cultural symbol

symbol continuity
≠ literal object continuity
≠ visual-form continuity

admission_evidence
stable_meanings / meaning_shifts
explicit_reference / symbol_reuse / historical_transmission 分离
ordinary visual similarity ≠ symbol reuse
```

跨媒介压力测试：

```text
Bruegel《The Tower of Babel》(1563)
→ symbol_reuse / documented / visual

Borges《The Library of Babel》(1941)
→ explicit_reference / documented / textual

Iñárritu《Babel》(2006)
→ explicit_reference / documented / media
```

当前数据：

```text
1 × qt82_source_reference
3 × qt82_work_reference
0 × qt82_component_relation
```

symbol-specific optional work fields 已验证并启用：

```yaml
symbolic_meaning: []
meaning_shift: []
evidence_medium: textual | visual | material | ritual | media
```

`iconographic_inheritance` 不进入当前共享 relation vocabulary；未来只有出现 documented visual chain 才允许重新提交 vocabulary review。

Symbol template：

```text
QT8.2_SYMBOL_TEMPLATE_V0
= VALIDATED_BY_ONE_REFERENCE_SYMBOL
```

## Freeze Gate

四类 component 现在均已有通过验收的 reference Pilot：

```text
motif → ACCEPTED
archetype → ABSTRACT + NAMED ACCEPTED
plot_pattern → ACCEPTED
symbol → ACCEPTED
```

但 V1 Freeze 尚未自动授权。下一阶段必须完成：

```text
four-type cross-template conflict review
+ Shared Data Layer final cross-type review
```

当前：

```text
QT8.2_PILOT_A = CLOSED_ACCEPTED
QT8.2_PILOT_B = CLOSED_ACCEPTED
QT8.2_PILOT_B1 = CLOSED_ACCEPTED
QT8.2_PILOT_C = CLOSED_ACCEPTED
QT8.2_PILOT_D = CLOSED_ACCEPTED

QT8.2_MOTIF_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_MOTIF
QT8.2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
QT8.2_PLOT_PATTERN_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_PLOT_PATTERN
QT8.2_SYMBOL_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_SYMBOL

QT8.2_SYMBOL_BOUNDARY = PASS
QT8.2_SYMBOL_ADMISSION_MODEL = PASS
QT8.2_SYMBOL_SOURCE_WORK_SCHEMA_REUSE = PASS
QT8.2_SYMBOL_WORK_MEANING_FIELDS = ACTIVE_OPTIONAL_EXTENSION
QT8.2_ICONOGRAPHIC_INHERITANCE_RELATION = NOT_PROMOTED / REQUIRES_DOCUMENTED_VISUAL_CHAIN

QT8.2_ALL_FOUR_COMPONENT_TYPES_HAVE_ACCEPTED_REFERENCE_PILOT = YES
QT8.2_TEMPLATE_V1_FREEZE = NOT_YET_AUTHORIZED
QT8.2_NEXT_STAGE = FOUR_TYPE_CROSS_TEMPLATE_CONFLICT_AND_SHARED_DATA_REVIEW
QT8.2_TEMPLATE_STATUS = V0_DRAFT / NOT_FROZEN
```
