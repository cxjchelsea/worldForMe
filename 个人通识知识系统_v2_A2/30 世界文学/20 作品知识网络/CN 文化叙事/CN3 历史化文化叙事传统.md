---
id: WL-CN3
legacy_id: WL-QC3
type: literature_node
name: 历史化文化叙事传统
code: CN3
legacy_code: QC3
namespace: CN
legacy_axis: Q
system_role: work_knowledge_network
parent: WL-CN
level: 3
node_kind: taxonomy_branch
status: TAXONOMY_CANDIDATE_REVIEW
source_version: "3.1-qc3-taxonomy-candidate-pool-v1"
---

# CN3 历史化文化叙事传统

> 路径：作品知识网络 → CN 母题与叙事组件 → **CN3 历史化文化叙事传统**

## 一句话理解

CN3 研究：**CN1 的叙事资源与 CN2 的可复用组件进入具体历史社会后，如何与制度、阶层、伦理、空间经验和媒介传统结合，形成稳定的文化角色世界、社会想象与后世可持续重写的文化模型。**

```text
CN1 = 传统从哪里来
CN2 = 由哪些组件构成
CN3 = 这些组件在具体社会中被组织成什么文化模型
```

## 已验证的文化模型模板

[[CN3 文化模型专题模板 V1]] 已由两个差异明显的正式 Pilot 验证：

- 欧洲骑士英雄模型；
- 侠／江湖英雄模型。

因此以下五项已经冻结为**每个具体文化模型内部的分析维度**，而不是平行一级 taxonomy：

1. 角色；
2. 社会关系；
3. 价值／伦理；
4. 秩序／空间；
5. 后世重构。

## CN3 一级 taxonomy 当前原则

一级簇不按“角色/关系/伦理/空间/应用”切分，而按：

> **社会反复把哪一类角色、关系与秩序组织成可持续重写的文化模型世界？**

当前不批量创建 CN3.2、CN3.3……，而先进入一级簇候选审查。

## 已接受一级簇

### [[CN3.1 英雄文化模型]]

当前已验证两个正式模型：

- 欧洲骑士英雄模型；
- 侠／江湖英雄模型。

旧 `TY8.3 英雄、边疆与法外者文化传统` 的 8 个历史资产已完成语义迁移；文化模型进入 CN3，文学类型继续由 TY 承担。

## 当前一级簇候选

### P1｜READY_FOR_ADMISSION

- 君王、统治者与合法秩序模型；
- 家庭、亲属与代际角色模型。

### P2｜READY_FOR_ADMISSION

- 爱情、婚姻与性别角色模型；
- 宗教角色与神圣生活模型；
- 知识人、智者与文化权威模型。

### P3｜NEEDS_BOUNDARY

- 反叛者、革命者与政治行动模型；
- 社会身份、阶层与边缘角色模型。

详细 Gate 与边界见：[[CN3 一级文化模型簇候选池 V1]]。

## CN3 不是什么

```text
CN3 ≠ 某国文化百科
CN3 ≠ 单一 motif
CN3 ≠ 单一人物传说
CN3 ≠ 文学类型目录
CN3 ≠ 真实制度史本身
CN3 ≠ 抽象主题讨论
```

真实制度 → 历史；文学类型 → TY；抽象主题 → TH；可复用组件 → CN2。

## 标准解释链

```text
CN1.1 来源环境 / CN1.2 具体叙事传统
              +
CN2 motif / archetype / plot_pattern / symbol
              +
历史制度 / 阶层 / 伦理 / 空间 / 媒介
              ↓
CN3 历史化文化模型
              ↓
40 作品 / TY / TH / R / T / 后世应用
```

不是强制线性链；允许 CN1.1、CN1.2、CN2、Work 分别直接提供证据。

## 当前治理入口

- [[CN3 文化模型专题模板 V1]]
- [[CN3 一级文化模型簇候选池 V1]]
- [[CN3 候选文化模型池 V1]]
- [[CN 总体架构与建设规范 V2]]

## 当前状态

```text
CN3_CULTURAL_MODEL_TEMPLATE = VALIDATED_V1
CN3.1_HERO_CLUSTER = ACCEPTED_CLUSTER
FORMAL_MODEL_PILOTS = 2
CN3_TAXONOMY = CANDIDATE_REVIEW
BULK_BUILD = NO
NEXT_CLUSTER_PILOT = 君王模型 OR 家庭亲属模型
```

现阶段目标不是填满 CN3，而是用一个“非英雄”一级簇进一步验证 taxonomy 边界；通过后再决定是否冻结 CN3 总骨架。
