# QC2｜共享数据层规范 V1

> 状态：`QC2_SHARED_DATA_LAYER_V1_FROZEN`
>
> 适用范围：motif / archetype / plot_pattern / symbol。
>
> Freeze condition：四类 Pilot accepted；cross-type review PASS；真实 component relation 证据缺口以 governed deferred gap 接受。

## 一、设计原则

```text
解释层 ≠ 数据层
one relation record = one relation_type + one evidence_level
QC2 已核证来源 ≠ QC1.1 来源专题已完成
结构／功能相似 ≠ 历史传播
类型专属字段保持 component_type 语境
```

## 二、qc2_source_reference

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

冻结结论：跨四类复用通过。

## 三、qc2_component_relation

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

只有 source 与 target 均已正式准入、关系具有独立解释价值且证据等级可明确时才创建。

V1 Freeze 时：

```text
REAL_RECORD_COUNT = 0
SCHEMA_STATUS = STRUCTURALLY_ACCEPTED
REAL_EVIDENCE_STATUS = DEFERRED_BY_MEANINGFUL_TARGET_GATE
```

禁止为填 checklist 强制造边。

未来第一条真实跨类型 relation：
- 若可直接使用 V1 vocabulary，按 V1 正常落库；
- 若需要新 relation type 或语义改变，必须先 Governance Amendment。

## 四、qc2_work_reference

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

### archetype 关系细分

```text
character_or_name_borrowing
≠ figure_rewriting
≠ direct_adaptation
```

### plot_pattern optional extension

```yaml
matched_slots: []
missing_slots: []
added_slots: []
```

### symbol optional extension

```yaml
symbolic_meaning: []
meaning_shift: []
evidence_medium: textual | visual | material | ritual | media
```

这些扩展均为 component-type-scoped optional fields。

## 五、source_status

冻结词汇：

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

## 六、relation governance

冻结边界：

```text
relation_type ≠ evidence_level
structural_similarity ≠ structural_inheritance
functional_similarity ≠ historical_transmission
symbol_reuse ≠ historical_transmission
visual similarity ≠ iconographic_inheritance
motif_inversion ≠ plot_pattern_inversion
```

`iconographic_inheritance` 不进入 V1 vocabulary。

## 七、共享 Base

统一聚合入口：`QC2｜共享数据.base`。

```text
来源引用 → qc2_source_reference
组件关系 → qc2_component_relation
作品实例 → qc2_work_reference
```

类型专属 optional fields 不要求所有记录统一拥有；辅助视图可非破坏性增加。

## 八、Freeze 后变更规则

无需升级：新增数据记录、canonical_work 回填、证据等级修订、辅助视图。

需要 amendment / V1.x / V2：
- 新增／删除共享实体；
- relation vocabulary 变化；
- evidence_level 语义变化；
- source_status 核心词汇变化；
- relation atomicity 改变；
- 类型专属字段提升为跨类型共享字段。

```text
QC2_SHARED_DATA_LAYER_V1 = FROZEN
```
