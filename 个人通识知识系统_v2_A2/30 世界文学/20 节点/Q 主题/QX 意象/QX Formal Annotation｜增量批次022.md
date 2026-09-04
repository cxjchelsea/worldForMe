---
id: WL-QX-FORMAL-ANNOTATION-022
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次022
code: QX-ANNOTATION-022
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 生死疲劳
  - 孽子
  - 水浒传
  - 杨家将
  - 一句顶一万句
  - 再见，冥王星
  - 在细雨中呼喊
  - 机器人短篇全集
---

# QX Formal Annotation｜增量批次022

> 本批继续连续循环，并开始显式区分：正式关系、QX=0、collection-deferred 三种结果。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 结论 |
|---|---:|---|
| 《生死疲劳》 | 3 | 转生动物身体；西门屯 / 土地；蓝脸独耕的田地 |
| 《孽子》 | 3 | 台北新公园；夜 / 黑暗；家门 / 被逐出的家庭住宅 |
| 《水浒传》 | 3 | 梁山泊 / 水泊梁山；酒 / 酒肆；招安诏书 / 朝廷文书 |
| 《杨家将》 | 0 | 本轮无对象达到整本层面的高置信 Admission Gate |
| 《一句顶一万句》 | 0 | “说话 / 找得到能说话的人”更接近关系与主题，不强行物象化 |
| 《再见，冥王星》 | 0 | 不因标题中的“冥王星”直接准入 |
| 《在细雨中呼喊》 | 0 | 细雨 / 呼喊虽具辨识度，但当前不足以证明整本 recurrent object |
| 《机器人短篇全集》 | deferred | 稳定作者短篇集；默认回到独立叙事单元处理 |

```text
BATCH_022_REVIEWED_WORKS = 8
BATCH_022_WORKS_WITH_FORMAL_QX = 3
BATCH_022_ZERO_QX_WORKS = 4
BATCH_022_DEFERRED_COLLECTIONS = 1
BATCH_022_FORMAL_RELATIONS = 9
FORMAL_QX_RELATIONS_BEFORE = 325
FORMAL_QX_RELATIONS_AFTER = 334
FORMAL_WORKS_WITH_QX_BEFORE = 103
FORMAL_WORKS_WITH_QX_AFTER = 106
```

## 02｜经典长篇与类型长篇使用同一 Gate

《水浒传》《生死疲劳》都允许出现较多正式关系，但原因不是“经典作品应多标”，而是对象本身持续承担结构作用：

```text
梁山泊 → 法外共同体的稳定空间
招安诏书 → 国家重新吸纳共同体的物质媒介
动物转生身体 → 分期、视角、身份的结构机制
土地 → 家族 / 制度 / 历史变化的稳定空间载体
```

## 03｜标题意象继续严格限制

本批再次确认：

```text
再见，冥王星
在细雨中呼喊
```

不能仅凭标题或高度可解释的开篇场景进入 QX。

```text
TITLE_SALIENCE ≠ WORK_LEVEL_RECURRENCE
```

## 04｜合集处理保持一致

《机器人短篇全集》虽然“机器人”跨多篇反复出现，但当前治理规则默认以独立叙事单元作为 QX 标注粒度，因此登记：

```text
DEFERRED_WORK = 机器人短篇全集
DEFER_REASON = AUTHOR_COLLECTION_REQUIRES_STORY_LEVEL_REVIEW
```

与《夜晚的潜水艇》等集合型作品进入同一待处理队列。

## 05｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 334
FORMAL_WORKS_WITH_QX = 106
NEW_QX_LEAF = NO
FULL_CORPUS_AUDIT = DEFERRED
NEXT_BATCH = 023
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次021]]
