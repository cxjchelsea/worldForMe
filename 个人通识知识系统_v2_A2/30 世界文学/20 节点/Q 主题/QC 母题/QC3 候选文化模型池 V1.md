---
id: WL-QC3-CANDIDATE-POOL-V1
type: literature_governance
scope: QC3
status: ACTIVE_V1
version: "1.2"
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
qc1_links / qc1_readiness
qc2_links / qc2_readiness
work_readiness
reuse_value
overlap_risk
admission_score
status
legacy_code（如来自旧体系）
migrated_from（如来自旧体系）
migration_mode（如需拆分职责）
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

## 2. 当前英雄文化模型候选

当前 QC3.1 管理 9 个英雄文化模型对象：8 个来自旧 QT8.3，1 个为新增压力测试。欧洲骑士已通过准入并进入正式模型，候选卡保留为历史记录与导航。

| 候选 | 来源 | 历史社会基底 | 稳定角色/伦理/空间 | 跨时期生命 | QC1/QC2可接性 | 复用价值 | 当前状态 |
|---|---|---|---|---|---|---|---|
| 古希腊英雄模型 | 新增压力测试 | 高 | 高 | 高 | 高 | 高 | READY_FOR_ADMISSION |
| 欧洲骑士英雄模型 | QT8.3.2 | 高 | 高 | 高 | 高 | 高 | **ACCEPTED** |
| 侠／江湖英雄模型 | QT8.3.1 | 高 | 高 | 高 | 中—高 | 高 | READY_FOR_ADMISSION |
| 日本武士／剑豪英雄模型 | QT8.3.3 | 高 | 高 | 高 | 中 | 高 | NEEDS_EVIDENCE |
| 美国西部 cowboy / outlaw 模型 | QT8.3.4 | 高 | 高 | 高 | 中 | 高 | NEEDS_EVIDENCE |
| 欧洲剑客／Swashbuckler 英雄模型 | QT8.3.5 | 中—高 | 高 | 高 | 中 | 中—高 | NEEDS_EVIDENCE |
| Robin Hood / social bandit 模型 | QT8.3.6 | 中—高 | 高 | 高 | 高 | 高 | NEEDS_EVIDENCE |
| 海盗／海洋法外者模型 | QT8.3.7 | 高 | 中—高 | 高 | 中 | 中—高 | NEEDS_EVIDENCE |
| Gaucho 英雄文化模型 | QT8.3.8 | 高 | 中—高 | 高 | 中 | 中—高 | NEEDS_EVIDENCE |

另有：

- 革命英雄模型：DEFERRED；
- 超级英雄模型：DEFERRED。

## 3. QT8.3 迁移原则

旧 QT8.3 的内容不是废弃，而是语义拆分：

```text
文化角色／伦理／社会秩序模型 → QC3
文学类型／文类生产机制       → QT
命名人物与具体叙事生命       → QC1
真实制度与社会运行           → 历史领域
```

→ [[QT8.3 → QC3.1 Migration Review V1]]

旧 QT8.3.x 已改为 `MIGRATED_LEGACY` 兼容入口，后续不再作为文化模型的新内容建设位置。

## 4. 首轮 Pilot 策略

```text
P1 欧洲骑士英雄模型 = ACCEPTED_PILOT_V1
P2 古希腊英雄模型 或 侠／江湖英雄模型 = NEXT
```

P1 已验证：

- QC1.1 / QC1.2 可作为来源与具体传统输入；
- QC2 可作为组件星座输入而不复制定义；
- 历史社会条件可以作为解释条件而不变成制度百科；
- 中央 40 作品可通过模型字段投影进独立 Works Base；
- QC3 与 QT / QC1 / 历史层可以明确分工。

P2 应与 P1 在社会结构、伦理与叙事生产机制上有明显差异，用于压力测试模板可迁移性。

## 5. Admission Gate

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

## 6. 当前决策

```text
QC3_TAXONOMY = NOT_FROZEN
HERO_MODEL_CLUSTER = PILOT
QT83_MIGRATION = PASS
QT83_LEGACY_CHILDREN = 8
QC31_MANAGED_MODELS = 9
EUROPEAN_KNIGHT_MODEL = ACCEPTED_PILOT_V1
FORMAL_MODEL_COUNT = 1
SECOND_PILOT = GREEK_OR_XIA
```
