# QC2｜Pilot A 洪水与灾后重建 Structure / Acceptance Review

> 审查对象：`QC2.2 毁灭、灾变与世界重生 / 洪水与灾后重建`
>
> 审查阶段：Content Pass B 后结构审查
>
> 目标：判断 motif Pilot 是否达到 Acceptance、Template V0 回写是否与其他对象模板冲突，以及是否应在进入 archetype / plot_pattern / symbol Pilot 前建立共享数据层。

---

# 1. 总结结论

```text
QC2_PILOT_A_CONTENT_ACCEPTANCE = PASS
QC2_PILOT_A_OBJECT_BOUNDARY_ACCEPTANCE = PASS
QC2_PILOT_A_SOURCE_GOVERNANCE = PASS
QC2_PILOT_A_RELATION_GOVERNANCE = PASS
QC2_PILOT_A_DATA_LAYER_ACCEPTANCE = NOT_YET
QC2_PILOT_A_FINAL_ACCEPTANCE = PASS_WITH_DATA_LAYER_GATE_OPEN

QC2_TEMPLATE_V0_MOTIF_REVISION = SUPPORTED
QC2_TEMPLATE_V0_SHARED_SCHEMA_REQUIRED_BEFORE_PILOT_B = YES
QC2_PILOT_A_COMPONENT_SPLIT_NOW = NO
```

Pilot A 已经证明 motif 模板在内容层可执行，但还没有证明四类对象能够共享稳定的数据实体与 Base。因此现在不应直接把 Pilot A 标记为最终 `ACCEPTED_REFERENCE_COMPONENT`。

---

# 2. Motif 模板完成判定

| 条件 | 结果 | 说明 |
|---|---|---|
| 最小 motif 定义 | PASS | 已用 R1–R3 表达最低准入 |
| `required_invariants` | PASS | R1 大规模水灾破坏旧秩序；R2 选择性保存；R3 灾后进入新阶段 |
| `optional_slots` | PASS | 预警、保存媒介、祭祀、盟约、再生方式等已降为可选槽位 |
| motif / theme / plot_pattern 区分 | PASS | `required_invariants` 与 `ordered_slots` 已分离 |
| 至少两个来源实例 | PASS | 希伯来—圣经、美索不达米亚、希腊—罗马均已进入压力测试 |
| 每个来源有 `source_status` | PASS | 已区分 reference topic、story pending、external pending 等状态 |
| 主要变体识别 | PASS | 《创世记》《阿特拉哈西斯》《吉尔伽美什》XI、丢卡利翁／皮拉已形成有效差异矩阵 |
| 来源／定型文本分层 | PASS | early_witness / defining_text / defining_reworking / later_defining_reworking 已出现 |
| 传播与结构相似分离 | PASS | 已禁止“相似 = 传播” |
| 一条 relation 一种 `relation_type` | PASS | Content Pass B 已明确原子关系规则 |
| archetype / plot / symbol 关系 | CONTENT_PASS | 已识别候选关系，但尚未建立独立 relation entity |
| 后世实例具有 relation/evidence | NOT_YET | 当前 09 仍主要是来源／定型实例；现代／后世实例只有候选池，尚未形成正式关系记录 |

因此内容层已经通过，但数据层与后世关系证据仍未闭环。

---

# 3. 三个关键结构判断

## 3.1 `source_status` 应进入共享治理

结论：**YES**。

理由：它不是 motif 专属语义，而是所有 QC2 对象回指 QC1.1 时都会遇到的问题。

建议作为共享字段：

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

archetype、plot_pattern、symbol 后续都可能先发现跨传统材料，因此都需要这一层状态。

## 3.2 `required_invariants / optional_slots` 不应强制进入所有四类模板

结论：**只固定在 motif；其他类型按自身结构使用专属字段。**

```text
motif
→ required_invariants / optional_slots

plot_pattern
→ core_slots / optional_slots / repeatable_slots / terminal_variants

archetype
→ core_functions / variable_features / archetype_kind

symbol
→ admission_evidence / stable_meanings / meaning_shifts
```

共享的是“可区分核心与可变部分”的治理思想，不是同一套字段名。

## 3.3 relation record 原子性应进入共享治理

结论：**YES，且应在 Pilot B 前落实到数据实体。**

稳定规则：

```text
one relation record
=
one source
+
one target
+
one relation_type
+
one evidence_level
```

若同一对对象同时存在结构相似与可能传播，应是两条记录，而不是一个混合字段。

---

# 4. 是否需要现在建立共享 Base / relation schema？

结论：**需要。**

原因不是 Pilot A 文件太多，而是从 Pilot B 开始会出现四类对象之间的真实交叉：

```text
motif ↔ archetype
motif ↔ plot_pattern
motif ↔ symbol
archetype ↔ symbol
plot_pattern ↔ work
component ↔ QC1.1 source
component ↔ later work
```

如果继续只在说明页里写这些关系，四个 Pilot 会各自发明字段，最终难以统一查询。

建议先建立最小共享数据层，而不是复杂 ontology。

## 4.1 建议的最小实体一：`qc2_component_relation`

