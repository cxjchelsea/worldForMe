---
id: WL-TY
legacy_id: WL-QT
type: literature_node
name: "类型与叙事机制"
code: TY
legacy_code: QT
axis: TY
system_role: work_coordinate
coordinate_field: axis_ty
legacy_parent: WL-Q
parent: WL-COORDINATES
level: 1
node_kind: coordinate_group
anchorable: false
topic_map: null
source_version: "3.0-coordinate-network"
---

# TY 类型与叙事机制

> 新路径：世界文学 → 作品坐标系统 → **TY 类型与叙事机制**。物理目录 `20 节点/Q 主题/` 仅为兼容旧 WikiLink 保留。

TY 是作品坐标，不再被定义为 Q 轴 facet。它回答：**作品采用什么类型契约、叙事机制或稳定类型传统？**

一部作品可以同时拥有多个 TY；canonical 作品字段为 `axis_ty`。迁移期旧 `axis_q` 中的 TY 值仍可作为 fallback 读取。

## 当前骨架

```text
TY  类型与叙事机制
├─ TY1 推理与犯罪叙事
├─ TY2 科幻
├─ TY3 奇幻
├─ TY4 恐怖与哥特
├─ TY5 冒险与探索叙事
├─ TY6 乌托邦、反乌托邦与社会想象
├─ TY7 历史叙事
├─ TY8 世界文化母题、原型与叙事传统   ← legacy compatibility branch / FROZEN
├─ TY10 惊悚与悬疑叙事
├─ TY11 爱情与浪漫叙事
├─ TY12 灾变、末世与后末日叙事
├─ TY13 讽刺叙事
└─ TY14 旅行与游记
```

## TY8 兼容冻结

TY8 及其部分子树来自旧“类型 + 文化传统”混合设计。随着 CN3 文化模型机制成立，它已出现明显职责重叠。

本轮处理：

1. 保留现有 TY8 编号、文件和专题路径，避免破坏 WikiLink；
2. 不继续在 TY8 下新增文化角色 / 社会秩序类 taxonomy；
3. 新的历史化文化模型进入 CN3；
4. 已有作品的 TY8.* 不做无证据批量删除，后续在主动校准时判断：
   - 真正属于类型契约 / 叙事机制的部分留在 TY；
   - 属于文化角色、关系、伦理、秩序模型的部分迁移为 CN3 关系；
5. 结构相似只可建立 `structural_similarity`，不能自动断言直接来源。

这意味着 TY8 是**兼容遗留分支**，不是未来 TY 的设计样板。

## 子节点

- [[TY1 推理与犯罪叙事]]
- [[TY2 科幻]]
- [[TY3 奇幻]]
- [[TY4 恐怖与哥特]]
- [[TY5 冒险与探索叙事]]
- [[TY6 乌托邦、反乌托邦与社会想象]]
- [[TY7 历史叙事]]
- [[TY8 世界文化母题、原型与叙事传统]]（兼容冻结）
- [[TY10 惊悚与悬疑叙事]]
- [[TY11 爱情与浪漫叙事]]
- [[TY12 灾变、末世与后末日叙事]]
- [[TY13 讽刺叙事]]
- [[TY14 旅行与游记]]

## 与其他系统的边界

- “采用什么类型机制” → TY；
- “思考什么问题” → TH；
- “具体意象如何工作” → IM；
- “继承、重写、批判了什么长期叙事传统 / 文化模型” → CN。

## 返回

- [[../../../04 系统架构/01 作品坐标系统|作品坐标系统]]
- [[../../../00 世界文学使用规则|世界文学使用规则]]
