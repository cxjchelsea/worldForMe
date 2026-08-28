# QT8.2.1｜M5 Earth-diver / 潜水取土创世 Admission Research

> 目标：判断 Earth-diver 是否应作为 QT8.2.1 的独立 motif component 准入。
>
> 基线：`QT8.2 Motif Template V1 FROZEN`。
>
> 本文件只决定 Admission；不等于 Topic Build / Component Acceptance。

## 1. Working Definition

M5 研究的不是“水很多的创世神话”，也不是“动物帮助创世”，而是一种具有明确因果链的造陆机制：

```text
在尚无稳定陆地的 water-dominant world 中
→ 一个或多个行动者向水下潜降
→ 从水底取得 earth / mud / sand / soil 等地质材料
→ 该材料直接成为、被使用为或扩展为陆地
```

因此候选 required invariants 定为：

```text
R1 pre_land_water_dominant_world
R2 underwater_descent_for_earth_material
R3 retrieved_earth_material
R4 retrieved_material_causes_land_formation
```

其中 R4 是最低边界的关键：如果潜水取得的对象不参与陆地形成，就不属于本 motif。

## 2. Why `pre_land_water_dominant_world`, not `primordial_water_world`

不把 R1 写成绝对的 `primordial_water_world`，原因是：

- 部分传统存在上层 Sky World 或先存神祇／生命；
- Earth-diver 真正稳定的是“当前待形成世界尚无稳定陆地”，而不是“宇宙绝对什么都没有”；
- 这样可以容纳 Haudenosaunee / Iroquois 的 Sky World + lower water world，而不错误要求整个宇宙只有水。

因此：

```text
before stable land exists
≠ before anything exists
```

## 3. Required vs Optional Slots

### Required invariants

```text
R1 pre_land_water_dominant_world
R2 underwater_descent_for_earth_material
R3 retrieved_earth_material
R4 retrieved_material_causes_land_formation
```

### Optional slots

```text
animal_diver
multiple_failed_dives
small_or_unlikely_successful_diver
turtle_or_other_support_platform
creator_uses_retrieved_material
material_self_expands
sky_world_above
cooperative_creation
sacrifice_or_death_of_diver
post_flood_setting
```

这些都不能提升为 required invariants。

尤其：

```text
muskrat success
≠ Earth-diver 必需

turtle support
≠ Earth-diver 必需

animal diver
≠ 唯一可能 agent type
```

## 4. Comparative Motif Precedent

比较神话／民俗学已经长期把 Earth-diver 作为独立 creation-myth type 讨论。

Stith Thompson 的 *Motif-Index of Folk-Literature* 中存在 `A812 Earth Diver`；现代世界神话概论也将 Earth-diver 单列为 creation-myth type：动物潜入 primordial waters，取得 soil，soil 成为 Earth。

因此：

```text
EARTH_DIVER
= established comparative motif family
≠ repository-invented taxonomy
```

比较文献只证明 motif family 的学术先例与分布，不替代具体 tradition witness。

## 5. Tradition Witness A｜Haudenosaunee / Iroquois

Library of Congress 的 Iroquois creation material 明确描述：

```text
lower world contains only water and water creatures
→ Sky Woman falls
→ water creatures obtain earth from bottom of sea
→ earth is placed on Great Turtle
→ Earth forms
```

匹配：

```text
R1 = PASS
R2 = PASS
R3 = PASS
R4 = PASS
```

这里 Sky World 已存在不构成反例，因为待形成的 lower world 尚不存在稳定陆地。

### 结构意义

这个实例同时证明：

```text
Earth-diver
≠ ex nihilo creation
≠ sky-earth separation
≠ body-to-world transformation
```

世界陆地来自“潜水取得外部地质材料”，而不是空间分开或身体转化。

## 6. Tradition Witness B｜Slavic / Eastern European Earth-diver

Johns 对 Slavic creation narratives 的研究记录了一组明确 Earth Diver 传统：

```text
primeval ocean
→ devil or bird dives to bottom
→ retrieves earth
→ earth participates in world / land creation
```

文章同时指出此 motif 被记录于 Siberia、South / Southeast Asia、North America，并进入 Russia、Belarus、Ukraine、Hungary、Romania、Slovenia、Bulgaria 等 Eastern European traditions。

对 Slavic witness：

```text
R1 = PASS
R2 = PASS
R3 = PASS
R4 = PASS
```

其 agent structure 与 Haudenosaunee 明显不同，却保留同一最低因果链，因此提供独立跨传统压力测试。

## 7. Cross-Tradition Pressure Test

