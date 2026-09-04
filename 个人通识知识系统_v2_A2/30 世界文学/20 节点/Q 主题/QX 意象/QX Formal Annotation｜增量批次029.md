---
id: WL-QX-FORMAL-ANNOTATION-029
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次029
code: QX-ANNOTATION-029
axis: Q
facet: QX
status: PARTIAL_UPSTREAM_RECONCILIATION
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次029

> 本批开始执行 Batch028 指定的 `UPSTREAM RECONCILIATION`：先恢复 R3.5 已确认已读、但中央 `40 作品` 缺失的独立 Work，再按现行 Admission Gate 做 QX。不上推其他轴的推断元数据。

## 01｜当前累计

```text
BATCH_029_RECOVERED_WORKS = 6
BATCH_029_FORMAL_QX_WORKS = 3
BATCH_029_ZERO_QX_WORKS = 3
BATCH_029_FORMAL_RELATIONS = 6
FORMAL_QX_RELATIONS_BEFORE = 356
FORMAL_QX_RELATIONS_AFTER = 362
FORMAL_WORKS_WITH_QX_BEFORE = 117
FORMAL_WORKS_WITH_QX_AFTER = 120
UPSTREAM_WORK_BUILD_GAP_REMAINING = 4
```

## 02｜第一组：FORMAL_QX

### 《你当像鸟飞往你的山》

中央 Work：`40 作品/你当像鸟飞往你的山.md`

通过 Gate：

```text
巴克峰 / 山 → QX6 / dominant
废料场 → QX8 / core
```

巴克峰是童年家庭世界的固定空间中心，并持续连接故乡、家庭身份与归返；废料场长期组织童年劳动、父权关系和身体风险。

### 《苏菲的世界》

中央 Work：`40 作品/苏菲的世界.md`

通过 Gate：

```text
书信 / 明信片 → QX16.1 / dominant
书 / 书稿 → QX16 / dominant
```

前者启动并持续组织哲学课程与跨叙事层级谜团；后者最终成为人物意识到自身虚构存在状态的结构性对象。

## 03｜第二组：《鱼翅与花椒》FORMAL_QX

中央 Work：`40 作品/鱼翅与花椒.md`

通过 Gate：

```text
花椒 → QX13 / core
鱼翅 → QX13 / significant
```

两者并非仅因出现在书名而入库。作者对书名选择有明确解释：花椒代表其进入四川饮食文化时高度独特的感官经验；鱼翅则连接珍贵食材、文化陌生性以及生态 / 消费伦理争议。两者均与整部饮食旅行回忆录的跨文化经验稳定绑定并具有强辨识度。

## 04｜第二组：ZERO_QX

### 《看见》

```text
QX_REVIEW = COMPLETE
RESULT = ZERO_QX
```

新闻现场、采访设备、镜头等均可被解释，但目前没有单一具体对象获得足够的作品内部复现、结构绑定或辨识度证据。尤其不把书名“看见”直接推导为视觉意象。

### 《天才在左，疯子在右》

```text
QX_REVIEW = COMPLETE
RESULT = ZERO_QX
```

全书由多组访谈 / 个案构成，具体物象主要依附于局部个案；没有证据支持某个具体对象在全书层面稳定承担结构作用。标题“左 / 右”是概念性对举，不按空间意象入库。

### 《我的一个世纪（增订版）》

```text
QX_REVIEW = COMPLETE
RESULT = ZERO_QX
```

青楼、家庭、川菜馆 / 锦江饭店等地点对人物生平重要，但“重要人生地点”不自动等于文学意象。当前没有足够作品内部证据证明某一对象在整部回忆录中达到 Gate。

## 05｜上游恢复策略

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

## 06｜剩余 UPSTREAM_WORK_BUILD_GAP

```text
盗墓笔记：七星鲁王宫
临界·爵迹I
盐镇
金鸡
```

当前：

```text
UPSTREAM_WORK_BUILD_GAP_REMAINING = 4
QX_DECISION = NOT_YET_EVALUATED
```

## 07｜下一步

继续 Batch029 第三组，完成上述 4 个 upstream gap。完成后，不立即扩张 ontology，而转入：

```text
SERIES / VOLUME GRANULARITY
→ STORY-LEVEL READING MAP
→ EDITORIAL COLLECTION VERSION MAP
→ FULL 173-RECORD COVERAGE RECOUNT
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次028]]
