---
id: WL-QC12-FIGURE-TRADITION-TEMPLATE-V1
type: literature_governance_template
system_role: work_knowledge_network
scope: QC1.2
resource_type: figure_tradition
status: FROZEN_V1
version: "1.0"
validated_by:
  - WL-QC1.2.3
---
# QC1.2 figure_tradition 专题模板 V1

> 本模板由 [[QC1.2.3 亚瑟王叙事传统]] 作为首个 `figure_tradition` 异质样板验证。
>
> 它冻结的是人物中心型叙事传统的 V1 产品能力，不自动适用于 `story_tradition` 或 `collection_tradition`。

# 1. 核心目标

一个成熟的 `figure_tradition` 专题应回答：

> **一个命名中心人物如何在多文本、多语言、多时期中持续被重写，并通过共享世界、人物网络和子传统维持自身的传统同一性？**

其核心不必是一条固定 biography，也不要求中心人物在每部作品里都是行动主角。

通用模型：

```text
central_figure
      ↓
court_or_world_framework
      ↓
figure_network
      ↓
subtraditions
      ↓
text stages / cycles / integrations
      ↓
modern figure reinvention
      ↓
QC2 abstract interfaces
```

---

# 2. 冻结的产品壳

```text
00 主页.md
01 Canvas.canvas
02 结构／人物网络.base
03 作品／文本见证.base
10 中心人物、边界与世界框架/
11 早期人物与关键文本见证/
12 多语言扩张、文本阶段与循环化/
13 人物网络、子传统与升格边界/
14 集成文本、后世再发明与现代生命/
15 QC2 组件、证据与阅读/
```

规则：

- `00–03` 职责固定；
- `10–15` 固定认知职责，不强制固定中文标题；
- 二级页面数量按材料决定；
- 不因人物网络庞大而建设人物百科。

---

# 3. 六项核心建模能力

## 3.1 `central_figure`

记录传统的命名中心人物。

中心人物可以：
- 是某些文本主角；
- 在另一些文本中退居王廷／世界中心；
- 作为合法性、共同体或象征性中心维持传统归属。

`central_figure` 不等于“每个故事的 protagonist”。

## 3.2 `court_or_world_framework`

记录能够吸附其他人物和故事的共享世界框架，例如：

```text
Arthur
→ Camelot / Round Table / Arthurian court
```

该框架是 `figure_tradition` 能容纳大量非中心人物故事的重要机制。

## 3.3 `figure_network`

人物网络不是普通人物表，而是记录：

- 与中心人物的关系；
- 在共享世界中的叙事功能；
- 不同文本阶段中的功能变化；
- 是否形成自己的长期子传统。

建议局部字段：

```yaml
figure_name:
network_role:
relation_to_central_figure:
text_stages: []
subtradition_status:
```

## 3.4 `subtradition`

子传统用于处理“既属于大人物传统、又已经拥有较强独立生命”的对象。

V1 使用三档：

```text
embedded
semi_independent
independent_candidate
```

- `embedded`：主要依赖中心人物／共享世界；
- `semi_independent`：拥有明显自主文本生命，但仍强依赖上级世界；
- `independent_candidate`：已具备独立 QC1.2 准入可能，应单独做 source readiness。

不得仅因人物知名就自动拆分独立专题。

## 3.5 多层 witness

`figure_tradition` 必须允许：

```text
figure_tradition
→ cycle_witness
→ component_witness / story_witness
→ work（若适合作为中央作品独立管理）
```

因此：

```text
tradition ≠ cycle_witness ≠ component_witness ≠ work
```

大型文本循环不得为了进入 Works Base 被压平成一本虚构作品。

## 3.6 `modern_figure_reinvention`

至少保留一个能证明“中心人物功能发生历史性变化”的后世锚点。

观察重点：
- 人物代表的政治／伦理问题是否改变；
- 人物是英雄、统治者、失败者、民族象征还是现代心理／政治模型；
- 传统如何在现代文类与媒介中重新解释中心人物。

不要求建立完整接受史。

---

# 4. 稳定的认知职责

## 10 中心人物、边界与世界框架

回答：
- 中心人物是谁；
- 传统边界为何不等于人物 biography；
- 什么共享世界使人物群持续聚合；
- 与一般类型／来源传统如何区分。

## 11 早期人物与关键文本见证

回答：
- 最早材料如何呈现该人物；
- 哪些文本使人物获得较连贯形象；
- 哪些是 work，哪些是 witness 群；
- 早期材料的不确定性如何标记。

## 12 多语言扩张、文本阶段与循环化

回答：
- 人物传统如何跨语言、地域和文类扩张；
- 单篇故事如何逐步形成大型文本网络；
- 哪些文本阶段改变了人物世界结构。

## 13 人物网络、子传统与升格边界

回答：
- 哪些人物围绕中心人物形成稳定网络；
- 哪些人物／故事形成独立子传统；
- 什么条件触发拆分为独立 QC1.2；
- 人物对应与功能变化如何记录。

## 14 集成文本、后世再发明与现代生命

回答：
- 哪些文本重新集成多个既有子传统；
- 后世如何选择、删改、压缩人物网络；
- 现代语境如何重新定义中心人物。

## 15 QC2 组件、证据与阅读

负责：
- 将具体人物／故事抽象到 QC2；
- 区分 symbol / motif 与具体 story tradition；
- 标记文本关系证据；
- 提供不同阅读入口。

---

# 5. 证据纪律

冻结以下原则：

1. 人物同名／相似 ≠ 完全同一文本功能；
2. 王廷网络归属 ≠ 直接文本来源；
3. 子传统被某一大型循环吸收 ≠ 失去独立传统生命；
4. 后世集成文本 ≠ 早期传统原貌；
5. 编纂顺序 ≠ 创作顺序；
6. `cycle_witness` 内部组件可以各自拥有独立文本生命；
7. Canvas 的网络边表示归属／功能／可证关系，不得暗示未经证实的来源链。

---

# 6. Works Base 与 witness 规则

中央 `40 作品` 仍是 work 事实唯一来源。

进入中央 Works Base 的对象应至少满足一个条件：
- 是可独立阅读／引用的作品；
- 多专题需要复用其作品事实；
- 需要独立维护作者、年代、语言、阅读状态；
- 不中央化会造成重复书目事实。

大型循环、抄本群、文本集合若不满足独立 work 语义，保留为局部 witness。

作品数量不是成熟度指标。

---

# 7. Stage Freeze 条件

`figure_tradition` 可冻结，当：

- 中心人物边界稳定；
- 共享世界框架可解释主要网络；
- 主要人物网络已建立；
- 强子传统已识别并标明自治程度；
- 关键文本阶段和 witness 已覆盖；
- 至少一个后世人物功能重构锚点存在；
- QC2 接口和证据纪律可用；
- 当前结构足以服务阅读，不要求穷尽所有人物／作品。

---

# 8. Reopen Gate

仅在以下情况下重开模板或专题：

- 新 figure_tradition 样板无法由当前能力解释；
- 多个专题反复需要当前不存在的人物网络关系类型；
- subtradition 三档无法表达真实自治程度；
- 多层 witness 模型出现系统性缺口；
- 当前结构阻碍实际检索和阅读。

局部新增人物或作品不自动触发模板重开。

---

# 9. 当前验证边界

V1 由亚瑟王传统单个高复杂度样板验证，因此属于：

> **figure-tradition validated V1 skeleton**

后续应优先用另一种人物传统（如浮士德、亚历山大、木兰等）做反例校验，而不是立即重写模板。

`story_tradition` 与 `collection_tradition` 仍未冻结。
