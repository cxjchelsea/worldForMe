---
id: WL-TOPIC-Q2-LOVE-LEGACY-MIGRATION
type: literature_topic_structure
topic_id: WL-TOPIC-Q2-LOVE
dimension: legacy_migration
sequence: 8
parent: WL-TOPIC-Q2-LOVE
status: frozen
---

# 旧 love_axes 迁移方案

## 原则

旧 `love_axes` 的十二横轴不是同一种分类：它混合了人类问题、关系阶段、社会条件、身份议题、文类标签和跨类型接口。因此不做“一一改名”，而采用**分流迁移**。

迁移只改变这些字段未来的解释方式，不在本次冻结中批量重写所有中央作品实体。

## 十二横轴的去向

| 旧横轴 | 新治理去向 | 说明 |
|---|---|---|
| 求偶 → 婚姻 | P1 / P3 / P5 + TH2.2 接口 | 求偶中的对象选择、回应与社会许可可进入 TH2.1；一旦中心转为婚姻制度与共同生活，转 TH2.2。 |
| 婚姻以后 | TH2.2 | 属于长期亲密关系、共同生活和婚姻协商，不再作为 TH2.1 内部轴。 |
| 禁忌爱情 | P5 | 当禁忌正在阻断一段具体爱欲关系时直接映射 P5。 |
| 无法实现 / 错过 | P3 / P7 | 无回应偏 P3；时间、距离与错过导致爱欲变形偏 P7。 |
| 爱情与阶级 | P5 | 阶级成为具体爱欲关系的许可边界时映射 P5；若主要讨论阶级社会本身，桥接 TH4。 |
| 爱与毁灭 | P4 / P6 / P7 | 可能来自占有与控制、主体自我取消，或失去/死亡后的转化，不能压成单一新轴。 |
| 欲望 / 身体 / 性 | TH2.1 与 TH3.2 分流 | 对具体他者的爱欲可进入 P1/P2/P3/P4；身体、性身份、性实践与规范本身优先 TH3.2。 |
| 爱情与女性主体 | P5 / P6 + TH1.1 / TH3.1 接口 | 若中心是社会许可与主体边界，可映射 P5/P6；若中心是主体认同或性别结构，则转相应专题。 |
| Queer Love | TH2.1 + TH3.2 接口 | 不作为独立人类问题轴。具体爱欲关系仍按 P1–P7 分析；酷儿身份、性规范与规训进入 TH3.2。 |
| Gothic Romance | TY / M / 类型比较接口 | 是文类/美学组合，不是 TH2.1 人类问题。保留用于跨类型比较。 |
| 历史爱情 | TY / 时间比较接口 | “历史”是设定、文类或时间比较维度，不构成独立爱情问题。 |
| 爱情 × 其他类型 | TY / 跨类型接口 | 明确保留为类型接口，不进入 TH2.1 内部问题结构。 |

## 字段治理

### 继续保留

旧作品中的：

```yaml
love_priority:
love_history_stage:
love_axes:
```

暂不删除，以保证旧专题、Base 与历史材料仍可工作。

### 解释权变化

- `love_axes`：从“当前结构轴”降级为 `legacy compatibility / historical tags`；
- `love_history_stage`：只承担爱情书写史比较，不再决定 TH2.1 内部结构；
- `love_priority`：可继续表示旧专题阅读优先级，但不能单独证明作品属于 TH2.1 核心。

### 后续如需新增结构化字段

若未来需要支持算法分析，可新增稳定的问题字段，例如：

```yaml
qh21_problems:
  - P2
  - P5
  - P7
```

但必须在作品重新人工校准后写入，不能机械由旧 `love_axes` 自动转换。

## 为什么不自动迁移

旧标签存在多对多与跨专题关系。例如：

- `爱与毁灭` 可能是 P4、P6 或 P7；
- `爱情与女性主体` 可能是 P5/P6，也可能真正属于 TH1.1 或 TH3.1；
- `欲望 / 身体 / 性` 可能属于具体爱欲，也可能根本应进入 TH3.2。

因此自动映射会制造伪精确数据。

## 最终状态

```text
LEGACY_LOVE_AXES = PRESERVED
LEGACY_LOVE_AXES_ROLE = COMPATIBILITY_ONLY
AUTO_MIGRATION = FORBIDDEN
MANUAL_PROBLEM_CALIBRATION = REQUIRED_IF_NEW_FIELD_IS_ADDED
```
