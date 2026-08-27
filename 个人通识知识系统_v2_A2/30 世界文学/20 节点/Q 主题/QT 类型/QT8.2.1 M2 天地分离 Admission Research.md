# QT8.2.1｜M2 天地分离｜Admission Research

> component candidate：`天地分离`
>
> candidate type：`motif`
>
> primary cluster：`WL-QT8.2.1`
>
> baseline：`QT8.2 Motif Template V1 FROZEN`
>
> review status：`ADMISSION_RESEARCH_COMPLETE`

---

## 1. Admission question

本轮只回答：

> “天地分离”是否已经具备作为独立 `motif` component 的最低稳定性，而不是仅仅作为创世主题、一般宇宙论描述或某个 plot pattern 的一个槽位存在？

不在本轮建立完整专题包，也不把所有“世界父母”材料自动并入本 motif。

---

## 2. 工作定义

候选工作定义：

> **原本未充分分离、贴合、混合或处于同一原初整体中的天／地（或可明确对应的上、下宇宙域）发生分化，使世界形成上下空间，并由此获得可居住、可见或有序的宇宙结构。**

它是一个基本叙事关系／事件，不要求固定角色身份，也不要求完整的多节点顺序。

---

## 3. Required invariants

建议正式冻结为：

```text
R1 primordial_non_separation
= 天与地／上与下宇宙域在初始状态中尚未充分分离

R2 cosmological_separation
= 发生明确分离、拉开、上升／下沉、切开或等价的宇宙分化

R3 world_space_result
= 分离结果形成可辨识的上下世界空间／宇宙结构
```

其中：

```text
R1 + R2 + R3
= motif 最低辨识条件
```

如果只有“世界有天和地”，没有从未分状态到分离状态的转变，不准入。

---

## 4. Optional slots

以下均为高频实现，但不属于 required invariants：

```text
personified_sky_and_earth
world_parents
offspring_trapped_between_parents
named_separator_agent
violent_or_sexual_separation
light_enters_after_separation
intermediate_air_or_habitable_space
pillar_or_body_holds_realms_apart
yin_yang_or_light_heavy_differentiation
body_to_world_transformation
```

特别注意：

```text
world_parents
≠ required invariant

offspring trapped
≠ required invariant

specific separator hero/deity
≠ required invariant
```

否则 motif 会被错误收窄成 P1「世界父母分离」plot pattern。

---

## 5. Cross-tradition source pressure test

### 5.1 中国｜盘古／《三五历纪》引文

`source_status: external_source_verified_text_only`

《艺文类聚》引徐整《三五历纪》保存的文本明确写到天地原初混沌如鸡子，随后“天地开辟”，清阳为天、阴浊为地，盘古处于其中，天地继续拉开距离。

匹配：

```text
R1 = YES
R2 = YES
R3 = YES
world_parents = NO
named_separator_agent = PARTIAL / Pangu present
```

这说明“天地分离”不依赖 world-parent 结构，也可以通过宇宙物质的上升／下沉完成。

证据：
- https://ctext.org/text.pl?if=gb&node=539866
- Wu Xiaodong, “Pangu and the Origin of the Universe” (Brill volume excerpt)

### 5.2 Māori｜Rangi 与 Papa

`source_status: external_source_verified_text_only`

George Grey 1855 收录的 Māori 创世叙事明确描述 Rangi（天）与 Papa（地）原本紧密相连，天地尚未分开，子代生活在黑暗中；后代讨论并最终把父母分开，使光与空间出现。

匹配：

```text
R1 = YES
R2 = YES
R3 = YES
world_parents = YES
trapped_offspring = YES
separator_agent = YES
```

这是 M2 与 P1 的典型重叠实例：

```text
同一来源
→ 可以实例化 M2 motif
→ 也可能实例化 P1 plot_pattern
```

但两者不应合并。

证据：
- George Grey, Polynesian Mythology and Ancient Traditional History of the New Zealand Race (1855)
- https://www.originalsources.com/Document.aspx?DocID=GZ71R9LJYA4UG5C

### 5.3 希腊｜Gaia 与 Ouranos

`source_status: reference_topic`

QT8.1.2 希腊—罗马神话传统已存在。Hesiod《神谱》中 Gaia 生出 Ouranos 覆盖她，Ouranos 将子代压回 Gaia 内部；Cronos 对 Ouranos 的暴力行动结束这一压迫结构。古典注释传统长期把该段作为 Heaven / Earth separation 解释。

