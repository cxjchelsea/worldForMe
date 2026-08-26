# QT8.2｜共享数据层规范 V0

> 状态：`SHARED_DATA_LAYER_V0_ESTABLISHED_AFTER_PILOT_A_REVIEW`
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

数据层不替代研究论证，只保存已经形成的结构化关系。

固定治理：

```text
一个主要归属地 + 多关系
one relation record = one relation_type + one evidence_level
QT8.2 已核证来源 ≠ QT8.1 来源专题已完成
```

---

# 二、共享实体 1｜qt82_source_reference

职责：记录“某个 QT8.2 组件从哪个 QT8.1 来源传统／故事／文本中抽取出来”。

最小 schema：

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

说明：

- `source_tradition` 优先使用 QT8.1 topic id；若尚未建档，可使用 `external:` 前缀临时标识；
- `source_status` 明确来源层建设状态；
- `canonical_work` 指向唯一作品主节点，尚未建立时允许 `null`；
- source reference 不承担跨组件关系，也不承担后世作品重写关系。

---

# 三、共享实体 2｜qt82_component_relation

职责：记录 QT8.2 组件之间的语义关系。

最小 schema：

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

如果同一对组件同时具有两个不同关系，建立两条记录。

只有 target 已经成为正式 QT8.2 component 时才创建正式 `qt82_component_relation`。候选 archetype / plot_pattern / symbol 不因一个 Pilot 的发现自动升级为正式组件。

---

# 四、共享实体 3｜qt82_work_reference

职责：记录后世作品或跨媒介实例如何调用、改编、继承、反转某个 QT8.2 组件。

最小 schema：

```yaml
type: qt82_work_reference
component_id: WL-TOPIC-...
component_type: motif | archetype | plot_pattern | symbol
work: ""
work_role: later_reworking | adaptation | explicit_reuse | inversion | cross_media_reuse
retained_features: []
modified_features: []
relation_type: direct_adaptation | explicit_reference | character_or_name_borrowing | structural_inheritance | motif_inversion | symbol_reuse | plot_pattern_inversion

evidence_level: documented | strongly_supported | probable | possible | similarity_only | unknown
source_evidence: []
canonical_work: null
sequence: 0
status: active
```

如果同一作品同时构成 `explicit_reference` 与 `motif_inversion`，必须建立两条 work reference，而不是在一个字段内并列。

---

# 五、source_status 共享词汇

```text
reference_topic
= QT8.1 来源专题存在，且对应来源材料已经被纳入

reference_topic_source_story_pending_index
= QT8.1 来源专题存在，但当前具体故事／材料尚未正式索引

external_source_pending_qt81_topic
= 已核证来源材料，但 QT8.1 尚无对应来源专题

external_source_verified_text_only
= 只完成了具体文本核证，尚不足以宣称来源传统结构已建立

unknown_source_status
= 暂无法判断来源层状态
```

---

# 六、共享 Base 规范

统一 Base：`QT8.2｜共享数据.base`。

建议四个视图：

```text
来源引用
→ qt82_source_reference

组件关系
→ qt82_component_relation

作品实例
→ qt82_work_reference

全部 QT8.2 数据记录
→ 上述三类实体
```

各专题如果需要局部查看，优先按 `component_id` 过滤共享数据，而不是重新发明 schema。

---

# 七、四类对象的专属字段保持独立

共享数据层不意味着四类组件使用同一内容字段。

```text
motif
→ required_invariants / optional_slots

archetype
→ archetype_kind / core_functions / variable_features

plot_pattern
→ core_slots / optional_slots / repeatable_slots / terminal_variants

symbol
→ admission_evidence / stable_meanings / meaning_shifts
```

共享的是来源状态、关系原子性、证据等级和作品关系模型。

---

# 八、Pilot A 的应用规则

“洪水与灾后重建” Pilot 首批数据化：

- 《创世记》6–9 → `qt82_source_reference`
- 《阿特拉哈西斯》洪水段 → `qt82_source_reference`
- 《吉尔伽美什史诗》第 XI 泥版 → `qt82_source_reference`
- 奥维德《变形记》第一卷丢卡利翁／皮拉 → `qt82_source_reference`
- Darren Aronofsky《Noah》 → `qt82_work_reference / direct_adaptation`
- Margaret Atwood《The Year of the Flood》 → 分别以 `explicit_reference` 与 `motif_inversion` 建两条 work reference

“洪水幸存者／第二祖先”“失序→毁灭→幸存→重建”“方舟”等当前仍保持 candidate，不建立正式 `qt82_component_relation`。

---

# 九、当前状态

```text
QT8.2_SHARED_DATA_LAYER = ESTABLISHED_V0
QT8.2_SOURCE_REFERENCE_SCHEMA = ACTIVE
QT8.2_COMPONENT_RELATION_SCHEMA = ACTIVE_WITH_PROMOTION_GATE
QT8.2_WORK_REFERENCE_SCHEMA = ACTIVE
QT8.2_RELATION_ATOMICITY = REQUIRED
QT8.2_SHARED_BASE = REQUIRED
```
