---
id: WL-QC1.2.4
type: literature_node
name: 一千零一夜故事集合与传播传统
code: QC1.2.4
axis: Q
parent: WL-QC1.2
level: 5
coverage_priority: Core
node_kind: taxonomy_leaf
anchorable: true
resource_type: collection_tradition
status: ACTIVE
build_stage: topic_build
---
# QC1.2.4 一千零一夜故事集合与传播传统

QC1.2 的第一个 `collection_tradition` 验证样板。

本专题研究的不是“《一千零一夜》有哪些故事”，而是：

> **一个没有固定终极目录的故事集合，如何在手稿、编纂、印本、翻译与文化再生产中不断改变自己的边界，同时仍然被识别为“同一个集合传统”？**

## 核心模型

```text
多层早期叙事资源
      ↓
框架叙事 frame_narrative
      ↓
阿拉伯语手稿／版本家族 manuscript_family / recension
      ↓
故事成员 story_membership 持续增删与重排
      ↓
翻译层 translation_layer
      ↓
编辑重组 editorial_recomposition
      ↓
印本与全球传播
```

## 与既有 QC1.2 类型的差异

- `narrative_cycle` 主要追踪共享故事材料如何形成文本谱系、版本与分支；
- `figure_tradition` 主要追踪中心人物如何吸附人物网络与子传统；
- `collection_tradition` 则必须回答：**集合边界本身如何变化。**

因此本专题重点验证：

1. `collection_boundary`；
2. `frame_narrative`；
3. `collection_witness`；
4. `manuscript_family` / `recension`；
5. `story_membership`；
6. `membership_status`；
7. `addition_removal`；
8. `translation_layer`；
9. `editorial_recomposition`；
10. `source_mode`。

## 当前边界

### 纳入

- 山鲁佐德／国王的框架叙事及其集合识别功能；
- 早期形成与阿拉伯语手稿传统；
- 不同手稿／版本家族中的故事成员变化；
- 后期埃及版本与阿拉伯语印本；
- 加朗法译及其对全球《一千零一夜》形态的重构；
- 迪亚布等口述／书面来源进入翻译传统的过程；
- 近现代重要译本、选本与编辑重组所造成的集合边界变化。

### 不自动纳入

- 所有阿拉伯、波斯或中东民间故事；
- 仅因“东方故事”风格相似而被并入的文本；
- 《阿拉丁》《阿里巴巴》等单个故事的全部后世改编；
- 所有现代《一千零一夜》改写作品。

单个故事若拥有独立、可追踪的跨文本生命，可另行评估为 `story_tradition`，而不是无限扩张本专题。

## 当前证据纪律

- “1001”不是稳定故事数量的同义词；
- 某故事出现在著名译本中，不等于它属于所有早期阿拉伯语手稿；
- 后出印本的完整目录不能反推为早期集合原貌；
- 翻译、口述采集、编辑补写和原手稿见证必须区分；
- 不把“原始／伪作”作为唯一二分，而记录故事进入集合的具体见证层。

## 专题产品

→ [[../../30 专题/QC1.2.4 一千零一夜故事集合与传播传统/00 一千零一夜故事集合与传播传统|QC1.2.4 专题主页]]

准入记录：[[QC1.2.4 一千零一夜故事集合与传播传统 Source Readiness Review]]

## 当前状态

`TOPIC_BUILD`

当前任务是验证 `collection_tradition` 的知识组织能力，而不是建立故事全集。