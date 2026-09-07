---
id: WL-QC1.2
type: literature_node
name: 故事循环、人物传说与跨文本叙事传统
code: QC1.2
axis: Q
parent: WL-QC1
level: 4
node_kind: taxonomy_branch
status: ACTIVE
scope_note: "追踪具体故事、人物与故事群跨文本形成、传播和重写的叙事传统层"
---
# QC1.2 故事循环、人物传说与跨文本叙事传统

QC1.2 是 QC1 的**具体叙事传统层（cross-text narrative traditions）**。

它研究一个可识别的故事、人物、故事群或叙事集合如何穿过不同时代、语言、地域、作者、文类和媒介，形成具有自身历史生命的叙事传统。

## 1. 当前四类资源与模板状态

| resource_type | 说明 | 当前模板状态 |
|---|---|---|
| narrative_cycle | 围绕共同事件、人物群或世界形成的故事循环 | `FROZEN_V1` |
| figure_tradition | 围绕命名人物长期积累的叙事传统 | `FROZEN_V1` |
| collection_tradition | 故事集、框架叙事或叙事集合的形成、编纂与传播传统 | `FROZEN_V1` |
| story_tradition | 一个具体故事在多个文本与文化中的历时生命 | `NOT_FROZEN` |

正式专题仍需独立经过准入判断；模板存在不等于候选自动准入。

## 2. QC1.2 与 QC1.1 / QC2 的边界

### QC1.1
看一个文化／宗教／区域环境产生了什么叙事资源。

### QC1.2
看一个**具体命名叙事资源自己的历时生命**。

### QC2
从多个具体传统中抽取可复用 motif / role / symbol / structure / tale type。

例如：

```text
亚瑟王传统 → QC1.2 figure_tradition
圣杯故事传统 → 可评估 QC1.2 story_tradition
圣杯 symbol → QC2
神圣目标求索 → QC2
```

```text
《一千零一夜》集合传统 → QC1.2 collection_tradition
框架叙事 → QC2 narrative_structure
阿拉丁具体历时生命 → 可独立评估 story_tradition
```

## 3. narrative_cycle V1

参考样板：

- [[QC1.2.1 特洛伊故事循环]]
- [[QC1.2.2 沃尔松—尼伯龙根叙事传统]]

冻结模板：[[QC1.2 narrative_cycle 专题模板 V1]]  
冻结记录：[[QC1.2 narrative_cycle Stage Freeze Review V1]]

稳定职责：

```text
核心叙事材料
→ 文本见证
→ 谱系／版本／分支
→ 人物与结构变体
→ 后世重构
→ QC2 / evidence / reading
```

## 4. figure_tradition V1

参考样板：[[QC1.2.3 亚瑟王叙事传统]]

冻结模板：[[QC1.2 figure_tradition 专题模板 V1]]  
冻结记录：[[QC1.2 figure_tradition Stage Freeze Review V1]]

稳定核心能力：

```text
central_figure
court_or_world_framework
figure_network
subtradition
subtradition_status
text_stage
cycle_witness
component_witness
modern_figure_reinvention
```

核心机制：

```text
中心人物
→ 共享世界
→ 人物网络
→ 子传统
→ 文本循环／集成
→ 后世人物功能再发明
```

## 5. collection_tradition V1

参考样板：[[QC1.2.4 一千零一夜故事集合与传播传统]]

冻结模板：[[QC1.2 collection_tradition 专题模板 V1]]  
冻结记录：[[QC1.2 collection_tradition Stage Freeze Review V1]]

稳定核心能力：

```text
collection_boundary
collection_witness
manuscript_family
recension
story_membership
membership_status
translation_layer
editorial_recomposition
source_mode
addition_removal
```

可选能力：

```text
frame_narrative
edition_witness
translation_witness
source_layer
```

核心关系：

```text
story × collection_witness → membership_status
```

`membership_status V1`：

```text
core_attested
branch_attested
translation_added
later_print_added
absent_attested
uncertain
```

冻结依据包括 membership matrix 与现实阅读版本 provenance 两次真实数据实测，而不是仅凭页面结构判断。

## 6. QC1.2 的通用产品壳

三种已冻结类型共同支持：

```text
00 主页.md
01 Canvas.canvas
02 结构／谱系／版本.base
03 作品／文本投影.base
10–15 六层认知职责
Coverage Review
```

**冻结的是产品职责，不是所有专题必须使用相同二级标题。**

其中：

- `02` 的 semantic dimensions 随 resource_type 改变；
- `03` 只投影中央 `40 作品`；
- manuscript / witness / recension 等非作品对象不能为填表伪装成 work。

## 7. 正式专题准入门槛

原则上至少满足以下 6 项中的 4 项：

1. 可识别的故事核、人物核、循环或集合边界；
2. 跨多个时期；
3. 多个重要文本／版本／见证；
4. 演变谱系本身具有解释价值；
5. 有重要跨语言／地域／文类／媒介生命；
6. 对多部作品或多个 QC2 组件有解释复用价值。

仅仅“故事很有名”不足以准入。

## 8. 当前正式专题

- [[QC1.2.1 特洛伊故事循环]] — `narrative_cycle` — `STAGE_FROZEN`
- [[QC1.2.2 沃尔松—尼伯龙根叙事传统]] — `narrative_cycle` — `STAGE_FROZEN`
- [[QC1.2.3 亚瑟王叙事传统]] — `figure_tradition` — `STAGE_FROZEN`
- [[QC1.2.4 一千零一夜故事集合与传播传统]] — `collection_tradition` — `STAGE_FROZEN`

当前模板状态：

```text
narrative_cycle   → FROZEN_V1
figure_tradition  → FROZEN_V1
collection_tradition → FROZEN_V1
story_tradition   → NOT_FROZEN
```

## 9. 下一异质验证重点

现在不再继续做第二个 collection_tradition，也不继续扩展 narrative_cycle / figure_tradition。

下一步应测试最后一个尚未冻结的资源类型：

```text
story_tradition
```

优先候选应满足：

- 故事边界清楚；
- 有多个显著不同的文本版本；
- 不是单纯人物中心；
- 不依赖一个开放集合来维持身份；
- 与已建专题存在接口，但可以独立追踪。

当前候选池中，**圣杯叙事传统**与**特里斯坦—伊索尔德叙事传统**都具有较高验证价值。

## 10. 完整候选池

→ [[QC1.2 候选叙事传统池 V1]]

## 11. 建设状态原则

```text
candidate
→ boundary_check
→ source_readiness
→ admitted
→ topic_build
→ coverage_review
→ stage_frozen
```

冻结后，只有出现新阅读需求、关键新材料、明显结构缺口或证据修正时才重开。

> 上级：[[QC1 世界文化叙事传统|QC1 世界叙事资源与来源传统]]  
> 同级：[[QC1.1 神话、传说与民间叙事|QC1.1 神话、宗教与民间叙事来源传统]]  
> 候选池：[[QC1.2 候选叙事传统池 V1]]  
> narrative_cycle：[[QC1.2 narrative_cycle 专题模板 V1]]  
> figure_tradition：[[QC1.2 figure_tradition 专题模板 V1]]  
> collection_tradition：[[QC1.2 collection_tradition 专题模板 V1]]  
> 专属治理：[[QC1 建设规范 V1]]  
> 全局治理：[[QC 总体架构与建设规范 V2]]