---
id: WL-CN1-GOV-V1
legacy_id: WL-QC1-GOV-V1
type: literature_governance
name: CN1 建设规范 V1
namespace: CN
legacy_axis: Q
system_role: work_knowledge_network
scope: CN1
status: ACTIVE
version: "1.2"
---

# CN1 建设规范 V1

> 本文件是 [[CN 总体架构与建设规范 V2]] 在 CN1 层的实施规范。它规定 CN1.1 与 CN1.2 的分工、资源对象、专题准入、证据记录、产品结构与冻结机制。
>
> CN1.1 的具体产品模板以 [[CN1.1 来源传统专题模板 V1]] 为准；CN1.2 的 `narrative_cycle` 具体产品模板以 [[CN1.2 narrative_cycle 专题模板 V1]] 为准。

# 0. CN1 的建设目标

CN1 不建设“世界故事大全”，而建设**叙事资源的可追踪来源网络**。

一个成熟 CN1 系统应允许从某部作品中的典故、人物、情节或象征反向追踪：

```text
具体作品中的调用
      ↓
CN2 可复用叙事组件
      ↓
CN1.2 具体故事／人物／循环的文本传统
      ↓
CN1.1 更大的来源传统与形成环境
      ↓
早期见证、文本、口头材料、历史接触与证据
```

实际关系不要求严格单线展开；该图用于说明职责，而不是预设历史传播方向。

---

# 1. CN1 的两层尺度

## 1.1 CN1.1：来源环境尺度

对象：`source_tradition`

核心问题：

> **一个文化、宗教或区域叙事传统形成了怎样的叙事资源库？**

典型特征：

- 覆盖大量人物、故事、文本或口头材料；
- 有自身形成环境、宗教／仪式、社会结构或口传机制；
- 内部存在多个故事群、人物群、版本或文本传统；
- 适合作为来源导航 hub，而不是某个具体故事的详尽谱系。

当前 CN1.1 的 11 个来源 hubs 已冻结，不为了形式上的全球覆盖继续扩表。

## 1.2 CN1.2：具体叙事传统尺度

对象包括：

- `narrative_cycle`
- `story_tradition`
- `figure_tradition`
- `collection_tradition`

核心问题：

> **一个具体故事、人物或故事群如何跨文本形成自己的历史生命？**

典型特征：

- 可以建立最低限度 chronology；
- 存在多个重要文本见证或版本；
- 发生过重要分叉、传播、翻译或重写；
- 对多部文学作品或多个 CN2 component 具有解释复用价值。

---

# 2. 判定决策树

```text
A. 较大的文化／宗教／区域来源系统？
   是 → CN1.1
   否 → B

B. 有自身历时文本生命的具体故事、人物或故事群？
   是 → CN1.2
   否 → C

C. 跨故事反复出现的 motif / role / structure / symbol / tale type？
   是 → CN2
   否 → D

D. 一部具体作品或确定版本？
   是 → 40 作品 / work_reference / story_witness
   否 → E

E. 由制度、阶层、伦理和历史经验组织出的文化角色世界？
   是 → CN3
   否 → 普通知识笔记／数据实体，暂不升格 taxonomy
```

若对象同时涉及多个层次，分别建立关系，不通过复制正文解决。

---

# 3. 资源实体模型

CN1 常见对象：

```text
source_tradition
narrative_cycle
story_tradition
figure_tradition
collection_tradition
story_witness
```

最低字段按对象需要选择：

```yaml
resource_type:
name:
aliases: []
source_traditions: []
time_range:
regions: []
languages: []
earliest_witnesses: []
key_texts: []
branches: []
variants: []
qc2_links: []
source_references: []
```

这些是数据建模建议，不要求每篇 Markdown 机械显示全部字段。

---

# 4. 传统、文本见证与作品必须区分

```text
传统 tradition
≠
文本见证 story_witness
≠
具体作品 work
```

一部作品可以是某传统的重要 witness，但作品本身不等于整个传统。

反过来，抄本群、古代译本、版本传统、口头见证、编纂层或一部作品内部的细粒度诗篇，不应为了进入专题产品而被强制伪装成 `work`。

作品事实只在中央 `40 作品` 维护；专题通过局部字段和 Base 投影作品。

