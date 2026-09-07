---
id: WL-QC12-COLLECTION-STAGE-FREEZE-V1
type: literature_governance_review
scope: QC1.2
resource_type: collection_tradition
status: PASS_FROZEN_V1
version: "1.1"
---
# QC1.2 collection_tradition Stage Freeze Review V1

## 结论

`PASS_FROZEN_V1`

由 [[QC1.2.4 一千零一夜故事集合与传播传统]] 作为第一异质样板，并通过：

- boundary / source readiness；
- topic build；
- coverage review；
- membership matrix 实测；
- 现实阅读版本 provenance 实测；
- 中央作品锚点验证；

现有证据已足以冻结 `collection_tradition` 的 **V1 产品模板与核心语义能力**。

冻结的是第一版稳定职责，不是宣称所有故事集合都必须长得和《一千零一夜》一样。

---

# 1. 核心对象定义

`collection_tradition` 适用于：

> 一个故事集合、框架叙事集合或编纂体系，在多个手稿、版本、印本、译本和编辑层中持续改变成员边界，同时保持可识别集合身份的历时传统。

它不以单一作者原作、固定故事数量或唯一目录为必要条件。

---

# 2. 冻结的 V1 核心能力

```text
collection_boundary
collection_witness
manuscript_family
recension
story_membership
membership_status
translation_layer
editorial_recomposition
source_mode
addition_removal
```

正式支持但不要求每个专题都有：

```text
frame_narrative
edition_witness
translation_witness
source_layer
```

关系层支持：

```text
translated_from
edited_from
based_on_witness
belongs_to_family
```

这些关系不另升格为顶级知识层。

---

# 3. membership_status V1

冻结为：

```text
core_attested
branch_attested
translation_added
later_print_added
absent_attested
uncertain
```

含义：

- `core_attested`：在当前专题定义的早期／核心 collection witness 中可证；
- `branch_attested`：在某一特定 manuscript family / recension / edition 分支中可证；
- `translation_added`：通过翻译或译者来源层进入该传播集合；
- `later_print_added`：在后期印本或编辑重组中进入；
- `absent_attested`：有可靠证据表明该具体 witness 不收录；
- `uncertain`：当前证据不足。

状态描述的是**story × witness 关系**，不是故事本体的永久属性。

---

# 4. 冻结的关系模型

```text
story
×
collection_witness
→ membership_status
```

禁止简化为：

```text
story.belongs_to_collection = true / false
```

因为同一故事可在不同 witness 中出现完全不同状态。

---

# 5. 六层认知职责 V1

```text
10 集合边界、识别机制与可选框架叙事
11 早期形成、collection witness、手稿家族与 recension
12 story membership、增删、重排与集合边界变动
13 翻译层、source mode 与编辑重组
14 印本、跨语言传播、现代选本与再编
15 QC2 组件、证据纪律与阅读接口
```

标题可因专题调整；冻结的是语义职责，不是必须逐字复制的目录名。

---

# 6. 产品壳 V1

继续沿用 QC1.2 通用产品壳：

```text
00 主页.md
01 Canvas.canvas
02 结构／版本.base
03 作品／版本投影.base
10–15 认知层
Coverage Review
```

模板规则：

- `03` 只投影真正存在于中央 `40 作品` 的实体；
- manuscript / recension / collection witness 不得为了填满 Works Base 被伪装成中央 `work`；
- 如果专题确有合法中央作品锚点，应接入，而不是因为文本版本复杂就把作品层永久留空。

QC1.2.4 当前已验证这一点：中央 `40 作品` 中的 [[../../../40 作品/一千零一夜|《一千零一夜》]]（`WL-WORK-0558`）作为 ★ 集合性作品锚点进入 Works Base；Galland、Haddawy、Bulaq、Calcutta 等仍分别保持 translation / edition witness 身份。

---

# 7. frame_narrative 的冻结位置

`frame_narrative` 经《一千零一夜》验证非常重要，但不能假定所有 collection_tradition 都有框架叙事。

因此：

```text
supported capability = YES
mandatory field = NO
```

---

# 8. 证据纪律 V1

1. 集合名称相同 ≠ 故事目录相同；
2. 后期完整印本 ≠ 早期原貌；
3. 某故事全球知名 ≠ 早期核心 witness 可证；
4. 翻译可改变集合边界，不能只建 `language` 字段；
5. 口述来源、单独文本、手稿来源、译者改写必须区分 `source_mode`；
6. `absent_attested` 是正数据；
7. 未核验不能推断为 absent；
8. work / manuscript / recension / edition / translation 分型保持独立；
9. Canvas 不画“后期成员 → 早期手稿”的反向历史箭头；
10. 单个故事形成自己的跨文本历时生命后，可另评估 `story_tradition`。

---

# 9. 实测 gate

| Gate | 状态 |
|---|---|
| collection boundary | PASS |
| collection witness / manuscript family | PASS |
| recension | PASS |
| story membership | PASS |
| membership status | PASS |
| translation/editorial layer | PASS |
| central work anchor | PASS |
| work/witness 粒度 | PASS |
| membership matrix | PASS |
| real-edition provenance | PASS |
| evidence discipline | PASS |

因此：

```text
collection_tradition → FROZEN_V1
```

---

# 10. 尚未冻结成“宇宙通则”的部分

只有一个样板，因此以下仍作为可选能力而非强制普遍字段：

- frame_narrative；
- 具体 manuscript family 命名法；
- translation-added 与 later-print-added 是否足以覆盖所有未来集合；
- 嵌套型 collection-within-collection 是否需要独立层。

未来第二个 collection_tradition（如《五卷书》—《卡里来和笛木乃》）若暴露新需求，再版本升级，不阻止 V1 冻结。

## 最终判定

> `QC1.2 collection_tradition 专题模板 V1` 已可正式使用；QC1.2.4 同时验证了“有中央作品锚点时应接入 Works Base，但 witness 不随之被作品化”的作品／见证分层规则。