本轮处理为：

```text
R1 = STRONG_VARIANT
R2 = STRONG_VARIANT
R3 = IMPLICIT / COMPARATIVE_INTERPRETATION
```

因此希腊材料可作为强变体，但不拿它单独定义 M2 的 required invariants。

证据：
- Hesiod, Theogony 104–206, Perseus Digital Library
- https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0130:card=104
- https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0130:card=173

---

## 6. Boundary test

### 6.1 与 theme 的边界

```text
“混沌与秩序”
= theme / problem domain

“天地从未分状态被分开”
= motif
```

M2 必须有一个可叙述的宇宙转变事件，不是抽象价值或哲学对立。

### 6.2 与 P1 plot pattern 的边界

M2 只要求：

```text
non-separated sky/earth
→ separation
→ world-space result
```

P1 额外要求稳定角色—因果顺序：

```text
world parents joined
→ offspring constrained
→ offspring/separator acts
→ parents separated
→ habitable space opens
```

因此：

```text
P1 instance
→ usually contains M2

M2 instance
→ does NOT necessarily satisfy P1
```

盘古材料就是关键反例：它支持 M2，但不需要 world-parent + offspring sequence。

### 6.3 与 symbol 的边界

“天”“地”“天地结合”本身不因反复出现就自动成为 symbol。

M2 研究的是叙事事件；未来若某一具体形象（如宇宙卵、世界树）形成稳定跨文本意义，应另按 symbol admission 处理。

---

## 7. Source-governance decision

当前可用来源状态：

```text
QT8.1.2 Greek-Roman
→ reference_topic

Chinese Pangu
→ external_source_verified_text_only
→ future QT8.1.7 backfill candidate

Māori Rangi-Papa
→ external_source_verified_text_only
→ current QT8.1 taxonomy has no dedicated Oceania topic
```

治理结论：

```text
QT8.2 source attestation
≠ QT8.1 source topic completion
```

所以不需要等待 QT8.1.7 或未来 Oceania 来源专题建设完毕，才允许 M2 准入；但正式 source reference 必须保留真实 `source_status`，不得冒充 reference_topic。

---

## 8. Admission decision

三组压力材料已经满足：

```text
跨文化重复出现 = YES
最低叙事单元可定义 = YES
required_invariants 可稳定分离 = YES
optional slots 可变 = YES
不依赖固定人物身份 = YES
不依赖 ordered plot sequence = YES
与 theme 边界 = PASS
与 P1 plot_pattern 边界 = PASS
与 symbol 边界 = PASS
来源治理可表达 = PASS
```

因此：

```text
QT8.2.1_M2_ADMISSION_RESEARCH = PASS
QT8.2.1_M2_COMPONENT_TYPE = motif
QT8.2.1_M2_WORKING_NAME = 天地分离
QT8.2.1_M2_REQUIRED_INVARIANTS = STABLE
QT8.2.1_M2_SOURCE_PRESSURE_TEST = PASS
QT8.2.1_M2_BOUNDARY_TEST = PASS
QT8.2.1_M2_PROMOTE_TO_TOPIC_BUILD_QUEUE = YES
```

但本轮不等于专题完成：

```text
M2_ADMITTED_FOR_BUILD
≠ M2_TOPIC_ACCEPTED
```

---

## 9. Topic-build authorization

下一阶段允许创建正式 motif 专题包：

```text
QT8.2.1 创世、宇宙与世界秩序
└─ 天地分离
   └─ component_type: motif
```

建议正式 component id：

```text
WL-TOPIC-QT821-SKY-EARTH-SEPARATION
```

首批 source references：

```text
1. Chinese Pangu / Sanwu Liji citation
2. Māori Rangi-Papa / Grey 1855
3. Greek Gaia-Ouranos / Hesiod（strong variant）
```

正式 Topic Build 时应再决定是否补入 Mesopotamian、Egyptian、Japanese 等材料，不在 admission 阶段追求穷尽。

---

## 10. Next stage

```text
QT8.2.1_NEXT_STAGE
= M2_SKY_EARTH_SEPARATION_TOPIC_BUILD

P1_ADMISSION_RESEARCH
= NOT_STARTED_THIS_PASS

S1_ADMISSION_RESEARCH
= NOT_STARTED_THIS_PASS
```