CN1.2.2 已验证：一个中央 work 可以继续下钻到多个 `story_witness`，作品数量不是专题成熟度指标。

---

# 5. 文本谱系与传播证据

## 5.1 时间先后不等于来源关系

至少区分：

- 明确改写／翻译；
- 明确引用或借名；
- 有研究支持的传播或继承；
- 可能传播；
- 共同来源；
- 独立平行；
- 弱结构相似；
- 未知。

## 5.2 禁止自动补线

不得因为情节、人物功能或结构相似，就自动建立 direct transmission。

所有传播、继承、借用关系遵循 [[CN 总体架构与建设规范 V2]] 的 GEN 证据等级；Canvas 同样不得用视觉连线暗示无证据关系。

---

# 6. CN1.1 专题产品标准

CN1.1 的 V1 产品结构已由 [[CN1.1.1 希伯来—圣经叙事传统]] 与 [[CN1.1.2 希腊—罗马神话传统]] 共同验证并冻结。

固定产品壳：

```text
00 主页.md
01 Canvas.canvas
02 结构.base
03 作品.base
10 传统本体与形成结构/
11 文本见证与内部演变/
12 叙事组件与跨文化关系/
13 后世接受与阅读/
```

四层职责：

```text
10 传统本体与形成结构
→ 传统是什么、怎样形成、怎样发生历史变化

11 文本见证与内部演变
→ 哪些文本／版本使传统可见，它们如何重组传统材料

12 叙事组件与跨文化关系
→ 向 CN2 提供什么，又与其他传统有什么可证实关系

13 后世接受与阅读
→ 后来如何被调用，我实际如何进入和阅读
```

二级页面不是固定目录；不同来源传统按自身材料调整。

完整固定项、可变项、作品字段与验收清单见 [[CN1.1 来源传统专题模板 V1]]。

特别规定：

1. 不再使用独立 `20 数据层` 作为 CN1.1 成熟专题的标准结构；
2. `11` 可以承载抄本、译本、版本群等非普通作品见证；
3. `11/谱系阅读入口` 与 `13/阅读路线` 分工，不重复；
4. Structure Base 使用语义字段，不以 `file.folder` 代替知识模型；
5. Works Base 只查询中央 `40 作品`；
6. `text_role` 字段通用，但角色词表允许按来源传统局部定义；
7. 作品池不设固定数量，约 15–25 个锚点只是当前经验尺度，20 本不是配额。

---

# 7. CN1.2 专题产品标准

## 7.1 当前模板状态

CN1.2 不再处于“完全未冻结”状态。

当前已完成：

```text
CN1.2.1 特洛伊故事循环      → STAGE_FROZEN
CN1.2.2 沃尔松—尼伯龙根    → STAGE_FROZEN
```

两个样板共同验证并冻结：

→ [[CN1.2 narrative_cycle 专题模板 V1]]

横向验证依据：

→ [[CN1.2 样板横向比较 V1]]

## 7.2 narrative_cycle V1 固定产品壳

```text
00 主页.md
01 Canvas.canvas
02 结构／谱系.base
03 作品／文本见证.base
10 定义、边界与核心叙事材料/
11 早期材料与文本见证/
12 文本谱系、版本与分支/
13 人物与叙事结构变体/
14 后世生命与跨语言／文类／媒介重构/
15 CN2 组件、证据与阅读/
```

规则：

- `00–03` 职责固定；
- `10–15` 编号和认知职责固定；
- 实际文件夹标题允许因专题材料局部改名；
- 二级页面数量不固定；
- chronology 是能力，不是唯一骨架；
- branch 是通用能力，但不强制所有专题形成树状 branch；
- 人物对应不等于 canonical identity；
- 非 work 型 witness 不强制进入中央作品库；
- 不设置固定作品数量配额。

## 7.3 适用边界

目前只冻结 `narrative_cycle`。

尚未验证：

- `figure_tradition`
- `story_tradition`
- `collection_tradition`

上述类型可以把 narrative-cycle V1 当候选起点，但不得在验证前直接宣布为同一固定模板。

下一异质样板应优先选择 `figure_tradition`。

---

# 8. 正式 taxonomy 准入

## 8.1 CN1.1

新增来源 hub 必须说明：

