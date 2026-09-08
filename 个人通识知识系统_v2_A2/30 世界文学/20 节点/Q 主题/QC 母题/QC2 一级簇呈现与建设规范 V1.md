---
id: WL-QC2-CLUSTER-PRESENTATION-SPEC-V1
type: literature_governance
system_role: work_knowledge_network
scope: QC2
status: ACTIVE_V1
version: "1.1"
---
# QC2 一级簇呈现与建设规范 V1

## 目的

QC2.1–QC2.20 是**一级问题域／母题簇导航容器**，不是单一母题，也不是直接承载全部研究细节的重型专题。

本规范解决三个问题：

1. **人打开 QC2.x 时要能迅速看懂**：这个问题域研究什么、里面有什么组件、来自哪些传统、怎么读；
2. **系统仍保留严谨治理**：component acceptance、source evidence、coverage review、stage freeze、reopen gate 等继续存在，但不占据认知主页主体；
3. **作品层必须可见**：QC2.x 必须提供中央 `40 作品` 的投影视图，使“来源传统—叙事传统—组件—作品”在产品层闭合。

核心原则：

```text
前台认知层 = 可读、可导航、可理解
结构化视图 = component + work projection
后台治理层 = 可审查、可维护、可冻结
```

---

# 1. QC2.x 的正式定位

每个 QC2.x 都是：

```text
resource_type: taxonomy_cluster / problem_domain
```

它负责组织四类正式 component：

```text
motif
archetype
plot_pattern
symbol
```

一级簇本身不等于这四类中的任何一种。

允许：

```text
one primary cluster + multiple secondary clusters
```

不要求四类 component 数量均衡，也不为了“填满四格”强建对象。

---

# 2. 一级簇主页必须回答的六个问题

QC2.x 的人类可读主页优先回答：

1. **这个问题域在研究什么？**
2. **当前有哪些正式 component？**
3. **这些 component 分别是什么类型？**
4. **它们来自哪些 QC1.1 来源传统？**
5. **它们在哪些 QC1.2 具体叙事传统中被组织、定型或强化？**
6. **我通过哪些文本／作品／阅读路线最容易理解它们？**

主页不以治理状态码作为主要内容。

---

# 3. 一级簇主页标准结构

```text
# QC2.x 标题

## 一句话理解
## 这个问题域关心什么
## 当前核心组件
### 母题 Motif
### 文化原型 Archetype
### 叙事结构 Plot Pattern
### 意象／符号 Symbol
## 这些组件之间是什么关系
## 来源传统（QC1.1）
## 具体叙事传统（QC1.2）
## 典型文本／作品与阅读入口
## 推荐理解顺序
## 产品入口
## 维护与治理
```

没有内容的类型应明确写“当前无必须独立建立的对象”，而不是强行补齐。

---

# 4. QC1 → QC2 双输入规则

QC2 不是只接 QC1.1，也不是只接 QC1.2。

## 4.1 QC1.1 的职责：来源环境

QC1.1 回答：

> 这个 component 出现在哪些文化／宗教／区域叙事资源环境中？

典型映射：

```text
QC1.1 source_tradition
→ source material / source witness
→ QC2 component
```

QC1.1 可以直接向 QC2 提供 component 候选，不要求先经过 QC1.2。

## 4.2 QC1.2 的职责：具体传统生命史

QC1.2 回答：

> 这个 component 在哪些可识别的故事、人物、循环或集合传统中被组织、定型、反复调用或发生重要变体？

典型映射：

```text
QC1.2 narrative tradition
→ stable use / transformation
→ QC2 component
```

## 4.3 标准链路

理想情况下，一个 QC2 component 同时可连接：

```text
QC1.1 来源传统
      ↓
QC1.2 具体叙事传统（若存在）
      ↓
QC2 component
      ↓
40 作品 / work reference
```

但这不是强制线性链。合法情况包括：

```text
QC1.1 → QC2
QC1.2 → QC2
QC1.1 + QC1.2 → QC2
```

---

# 5. component 页面与一级簇主页的职责分离

一级簇主页只做导航与认知总览。

具体 component 页面承担：

```text
定义与边界
required invariants / stable meanings / core slots
来源与证据
跨传统比较
component relations
后世重写与作品实例
阅读与研究
```

不得把所有 component 研究细节复制到一级簇主页。

---

# 6. 作品与文本的呈现规则

一级簇主页中的“典型文本／作品”只列：

