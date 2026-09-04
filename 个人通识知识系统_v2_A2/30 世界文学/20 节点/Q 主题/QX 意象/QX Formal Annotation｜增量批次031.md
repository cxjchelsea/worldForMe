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

```text
TAIPEI_PEOPLE_STORIES_REVIEWED = 14
TAIPEI_PEOPLE_FORMAL_QX_WORKS = 10
TAIPEI_PEOPLE_ZERO_QX_WORKS = 4
TAIPEI_PEOPLE_FORMAL_RELATIONS = 11
TAIPEI_PEOPLE_STORY_LEVEL = CLOSED
ZERO_QX = [思旧赋, 梁父吟, 满天里亮晶晶的星星, 冬夜]
```

核心正式对象包括：

```text
永远的尹雪艳 → 素白旗袍
一把青 → 军机
岁除 → 年夜饭
金大班的最后一夜 → 舞厅
那片血一般红的杜鹃花 → 红杜鹃花
孤恋花 → 《孤恋花》歌声
花桥荣记 → 桂林米粉
秋思 → 一捧雪菊花
游园惊梦 → 昆曲清唱；宴席
国葬 → 国葬仪式
```

## 05｜《燃烧的原野》：17篇完成

父记录 `燃烧的原野.md` 已确认 `read_status = 已读`。按作者稳定短篇集拆为 17 个独立叙事单元；父记录继续只作为 collection-level 阅读事实。

| 独立短篇 | 状态 | 正式对象 | 关系数 |
|---|---|---|---:|
| 马卡里奥 | FORMAL_QX | 青蛙 | 1 |
| 他们给了我们土地 | FORMAL_QX | 干旱平原 | 1 |
| 科马德雷斯坡 | FORMAL_QX | 科马德雷斯坡 | 1 |
| 我们真的很穷 | FORMAL_QX | 洪水中的河；塞尔佩蒂娜母牛 | 2 |
| 那个人 | ZERO_QX | — | 0 |
| 清晨 | ZERO_QX | — | 0 |
| 塔尔帕 | FORMAL_QX | 去塔尔帕的朝圣路；塔尔帕圣母像 | 2 |
| 燃烧的原野（短篇） | FORMAL_QX | 燃烧的原野 | 1 |
| 叫他们别杀我！ | ZERO_QX | — | 0 |
| 卢维纳 | FORMAL_QX | 卢维纳的风；卢维纳荒山与小镇 | 2 |
| 他被单独留下的那个夜晚 | ZERO_QX | — | 0 |
| 记住 | ZERO_QX | — | 0 |
| 你听不到狗叫吗？ | FORMAL_QX | 父亲背负儿子的身体 | 1 |
| 北方通道 | FORMAL_QX | 北上边境之路 | 1 |
| 阿纳克莱托·莫罗内斯 | ZERO_QX | — | 0 |
| 玛蒂尔德·阿尔坎赫尔的遗产 | ZERO_QX | — | 0 |
| 山崩那天 | FORMAL_QX | 灾后公共宴会与演说场景 | 1 |

```text
BURNING_PLAIN_STORIES_REVIEWED = 17
BURNING_PLAIN_FORMAL_QX_WORKS = 10
BURNING_PLAIN_ZERO_QX_WORKS = 7
BURNING_PLAIN_FORMAL_RELATIONS = 13
BURNING_PLAIN_STORY_LEVEL = CLOSED
```

## 06｜Batch031 当前统计

```text
STORY_UNITS_REVIEWED = 56
STORY_FORMAL_QX_WORKS = 39
STORY_ZERO_QX_WORKS = 17
STORY_FORMAL_RELATIONS = 55

FORMAL_WORKS_WITH_QX_CURRENT = 228
FORMAL_QX_RELATIONS_CURRENT = 535
```

## 07｜精度规则继续生效

```text
COLLECTION_READ ≠ COLLECTION_LEVEL_QX
STORY_READ_MAP → SMALLEST_INDEPENDENT_NARRATIVE_UNIT
SHORT_STORY ≠ MUST_HAVE_QX
ATMOSPHERE_ONLY ≠ ADMISSION
TITLE_WORD ≠ AUTOMATIC_OBJECT
```

## 08｜下一组

```text
夜晚的潜水艇 → NEXT
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
