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

它研究一个可识别的故事、人物或故事群如何穿过不同时代、语言、地域、作者、文类和媒介，形成具有自身历史生命的叙事传统。

它回答：

> **“这个故事／人物／故事循环是怎样形成、分叉、传播、被重新解释，并最终成为后世可以持续调用的叙事资源的？”**

QC1.2 的建立，是为了填补 [[QC1.1 神话、传说与民间叙事|QC1.1 来源传统]] 与 [[QC2 世界文化母题、原型与叙事结构|QC2 叙事组件]] 之间的尺度断层。

## 1. 典型对象

QC1.2 可以容纳四类主要对象：

| resource_type | 说明 | 当前模板状态 |
|---|---|---|
| narrative_cycle | 围绕共同事件、人物群或世界形成的故事循环 | `FROZEN_V1` |
| figure_tradition | 围绕命名人物长期积累的叙事传统 | `FROZEN_V1` |
| story_tradition | 一个具体故事在多个文本与文化中的历时生命 | 未验证 |
| collection_tradition | 故事集、框架叙事或叙事集合的形成、编纂与传播传统 | `BUILDING / QC1.2.4` |

正式专题仍需独立经过准入判断；模板存在不等于候选自动准入。

## 2. QC1.2 与 QC1.1 的区别

### QC1.1 看来源环境

```text
希腊—罗马神话传统
凯尔特—不列颠传说传统
日耳曼—北欧神话传统
中国神话—传说—民间传统
……
```

问题是：**这个文化世界产生了什么叙事资源？**

### QC1.2 看一个资源自己的生命史

```text
早期材料
→ 文本见证
→ 关键定型
→ 分支／人物网络／集合成员变化
→ 跨语言／地域传播
→ 重要重写／编辑重组
→ 现代再生产
```

问题是：**这个具体叙事传统怎样一路变化？**

一个 QC1.2 对象可以同时连接多个 QC1.1 来源传统；因此 QC1.2 不按文明硬分箱。

## 3. 与 QC2 的边界

QC1.2 研究**有名称、有历史、有文本见证的具体叙事传统**；QC2 研究从许多故事中抽象出的可复用组件。

例如：

```text
“亚瑟王传统” → QC1.2 figure_tradition
“圣杯故事传统” → 可独立评估 QC1.2 story_tradition
“圣杯”作为长期文化符号 → QC2 symbol
“求索神圣目标” → QC2 motif / plot_pattern
```

又如：

```text
“《一千零一夜》集合传统” → QC1.2 collection_tradition
“框架叙事” → QC2 structure
“故事中的故事” → QC2 narrative_structure
单个《阿拉丁》若形成独立历时生命 → 可评估 story_tradition
```

不得为了寻找共同母题而抹去具体文本谱系；也不得因为两个传统拥有相似组件，就推断二者存在历史传播。

## 4. 已冻结的 narrative_cycle V1

由 [[QC1.2.1 特洛伊故事循环]] 与 [[QC1.2.2 沃尔松—尼伯龙根叙事传统]] 两个结构差异明显的样板共同验证。

冻结模板：[[QC1.2 narrative_cycle 专题模板 V1]]  
冻结记录：[[QC1.2 narrative_cycle Stage Freeze Review V1]]  
样板比较：[[QC1.2 样板横向比较 V1]]

稳定骨架：

```text
10 定义、边界与核心叙事材料
11 早期材料与文本见证
12 文本谱系、版本与分支
13 人物与叙事结构变体
14 后世生命与跨语言／文类／媒介重构
15 QC2 组件、证据与阅读
```

## 5. 已冻结的 figure_tradition V1

由 [[QC1.2.3 亚瑟王叙事传统]] 作为第一个异质样板验证。

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

稳定认知职责：

```text
10 中心人物、边界与世界框架
11 早期人物与关键文本见证
12 多语言扩张、文本阶段与循环化
13 人物网络、子传统与升格边界
14 集成文本、后世再发明与现代生命
15 QC2 组件、证据与阅读
```

## 6. 正在验证的 collection_tradition

[[QC1.2.4 一千零一夜故事集合与传播传统]] 是第一个 `collection_tradition` 正式样板，已经完成 `boundary_check / source_readiness / admission / topic_build / first coverage_review`，当前状态：`COVERAGE_REVIEW_PASS_WITH_PATCH`。

第一轮已验证候选能力：

```text
collection_boundary
frame_narrative
collection_witness
manuscript_family
recension
story_membership
membership_status
addition_removal
translation_layer
editorial_recomposition
source_mode
```

其核心关系不是固定目录，而是：

```text
story × collection_witness → membership_status
```

冻结前仍需用真实数据完成 membership 对照矩阵与一个实际阅读版本的 provenance 实测，因此暂不把 `collection_tradition` 标为 `FROZEN_V1`。

## 7. 正式专题准入门槛

一个对象升格为正式 QC1.2 专题，原则上至少满足以下条件中的四项：

1. **可识别性**：存在相对稳定的故事核、人物核或循环／集合边界；
2. **历时性**：跨越多个时期，不能由单一作品完全解释；
3. **多文本性**：拥有多个重要文本见证、版本或重写；
4. **谱系价值**：其演变过程本身具有解释价值；
5. **跨语境生命**：发生重要的跨语言、地域、文类或媒介迁移；
6. **复用价值**：能显著帮助理解多部重要文学作品或多个 QC2 组件。

仅仅“故事很有名”不足以准入。

## 8. 当前正式专题

- [[QC1.2.1 特洛伊故事循环]] — `narrative_cycle`；第一冻结参考样板；`STAGE_FROZEN`。
- [[QC1.2.2 沃尔松—尼伯龙根叙事传统]] — `narrative_cycle`；第二冻结参考样板；`STAGE_FROZEN`。
- [[QC1.2.3 亚瑟王叙事传统]] — `figure_tradition`；第一冻结参考样板；`STAGE_FROZEN`。
- [[QC1.2.4 一千零一夜故事集合与传播传统]] — `collection_tradition`；第一集合型验证样板；`COVERAGE_REVIEW_PASS_WITH_PATCH`。

当前：

```text
narrative_cycle → FROZEN_V1
figure_tradition → FROZEN_V1
collection_tradition → BUILDING / COVERAGE_REVIEW_PASS_WITH_PATCH
story_tradition → NOT_FROZEN
```

## 9. 当前异质验证重点

QC1.2.4 不建设“1001个故事大全”，而测试：

```text
collection identity
→ collection witness / manuscript family / recension
→ story membership
→ translation layer
→ editorial recomposition
→ print / global reception
```

冻结前的两个实测任务：

1. 用 3 个代表性 witness × 5–10 个故事建立 membership 矩阵；
2. 选择一个真实可阅读版本，追踪底本、中介译本、成员选择和编辑路径。

## 10. 完整候选池

→ [[QC1.2 候选叙事传统池 V1]]

候选节点不等于正式 taxonomy。建设时仍从真实阅读问题、模板验证需求和 source readiness 反向选择对象，而不是按候选清单批量建包。

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
> narrative_cycle 模板：[[QC1.2 narrative_cycle 专题模板 V1]]  
> figure_tradition 模板：[[QC1.2 figure_tradition 专题模板 V1]]  
> 专属治理：[[QC1 建设规范 V1]]  
> 全局治理：[[QC 总体架构与建设规范 V2]]
