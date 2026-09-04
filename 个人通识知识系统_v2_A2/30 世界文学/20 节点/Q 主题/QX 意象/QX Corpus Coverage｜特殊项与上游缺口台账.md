---
id: WL-QX-CORPUS-COVERAGE-LEDGER
type: literature_qx_governance
name: QX Corpus Coverage｜特殊项与上游缺口台账
axis: Q
facet: QX
status: ACTIVE
schema: QX_RELATION_SCHEMA_V1
---

# QX Corpus Coverage｜特殊项与上游缺口台账

> 目的：记录“没有进入 Work-level 正式 QX”的非普通原因。这里的项目不得自动计为 QX=0。

## 01｜状态定义

```text
FORMAL_QX
= Work 已核实为实际阅读单元，且至少一条关系通过 Admission Gate

ZERO_QX
= Work 已核实为实际阅读单元，也完成 QX 审查，但当前没有对象通过 Gate

DEFER_STORY_LEVEL
= 阅读事实对应短篇集 / 多独立叙事，需要篇章级处理

DEFER_SERIES_GRANULARITY
= 阅读记录是系列总称或卷级不清，需要先恢复卷级阅读事实

DEFER_EDITORIAL_COLLECTION
= 编辑型选集 / 精选，目录依版本变化，不能用标题中的某一篇代替整个阅读事实

ONE_TO_MANY_RECONCILIATION
= 一条读书记录实际映射多个 Work

UPSTREAM_WORK_BUILD_GAP
= R3.5 已要求创建中央 Work，但当前分支没有可复用 Work；QX 尚未真正审查
```

## 02｜R3.5 原生“特殊待确认”8条

### 系列 / 全集粒度

| 读书记录 | 状态 | QX 下一步 |
|---|---|---|
| 福尔摩斯探案全集 | DEFER_SERIES_GRANULARITY | 根据实际版本目录恢复长篇 / 短篇阅读单元 |
| 哈利·波特 | DEFER_SERIES_GRANULARITY | 先确认实际读过哪些单卷，再按卷标 QX |
| 龙族 | DEFER_SERIES_GRANULARITY | 先确认具体已读卷，不给系列总称挂跨卷 QX |

### 编辑型短篇选集

| 读书记录 | 状态 | QX 下一步 |
|---|---|---|
| 麦琪的礼物：欧·亨利短篇小说经典 | DEFER_EDITORIAL_COLLECTION | 先取得具体版本目录 / 实际读篇 |
| 莫泊桑短篇小说精选 | DEFER_EDITORIAL_COLLECTION | 同上 |
| 欧·亨利短篇小说选 | DEFER_EDITORIAL_COLLECTION | 同上 |
| 契诃夫短篇小说选 | DEFER_EDITORIAL_COLLECTION | 同上 |
| 项链：莫泊桑中短篇小说选 | DEFER_EDITORIAL_COLLECTION | 不以《项链》单篇替代整本选集阅读事实 |

## 03｜QX 阶段额外发现的篇章级项目

| 中央 Work / 阅读记录 | 状态 | 原因 |
|---|---|---|
| 夜晚的潜水艇 | DEFER_STORY_LEVEL | 短篇小说集；默认最小独立叙事单元 |
| 机器人短篇全集 | DEFER_STORY_LEVEL | 多独立机器人短篇 |
| 草 | DEFER_STORY_LEVEL | 文集 / 杂文集合，中央元数据粒度与实际阅读形态不完全一致 |
| 人类的群星闪耀时 | DEFER_STORY_LEVEL | 多篇相对独立的历史微型传记 |
| 哑舍 | DEFER_STORY_LEVEL | 连缀式独立器物故事，需要篇章级核验 |
| 台北人 | DEFER_STORY_LEVEL | 作者短篇小说集，不能把单篇强意象直接提升为整本事实 |
| 燃烧的原野 | DEFER_STORY_LEVEL | 鲁尔福短篇集；来自一对多阅读记录 |
| 彷徨 | DEFER_STORY_LEVEL | 短篇小说集 |
| 呐喊 | DEFER_STORY_LEVEL | 短篇小说集 |
| 俗世奇人（足本） | DEFER_STORY_LEVEL | 多篇人物故事集合 |

## 04｜一对多阅读记录

### 《燃烧的原野：鲁尔福三部曲》

R3.5 收口为：

```text
一条读书记录
→ 佩德罗·巴拉莫
→ 燃烧的原野
→ 金鸡
```

当前：

| 子 Work | 当前 QX 状态 |
|---|---|
| 佩德罗·巴拉莫 | FORMAL_QX |
| 燃烧的原野 | DEFER_STORY_LEVEL |
| 金鸡 | UPSTREAM_WORK_BUILD_GAP |

## 05｜已确认的上游 Work 建库缺口

以下项目在 R3.5 / 已读覆盖层中属于文学已读；Batch029 起逐项恢复中央 Work 并进入正式 QX：

| 作品 / 阅读记录 | 状态 |
|---|---|
| 盗墓笔记：七星鲁王宫 | UPSTREAM_WORK_BUILD_GAP |
| 临界·爵迹I | UPSTREAM_WORK_BUILD_GAP |
| 我的一个世纪（增订版） | UPSTREAM_WORK_BUILD_GAP |
| 你当像鸟飞往你的山 | FORMAL_QX |
| 看见 | UPSTREAM_WORK_BUILD_GAP |
| 天才在左，疯子在右 | UPSTREAM_WORK_BUILD_GAP |
| 盐镇 | UPSTREAM_WORK_BUILD_GAP |
| 鱼翅与花椒 | UPSTREAM_WORK_BUILD_GAP |
| 苏菲的世界 | FORMAL_QX |
| 金鸡 | UPSTREAM_WORK_BUILD_GAP |

对尚未恢复项目继续执行：

```text
QX_DECISION = NOT_YET_EVALUATED
DO_NOT_COUNT_AS_ZERO_QX
DO_NOT_CREATE_DUPLICATE_WORK_IN_QX_PHASE
```

Batch029 已恢复项目：

```text
你当像鸟飞往你的山 → 2 formal QX
苏菲的世界 → 2 formal QX
```

## 06｜已发生并纠正的粒度错误

### 《麦琪的礼物》

曾错误地依据中央 `麦琪的礼物.md`，将短篇《麦琪的礼物》的长发、金表、发梳 / 表链写成正式 QX。

尾部复核发现个人读书记录实际是编辑型选集《麦琪的礼物：欧·亨利短篇小说经典》，R3.5 明确要求“特殊项待确认”。

因此：

```text
3 formal relations = REVERTED
reason = COLLECTION_TITLE ≠ VERIFIED_STORY_READ_FACT
```

该案例作为后续 collection-level QA 的基准反例。

## 07｜后续处理顺序

```text
1. 先补 UPSTREAM_WORK_BUILD_GAP
2. 恢复 SERIES 的卷级阅读事实
3. 对稳定作者短篇集建立 story-level reading map
4. 对编辑型选集取得具体版本目录 / 实际读篇
5. 再进行 story-level QX
6. 最后重新计算 corpus coverage
```

## 08｜当前正式 QX 基线

截至 Batch029 第一组：

```text
FORMAL_WORKS_WITH_QX = 119
FORMAL_QX_RELATIONS = 360
```

> 这两个数字只表示“拥有至少一条正式 QX 的 Work”，不是 173 条文学阅读记录的完成率。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次028]]
- [[QX Formal Annotation｜增量批次029]]
