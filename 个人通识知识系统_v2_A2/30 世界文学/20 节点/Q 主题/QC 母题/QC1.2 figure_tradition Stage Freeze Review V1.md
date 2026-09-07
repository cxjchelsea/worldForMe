---
id: WL-QC12-FIGURE-STAGE-FREEZE-V1
type: literature_governance_review
scope: QC1.2
resource_type: figure_tradition
status: PASS_STAGE_FROZEN
version: "1.0"
validated_topic: WL-QC1.2.3
---
# QC1.2 figure_tradition Stage Freeze Review V1

## 结论

`PASS_STAGE_FROZEN`

QC1.2.3 亚瑟王叙事传统已经完成从候选、source readiness、正式准入、topic build、coverage review 到补丁修复的完整流程。

两个冻结前补丁均已完成：

1. Lancelot-Grail / Vulgate Cycle 已明确拆成 `cycle_witness → component_witness` 两级；
2. T. H. White *The Once and Future King* 已接入中央作品库，承担 `modern_figure_reinvention`。

因此，可以冻结：

> [[QC1.2 figure_tradition 专题模板 V1]]

同时将 [[QC1.2.3 亚瑟王叙事传统]] 标记为 `STAGE_FROZEN`。

---

# 1. 冻结检查

| 条件 | 结果 |
|---|---|
| 中心人物边界稳定 | PASS |
| 共享王廷／世界框架稳定 | PASS |
| 主要人物网络建立 | PASS |
| 强子传统及自治程度可表达 | PASS |
| 关键文本阶段覆盖 | PASS |
| work / cycle_witness / component_witness 分层 | PASS |
| 现代人物功能再发明锚点 | PASS |
| QC2 接口 | PASS |
| 证据纪律 | PASS |
| 足以服务当前阅读 | PASS |

---

# 2. 亚瑟样板真正验证出的结构

核心不是固定故事序列，而是：

```text
Arthur
→ Arthurian court / Round Table world
→ figure network
→ subtraditions
→ textual cycles / integrations
→ modern reinvention
```

这说明 `figure_tradition` 与 `narrative_cycle` 虽然共享 QC1.2 的宏观任务，但中层知识组织机制不同。

---

# 3. Vulgate 补丁为什么足以通过

Vulgate Cycle 当前明确建模为：

```text
cycle_witness: Lancelot-Grail / Vulgate Cycle
│
├─ component_witness: Estoire del Saint Graal
├─ component_witness: Estoire de Merlin
├─ component_witness: Lancelot Proper
├─ component_witness: Queste del Saint Graal
└─ component_witness: Mort Artu
```

这解决了原先“一个大型循环既不是普通作品、又不能只写在正文里”的粒度问题。

同时，它进一步验证：

```text
figure_tradition
≠ cycle_witness
≠ component_witness
≠ work
```

---

# 4. 现代锚点为什么选择 T. H. White

*The Once and Future King* 的价值不只是时间晚，而是它重新解释 Arthur 的人物功能。

在专题中，它作为：

```text
modern_figure_reinvention
```

用于观察亚瑟如何从中世纪王者／骑士世界中心，转化为现代关于教育、暴力、理想主义、权力与政治失败的思想人物。

这满足 `figure_tradition` 对“人物功能史”的最低验证要求。

---

# 5. 冻结的稳定能力

正式冻结：

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

其中 `subtradition_status` V1 使用：

```text
embedded
semi_independent
independent_candidate
```

这是一套工作型等级，不是假装存在绝对清晰的本体边界。

---

# 6. 不冻结的部分

以下暂不升格为 QC1.2 全局强制模型：

- 全局人物实体库；
- 所有人物关系的统一 ontology；
- 所有大型 cycle 的统一 component schema；
- 所有后世接受作品的完整列表；
- story_tradition / collection_tradition 的模板。

原因：只有亚瑟样板验证了 figure_tradition；不能据此替其他资源类型预设答案。

---

# 7. QC1.2 当前模板状态

```text
narrative_cycle
→ FROZEN_V1
→ validated by QC1.2.1 + QC1.2.2

figure_tradition
→ FROZEN_V1
→ validated by QC1.2.3

story_tradition
→ NOT_FROZEN

collection_tradition
→ NOT_FROZEN
```

---

# 8. 下一步

不应继续用第四个 `figure_tradition` 立即验证同一模板。

下一异质样板优先：

```text
collection_tradition
→ 《一千零一夜》故事集合与传播传统
```

或：

```text
story_tradition
→ 莱拉与马杰农 / 白蛇 / 特里斯坦与伊索尔德
```

优先级上建议先做 `collection_tradition`，因为它最可能迫使 QC1.2 引入新的“编纂—抄本—翻译—故事增删—框架叙事”能力，对现有模板的反例价值最高。
