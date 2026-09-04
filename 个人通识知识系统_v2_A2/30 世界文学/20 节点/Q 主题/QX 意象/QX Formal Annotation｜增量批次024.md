---
id: WL-QX-FORMAL-ANNOTATION-024
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次024
code: QX-ANNOTATION-024
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次024

> 本批继续连续循环，并把“无正式关系”的原因拆成三类：QX=0、独立叙事合集延期、中央 Work 路径未解析。

## 01｜已解析 Work 的批次结果

| 作品 | 正式 QX 关系数 | 结论 |
|---|---:|---|
| 《文城》 | 1 | 文城 / 被寻找的城 |
| 《太白金星有点烦》 | 1 | 公文 / 奏报 / 批文 |
| 《花千骨》 | 3 | 长留山 / 绝情殿；绝情池水；断念剑 |
| 《三生三世十里桃花》 | 3 | 十里桃林 / 桃花；诛仙台；被夺去的双眼 / 眼睛 |
| 《华胥引》 | 2 | 华胥引 / 琴曲；华胥幻境 / 梦境 |
| 《我胆小如鼠》 | 0 | 本轮无对象通过 Admission Gate |
| 《凉生我们可不可以不忧伤》 | 0 | 本轮无高置信整本物象 |
| 《夏有乔木雅望天堂》 | 0 | 标题中的“乔木 / 天堂”不直接准入 |
| 《人类的群星闪耀时》 | deferred | 多篇历史微型传记，默认按独立篇章处理 |
| 《哑舍》 | deferred | 连缀式独立物件故事，需篇章级审查 |

```text
BATCH_024_RESOLVED_WORKS = 10
BATCH_024_WORKS_WITH_FORMAL_QX = 5
BATCH_024_ZERO_QX_WORKS = 3
BATCH_024_DEFERRED_MULTI_NARRATIVE = 2
BATCH_024_FORMAL_RELATIONS = 10
FORMAL_QX_RELATIONS_BEFORE = 344
FORMAL_QX_RELATIONS_AFTER = 354
FORMAL_WORKS_WITH_QX_BEFORE = 110
FORMAL_WORKS_WITH_QX_AFTER = 115
```

## 02｜中央 Work 路径未解析

已读审计中明确属于文学地图，但当前分支按标准化标题无法取得中央 Work：

```text
我的一个世纪
你当像鸟飞往你的山
看见
天才在左，疯子在右
```

它们登记为：

```text
STATUS = CENTRAL_WORK_MISSING_OR_PATH_UNRESOLVED
```

这不是 QX=0，也不是作品不适合标注；在中央 Work 身份解决前不猜文件名、不创建重复实体。

## 03｜网络 / 类型文学继续使用同一 Gate

本批《花千骨》《三生三世十里桃花》《华胥引》形成较高密度 QX，是因为作品内部存在稳定的：

```text
关系绑定器物
超自然阈限空间
身体损伤
反复进入的幻境
```

而不是因为网络奇幻作品天然“意象多”。

相反，《凉生我们可不可以不忧伤》《夏有乔木雅望天堂》仍可合法为 0。

## 04｜标题与正式 object 的边界

《文城》中的“文城”能够准入，并不是因为它在标题里，而是因为“寻找文城”持续规定人物的移动、追索和结构目标。

同理：

```text
十里桃花 → 正文中有反复出现的十里桃林空间
华胥引 → 正文中是反复实际运作的琴曲媒介
夏有乔木雅望天堂 → 暂无足够证据把标题词直接升级成整本 QX
```

## 05｜合集 / 连缀叙事继续延期

新增：

```text
人类的群星闪耀时
哑舍
```

与既有：

```text
夜晚的潜水艇
机器人短篇全集
草
```

进入同一篇章级 / 独立叙事级待审队列。

## 06｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 354
FORMAL_WORKS_WITH_QX = 115
FULL_CORPUS_AUDIT = DEFERRED
NEXT_BATCH = 025
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次023]]
