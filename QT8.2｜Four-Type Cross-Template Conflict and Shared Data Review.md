# QT8.2｜Four-Type Cross-Template Conflict and Shared Data Review

> Review scope：motif / archetype / plot_pattern / symbol + Shared Data Layer V0
>
> Review basis：四类已验收 reference Pilot + 四套 V0 类型模板 + Template V0 总则 + Shared Data Layer V0 + 共享数据 Base

---

## 1. Review summary

本轮跨类型总复核通过。

```text
QT8.2_FOUR_TYPE_CROSS_TEMPLATE_CONFLICT_REVIEW = PASS
QT8.2_SHARED_DATA_FINAL_CROSS_TYPE_REVIEW = PASS_WITH_DEFERRED_REAL_COMPONENT_RELATION_EVIDENCE
QT8.2_TYPE_BOUNDARY_CONFLICT = NONE_BLOCKING
QT8.2_TYPE_SPECIFIC_FIELD_LEAKAGE = NONE_BLOCKING
QT8.2_SHARED_SOURCE_SCHEMA = PASS
QT8.2_SHARED_WORK_SCHEMA = PASS
QT8.2_COMPONENT_RELATION_SCHEMA = PASS_BY_GOVERNED_DEFERRED_EVIDENCE
QT8.2_RELATION_ATOMICITY = PASS
QT8.2_SOURCE_STATUS_GOVERNANCE = PASS
QT8.2_SHARED_BASE_COMPATIBILITY = PASS

QT8.2_TEMPLATE_V1_FREEZE_REVIEW = AUTHORIZED_TO_START
QT8.2_TEMPLATE_V1_FREEZE = NOT_YET_AUTHORIZED
```

## 2. 四类对象边界

```text
motif
→ required_invariants / optional_slots
→ 回答“故事反复发生什么基本叙事单元或关系”

archetype
→ core_functions / variable_features
→ named archetype 另有 identity anchors
→ 回答“谁成为可反复调用的文化角色模型”

plot_pattern
→ core_slots / optional_slots / repeatable_slots / terminal_variants / causal_variants
→ 回答“故事怎样以稳定顺序与关系展开”

symbol
→ admission_evidence / stable_meanings / meaning_shifts
→ 回答“什么对象、空间或意象获得跨文本、时代、媒介可识别的文化意义”
```

关键边界均已由 Pilot 支持：

```text
motif required_invariants ≠ ordered plot slots
archetype core_functions ≠ personality traits ≠ ordered plot slots
plot_pattern = relation + sequence，≠ motif list
source object / source-story function ≠ later symbol
```

结论：

```text
QT8.2_MOTIF_VS_PLOT_PATTERN_BOUNDARY = PASS
QT8.2_ARCHETYPE_VS_TRAIT_THEME_BOUNDARY = PASS
QT8.2_ARCHETYPE_VS_PLOT_PATTERN_BOUNDARY = PASS
QT8.2_SYMBOL_VS_SOURCE_OBJECT_BOUNDARY = PASS
QT8.2_CROSS_TYPE_OBJECT_MODEL = PASS
```

## 3. 类型专属字段冲突检查

四类专属字段继续按 `component_type` 隔离：

```text
motif
→ required_invariants / optional_slots

archetype
→ archetype_kind / core_functions / variable_features
→ required_identity_anchors / supporting_identity_anchors（named only）

plot_pattern
→ core_slots / optional_slots / repeatable_slots / terminal_variants / causal_variants
→ work optional: matched_slots / missing_slots / added_slots

symbol
→ admission_evidence / stable_meanings / meaning_shifts
→ work optional: symbolic_meaning / meaning_shift / evidence_medium
```

`motif.optional_slots` 与 `plot_pattern.optional_slots` 虽同名，但语义由类型模板限定，不合并为一个跨类型统一本体字段。

```text
QT8.2_TYPE_SPECIFIC_FIELD_ISOLATION = PASS
QT8.2_CROSS_TYPE_FIELD_COLLISION = NO_BLOCKING_COLLISION
QT8.2_SHARED_DATA_BREAKING_CHANGE_REQUIRED = NO
```

## 4. Shared source schema

四类对象统一复用 `qt82_source_reference`。`source_status` 可处理已建 QT8.1、待建来源专题、外部已核证文本与未知来源状态。

```text
QT8.2_SHARED_SOURCE_SCHEMA_CROSS_TYPE = PASS
QT8.2_SOURCE_STATUS_MODEL = PASS
QT8.2_QT81_BACK_REFERENCE_GOVERNANCE = PASS
```

## 5. Shared work schema

四类对象统一复用 `qt82_work_reference`。plot_pattern 与 symbol 的类型专属字段均保持 optional extension；archetype 已验证 `figure_rewriting`，plot_pattern 已验证 `structural_similarity`，symbol 已验证 visual / textual / media 三种媒介记录。

