---
id: WL-QX-FORMAL-ANNOTATION-005
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次005
code: QX-ANNOTATION-005
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 简·爱
  - 金锁记
  - 五号屠场
  - 素食者
---

# QX Formal Annotation｜增量批次005

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。
>
> 不设配额；标题隐喻不自动转化为 QX object；允许不同作品产生明显不同的关系密度。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《简·爱》 | 4 | 红房间；桑菲尔德庄园；火；栗树 |
| 《金锁记》 | 3 | 月亮；金饰与首饰；鸦片烟枪 |
| 《五号屠场》 | 4 | 五号屠场地下肉库；火与焚毁后的德累斯顿；飞碟；鸟鸣 |
| 《素食者》 | 4 | 肉；花卉身体彩绘；树与植物；阳光 |

```text
BATCH_005_WORKS = 4
BATCH_005_FORMAL_RELATIONS = 15
FORMAL_QX_RELATIONS_BEFORE = 98
FORMAL_QX_RELATIONS_AFTER = 113
FORMAL_WORKS_WITH_QX_BEFORE = 21
FORMAL_WORKS_WITH_QX_AFTER = 25
```

---

## 02｜标题隐喻边界：以《金锁记》为例

本批明确没有因为作品标题中存在“金锁”，就建立：

```yaml
object: 金锁
```

原因是 QX object 要求作品内部存在可复核的感知对象与叙事运行证据，标题级隐喻本身不能替代作品内部关系。

因此正式保留的是作品内部更稳定的：

- 月亮；
- 金饰与首饰；
- 鸦片烟枪。

这一结果继续支持：

```text
TITLE_METAPHOR ≠ QX_OBJECT
```

---

## 03｜空间并不只是背景

《简·爱》的红房间与桑菲尔德庄园，以及《五号屠场》的地下肉库，都属于空间对象，但功能完全不同：

- 红房间：童年惩罚、隔离与记忆创伤；
- 桑菲尔德庄园：关系形成、秘密遮蔽与家庭结构转化；
- 五号屠场地下肉库：战争幸存的物质条件与标题锚点。

因此空间类 QX 仍需比较：

```text
object
× manifestation
× function
× mode
```

不能把“房间 / 庄园 / 地下室”直接归并为一个泛化节点。

---

## 04｜身体—植物链条在《素食者》中形成

《素食者》本批录入：

```text
肉
→ 花卉身体彩绘
→ 树与植物
→ 阳光
```

这不是人工建立的 `IMAGERY_CONSTELLATION`，而是四条独立 `HAS_IMAGERY` 关系后可供未来派生分析使用的共现结构。

它们共同涉及：

- 动物性食物的拒绝；
- 身体表面的植物化；
- 主体向树木/植物的转化想象；
- 以阳光替代普通摄食的身体实践。

因此该作品非常适合未来测试：

```text
BODY_TRANSFORMATION
× PLANT_IMAGERY
× PERCEPTUAL_CHANNEL
```

的派生关系。

---

## 05｜声音对象再次通过 Admission Gate

《五号屠场》的“鸟鸣”被保留，原因不是它是一句著名文本，而是它具有明确的听觉 manifestation，并在战争毁灭之后承担结构收束与反讽功能。

这与此前《挪威的森林》的音乐媒介一起说明：

```text
QX ≠ VISUAL_ONLY
```

但声音必须仍然满足：

- 可感知；
- 有明确叙事功能；
- 有可复核 evidence。

---

## 06｜Object Normalization 检查

本批没有因名称相近就进行强制归一：

- 《简·爱》的“火”与《五号屠场》的“火与焚毁后的德累斯顿”暂不合并为同一 object；前者是反复出现并改变家庭结构的火灾装置，后者是总体战造成的城市毁灭景观。
- “桑菲尔德庄园”不与“彭伯里”“呼啸山庄”“画眉田庄”合并；跨宅邸相似性留给 function / mode / scope 派生分析。
- 《素食者》的“树与植物”不与《追风筝的人》的“石榴树”或《简·爱》的“栗树”直接合并。

因此：

```text
NEW_QX_TOPIC_ACTIVATED = 0
```

当前仍保持“数据先积累，专题后激活”的策略。

---

## 07｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 113
FORMAL_WORKS_WITH_QX = 25
NEW_TOPIC_THIS_BATCH = NONE
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次004]]
- [[QX Object Normalization｜首批55条正式关系]]
