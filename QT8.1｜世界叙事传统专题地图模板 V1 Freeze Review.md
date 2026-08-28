# QT8.1｜世界叙事传统专题地图模板 V1 Freeze Review

> Freeze Status: `QT8.1_TEMPLATE_V1_FROZEN`
>
> Review Result: `PASS`
>
> Freeze Branch: `feature/qt8-cultural-motif-restructure`
>
> Reviewed Template: `QT8.1｜世界叙事传统专题地图模板 V1.md`
>
> Reviewed Template Blob SHA: `4eee0f9d894385373f521e007a01a9940c02ccf0`
>
> Pilot: `QT8.1.2 希腊—罗马神话传统`
>
> Pilot State at Review: `PILOT_V1_REVISED`

---

## 1. Freeze 结论

QT8.1 V1 模板通过 Pilot Freeze Review。

本次冻结确认的是**模板结构、职责边界、对象模型和数据治理规则**，不是宣称 QT8.1.2 的内容已经穷尽，也不是冻结具体历史事实、书目或后世案例。

冻结后，后续 QT8.1.x 专题默认复用 V1；若新 Pilot 暴露出真正的跨传统结构性缺陷，应以 `V1.x / V2` 形式显式修订，不静默改变已冻结模板。

---

## 2. 稳定骨架验收

以下一级模块全部通过：

```text
10 核心结构
11 文本谱系
12 母题与跨文化关系
13 后世传播与阅读
```

### 10 核心结构

通过。能够稳定承载：

- 定义、范围与边界
- 历史文化环境
- 世界观与宇宙结构
- 人物与超自然存在系统
- 核心叙事循环与故事群
- 口传、仪式与表演机制
- 书写、编纂与经典化
- 内部演变与关键转折

Pilot 未发现需要新增第五个一级模块才能解释希腊—罗马传统的问题。

### 11 文本谱系

通过，且已完成 V0 → V1 的关键修订：

```text
11 文本谱系 = 解释层
03 文本.base = 数据层
```

专题—文本关系记录使用 `literature_topic_text_reference`；作品主节点继续保持唯一归属，关系记录仅保存其在当前传统中的角色。

### 12 QT8.2 映射

通过。固定区分：

```text
motif
archetype
plot_pattern
symbol
```

命名型文化原型、symbol 准入规则以及传播置信度均已形成治理边界。

### 13 后世传播与阅读

通过。后世传播只作为出口索引；原典阅读与现代研究入口分离，新增 `13.04 支撑研究书目` 后，研究支撑层不再缺位。

---

## 3. QT8.1 / QT8.2 / QT8.3 边界验收

通过。

```text
QT8.1 = 来源谱系
QT8.2 = 母题／文化原型／叙事结构／文化符号的横向抽象层
QT8.3 = 叙事资源在具体历史社会中形成的成熟文化传统层
```

`theme` 不进入 QT8.2 核心对象，继续主要由 QH facet 承担。

结构相似不自动解释为历史传播；Canvas 不画无证据推断边。

---

## 4. Pilot 结构验收

`QT8.1.2 希腊—罗马神话传统` 已具备完整 Pilot 包：

- 专题主页
- Canvas
- 结构 Base
- 文本 Base
- 10 核心结构
- 11 文本谱系
- 12 QT8.2 映射
- 13 后世传播、阅读与研究书目
- 首批专题—文本关系记录

Pilot 当前适合作为**模板验证案例和后续专题的结构参照**。

但 Pilot 内容仍保持开放：具体版本、文本年代、人物原型化证据、后世接受案例与研究书目可继续增补。

---

## 5. Base 验收

### 02 结构.base

`PASS`

职责是浏览专题结构节点，并可按核心结构、QT8.2 映射、后世传播等模块查看。

### 03 文本.base

`PASS`

已不再聚合文本说明页，而只聚合：

```yaml
type: literature_topic_text_reference
```

这是 V1 Freeze 的必要条件，现已满足。

---

## 6. Canvas 验收

`PASS`

总 Canvas 保持机制图而非人物百科图，核心关系为：

```text
主页
├─→ 核心叙事循环
└─→ 文本谱系

核心叙事循环 ─┐
               ├─→ QT8.2 映射 ─→ 后世传播
文本谱系 ──────┘
```

未发现需要为了“信息更多”而继续扩张总 Canvas 的必要。

---

## 7. 兼容性验收

`PASS`

旧 QT8 / QT9 文件保留为 `literature_redirect`，不再拥有 taxonomy `id/code`，因此可继续兼容旧 Obsidian 文件名链接，同时不会形成重复 taxonomy 节点。

兼容层属于迁移机制，不是新架构的一部分；冻结后继续保留，直到未来有独立的链接迁移与清理阶段。

---

## 8. Freeze 后允许变化的内容

以下内容**不属于模板冻结对象**，可以持续更新：

- 具体人物和故事材料
- 文本关系记录
- `canonical_work` 的回填
- 支撑研究书目
- 后世接受案例
- QT8.2 映射的实体数量
- 具体年代、版本和证据等级的核证
- 专题内部二级页面在不改变一级职责前提下的适配

以下内容若要改变，应视为模板版本升级：

- 10–13 一级职责
- 解释层／数据层分离原则
- QT8.2 四对象模型
- source figure 与 named archetype 的分离
- symbol 准入原则
- 传播置信度治理
- “一个主要归属地 + 多关系”的文本数据治理原则

---

## 9. 分支状态说明

Freeze Review 同时检查了当前分支相对 `main` 的 Git 状态。

当前 feature branch 与 main 已分叉：在 Freeze Review 时为 `ahead 29 / behind 47`，merge base 为 `1d1b76ef667a5075a2192abe5cd6dafd5cec8006`。

因此：

```text
QT8.1_TEMPLATE_V1_FROZEN = YES
CURRENT_BRANCH_READY_FOR_CONTENT_EXPANSION = YES
CURRENT_BRANCH_READY_FOR_DIRECT_MERGE_TO_MAIN = NO
```

模板冻结与分支可直接合并是两个不同问题。开始下一个 QT8.1 专题可以继续在此分支进行；但在未来创建 PR / 合并 main 前，应单独做一次 main 同步与冲突复核。

---

## 10. Final Decision

```text
QT8.1_TEMPLATE_V1_FREEZE_REVIEW = PASS
QT8.1_TEMPLATE_V1_STATUS = FROZEN
QT8.1.2_PILOT_STRUCTURE_STATUS = ACCEPTED_AS_REFERENCE_PILOT
QT8.1.2_CONTENT_STATUS = OPEN_FOR_INCREMENTAL_RESEARCH
BASE_STATUS = PASS
CANVAS_STATUS = PASS
COMPATIBILITY_REDIRECT_STATUS = PASS
DIRECT_MERGE_TO_MAIN = NOT_READY_BRANCH_DIVERGED
```

下一阶段默认使用 `QT8.1｜世界叙事传统专题地图模板 V1.md` 作为 QT8.1.x 新专题的固定结构基线。