```text
QT8.2_SHARED_WORK_SCHEMA_CROSS_TYPE = PASS
QT8.2_WORK_TYPE_OPTIONAL_EXTENSION_MODEL = PASS
QT8.2_RELATION_ATOMICITY = PASS
```

## 6. relation vocabulary

当前治理已稳定区分：

```text
relation_type ≠ evidence_level
structural_similarity ≠ structural_inheritance
functional_similarity ≠ historical_transmission
symbol_reuse ≠ historical_transmission
visual similarity ≠ iconographic_inheritance
character_or_name_borrowing ≠ figure_rewriting ≠ direct_adaptation
motif_inversion ≠ plot_pattern_inversion
```

`iconographic_inheritance` 不因单一视觉相似证据进入共享 vocabulary。

```text
QT8.2_RELATION_VOCABULARY_CONFLICT = NONE_BLOCKING
QT8.2_RELATION_EVIDENCE_SEPARATION = PASS
QT8.2_ICONOGRAPHIC_INHERITANCE_NON_PROMOTION = PASS
```

## 7. qt82_component_relation 剩余证据缺口

当前真实数据仍为：

```text
0 × qt82_component_relation
```

schema 与 promotion gate 已经在多个 Pilot 中被检查，但尚未出现一条两个已正式准入组件之间、同时具有独立解释价值的自然跨类型边。

本轮不为了 checklist 强行把洪水、受苦义人、预言→逃避→实现、巴别塔四个 reference Pilot 互相连边。

因此：

```text
QT8.2_COMPONENT_RELATION_SCHEMA = STRUCTURALLY_ACCEPTED
QT8.2_REAL_CROSS_TYPE_COMPONENT_RELATION_EVIDENCE = DEFERRED_BY_MEANINGFUL_TARGET_GATE
QT8.2_COMPONENT_RELATION_GAP = NON_BLOCKING_FOR_FREEZE_REVIEW_START
```

V1 Freeze Review 必须显式决定是否接受这一剩余限制。

## 8. Shared Base 兼容性

`QT8.2｜共享数据.base` 只按三种共享实体聚合，不要求所有记录具有同一组类型专属字段，因此类型专属 optional fields 不造成 Base 冲突。

```text
QT8.2_SHARED_BASE_COMPATIBILITY = PASS
QT8.2_SHARED_BASE_SCHEMA_CHANGE_REQUIRED = NO
```

可在未来增加类型专属辅助视图，但不是冻结阻塞项。

## 9. 四套模板状态

```text
QT8.2_MOTIF_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_MOTIF
QT8.2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
QT8.2_PLOT_PATTERN_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_PLOT_PATTERN
QT8.2_SYMBOL_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_SYMBOL
QT8.2_NEW_CONTENT_PILOT_REQUIRED_BEFORE_FREEZE_REVIEW = NO
```

## 10. 总则反馈

### KEEP

```text
四类 component 分型
一级母题簇作为导航／问题域，而非本体唯一归属
source_status
三实体 Shared Data Layer
relation atomicity
meaningful target promotion gate
结构／功能相似与历史传播分离
类型专属 optional extension
```

### REVISE

Template V0 总则中的 Pilot 进度与验收 checklist 已落后，应同步为四类 Pilot 全部 accepted，并把“真实 component relation 尚无记录”改写为显式 deferred evidence gap，由 Freeze Review 决定是否接受。

### ADD

```text
cross-type field semantics must remain component_type-scoped
real component relation evidence may be deferred only by meaningful target gate
Freeze Review must explicitly acknowledge deferred evidence gaps
```

## 11. Freeze gate impact

```text
QT8.2_FOUR_TYPE_CROSS_TEMPLATE_CONFLICT_REVIEW = PASS
QT8.2_SHARED_DATA_FINAL_CROSS_TYPE_REVIEW = PASS_WITH_DEFERRED_REAL_COMPONENT_RELATION_EVIDENCE
QT8.2_ALL_FREEZE_REVIEW_PREREQUISITES = SATISFIED_WITH_DOCUMENTED_DEFERRED_GAP

QT8.2_TEMPLATE_V1_FREEZE_REVIEW = AUTHORIZED_TO_START
QT8.2_TEMPLATE_V1_FREEZE = NOT_YET_AUTHORIZED
QT8.2_NEXT_STAGE = QT8.2_TEMPLATE_V1_FREEZE_REVIEW
```

Freeze Review 应集中决定：四类边界、Shared Data Layer 冻结范围、类型专属字段、relation vocabulary 命名、是否接受 component relation 的 deferred evidence gap，以及未来 amendment / reopen 条件。
