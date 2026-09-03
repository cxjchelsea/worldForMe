---
id: WL-QC1-GOV-V1
type: literature_governance
name: QC1 建设规范 V1
axis: Q
scope: QC1
status: ACTIVE
version: "1.0"
---

# QC1 建设规范 V1

> 本文件是 [[QC 总体架构与建设规范 V2]] 在 QC1 层的实施规范。它规定 QC1.1 与 QC1.2 的分工、资源对象、专题准入、证据记录、专题产品结构以及冻结机制。

# 0. QC1 的建设目标

QC1 不建设“世界故事大全”，而建设**叙事资源的可追踪来源网络**。

一个成熟 QC1 系统应允许从某部作品中的典故、人物、情节或象征反向追踪：

```text
具体作品中的调用
      ↓
QC2 可复用叙事组件
      ↓
QC1.2 具体故事／人物／循环的文本传统
      ↓
QC1.1 更大的来源传统与形成环境
      ↓
早期见证、文本、口头材料、历史接触与证据
```

实际关系不一定严格沿此方向单线展开；该图用于说明各层职责。

---

# 1. QC1 的两层尺度

## 1.1 QC1.1：来源环境尺度

对象：`source_tradition`

核心问题：

> **一个文化、宗教或区域叙事传统形成了怎样的叙事资源库？**

典型特征：

- 覆盖大量人物、故事和文本；
- 有自身形成环境、宗教／仪式或口传机制；
- 内部存在多个故事群与版本；
- 适合作为导航 hub，而不是某个具体故事的详尽谱系。

## 1.2 QC1.2：具体叙事传统尺度

对象包括：

- `narrative_cycle`
- `story_tradition`
- `figure_tradition`
- `collection_tradition`

核心问题：

> **一个具体故事、人物或故事群如何跨文本形成自己的历史生命？**

典型特征：

- 可以建立基本 chronology；
- 存在多个重要文本见证／版本；
- 发生过重要分叉、传播或重写；
- 对多部文学作品具有解释复用价值。

---

# 2. 判定决策树

新材料进入 QC1 时，按以下顺序判断：

```text
A. 研究对象是不是一个较大的文化／宗教／区域来源系统？
   是 → QC1.1 候选
   否 → B

B. 它是不是一个有自身历时文本生命的具体故事、人物或故事群？
   是 → QC1.2 候选
   否 → C

C. 它是不是跨故事反复出现的 motif / role / structure / symbol / tale type？
   是 → QC2
   否 → D

D. 它是不是一部具体作品或某一确定版本？
   是 → 40 作品 / work_reference / story_witness
   否 → E

E. 它是不是由制度、阶层、伦理和历史经验共同组织出的文化角色世界？
   是 → QC3
   否 → 普通知识笔记／数据实体，暂不升格 taxonomy
```

若对象同时符合多个层次，分别记录关系，不通过复制正文解决。

---

# 3. 资源实体模型

## 3.1 source_tradition

最低字段建议：

```yaml
resource_type: source_tradition
name:
aliases: []
time_range:
regions: []
languages: []
religious_context: []
oral_context: []
textual_witnesses: []
major_cycles: []
major_figures: []
major_stories: []
qc2_links: []
source_references: []
```

## 3.2 narrative_cycle

```yaml
resource_type: narrative_cycle
name:
aliases: []
source_traditions: []
core_figures: []
core_events: []
earliest_witnesses: []
key_texts: []
branches: []
qc2_links: []
source_references: []
```

## 3.3 figure_tradition

```yaml
resource_type: figure_tradition
name:
aliases: []
source_traditions: []
earliest_witnesses: []
identity_variants: []
key_texts: []
major_rewrites: []
qc2_links: []
source_references: []
```

## 3.4 story_tradition

```yaml
resource_type: story_tradition
name:
aliases: []
source_traditions: []
core_narrative:
earliest_witnesses: []
variants: []
key_texts: []
qc2_links: []
source_references: []
```

## 3.5 collection_tradition

```yaml
resource_type: collection_tradition
name:
aliases: []
source_traditions: []
compilation_history: []
frame_structure:
textual_layers: []
translation_routes: []
key_editions: []
qc2_links: []
source_references: []
```

这些字段是数据建模建议，不要求每篇 Markdown 都机械显示所有字段。

---

# 4. story_witness 与“传统”的区别

QC1 必须区分：

```text
传统 tradition
≠
文本 witness
≠
现代作品 work
```

例如某个中世纪文本可以是“亚瑟王传统”的重要 witness，但文本本身仍然是具体作品，不应与整个传统合并为一个知识对象。

同理，后世小说、电影或游戏可能参与传统再生产，但不因流行就自动成为“传统的来源”。

---

# 5. 文本谱系规则

## 5.1 谱系不是简单时间线

时间先后只能证明“早于／晚于”，不能自动证明“来源于”。

文本谱系至少区分：

- 明确改写／翻译；
- 明确引用或借名；
- 有研究支持的传播或继承；
- 可能的传播；
- 共同来源；
- 独立平行；
- 仅结构相似；
- 未知。

