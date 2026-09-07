---
id: WL-QC124-COVERAGE-REVIEW-V1
type: literature_review
scope: QC1.2.4
resource_type: collection_tradition
status: PASS
version: "1.1"
---
# QC1.2.4 Coverage Review V1

## 结论

`PASS`

QC1.2.4 已完成第一轮结构验证、membership matrix 实测与真实阅读版本 provenance 实测，原有两个 PATCH 均已关闭。

因此本专题可以进入 `STAGE_FROZEN`，并作为 `QC1.2 collection_tradition 专题模板 V1` 的第一参考样板。

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

本轮新增并确认 `absent_attested`：已有可靠证据表明某具体 witness 不收录某故事时，缺失本身是正数据。

实测：[[QC1.2.4 Membership Matrix V1]]

---

# 4. translation_layer / editorial_recomposition / source_mode

## PASS

集合型传统中的翻译不只是语言转换，还可能：

- 选择；
- 删除；
- 重排；
- 合并独立材料；
- 引入口述／书面新来源；
- 改变后世读者理解的集合边界。

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

该模型可以解释为什么 Haddawy 收录早期叙利亚系核心故事，却不把 Galland / Diyab 路径中的《阿拉丁》《阿里巴巴》重新塞回核心正文。

实测：[[QC1.2.4 Provenance Test V1]]

---

# 6. work 与 witness 粒度

## PASS

继续保持：

```text
collection_tradition
≠ collection_witness
≠ manuscript
≠ recension
≠ edition_witness
≠ translation_witness
≠ story_witness
≠ work
```

当前没有为了填满 `03 Works Base` 创造假的中央作品 ID；这是正确的结构行为。

---

# 7. 与既有类型的稳定差异

```text
narrative_cycle
核心材料 → 文本见证 → 版本／分支 → 人物／事件变体

figure_tradition
中心人物 → 世界框架 → 人物网络 → 子传统 → 人物功能再发明

collection_tradition
集合身份 → collection witness → membership 变化 → 翻译／编辑重组 → 印本／全球版本生命
```

因此 QC1.2 可以共享产品壳，但不能共享一套中层字段。

---

# 8. 冻结 Gate

| 条件 | 状态 |
|---|---|
| collection boundary | PASS |
| frame_narrative 支持 | PASS |
| manuscript / recension | PASS |
| story_membership | PASS |
| membership_status | PASS |
| translation/editorial | PASS |
| work/witness 分层 | PASS |
| membership matrix 实测 | PASS |
| real-edition provenance 实测 | PASS |
| evidence discipline | PASS |

## 最终判断

```text
QC1.2.4 = STAGE_FREEZE_READY
collection_tradition = FROZEN_V1
```

冻结模板：[[QC1.2 collection_tradition 专题模板 V1]]  
冻结记录：[[QC1.2 collection_tradition Stage Freeze Review V1]]