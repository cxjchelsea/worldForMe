---
id: WL-QX-FORMAL-ANNOTATION-031
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次031
code: QX-ANNOTATION-031
axis: Q
facet: QX
status: ACTIVE_STORY_LEVEL_RECONCILIATION
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次031

> Batch031 进入稳定作者文集 / 短篇集的 `STORY-LEVEL READING MAP`。父级 collection 保留阅读事实，但不承载跨篇 QX；正式关系只写入最小独立叙事单元。

## 01｜前置状态

```text
HARRY_POTTER = CLOSED
SHERLOCK_HOLMES = CLOSED
DRAGON_RAJAS = DEFER_VERSION_BOUNDARY
FORMAL_WORKS_WITH_QX_BEFORE_BATCH031 = 189
FORMAL_QX_RELATIONS_BEFORE_BATCH031 = 480
```

## 02｜《呐喊》：14篇完成

```text
NAHAN_STORIES_REVIEWED = 14
NAHAN_FORMAL_QX_WORKS = 12
NAHAN_ZERO_QX_WORKS = 2
NAHAN_FORMAL_RELATIONS = 21
NAHAN_STORY_LEVEL = CLOSED
ZERO_QX = [明天, 端午节]
```

## 03｜《彷徨》：11篇完成

```text
PANGHUANG_STORIES_REVIEWED = 11
PANGHUANG_FORMAL_QX_WORKS = 7
PANGHUANG_ZERO_QX_WORKS = 4
PANGHUANG_FORMAL_RELATIONS = 10
PANGHUANG_STORY_LEVEL = CLOSED
ZERO_QX = [幸福的家庭, 高老夫子, 弟兄, 离婚]
```

## 04｜《台北人》：14篇完成

父记录 `台北人.md` 已确认 `read_status = 已读`，按稳定作者短篇集拆为 14 个独立叙事单元。

| 独立短篇 | 状态 | 正式对象 | 关系数 |
|---|---|---|---:|
| 永远的尹雪艳 | FORMAL_QX | 素白旗袍 | 1 |
| 一把青 | FORMAL_QX | 军机 | 1 |
| 岁除 | FORMAL_QX | 年夜饭 | 1 |
| 金大班的最后一夜 | FORMAL_QX | 舞厅 | 1 |
| 那片血一般红的杜鹃花 | FORMAL_QX | 红杜鹃花 | 1 |
| 思旧赋 | ZERO_QX | — | 0 |
| 梁父吟 | ZERO_QX | — | 0 |
| 孤恋花 | FORMAL_QX | 《孤恋花》歌声 | 1 |
| 花桥荣记 | FORMAL_QX | 桂林米粉 | 1 |
| 秋思 | FORMAL_QX | 一捧雪菊花 | 1 |
| 满天里亮晶晶的星星 | ZERO_QX | — | 0 |
| 游园惊梦 | FORMAL_QX | 昆曲《游园惊梦》清唱；宴席 | 2 |
| 冬夜 | ZERO_QX | — | 0 |
| 国葬 | FORMAL_QX | 国葬仪式 | 1 |

```text
TAIPEI_PEOPLE_STORIES_REVIEWED = 14
TAIPEI_PEOPLE_FORMAL_QX_WORKS = 10
TAIPEI_PEOPLE_ZERO_QX_WORKS = 4
TAIPEI_PEOPLE_FORMAL_RELATIONS = 11
TAIPEI_PEOPLE_STORY_LEVEL = CLOSED
```

ZERO_QX：

```text
思旧赋
梁父吟
满天里亮晶晶的星星
冬夜
```

## 05｜Batch031 当前统计

```text
STORY_UNITS_REVIEWED = 39
STORY_FORMAL_QX_WORKS = 29
STORY_ZERO_QX_WORKS = 10
STORY_FORMAL_RELATIONS = 42

FORMAL_WORKS_WITH_QX_CURRENT = 218
FORMAL_QX_RELATIONS_CURRENT = 522
```

## 06｜精度规则继续生效

```text
COLLECTION_READ ≠ COLLECTION_LEVEL_QX
STORY_READ_MAP → SMALLEST_INDEPENDENT_NARRATIVE_UNIT
SHORT_STORY ≠ MUST_HAVE_QX
ATMOSPHERE_ONLY ≠ ADMISSION
TITLE_WORD ≠ AUTOMATIC_OBJECT
```

## 07｜下一组

```text
燃烧的原野 → stable author story collection → NEXT
夜晚的潜水艇 → PENDING
机器人短篇全集 → PENDING / 需稳定篇目边界
草 → PENDING / 文集粒度待恢复
人类的群星闪耀时 → PENDING
哑舍 → PENDING
俗世奇人（足本） → PENDING
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次030]]
