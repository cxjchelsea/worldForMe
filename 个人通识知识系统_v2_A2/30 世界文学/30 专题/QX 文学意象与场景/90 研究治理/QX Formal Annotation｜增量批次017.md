---
id: WL-QX-FORMAL-ANNOTATION-017
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次017
code: QX-ANNOTATION-017
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 窗边的小豆豆
  - 春桃
  - 手机
  - 她对此感到厌烦
  - 关于女儿
  - 红拂夜奔
  - 幻城
  - 老师好美
  - 狼牙
---

# QX Formal Annotation｜增量批次017

> 本批继续“大批次 + 连续循环”模式。本批实际审查 9 部中央作品库明确 `read_status: 已读` 的作品，其中 8 部通过 Admission Gate 形成正式关系，1 部（《狼牙》）本轮判定为 QX=0。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 / 结论 |
|---|---:|---|
| 《窗边的小豆豆》 | 3 | 电车教室；“海的味道、山的味道”盒饭；巴学园树木校门 |
| 《春桃》 | 2 | 破烂 / 废纸；李茂伤残的双腿 |
| 《手机》 | 1 | 手机 |
| 《她对此感到厌烦》 | 3 | 游戏选项 / 选择界面；剑；斗兽场 |
| 《关于女儿》 | 2 | 母亲的房子 / 共同住宅；养老院 / 护理空间 |
| 《红拂夜奔》 | 3 | 长安城 / 方格城市；夜路 / 出城大道；红拂 / 红色拂尘 |
| 《幻城》 | 3 | 冰雪；火焰；幻雪神山 |
| 《老师好美》 | 3 | 手机短信；教室 / 校园；法院 / 被告席 |
| 《狼牙》 | 0 | 本轮无对象通过 Admission Gate |

```text
BATCH_017_REVIEWED_WORKS = 9
BATCH_017_WORKS_WITH_FORMAL_QX = 8
BATCH_017_ZERO_QX_WORKS = 1
BATCH_017_FORMAL_RELATIONS = 20
FORMAL_QX_RELATIONS_BEFORE = 280
FORMAL_QX_RELATIONS_AFTER = 300
FORMAL_WORKS_WITH_QX_BEFORE = 85
FORMAL_WORKS_WITH_QX_AFTER = 93
```

## 02｜QX=0 是合法结果

《狼牙》本轮明确记录：

```text
DECISION = ZERO_QX_FOR_NOW
```

原因：当前可高置信提取的候选主要是：

```text
训练场
军装 / 迷彩
枪械
军营
特种部队装备
```

这些对象虽然大量出现，但仅凭“军旅小说常见且反复出现”不足以通过 Admission Gate。

目前缺少足够证据证明：

```text
A. 某一具体对象具有超出军事背景的独特反复结构；
B. 或稳定绑定核心人物 / 关系 / 叙事阶段；
C. 或承担足够明确的转折、回声、阈限等功能。
```

因此不为了覆盖率强行标注。

## 03｜《手机》验证单对象作品

《手机》仅保留：

```yaml
object: 手机
primary_group: QX16
salience: dominant
```

没有继续拆为：

```text
短信
电话铃声
通话记录
震动模式
```

因为这些更适合作为同一 canonical object 的 manifestation / interaction，而不是独立 object。

```text
ONE_STRONG_OBJECT > MULTIPLE_MECHANICAL_SPLITS
```

## 04｜数字界面首次成为高强度 QX 候选

《她对此感到厌烦》中的：

```text
游戏选项 / 选择界面
```

正式进入 QX16。

其关键不是“游戏”这一类型标签，而是：

- 选项以可见界面形式反复规定人物行动；
- 莉莉丝最终“打碎选项”；
- 同一对象从操作媒介转化为反抗预设叙事的结构节点。

这为未来 QX16 中：

```text
纸面媒介
声音媒介
数字界面
算法 / 系统可见层
```

的 object family 比较提供了候选，但本阶段不建 family。

## 05｜空间对象继续表现出强关系结构

本批新增：

```text
电车教室
共同住宅
养老院
长安城
夜路
幻雪神山
校园
法院
斗兽场
```

它们分别承担教育、家庭边界、养老制度、城市秩序、出逃阈限、奇幻试炼、师生身份和司法暴露等不同功能。

功能相似不等于 object identity，因此不合并。

## 06｜标题对象仍需通过 Admission Gate

本批出现两种不同情况：

### 《手机》
标题对象“手机”本身就是全书反复推动关系和秘密暴露的核心媒介，因此正式进入 QX。

### 《红拂夜奔》
“红拂”不是因为出现在标题中就进入，而是具体落实为：

```text
红色拂尘
```

并稳定绑定人物称谓、外观和身份识别。

因此：

```text
TITLE_OBJECT_CAN_BE_QX
BUT
TITLE_OCCURRENCE ≠ ADMISSION
```

## 07｜类型文学没有降低 Admission Gate

《幻城》《她对此感到厌烦》等奇幻 / 网文作品仍使用与经典文学完全相同的 QX 标准。

例如《幻城》中的：

```text
冰雪
火焰
幻雪神山
```

入选的原因是它们稳定构成族群、空间、行动条件与叙事阶段，而不是因为奇幻作品“意象多”。

## 08｜对象粒度待审计候选

本批新增：

```text
电车教室 vs 非传统教室
破烂 / 废纸
伤残双腿 vs 伤病身体 / 肢体
手机 vs 手机短信
数字选择界面
共同住宅
养老院 / 护理空间
长安城 / 方格城市
夜路 / 出城大道
红色拂尘
冰雪
火焰
校园
法院
```

其中重点：

```text
手机短信（老师好美）
vs
手机（手机）
```

未来 Object Identity Review 应判断：

- “手机短信”是否应作为 `手机` 的 manifestation；
- 或作为独立的数字文字媒介 canonical object；
- 与 QX16.1 书信之间是否形成“异步私人通信”object family。

当前不提前处理。

## 09｜300 条关系里程碑

本批后：

```text
FORMAL_QX_RELATIONS = 300
FORMAL_WORKS_WITH_QX = 93
```

从大批次模式启动以来：

```text
Batch 014 = 7 works / 21 relations
Batch 015 = 10 works / 27 relations
Batch 016 = 12 works / 32 relations
Batch 017 = 9 reviewed / 20 relations
```

累计审查：

```text
CONTINUOUS_LOOP_REVIEWED_WORKS = 38
CONTINUOUS_LOOP_RELATIONS = 100
```

说明扩大吞吐量后，Admission Gate 仍能保持：

```text
1 relation works
2 relation works
3 relation works
0 relation works
```

均可合法存在。

## 10｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 300
FORMAL_WORKS_WITH_QX = 93
ZERO_QX_REVIEWED_WORKS_THIS_BATCH = 狼牙
NEW_QX_LEAF = NO
TOPIC_DERIVED_DATA_REFRESH = DEFERRED
SHORT_STORY_COLLECTION_DEFERRED = 夜晚的潜水艇
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
NEXT_BATCH = 018
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次016]]
- [[QX16.1 文学中的书信]]
