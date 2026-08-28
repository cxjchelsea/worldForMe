# QC2｜Pilot B 受苦义人 Acceptance Review

> 对象：`受苦义人`
>
> 类型：`archetype / abstract_archetype`
>
> 分支：`feature/qt8-cultural-motif-restructure`
>
> 审查依据：[[QC2｜文化原型型专题模板 V0]]、[[QC2｜世界文化母题、原型与叙事结构模板总则 V0]]、[[QC2｜共享数据层规范 V0]]。

---

# 1. Review Scope

本次只审查 Pilot B 是否已经足以作为第一个 `abstract_archetype` Reference Topic，不扩大“受苦义人”案例池，也不提前启动 named archetype、plot_pattern 或 symbol Pilot。

审查对象包括：

```text
00–10 解释层
20 数据层
qc2_source_reference
qc2_work_reference
component relation target gate
archetype Template V0 的非破坏性适配情况
```

---

# 2. Object Boundary Acceptance

## 2.1 archetype vs theme

PASS。

当前专题稳定区分：

```text
“为什么义人受苦？”
= theme / problem

“承担正直身份 + 不成比例苦难 + 报偿解释危机的角色模型”
= archetype
```

同时已排除：一般受难者、殉道者、替罪者、悲剧英雄、单纯被迫害者等近邻对象的自动并入。

## 2.2 archetype vs plot_pattern

PASS。

`core_functions` 被定义为稳定角色功能，而不是固定事件顺序。朋友辩论、身体疾病、恢复、神圣回应等保留为 `variable_features`，因此没有把《约伯记》的完整剧情误写成 archetype。

## 2.3 source figure vs archetype

PASS。

```text
约伯
= source figure

《约伯记》
= defining text

受苦义人
= abstract archetype
```

约伯是强来源实例，但不反向垄断 archetype 的全部准入条件。

---

# 3. Core / Variable Model Acceptance

PASS。

当前稳定模型：

```text
core_functions
= moral_or_pious_integrity
+ disproportionate_or_unexplained_suffering
+ challenge_to_simple_retribution
+ response_to_divine_or_cosmic_opacity
```

而：

```text
restoration
protest
praise
dialogue_with_advisers
social_loss
bodily_affliction
```

作为 `variable_features`。

`Ludlul bēl nēmeqi` 与《约伯记》的比较证明，archetype 可以保持角色功能稳定，同时允许宗教语境、修辞结构、回应方式与结局方式发生明显变化。

结论：

```text
archetype stability
= stable role-function bundle
≠ fixed plot sequence
```

---

# 4. Source Governance Acceptance

PASS。

当前两条正式来源记录：

```text
约伯／《约伯记》
→ source_status: reference_topic

Šubši-mēšrê-Šakkan／Ludlul bēl nēmeqi
→ source_status: external_source_pending_qt81_topic
```

这证明共享 `source_status` 不仅适用于 motif，也适用于 archetype。

同时：

```text
QC2 已核证美索不达米亚来源实例
≠ QC1.1 已完成美索不达米亚来源传统
```

治理未越界。

---

# 5. Cross-Tradition Relation Acceptance

PASS。

《约伯记》与 `Ludlul bēl nēmeqi` 当前只支持：

```yaml
relation_type: functional_similarity
evidence_level: documented
```

没有因为共享“义人受苦”问题域而自动建立 `historical_transmission`。

如果未来存在传播证据，应另建独立 relation record。

因此继续支持：

```text
functional_similarity
≠ historical_transmission

one relation record
= one relation_type + one evidence_level
```

---

# 6. Later Reworking Acceptance

PASS。

Pilot B 已核证三条正式 `qc2_work_reference`：

```text
Joseph Roth, Job
→ direct_adaptation / documented

Archibald MacLeish, J.B.
→ direct_adaptation / documented

Muriel Spark, The Only Problem
→ explicit_reference / documented
```

三条记录共同证明 archetype 可以通过不同调用强度继续存在：

