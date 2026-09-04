---
id: WL-QX-FORMAL-ANNOTATION-023
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次023
code: QX-ANNOTATION-023
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 三国演义
  - 西游记
  - 玩偶之家
  - 隐形墨水
  - 时间
  - 我不可能只是仰望着你
  - 梦里花落知多少
  - 夏至未至
  - 像少年啦飞驰
  - 小时代
  - 致青春
---

# QX Formal Annotation｜增量批次023

> 本批审查古典长篇、戏剧、历史小说与青春 / 大众文学，继续使用完全相同的 Admission Gate。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 / 结论 |
|---|---:|---|
| 《三国演义》 | 2 | 赤壁火攻 / 火船；青龙偃月刀 |
| 《西游记》 | 3 | 如意金箍棒；紧箍 / 紧箍咒；真经 / 经卷 |
| 《玩偶之家》 | 3 | 书信；圣诞树；门 / 关门声 |
| 《夏至未至》 | 2 | 香樟树；浅川校园 / 教室与操场 |
| 《隐形墨水》 | 0 | 不因标题“墨水”直接准入；元数据体裁异常另记 |
| 《时间》 | 0 | 战争 / 记忆主题不自动转成物象 |
| 《我不可能只是仰望着你》 | 0 | 本轮缺乏高置信整本物象 |
| 《梦里花落知多少》 | 0 | 标题“花落”不直接准入 |
| 《像少年啦飞驰》 | 0 | 标题“飞驰”及青春道路感不直接准入 |
| 《小时代》 | 0 | 都市 / 奢侈消费等背景不足以单独构成高置信对象 |
| 《致青春》 | 0 | 校园与青春主题不足以自动准入 |

```text
BATCH_023_REVIEWED_WORKS = 11
BATCH_023_WORKS_WITH_FORMAL_QX = 4
BATCH_023_ZERO_QX_WORKS = 7
BATCH_023_FORMAL_RELATIONS = 10
FORMAL_QX_RELATIONS_BEFORE = 334
FORMAL_QX_RELATIONS_AFTER = 344
FORMAL_WORKS_WITH_QX_BEFORE = 106
FORMAL_WORKS_WITH_QX_AFTER = 110
```

## 02｜古典长篇对象仍然要求具体物质形态

没有标注：

```text
三国争霸
忠义
取经
修行
英雄
```

而是落到：

```text
赤壁火攻
青龙偃月刀
金箍棒
紧箍
经卷
```

即便对象具有高度文化象征性，也必须先作为作品内部的可感知对象通过 Gate。

## 03｜《玩偶之家》的三种对象类型

本批同时出现：

```text
书信 → 信息媒介
圣诞树 → 家庭内部状态变化的植物 / 装饰物
门 / 关门声 → singular_pivotal 的建筑边界与声音事件
```

其中“书信”直接复用 `QX16.1`；关门声使用 singular_pivotal，而不是因为“著名结尾”自动准入，而是其终局结构位置不可替代。

## 04｜大众青春文学不降低标准

《夏至未至》保留香樟树和浅川校园，是因为二者反复绑定明确的青春时间、空间和人物关系。

其余多部青春作品本轮为 0，说明：

```text
校园出现 ≠ 校园一定是 QX
爱情关系 ≠ 必须找物件承载
书名有景物 ≠ 景物通过 Gate
```

## 05｜元数据异常登记

《隐形墨水》当前中央 Work 的：

```yaml
axis_g:
- G2 戏剧
```

与作品实际文类存在明显冲突。

```text
METADATA_ANOMALY = 隐形墨水.axis_g
QX_SCHEMA_CHANGE = NO
```

本批不让该问题阻断 QX 主流程，留给后续元数据 QA。

## 06｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_QX_RELATIONS = 344
FORMAL_WORKS_WITH_QX = 110
FULL_CORPUS_AUDIT = DEFERRED
NEXT_BATCH = 024
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次022]]
- [[QX16.1 文学中的书信]]
