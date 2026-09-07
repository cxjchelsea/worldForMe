---
id: WL-QC124-COVERAGE-REVIEW-V1
type: literature_review
scope: QC1.2.4
resource_type: collection_tradition
status: PASS_WITH_PATCH
version: "1.0"
---
# QC1.2.4 Coverage Review V1

## 结论

`PASS_WITH_PATCH`

QC1.2.4 已经足以证明 `collection_tradition` 与 `narrative_cycle`、`figure_tradition` 存在稳定的中层组织差异：其核心对象不是固定情节链或中心人物，而是**集合身份、版本见证和故事成员关系的变化**。

当前不 stage freeze。下一轮只补两个真正影响模型稳定性的部分，而不扩充故事数量。

---

# 1. 集合边界模型

## PASS

本专题已经验证：

```text
collection identity
≠ fixed table of contents
```

集合传统可以在成员规模、顺序和嵌套结构变化的情况下持续维持可识别身份。

建议进入正式候选能力：

```text
collection_boundary
frame_narrative
```

---

# 2. frame_narrative 是否应成为独立能力

## PASS

山鲁佐德框架不是普通成员故事，而是组织整个开放集合的重要容器机制。

因此：

```text
frame_narrative
≠ ordinary story_membership
```

未来其他 collection_tradition 不一定都有框架叙事，所以它应是“正式支持的可选能力”，而不是所有集合传统强制字段。

---

# 3. manuscript_family / recension

## PASS

仅使用 chronology 无法表达同一时期不同集合见证拥有不同故事成员的情况。

因此 collection_tradition 至少需要：

```text
collection_witness
manuscript_family
recension
edition_witness
```

其职责是回答“这一具体版本的集合边界是什么”，而不是制造一个抽象标准原本。

---

# 4. story_membership

## PASS

这是本专题相较前两个模板最重要的新数据能力。

推荐关系模型：

```text
story
×
collection_witness
→ membership relation
```

第一轮状态词：

```text
core_attested
branch_attested
translation_added
later_print_added
uncertain
```

注意：这些状态描述见证层级，不是文学价值等级。

---

# 5. translation_layer / editorial_recomposition

## PASS

本专题证明翻译对集合型传统不能只记录语言转换。

需要允许：

```text
translation_layer
editorial_recomposition
source_mode
addition_removal
```

因为译本可能选择、删减、重排，并引入新的来源层，从而实际改变后续读者所理解的“集合边界”。

---

# 6. work 与 witness 粒度

## PASS

当前继续保持：

```text
collection_tradition
≠ collection_witness
≠ manuscript / recension / edition
≠ translation_witness
≠ story_witness
≠ work
```

本专题尚未找到可安全复用的中央 `40 作品` 实体，也没有明确的数字作品 ID 分配规则，因此本轮**不新造 work ID**。

这是正确的空缺，而不是产品缺陷。当前核心研究事实由 witness registry 承担；未来发现／建立合法中央作品实体后，`03 Works Base` 会自动成为投影视图。

---

# 7. 与既有类型的差异

当前三种已建类型可以比较为：

```text
narrative_cycle
核心材料 → 文本见证 → 版本／分支 → 人物／事件变体

figure_tradition
中心人物 → 世界框架 → 人物网络 → 子传统 → 人物功能再发明

collection_tradition
集合身份 → 框架机制 → collection witness → membership 变化 → 翻译／编辑重组
```

这进一步证明 QC1.2 的六层产品壳可以共享，但中层知识模型不能统一成一套字段。

---

# 8. 当前两个补丁

## PATCH A：建立具体 membership 对照矩阵

下一轮至少选 3 个具有代表性的 collection witness / translation layer，对 5–10 个关键故事建立：

```text
story × witness → membership_status
```

目的不是做故事大全，而是实测 membership 模型是否足够表达真实差异。

应优先包含：

- 框架核心相关成员；
- 在早期关键见证中可证的故事；
- 《阿拉丁》《阿里巴巴》等 translation-added / later-canonized 案例。

## PATCH B：验证一个实际阅读版本的 provenance 路径

选择一个真实可阅读的现代／近代版本，完整追踪：

```text
当前版本
→ 直接底本／中介译本
→ recension / manuscript family（如可证）
→ membership selection
```

用来验证 `translation_layer` 和 `editorial_recomposition` 是否足以服务实际阅读。

---

# 9. 冻结判定

| 条件 | 状态 |
|---|---|
| collection boundary 稳定 | PASS |
| frame_narrative 能表达 | PASS |
| manuscript / recension 模型 | PASS |
| story_membership 模型 | PASS |
| translation/editorial 模型 | PASS |
| work/witness 分层 | PASS |
| 具体 membership 数据实测 | PATCH |
| 实际阅读版本 provenance 实测 | PATCH |
| collection_tradition 模板冻结 | 尚早 |

## 最终判断

```text
QC1.2.4 = COVERAGE_REVIEW_PASS_WITH_PATCH
```

下一阶段只做两个实测补丁，再判断是否冻结 `QC1.2 collection_tradition 专题模板 V1`。