---
id: WL-QC124-MEMBERSHIP-MATRIX-V1
type: literature_review
scope: QC1.2.4
resource_type: membership_test
status: PASS
version: "1.0"
---
# QC1.2.4 Membership Matrix V1

> 目的：用少量高信息量样本实测 `story × collection_witness → membership_status`，不是建立《一千零一夜》故事全集。

## 1. 本轮 witness

| witness | 类型 | 用途 |
|---|---|---|
| Mahdi / Haddawy 所据14世纪叙利亚手稿传统 | manuscript / critical-edition witness | 代表早期叙利亚系集合边界 |
| Antoine Galland 法译传统（1704–1717） | translation_witness | 代表翻译层对集合边界的扩展与重组 |
| Bulaq 1835 / Calcutta II 1839–1842 后期埃及“vulgate”层 | edition_witness / recension | 代表19世纪后期埃及完整化、印刷化集合 |

## 2. membership_status V1

本轮实测后，将状态词收敛为：

```text
core_attested        在早期核心 witness 中可证
branch_attested      在某一后期 manuscript / recension / edition 分支中可证
translation_added    在翻译／译者来源层进入传播集合
later_print_added    在后期印本／编辑重组层进入
absent_attested      已有可靠证据表明该 witness 不收录
uncertain             当前证据不足，不做推断
```

其中新增 `absent_attested` 很重要：**缺失本身也是 membership 数据**，不能只记录“出现”。

## 3. 第一轮矩阵

| 故事／单元 | Mahdi/Haddawy 叙利亚系 | Galland 法译层 | Bulaq/Calcutta II 层 | 说明 |
|---|---|---|---|---|
| 山鲁佐德—沙赫里亚尔框架 | `core_attested` | `branch_attested` | `branch_attested` | 属于集合识别机制；建模时仍与普通成员故事分开 |
| 商人与魔鬼 | `core_attested` | `branch_attested` | `branch_attested` | 早期核心成员样本 |
| 渔夫与魔鬼 | `core_attested` | `branch_attested` | `branch_attested` | 早期核心成员样本 |
| 脚夫与三个女人 | `core_attested` | `branch_attested` | `branch_attested` | 早期核心成员样本 |
| 三个苹果 | `core_attested` | `branch_attested` | `branch_attested` | 早期核心成员样本 |
| 驼背故事 | `core_attested` | `branch_attested` | `branch_attested` | 早期核心成员样本 |
| 辛巴达航海 | `absent_attested`（作为独立故事组不在 Mahdi/Haddawy 核心文本目录） | `translation_added / editorially_integrated` | `branch_attested` | 加朗先独立处理后并入其《一千零一夜》传播形态；后期集合亦常吸收 |
| 阿拉丁 | `absent_attested` | `translation_added` | `absent_attested` | 通过 Galland / Diyab 来源层进入全球《一千零一夜》传统，但不应反投射到早期核心手稿或Bulaq/Calcutta II |
| 阿里巴巴 | `absent_attested` | `translation_added` | `absent_attested` | 与阿拉丁类似，是“全球经典成员 ≠ 所有阿拉伯文本成员”的关键案例 |

## 4. 实测结论

### 4.1 关系模型成立

同一个故事不能拥有一个脱离 witness 的单一 `membership_status`。

必须记录：

```text
story
×
collection_witness
→ membership_status
```

例如：

```text
Aladdin × Mahdi/Haddawy → absent_attested
Aladdin × Galland → translation_added
Aladdin × Bulaq/Calcutta II → absent_attested
```

因此“阿拉丁是不是《一千零一夜》的故事”不是合法的一阶数据问题；合法问题是“它在什么集合见证中、通过什么来源层成为成员”。

### 4.2 `absent_attested` 必须进入正式模板

原候选状态没有明确表达“已证缺失”。本轮证明它不可缺少。

最终 V1 建议：

```text
core_attested
branch_attested
translation_added
later_print_added
absent_attested
uncertain
```

### 4.3 `source_mode` 与 membership 必须并存

尤其对 Galland 层：

```text
membership_status: translation_added
source_mode: oral_source / translator_source_layer / separate_text_integration
```

这样才能区分“译自已有核心 manuscript”与“通过翻译者的新来源进入集合”。

## 5. 边界纪律

- 本矩阵只证明模型能处理关键差异，不代表这些 witness 的完整目录；
- 不从一个后期印本的收录反推早期手稿；
- 不把全球知名度当作 `core_attested`；
- `branch_attested` 只说明该具体分支可证，不自动提升为全传统共同成员；
- 未核验单元一律 `uncertain`，不凭常识补表。

## 6. 判定

```text
Membership data test = PASS
```

`story_membership`、`membership_status`、`source_mode` 足以承担第一版 collection_tradition 的真实成员差异；仅需把 `absent_attested` 固化进 V1。