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
= 阅读记录是系列总称或卷级边界尚无法稳定映射，需要先恢复实际阅读单元

DEFER_EDITORIAL_COLLECTION
= 编辑型选集 / 精选，目录依版本变化，不能用标题中的某一篇代替整个阅读事实

ONE_TO_MANY_RECONCILIATION
= 一条读书记录实际映射多个 Work

UPSTREAM_WORK_BUILD_GAP
= 已读覆盖层要求创建中央 Work，但当前分支没有可复用 Work；QX 尚未真正审查
```

## 02｜R3.5 原生“特殊待确认”8条

### 系列 / 全集粒度

| 读书记录 | 状态 | 当前结论 / QX 下一步 |
|---|---|---|
| 福尔摩斯探案全集 | ONE_TO_MANY_RECONCILIATION | 全集阅读事实已确认；当前完成 4 长篇 +《福尔摩斯历险记》12短篇，共 16/60；剩余 44 短篇 |
| 哈利·波特 | ONE_TO_MANY_RECONCILIATION | 七册中央 Work 均为已读，7 Work / 21 formal QX；系列粒度闭环 |
| 龙族 | DEFER_SERIES_GRANULARITY | 全集阅读事实已确认，但原始出版 / 修订 / 连载 / 重写边界不稳定；先恢复采用的版本 / 卷级结构，不给系列父节点挂跨卷 QX |

> Batch030 已确认三条系列记录的“是否完整读过”都不是未知项。剩余问题仅是中央 Work 映射与版本 / 独立叙事粒度。

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

```text
一条读书记录
→ 佩德罗·巴拉莫 → FORMAL_QX
→ 燃烧的原野 → DEFER_STORY_LEVEL
→ 金鸡 → FORMAL_QX
```

### 《哈利·波特》

```text
7 child Works
7 FORMAL_QX
21 formal relations
HARRY_POTTER_GRANULARITY = CLOSED
```

### 《福尔摩斯探案全集》

全集阅读事实已确认；标准粒度：

```text
4 novels + 56 short stories = 60 independent narrative units
```

当前已完成：

```text
4 novels → FORMAL_QX / 12 relations
The Adventures of Sherlock Holmes 12 stories → FORMAL_QX / 19 relations
```

《福尔摩斯历险记》12篇已全部恢复为中央 Work：

```text
波希米亚丑闻
红发会
身份案
博斯科姆比溪谷秘案
五个橘核
歪唇男人
蓝宝石案
斑点带子案
工程师大拇指案
单身贵族案
绿玉皇冠案
铜山毛榉案
```

```text
SHERLOCK_CANON_UNITS = 60
SHERLOCK_UNITS_COMPLETE = 16
SHERLOCK_SHORT_STORIES_COMPLETE = 12
SHERLOCK_SHORT_STORIES_REMAINING = 44
SHERLOCK_FORMAL_RELATIONS_CURRENT = 31
```

后续按短篇集逐组推进，不将“贝克街 / 烟斗 / 放大镜”等系列标志物自动复制到各篇。

## 05｜上游 Work 建库缺口：Batch029 已收口

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_FORMAL_QX = 7
UPSTREAM_ZERO_QX = 3
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 06｜已发生并纠正的粒度错误

### 《麦琪的礼物》

```text
3 formal relations = REVERTED
reason = COLLECTION_TITLE ≠ VERIFIED_STORY_READ_FACT
```

该案例继续作为 collection-level QA 的基准反例。

## 07｜后续处理顺序

```text
1. UPSTREAM_WORK_BUILD_GAP → CLOSED
2. SERIES / VOLUME GRANULARITY
   - 哈利·波特 → CLOSED
   - 福尔摩斯探案全集 → CURRENT / 16 OF 60 COMPLETE
     - 四部长篇 → CLOSED
     - 福尔摩斯历险记 → CLOSED
     - 福尔摩斯回忆录 → NEXT
     - 福尔摩斯归来记 → PENDING
     - 最后致意 → PENDING
     - 福尔摩斯案件簿 → PENDING
   - 龙族 → DEFER_VERSION_BOUNDARY
3. 稳定作者短篇集 story-level reading map
4. 编辑型选集版本目录 / 实际读篇
5. story-level QX
6. 重新计算 corpus coverage
```

## 08｜当前正式 QX 基线

截至 Batch030《哈利·波特》七册 + 福尔摩斯四部长篇 +《福尔摩斯历险记》12短篇：

```text
FORMAL_WORKS_WITH_QX = 147
FORMAL_QX_RELATIONS = 420
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
```

> 正式 QX 数字只统计拥有至少一条正式关系的 Work。ZERO_QX 表示已完成审查但不进入该计数；系列父记录也不作为独立 QX Work 计数。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次028]]
- [[QX Formal Annotation｜增量批次029]]
- [[QX Formal Annotation｜增量批次030]]