## 5.2 禁止自动补线

不得因为：

- 情节相似；
- 人物功能相似；
- 都存在洪水、龙、神树、英雄试炼等；
- 后世理论家把二者并列；

就自动建立 direct transmission。

关系必须遵循全局 GEN 证据等级。

---

# 6. QC1.1 专题产品标准

已有 QC1.1 专题包继续保留当前产品壳：

```text
00 主页.md
01 Canvas.canvas
02 结构.base（或现有同类 Base）
03 作品.base（或现有同类 Base）
```

内容层逐步统一为：

```text
10 传统边界
11 形成环境
12 叙事世界
13 核心叙事群
14 载体演化
15 文本谱系
16 内部变体
17 跨文化传播
18 QC2 组件映射
19 后世生命
20 阅读路线与数据层
```

这是**解释问题清单**，不是要求所有标题逐字一致。

---

# 7. QC1.2 专题产品标准

正式 QC1.2 专题建议沿用同一种最小产品壳，以保持整个世界文学系统的一致操作体验：

```text
00 主页.md
01 Canvas.canvas
02 谱系／结构.base
03 作品／文本见证.base
```

内容层：

```text
10 定义与边界
11 早期材料与最初见证
12 核心叙事核
13 文本谱系
14 地域、语言与版本分支
15 人物与叙事结构的历史变化
16 文类与媒介迁移
17 传播、借用与证据
18 QC2 组件地图
19 后世生命与现代再发明
20 阅读路线与数据层
```

---

# 8. 正式 taxonomy 准入

## 8.1 QC1.1 准入

新增来源 hub 必须说明：

1. 为什么现有 11 个 hubs 无法合理容纳；
2. 它是否拥有相对稳定的历史／文化／宗教叙事环境；
3. 是否拥有足够多的独立叙事资源，而非单一故事；
4. 新节点是否明显改善导航与解释，而不是只增加目录完整感。

## 8.2 QC1.2 准入

候选对象至少满足以下六项中的四项：

- 可识别的核心叙事／人物／循环边界；
- 跨时期；
- 多文本；
- 有可研究的谱系或重要分叉；
- 有重要跨语言／地域／媒介生命；
- 对多作品或多个 QC2 component 具有复用价值。

## 8.3 不以“著名程度”为准入标准

高知名度对象可能只需要一个实体页；较不知名但对大量文学作品有谱系解释价值的对象反而可能值得深建。

---

# 9. Candidate → Freeze 工作流

QC1 专题统一采用：

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

- 有足够可靠材料解释基本边界；
- 能建立最低限度 chronology；
- 能找到关键文本／版本，而非完全依赖二手摘要；
- 重要传播关系有来源可查。

## 9.2 stage_freeze

达到以下状态即可冻结，不要求“研究完世界上所有材料”：

- 核心边界稳定；
- 主要文本见证和转折已覆盖；
- 关键 QC2 映射已建立；
- 主要不确定性已明确标注；
- 已足以服务当前阅读需求。

## 9.3 reopen gate

只有出现以下情况才重开：

- 新阅读产生明确知识缺口；
- 获得改变现有谱系的重要材料；
- 发现错误关系或证据等级需修正；
- 新作品反复需要同一尚未建模的传统分支；
- 当前专题结构已阻碍检索或理解。

---

# 10. 跨层关系建议

QC1 常用关系优先采用：

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

关系名用于数据层时应保持稳定；Markdown 正文可以使用自然语言。

涉及传播、继承、借用的关系必须同时记录证据等级和来源。

---

# 11. 与其他轴的边界

| 问题 | 主要去向 |
|---|---|
| 故事从何而来、有哪些文本版本？ | QC1 |
| 某个叙事组件如何跨故事重复？ | QC2 |
| 某文化角色世界如何被历史制度塑造？ | QC3 |
| 作品讨论什么抽象问题？ | QH |
| 某种文学类型如何形成并运作？ | QT |
| 某地区文学历史如何发展？ | R |
| 某时期文学发生了什么？ | T |
| 某一具体文本／作品本身 | 40 作品 |

---

# 12. 当前建设策略

1. **冻结 QC1.1 的 11 个一级来源 hubs**，暂不为了全球覆盖继续扩表；
2. 不重建现有 QC1.1 专题包，而在实际使用中逐个升级到新解释结构；
3. QC1.2 先保持只有根节点和候选池；
4. 选择一个真正有阅读价值的对象建立第一个 QC1.2 样板；
5. 样板验证后再决定是否需要 QC1.2 子分类，不预设按文明或对象类型再分一层；
6. QC1.1 与 QC1.2 均以网络关系连接 QC2，不追求目录树表达全部知识。

当前最重要的成功标准不是节点数量，而是是否能够形成如下可解释链路：

```text
作品中的具体调用
↕
QC2 组件
↕
QC1.2 具体叙事传统
↕
QC1.1 来源传统
↕
可核查文本与证据
```
