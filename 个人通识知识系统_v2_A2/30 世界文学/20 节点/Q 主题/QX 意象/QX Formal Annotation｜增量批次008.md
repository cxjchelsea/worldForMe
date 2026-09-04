---
id: WL-QX-FORMAL-ANNOTATION-008
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次008
code: QX-ANNOTATION-008
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 杀死一只知更鸟
  - 白夜行
  - 解忧杂货店
---

# QX Formal Annotation｜增量批次008

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。
>
> 重点测试：标题隐喻边界、犯罪叙事起点空间、跨时间书信机制，以及公共审判空间。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《杀死一只知更鸟》 | 3 | 拉德利宅；树洞礼物；法庭 |
| 《白夜行》 | 2 | 太阳与白夜；当铺 |
| 《解忧杂货店》 | 3 | 浪矢杂货店；书信；牛奶箱 |

```text
BATCH_008_WORKS = 3
BATCH_008_FORMAL_RELATIONS = 8
FORMAL_QX_RELATIONS_BEFORE = 139
FORMAL_QX_RELATIONS_AFTER = 147
FORMAL_WORKS_WITH_QX_BEFORE = 33
FORMAL_WORKS_WITH_QX_AFTER = 36
```

---

## 02｜标题与正式 QX：两个不同案例

### 《杀死一只知更鸟》

本批没有建立：

```yaml
object: 知更鸟
```

原因是“知更鸟”在作品中高度重要，但当前更稳定地承担伦理比喻与主题表达功能；仅凭标题和解释性比喻不足以把它当成持续运行的 object-level QX。

因此继续坚持：

```text
TITLE / ETHICAL METAPHOR alone ≠ FORMAL QX OBJECT
```

### 《白夜行》

“太阳与白夜”则被保留，因为它不只是标题，而是在文本内部以明确的反常昼夜图景被人物语言化，并持续概括两名人物的生存状态。

因此边界不是“标题出现的一律不要”，而是：

```text
TITLE_ONLY → DROP
TEXT-INTERNAL STABLE IMAGERY → CAN PASS
```

---

## 03｜QX16.1 文学中的书信扩展至第 4 部作品

《解忧杂货店》的书信直接复用：

```yaml
qx_id: QX16.1
object: 书信
```

当前正式实例：

1. 《傲慢与偏见》：信息校正；
2. 《一个陌生女人的来信》：生命自述；
3. 《陆犯焉识》：分离中的关系维系；
4. 《解忧杂货店》：跨时间咨询与多故事编织。

因此 QX16.1 的比较维度继续扩张，而不是趋向单一象征解释。

---

## 04｜空间 object 的功能继续分化

本批新增多个空间对象：

- 拉德利宅：儿童恐惧、想象与认知修正；
- 法庭：制度公开运行与偏见暴露；
- 当铺：长期犯罪因果链的起点；
- 浪矢杂货店：跨时间通信与故事汇聚。

这些对象虽然都属于“空间”，但不应合并为一个 object。

它们的结构相似性继续留给：

```text
primary_group
+ function
+ mode
+ scope
```

做派生分析。

---

## 05｜《解忧杂货店》的物质化时间机制

“牛奶箱”被保留，是因为跨时间通信并非只停留在抽象设定，而是通过一个反复使用的具体投递容器实现。

因此可表示为：

```text
超自然时间连接
↓
书信
↓
牛奶箱
↓
可重复的投递动作
```

这证明 QX 很适合记录“抽象叙事机制如何被具体物件物质化”。

---

## 06｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 147
FORMAL_WORKS_WITH_QX = 36
ACTIVE_QX_LEAVES = 2
QX3.1_ACTIVATION_WORKS = 5
QX16.1_ACTIVATION_WORKS = 4
NEW_TOPIC_THIS_BATCH = NONE
EXPANDED_TOPIC_THIS_BATCH = QX16.1
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次007]]
- [[QX16.1 文学中的书信]]
- [[QX3.1 文学中的海]]