1. 为什么现有 11 hubs 无法合理容纳；
2. 是否拥有相对稳定的历史／文化／宗教叙事环境；
3. 是否拥有足够多的独立叙事资源，而非单一故事；
4. 新节点是否明显改善导航与解释，而不是增加目录完整感。

目前默认不新增。

## 8.2 CN1.2

候选对象至少满足以下六项中的四项：

- 可识别的核心叙事／人物／循环边界；
- 跨时期；
- 多文本；
- 有可研究的谱系或重要分叉；
- 有重要跨语言／地域／文类／媒介生命；
- 对多作品或多个 CN2 component 具有复用价值。

著名程度不是准入标准。

---

# 9. Candidate → Freeze 工作流

```text
candidate
↓
boundary_check
↓
source_readiness
↓
admission
↓
chronology_and_witness_build
↓
relation_build
↓
qc2_mapping
↓
coverage_review
↓
stage_freeze
```

## 9.1 source_readiness

至少确认：

- 有足够材料解释基本边界；
- 能建立最低限度 chronology；
- 能找到关键文本／版本，而非完全依赖二手摘要；
- 重要传播关系有来源可查。

## 9.2 stage_freeze

达到以下状态即可冻结：

- 核心边界稳定；
- 主要文本见证和转折已覆盖；
- 关键 CN2 映射已建立；
- 主要不确定性已明确标注；
- 产品接口稳定；
- 已足以服务当前阅读需求。

不要求：

- 研究完世界上所有材料；
- 补齐全部接受史；
- 达到固定作品数量；
- 为尚不存在的检索需求提前建实体。

## 9.3 reopen gate

只有出现以下情况才重开：

- 新阅读产生明确知识缺口；
- 获得改变现有谱系的重要材料；
- 发现错误关系或证据等级需修正；
- 新作品反复需要同一尚未建模的传统分支；
- 当前专题结构已阻碍检索或理解。

普通新增参考书目不自动触发重开。

---

# 10. 常用跨层关系

```text
belongs_to_tradition
contains_cycle
contains_story
contains_figure_tradition
attested_in
textualized_in
compiled_in
adapted_in
translated_into
transmitted_to
branches_into
variant_of
rewrites
receives_from
supplies_component
realizes_component
```

关系名用于数据层时保持稳定；Markdown 正文可使用自然语言。

---

# 11. 与其他轴的边界

| 问题 | 主要去向 |
|---|---|
| 来源传统怎样形成、有哪些重要文本见证？ | CN1.1 |
| 某具体故事／人物／循环如何跨文本演变？ | CN1.2 |
| 某叙事组件如何跨故事重复？ | CN2 |
| 某文化角色世界如何被历史制度塑造？ | CN3 |
| 作品讨论什么抽象问题？ | TH |
| 某种文学类型如何形成并运作？ | TY |
| 某地区文学历史如何发展？ | R |
| 某时期文学发生了什么？ | T |
| 某一具体文本／作品本身 | 40 作品 |

---

# 12. 当前建设策略

1. **CN1.1 的 11 个来源 hubs 保持冻结**，不为全球覆盖继续扩表；
2. **CN1.1.1 与 CN1.1.2 继续作为 V1 冻结参考样板**；
3. 后续 CN1.1.3–CN1.1.11 按 [[CN1.1 来源传统专题模板 V1]] 升级；
4. **CN1.2.1 与 CN1.2.2 已完成 stage freeze**；
5. **[[CN1.2 narrative_cycle 专题模板 V1]] 已冻结**，后续 narrative_cycle 默认遵循该 V1，除非材料明确要求局部偏离；
6. 下一个 CN1.2 正式验证样板必须优先选择不同 resource_type，而不是继续建立第三个 narrative_cycle 来证明同一件事；
7. 当前首选 `figure_tradition`，候选为亚瑟王叙事传统；
8. 第三样板重点验证人物网络、子人物传统、多语言扩张与 12–13 职责是否需要调整；
9. 在 `figure_tradition / story_tradition / collection_tradition` 获得足够验证前，不宣布 CN1.2 全类型统一模板；
10. CN1.1 与 CN1.2 均通过网络关系连接 CN2，不追求目录树表达全部知识。

当前成功标准不是节点数量，而是：**能否从作品调用反向追踪到组件、具体传统、来源环境和证据，同时保持不同文化材料的真实差异。**
