---
id: WL-QC124-COVERAGE-REVIEW-V1
type: literature_review
scope: QC1.2.4
resource_type: collection_tradition
status: PASS
version: "1.2"
---
# QC1.2.4 Coverage Review V1

## 结论

`PASS`

QC1.2.4 已完成第一轮结构验证、membership matrix 实测、真实阅读版本 provenance 实测，并补齐中央作品锚点。

当前专题由：

```text
《一千零一夜》 WL-WORK-0558
→ central work anchor

collection witness / manuscript family / recension
→ 版本与集合边界层

story × witness → membership_status
→ 故事成员层

translation / editorial provenance
→ 传播与重组层
```

共同构成完整的 `collection_tradition` 样板，因此保持 `STAGE_FROZEN`。

---

# 1. 集合边界模型

## PASS

```text
collection identity
≠ fixed table of contents
```

集合传统可以在成员规模、顺序、嵌套结构和版本边界发生变化时维持可识别身份。

正式能力：

```text
collection_boundary
```

`frame_narrative` 经本样板验证重要，但冻结为可选能力，不强制所有 collection_tradition 使用。

---

# 2. collection witness / manuscript family / recension

## PASS

仅使用 chronology 不足以表达同一时期不同集合见证的成员差异。

正式支持：

```text
collection_witness
manuscript_family
recension
edition_witness
translation_witness
```

这些对象不能被压扁成一个“标准原本”。

---

# 3. story_membership

## PASS

核心关系正式稳定为：

```text
story × collection_witness → membership_status
```

Membership Matrix V1 已用早期叙利亚系、Galland 翻译层和后期埃及印本层进行实测。

正式 `membership_status V1`：

```text
core_attested
branch_attested
translation_added
later_print_added
absent_attested
uncertain
```

`absent_attested` 表示已有可靠证据表明某具体 witness 不收录某故事；缺失本身是正数据。

实测：[[QC1.2.4 Membership Matrix V1]]

---

# 4. translation_layer / editorial_recomposition / source_mode

## PASS

集合型传统中的翻译不只是语言转换，还可能发生选择、删除、重排、合并独立材料、引入口述／书面新来源，从而改变后世集合边界。

正式支持：

```text
translation_layer
editorial_recomposition
source_mode
addition_removal
```

---

# 5. 真实阅读版本 provenance

## PASS

已使用 Husain Haddawy 的 *The Arabian Nights* 完成现实阅读路径实测：

```text
Haddawy modern translation
→ Muhsin Mahdi critical edition
→ fourteenth-century Syrian manuscript witness
→ Syrian manuscript family
→ QC1.2.4 collection tradition
```

该模型可以解释为什么不同现代版本的故事目录不同，而不把差异误判为简单的“完整版／删节版”。

实测：[[QC1.2.4 Provenance Test V1]]

---

# 6. 中央作品锚点

## PASS

中央 `40 作品` 中已有：

```text
《一千零一夜》
ID: WL-WORK-0558
priority: ★
role: 中央集合性作品锚点
```

现已补入 `qc124_*` 字段，并修复旧记录中的错误作者元数据。

中央作品锚点负责：

- 统一书目入口；
- 阅读状态；
- 跨轴与跨专题连接；
- `03 Works Base` 投影。

它不负责指定唯一标准手稿、唯一目录或唯一文本版本。

因此：

```text
central work anchor
≠ manuscript
≠ recension
≠ edition witness
≠ translation witness
```

---

# 7. work 与 witness 粒度

## PASS

当前稳定分层：

```text
《一千零一夜》
→ central work anchor

叙利亚手稿／后期埃及 recension
→ collection_witness

Bulaq / Calcutta
→ edition_witness

Galland / Haddawy
→ translation_witness

Diyab
→ source_layer

《阿拉丁》《阿里巴巴》等
→ story membership / story witness
```

Galland 等关键译本当前继续作为 `translation_witness`；只有未来中央作品治理规则明确需要把某一译本作为独立可阅读作品实体时，再单独升格，不因专题展示需要而机械建 work。

---

# 8. 与既有类型的稳定差异

```text
narrative_cycle
核心材料 → 文本见证 → 版本／分支 → 人物／事件变体

figure_tradition
中心人物 → 世界框架 → 人物网络 → 子传统 → 人物功能再发明

collection_tradition
中央集合性作品锚点 + 集合身份 → collection witness → membership 变化 → 翻译／编辑重组 → 印本／全球版本生命
```

因此 QC1.2 可以共享产品壳，但不能共享一套中层字段。

---

# 9. 冻结 Gate

| 条件 | 状态 |
|---|---|
| collection boundary | PASS |
| frame_narrative 支持 | PASS |
| manuscript / recension | PASS |
| story_membership | PASS |
| membership_status | PASS |
| translation/editorial | PASS |
| central work anchor | PASS |
| work/witness 分层 | PASS |
| membership matrix 实测 | PASS |
| real-edition provenance 实测 | PASS |
| evidence discipline | PASS |

## 最终判断

```text
QC1.2.4 = STAGE_FROZEN
collection_tradition = FROZEN_V1
```

冻结模板：[[QC1.2 collection_tradition 专题模板 V1]]  
冻结记录：[[QC1.2 collection_tradition Stage Freeze Review V1]]