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
14 reviewed = 12 FORMAL_QX + 2 ZERO_QX / 21 relations
ZERO_QX = [明天, 端午节]
NAHAN_STORY_LEVEL = CLOSED
```

## 03｜《彷徨》：11篇完成

```text
11 reviewed = 7 FORMAL_QX + 4 ZERO_QX / 10 relations
ZERO_QX = [幸福的家庭, 高老夫子, 弟兄, 离婚]
PANGHUANG_STORY_LEVEL = CLOSED
```

## 04｜《台北人》：14篇完成

```text
14 reviewed = 10 FORMAL_QX + 4 ZERO_QX / 11 relations
ZERO_QX = [思旧赋, 梁父吟, 满天里亮晶晶的星星, 冬夜]
TAIPEI_PEOPLE_STORY_LEVEL = CLOSED
```

核心对象：素白旗袍、军机、年夜饭、舞厅、红杜鹃花、《孤恋花》歌声、桂林米粉、一捧雪菊花、昆曲《游园惊梦》清唱与宴席、国葬仪式。

## 05｜《燃烧的原野》：17篇完成

```text
17 reviewed = 10 FORMAL_QX + 7 ZERO_QX / 13 relations
BURNING_PLAIN_STORY_LEVEL = CLOSED
```

ZERO_QX：

```text
那个人
清晨
叫他们别杀我！
他被单独留下的那个夜晚
记住
阿纳克莱托·莫罗内斯
玛蒂尔德·阿尔坎赫尔的遗产
```

核心对象包括：干旱平原、洪水中的河与母牛、塔尔帕朝圣路、燃烧的原野、卢维纳的风、父亲背负儿子的身体、北上边境之路、灾后公共宴会与演说场景。

## 06｜《夜晚的潜水艇》：9篇完成

父记录 `夜晚的潜水艇.md` 明确 `read_status = 已读`，按稳定九篇结构拆分。

| 独立短篇 | 状态 | 正式对象 | 关系数 |
|---|---|---|---:|
| 夜晚的潜水艇（短篇） | FORMAL_QX | 夜晚的潜水艇 | 1 |
| 竹峰寺 | FORMAL_QX | 竹峰寺 | 1 |
| 传彩笔 | FORMAL_QX | 彩笔 | 1 |
| 裁云记 | FORMAL_QX | 云 | 1 |
| 酿酒师 | FORMAL_QX | 酒 | 1 |
| 红楼梦弥撒 | FORMAL_QX | 《红楼梦》文本；弥撒仪式 | 2 |
| 李茵的湖 | FORMAL_QX | 湖 | 1 |
| 尺波 | ZERO_QX | — | 0 |
| 音乐家 | ZERO_QX | — | 0 |

```text
NIGHT_SUBMARINE_STORIES_REVIEWED = 9
NIGHT_SUBMARINE_FORMAL_QX_WORKS = 7
NIGHT_SUBMARINE_ZERO_QX_WORKS = 2
NIGHT_SUBMARINE_FORMAL_RELATIONS = 8
NIGHT_SUBMARINE_STORY_LEVEL = CLOSED
```

## 07｜Batch031 当前统计

```text
STORY_UNITS_REVIEWED = 65
STORY_FORMAL_QX_WORKS = 46
STORY_ZERO_QX_WORKS = 19
STORY_FORMAL_RELATIONS = 63

FORMAL_WORKS_WITH_QX_CURRENT = 235
FORMAL_QX_RELATIONS_CURRENT = 543
```

## 08｜精度规则继续生效

```text
COLLECTION_READ ≠ COLLECTION_LEVEL_QX
STORY_READ_MAP → SMALLEST_INDEPENDENT_NARRATIVE_UNIT
SHORT_STORY ≠ MUST_HAVE_QX
ATMOSPHERE_ONLY ≠ ADMISSION
TITLE_WORD ≠ AUTOMATIC_OBJECT
FICTIONAL_OBJECT = ALLOWED_IF_CONCRETE_AND_STRUCTURAL
```

## 09｜下一组

```text
人类的群星闪耀时 → NEXT
机器人短篇全集 → PENDING / 需稳定篇目边界
草 → PENDING / 文集粒度待恢复
哑舍 → PENDING
俗世奇人（足本） → PENDING
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次030]]