| Tradition | pre-land water world | underwater descent | earth material retrieved | land formation | Result |
|---|---|---|---|---|---|
| Haudenosaunee / Iroquois | YES | YES | YES | YES | FULL MATCH |
| Slavic / Eastern European | YES | YES | YES | YES | FULL MATCH |

两组传统的差异包括：

```text
Haudenosaunee
→ Sky Woman + animal cooperation + Turtle platform

Slavic variants
→ God / devil dualism or bird diver
```

但这些差异都不破坏 R1–R4。

因此 required invariants 具有跨传统稳定性，而不是某一个具体故事的复制。

## 8. Domain Gate｜Primordial Creation vs Post-Flood Recreation

这是本 Admission Research 的关键治理边界。

Earth-diver 结构也可出现在洪水后重建世界的故事中，例如某些现代整理版本：

```text
old world flooded
→ animals dive for mud
→ dry land is made again
```

这种结构与 M5 在形式上相似，但其问题域不同：

```text
first stable land formation
→ primary cluster: QT8.2.1

post-catastrophe land re-creation
→ primary cluster: QT8.2.2 毁灭、灾变与世界重生
```

因此正式 M5 component 采用：

```text
PRIMARY_ADMISSION_SCOPE
= pre-land / first-land cosmogonic Earth-diver
```

洪水后 Earth-diver：

```text
may be structural variant
may be secondary-cluster evidence
must NOT be used to inflate QT8.2.1 source count
```

这解决了 QT8.2.1 / QT8.2.2 域污染风险。

## 9. Boundary Tests

### M5 ≠ S2「原初水域」

```text
S2 candidate
= water as setting / substance / possible symbol

M5
= descent + retrieval + causal land formation
```

只有“世界最初是一片水”不满足 M5。

### M5 ≠ M2「天地分离」

```text
M2
= world-space via separation

M5
= land via retrieved material
```

二者机制不同。

### M5 ≠ M3「身体化为世界」

```text
M3
= body material → cosmos

M5
= retrieved geological material → land
```

来源材料完全不同。

### M5 ≠ generic emergence

从洞穴、地下世界、植物或母体“出现”到地表，并不自动满足：

```text
underwater descent
+
retrieved earth material
+
land formation
```

### M5 ≠ flood-rebirth motif

post-flood retrieval 可共享结构，但 primary problem domain 不同。

## 10. Incremental Explanatory Value

当前 QT8.2.1 已有：

```text
M2 separation
M3 bodily transformation
S1 gestational totality
S3 cosmic-axis organization
P1 ordered world-parent separation
```

M5 新增的是：

```text
retrieval-from-water
→ material acquisition
→ land formation / expansion
```

因此：

```text
M5_INCREMENTAL_EXPLANATORY_VALUE = HIGH
```

它不是现有 component 的细分复写。

同时还补足 North American / Eurasian Earth-diver tradition 的来源覆盖缺口。

## 11. Admission Decision

```text
QT8.2.1_M5_ADMISSION_RESEARCH = PASS
QT8.2.1_M5_COMPONENT_TYPE = motif
QT8.2.1_M5_REQUIRED_INVARIANTS = STABLE
QT8.2.1_M5_CROSS_TRADITION_PRESSURE = PASS
QT8.2.1_M5_PRIMORDIAL_VS_POST_FLOOD_BOUNDARY = PASS
QT8.2.1_M5_VS_M2_BOUNDARY = PASS
QT8.2.1_M5_VS_M3_BOUNDARY = PASS
QT8.2.1_M5_VS_S2_BOUNDARY = PASS
QT8.2.1_M5_INCREMENTAL_EXPLANATORY_VALUE = HIGH
QT8.2.1_M5_PROMOTE_TO_TOPIC_BUILD_QUEUE = YES
QT8.2_TEMPLATE_REOPEN_REQUIRED = NO
```

M5 正式从：

```text
SOURCE_READY_CANDIDATE
```

提升为：

```text
ADMITTED_FOR_BUILD
```

但仍未成为 `ACTIVE_V1_COMPONENT`。

## 12. Topic Build Gate

正式 Topic Build 必须保持：

```text
required_invariants:
  - pre_land_water_dominant_world
  - underwater_descent_for_earth_material
  - retrieved_earth_material
  - retrieved_material_causes_land_formation
```

并优先建立：

```text
Haudenosaunee / Iroquois source reference
Slavic / Eastern European source reference
additional third witness only if independently useful
```

不得把 post-flood Great Plains retelling 当作 QT8.2.1 的核心 defining source。

## 13. Next Stage

```text
QT8.2.1_NEXT_STAGE
= M5_EARTH_DIVER_MOTIF_TOPIC_BUILD
```

只有 Topic Build + Component Acceptance 通过后，M5 才成为 QT8.2.1 第六个 active component。
