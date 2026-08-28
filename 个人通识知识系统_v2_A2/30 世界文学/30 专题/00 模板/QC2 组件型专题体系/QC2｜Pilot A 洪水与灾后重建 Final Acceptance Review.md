# QC2｜Pilot A 洪水与灾后重建 Final Acceptance Review

> 对象：`WL-TOPIC-QC22-FLOOD`
>
> 前置：Content Pass B + Structure Review + Shared Data Layer Pass

---

# 1. 最终结论

```text
QC2_PILOT_A_CONTENT_ACCEPTANCE = PASS
QC2_PILOT_A_OBJECT_BOUNDARY_ACCEPTANCE = PASS
QC2_PILOT_A_SOURCE_GOVERNANCE = PASS
QC2_PILOT_A_RELATION_GOVERNANCE = PASS
QC2_PILOT_A_SOURCE_REFERENCE_DATA = PASS
QC2_PILOT_A_WORK_REFERENCE_DATA = PASS
QC2_PILOT_A_SHARED_BASE = PASS
QC2_PILOT_A_COMPONENT_RELATION_SCHEMA = READY_BUT_CROSS_TYPE_VALIDATION_PENDING
QC2_PILOT_A_FINAL_ACCEPTANCE = PASS
QC2_PILOT_A_REFERENCE_STATUS = ACCEPTED_REFERENCE_MOTIF_V0
```

Pilot A 可以结束。它已经完成 motif 模板本身、来源回指、后世作品关系和共享数据层的首轮验证。

`qc2_component_relation` 尚未创建真实跨类型记录，不视为 Pilot A 缺口，因为当前相关 archetype / plot_pattern / symbol 仍处于 candidate 状态；正式跨类型关系应由后续对应 Pilot 完成准入后再验证。

---

# 2. Motif 准入模型

最终保留：

```text
required_invariants
+
optional_slots
```

洪水 motif 的最低条件：

```text
R1 大规模洪水破坏旧秩序
R2 一部分生命／共同体资源被选择性保存
R3 洪水之后进入新的秩序阶段
```

压力测试实例：

- 《创世记》6–9；
- 《阿特拉哈西斯》洪水段；
- 《吉尔伽美什史诗》第 XI 泥版；
- 奥维德《变形记》第一卷丢卡利翁／皮拉。

丢卡利翁／皮拉案例证明“方舟／船、预警、盟约”不能成为 motif 必选条件。

---

# 3. 来源数据层验收

已经建立 4 条 `qc2_source_reference`：

```text
Genesis 6–9
→ reference_topic

Atrahasis
→ external_source_pending_qt81_topic

Gilgamesh XI
→ external_source_pending_qt81_topic

Ovid / Deucalion and Pyrrha
→ reference_topic_source_story_pending_index
```

结果：`source_status` 已证明可以处理三种不同来源建设状态。

---

# 4. 后世作品数据层验收

已经建立 3 条 `qc2_work_reference`：

```text
Noah (2014)
→ direct_adaptation / documented

The Year of the Flood
→ explicit_reference / documented

The Year of the Flood
→ motif_inversion / documented
```

同一作品的两个不同关系被拆成两条记录，因此：

```text
one relation record
=
one relation_type
+
one evidence_level
```

已经通过真实数据验证。

---

# 5. 共享 Base 验收

已建立：

`QC2｜共享数据.base`

提供：

```text
来源引用
组件关系
作品实例
全部 QC2 数据记录
```

后续 archetype / plot_pattern / symbol Pilot 不应重新设计一套独立数据实体，而应继续复用：

```text
qc2_source_reference
qc2_component_relation
qc2_work_reference
```

---

# 6. 为什么组件关系暂时为空

Pilot A 已识别：

```text
洪水幸存者／第二祖先
→ archetype_candidate

失序→毁灭→幸存→重建
→ plot_pattern_candidate

方舟
→ symbol_candidate
```

但没有创建正式 `qc2_component_relation`。

这是治理上的有意行为，不是遗漏：

```text
candidate discovered by motif Pilot
≠ formally admitted QC2 component
```

下一轮 archetype Pilot 若完成“受苦义人”的正式 component 准入，即可开始验证跨类型 relation entity。

---

# 7. 对 Template V0 的已确认修订

## KEEP

- 一级母题簇只做导航／问题域容器；
- motif 与 plot_pattern 分离；
- QC2 必须回指 QC1.1；
- relation_type 与 evidence_level 分离；
- 文本见证年代与故事起源年代分离。

## ADD

共享治理已增加：

```text
source_status
shared data layer
qc2_source_reference
qc2_component_relation
qc2_work_reference
shared Base
relation record atomicity
```

motif 专属增加：

```text
required_invariants
optional_slots
```

## DEFER

- archetype 的正式 relation target；
- plot_pattern 的正式 relation target；
- symbol 的正式 relation target；
- 四类 Pilot 完成后的 Template V1 Freeze。

---

# 8. 下一阶段授权边界

Pilot A 完成后，可以进入：

```text
Pilot B｜archetype
第一对象：受苦义人
```

Pilot B 必须直接复用 Shared Data Layer V0，不再重新设计来源／作品关系 schema。

Pilot B 重点新增验证：

```text
abstract_archetype 准入
archetype vs theme
core_functions / variable_features
跨来源 functional_similarity
首次正式 qc2_component_relation 跨类型记录
```

---

# 9. 状态

```text
QC2_PILOT_A = CLOSED_ACCEPTED
QC2_MOTIF_TEMPLATE_V0 = VALIDATED_BY_ONE_REFERENCE_MOTIF
QC2_SHARED_DATA_LAYER_V0 = ESTABLISHED
QC2_SHARED_DATA_LAYER_CROSS_TYPE_VALIDATION = PENDING_PILOT_B_PLUS
QC2_TEMPLATE_V1_FREEZE = NOT_AUTHORIZED
QC2_NEXT_STAGE = PILOT_B_SUFFERING_RIGHTEOUS_ARCHETYPE
```
