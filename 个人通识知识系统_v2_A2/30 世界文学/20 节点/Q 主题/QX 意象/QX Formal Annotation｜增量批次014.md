---
id: WL-QX-FORMAL-ANNOTATION-014
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次014
code: QX-ANNOTATION-014
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 切尔诺贝利的悲鸣
  - 轻舔丝绒
  - 球状闪电
  - 风声
  - 扶桑
  - 浮生六记
  - 情书
---

# QX Formal Annotation｜增量批次014

> 本批开始采用“大批次 + 连续循环”模式。冻结 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1` 不变；扩大的是吞吐量，不是 Admission Gate 的宽松程度。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《切尔诺贝利的悲鸣》 | 3 | 废弃村庄 / 空房屋；铅棺 / 密封棺木；口述声音 |
| 《轻舔丝绒》 | 3 | 音乐厅舞台；男装 / 男性舞台服饰；牡蛎 |
| 《球状闪电》 | 3 | 球状闪电；雷暴 / 雷电；灰烬 / 被烧毁的遗留物 |
| 《风声》 | 3 | 裘庄 / 封闭别墅；密码 / 密电；刑具 / 审讯器械 |
| 《扶桑》 | 3 | 唐人街 / 华人聚居区；红色衣裙；裹足 / 小脚 |
| 《浮生六记》 | 3 | 沧浪亭 / 园居空间；花木 / 盆景；香 / 焚香 |
| 《情书》 | 3 | 书信；雪；图书借阅卡 / 借书卡 |

```text
BATCH_014_WORKS = 7
BATCH_014_FORMAL_RELATIONS = 21
FORMAL_QX_RELATIONS_BEFORE = 200
FORMAL_QX_RELATIONS_AFTER = 221
FORMAL_WORKS_WITH_QX_BEFORE = 56
FORMAL_WORKS_WITH_QX_AFTER = 63
```

## 02｜对象复用

《情书》的“书信”直接复用既有：

```yaml
qx_id: QX16.1
object: 书信
```

其余对象继续保持 `qx_id: null`，不在建设阶段提前激活叶专题。

## 03｜纪实作品边界

《切尔诺贝利的悲鸣》与此前《二手时间》一样，允许“口述声音”作为正式媒介对象，但没有将：

```text
核灾难
创伤
苏联
死亡
记忆
```

直接当作 QX object。

## 04｜对象粒度继续延期治理

本批新增待 Full Corpus Audit 复核的对象粒度候选：

```text
口述声音
男装 / 男性舞台服饰
雷暴 / 雷电
灰烬 / 被烧毁的遗留物
密码 / 密电
唐人街 / 华人聚居区
红色衣裙
裹足 / 小脚
沧浪亭 / 园居空间
花木 / 盆景
图书借阅卡 / 借书卡
```

当前不强制 canonical normalization。

## 05｜短篇集粒度异常

扫描到《夜晚的潜水艇》时发现其中央 Work 实体对应短篇小说集。按照治理规则“默认使用最小独立叙事单元”，本批不直接给整本集子附加跨篇混合 QX。

```text
DEFERRED_WORK = 夜晚的潜水艇
DEFER_REASON = COLLECTION_REQUIRES_STORY_LEVEL_GRANULARITY
SCHEMA_CHANGE = NO
```

该问题仅登记，不阻断其余作品继续标注。

## 06｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 221
FORMAL_WORKS_WITH_QX = 63
BATCH_014_FORMAL_RELATIONS = 21
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
NEXT_BATCH = 015
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次013]]
- [[QX16.1 文学中的书信]]