```text
直接现代化角色重写
直接戏剧改编
显式引用 + 元叙事解释
```

而不要求每个后世实例都一对一复制约伯人物或情节。

Shared Data Layer 的 `qc2_work_reference` 因而完成第一次 archetype 类型复用验证。

---

# 7. Component Relation Gate Review

PASS_BY_DEFERRED_GATE。

当前没有正式 `qc2_component_relation`，但这不是缺失。

已识别：

```text
motif candidates
plot_pattern candidate
symbol candidates
```

对应 target 尚未完成自身 QC2 准入，因此不应由 archetype Pilot 提前制造正式 component。

结论：

```text
candidate relation
≠ formal component relation
```

当前 deferred 状态证明 target gate 正常工作。

---

# 8. Archetype Template V0 Checklist

| 检查项 | 结果 |
|---|---|
| abstract / named 类型已确定 | PASS |
| 来源人物与原型层已分离 | PASS |
| core_functions 已明确 | PASS |
| variable_features 已明确 | PASS |
| archetype 与 theme / trait / plot_pattern 未混淆 | PASS |
| 至少两个来源实例已核证 | PASS |
| 每个来源具有 source_status | PASS |
| 来源已进入 qc2_source_reference | PASS |
| 功能抽象／原型化过程有证据链 | PASS |
| named archetype 非著名即准入 | N/A，本 Pilot 为 abstract archetype |
| motif / plot / symbol 关系已识别 | PASS，保持 candidate gate |
| functional similarity 与 historical transmission 已区分 | PASS |
| relation record 原子性 | PASS |
| 后世实例能显示 core / variable features 变化 | PASS |

结论：

```text
ABSTRACT_ARCHETYPE_CHECKLIST = PASS
NAMED_ARCHETYPE_CHECKLIST = NOT_TESTED_BY_THIS_PILOT
```

---

# 9. Template Feedback

## KEEP

- `abstract_archetype / named_archetype`
- `core_functions / variable_features`
- source figure / archetype 分层
- `source_status`
- `functional_similarity / historical_transmission` 分离
- Shared Data Layer 三类实体
- component target gate
- relation record 原子性

## REVISE

无破坏性修订要求。

## ADD

无新的共享必选字段。

后续 named archetype Pilot 可再判断是否需要 named archetype 专属字段，例如 `source_figure_identity / archetypalization_threshold / reusable_identity_features`；本次不提前加入。

## REMOVE

无。

---

# 10. Final Acceptance

```text
QC2_PILOT_B_CONTENT_ACCEPTANCE = PASS
QC2_PILOT_B_OBJECT_BOUNDARY_ACCEPTANCE = PASS
QC2_PILOT_B_CORE_FUNCTION_MODEL = PASS
QC2_PILOT_B_SOURCE_GOVERNANCE = PASS
QC2_PILOT_B_RELATION_GOVERNANCE = PASS
QC2_PILOT_B_WORK_REFERENCE_ACCEPTANCE = PASS
QC2_PILOT_B_COMPONENT_RELATION_GATE = PASS_BY_DEFERRED_GATE

QC2_PILOT_B_REFERENCE_STATUS = ACCEPTED_REFERENCE_ARCHETYPE_V0
QC2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ONE_ABSTRACT_ARCHETYPE
QC2_SHARED_DATA_LAYER_CROSS_TYPE_SOURCE = PASS
QC2_SHARED_DATA_LAYER_CROSS_TYPE_WORK = PASS

QC2_NAMED_ARCHETYPE_VALIDATION = NOT_YET
QC2_TEMPLATE_V1_FREEZE = NOT_AUTHORIZED
```

---

# 11. Next Stage

Pilot B abstract archetype 已结题。

下一阶段按既定计划进入：

```text
Pilot B.1
→ 所罗门王
→ named_archetype pressure test
```

重点验证：

```text
来源人物
→ 跨文本／跨时代重写
→ 可复用身份特征
→ named archetype
```

只有 named archetype 也通过后，才能说 archetype 类型的两种子型都完成压力测试。
