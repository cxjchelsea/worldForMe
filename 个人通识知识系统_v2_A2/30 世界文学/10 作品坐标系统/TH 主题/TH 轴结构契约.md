---
id: WL-TH-CONTRACT
type: literature_axis_contract
axis: TH
status: frozen
version: TH-contract-v2
aligned_with:
  - T
  - R
  - M
---

# TH 轴结构契约

## 目标

TH 与 T / R / M 使用同一套作品坐标轴公共契约。统一的是**轴、坐标节点、专题主页、专题知识节点、结构 Base、作品 Base 的公共接口**；各专题仍可保留与自身问题结构相匹配的内部目录。

## 1. 轴根节点契约

TH 根节点使用：

```yaml
type: literature_axis
role: primary
coordinate_field: axis_th
priority_scheme:
  core: "★"
  important: "◆"
  extension: "△"
node_model: "group → leaf → topic map"
```

轴根节点只负责：坐标用途、节点树、公共规则、跨轴边界与治理入口；不直接挂专题内容。

## 2. 坐标节点契约

所有 TH 坐标节点至少具有：

```yaml
type: literature_node
axis: TH
system_role: work_coordinate
importance: Core
node_kind: taxonomy_group | taxonomy_leaf
anchorable: true | false
topic_map: null | "[[...]]"
```

规则：

- group 不直接挂专题，`anchorable: false`；
- leaf 可作为作品坐标并挂专题，`anchorable: true`；
- 专题内部问题不升级为新的 `axis_th`，除非重新通过坐标级压力测试。

## 3. 专题主页契约

所有 TH 叶专题主页统一使用：

```yaml
type: literature_topic_map
primary_anchor: WL-TH...
anchor_mode: leaf
topic_role: direct
structure_status: frozen | developing
work_database: "[[03 ...作品.base]]"
structure_database: "[[02 ...结构.base]]"
priority_scheme:
  core: "★"
  important: "◆"
  extension: "△"
```

主页正文至少承担：

1. 专题定位；
2. 核心问题；
3. Canvas / 结构 Base / 作品 Base 入口；
4. 内部结构入口；
5. 与相邻 TH / TY / IM / CN / M 的边界；
6. 阅读路线或作品语料说明；
7. 数据职责。

## 4. 专题知识节点契约

进入 `02 ...结构.base` 的知识节点统一采用：

```yaml
id: ...
type: literature_topic_structure | literature_topic_section
topic_id: WL-TOPIC-...
parent: ...
dimension: ...
sequence: 1
history_position: ... # 可选
```

推荐维度代码：

- `definition`：定义与边界；
- `core_problem`：核心问题；
- `mechanism`：作用机制；
- `comparison`：跨轴 / 跨传统比较；
- `reading_route`：阅读路线；
- `review`：压力测试、终审、冻结说明；
- 专题可以增加自己的专属 dimension，但不得替代上述公共语义。

## 5. 结构 Base 契约

结构 Base 必须：

- 以稳定 `topic_id` 聚合知识节点，而不是只依赖文件路径；
- 至少展示 `file.name / type / dimension / sequence / parent / id`；
- 至少提供“全部知识节点”“核心结构”“核心问题”三个视图；
- 专题自有旧结构可保留为额外视图，不破坏公共视图。

## 6. 作品 Base 契约

作品 Base 必须：

- 从 `40 作品/` 按稳定 topic ID 动态投影；
- 使用专题自己的 priority 字段，但统一语义：`★ 核心 / ◆ 重点 / △ 扩展`；
- 至少提供：核心、重点、扩展、已读、未读、全部作品；
- 能展示 T / R / M / G / TH 交叉坐标；
- 专题已有旧字段可以兼容保留，不为格式统一做破坏性改名。

## 7. 作品字段契约

TH 不强制所有专题使用同一个字段前缀，但字段语义统一为：

```text
<topic>_priority   → ★ / ◆ / △
<topic>_role       → 骨架 / 比较 / 边界 / 扩展等
<topic>_problems 或 <topic>_dimensions
<topic>_note
```

旧稳定字段（如 `war_*`、`memory_*`）继续保留；新的治理字段与旧字段并存时，由专题主页说明职责。

## 8. Canvas 契约

Canvas 只可视化仓库中已经存在且有文件支撑的结构关系，不承担唯一知识来源。所有 Canvas 关系必须能回落到专题主页、结构节点或作品实体。

## 9. 内部目录原则

统一公共入口：

```text
00 专题主页
01 Canvas
02 结构.base
03 作品.base
```

其后目录按专题内容决定，例如：

```text
10 核心结构/
11 核心问题/
12 历史层/
13 比较层/
```

不要求所有专题拥有相同的 `10/11/12/13` 内容；**结构一致性来自 frontmatter 与 Base contract，而不是来自机械复制文件夹名称。**

## 10. 冻结原则

TH 的分类结构已经冻结，但格式契约允许持续校准。后续新增或修改专题时，先满足本 contract，再增加专题特有结构。
