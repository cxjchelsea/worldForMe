---
id: WL-QX-FORMAL-ANNOTATION-031
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次031
code: QX-ANNOTATION-031
axis: Q
facet: QX
status: COMPLETE_STORY_LEVEL_AND_SCOPE_RECONCILIATION
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次031

> Batch031 完成稳定短篇集的 story-level 审查，并在后半程依据个人体系目标修正完成标准：短篇 / 编辑型选集不再默认要求逐篇 QX；只有高价值且阅读事实可确认的独立短篇才进入正式关系。

## 01｜前置状态

```text
FORMAL_WORKS_WITH_QX_BEFORE_BATCH031 = 189
FORMAL_QX_RELATIONS_BEFORE_BATCH031 = 480
```

## 02｜已完成的稳定短篇集

```text
呐喊 = 14 reviewed = 12 FORMAL + 2 ZERO / 21 relations
彷徨 = 11 reviewed = 7 FORMAL + 4 ZERO / 10 relations
台北人 = 14 reviewed = 10 FORMAL + 4 ZERO / 11 relations
燃烧的原野 = 17 reviewed = 10 FORMAL + 7 ZERO / 13 relations
夜晚的潜水艇 = 9 reviewed = 7 FORMAL + 2 ZERO / 8 relations
机器人短篇全集 = 32 reviewed = 22 FORMAL + 10 ZERO / 24 relations
```

```text
STORY_UNITS_REVIEWED = 97
STORY_FORMAL_QX_WORKS = 68
STORY_ZERO_QX_WORKS = 29
STORY_FORMAL_RELATIONS = 87
```

## 03｜短篇完成标准修正

从本批尾部开始，QX 不再把“每个已读短篇都必须经过逐篇 Gate”作为完整性要求。

```text
SHORT_FORM_DEFAULT = SELECTIVE_REVIEW
```

进入 story-level QX 的短篇应至少符合以下之一：

```text
1. 存在 dominant / core 级高辨识物象
2. 标题指向具体对象，且该对象确实承担结构作用
3. 该物象具有明显跨作品比较价值
4. 该短篇本身是个人阅读中的重要独立作品
```

因此：

```text
SHORT_STORY ≠ MANDATORY_QX_UNIT
EDITORIAL_COLLECTION ≠ MANDATORY_STORY_MAP
ZERO_QX_SHORT_STORY ≠ COVERAGE_GAP
```

## 04｜系列范围不完整时的受控处理

### 《龙族》

个人阅读事实确认到“全集已读”，但无法恢复统一分卷 / 版本边界。允许建立：

```text
SERIES_SCOPE_QX
```

但只记录跨卷、跨版本稳定成立的对象：

```text
黄金瞳 → QX9
卡塞尔学院 → QX7
尼伯龙根 → QX19
```

```text
DRAGON_RAJAS = CLOSED_SERIES_SCOPE
FORMAL_RELATIONS = 3
```

### 《哑舍》

具体卷级阅读范围未知，因此只允许记录无论阅读到哪一卷都成立的范围无关核心对象：

```text
哑舍古董店 → QX7 / dominant
```

```text
YASHE = CLOSED_SCOPE_INVARIANT
FORMAL_RELATIONS = 1
```

不推断任何具体卷器物。

## 05｜不再作为 QX 强制拆分对象的已读记录

以下记录已经完成“是否需要 QX”的判断，但不再要求恢复完整目录：

```text
人类的群星闪耀时
→ 历史小品合集；版本目录差异不影响 QX 完成性
→ REVIEWED_NO_QX_REQUIRED_COLLECTION

草
→ 摘录 / 精选集，不是稳定独立叙事集合
→ REVIEWED_NO_QX_REQUIRED_EXCERPT_COLLECTION

俗世奇人（足本）
→ 多人物短篇集合；具体版本差异不再构成 QX 必做缺口
→ REVIEWED_NO_QX_REQUIRED_SHORT_FORM_COLLECTION

麦琪的礼物：欧·亨利短篇小说经典
莫泊桑短篇小说精选
欧·亨利短篇小说选
契诃夫短篇小说选
项链：莫泊桑中短篇小说选
→ 编辑型短篇选集
→ REVIEWED_NO_QX_REQUIRED_EDITORIAL_COLLECTION
```

这不表示这些书“没有文学意象”，而是表示：为个人 QX 跨作品比较系统，不值得为了完整覆盖去重建每一版目录并逐篇抽取。

## 06｜Batch031 最终统计

```text
STORY_LEVEL_FORMAL_QX_WORKS = 68
STORY_LEVEL_ZERO_QX_WORKS = 29
STORY_LEVEL_FORMAL_RELATIONS = 87
SERIES_SCOPE_FORMAL_WORKS_ADDED = 2
SERIES_SCOPE_FORMAL_RELATIONS_ADDED = 4

FORMAL_WORKS_WITH_QX_CURRENT = 259
FORMAL_QX_RELATIONS_CURRENT = 571
```

## 07｜完成性定义

已读书目的 QX 完成不再等于“每一个最小短篇都标过”，而定义为：

```text
每条已读记录
→ 已判断是否属于 QX 必审对象
→ 需要 QX 的作品：FORMAL_QX / ZERO_QX / controlled scope QX
→ 不值得为 QX 继续拆分的短篇 / 选集：REVIEWED_NO_QX_REQUIRED
→ 不允许存在未判断的普通单本作品
```

```text
BATCH031 = CLOSED
NEXT = FINAL_READ_CORPUS_COVERAGE_AUDIT
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Version Reconciliation｜版本阻塞项证据台账]]
- [[QX Formal Annotation｜增量批次030]]
