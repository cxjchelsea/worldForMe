---
id: WL-CN12-NARRATIVE-CYCLE-TEMPLATE-V1
legacy_id: WL-QC12-NARRATIVE-CYCLE-TEMPLATE-V1
type: literature_governance_template
system_role: work_knowledge_network
scope: CN1.2
resource_type: narrative_cycle
status: FROZEN_V1
version: "1.0"
validated_by:
  - WL-CN1.2.1
  - WL-CN1.2.2
---
# CN1.2 narrative_cycle 专题模板 V1

> 本模板由 [[CN1.2.1 特洛伊故事循环]] 与 [[CN1.2.2 沃尔松—尼伯龙根叙事传统]] 两个结构差异明显的 `narrative_cycle` 样板共同验证。
>
> 它只冻结 `narrative_cycle` 的 V1 产品骨架，不代表 `figure_tradition`、`story_tradition`、`collection_tradition` 已经完成模板验证。

# 1. 核心目标

一个成熟的 `narrative_cycle` 专题应回答：

> **一个可识别的故事群如何在多个文本、版本、语言、地域、文类与历史环境中形成自己的长期叙事生命？**

重点不是复述一个“标准故事”，而是建立：

```text
核心叙事材料
→ 文本见证
→ 谱系／版本／分支
→ 人物与叙事结构变体
→ 后世重构
→ CN2 抽象接口
```

---

# 2. 冻结的物理产品壳

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

- `00–03` 的职责固定；
- `10–15` 的编号与认知职责固定；
- `10–15` 的实际文件夹标题允许按专题材料局部改名；
- 二级页面数量不固定，不为目录整齐机械扩写。

---

# 3. 六个稳定认知职责

## 10 定义、边界与核心叙事材料

至少回答：

- 这个循环是什么；
- 它不是什么；
- 叙事核包含哪些主要人物／事件／区段；
- 与相邻传统如何交叉但不混同。

## 11 早期材料与文本见证

至少回答：

- 最早可见材料在哪里；
- 现存文本、失传文本、手稿、诗群、编纂层分别是什么角色；
- 哪些是 `work`，哪些只是 `story_witness`；
- 现代完整叙述不能被当作早期传统原貌。

## 12 文本谱系、版本与分支

按实际材料选择 chronology、language、region、version、branch 等维度。

注意：

- chronology 是可用能力，不是唯一骨架；
- branch 是必须支持的能力，但不要求每个专题都有清晰树状分支；
- branch 不等于 geography，它可综合语言、文本环境、体裁、叙事组织和价值结构。

## 13 人物与叙事结构变体

记录：

- 人物在不同文本中的角色功能变化；
- 人物对应关系；
- 事件因果、关系、动机与结局的变体；
- 同一传统中的结构重组。

禁止把跨文本人物简单合并为“完全同一实体”。

## 14 后世生命与跨语言／文类／媒介重构

至少保留一个能证明传统被重大重新组织的后世锚点。

重点观察：

- 谁成为新的中心；
- 叙事终点是否改变；
- 政治／宗教／民族／性别／创伤等解释框架是否改变；
- 文类与媒介变化带来什么结构性重组。

不要求穷尽全部接受史。

## 15 CN2 组件、证据与阅读

负责：

- 将具体叙事材料映射到 CN2；
- 标记传播与谱系证据等级；
- 给出阅读入口与下一步问题；
- 防止 CN1.2 重复建设母题百科。

---

# 4. 四个产品文件的职责

## 00 主页

至少包含：

- 一句话定位；
- 核心边界；
- 主要叙事材料；
- 核心见证；
- 结构／作品 Base 嵌入；
- 阅读入口；
- 当前建设状态。

## 01 Canvas

用于关系导航，不用于制造历史确定性。

必须遵守：

- 不因时间先后自动画来源箭头；
- 不因情节相似自动画传播箭头；
- 未确定关系应通过说明节点或弱关系语义表达，而不是视觉上伪装成确定谱系。

## 02 结构／谱系 Base

使用语义字段组织专题页面，例如：

```yaml
structure_type_zh:
dimension:
sequence:
history_position:
```

禁止仅用 `file.folder` 充当知识模型。

## 03 作品／文本见证 Base

主要投影中央 `40 作品` 的 work 实体。

推荐局部字段：

```yaml
qc12x_priority:
qc12x_branch:
qc12x_tradition_stage:
qc12x_text_role:
qc12x_role:
```

具体英雄诗、手稿、失传作品摘要、版本层等非普通 work 见证可以在专题内建立 `story_witness`，不强制复制到中央作品库。

---

# 5. 作品池与 witness 覆盖原则

不设固定作品数量。

冻结关注的是结构位置是否被覆盖，而不是达到某个书目配额：

```text
核心早期见证
+ 主要文本化节点
+ 重要版本／分支
+ 必要桥接见证
+ 后世重大重构
```

一个成熟专题可以表现为：

```text
少量中央 work 锚点
+
更细粒度 story_witness
+
关系、版本、人物和 CN2 接口
```

因此“作品数”不是成熟度指标。

---

# 6. narrative_cycle 的证据纪律

冻结以下原则：

1. 叙事顺序 ≠ 文本年代；
2. 文本年代 ≠ 故事起源；
3. 文本年代先后 ≠ 直接来源；
4. 情节相似 ≠ direct transmission；
5. 人物对应 ≠ canonical identity；
6. 后世完整叙事 ≠ 早期传统透明原貌；
7. 失传文本的现代摘要 ≠ 完整现存作品；
8. `tradition ≠ story_witness ≠ work`；
9. Canvas 不得通过箭头暗示未经证实的传播；
10. 重要传播关系必须保留证据等级和不确定性。

---

# 7. 最低数据能力

按对象需要支持：

```yaml
resource_type: narrative_cycle
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

可选扩展：

```text
figure_correspondence
event_variant
manuscript_group
translation_branch
reception_cluster
```

这些扩展只有在真实检索需求出现时才升级为独立实体。

---

# 8. Stage Freeze 验收

满足以下条件即可 `stage_frozen`：

- 核心边界稳定；
- 主要文本见证与关键转折覆盖；
- 核心分支／版本关系足以支撑理解；
- 关键 CN2 映射已建立；
- 主要不确定性已明确标注；
- 00–03 与 10–15 产品接口稳定；
- 已足以服务当前阅读需求。

不要求：

- 穷尽所有版本；
- 穷尽所有现代改写；
- 达到固定作品数量；
- 建立没有实际需求的数据实体。

---

# 9. Reopen Gate

冻结后仅在以下情况重开：

- 新阅读产生明确知识缺口；
- 新材料改变现有谱系或关键分支判断；
- 发现错误传播关系或证据等级；
- 多个作品反复需要一个尚未建模的分支／人物／事件；
- 当前结构已经阻碍检索或理解。

普通新增参考书目不自动触发专题重开。

---

# 10. V1 的适用边界

本模板已验证：

- `CN1.2.1 特洛伊故事循环`
- `CN1.2.2 沃尔松—尼伯龙根叙事传统`

尚未验证：

- `figure_tradition`
- `story_tradition`
- `collection_tradition`

下一样板应优先选择不同资源类型。当前优先建议：亚瑟王叙事传统，用于验证 `figure_tradition` 是否需要改变六层职责或新增人物网络能力。

只有不同资源类型继续验证后，才判断本 V1 是否能升级为 CN1.2 全类型通用模板。