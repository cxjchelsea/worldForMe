---
id: WL-QC3-CANDIDATE-POOL-V1
type: literature_governance
system_role: work_knowledge_network
scope: QC3
status: ACTIVE_V1
version: "1.3"
---

# QC3 候选文化模型池 V1

> 管理“可能值得建设成 QC3 正式文化模型”的对象。候选池不是正式 taxonomy；只有通过 Admission Gate 的对象才进入 Topic Build。

## 1. 状态生命周期

```text
SEED
→ NEEDS_EVIDENCE
→ READY_FOR_ADMISSION
→ PILOT
→ ACCEPTED
→ DEFERRED / REJECTED
```

## 2. 当前 QC3.1 管理对象

| 候选 | 来源 | 当前状态 | 说明 |
|---|---|---|---|
| 欧洲骑士英雄模型 | QT8.3.2 | **ACCEPTED** | Pilot 1；强 QC1.2 上游样板 |
| 侠／江湖英雄模型 | QT8.3.1 | **ACCEPTED** | Pilot 2；无单一 QC1.2 上游样板 |
| 古希腊英雄模型 | 新增压力测试 | READY_FOR_ADMISSION | 后续按阅读需求决定是否建设 |
| 日本武士／剑豪英雄模型 | QT8.3.3 | NEEDS_EVIDENCE | 区分历史武士、武士道建构与文学形象 |
| 美国西部 cowboy / outlaw 模型 | QT8.3.4 | NEEDS_EVIDENCE | frontier myth / Western / outlaw 边界复杂 |
| 欧洲剑客／Swashbuckler 英雄模型 | QT8.3.5 | NEEDS_EVIDENCE | 与冒险类型史高度重叠 |
| Robin Hood / social bandit 模型 | QT8.3.6 | NEEDS_EVIDENCE | 人物传统与上位法外英雄模型需拆 |
| 海盗／海洋法外者模型 | QT8.3.7 | NEEDS_EVIDENCE | 防止退化成题材清单 |
| Gaucho 英雄文化模型 | QT8.3.8 | NEEDS_EVIDENCE | 需验证区域模型复用价值 |

另有：革命英雄、超级英雄继续 `DEFERRED`。

## 3. 两 Pilot 验证结果

### Pilot 1：欧洲骑士

```text
强 QC1.2 具体传统
+ QC2 组件
+ 中世纪宫廷／主君／宗教秩序
→ 骑士文化模型
```

### Pilot 2：侠／江湖

```text
多层中国来源环境
+ QC2 法外正义／复仇／武人共同体等
+ 历史社会条件
+ QT 武侠接口
→ 侠／义／师徒门派／江湖／国家法模型
```

两者社会结构差异显著，但同一 QC3 模型结构均可成立，因此：

```text
QC3_CULTURAL_MODEL_TEMPLATE = VALIDATED_V1
```

模板：[[QC3 文化模型专题模板 V1]]。

## 4. Admission Gate

```text
A1 可识别历史社会基底
A2 稳定角色 / 关系 / 伦理 / 空间结构
A3 跨时期叙事或媒介生命
A4 超出单一 QC2 component / 单一人物 / 单一 genre
A5 可连接 QC1 / QC2 / Work 等多个证据入口
A6 能解释现实与文化神话之间的距离
```

4/6 可研究；5/6 高优先级；6/6 强候选。

**A5 不要求存在一个单一 QC1.2.x。**第二 Pilot 已验证多来源输入同样合法。

## 5. QT8.3 迁移原则

```text
文化角色／伦理／社会秩序模型 → QC3
文学类型／文类生产机制       → QT
命名人物与具体叙事生命       → QC1
真实制度与社会运行           → 历史领域
```

→ [[QT8.3 → QC3.1 Migration Review V1]]

## 6. 当前决策

```text
QC3_TAXONOMY = NOT_FROZEN
QC3_CULTURAL_MODEL_TEMPLATE = VALIDATED_V1
QT83_MIGRATION = PASS
QC31_MANAGED_MODELS = 9
FORMAL_MODEL_COUNT = 2
EUROPEAN_KNIGHT_MODEL = ACCEPTED
XIA_JIANGHU_MODEL = ACCEPTED
NEXT_BUILD = READING_DRIVEN
```

现在不再为了验证架构继续批量接受候选。后续按真实阅读、QC1/QC2 新增和高复用缺口增量建设。