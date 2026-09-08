---
id: WL-CN12-COLLECTION-TEMPLATE-V1
legacy_id: WL-CN12-COLLECTION-TEMPLATE-V1
type: literature_governance_template
system_role: work_knowledge_network
scope: CN1.2
resource_type: collection_tradition
status: FROZEN_V1
version: "1.0"
---
# CN1.2 collection_tradition 专题模板 V1

> 适用于故事集合、框架叙事集合、编纂集合等拥有多版本／多见证生命史的 CN1.2 对象。模板冻结的是认知职责与数据接口，不要求所有专题逐字复制标题。

## 0. 准入前提

候选至少满足 CN1.2 通用准入门槛中的 4 项，并额外确认：

1. 研究对象是“集合的历时生命”，不是单一固定版本；
2. 至少存在两个可比较的 collection witness / edition / translation layer；
3. 集合成员、顺序、边界或编纂方式的变化本身具有解释价值。

## 1. 主页必须回答

- 集合身份如何被识别；
- 是否存在固定目录；
- 关键 witness / manuscript family / recension 是什么；
- 哪些变化发生在手稿层、印本层、翻译层或编辑层；
- 当前 build stage 与证据风险。

## 2. 六层认知职责

```text
10 集合边界、识别机制与可选框架叙事
11 早期形成、collection witness、手稿家族与 recension
12 story membership、增删、重排与集合边界变动
13 翻译层、source mode 与编辑重组
14 印本、跨语言传播、现代选本与再编
15 CN2 组件、证据纪律与阅读接口
```

## 3. 核心字段

```yaml
resource_type: collection_tradition
collection_boundary:
collection_witness:
manuscript_family:
recension:
story_membership:
membership_status:
translation_layer:
editorial_recomposition:
source_mode:
addition_removal:
```

可选：

```yaml
frame_narrative:
edition_witness:
translation_witness:
source_layer:
```

## 4. membership relation

必须采用：

```text
story × collection_witness → membership_status
```

禁止把 membership 写成故事本体上的永久 true/false 属性。

### membership_status V1

```text
core_attested
branch_attested
translation_added
later_print_added
absent_attested
uncertain
```

## 5. witness 分型

至少区分：

```text
early_witness
manuscript_witness
collection_witness
recension
edition_witness
translation_witness
source_layer
story_witness
work
```

`work` 只指中央 `40 作品` 的合法作品实体。

## 6. provenance 关系

推荐关系：

```text
translated_from
edited_from
based_on_witness
belongs_to_family
includes_story
excludes_story
adds_from_source
```

其中 `includes_story / excludes_story` 的语义应落到 membership relation，而不是无证据的 Canvas 箭头。

## 7. Canvas

Canvas 优先表达：

```text
来源环境
→ collection identity / frame
→ manuscript families / recensions
→ membership change
→ translations / editorial recomposition
→ print / global reception
```

禁止：

- 把后出印本画成早期手稿的直接原本；
- 把某故事在后期译本中的出现反向连接为早期核心成员；
- 仅凭故事相似性画历史传播箭头。

## 8. Structure Base

建议支持以下 semantic dimensions：

```text
boundary_and_identity
witness_and_recension
membership_change
translation_and_editing
print_and_reception
qc2_and_evidence
```

Base 反映语义责任，不依赖物理目录名。

## 9. Works / Versions Base

`03` 只投影中央 `40 作品` 中真正的 works。

手稿、recension、印本、translation witness 若未被中央作品库定义为合法 work，不得为了填表创建假 work。

允许：

```text
03 暂时为空
```

这是合法状态。

## 10. Coverage Review Gate

冻结前至少检查：

| Gate | 要求 |
|---|---|
| boundary | 集合身份可解释 |
| witnesses | 关键 collection witnesses 可区分 |
| membership | 至少有少量真实 story × witness 实测 |
| translation/editorial | 能解释集合边界因翻译／编辑而变化 |
| provenance | 至少一个现实可读版本可追底本 |
| work/witness | 未混淆 |
| evidence | 不反推、不假造 |
| reading reuse | 能回答真实版本差异问题 |

## 11. 冻结后重开条件

只有出现以下情况才重开：

- 新阅读版本无法由现有 provenance 模型解释；
- 新样板反复需要新的 membership 状态；
- collection-within-collection 结构无法承载；
- 关键 witness 关系被新研究推翻；
- 用户阅读持续遇到现有专题无法解释的集合边界问题。

## 12. 第一参考样板

→ [[CN1.2.4 一千零一夜故事集合与传播传统]]

> V1 原则：不做集合百科；只建足够解释“这个版本为什么长这样”的可追踪结构。