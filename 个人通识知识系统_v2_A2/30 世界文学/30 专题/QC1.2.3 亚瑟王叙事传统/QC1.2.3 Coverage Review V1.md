---
id: WL-QC123-COVERAGE-REVIEW-V1
type: literature_review
scope: QC1.2.3
resource_type: figure_tradition
status: PASS_WITH_PATCH
version: "1.0"
---
# QC1.2.3 Coverage Review V1

## 结论

`PASS_WITH_PATCH`

QC1.2.3 已经足以证明 `figure_tradition` 与已冻结的 `narrative_cycle` 在组织逻辑上存在稳定差异：其核心不是单一故事顺序，而是**中心人物 + 共享世界框架 + 人物网络 + 子传统**。

当前专题已具备进入下一轮模板验证的条件，但暂不 stage freeze。冻结前仍需补两个方面：

1. 让 Lancelot-Grail / Vulgate Cycle 在专题中拥有更明确的 `cycle_witness` 结构位置；
2. 至少补一个近现代重大再发明锚点，用来测试 figure_tradition 的长期人物功能变化。

---

# 1. 中心人物模型检查

## PASS

亚瑟并不需要在每部文本中都是主角，仍然可以维持整个传统的组织中心。

推荐冻结候选能力：

```text
central_figure
court_or_world_framework
figure_network
subtradition
```

这四项共同解释了为什么兰斯洛特、梅林、圣杯骑士、特里斯坦等高度自治的故事仍能继续属于亚瑟传统。

---

# 2. 文本阶段覆盖

当前已形成最低阶段链：

```text
早期不列颠材料
→ 《不列颠诸王史》
→ Wace《Roman de Brut》
→ Chrétien de Troyes 宫廷传奇
→ Lancelot-Grail / Vulgate Cycle
→ Post-Vulgate / Prose Tristan
→ Malory《Le Morte Darthur》
```

其中中央作品锚点当前已有：

- 《不列颠诸王史》；
- 《布鲁特传奇》；
- 《兰斯洛特：大车骑士》；
- 《佩尔西瓦尔或圣杯故事》；
- 《亚瑟王之死》。

而 Lancelot-Grail、Post-Vulgate、Prose Tristan 暂以 `cycle_witness / story_witness` 保留，不强制伪装成单一 work。

判断：`PASS`。

---

# 3. 人物网络与子传统模型

## PASS

当前至少可稳定识别：

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

这一结构证明：

- `figure_network` 不是普通人物表；
- 网络成员可以拥有不同自治程度；
- 子传统是否升格独立 QC1.2，需要单独判断其历时生命和文本谱系。

建议保留三档：

```text
embedded
semi_independent
independent_candidate
```

当前：

- Merlin：embedded / semi_independent 观察；
- Lancelot：semi_independent；
- Grail tradition：independent_candidate；
- Tristan–Iseult：independent_candidate。

---

# 4. `figure_tradition` 与 `narrative_cycle` 的结构差异

## 已验证差异

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
→ 后世人物功能再发明
```

因此，当前不建议直接把 `QC1.2 narrative_cycle 专题模板 V1` 原样提升为所有 QC1.2 的通用模板。

---

# 5. Figure-network 是否应正式成为数据能力

## PASS

判断：应成为 `figure_tradition` 的候选正式能力。

理由：

1. 亚瑟传统的同一性部分依赖人物围绕王廷世界的持续聚合；
2. 兰斯洛特、梅林、珀西瓦尔等人物在部分文本中比亚瑟本人更具行动中心性；
3. 仅用 chronology 或 branch 无法表达这种关系；
4. 子传统升格边界本身就是检索与理解需求。

未来 Base 可考虑稳定字段：

```yaml
central_figure:
figure_role:
network_role:
subtradition_status:
world_framework:
text_stage:
```

当前仍不单独建立全局人物实体库，先在 QC1.2.3 内验证。

---

# 6. 作品与 witness 粒度

## PASS

本专题进一步验证：

```text
work ≠ cycle_witness ≠ story_witness ≠ figure_tradition
```

例如：

- Chrétien 的《兰斯洛特：大车骑士》是中央 work；
- Lancelot-Grail 是大型 `cycle_witness`；
- 其内部 Queste del Saint Graal、Mort Artu 等可以继续作为更细 witness；
- 整体亚瑟王传统仍是 `figure_tradition`。

因此，不应为了让 Works Base 看起来“书很多”而把大型文本循环粗暴压成一本书。

---

# 7. 当前补丁

## PATCH A：Vulgate Cycle 结构化

当前已有文本说明，但下一轮应明确记录它的内部五部分及其在 figure network 中的功能，以测试 `cycle_witness` 是否需要可查询字段。

## PATCH B：近现代再发明锚点

至少选择一个真正改变“Arthur 作为何种人物”的近现代作品，而不是仅增加普通改编书目。

候选可在真实阅读需求出现后从 T. H. White、Tennyson 等重大重写中选择。

---

# 8. 当前冻结判定

| 条件 | 状态 |
|---|---|
| 中心人物边界稳定 | PASS |
| 主要文本阶段覆盖 | PASS |
| 人物网络建立 | PASS |
| 子传统边界可表达 | PASS |
| work / witness 分层 | PASS |
| 近现代人物功能变化 | PATCH |
| figure_tradition 模板稳定 | 尚需第二轮 |

## 最终判断

```text
QC1.2.3 = COVERAGE_REVIEW_PASS_WITH_PATCH
```

下一阶段不是扩大作品数量，而是完成 Vulgate Cycle 结构化与一个现代再发明锚点，再判断是否可以冻结 `figure_tradition V1`。
