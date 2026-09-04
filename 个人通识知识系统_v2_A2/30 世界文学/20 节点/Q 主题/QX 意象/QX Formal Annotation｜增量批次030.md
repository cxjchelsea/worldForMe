---
id: WL-QX-FORMAL-ANNOTATION-030
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次030
code: QX-ANNOTATION-030
axis: Q
facet: QX
status: SERIES_RECONCILIATION_SHERLOCK_CLOSED
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次030

> 本批处理 `SERIES / VOLUME GRANULARITY`。系列总称不直接挂 QX；先恢复真实阅读单元，再按 `SMALLEST_INDEPENDENT_NARRATIVE_UNIT` 标注。

## 01｜阶段总览

```text
HARRY_POTTER = CLOSED
SHERLOCK_HOLMES = CLOSED
DRAGON_RAJAS = DEFER_VERSION_BOUNDARY

FORMAL_WORKS_WITH_QX_BEFORE = 124
FORMAL_QX_RELATIONS_BEFORE = 368
FORMAL_WORKS_WITH_QX_CURRENT = 189
FORMAL_QX_RELATIONS_CURRENT = 480
```

## 02｜《哈利·波特》：闭环

```text
7 child Works
7 FORMAL_QX
21 formal relations
HARRY_POTTER_GRANULARITY = CLOSED
```

七册均复用中央 Work，不创建系列级 QX。

## 03｜《福尔摩斯探案全集》：60-unit 全闭环

个人完整阅读事实已确认。标准作品粒度：

```text
4 novels + 56 short stories = 60 independent narrative units
```

### 03.1｜最终统计

```text
SHERLOCK_CANON_UNITS = 60
SHERLOCK_UNITS_REVIEWED = 60
SHERLOCK_FORMAL_QX_WORKS = 58
SHERLOCK_ZERO_QX_WORKS = 2
SHERLOCK_FORMAL_RELATIONS = 91
SHERLOCK_RECONCILIATION = CLOSED
```

### 03.2｜分组统计

```text
4 novels
→ 4 FORMAL_QX / 12 relations

The Adventures of Sherlock Holmes
→ 12 FORMAL_QX / 19 relations

The Memoirs of Sherlock Holmes
→ 10 FORMAL_QX + 1 ZERO_QX / 13 relations

The Return of Sherlock Holmes
→ 12 FORMAL_QX + 1 ZERO_QX / 20 relations

His Last Bow
→ 8 FORMAL_QX / 9 relations

The Case-Book of Sherlock Holmes
→ 12 FORMAL_QX / 18 relations
```

### 03.3｜ZERO_QX

```text
住院的病人
失踪的中卫
```

两篇均已完成审查，只是没有单一具体对象达到正式 QX 门槛；不因全集闭环而强行制造关系。

### 03.4｜《最后致意》8篇

```text
紫藤别墅 → 紫藤别墅；密码便条
硬纸盒 → 装有两只人耳的硬纸盒
红圈会 → 报纸密码广告
布鲁斯-帕廷顿计划 → 潜艇设计图纸
临终的侦探 → 象牙小盒
弗朗西丝·卡法克斯女士失踪案 → 棺材
魔鬼之足 → 魔鬼之足毒根粉末
最后致意 → 德国情报文件
```

```text
HIS_LAST_BOW_FORMAL_QX_WORKS = 8
HIS_LAST_BOW_FORMAL_RELATIONS = 9
```

### 03.5｜《福尔摩斯案件簿》12篇

```text
显贵的主顾 → 格鲁纳的私密记事簿
苍白的士兵 → 苍白斑驳的皮肤
马萨林宝石 → 马萨林宝石
三角墙山庄 → 三角墙山庄；未完成的小说手稿
苏塞克斯吸血鬼 → 毒箭
三个加里德布 → 地下伪钞印刷设备
雷神桥之谜 → 雷神桥；系绳石块
爬行人 → 猿类血清药剂；四肢爬行的身体姿态
狮鬃毛 → 狮鬃水母
戴面纱的房客 → 面纱；面部伤疤
肖斯科姆别墅 → 地下墓室与棺材；肖斯科姆王子赛马
退休的颜料商 → 密闭保险室；新刷油漆
```

```text
CASE_BOOK_FORMAL_QX_WORKS = 12
CASE_BOOK_FORMAL_RELATIONS = 18
```

### 03.6｜本轮精度规则确认

```text
SHORT_STORY ≠ MUST_HAVE_QX
SHORT_STORY ≠ MUST_HAVE_MULTIPLE_QX
SERIES_ICON ≠ AUTOMATIC_STORY_QX
COLLECTION_TITLE ≠ WORK_LEVEL_QX
```

“贝克街、烟斗、放大镜、华生手记”等系列识别物不自动继承到全部 56 篇。

## 04｜《龙族》：当前唯一未闭环 SERIES 项

个人阅读事实：

```text
READ_SCOPE = COMPLETE_SERIES_CONFIRMED
SOURCE_NOTE = 来时路：网文
```

当前中央库只有系列父记录 `龙族.md`。由于原始连载、纸质单行本、第三部上中下分册、第五部连载与后续修订 / 重写存在不同边界：

```text
QX_ON_SERIES_PARENT = PROHIBITED
VOLUME_MAP = DEFER_VERSION_BOUNDARY
```

下一步只恢复可由个人阅读记录 / 上游版本事实支持的卷级或叙事级 Work，不以现代修订版倒推早期阅读事实。

## 05｜Batch030 当前状态

```text
SERIES_RECORDS_TOTAL = 3
HARRY_POTTER = CLOSED
SHERLOCK_HOLMES = CLOSED
DRAGON_RAJAS = CURRENT / VERSION_BOUNDARY_RECONCILIATION
```

## 06｜下一步

```text
Batch030-C
→ 搜索仓库中的《龙族》阅读记录、版本、卷名和历史补录证据
→ 恢复可证明的阅读边界
→ 建立 / 复用卷级 Work
→ 单卷 Admission Gate
→ 不确定边界继续 DEFER，不猜测
```

完成 SERIES 后：

```text
Batch031 = STORY-LEVEL READING MAP
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次029]]
