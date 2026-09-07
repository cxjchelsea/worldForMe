---
id: WL-QC1.2.3
type: literature_node
name: 亚瑟王叙事传统
code: QC1.2.3
axis: Q
parent: WL-QC1.2
level: 5
coverage_priority: Core
node_kind: taxonomy_leaf
anchorable: true
resource_type: figure_tradition
status: ACTIVE
build_stage: stage_frozen
---
# QC1.2.3 亚瑟王叙事传统

QC1.2 的第一个 `figure_tradition` 冻结样板。

本专题研究的不是“亚瑟王故事全集”，也不是一般性的骑士文学，而是：

> **亚瑟这一命名中心人物如何从早期不列颠材料与编年史人物，逐步成为一个可以容纳圆桌骑士、梅林、兰斯洛特、圣杯、特里斯坦、莫德雷德等子传统的跨文本叙事中心？**

## 核心模型

```text
亚瑟 central_figure
      ↓
王权／王廷 world framework
      ↓
人物网络 figure_network
      ↓
梅林、兰斯洛特、高文、珀西瓦尔／加拉哈德、特里斯坦、莫德雷德……
      ↓
子传统 subtraditions
      ↓
编年史 → 宫廷 romance → 法语散文循环 → 英语集成 → 现代重写
```

## 已冻结的 figure_tradition 能力

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

## 与 narrative_cycle 的差异

QC1.2.1、QC1.2.2 可以较强地通过故事区段、版本与分支组织；QC1.2.3 证明：

- 中心人物不必在每部作品中承担主角功能；
- 传统可以通过“人物网络 + 共同王廷世界”保持同一性；
- 子传统可以高度独立又继续挂接亚瑟王廷；
- chronology 只是辅助，人物网络和文本吸附能力可能成为更强骨架；
- 大型文本循环需要 `cycle_witness → component_witness` 两级表达。

## 当前核心文本阶段

```text
早期不列颠材料
→ 《不列颠诸王史》
→ Wace《布鲁特传奇》
→ Chrétien de Troyes 宫廷传奇
→ Lancelot-Grail / Vulgate Cycle
→ Post-Vulgate / Prose Tristan
→ 《亚瑟王之死》
→ T. H. White《The Once and Future King》
```

## 当前中央作品锚点

1. 《不列颠诸王史》——连贯亚瑟王者传记与编年史定型；
2. Wace《布鲁特传奇》——法语俗语化与圆桌概念的重要早期见证；
3. Chrétien de Troyes《兰斯洛特：大车骑士》——兰斯洛特子传统关键早期定型；
4. Chrétien de Troyes《佩尔西瓦尔或圣杯故事》——佩尔西瓦尔／圣杯子传统关键起点；
5. 《亚瑟王之死》——中古英语晚期大型集成；
6. T. H. White《The Once and Future King》——20世纪现代人物功能再发明锚点。

作品数量不是冻结标准；大型 cycle 与内部文本继续按 witness 粒度管理。

## Vulgate 两级 witness

```text
Lancelot-Grail / Vulgate Cycle
│
├─ Estoire del Saint Graal
├─ Estoire de Merlin
├─ Lancelot Proper
├─ Queste del Saint Graal
└─ Mort Artu
```

整个循环作为 `cycle_witness`，五个组成文本作为 `component_witness`。

## 子传统自治等级

```text
embedded
semi_independent
independent_candidate
```

代表性判断：

- Merlin：embedded / semi_independent 观察；
- Lancelot：semi_independent；
- Grail tradition：independent_candidate；
- Tristan–Iseult：independent_candidate。

## 专题产品

→ [[../../30 专题/QC1.2.3 亚瑟王叙事传统/00 亚瑟王叙事传统|QC1.2.3 亚瑟王叙事传统专题主页]]

准入记录：[[QC1.2.3 亚瑟王叙事传统 Source Readiness Review]]  
覆盖审查：[[../../30 专题/QC1.2.3 亚瑟王叙事传统/QC1.2.3 Coverage Review V1|QC1.2.3 Coverage Review V1]]  
冻结模板：[[QC1.2 figure_tradition 专题模板 V1]]  
冻结记录：[[QC1.2 figure_tradition Stage Freeze Review V1]]

## 当前状态

`STAGE_FROZEN`

QC1.2.3 已完成首个 `figure_tradition` 的完整验证。后续只在新阅读、重要新材料、证据修正或人物网络结构性缺口出现时 reopen，不再为了覆盖所有圆桌人物与现代改编机械扩充。
