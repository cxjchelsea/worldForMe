---
id: WL-TEMPLATE-QC-TRADITION-V2
type: literature_topic_template
name: QC 传统型专题地图模板 V2
status: FROZEN_V2_1
scope: QC narrative/cultural tradition topics
validated_by:
  - QC1.1.1 希伯来—圣经叙事传统
  - QC1.1.2 希腊—罗马神话传统
---

# QC 传统型专题地图模板 V2.1

> 适用于 QC 中以“某套文化叙事传统如何形成、保存、定型、传播与被重写”为核心问题的专题。V2.1 统一 R/T/M 的产品接口，同时保留 QC 自己的内部知识结构和研究数据层。

## 1. 固定产品外壳

每个正式 QC 传统型专题必须具有：

```text
00 专题主页.md
01 专题地图.canvas
02 专题结构.base
03 专题作品.base

10 核心结构/
11 内部文本与传统/
12 母题与跨文化关系/
13 后世传播与阅读/
20 数据层/
```

其中 `20 数据层` 不进入普通阅读导航，只保存专题关系、来源记录和其他研究支撑数据。

## 2. 四个产品文件职责

### 00 专题主页

回答：专题研究什么、边界在哪里、如何进入结构与阅读。主页必须直接链接 Canvas、结构 Base、作品 Base，并说明四个知识模块与数据层的职责。

### 01 专题地图 Canvas

最低稳定路径：

```text
主页
├─ 核心结构 ─→ 母题与跨文化关系 ─→ 后世传播／阅读
└─ 内部文本与传统 ─→ 作品 Base ─→ 后世传播／阅读
```

Canvas 是导航和机制图，不把“结构相似”画成未经证实的历史传播关系。

### 02 专题结构 Base

结构 Base 与成熟 R/T/M 专题保持同一接口：

- 按当前 `topic_id` 过滤；
- 直接读取显式 `structure_type_zh`；
- 使用 `dimension` 作为专题内部语义维度，并可通过公式映射为中文显示；
- 使用 `sequence / history_position / id` 作为排序与说明字段。

稳定模块词汇：

- `核心结构`
- `内部文本与传统`
- `母题与跨文化关系`
- `后世传播与阅读`

所有正式 QC 结构节点必须显式维护：

```yaml
topic_id: <current QC topic id>
structure_type_zh: 核心结构 | 内部文本与传统 | 母题与跨文化关系 | 后世传播与阅读
dimension: <topic-local dimension>
sequence: <local order>
history_position: <optional semantic role>
```

**目录位置不再作为正式模块语义来源。** 文件夹只承担物理组织职责；不得以 folder fallback 替代 `topic_id` 或 `structure_type_zh`。

禁止重新使用 `sequence < 20 / 20–29 / 30–39` 作为一级知识模块判定。

### 03 专题作品 Base

必须直接投影中央 `40 作品` 中的 `type: work`，不得以专题本地 relation/reference 页冒充作品实体。

专题归属由 scoped metadata 控制，例如 QC1.1.1：

```yaml
qc111_priority: ★ | ◆ | △
qc111_internal_tradition: <内部传统>
qc111_tradition_stage: <传统阶段>
qc111_role: <专题角色>
```

作品池必须区分“核心骨架”与“完整专题阅读池”：

- `★`：理解该传统不可绕开的核心入口；
- `◆`：补足内部传统、关键阶段与重要重写；
- `△`：扩展文本、旁支、背景或接受史入口。

不设机械统一数量，但不得把少量核心参考集直接当成完整专题覆盖。

作品 Base 至少提供：全部作品、核心 ★、重点 ◆、扩展 △、已读 / 未读、按内部传统、按传统阶段、按专题角色、T/M/G/Q 交叉视图与待校验视图。

## 3. 中央作品与本地关系层

一部作品只在 `40 作品` 保留一个 canonical work 实体。专题本地关系页位于：

```text
20 数据层/10 文本关系/
```

并在可以可靠对齐时维护：

```yaml
canonical_work: "[[中央作品节点]]"
source_status: canonical_aligned
```

抄本、译本、文本见证、资料汇编等若不适合作为独立文学作品，不为了让作品 Base 完整而强行转换成 `work`。

## 4. scoped metadata 规则

稳定四字段：

```text
<scope>_priority
<scope>_internal_tradition
<scope>_tradition_stage
<scope>_role
```

其中：

- priority 只允许 `★ / ◆ / △`；
- internal_tradition 回答“属于该专题内部哪套传统或文本群”；
- tradition_stage 回答“在该传统内部处于什么形成／定型／重写阶段”；
- role 回答“为什么值得在这个专题中读”。

同一作品可以同时拥有 T/R/M/G/Q/QC 等多个专题的 scoped metadata，互不覆盖。

## 5. 内部模块语义

### 10 核心结构

可包含：定义与边界、历史文化环境、世界观、角色与超自然存在、核心叙事循环、口传／仪式／表演、书写与编纂、内部演变。

### 11 内部文本与传统

解释文本谱系和内部传统，而不是复制书目百科。可按专题需要拆成源文本、早期见证、定型文本、内部文本群、阅读入口等。

### 12 母题与跨文化关系

负责与 QC 的 motif / archetype / plot_pattern / symbol 等对象连接，并严格区分：结构相似、可能传播、历史传播、明确引用、人物／名称借用、直接改编。

### 13 后世传播与阅读

容纳接受史出口、跨专题桥接、阅读路线和现代研究书目。不在单一传统专题内部无限重建完整世界文学史。

## 6. 验收门槛

一个 QC 传统型专题只有同时满足以下条件才可标记 Product PASS：

1. 四文件产品壳完整且链接有效；
2. 结构 Base 按当前 `topic_id` 查询，并由显式 `structure_type_zh` 组织；
3. 结构节点不依赖目录或 sequence 区间推断一级模块；
4. 作品 Base 查询真实中央作品；
5. 作品池具有 ★ / ◆ / △ 分层，且核心集不冒充完整覆盖；
6. 核心及重点作品具有 scoped metadata；
7. 可对齐的本地文本关系已连接 canonical work；
8. 同名作品已完成实体消歧；
9. Canvas 不包含未经证实的传播边；
10. 原典／作品阅读与现代支撑研究明确分层；
11. 历史研究数据可以保留 legacy provenance，但产品层使用当前 QC 编号；
12. 缺失证据必须显式留空或标记待核证，不为了完整度制造事实。

## 7. 当前治理状态

```text
QC_TRADITION_TOPIC_TEMPLATE_V2_1 = FROZEN
REFERENCE_TOPIC_1 = QC1.1.1
REFERENCE_TOPIC_2 = QC1.1.2
REFERENCE_TOPIC_WORK_POOL = 20 + 20（当前参考实现，不是全局硬性数量标准）
BULK_REUSE_FOR_QC1.1.3_TO_QC1.1.11 = AUTHORIZED_AFTER_PER_TOPIC_CONTENT_REVIEW
QT8.2_QT8.3_MIGRATION = OUT_OF_SCOPE
```
