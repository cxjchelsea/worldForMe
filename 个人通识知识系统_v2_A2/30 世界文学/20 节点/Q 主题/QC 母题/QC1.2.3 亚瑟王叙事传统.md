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
build_stage: coverage_review_pass_with_patch
---
# QC1.2.3 亚瑟王叙事传统

QC1.2 的第一个 `figure_tradition` 验证样板。

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

## 与 narrative_cycle 的差异

QC1.2.1、QC1.2.2 可以较强地通过故事区段、版本与分支组织；QC1.2.3 则重点验证：

- 中心人物不必在每部作品中承担主角功能；
- 传统可以通过“人物网络 + 共同王廷世界”保持同一性；
- 子传统可以高度独立又继续挂接亚瑟王廷；
- chronology 只是辅助，人物网络和文本吸附能力可能成为更强骨架。

## 当前边界

### 纳入

- 亚瑟人物形象及王权叙事的长期变化；
- 亚瑟王廷作为共享叙事世界的形成；
- 与亚瑟传统有稳定文本关系的重要人物和子传统；
- 编年史、romance、散文循环、集成文本和后世重写中的结构变化。

### 不自动纳入

- 一般骑士文学；
- 所有圆桌骑士的全部作品；
- 仅共享“圣杯／魔剑／王权”等 QC2 组件的作品；
- 尚未证明具有独立历时生命的边缘人物。

## 当前作品锚点

当前中央作品锚点已有：

1. 《不列颠诸王史》——连贯亚瑟传记与编年史定型；
2. Wace《布鲁特传奇》——法语俗语化与圆桌概念的重要早期见证；
3. Chrétien de Troyes《兰斯洛特：大车骑士》——兰斯洛特子传统关键早期定型；
4. Chrétien de Troyes《佩尔西瓦尔或圣杯故事》——佩尔西瓦尔／圣杯子传统关键起点；
5. 《亚瑟王之死》——英语晚期大型集成。

大型文本循环继续按 witness 处理：

- Lancelot-Grail / Vulgate Cycle；
- Post-Vulgate；
- Prose Tristan。

## figure_tradition 第一轮验证结果

当前已初步验证以下能力：

1. `central_figure`；
2. `figure_network`；
3. `subtradition`；
4. `court_or_world_framework`；
5. 人物与子传统的升格／拆分门槛；
6. `work / cycle_witness / story_witness / figure_tradition` 粒度分层。

人物网络当前可稳定表达：

```text
Arthur
├─ Merlin
├─ Guinevere
├─ Lancelot
├─ Gawain
├─ Perceval / Galahad / Grail quest
├─ Tristan / Iseult
├─ Mordred
└─ Round Table / Camelot world framework
```

子传统状态候选：

```text
embedded
semi_independent
independent_candidate
```

当前判断：

- Merlin：embedded / semi_independent 观察；
- Lancelot：semi_independent；
- Grail tradition：independent_candidate；
- Tristan–Iseult：independent_candidate。

## 专题产品

→ [[../../30 专题/QC1.2.3 亚瑟王叙事传统/00 亚瑟王叙事传统|QC1.2.3 亚瑟王叙事传统专题主页]]

准入记录：[[QC1.2.3 亚瑟王叙事传统 Source Readiness Review]]

覆盖审查：[[../../30 专题/QC1.2.3 亚瑟王叙事传统/QC1.2.3 Coverage Review V1|QC1.2.3 Coverage Review V1]]

## 当前状态

`COVERAGE_REVIEW_PASS_WITH_PATCH`

当前不再为了数量扩大作品池。下一轮只处理两个结构性补丁：

1. 明确 Lancelot-Grail / Vulgate Cycle 的内部 `cycle_witness` 结构；
2. 补一个能显示近现代 Arthur 人物功能重新定义的重大重写锚点。

完成后再判断是否可以冻结 `figure_tradition V1`。
