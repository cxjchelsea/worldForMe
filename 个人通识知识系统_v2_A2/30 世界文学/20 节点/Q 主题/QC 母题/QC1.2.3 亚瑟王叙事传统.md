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
build_stage: topic_build
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

## 当前重点文本锚点

- 《不列颠诸王史》——连贯亚瑟传记与编年史定型；
- Chrétien de Troyes 的亚瑟宫廷 romances——骑士人物与宫廷叙事扩张；
- Lancelot-Grail / Vulgate Cycle——人物网络与散文循环世界化；
- Post-Vulgate / Prose Tristan——重组和子传统吸附；
- 《亚瑟王之死》——英语晚期大型集成；
- 近现代重大重写——后续按实际阅读加入。

## 本专题要验证的 figure_tradition 能力

1. `central_figure`；
2. `figure_network`；
3. `subtradition`；
4. `court_or_world_framework`；
5. 人物与子传统的升格／拆分门槛；
6. 多语言文本阶段与人物功能变化；
7. 中心人物“在场但非主角”的传统归属。

## 专题产品

→ [[../../30 专题/QC1.2.3 亚瑟王叙事传统/00 亚瑟王叙事传统|QC1.2.3 亚瑟王叙事传统专题主页]]

准入记录：[[QC1.2.3 亚瑟王叙事传统 Source Readiness Review]]

## 当前状态

`TOPIC_BUILD`

下一阶段：建立第一个 `figure_tradition` 专题包，重点观察“中心人物—人物网络—子传统—文本阶段”是否需要区别于已冻结 `narrative_cycle` V1 的物理职责。