```text
早期／来源见证
关键定型文本
推荐阅读作品
```

不做百科书单。

每个 QC2.x 必须存在 `03 作品.base`，只投影中央 `40 作品` 的合法 work 实体；它可以因尚未完成 work backfill 而暂时为空，但**不可以因为当前为空而省略产品入口**。

严格区分：

```text
source witness ≠ work
QC1.1 tradition ≠ work
QC1.2 tradition ≠ work
QC2 component ≠ work
```

中央 `40 作品` 仍是 work 的唯一事实源；非作品材料继续留在 source/reference/witness 层。

作品 Base 的推荐匹配方式：

```text
work.qc2_clusters contains current_cluster
OR
work.topics contains one of current cluster component topic ids
```

不为填满 Works Base 创造假作品，不把 source witness 升格成 work。

---

# 7. Canvas 规则

一级簇 Canvas 是认知关系图，不是文件树镜像。

应优先表达：

```text
QC1.1 来源环境
QC1.2 具体叙事传统（若存在）
        ↓
QC2.x cluster
        ↓
component type groups
        ↓
具体 components
        ↓
03 作品.base
```

Canvas 的 `file` 路径必须使用 **Obsidian 库根相对路径**。当前库根是仓库根，世界文学文件必须写成：

```text
个人通识知识系统_v2_A2/30 世界文学/...
```

禁止只写到中间目录，例如：

```text
30 世界文学/...
30 专题/...
```

Canvas 更新后必须至少做一次实际路径核对，不能仅验证 JSON 语法。

---

# 8. 后台治理层

下列内容保留，但从一级簇主页主体移出：

```text
Component Inventory
Candidate Triage
Source Readiness
Admission / Acceptance Review
Coverage Review
Stage Freeze Review
Reopen Gate
Data-layer diagnostics
```

推荐通过统一“治理索引”页集中访问，不要求立即物理移动历史文件，以免破坏已有链接。

---

# 9. 推荐产品壳

```text
00 QC2.x 一级簇主页.md
01 QC2.x 组件关系.canvas
02 QC2.x 组件.base
03 QC2.x 作品.base
90 治理/00 QC2.x 治理索引.md

具体 component/
  00 component 主页.md
  01 component.canvas
  02 结构.base
  03 证据关系.base
  10 核心结构/
  11 来源与证据/
  12 跨传统关系/
  13 后世重写与阅读/
  20 数据层/
```

已有专题无需为了目录形式而强制搬迁；冻结的是职责，不是物理文件名。

---

# 10. 建设流程

```text
已有 QC1.1 / QC1.2 / 作品材料
→ 抽取 candidate component
→ 去重与边界判断
→ 判定 component_type
→ 指定 primary / secondary cluster
→ source readiness
→ component build
→ acceptance
→ work backfill / Works Base projection
→ cluster coverage review
→ stage freeze
```

不得按 QC2.1 → QC2.2 → … → QC2.20 的顺序机械填满。

---

# 11. QC2.x Stage Freeze 的含义

Stage Freeze 表示：

- 当前核心问题已有足够代表性 component 覆盖；
- 没有明确、真实的 required component gap；
- 页面结构与数据接口足以服务当前阅读；
- 后续只因新证据、真实阅读缺口或模型冲突而 reopen。

Stage Freeze 不等于：

- 候选已穷尽；
- 所有文化都已覆盖；
- 四类 component 都必须存在；
- Works Base 必须已经非空；
- 阅读和 source enrichment 停止。

---

# 12. 人类可读性与产品完整性 Gate

一个 QC2.x 主页合格，至少应满足：

```text
30 秒内能回答：
- 这个簇讲什么？
- 里面现在有什么？
- 每个对象是什么类型？
- 它们大致来自哪里？
- 我先看什么？
```

同时产品壳必须通过：

```text
HOME_PAGE      PASS
CANVAS_LINKS   PASS
COMPONENT_BASE PASS
WORKS_BASE     PASS
GOVERNANCE     PASS
```

如果用户必须先理解 `M5 / Tier A / PASS / CLOSED / reopen gate` 才能知道专题内容，或 Canvas 大量出现未找到文件，则呈现不合格。

---

# 13. V1 样板

首个正式样板：

```text
QC2.1 创世、宇宙与世界秩序
```

QC2.1 已有六个经过验证的 active components，适合用于冻结一级簇的前台呈现职责；其历史治理材料继续保留为后台证据。