# QC2｜共享数据层规范 V0

> 状态：`SHARED_DATA_LAYER_V0_CROSS_TYPE_REVIEWED / PASS_WITH_DEFERRED_REAL_COMPONENT_RELATION_EVIDENCE`
>
> 适用范围：QC2 的 motif / archetype / plot_pattern / symbol 四类组件。
>
> 目标：让来源回指、组件关系与后世作品实例使用同一套最小数据模型，而不是散落在说明页里。

---

# 一、设计原则

QC2 的解释层与数据层必须分离：

```text
解释层
→ 定义、边界、来源谱系、结构变体、传播判断、阅读路线

数据层
→ source reference / component relation / work reference
```

固定治理：

```text
一个主要归属地 + 多关系
one relation record = one relation_type + one evidence_level
QC2 已核证来源 ≠ QC1.1 来源专题已完成
结构相似 ≠ 历史继承／传播
```

---

# 二、共享实体 1｜qc2_source_reference

```yaml
type: qc2_source_reference
component_id: WL-TOPIC-...
component_type: motif | archetype | plot_pattern | symbol
source_tradition: WL-TOPIC-... | external:...
source_story: ""
source_text: ""
source_status: reference_topic | reference_topic_source_story_pending_index | external_source_pending_qt81_topic | external_source_verified_text_only | unknown_source_status
tradition_role: source_instance | early_witness | defining_text | defining_reworking | later_defining_reworking
canonical_work: null
sequence: 0
status: active
```

四类型 cross-type review 结论：

```text
QC2_SHARED_SOURCE_SCHEMA_CROSS_TYPE = PASS
QC2_SOURCE_STATUS_MODEL = PASS
QC2_QT81_BACK_REFERENCE_GOVERNANCE = PASS
```

---

# 三、共享实体 2｜qc2_component_relation

```yaml
type: qc2_component_relation
source_component: WL-TOPIC-...
target_component: WL-TOPIC-...
relation_type: carries_motif | contained_by_plot_pattern | organized_by_plot_pattern | represented_by_symbol | associated_with_symbol | overlaps_archetype | contrasts_with_archetype | variant_of_plot_pattern | inverts_plot_pattern | transforms_into_symbol | co_occurs_with_motif | structural_similarity | functional_similarity | historical_transmission
evidence_level: documented | strongly_supported | probable | possible | similarity_only | unknown
source_evidence: []
sequence: 0
status: active
```

原子性规则：

```text
一条记录
= 一个 source_component
+ 一个 target_component
+ 一个 relation_type
+ 一个 evidence_level
```

只有 target 已经成为正式 QC2 component 时才创建正式 `qc2_component_relation`。

当前真实记录仍为：

```text
0 × qc2_component_relation
```

这不触发强制造边。跨类型总复核将其记录为：

```text
QC2_COMPONENT_RELATION_SCHEMA = STRUCTURALLY_ACCEPTED
QC2_REAL_CROSS_TYPE_COMPONENT_RELATION_EVIDENCE = DEFERRED_BY_MEANINGFUL_TARGET_GATE
```

该限制必须在 V1 Freeze Review 中被显式接受或要求补证。

---

# 四、共享实体 3｜qc2_work_reference

```yaml
type: qc2_work_reference
component_id: WL-TOPIC-...
component_type: motif | archetype | plot_pattern | symbol
work: ""
work_role: later_reworking | adaptation | explicit_reuse | inversion | cross_media_reuse
retained_features: []
modified_features: []
relation_type: direct_adaptation | explicit_reference | figure_rewriting | character_or_name_borrowing | structural_inheritance | structural_similarity | motif_inversion | symbol_reuse | plot_pattern_inversion
evidence_level: documented | strongly_supported | probable | possible | similarity_only | unknown
source_evidence: []
canonical_work: null
sequence: 0
status: active
```

## 4.1 figure_rewriting

```text
character_or_name_borrowing
= 主要借人物／名字

figure_rewriting
= 保留人物身份锚点，同时系统性改变其功能／叙事

direct_adaptation
= 明确以某一来源故事／文本为主要整体改编对象
```

## 4.2 structural_similarity

```text
structural_similarity
= 作品稳定实例化某一 plot pattern 的关键顺序／关系，
  但当前没有足够独立证据证明它历史上继承自某一具体来源链
```

与 `structural_inheritance` 严格区分。

## 4.3 plot_pattern 可选字段扩展

```yaml
matched_slots: []
missing_slots: []
added_slots: []
```

## 4.4 symbol 可选字段扩展

