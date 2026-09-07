---
id: WL-QC1.2.4
type: literature_node
name: 一千零一夜故事集合与传播传统
code: QC1.2.4
axis: Q
system_role: work_knowledge_network
parent: WL-QC1.2
level: 5
coverage_priority: Core
node_kind: taxonomy_leaf
anchorable: true
resource_type: collection_tradition
status: ACTIVE
build_stage: stage_frozen
---
# QC1.2.4 一千零一夜故事集合与传播传统

QC1.2 的第一个 `collection_tradition` 冻结参考样板。

本专题研究的不是“《一千零一夜》有哪些故事”，而是：

> **一个没有固定终极目录的故事集合，如何在手稿、编纂、印本、翻译与文化再生产中不断改变自己的边界，同时仍然被识别为“同一个集合传统”？**

## 核心模型

```text
collection identity
      ↓
可选 frame_narrative
      ↓
collection witness / manuscript family / recension
      ↓
story × witness → membership_status
      ↓
translation_layer / source_mode
      ↓
editorial_recomposition
      ↓
印本与全球版本生命
```

## 已冻结 V1 核心能力

```text
collection_boundary
collection_witness
manuscript_family
recension
story_membership
membership_status
addition_removal
translation_layer
editorial_recomposition
source_mode
```

正式支持但不强制：

```text
frame_narrative
edition_witness
translation_witness
source_layer
```

## membership_status V1

```text
core_attested
branch_attested
translation_added
later_print_added
absent_attested
uncertain
```

注意：状态永远描述 `story × collection_witness`，不是故事本体的永久属性。

## 边界

### 纳入

- 山鲁佐德／国王的框架叙事及其集合识别功能；
- 早期形成与阿拉伯语手稿传统；
- 不同手稿／版本家族中的故事成员变化；
- 后期埃及 recension 与阿拉伯语印本；
- 加朗法译及其对全球集合边界的重构；
- 迪亚布等口述／书面来源进入翻译传统的过程；
- 重要现代译本、选本与编辑重组。

### 不自动纳入

- 所有阿拉伯、波斯或中东民间故事；
- 仅因“东方故事”风格相似而被并入的文本；
- 《阿拉丁》《阿里巴巴》等单个故事的全部后世改编；
- 所有现代《一千零一夜》改写作品。

单个故事若形成自己的历时文本生命，另行评估 `story_tradition`。

## 证据纪律

- “1001”不是稳定故事数量；
- 著名译本收录 ≠ 所有早期阿拉伯语 witness 收录；
- 后期完整印本不能反推早期集合原貌；
- 翻译、口述采集、单独文本整合、编辑补写和原手稿见证必须区分；
- `absent_attested` 是正数据，`uncertain` 不能伪装成 absent；
- 不使用“原始／伪作”二分取代 provenance。

## 已完成验证

- Source Readiness：PASS
- Topic Build：PASS
- Coverage Review：PASS
- Membership Matrix：PASS
- Real-edition Provenance Test：PASS
- Stage Freeze：PASS

专题主页：[[../../30 专题/QC1.2.4 一千零一夜故事集合与传播传统/00 一千零一夜故事集合与传播传统|QC1.2.4 专题主页]]  
冻结模板：[[QC1.2 collection_tradition 专题模板 V1]]

## 当前状态

`STAGE_FROZEN`

除非真实阅读暴露新版本无法解释、关键证据修正或第二 collection_tradition 样板迫使模板升级，否则停止横向扩充本专题。