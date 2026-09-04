---
id: WL-QX-FORMAL-ANNOTATION-030
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次030
code: QX-ANNOTATION-030
axis: Q
facet: QX
status: PARTIAL_SERIES_RECONCILIATION
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次030

> 本批进入 `SERIES / VOLUME GRANULARITY`。系列总称不直接挂 QX；先恢复真实阅读单元，再按 `SMALLEST_INDEPENDENT_NARRATIVE_UNIT` 进入正式标注。

## 01｜本批阶段结果

```text
HARRY_POTTER_SERIES = RESOLVED
HARRY_POTTER_CHILD_WORKS = 7
HARRY_POTTER_FORMAL_QX_WORKS = 7
HARRY_POTTER_FORMAL_RELATIONS = 21

SHERLOCK_HOLMES_SERIES = ONE_TO_MANY_RECONCILIATION
SHERLOCK_READ_SCOPE = COMPLETE_CANON_CONFIRMED
SHERLOCK_CANON_UNITS = 60
SHERLOCK_LONG_NOVELS_RECONCILED = 4
SHERLOCK_LONG_NOVEL_FORMAL_RELATIONS = 12
SHERLOCK_ADVENTURES_STORIES_RECONCILED = 12
SHERLOCK_ADVENTURES_FORMAL_RELATIONS = 19
SHERLOCK_UNITS_COMPLETE = 16
SHERLOCK_SHORT_STORIES_REMAINING = 44
SHERLOCK_QX = PARTIAL_16_OF_60_COMPLETE

DRAGON_RAJAS_SERIES = DEFER_SERIES_GRANULARITY
DRAGON_RAJAS_READ_SCOPE = COMPLETE_SERIES_CONFIRMED
DRAGON_RAJAS_VERSION_BOUNDARY = UNRESOLVED

FORMAL_WORKS_WITH_QX_BEFORE = 124
FORMAL_QX_RELATIONS_BEFORE = 368
FORMAL_WORKS_WITH_QX_AFTER_GROUP_HP = 131
FORMAL_QX_RELATIONS_AFTER_GROUP_HP = 389
FORMAL_WORKS_WITH_QX_AFTER_SHERLOCK_NOVELS = 135
FORMAL_QX_RELATIONS_AFTER_SHERLOCK_NOVELS = 401
FORMAL_WORKS_WITH_QX_AFTER_SHERLOCK_ADVENTURES = 147
FORMAL_QX_RELATIONS_AFTER_SHERLOCK_ADVENTURES = 420
```

## 02｜《哈利·波特》：粒度闭环

七册中央 Work 均已存在且为 `read_status = 已读`，Batch030 复用既有实体完成 7 Work / 21 formal QX：

```text
哈利·波特与魔法石 → 3
哈利·波特与密室 → 3
哈利·波特与阿兹卡班的囚徒 → 3
哈利·波特与火焰杯 → 3
哈利·波特与凤凰社 → 3
哈利·波特与混血王子 → 3
哈利·波特与死亡圣器 → 3
```

```text
HARRY_POTTER_GRANULARITY = CLOSED
```

## 03｜《福尔摩斯探案全集》：60-unit reconciliation

个人完整阅读事实已确认。标准 canon：

```text
4 novels + 56 short stories = 60 independent narrative units
```

### 03.1｜四部长篇：完成

原中央 Work 均错误写为 `read_status = 未读`，现已依据全集阅读事实统一校正为 `已读` 并完成 QX：

```text
血字的研究 → 3
四签名 → 3
巴斯克维尔的猎犬 → 3
恐怖谷 → 3
```

```text
SHERLOCK_NOVELS_COMPLETE = 4
SHERLOCK_LONG_NOVEL_FORMAL_RELATIONS = 12
```

### 03.2｜《福尔摩斯历险记》12篇：完成

中央库此前没有这 12 个独立短篇 Work。Batch030 依据完整全集阅读事实建立最小中央实体，并逐篇通过 Admission Gate：

| 独立短篇 | 正式 QX | 关系数 |
|---|---|---:|
| 波希米亚丑闻 | 艾琳·艾德勒与国王的合影 | 1 |
| 红发会 | 红头发；地下隧道 | 2 |
| 身份案 | 打字信 | 1 |
| 博斯科姆比溪谷秘案 | 博斯科姆比溪谷水塘 | 1 |
| 五个橘核 | 五个橘核；K.K.K.匿名信 | 2 |
| 歪唇男人 | 歪嘴与乞丐面容；鸦片烟馆 | 2 |
| 蓝宝石案 | 蓝宝石；鹅 | 2 |
| 斑点带子案 | 沼地蝰蛇；通风孔与假铃绳 | 2 |
| 工程师大拇指案 | 被斩断的拇指；水压机 | 2 |
| 单身贵族案 | 婚礼 | 1 |
| 绿玉皇冠案 | 绿玉皇冠 | 1 |
| 铜山毛榉案 | 铜山毛榉宅邸；蓝色连衣裙 | 2 |

```text
SHERLOCK_ADVENTURES_STORIES = 12
SHERLOCK_ADVENTURES_FORMAL_QX_WORKS = 12
SHERLOCK_ADVENTURES_FORMAL_RELATIONS = 19
```

### 03.3｜精度说明

本组没有把“贝克街、烟斗、放大镜、华生手记”等系列标志物自动继承给所有短篇。QX 只记录在该独立叙事内部满足 `recurrent / structural / binding / distinctiveness` 至少两项，或符合 `singular_pivotal` 例外的对象。

因此：

```text
SHORT_STORY ≠ MUST_HAVE_MULTIPLE_QX
SERIES_ICON ≠ AUTOMATIC_STORY_QX
```

### 03.4｜剩余福尔摩斯任务

```text
CANON_TOTAL = 60
UNITS_COMPLETE = 16
SHORT_STORIES_COMPLETE = 12
SHORT_STORIES_REMAINING = 44
```

下一组按短篇集继续：

```text
福尔摩斯回忆录
→ story-level Work recovery
→ read_status = 已读
→ Admission Gate
→ FORMAL_QX / ZERO_QX
```

## 04｜《龙族》：全集已读，但版本边界仍不稳定

个人阅读事实明确为《龙族》全集已读；中央库当前仍只有系列父记录 `龙族.md`。原始出版、修订版、第三部上中下分册、第五部连载及后续重写存在不同粒度边界，因此继续保持：

```text
READ_SCOPE = COMPLETE_SERIES_CONFIRMED
QX_ON_SERIES_PARENT = PROHIBITED
VOLUME_MAP = DEFER_VERSION_BOUNDARY
```

## 05｜Batch030 当前状态

```text
SERIES_RECORDS_TOTAL = 3
SERIES_FULL_READ_FACT_CONFIRMED = 3

HARRY_POTTER = CLOSED
SHERLOCK_HOLMES = 16_OF_60_UNITS_QX_COMPLETE
DRAGON_RAJAS = DEFER_VERSION_BOUNDARY

FORMAL_WORKS_WITH_QX = 147
FORMAL_QX_RELATIONS = 420
```

## 06｜下一步

```text
Batch030-B2
→ 《福尔摩斯回忆录》story-level reading map + central Work recovery + QX

之后继续：
→ 《福尔摩斯归来记》
→ 《最后致意》
→ 《福尔摩斯案件簿》

Batch030-C
→ 龙族版本 / 卷级边界恢复
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次029]]