```yaml
symbolic_meaning: []
meaning_shift: []
evidence_medium: textual | visual | material | ritual | media
```

字段职责：

```text
symbolic_meaning
= 该实例实际承载的 stable meaning 子集

meaning_shift
= 该实例新增、替换、抽象化或重新加权的意义重心

evidence_medium
= 媒介分类；不替代 relation_type，也不自动证明传播／继承
```

`iconographic_inheritance` 暂不加入共享 work relation vocabulary；只有 documented visual chain 出现后才重新 review。

四类型 cross-type review 结论：

```text
QC2_SHARED_WORK_SCHEMA_CROSS_TYPE = PASS
QC2_WORK_TYPE_OPTIONAL_EXTENSION_MODEL = PASS
QC2_RELATION_ATOMICITY = PASS
```

---

# 五、source_status 共享词汇

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

---

# 六、共享 Base 规范

统一 Base：`QC2｜共享数据.base`。

```text
来源引用 → qc2_source_reference
组件关系 → qc2_component_relation
作品实例 → qc2_work_reference
全部 QC2 数据记录 → 上述三类实体
```

Cross-type review：

```text
QC2_SHARED_BASE_COMPATIBILITY = PASS
QC2_SHARED_BASE_SCHEMA_CHANGE_REQUIRED = NO
```

类型专属 optional fields 不要求所有记录统一拥有；未来可增加辅助视图，但不是冻结阻塞项。

---

# 七、四类对象的专属字段保持独立

```text
motif
→ required_invariants / optional_slots

archetype
→ archetype_kind / core_functions / variable_features
→ named_archetype: required_identity_anchors / supporting_identity_anchors

plot_pattern
→ core_slots / optional_slots / repeatable_slots / terminal_variants / causal_variants
→ work optional: matched_slots / missing_slots / added_slots

symbol
→ admission_evidence / stable_meanings / meaning_shifts
→ work optional: symbolic_meaning / meaning_shift / evidence_medium
```

同名字段（如 motif 与 plot_pattern 的 `optional_slots`）必须保持 `component_type` 语境，不自动合并为跨类型统一语义。

---

# 八、Pilot 应用状态

```text
Pilot A｜洪水 motif = CLOSED_ACCEPTED
Pilot B｜受苦义人 abstract archetype = CLOSED_ACCEPTED
Pilot B.1｜所罗门王 named archetype = CLOSED_ACCEPTED
Pilot C｜预言→逃避→实现 plot_pattern = CLOSED_ACCEPTED
Pilot D｜巴别塔 symbol = CLOSED_ACCEPTED
```

已完成：

```text
QC2_FOUR_TYPE_CROSS_TEMPLATE_CONFLICT_REVIEW = PASS
QC2_SHARED_DATA_FINAL_CROSS_TYPE_REVIEW = PASS_WITH_DEFERRED_REAL_COMPONENT_RELATION_EVIDENCE
```

---

# 九、当前状态

```text
QC2_SHARED_DATA_LAYER = ESTABLISHED_V0 / CROSS_TYPE_REVIEWED
QC2_SOURCE_REFERENCE_SCHEMA = ACTIVE / CROSS_TYPE_PASS
QC2_COMPONENT_RELATION_SCHEMA = ACTIVE_WITH_PROMOTION_GATE / STRUCTURALLY_ACCEPTED
QC2_REAL_CROSS_TYPE_COMPONENT_RELATION_EVIDENCE = DEFERRED_BY_MEANINGFUL_TARGET_GATE
QC2_WORK_REFERENCE_SCHEMA = ACTIVE / CROSS_TYPE_PASS
QC2_FIGURE_REWRITING_RELATION = ACTIVE
QC2_STRUCTURAL_SIMILARITY_WORK_RELATION = ACTIVE
QC2_PLOT_PATTERN_SLOT_FIELDS = ACTIVE_OPTIONAL_EXTENSION
QC2_SYMBOL_WORK_MEANING_FIELDS = ACTIVE_OPTIONAL_EXTENSION
QC2_ICONOGRAPHIC_INHERITANCE_RELATION = NOT_PROMOTED / REQUIRES_DOCUMENTED_VISUAL_CHAIN
QC2_RELATION_ATOMICITY = REQUIRED / PASS
QC2_SHARED_BASE = REQUIRED / COMPATIBILITY_PASS

QC2_TEMPLATE_V1_FREEZE_REVIEW = AUTHORIZED_TO_START
QC2_TEMPLATE_V1_FREEZE = NOT_YET_AUTHORIZED
```

详细总复核：[[QC2｜Four-Type Cross-Template Conflict and Shared Data Review]]
