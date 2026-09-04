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

Batch030 收口：

```text
HARRY_POTTER = CLOSED
SHERLOCK_HOLMES = CLOSED
DRAGON_RAJAS = DEFER_VERSION_BOUNDARY
```

《龙族》不再阻塞下游：现有个人材料没有卷名、版本、阅读时间；网络连载版与后续修订 / 重写边界不稳定，因此保持 deferred，不猜测。

```text
FORMAL_WORKS_WITH_QX_BEFORE_BATCH031 = 189
FORMAL_QX_RELATIONS_BEFORE_BATCH031 = 480
```

## 02｜《呐喊》：14篇完成

父记录：

```text
呐喊.md
read_status = 已读
```

拆分标准小说单元 14 篇：

| 独立短篇 | 状态 | 正式对象 | 关系数 |
|---|---|---|---:|
| 狂人日记 | FORMAL_QX | 月光 | 1 |
| 孔乙己 | FORMAL_QX | 长衫；茴香豆 | 2 |
| 药 | FORMAL_QX | 人血馒头；坟上的花环 | 2 |
| 明天 | ZERO_QX | — | 0 |
| 一件小事 | FORMAL_QX | 人力车 | 1 |
| 头发的故事 | FORMAL_QX | 辫子与剪发后的头发 | 1 |
| 风波 | FORMAL_QX | 辫子 | 1 |
| 故乡 | FORMAL_QX | 月下西瓜地；银项圈 | 2 |
| 阿Q正传 | FORMAL_QX | 辫子；认罪状上的圆圈 | 2 |
| 端午节 | ZERO_QX | — | 0 |
| 白光 | FORMAL_QX | 白光；地下银子 / 财宝 | 2 |
| 兔和猫 | FORMAL_QX | 白兔；黑猫 | 2 |
| 鸭的喜剧 | FORMAL_QX | 鸭子；蝌蚪 | 2 |
| 社戏 | FORMAL_QX | 航船；社戏戏台；罗汉豆 | 3 |

```text
NAHAN_STORIES_REVIEWED = 14
NAHAN_FORMAL_QX_WORKS = 12
NAHAN_ZERO_QX_WORKS = 2
NAHAN_FORMAL_RELATIONS = 21
NAHAN_STORY_LEVEL = CLOSED
```

ZERO_QX：

```text
明天
端午节
```

## 03｜《彷徨》：11篇完成

父记录：

```text
彷徨.md
read_status = 已读
```

| 独立短篇 | 状态 | 正式对象 | 关系数 |
|---|---|---|---:|
| 祝福 | FORMAL_QX | 土地庙门槛；额角伤疤 | 2 |
| 在酒楼上 | FORMAL_QX | 酒楼窗外的废园与老梅 | 1 |
| 幸福的家庭 | ZERO_QX | — | 0 |
| 肥皂 | FORMAL_QX | 肥皂 | 1 |
| 长明灯 | FORMAL_QX | 长明灯；庙宇 | 2 |
| 示众 | FORMAL_QX | 街头示众场景 | 1 |
| 高老夫子 | ZERO_QX | — | 0 |
| 孤独者 | FORMAL_QX | 棺材与丧葬 | 1 |
| 伤逝 | FORMAL_QX | 阿随；油鸡 | 2 |
| 弟兄 | ZERO_QX | — | 0 |
| 离婚 | ZERO_QX | — | 0 |

```text
PANGHUANG_STORIES_REVIEWED = 11
PANGHUANG_FORMAL_QX_WORKS = 7
PANGHUANG_ZERO_QX_WORKS = 4
PANGHUANG_FORMAL_RELATIONS = 10
PANGHUANG_STORY_LEVEL = CLOSED
```

## 04｜Batch031 当前统计

```text
STORY_UNITS_REVIEWED = 25
STORY_FORMAL_QX_WORKS = 19
STORY_ZERO_QX_WORKS = 6
STORY_FORMAL_RELATIONS = 31

FORMAL_WORKS_WITH_QX_CURRENT = 208
FORMAL_QX_RELATIONS_CURRENT = 511
```

## 05｜精度规则继续生效

```text
COLLECTION_READ ≠ COLLECTION_LEVEL_QX
STORY_READ_MAP → SMALLEST_INDEPENDENT_NARRATIVE_UNIT
SHORT_STORY ≠ MUST_HAVE_QX
ATMOSPHERE_ONLY ≠ ADMISSION
TITLE_WORD ≠ AUTOMATIC_OBJECT
```

## 06｜下一组

```text
台北人 → 14 stable author short stories → NEXT
燃烧的原野 → stable author story collection → PENDING
```

其余需要单独版本 / 结构治理：

```text
夜晚的潜水艇
机器人短篇全集
草
人类的群星闪耀时
哑舍
俗世奇人（足本）
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次030]]
