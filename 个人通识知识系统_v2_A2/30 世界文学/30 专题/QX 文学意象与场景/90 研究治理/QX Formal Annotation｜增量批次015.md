---
id: WL-QX-FORMAL-ANNOTATION-015
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次015
code: QX-ANNOTATION-015
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 高老头
  - 使女的故事
  - 我们
  - 西线无战事
  - 人鼠之间
  - 没有人给他写信的上校
  - 明亮的夜晚
  - 穆斯林的葬礼
  - 四世同堂
  - 无声告白
---

# QX Formal Annotation｜增量批次015

> 本批继续“大批次 + 连续循环”模式。扩大吞吐量，不改变 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。关系数量由作品本身决定，不设置每部最低条数。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《高老头》 | 3 | 伏盖公寓；上流社会沙龙 / 客厅；高老头的银器 / 财物 |
| 《使女的故事》 | 3 | 红色使女服；白色翼帽 / 头罩；墙 / 悬尸墙 |
| 《我们》 | 3 | 玻璃房屋 / 玻璃城市；绿色墙；积分号 |
| 《西线无战事》 | 3 | 战壕；靴子；泥土 / 大地 |
| 《人鼠之间》 | 3 | 河边空地；兔子；农场宿舍 / 工棚 |
| 《没有人给他写信的上校》 | 2 | 斗鸡 / 公鸡；书信 |
| 《明亮的夜晚》 | 3 | 黑白照片 / 旧相册；书信；祖母家老屋 |
| 《穆斯林的葬礼》 | 3 | 玉 / 玉器；博雅宅 / 玉器作坊；葬礼 / 墓地 |
| 《四世同堂》 | 2 | 小羊圈胡同；祁家院落 / 四世同堂住宅 |
| 《无声告白》 | 2 | 湖 / 湖水；莉迪亚的卧室 |

```text
BATCH_015_WORKS = 10
BATCH_015_FORMAL_RELATIONS = 27
FORMAL_QX_RELATIONS_BEFORE = 221
FORMAL_QX_RELATIONS_AFTER = 248
FORMAL_WORKS_WITH_QX_BEFORE = 63
FORMAL_WORKS_WITH_QX_AFTER = 73
```

## 02｜本批的高置信度边界

本批没有采用“每部固定 3 条”的机械策略。

例如：

```text
没有人给他写信的上校 = 2
四世同堂 = 2
无声告白 = 2
```

这些作品仍然完成 formal annotation，因为：

```text
QX_COUNT_PER_WORK has no minimum quota
precision > density
```

## 03｜书信对象继续复用

本批两部作品直接复用：

```yaml
qx_id: QX16.1
object: 书信
```

对应：

- 《没有人给他写信的上校》：长期缺席的养老金官方来信，以“等待信件”组织人物时间与官僚关系；
- 《明亮的夜晚》：旧信跨越代际保存女性友谊、离散经验与家族记忆。

同一 canonical object 在两部作品中的功能明显不同：

```text
上校：制度承诺 / 等待 / 缺席 / 时间仪式
明亮的夜晚：家族记忆 / 女性关系 / 代际连接
```

这正符合 QX 跨作品比较目标。

## 04｜制度空间密度上升，但暂不建新专题

本批出现一组高强度空间对象：

```text
伏盖公寓
玻璃城市
绿色墙
悬尸墙
战壕
农场宿舍
小羊圈胡同
祁家院落
莉迪亚的卧室
```

它们在功能上涉及：

```text
阶级分层
监控与透明性
政治边界
公共惩罚
战争生存
流动劳动
占领社会
家族秩序
家庭误解
```

当前只记录正式关系，不因为“制度空间”功能相似就创建 object family 或 QX leaf。

```text
FUNCTIONAL_CLUSTER_SIGNAL = OBSERVED
NEW_QX_LEAF = NO
ONTOLOGY_REFACTOR = DEFERRED
```

## 05｜身体、服饰与制度

《使女的故事》保留：

```text
红色使女服
白色翼帽 / 头罩
```

而没有直接标注：

```text
父权
生殖政治
女性压迫
宗教极权
```

前者是可感知、反复出现、直接规定身体可见性与行动条件的 QX object；后者继续属于 QH / M 解释层。

## 06｜战争文学中的物质环境

《西线无战事》保留：

```text
战壕
靴子
泥土 / 大地
```

其中“靴子”特别符合 QX 的跨作品价值：物件在士兵死亡后继续流转，使身体消失与军需物继续使用形成可见反差。

战争、反战、创伤本身仍不进入 QX object。

## 07｜《无声告白》：不把家庭问题抽象物象化

本批只保留：

```text
湖 / 湖水
莉迪亚的卧室
```

湖在童年落水、莉迪亚死亡及结尾再次落水之间形成稳定结构回声；卧室则在死后调查与家人重新理解莉迪亚的过程中，由私人空间变成暴露家庭误解的证据空间。

没有把：

```text
种族身份
父母期待
沉默
家庭压力
```

转换成伪 QX 对象。

## 08｜对象粒度继续延期治理

新增 Full Corpus Audit 候选：

```text
伏盖公寓 vs 寄宿空间
上流社会沙龙 / 客厅
红色使女服 vs 红色
玻璃房屋 / 玻璃城市
绿色墙
战壕
泥土 / 大地
兔子（现实动物 vs 想象对象）
斗鸡 / 公鸡
黑白照片 / 旧相册
玉 / 玉器
葬礼 / 墓地（仪式 vs 空间）
小羊圈胡同
湖 / 湖水
人物卧室
```

不在当前建设阶段解决。

## 09｜连续模式累计状态

本轮连续完成：

```text
Batch 014 = 7 works / 21 relations
Batch 015 = 10 works / 27 relations
CONTINUOUS_LOOP_WORKS = 17
CONTINUOUS_LOOP_RELATIONS = 48
```

从 Batch013 结束状态：

```text
56 works / 200 relations
```

推进至：

```text
73 works / 248 relations
```

## 10｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 248
FORMAL_WORKS_WITH_QX = 73
ACTIVE_QX_LEAVES = UNCHANGED
NEW_TOPIC_THIS_BATCH = NONE
SHORT_STORY_COLLECTION_DEFERRED = 夜晚的潜水艇
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
NEXT_BATCH = 016
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次014]]
- [[QX16.1 文学中的书信]]
