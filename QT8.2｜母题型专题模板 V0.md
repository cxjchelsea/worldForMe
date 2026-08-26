# QT8.2｜母题型专题模板 V0

> 对象类型：`motif`
>
> 前置治理：[[QT8.2｜世界文化母题、原型与叙事结构模板总则 V0]]

---

# 00｜对象主页

至少回答：

1. 这个 motif 是什么？
2. 它与 theme / plot_pattern / archetype 有什么区别？
3. 它出现在哪些 QT8.1 来源传统？
4. 哪些文本构成较早见证与关键定型？
5. 它有哪些主要结构变体？
6. 它如何与其他 motif / archetype / symbol 组合？
7. 后世有哪些明确重写？

建议 frontmatter：

```yaml
type: qt82_component
component_type: motif
name: ""
primary_clusters: []
secondary_clusters: []
status: PILOT
```

---

# 01｜定义、边界与准入

## 工作性定义

一句话说明这个 motif 的最低辨识条件。

## 准入规则

必须能够识别一个稳定的叙事单元或关系，而不是单纯的抽象概念。

例如：

```text
“兄弟相残” = motif
“嫉妒” = theme / emotion，通常不独立作为 motif
```

## 排除项

明确列出最容易混淆的近邻对象。

---

# 02｜来源谱系

按 QT8.1 来源传统组织，不按现代国家组织。

建议表：

| 来源传统 | 来源故事／人物 | 早期文本见证 | 关系状态 |
|---|---|---|---|

必须允许：

- 多中心起源；
- 独立同构；
- 可能传播；
- 无法判断。

禁止因为多个文明都有同类 motif 就强行寻找单一起源。

---

# 03｜内部结构与核心变体

母题专题的重点是“同一个基本叙事单元如何变化”。

至少记录：

- 核心不变量；
- 可变角色；
- 可变因果；
- 可变结局；
- 与其他 motif 的组合方式。

例如洪水 motif 可比较：

```text
灾变原因
幸存者选择机制
保存对象
灾后秩序
是否出现盟约／重建
```

---

# 04｜跨传统分布

不是做“全球都有这个故事”的罗列，而要判断不同实例属于：

- 高结构同构；
- 部分共享结构；
- 仅表面相似；
- 有历史传播证据；
- 来源关系未知。

必要时建立分布矩阵。

---

# 05｜文本证据与定型

至少分：

```text
early_witness
defining_text
later_reworking
recommended_reading
```

每个文本只记录它如何参与该 motif 的形成、定型或改写。

---

# 06｜传播、借用与结构相似

使用共享治理：

```text
relation_type
+
evidence_level
```

不得用“影响”覆盖所有关系。

---

# 07｜与其他 QT8.2 对象关系

母题不会孤立存在。

至少记录：

- `co_occurs_with_motif`
- `carried_by_archetype`
- `organized_by_plot_pattern`
- `represented_by_symbol`
- `inverted_by_motif`

例如：

```text
洪水与灾后重建 motif
├─ archetype：洪水幸存者／第二祖先
├─ plot_pattern：失序→毁灭→幸存→重建
└─ symbol：方舟（特定传统中的高复用符号）
```

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

每个实例至少回答：

```text
来源 motif 是什么？
保留了什么？
修改了什么？
关系类型是什么？
证据等级是什么？
```

---

# 10｜阅读与研究

至少提供：

- 最小来源文本路线；
- 跨传统比较路线；
- 后世重写路线；
- 现代研究入口。

研究书目要说明用途，而不是堆书名。

---

# 母题型完成判定

- [ ] 可给出最小 motif 定义
- [ ] 与 theme / plot_pattern 区分清楚
- [ ] 至少两个来源实例已核证，或明确说明单来源状态
- [ ] 主要变体已识别
- [ ] 来源与定型文本已分层
- [ ] 传播与结构相似已分离
- [ ] 至少建立一个 archetype / plot_pattern / symbol 关系
- [ ] 后世实例有明确关系类型