用于 QC2 对象之间，以及需要明确记录的跨对象关系。

```yaml
type: qc2_component_relation
source_component: WL-TOPIC-...
target_component: WL-TOPIC-...
relation_type: organized_by_plot_pattern
evidence_level: documented
source_evidence: []
status: pilot_relation
```

适合：

- motif → plot_pattern
- motif → archetype
- motif → symbol
- archetype → symbol
- component → component 的 inversion / overlap / representation 等

## 4.2 建议的最小实体二：`qc2_source_reference`

用于 QC2 对象回指 QC1.1 来源人物／故事／文本，不把来源状态塞进普通关系。

```yaml
type: qc2_source_reference
component_id: WL-TOPIC-...
source_tradition: WL-TOPIC-QC111
source_story: ...
source_text: ...
source_status: reference_topic
tradition_role: defining_text
sequence: ...
```

适合解决：

- 来源专题已完整；
- 来源专题存在但故事未索引；
- 外部文本已核证但 QC1.1 尚未建档。

## 4.3 建议的最小实体三：`qc2_work_reference`

用于后世作品／跨媒介实例。

```yaml
type: qc2_work_reference
component_id: WL-TOPIC-...
work: ...
work_role: later_reworking
retained_features: []
modified_features: []
relation_type: explicit_reference
evidence_level: documented
source_evidence: []
canonical_work: null
```

这样作品实例不会与 source reference 混在一起，也能继续遵守“一个主要归属地 + 多关系”。

---

# 5. Base 建议

不建议每个 QC2 组件各造一套不同 Base。

建议先做共享 Base 规范，组件专题可按 `component_id` 过滤：

```text
00/结构视图
→ qc2_component

来源视图
→ qc2_source_reference

组件关系视图
→ qc2_component_relation

作品实例视图
→ qc2_work_reference
```

这样 motif / archetype / plot_pattern / symbol 四类都能复用同一数据模型。

---

# 6. 是否现在拆“洪水幸存者 / 洪水结构 / 方舟”为独立 QC2 实体？

结论：**NO。**

当前保持候选关系更合理：

```text
洪水幸存者／第二祖先
→ archetype_candidate

失序→毁灭→幸存→重建
→ plot_pattern_candidate

方舟
→ symbol_candidate
```

原因：

1. archetype Pilot 尚未验证准入；
2. plot_pattern Pilot 尚未验证 ordered-slot 模型；
3. symbol Pilot 尚未验证“故事物件 → 稳定文化符号”的证据门槛；
4. 现在提前建档会用 motif Pilot 替另外三类 Pilot 做决定。

因此应等对应模板各自完成 Pilot 后再升级实体。

---

# 7. 后世实例仍是 Pilot A 的唯一内容缺口

当前 `09 作品实例与跨媒介使用` 已经建立严格的数据规则，但正式收入的仍主要是来源／定型级文本。

在最终 Acceptance 前，建议至少核证 2–3 个不同关系类型的后世实例：

```text
A direct_adaptation
B explicit_reference
C structural_inheritance 或 motif_inversion
```

目的不是丰富书单，而是验证 `qc2_work_reference` 是否真的可用。

---

# 8. 对其他三类模板的冲突检查

## archetype

无结构冲突。

需要继承：

- `source_status`
- relation record 原子性
- shared source/work reference schema

不继承 motif 的 `required_invariants` 字段；改用角色核心功能。

## plot_pattern

无结构冲突。

已有 `core_slots / optional_slots / repeatable_slots / terminal_variants`，与 motif 的 required/optional 分层互补而不重复。

需要继承：

- `source_status`
- relation record 原子性
- shared relation/work schema

## symbol

无结构冲突。

需要继承：

- `source_status`
- relation record 原子性
- source/work reference schema

symbol 的重点仍应是准入证据与语义漂移，不应复制 motif 字段。

---

# 9. Gate 判定

现在不建议直接进入 Pilot B 内容建设。

先完成一个很小的 **QC2 Shared Data Layer Pass**：

1. 在 Template V0 总则中固定三种共享关系实体；
2. 建立共享 Base 规范；
3. 用 Flood Pilot 写入最少真实关系记录；
4. 用 2–3 个正式后世实例验证 `qc2_work_reference`；
5. 再做 Pilot A Final Acceptance。

通过后再进入：

```text
Pilot B｜受苦义人 archetype
```

这样 archetype Pilot 将直接使用已有数据治理，不需要重新设计关系层。

---

# 10. 最终状态

```text
QC2_PILOT_A_STRUCTURE_REVIEW = PASS_WITH_DATA_LAYER_GATE_OPEN
QC2_PILOT_A_CONTENT = PASS
QC2_PILOT_A_FINAL_ACCEPTANCE = NOT_YET
QC2_SHARED_DATA_LAYER = REQUIRED
QC2_SHARED_RELATION_SCHEMA = REQUIRED
QC2_TEMPLATE_V0_CROSS_TYPE_CONFLICT = NONE_FOUND
QC2_COMPONENT_CANDIDATES_PROMOTION = DEFERRED
QC2_NEXT_STAGE = SHARED_DATA_LAYER_PASS
```
