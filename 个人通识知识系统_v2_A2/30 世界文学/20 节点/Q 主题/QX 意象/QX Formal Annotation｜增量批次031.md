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

> Batch031 处理稳定作者文集 / 短篇集的 `STORY-LEVEL READING MAP`。父级 collection 只保留阅读事实；正式 QX 只写入最小独立叙事单元。

## 01｜前置状态

```text
HARRY_POTTER = CLOSED
SHERLOCK_HOLMES = CLOSED
DRAGON_RAJAS = DEFER_VERSION_BOUNDARY
FORMAL_WORKS_WITH_QX_BEFORE_BATCH031 = 189
FORMAL_QX_RELATIONS_BEFORE_BATCH031 = 480
```

## 02｜已完成稳定短篇集

```text
呐喊 = 14 reviewed = 12 FORMAL_QX + 2 ZERO_QX / 21 relations
彷徨 = 11 reviewed = 7 FORMAL_QX + 4 ZERO_QX / 10 relations
台北人 = 14 reviewed = 10 FORMAL_QX + 4 ZERO_QX / 11 relations
燃烧的原野 = 17 reviewed = 10 FORMAL_QX + 7 ZERO_QX / 13 relations
夜晚的潜水艇 = 9 reviewed = 7 FORMAL_QX + 2 ZERO_QX / 8 relations
```

## 03｜《机器人短篇全集》：32篇完成

中央父记录明确说明：个人阅读事实对应“机器人短篇合集”，不能由《我，机器人》《钢穴》等分卷实体反推。公开书目交叉核验后，同名中文合集稳定收录32篇，因此建立 32-unit reading map。

```text
COMPLETE_ROBOT_STORIES_REVIEWED = 32
COMPLETE_ROBOT_FORMAL_QX_WORKS = 22
COMPLETE_ROBOT_ZERO_QX_WORKS = 10
COMPLETE_ROBOT_FORMAL_RELATIONS = 24
COMPLETE_ROBOT_STORY_LEVEL = CLOSED
```

ZERO_QX：

```text
观点
思考！
天堂异乡人
当我们同在一起
镜像
第一法则
转圈圈
抓兔子
证据
汝竟顾念他
```

代表性正式对象：

```text
孩子最好的朋友 → 机器狗罗比特
莎莉 → 自动驾驶汽车莎莉
总有一天 → 老式故事电脑“吟游诗人”
真爱 → 计算机乔
AL-76号走失记 → AL-76号机器人
光雕 → 光雕作品
分离主义者 → 人工心脏
理性 → 能源转换器
骗子！ → 读心机器人赫比
校工 → 学术校样
消失无踪 → 一群外形相同的NS-2机器人
逃避 → 超级计算机“脑”；超空间飞船
可避免的冲突 → 全球机器系统
机器人之梦 → 梦境记录与正电子脑波形
正电子人 → 安德鲁的木雕；不断更换的人造身体
```

关键控制：

```text
ROBOT_THEME ≠ AUTOMATIC_OBJECT
GENERIC_ROBOT ≠ FORMAL_QX
SPECIFIC_MACHINE_BODY_OR_MEDIUM = ADMIT_ONLY_IF_STRUCTURAL
```

## 04｜当前无法安全拆分的项目

### 《人类的群星闪耀时》

版本史存在 5 / 12 / 14 篇等不同收录形态；中央个人记录没有出版社、ISBN或目录。

```text
STATUS = DEFER_COLLECTION_VERSION
READ_FACT = 已读整本
STORY_MAP = PROHIBITED_UNTIL_VERSION_RESOLVED
```

### 《草》

公开书目信息确认它是从《一座城池》《光荣日》《他的国》《杂的文》中摘取片段的精选集，不是稳定的独立短篇小说集。

```text
STATUS = DEFER_EXCERPT_COLLECTION
PARENT_TYPE_NEEDS_UPSTREAM_FIX = TRUE
STORY_LEVEL_QX = NOT_APPLICABLE_WITHOUT_EXCERPT_MAP
```

### 《哑舍》

中央记录只有系列父名“哑舍”，没有具体卷。

```text
STATUS = DEFER_SERIES_GRANULARITY
QX_ON_SERIES_PARENT = PROHIBITED
```

### 《俗世奇人》/《俗世奇人（足本）》

现中央父记录规范名为《俗世奇人》，而已读覆盖层曾记作《俗世奇人（足本）》；公开出版史存在旧版、足本以及后续新增本。

```text
STATUS = DEFER_COLLECTION_VERSION
READ_FACT = 已读
STORY_MAP = WAIT_FOR_EDITION_RECONCILIATION
```

## 05｜Batch031 当前统计

```text
STORY_UNITS_REVIEWED = 97
STORY_FORMAL_QX_WORKS = 68
STORY_ZERO_QX_WORKS = 29
STORY_FORMAL_RELATIONS = 87

FORMAL_WORKS_WITH_QX_CURRENT = 257
FORMAL_QX_RELATIONS_CURRENT = 567
```

## 06｜精度规则继续生效

```text
COLLECTION_READ ≠ COLLECTION_LEVEL_QX
STORY_READ_MAP → SMALLEST_INDEPENDENT_NARRATIVE_UNIT
SHORT_STORY ≠ MUST_HAVE_QX
ATMOSPHERE_ONLY ≠ ADMISSION
TITLE_WORD ≠ AUTOMATIC_OBJECT
FICTIONAL_OBJECT = ALLOWED_IF_CONCRETE_AND_STRUCTURAL
VERSION_AMBIGUITY = DEFER, NOT GUESS
```

## 07｜下一阶段

```text
Batch031 stable story-level loop = NEAR_EXHAUSTED
NEXT = resolve edition / TOC blockers where external or upstream evidence can uniquely identify version
THEN = editorial collections
FINALLY = corpus coverage recount
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次030]]
