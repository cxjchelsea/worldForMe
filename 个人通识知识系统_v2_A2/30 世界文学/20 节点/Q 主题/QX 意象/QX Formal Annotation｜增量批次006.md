---
id: WL-QX-FORMAL-ANNOTATION-006
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次006
code: QX-ANNOTATION-006
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 海边的卡夫卡
  - 美丽新世界
  - 少年Pi的奇幻漂流
  - 房思琪的初恋乐园
---

# QX Formal Annotation｜增量批次006

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。
>
> 特别测试：阈限物、制度装置、海洋生存空间，以及高创伤文本中的低密度标注。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《海边的卡夫卡》 | 4 | 入口石；森林；甲村纪念图书馆；《海边的卡夫卡》歌曲与唱片 |
| 《美丽新世界》 | 4 | 孵化瓶；索麻；感官电影；野蛮人保留区 |
| 《少年Pi的奇幻漂流》 | 4 | 海；救生艇；理查德·帕克；食人岛 |
| 《房思琪的初恋乐园》 | 2 | 文学书籍与文本；封闭房间 |

```text
BATCH_006_WORKS = 4
BATCH_006_FORMAL_RELATIONS = 14
FORMAL_QX_RELATIONS_BEFORE = 113
FORMAL_QX_RELATIONS_AFTER = 127
FORMAL_WORKS_WITH_QX_BEFORE = 25
FORMAL_WORKS_WITH_QX_AFTER = 29
```

---

## 02｜QX3.1 文学中的海继续扩展

《少年Pi的奇幻漂流》的“海”直接复用：

```yaml
qx_id: QX3.1
object: 海
```

`QX3.1` 当前正式作品实例达到 5 部：

1. 《基督山伯爵》：跨越、逃亡与身份转换；
2. 《局外人》：身体经验与关系反差；
3. 《海底两万里》：世界本体与探索空间；
4. 《老人与海》：劳动、生存与搏斗空间；
5. 《少年Pi的奇幻漂流》：漂流世界、生存资源与持续威胁。

同一 object 已经形成明显的 function divergence，因此该叶节点继续保持稳定。

---

## 03｜制度装置：不是主题标签，而是可见机器

《美丽新世界》保留：

- 孵化瓶；
- 索麻；
- 感官电影；
- 野蛮人保留区。

没有直接录入“消费主义”“快乐控制”“生殖政治”等抽象概念，因为这些属于 QH5 / QT6 的解释层。

QX 只记录这些制度如何通过具体对象被看见和体验：

```text
制度
↓
孵化瓶 / 药物 / 娱乐媒介 / 隔离空间
↓
HAS_IMAGERY.function
```

这使 QX 与主题轴保持正交。

---

## 04｜阈限结构：《海边的卡夫卡》

“入口石”是本批一个高质量 QX 对象，因为它不是抽象的“命运之门”，而是可被搬动、翻转、开启和关闭的具体物。

其关系可以写成：

```text
入口石
× 边界 / 阈限
× 场景转换
× 结构标记
```

森林承担类似的阈限功能，但 object 不同；未来可由 function similarity 捕捉其结构接近，而不需要把石头和森林归为同一个 object。

---

## 05｜角色与动物边界再次验证

《少年Pi》的“理查德·帕克”通过 Admission Gate。

这与《动物农场》的角色动物处理并不冲突：

- 《动物农场》的猪、马、驴主要作为完整社会角色运作；
- 理查德·帕克同时持续作为真实动物危险、生存条件和空间关系对象存在，其物种与身体存在直接塑造 Pi 的行动。

因此仍然遵循：

```text
CHARACTER_STATUS alone ≠ EXCLUSION
OBJECT_FUNCTION must be evaluated
```

---

## 06｜高创伤文本允许低密度结果

《房思琪的初恋乐园》最终只保留 2 条：

- 文学书籍与文本；
- 封闭房间。

没有为了“作品重要”而补足更多对象，也没有把：

- 创伤；
- 语言暴力；
- 性别；
- 权力；
- 初恋；

直接当作 QX。

这再次验证：

```text
LITERARY_IMPORTANCE ≠ IMAGERY_DENSITY
QX_COUNT may legitimately be low
```

---

## 07｜Object Normalization 检查

本批仍不做表面名词强制合并：

- “甲村纪念图书馆”不与一般“书房 / 图书馆 / 房间”直接合并；
- “野蛮人保留区”不与其他封闭空间合并；
- “救生艇”不与列车、汽车、飞碟直接合并，交通类相似性应由 function 和 primary_group 处理；
- “文学书籍与文本”与“书信 / 进步报告 / 日记 / 羊皮卷”保持 object 区分，未来再通过媒介属性派生聚类。

因此：

```text
NEW_QX_TOPIC_ACTIVATED = 0
EXISTING_QX_TOPIC_EXPANDED = QX3.1
```

---

## 08｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 127
FORMAL_WORKS_WITH_QX = 29
QX3.1_ACTIVATION_WORKS = 5
NEW_TOPIC_THIS_BATCH = NONE
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次005]]
- [[QX3.1 文学中的海]]
