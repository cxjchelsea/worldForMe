---
id: WL-QT
type: literature_node
name: "类型与叙事机制"
code: QT
axis: QT
system_role: work_coordinate
coordinate_field: axis_qt
legacy_parent: WL-Q
parent: WL-COORDINATES
level: 1
node_kind: coordinate_group
anchorable: false
topic_map: null
source_version: "3.0-coordinate-network"
---

# QT 类型与叙事机制

> 新路径：世界文学 → 作品坐标系统 → **QT 类型与叙事机制**。物理目录 `20 节点/Q 主题/` 仅为兼容旧 WikiLink 保留。

QT 是作品坐标，不再被定义为 Q 轴 facet。它回答：**作品采用什么类型契约、叙事机制或稳定类型传统？**

一部作品可以同时拥有多个 QT；canonical 作品字段为 `axis_qt`。迁移期旧 `axis_q` 中的 QT 值仍可作为 fallback 读取。

## 当前骨架

```text
QT  类型与叙事机制
├─ QT1 推理与犯罪叙事
├─ QT2 科幻
├─ QT3 奇幻
├─ QT4 恐怖与哥特
├─ QT5 冒险与探索叙事
├─ QT6 乌托邦、反乌托邦与社会想象
├─ QT7 历史叙事
├─ QT8 世界文化母题、原型与叙事传统   ← legacy compatibility branch / FROZEN
├─ QT10 惊悚与悬疑叙事
├─ QT11 爱情与浪漫叙事
├─ QT12 灾变、末世与后末日叙事
├─ QT13 讽刺叙事
└─ QT14 旅行与游记
```

## QT8 兼容冻结

QT8 及其部分子树来自旧“类型 + 文化传统”混合设计。随着 QC3 文化模型机制成立，它已出现明显职责重叠。

本轮处理：

1. 保留现有 QT8 编号、文件和专题路径，避免破坏 WikiLink；
2. 不继续在 QT8 下新增文化角色 / 社会秩序类 taxonomy；
3. 新的历史化文化模型进入 QC3；
4. 已有作品的 QT8.* 不做无证据批量删除，后续在主动校准时判断：
   - 真正属于类型契约 / 叙事机制的部分留在 QT；
   - 属于文化角色、关系、伦理、秩序模型的部分迁移为 QC3 关系；
5. 结构相似只可建立 `structural_similarity`，不能自动断言直接来源。

这意味着 QT8 是**兼容遗留分支**，不是未来 QT 的设计样板。

## 子节点

- [[QT1 推理与犯罪叙事]]
- [[QT2 科幻]]
- [[QT3 奇幻]]
- [[QT4 恐怖与哥特]]
- [[QT5 冒险与探索叙事]]
- [[QT6 乌托邦、反乌托邦与社会想象]]
- [[QT7 历史叙事]]
- [[QT8 世界文化母题、原型与叙事传统]]（兼容冻结）
- [[QT10 惊悚与悬疑叙事]]
- [[QT11 爱情与浪漫叙事]]
- [[QT12 灾变、末世与后末日叙事]]
- [[QT13 讽刺叙事]]
- [[QT14 旅行与游记]]

## 与其他系统的边界

- “采用什么类型机制” → QT；
- “思考什么问题” → QH；
- “具体意象如何工作” → QX；
- “继承、重写、批判了什么长期叙事传统 / 文化模型” → QC。

## 返回

- [[../../../04 系统架构/01 作品坐标系统|作品坐标系统]]
- [[../../../00 世界文学使用规则|世界文学使用规则]]
