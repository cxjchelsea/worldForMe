---
id: WL-QX-NORMALIZATION-001
type: literature_qx_object_normalization
name: QX Object Normalization｜首批55条正式关系
code: QX-NORMALIZATION-001
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
formal_relations: 55
---

# QX Object Normalization｜首批55条正式关系

> 本文件对首批正式迁移后的 55 条 QX 关系进行 object normalization 与专题激活检查。
>
> 目标不是把相似词全部合并，而是识别“同一稳定对象在多部作品中重复出现”的情况，并按 `QX_TOPIC_GROWTH_MODEL` 判断是否值得激活正式叶节点。

---

## 01｜归一化原则

### 01.1 只有对象相同才优先归一

例如：

```text
海 / 海洋 → 海
```

但不会因为功能相近就合并：

```text
大观园
楼上房间
梁宅
基督山岛
```

它们可以在派生分析中形成“空间结构相似”，却不是同一个 object。

### 01.2 manifestation 不单独计 object

例如：

```text
海
├─ 海滨
├─ 深海
└─ 极地海域
```

这些首先作为 manifestation 处理，不重复计数。

### 01.3 类别相同不等于对象相同

例如：

```text
宴席 / 家宴
舞会 / 社交场
守灵 / 葬礼仪式
```

虽然都属于 QX20 社会仪式与公共场景，但并非同一对象，不因一级分类相同而强行合并。

---

## 02｜达到 3 部作品门槛的对象

### 海

归一化：

```text
《基督山伯爵》：海
《局外人》：海
《海底两万里》：海 / 海洋
→ normalized_object = 海
```

作品数：`3`

功能变体：

1. 《基督山伯爵》：通道、逃亡与身份转换；
2. 《局外人》：身体愉悦、关系空间与暴力反差；
3. 《海底两万里》：世界本体、探索空间与行动条件。

结论：

```text
WORK_COUNT = 3
FUNCTION_VARIANTS >= 2
ACTIVATION_RULE = PASSED
```

已正式激活：

```text
QX3.1 文学中的海
```

并已回填三部作品：

```yaml
qx_id: QX3.1
```

---

## 03｜接近门槛但暂不激活

### 冰

当前至少可确认：

```text
《百年孤独》：冰
《海底两万里》：冰 / 冰层
```

作品数：`2`

两者功能已经明显不同：

- 《百年孤独》：早期奇观、记忆与知识经验；
- 《海底两万里》：极地阻碍、困闭与自然边界。

但作品数仍不足 3，因此：

```text
STATUS = CANDIDATE
ACTIVATION = NOT_YET
```

### 火车 / 铁路 / 列车

当前至少可确认：

```text
《百年孤独》：火车 / 铁路
《银河铁道之夜》：银河列车 / 铁道
```

对象归一化时暂采用概念候选：

```text
铁路列车 / 火车 / 列车 → 列车（candidate normalization）
```

但由于一部是现代化进入城镇的现实交通系统，一部是宇宙旅程的核心阈限交通对象，当前仅记录为可比较对象族，不急于冻结统一 object 名称。

作品数：`2`

```text
STATUS = CANDIDATE
ACTIVATION = NOT_YET
```

---

## 04｜不应因为“结构相似”而合并的对象

首批正式关系已经出现若干潜在结构相似群：

### 空间转换 / 临时世界

```text
大观园 / 园林
楼上房间
梁宅 / 洋房
基督山岛
伊夫堡 / 监狱
沙漠
```

这些对象的 exact object 不同，不建立统一 QX 叶节点。

未来可由：

```text
function
+ mode
+ scope
+ meaning（有值时）
```

派生空间结构聚类。

### 社会仪式 / 公共场景

```text
宴席 / 家宴
舞会 / 社交场
法庭 / 审判空间
守灵 / 葬礼仪式
```

它们共同位于 QX20，但功能和场景类型不同，不合并成“社会场景”大节点。

### 书写 / 媒介对象

```text
羊皮卷 / 手稿
日记 / 空白书页
```

两者都与书写、记忆和结构有关，但对象与叙事机制不同，暂不归一。

---

## 05｜首批专题激活结果

基于当前 55 条正式关系：

```text
FORMAL_RELATIONS = 55
NEWLY_ACTIVATED_BY_DATA = 1
NEW_TOPIC = QX3.1 文学中的海
NEAR_THRESHOLD_OBJECTS = 2
  - 冰
  - 列车 / 铁路
```

注意：已有 `QX1.1 文学中的雨` 属于早期示范 / 兴趣驱动专题，不代表当前 55 条数据中“雨”已经满足 3 部作品激活门槛。

---

## 06｜这一步验证了什么

第一轮正式 object normalization 说明：

1. Admission Gate 并没有让所有作品都汇聚到少数常见 object；
2. 大部分正式关系仍保持较强作品辨识度；
3. 只有真正跨作品重复的对象才开始自然形成 QX 叶节点；
4. function-level 相似性应留给后续派生分析，而不是靠 object 过度合并来制造；
5. QX 可以从“作品标注层”自然长出“专题层”，不需要预先建立完整意象百科。

---

## 07｜下一阶段

```text
OBJECT_NORMALIZATION_001 = COMPLETE
QX3.1_ACTIVATION = COMPLETE
```

下一步可以开始：

1. 扩大到更多已读作品做正式 QX 标注；
2. 每增加一批作品后增量检查 object activation；
3. 等正式关系数量更大后，再实验 function / mode / scope 的派生聚类与作品距离。

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Migration｜首批十部作品]]
- [[QX3.1 文学中的海]]
- [[QX3 水域与液体]]
