---
id: WL-QX-FORMAL-ANNOTATION-029
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次029
code: QX-ANNOTATION-029
axis: Q
facet: QX
status: COMPLETE_UPSTREAM_RECONCILIATION
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次029

> 本批完成 Batch028 指定的 `UPSTREAM RECONCILIATION`：恢复 R3.5 已确认已读、但中央 `40 作品` 缺失的 10 个独立 Work，并逐项按现行 Admission Gate 完成 QX 审查。不上推其他轴的推断元数据。

## 01｜最终计数

```text
BATCH_029_RECOVERED_WORKS = 10
BATCH_029_FORMAL_QX_WORKS = 7
BATCH_029_ZERO_QX_WORKS = 3
BATCH_029_FORMAL_RELATIONS = 12
FORMAL_QX_RELATIONS_BEFORE = 356
FORMAL_QX_RELATIONS_AFTER = 368
FORMAL_WORKS_WITH_QX_BEFORE = 117
FORMAL_WORKS_WITH_QX_AFTER = 124
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
UPSTREAM_RECONCILIATION = CLOSED
```

## 02｜FORMAL_QX：7部

### 《你当像鸟飞往你的山》

```text
巴克峰 / 山 → QX6 / dominant
废料场 → QX8 / core
```

巴克峰持续连接童年家庭世界、身份与归返；废料场长期组织劳动、父权关系和身体风险。

### 《苏菲的世界》

```text
书信 / 明信片 → QX16.1 / dominant
书 / 书稿 → QX16 / dominant
```

书信启动并持续组织哲学课程与跨叙事层级谜团；书稿最终直接决定人物对自身虚构存在状态的认知。

### 《鱼翅与花椒》

```text
花椒 → QX13 / core
鱼翅 → QX13 / significant
```

两者均与整部饮食旅行回忆录的跨文化经验稳定绑定并具有强辨识度；不是仅因出现在书名而入库。

### 《盗墓笔记：七星鲁王宫》

```text
七星鲁王宫 / 地下墓穴 → QX18 / dominant
九头蛇柏 → QX4 / core
玉俑 → QX15 / core
```

墓穴空间构成整部行动的空间骨架；九头蛇柏主动改变人物行动条件；玉俑以 `singular_pivotal` 方式集中长生、墓主与活尸谜团。

### 《临界·爵迹I》

```text
爵印 → QX9 / core
```

爵印作为身体上的可见标记，稳定绑定魂术师身份、权力等级、王爵—使徒关系以及魂器 / 魂兽系统，满足 recurrence + binding + structural。

### 《盐镇》

```text
盐镇 / 小镇 → QX8 / dominant
```

同一小镇把十二位女性的家庭、婚姻、阶层与城乡处境组织为相互勾连的熟人社会样本，因此是结构空间而非泛背景。

### 《金鸡》

```text
金色斗鸡 → QX5 / dominant
```

迪奥尼西奥由贫困走向财富和赌博世界的转折始于救治受伤斗鸡；斗鸡持续与人物命运、欲望和社会流动绑定，并直接构成标题对象与叙事发动机。

## 03｜ZERO_QX：3部

### 《看见》

```text
QX_REVIEW = COMPLETE
RESULT = ZERO_QX
```

新闻现场、采访设备、镜头等可被解释，但当前没有单一具体对象获得足够的作品内部复现、结构绑定或辨识度证据；不因书名“看见”反推视觉意象。

### 《天才在左，疯子在右》

```text
QX_REVIEW = COMPLETE
RESULT = ZERO_QX
```

全书由多组访谈 / 个案构成，具体物象主要依附于局部个案；标题“左 / 右”属于概念性对举，不按空间意象入库。

### 《我的一个世纪（增订版）》

```text
QX_REVIEW = COMPLETE
RESULT = ZERO_QX
```

青楼、家庭、川菜馆 / 锦江饭店等地点对人物生平重要，但重要人生地点不自动等于文学意象；当前不足以证明某一对象在整部回忆录中达到 Gate。

## 04｜上游恢复策略

```text
READ FACT
→ 只继承 R3.5 / corpus ledger 已确认的“已读”

BIBLIOGRAPHY
→ 只补可高置信确认的题名、作者、原题、年份

OTHER AXES
→ 不因 QX 修复而顺手推断 T/R/M/QH
→ 无上游证据则留空

QX
→ 必须独立通过 ADMISSION_GATE_V1
```

新建 Work 统一使用：

```text
verification_status = 需复核
bibliography_status = qx_recovered_minimal
```

这表示中央作品库其他维度仍待后续上游治理，不降低 QX Gate 的独立判断标准。

## 05｜UPSTREAM 收口

```text
盗墓笔记：七星鲁王宫 → FORMAL_QX / 3
临界·爵迹I → FORMAL_QX / 1
我的一个世纪（增订版） → ZERO_QX
你当像鸟飞往你的山 → FORMAL_QX / 2
看见 → ZERO_QX
天才在左，疯子在右 → ZERO_QX
盐镇 → FORMAL_QX / 1
鱼翅与花椒 → FORMAL_QX / 2
苏菲的世界 → FORMAL_QX / 2
金鸡 → FORMAL_QX / 1
```

因此：

```text
UPSTREAM_WORK_BUILD_GAP_TOTAL = 10
UPSTREAM_WORK_BUILD_GAP_REMAINING = 0
```

## 06｜下一阶段

Batch029 结束后不扩张 ontology，转入阅读粒度恢复：

```text
Stage 1: SERIES / VOLUME GRANULARITY
- 福尔摩斯探案全集
- 哈利·波特
- 龙族

Stage 2: STORY-LEVEL READING MAP
- 夜晚的潜水艇
- 机器人短篇全集
- 草
- 人类的群星闪耀时
- 哑舍
- 台北人
- 燃烧的原野
- 彷徨
- 呐喊
- 俗世奇人（足本）

Stage 3: EDITORIAL COLLECTION VERSION MAP
- 麦琪的礼物：欧·亨利短篇小说经典
- 莫泊桑短篇小说精选
- 欧·亨利短篇小说选
- 契诃夫短篇小说选
- 项链：莫泊桑中短篇小说选

Stage 4: FULL 173-RECORD COVERAGE RECOUNT
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次028]]
