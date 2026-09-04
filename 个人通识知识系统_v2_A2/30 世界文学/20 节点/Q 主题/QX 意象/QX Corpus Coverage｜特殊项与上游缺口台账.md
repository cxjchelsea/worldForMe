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

> 目的：记录没有直接进入 Work-level 正式 QX 的特殊粒度、版本与上游原因，并维护当前审查断点。

## 01｜状态定义

```text
FORMAL_QX = Work 已核实为实际阅读单元，且至少一条关系通过 Admission Gate
ZERO_QX = Work 已核实为实际阅读单元，也完成 QX 审查，但没有对象通过 Gate
DEFER_STORY_LEVEL = 阅读事实对应短篇集 / 多独立叙事，需要篇章级处理
DEFER_SERIES_GRANULARITY = 系列总称或版本 / 卷级边界尚无法稳定映射
DEFER_EDITORIAL_COLLECTION = 编辑型选集 / 精选，目录依版本变化
ONE_TO_MANY_RECONCILIATION = 一条阅读记录实际映射多个 Work
UPSTREAM_WORK_BUILD_GAP = 已读覆盖层要求创建中央 Work，但当前没有可复用 Work
```

## 02｜系列 / 全集粒度

| 读书记录 | 状态 | 当前结论 |
|---|---|---|
| 福尔摩斯探案全集 | CLOSED | 60 units 全部审查；58 FORMAL_QX + 2 ZERO_QX / 91 relations |
| 哈利·波特 | CLOSED | 7 child Works / 21 formal relations |
| 龙族 | DEFER_VERSION_BOUNDARY | 系列已读事实保留；个人材料不足以确定网文 / 单行本 / 修订重写卷级边界，不猜测 |

```text
SERIES_RECONCILIATION_BLOCKING = NO
```

## 03｜稳定作者短篇集 / 文集

| 父级阅读记录 | 当前状态 | story-level 结果 |
|---|---|---|
| 呐喊 | CLOSED | 14 = 12 FORMAL_QX + 2 ZERO_QX / 21 relations |
| 彷徨 | CLOSED | 11 = 7 FORMAL_QX + 4 ZERO_QX / 10 relations |
| 台北人 | CLOSED | 14 = 10 FORMAL_QX + 4 ZERO_QX / 11 relations |
| 燃烧的原野 | CLOSED | 17 = 10 FORMAL_QX + 7 ZERO_QX / 13 relations |
| 夜晚的潜水艇 | CURRENT | 待 story-level map |
| 机器人短篇全集 | PENDING | 需先稳定具体篇目边界 |
| 草 | PENDING | 文集粒度待恢复 |
| 人类的群星闪耀时 | PENDING | 多独立历史叙事 |
| 哑舍 | PENDING | 连缀式器物故事 |
| 俗世奇人（足本） | PENDING | 多人物独立故事 |

## 04｜已闭环的一对多记录

```text
哈利·波特 = 7 FORMAL_QX / 21 relations / CLOSED
福尔摩斯探案全集 = 58 FORMAL_QX + 2 ZERO_QX / 91 relations / CLOSED
```

稳定短篇集 ZERO_QX 汇总：

```text
呐喊 = [明天, 端午节]
彷徨 = [幸福的家庭, 高老夫子, 弟兄, 离婚]
台北人 = [思旧赋, 梁父吟, 满天里亮晶晶的星星, 冬夜]
燃烧的原野 = [那个人, 清晨, 叫他们别杀我！, 他被单独留下的那个夜晚, 记住, 阿纳克莱托·莫罗内斯, 玛蒂尔德·阿尔坎赫尔的遗产]
```

## 05｜上游 Work 建库缺口

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_FORMAL_QX = 7
UPSTREAM_ZERO_QX = 3
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 06｜编辑型选集：仍需版本目录

```text
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
```

统一状态：`DEFER_EDITORIAL_COLLECTION`。

## 07｜当前处理顺序

```text
1. UPSTREAM_WORK_BUILD_GAP → CLOSED
2. SERIES / VOLUME GRANULARITY
   - 哈利·波特 → CLOSED
   - 福尔摩斯探案全集 → CLOSED
   - 龙族 → DEFER_VERSION_BOUNDARY / NON-BLOCKING
3. STORY-LEVEL READING MAP
   - 呐喊 → CLOSED
   - 彷徨 → CLOSED
   - 台北人 → CLOSED
   - 燃烧的原野 → CLOSED
   - 夜晚的潜水艇 → CURRENT
4. 其余稳定 / 半稳定文集逐项恢复
5. 编辑型选集版本目录 / 实际读篇
6. 最终 corpus coverage recount
```

## 08｜当前正式 QX 基线

截至 Batch031《燃烧的原野》收口：

```text
FORMAL_WORKS_WITH_QX = 228
FORMAL_QX_RELATIONS = 535
STORY_LEVEL_UNITS_REVIEWED_BATCH031 = 56
STORY_LEVEL_FORMAL_QX_WORKS_BATCH031 = 39
STORY_LEVEL_ZERO_QX_BATCH031 = 17
STORY_LEVEL_NEW_RELATIONS_BATCH031 = 55
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
```

> ZERO_QX 已完成审查但不进入 FORMAL_WORKS_WITH_QX；父级 collection 和 series 也不作为独立 QX Work 计数。

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次030]]
- [[QX Formal Annotation｜增量批次031]]
