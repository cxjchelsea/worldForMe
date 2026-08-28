# QC2｜母题型专题模板 V0

> 对象类型：`motif`
>
> 状态：`V0_REVISED_AFTER_FLOOD_PILOT_PASS_B`
>
> 前置治理：[[QC2｜世界文化母题、原型与叙事结构模板总则 V0]]

---

# 00｜对象主页

至少回答：

1. 这个 motif 是什么？
2. 它与 theme / plot_pattern / archetype 有什么区别？
3. 它出现在哪些 QC1.1 来源传统？
4. 哪些文本构成较早见证与关键定型？
5. 它有哪些必选不变量与高频可选槽位？
6. 它如何与其他 motif / archetype / symbol 组合？
7. 后世有哪些明确重写？

建议 frontmatter：

```yaml
type: qc2_component
component_type: motif
name: ""
primary_clusters: []
secondary_clusters: []
status: PILOT
source_status: {}
required_invariants: []
optional_slots: []
```

`source_status` 用于防止 QC2 把尚未完成的 QC1.1 来源研究伪装成已建档来源。建议值：

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

---

# 01｜定义、边界与准入

## 工作性定义

一句话说明这个 motif 的最低辨识条件。

## required_invariants｜必选不变量

必须列出“缺少后就不再属于本 motif”的最小条件。

例如洪水 Pilot：

```text
大规模洪水破坏旧秩序
+
选择性幸存／保存
+
灾后进入新秩序阶段
```

## optional_slots｜高频可选槽位

记录经常出现但并非所有实例都必须具有的结构槽位，例如：

```text
预警
保存媒介
祭祀
盟约
再生方式
```

治理：

```text
required_invariants
≠ optional_slots
≠ ordered plot slots
```

## 排除项

明确列出最容易混淆的近邻对象。

---

# 02｜来源谱系

按 QC1.1 来源传统组织，不按现代国家组织。

建议表：

| 来源传统 | 来源故事／人物 | 早期文本见证 | source_status |
|---|---|---|---|

必须允许：

- 多中心起源；
- 独立同构；
- 可能传播；
- 来源专题尚未建设；
- 已有 QC1.1 专题但具体故事尚未索引；
- 无法判断。

禁止因为多个文明都有同类 motif 就强行寻找单一起源。

---

# 03｜内部结构与核心变体

母题专题重点是“同一个基本叙事单元如何变化”。

至少记录：

- `required_invariants`；
- `optional_slots`；
- 可变角色；
- 可变因果；
- 可变结局；
- 与其他 motif 的组合方式。

如果某一组槽位形成稳定顺序，应作为 `plot_pattern` 候选，而不是继续塞进 motif 定义。

---

# 04｜跨传统分布

不是做“全球都有这个故事”的罗列，而要判断不同实例属于：

- 高结构同构；
- 部分共享结构；
- 仅表面相似；
- 有历史传播证据；
- 来源关系未知。

分布矩阵应优先比较 `required_invariants + optional_slots`，不要只比较关键词。

治理底线：

```text
cross_tradition_distribution
≠ transmission_history
```

---

# 05｜文本证据与定型

至少分：

```text
early_witness
defining_text
defining_reworking
later_reworking
recommended_reading
```

每个文本只记录它如何参与该 motif 的形成、定型或改写。

同时区分：

```text
故事传统形成时间
≠ 文学版本形成时间
≠ 现存抄本／泥版年代
```

---

# 06｜传播、借用与结构相似

使用共享治理：

```text
relation_type
+
evidence_level
```

Flood Pilot Pass B 新增规则：

> **一条 relation record 只表达一种 relation_type，并配一个 evidence_level。**

若 A 与 B 同时“结构相似”且“可能存在历史传播”，应拆成两条关系：

```yaml
source: A
target: B
relation_type: structural_similarity
evidence_level: documented

source: A
target: B
relation_type: historical_transmission
evidence_level: possible
```

不得写成：

```text
structural_similarity + possible historical transmission
```

这种混合字段。

---

# 07｜与其他 QC2 对象关系

母题不会孤立存在。

至少记录：

- `co_occurs_with_motif`
- `carried_by_archetype`
- `organized_by_plot_pattern`
- `represented_by_symbol`
- `inverted_by_motif`

---

# 08｜后世重写与文化化

区分：

- direct_adaptation
- explicit_reference
- structural_inheritance
- motif_inversion
- hybridization

不要把所有“类似故事”都列进来。

---

# 09｜作品实例与跨媒介使用

只选能证明该 motif 被稳定调用、反转或重组的代表作品。

建议记录：

```yaml
work: ...
source_component: ...
retained_invariants: []
modified_slots: []
relation_type: ...
evidence_level: ...
source_evidence: ...
```

不因为作品里出现同一物件、灾难或人物类型就自动判定为母题继承。

---

# 10｜阅读与研究

至少提供：

- 最小来源文本路线；
- 跨传统比较路线；
- 后世重写路线；
- 现代研究入口；
- 模板执行反馈：KEEP / REVISE / ADD / REMOVE。

---

# 母题型完成判定

- [ ] 可给出最小 motif 定义
- [ ] `required_invariants` 已明确
- [ ] `optional_slots` 已明确
- [ ] 与 theme / plot_pattern 区分清楚
- [ ] 至少两个来源实例已核证，或明确说明单来源状态
- [ ] 每个来源具有 `source_status`
- [ ] 主要变体已识别
- [ ] 来源与定型文本已分层
- [ ] 传播与结构相似已分离
- [ ] relation record 遵守“一条关系一种 relation_type”
- [ ] 至少建立一个 archetype / plot_pattern / symbol 关系
- [ ] 后世实例有明确关系类型与证据等级
