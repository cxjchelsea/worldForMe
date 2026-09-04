---
id: WL-QX-FORMAL-ANNOTATION-019
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次019
code: QX-ANNOTATION-019
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 爱与痛的边缘
  - 草
  - 斗罗大陆
  - 二月
  - 给樱桃以性别
  - 牛棚杂忆
  - 饺子
---

# QX Formal Annotation｜增量批次019

> 本批继续连续循环。审查 7 部明确已读作品，其中 3 部形成正式 QX，3 部本轮判定 QX=0，1 部因作品粒度 / 类型元数据异常延期。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 / 结论 |
|---|---:|---|
| 《爱与痛的边缘》 | 0 | 本轮无对象通过 Admission Gate |
| 《草》 | deferred | 文集 / 杂文集合粒度与当前“小说”元数据冲突，暂不整本标注 |
| 《斗罗大陆》 | 3 | 魂环；蓝银草；昊天锤 |
| 《二月》 | 0 | 本轮无对象通过 Admission Gate |
| 《给樱桃以性别》 | 0 | 不因标题与身体主题强行生成 object |
| 《牛棚杂忆》 | 3 | 牛棚；大字报 / 标语；挂牌 / 高帽 |
| 《饺子》 | 3 | 饺子；胎儿 / 人胎馅料；厨房 / 制作台 |

```text
BATCH_019_REVIEWED_WORKS = 7
BATCH_019_WORKS_WITH_FORMAL_QX = 3
BATCH_019_ZERO_QX_WORKS = 3
BATCH_019_DEFERRED_WORKS = 1
BATCH_019_FORMAL_RELATIONS = 9
FORMAL_QX_RELATIONS_BEFORE = 311
FORMAL_QX_RELATIONS_AFTER = 320
FORMAL_WORKS_WITH_QX_BEFORE = 98
FORMAL_WORKS_WITH_QX_AFTER = 101
```

## 02｜网络类型文学仍执行同一 Gate

《斗罗大陆》没有因为类型文学对象很多就批量收录技能、武器和地点；只保留：

```text
魂环
蓝银草
昊天锤
```

三者分别稳定绑定等级体系、人物身份成长与隐藏血统 / 力量继承。

## 03｜纪实作品中的政治身体化

《牛棚杂忆》保留：

```text
牛棚
大字报 / 标语
挂牌 / 高帽
```

三者分别把：

```text
隔离空间
公开文字定性
身体羞辱仪式
```

转化为可见、可定位的物质形式。

没有把“文革”“迫害”“政治运动”“记忆”直接写成 QX object。

## 04｜《饺子》：食物、身体与制作空间

《饺子》的核心关系不是抽象“女性衰老焦虑”，而是：

```text
饺子
胎儿 / 人胎馅料
厨房 / 制作台
```

三者形成稳定链条：

```text
身体原料 → 食物加工 → 食用 / 身体更新
```

这为未来 QX13 食物、QX9 身体与 QX7 室内空间之间的跨作品功能比较提供了高置信实例。

## 05｜标题与主题仍不能替代 object

本批《爱与痛的边缘》《给樱桃以性别》均没有因为标题高度意象化而自动准入。

```text
TITLE / THEME ≠ QX OBJECT
```

## 06｜《草》粒度异常

当前中央 Work 将《草》记录为：

```yaml
axis_g:
- G3 小说
```

但该书更接近文集 / 杂文集合形态。若直接整本抽取，会把不同篇章对象混合为一个叙事实体。

因此：

```text
DEFERRED_WORK = 草
DEFER_REASON = COLLECTION_OR_ESSAY_VOLUME_GRANULARITY_MISMATCH
SCHEMA_CHANGE = NO
```

只登记问题，不在 QX 阶段顺手重构 G 轴元数据。

## 07｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 320
FORMAL_WORKS_WITH_QX = 101
ZERO_QX_THIS_BATCH = 爱与痛的边缘；二月；给樱桃以性别
DEFERRED_THIS_BATCH = 草
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
NEXT_BATCH = 020
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次018]]
