# QC2.1｜P1 世界父母分离结构｜Admission Research

> 状态：`PASS / PROMOTE_TO_TOPIC_BUILD_QUEUE`
>
> Candidate type：`plot_pattern`
>
> Primary cluster：`WL-QC2.1`
>
> 基线：`QC2 Plot Pattern Template V1 FROZEN`

---

## 1. Candidate

工作名：

```text
世界父母结合
→ 后代受限
→ 分离行动
→ 天地分离
→ 世界空间展开
```

本研究判断它是否足以成为独立 `plot_pattern`，而不是 M2「天地分离」motif 的冗余描述。

---

## 2. Plot-pattern 最低结构

建议冻结候选 core slots：

```text
S1 WORLD_PARENTS_JOINED
天／地或等价世界父母处于紧密结合、贴合或不可分状态

S2 OFFSPRING_CONSTRAINED
后代／生命位于二者之间，并因缺乏空间、光或自由而受到限制

S3 SEPARATION_ACTION
后代或明确的分离者采取行动，将世界父母分开

S4 COSMIC_SPACE_OPENED
天地成为分离的宇宙域，光、空气、空间或可居世界由此展开
```

最低判定：

```text
S1 → S2 → S3 → S4
```

必须具有顺序与因果，不是四个 motif 标签的并列。

---

## 3. 与 M2「天地分离」的边界

M2 已是正式 active motif：

```text
primordial_non_separation
+
cosmological_separation
+
world_space_result
```

P1 比 M2 多出并冻结：

```text
world-parent identity
+
offspring constraint
+
offspring/separator action as causal bridge
+
ordered slot sequence
```

因此：

```text
P1 full match
→ 通常实例化 M2

M2 instance
→ 不一定满足 P1
```

盘古式天地分离可满足 M2，但不要求世界父母与受限后代，故不构成 P1 full match。

结论：

```text
P1 ≠ M2 duplicated motif
P1 = independent plot_pattern candidate
```

---

## 4. 跨传统压力测试

### 4.1 Māori｜Ranginui / Papatūānuku

匹配：`FULL_MATCH`

```text
S1 Rangi / Papa 紧密结合
→ S2 子代被困于黑暗与狭窄空间
→ S3 子代商议并实施分离，Tāne 成功推开父母
→ S4 光与世界空间展开
```

source status：`external_source_verified_text_only`

证据锚点：Te Ara 对 Māori creation traditions、Rangi/Papa 与 Tāne 分离天地的说明。

### 4.2 Egyptian｜Nut / Geb / Shu

匹配：`FULL_MATCH / STRONG_VARIANT`

```text
S1 Nut（天）与 Geb（地）紧密结合
→ S2 创世空间尚未展开／二者之间缺乏独立空间
→ S3 Shu 介入并抬起 Nut，使天与地分离
→ S4 空气／天地之间的空间形成，宇宙结构展开
```

与 Māori 版本不同：分离者不是 world parents 的受压子代群体经协商行动，而是作为明确 cosmic separator 的 Shu；因此 S2 的“offspring constrained”可视为 strong variant 的功能等价压力点。

source status：`external_source_verified_text_only`

证据锚点：Met 对 Shu amulet 的馆藏说明明确称 Shu 在创世时通过抬起天空分开天地；其他埃及学资料也保存 Nut/Geb 紧密结合与 Shu 分离结构。

### 4.3 Greek｜Gaia / Ouranos / Kronos

匹配：`STRONG_VARIANT`

```text
S1 Gaia / Ouranos 形成 earth-sky parental pair
→ S2 Ouranos 将子代压回／隐藏于 Gaia 内部，Gaia 被压迫
→ S3 Gaia 提供镰刀，Kronos 对 Ouranos 实施断裂行动
→ S4 父子／天地结构发生不可逆分离，后续宇宙代际秩序展开
```

Hesiod 本文对“子代被压入大地—Gaia 受压—Kronos 行动”的因果非常明确；“天地空间展开”在希腊材料中不如 Māori / Egyptian 版本直接，因此保留 strong variant，不提升为 full match。

source status：`reference_topic`

来源：`QC1.1.2 希腊—罗马神话传统`。

---

## 5. Causal variants

P1 可以允许不同因果机制，但不能丢失“限制 → 分离行动 → 空间展开”的主链。

候选：

```text
CV1 offspring_liberation
后代因被困／缺乏光与空间而主动分离父母

CV2 cosmic_separator_intervention
由专门分离者／空气神介入，使天地获得间隔

CV3 parental_oppression_revolt
父辈压制子代，子代反抗造成天地／代际结构断裂
```

这些是 causal variants，不是新的 core slots。

---

## 6. Optional / repeatable / terminal variants

### optional slots

```text
siblings debate
failed separation attempts
divine tool / weapon
light enters world
air fills the gap
post-separation conflict
```

### repeatable slots

```text
multiple_attempts_to_separate
```

### terminal variants

```text
stable_separation
separation_plus_cosmic_ordering
separation_plus_subsequent_conflict
```

---

## 7. Boundary checks

```text
“天地分离”
→ motif M2

“世界父母”
→ 角色／symbolic personification，不自动构成 archetype

“代际反抗”
→ motif/theme candidate，不等于 P1

“世界父母结合→受限后代→分离→空间展开”
→ plot_pattern P1
```

P1 不要求：

- 父母必须都是神；
- 分离必须暴力；
- 分离者必须是子代之一；
- 分离后必须立即出现人类；
- 必须存在王权或神战。

---

## 8. Admission decision

```text
PLOT_PATTERN_SEQUENCE = PASS
CAUSAL_LINKAGE = PASS
CROSS_TRADITION_FULL_OR_STRONG_VARIANTS = PASS
MOTIF_BOUNDARY = PASS
THEME_BOUNDARY = PASS
SOURCE_STATUS_GOVERNANCE = PASS
```

最终：

```text
QC2.1_P1_ADMISSION_RESEARCH = PASS
QC2.1_P1_COMPONENT_TYPE = plot_pattern
QC2.1_P1_PROMOTE_TO_TOPIC_BUILD_QUEUE = YES
QC2_TEMPLATE_REOPEN_REQUIRED = NO
```

---

## 9. 与 M2 的未来正式 component relation

M2 已是正式 component，P1 目前仍处于 `ADMITTED_FOR_BUILD`，所以本研究阶段**仍不创建**正式 `qc2_component_relation`。

P1 专题完成并通过 component acceptance 后，可审查第一条自然跨类型关系：

```text
source_component: P1 世界父母分离结构
→ target_component: M2 天地分离
→ relation_type candidate: carries_motif / contains_motif / organized_by_plot_pattern 的方向性规范需以 V1 vocabulary 为准
```

必须先选择 V1 已冻结 vocabulary 中语义和方向最准确的 relation type；若现有 vocabulary 不足，不得临时发明新类型，应走 Governance Amendment。

---

## 10. Next stage

```text
QC2.1_NEXT_STAGE
= P1_WORLD_PARENTS_SEPARATION_TOPIC_BUILD
```

正式专题建立后，再做 component acceptance 与首条真实跨类型 relation review。
