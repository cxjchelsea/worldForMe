---
id: WL-QC123-COVERAGE-REVIEW-V1
type: literature_review
scope: QC1.2.3
resource_type: figure_tradition
status: PASS
version: "1.1"
---
# QC1.2.3 Coverage Review V1

## 结论

`PASS / STAGE_FROZEN`

QC1.2.3 已经完成两个原冻结前补丁：

1. Lancelot-Grail / Vulgate Cycle 已结构化为 `cycle_witness → component_witness`；
2. T. H. White *The Once and Future King* 已作为现代人物功能再发明锚点接入中央作品库。

因此本专题不再处于 `PASS_WITH_PATCH`，而达到 stage-freeze 条件。

正式冻结记录：[[../../20 节点/Q 主题/QC 母题/QC1.2 figure_tradition Stage Freeze Review V1|QC1.2 figure_tradition Stage Freeze Review V1]]  
冻结模板：[[../../20 节点/Q 主题/QC 母题/QC1.2 figure_tradition 专题模板 V1|QC1.2 figure_tradition 专题模板 V1]]

---

# 1. 中心人物模型

## PASS

亚瑟无需在每部文本中都是主角，仍可以通过王廷／圆桌世界维持传统中心。

稳定能力：

```text
central_figure
court_or_world_framework
figure_network
subtradition
```

---

# 2. 主要文本阶段覆盖

## PASS

当前最低阶段链：

```text
早期不列颠材料
→ 《不列颠诸王史》
→ Wace《Roman de Brut》
→ Chrétien de Troyes 宫廷传奇
→ Lancelot-Grail / Vulgate Cycle
→ Post-Vulgate / Prose Tristan
→ Malory《Le Morte Darthur》
→ T. H. White《The Once and Future King》
```

中央作品锚点当前至少包括：

- 《不列颠诸王史》；
- 《布鲁特传奇》；
- 《兰斯洛特：大车骑士》；
- 《佩尔西瓦尔或圣杯故事》；
- 《亚瑟王之死》；
- *The Once and Future King*。

作品数量不是冻结标准；关键是阶段和功能位置被覆盖。

---

# 3. 人物网络与子传统

## PASS

当前稳定网络：

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

子传统 V1 三档：

```text
embedded
semi_independent
independent_candidate
```

当前代表性判断：

- Merlin：embedded / semi_independent 观察；
- Lancelot：semi_independent；
- Grail tradition：independent_candidate；
- Tristan–Iseult：independent_candidate。

这些状态不是永久本体判断，而是用于决定是否触发独立 QC1.2 source readiness。

---

# 4. Vulgate Cycle 多层 witness

## PASS

当前正式结构：

```text
Lancelot-Grail / Vulgate Cycle
│
├─ Estoire del Saint Graal
├─ Estoire de Merlin
├─ Lancelot Proper
├─ Queste del Saint Graal
└─ Mort Artu
```

上层为 `cycle_witness`，五个组成文本为 `component_witness`。

这一结构解决了大型散文循环既不应被压成一本中央 work、又必须可细粒度分析的问题。

---

# 5. 现代人物功能变化

## PASS

T. H. White *The Once and Future King* 作为 `modern_figure_reinvention`，用于观察 Arthur 从中世纪王权／骑士世界中心向现代政治、教育、战争和理想主义问题人物的转换。

这证明 figure_tradition 的“后世生命”不能只记录题材被继续使用，还应记录：

```text
figure_function_change
```

---

# 6. figure_tradition 与 narrative_cycle 的稳定差异

## PASS

`narrative_cycle` 更容易围绕：

```text
核心叙事材料
→ 文本见证
→ 版本／分支
→ 人物与事件变体
```

`figure_tradition` 更适合：

```text
中心人物
→ 共享世界框架
→ 人物网络
→ 子传统
→ 文本循环化／集成
→ 人物功能再发明
```

因此不能把 `narrative_cycle V1` 原样视为所有 QC1.2 的统一模板。

---

# 7. 冻结判定

| 条件 | 状态 |
|---|---|
| 中心人物边界稳定 | PASS |
| 共享世界框架稳定 | PASS |
| 人物网络建立 | PASS |
| 子传统边界可表达 | PASS |
| 主要文本阶段覆盖 | PASS |
| work / cycle / component witness 分层 | PASS |
| 近现代人物功能变化 | PASS |
| QC2 接口 | PASS |
| 证据纪律 | PASS |
| 足以服务当前阅读 | PASS |

## 最终判断

```text
QC1.2.3 = STAGE_FROZEN
QC1.2 figure_tradition = FROZEN_V1
```

后续新增亚瑟人物、作品和支线按真实阅读触发，不再为了“亚瑟王大全”机械扩充。
