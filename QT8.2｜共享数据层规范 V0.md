# QT8.2｜共享数据层规范 V0

> 状态：`SHARED_DATA_LAYER_V0_REVISED_AFTER_PLOT_PATTERN_PASS_B`
>
> 适用范围：QT8.2 的 motif / archetype / plot_pattern / symbol 四类组件。
>
> 目标：让来源回指、组件关系与后世作品实例使用同一套最小数据模型，而不是散落在说明页里。

---

# 一、设计原则

QT8.2 的解释层与数据层必须分离：

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
QT8.2 已核证来源 ≠ QT8.1 来源专题已完成
结构相似 ≠ 历史继承／传播
```

---

# 二、共享实体 1｜qt82_source_reference

职责：记录某个 QT8.2 组件从哪个 QT8.1 来源传统／故事／文本中抽取出来。

```yaml
type: qt82_source_reference
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

---

# 三、共享实体 2｜qt82_component_relation

职责：记录 QT8.2 组件之间的语义关系。

```yaml
type: qt82_component_relation
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

只有 target 已经成为正式 QT8.2 component 时才创建正式 `qt82_component_relation`。

---

# 四、共享实体 3｜qt82_work_reference

职责：记录后世作品或跨媒介实例如何调用、改编、继承、相似、反转某个 QT8.2 组件。

```yaml
type: qt82_work_reference
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

## 4.2 structural_similarity｜Pilot C 新增

```text
structural_similarity
= 作品稳定实例化某一 plot pattern 的关键顺序／关系，
  但当前没有足够独立证据证明它历史上继承自某一具体来源链
```

与：

```text
structural_inheritance
```

严格区分。后者要求额外的作者、文本、改编或传播证据；不能仅凭 slot 高匹配度升级。

## 4.3 plot_pattern 可选字段扩展

当 `component_type: plot_pattern` 时，允许增加：

```yaml
matched_slots: []
missing_slots: []
added_slots: []
```

这些字段用于节点级结构比较，不强迫 motif / archetype / symbol 使用。

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

统一 Base：`QT8.2｜共享数据.base`。

```text
来源引用 → qt82_source_reference
组件关系 → qt82_component_relation
作品实例 → qt82_work_reference
全部 QT8.2 数据记录 → 上述三类实体
```

---

# 七、四类对象的专属字段保持独立

```text
motif
→ required_invariants / optional_slots

archetype
→ archetype_kind / core_functions / variable_features
→ named_archetype 额外使用 required_identity_anchors / supporting_identity_anchors

plot_pattern
→ core_slots / optional_slots / repeatable_slots / terminal_variants / causal_variants
→ work reference 可选 matched_slots / missing_slots / added_slots

symbol
→ admission_evidence / stable_meanings / meaning_shifts
```

---

# 八、Pilot 应用状态

Pilot A｜洪水 motif：验证 source/work schema 与 relation atomicity。

Pilot B｜受苦义人 abstract archetype：验证 source/work schema 跨类型复用。

Pilot B.1｜所罗门王 named archetype：新增并验证 `required_identity_anchors / supporting_identity_anchors` 与 `figure_rewriting`。

Pilot C｜预言→逃避→实现 plot_pattern：新增并验证：

```text
causal_variants
matched_slots / missing_slots / added_slots
structural_similarity as work relation
```

并再次固定：

```text
structural_similarity
≠ structural_inheritance
```

`qt82_component_relation` 仍遵守 promotion gate。

---

# 九、当前状态

```text
QT8.2_SHARED_DATA_LAYER = ESTABLISHED_V0
QT8.2_SOURCE_REFERENCE_SCHEMA = ACTIVE
QT8.2_COMPONENT_RELATION_SCHEMA = ACTIVE_WITH_PROMOTION_GATE
QT8.2_WORK_REFERENCE_SCHEMA = ACTIVE
QT8.2_FIGURE_REWRITING_RELATION = ACTIVE
QT8.2_STRUCTURAL_SIMILARITY_WORK_RELATION = ACTIVE_AFTER_PILOT_C_PASS_B
QT8.2_PLOT_PATTERN_SLOT_FIELDS = ACTIVE_OPTIONAL_EXTENSION
QT8.2_RELATION_ATOMICITY = REQUIRED
QT8.2_SHARED_BASE = REQUIRED
```