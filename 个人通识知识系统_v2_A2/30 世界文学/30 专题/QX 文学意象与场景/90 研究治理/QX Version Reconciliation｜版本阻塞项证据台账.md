---
id: WL-QX-VERSION-RECONCILIATION
type: literature_qx_governance
name: QX Version Reconciliation｜版本阻塞项证据台账
axis: Q
facet: QX
status: CLOSED_FOR_QX
---

# QX Version Reconciliation｜版本阻塞项证据台账

> 目的：记录版本不稳定的已读条目在 QX 中如何安全处置。最终原则不是强行恢复每个目录，而是判断该记录是否值得为了 QX 继续拆分。

## 01｜最终策略

```text
VERSION_AMBIGUITY + QX_HIGH_VALUE
→ 尽可能做 scope-invariant / series-scope QX

VERSION_AMBIGUITY + SHORT_FORM_OR_EDITORIAL_COLLECTION
→ REVIEWED_NO_QX_REQUIRED

VERSION_AMBIGUITY ≠ AUTOMATIC_COVERAGE_GAP
```

## 02｜《龙族》

个人事实：全集已读；分卷 / 网文 / 修订边界不稳定。

最终：

```text
STATUS = FORMAL_QX_SERIES_SCOPE
```

只保留跨卷稳定意象：

```text
黄金瞳
卡塞尔学院
尼伯龙根
```

不记录任何单卷专属对象。

## 03｜《哑舍》

个人事实：已读，但具体卷级范围未知。

最终：

```text
STATUS = FORMAL_QX_SCOPE_INVARIANT
```

只保留范围无关核心对象：

```text
哑舍古董店
```

不推断具体卷中的器物。

## 04｜《人类的群星闪耀时》

版本史存在 5 / 12 / 14 篇等不同收录形态；个人记录没有出版社 / ISBN / 目录。

最终：

```text
STATUS = REVIEWED_NO_QX_REQUIRED_COLLECTION
```

理由：历史小品合集不值得为了 QX 完整性恢复具体版本目录。若未来某一篇因独立阅读价值需要进入 QX，可单篇追加。

## 05｜《草》｜韩寒

公开书目信息确认它是从其他作品中摘取片段的精选集，而非稳定独立叙事集合。

最终：

```text
STATUS = REVIEWED_NO_QX_REQUIRED_EXCERPT_COLLECTION
STORY_LEVEL_QX = NOT_REQUIRED
PARENT_METADATA_UPSTREAM_FIX_NEEDED = TRUE
```

QX 不因上游体裁元数据问题而继续拆分摘录。

## 06｜《俗世奇人》/《俗世奇人（足本）》

旧版、足本与后续增补版存在篇目边界差异。

最终：

```text
STATUS = REVIEWED_NO_QX_REQUIRED_SHORT_FORM_COLLECTION
```

不再把恢复具体版本目录视为 QX 完成条件。

## 07｜五本编辑型外国短篇选集

```text
麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
```

最终统一：

```text
STATUS = REVIEWED_NO_QX_REQUIRED_EDITORIAL_COLLECTION
```

说明：

- 《麦琪的礼物：欧·亨利短篇小说经典》可锁定至少一个2003年上海社会科学院出版社版本，但完整目录仍未安全恢复；
- 其余选集存在多个同名 / 近同名版本；
- 在短篇选择性审查规则下，不值得仅为 QX 完整性继续做版本目录工程。

若未来独立短篇因高辨识意象进入专题，可按“确认读过该篇 + Admission Gate”单独追加。

## 08｜已解除阻塞的《机器人短篇全集》

```text
32 reviewed
22 FORMAL_QX
10 ZERO_QX
24 relations
STATUS = CLOSED
```

## 09｜版本治理最终状态

```text
MANDATORY_VERSION_BLOCKERS = 0
OPTIONAL_BIBLIOGRAPHIC_BLOCKERS = remain outside QX completeness
VERSION_RECONCILIATION_FOR_QX = CLOSED
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次031]]
