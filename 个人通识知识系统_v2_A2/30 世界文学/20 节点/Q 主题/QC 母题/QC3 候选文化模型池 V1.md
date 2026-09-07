---
id: WL-QC3-CANDIDATE-POOL-V1
type: literature_governance
scope: QC3
status: ACTIVE_V1
version: "1.0"
---

# QC3 候选文化模型池 V1

> 用于管理“可能值得建设成 QC3 正式文化模型”的对象。候选池不是正式 taxonomy；只有通过准入 Gate 的对象才进入 Topic Build。

## 1. 候选字段

每个候选至少记录：

```text
candidate_name
candidate_family
historical_basis
role_ethic_structure
cross_period_life
qc1_links
qc2_links
work_readiness
reuse_value
overlap_risk
admission_score
status
```

建议状态：

```text
SEED
→ NEEDS_EVIDENCE
→ READY_FOR_ADMISSION
→ PILOT
→ ACCEPTED
→ DEFERRED
→ REJECTED
```

## 2. 当前首批候选

| 候选 | 候选族 | 历史社会基底 | 稳定角色/伦理/空间 | 跨时期生命 | 现有 QC1/QC2 可接性 | 复用价值 | 风险 | 当前状态 |
|---|---|---|---|---|---|---|---|---|
| 古希腊英雄模型 | 英雄文化模型 | 高 | 高 | 高 | 高 | 高 | 容易与 QC2“英雄 archetype”重叠 | READY_FOR_ADMISSION |
| 欧洲骑士英雄模型 | 英雄文化模型 | 高 | 高 | 高 | 高 | 高 | 容易滑向制度史或“骑士文学”类型史 | PILOT |
| 侠／江湖英雄模型 | 英雄文化模型 | 高 | 高 | 高 | 中—高 | 高 | 容易与武侠 QT、真实侠史混淆 | READY_FOR_ADMISSION |
| 日本武士／剑豪英雄模型 | 英雄文化模型 | 高 | 高 | 高 | 中 | 高 | “武士道”后世建构需严格区分 | NEEDS_EVIDENCE |
| 美国西部 cowboy / outlaw 模型 | 英雄文化模型 | 高 | 高 | 高 | 中 | 高 | cowboy / outlaw / frontier myth 边界复杂 | NEEDS_EVIDENCE |
| Robin Hood / social bandit 模型 | 英雄文化模型 | 中—高 | 高 | 高 | 高 | 高 | 命名人物传统与社会匪徒模型边界需拆 | NEEDS_EVIDENCE |
| 海盗／海洋法外者模型 | 法外与边疆模型 | 高 | 中—高 | 高 | 中 | 中—高 | 容易变成题材清单 | SEED |
| Gaucho 文化英雄模型 | 边疆文化模型 | 高 | 高 | 高 | 中 | 中—高 | 区域性强，需验证跨作品复用价值 | SEED |
| 革命英雄模型 | 政治英雄模型 | 高 | 高 | 高 | 中 | 高 | 跨文化范围过宽，需先限定历史语境 | DEFERRED |
| 超级英雄模型 | 现代媒介英雄模型 | 中 | 高 | 高 | 中—高 | 高 | 更接近现代媒介/类型系统，需验证是否属于 QC3 而非 QT | DEFERRED |

## 3. 首轮 Pilot 策略

不同时建设全部候选。第一轮只做：

```text
P1 欧洲骑士英雄模型
P2 古希腊英雄模型 或 侠／江湖英雄模型
```

选择理由：

- P1 便于直接连接现有 QC1.2.3 亚瑟王叙事传统与大量 QC2 组件；
- P2 应与 P1 在社会结构、伦理和叙事生产机制上有明显差异，用于压力测试 QC3 模型是否具有跨文化解释力。

## 4. Admission Gate

每个候选按 6 项检查：

```text
A1 可识别历史社会基底
A2 稳定角色 / 关系 / 伦理 / 空间结构
A3 跨时期叙事或媒介生命
A4 超出单一 QC2 component / 单一人物 / 单一 genre
A5 可连接多个 QC1 / QC2 / Work
A6 能解释现实与文化神话之间的距离
```

判定建议：

```text
4/6 = 可进入 Admission Research
5/6 = 高优先级
6/6 = 强 Pilot 候选
```

## 5. 与 QC1 / QC2 / QT / QH / 历史层的边界

```text
来源与文本生命史
→ QC1

可复用叙事组件
→ QC2

历史化的角色—伦理—秩序文化模型
→ QC3

文学类型
→ QT

抽象主题问题
→ QH

真实制度如何运作
→ 历史 / 制度史
```

候选只有在 QC3 层存在明显独立解释增量时才准入。

## 6. 当前决策

```text
QC3_TAXONOMY = NOT_FROZEN
HERO_MODEL_CLUSTER = PILOT
EUROPEAN_KNIGHT_MODEL = FIRST_PILOT
SECOND_PILOT = TO_BE_SELECTED_AFTER_P1_REVIEW
```

本池只做候选治理，不代表其中所有对象都会成为正式 QC3 节点。
