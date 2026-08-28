# QC2.1｜M5 Earth-diver Source Readiness Review

> Purpose: 判断 M5 是否已有足够来源基础进入正式 Motif Admission Research。
>
> 本文件不是 Admission Research，不授权 Topic Build。

## 1. Candidate Structure

工作结构：

```text
water-covered or water-dominant world
→ one or more beings dive downward
→ earth / mud / sand / material is retrieved
→ retrieved material becomes or expands into land
```

暂不把：

```text
specific diver species
multiple failed attempts
muskrat success
turtle support
creator command
post-flood setting
```

写入 required invariants；这些可能只是传统变体或 optional slots。

## 2. Comparative Motif Evidence

Stith Thompson 的 *Motif-Index of Folk-Literature* 将 `A812 Earth Diver` 作为独立叙事母题记录，核心正是：原初海上由动物下潜取得泥土，成功取得的少量泥土被用来形成大地；其分布索引同时指向 Siberian、India 与 North American Indian 传统。

这一点足以证明 M5 不是为了补地图临时发明的分类，而是有成熟 comparative-folklore precedent。

## 3. North American Source Readiness

当前已有多个独立来源入口：

### Haudenosaunee / Iroquois

Library of Congress 的 Iroquois creation 展示材料明确描述：Sky Woman 落入水世界后，水中生物从海底带来泥土，泥土置于 Great Turtle 背上并形成大地。

这提供：

```text
water_world
+ animal_diving / retrieval
+ retrieved_earth
+ land_formation
```

### Algonquin / Great Plains reception

Smithsonian Libraries 的 *Remaking the Earth* 馆藏摘要明确将其称为 Algonquin “Earth Diver” creation myth：动物潜入水中寻找泥土，随后 Creator 以其制造 dry land。

### Lenape

Nanticoke and Lenape Confederation Museum 保存的 Lenape creation account 中，Muskrat 带回水底泥土，泥土被置于 Turtle 背上并不断扩展成陆地。

结论：North American source readiness 不再是 blocker。

## 4. Eurasian / Siberian Comparative Readiness

第二条来源轴也已经存在。

Thompson A812 明确列出 Siberian 分布；现代比较研究同样把 Earth-diver 作为 Siberia / South Asia / North America 之间的重要共享神话类型讨论。

Slavic creation-narrative 研究也记录：神／魔或鸟从原初海底取得泥土的 Earth Diver motif 广泛出现于 Siberia、South/Southeast Asia、North America，并进入 Eastern European / Finno-Ugric–Slavic 传统。

因此：

```text
EARTH_DIVER_GEOGRAPHIC_DISTRIBUTION
≠ NORTH_AMERICA_ONLY
```

但正式 Admission Research 仍须选择具体 tradition witnesses，而不能只用分布综述代替 source records。

## 5. Critical Domain Boundary

当前最大风险不是“来源不足”，而是：

```text
primordial creation
vs
post-flood re-creation
```

Earth-diver 传统中两者都存在。

QC2.1 的主问题是创世／宇宙形成；QC2.2 则处理毁灭、灾变与世界重生。

因此正式 Admission Research 必须区分：

```text
A. primordial-water land creation
→ primary fit: QC2.1

B. flood-destroyed-world recreation by diving for earth
→ likely primary fit: QC2.2
→ may be secondary evidence for M5 structure only if domain role is explicit
```

禁止为了扩大实例数，把所有洪水后复土故事都无差别纳入 QC2.1。

## 6. Required Admission Questions

正式 M5 Admission Research 必须回答：

1. required invariants 是否应要求 `primordial_water_world`，还是更中性的 `water_dominant_world_before_land`；
2. `diver descends` 是否必须由动物承担，还是神、人、鸟类均可；
3. 是否必须有 `retrieved_material_expands_into_land`，还是“被 creator 使用成陆地”也满足；
4. post-flood recreation 是否只作为 secondary-cluster variant；
5. 至少两个独立 tradition witnesses 是否能在不依赖单一比较综述的情况下完整满足核心结构；
6. 与 S2「原初水域」setting、QC2.2 flood-rebirth、以及 generic emergence motif 的边界是否稳定。

## 7. Readiness Decision

```text
QC2.1_M5_SOURCE_READINESS_REVIEW = PASS
QC2.1_M5_COMPARATIVE_MOTIF_PRECEDENT = STRONG
QC2.1_M5_NORTH_AMERICAN_SOURCE_READINESS = PASS
QC2.1_M5_EURASIAN_COMPARATIVE_READINESS = PASS
QC2.1_M5_DOMAIN_BOUNDARY_RISK = MANAGEABLE_BUT_MUST_BE_TESTED
QC2.1_M5_READY_FOR_ADMISSION_RESEARCH = YES
QC2.1_M5_TOPIC_BUILD_AUTHORIZED = NO
QC2_TEMPLATE_REOPEN_REQUIRED = NO
```

## 8. Next Stage

```text
QC2.1_NEXT_STAGE
= M5_EARTH_DIVER_MOTIF_ADMISSION_RESEARCH
```

Admission Research 应优先选取：

```text
North American primary/ethnographic witness
+
second independent North American or Eurasian witness
+
comparative motif literature only as distribution/context support
```

通过 Admission Research 后，才决定是否建设第六个 active component。