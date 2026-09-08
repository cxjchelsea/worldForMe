---
id: WL-CN31-MIGRATION-TY83-V1
type: qc3_migration_review
cluster_id: WL-CN3.1
source_family: TY8.3
status: PASS
version: "1.0"
---

# TY8.3 → CN3.1 Migration Review V1

## 目的

旧 `TY8.3 英雄、边疆与法外者文化传统` 已经具备 CN3 的核心思想，但把“文化模型”“文学类型”“命名人物传统”放在同一层。此次迁移不丢弃旧内容，而是按当前 Q 轴职责重新分层。

```text
旧 TY8.3.x
      ↓ semantic migration
CN3 文化模型 + TY 类型接口 + 必要时 CN1 人物/叙事传统
```

## 迁移原则

1. 历史社会基底 + 稳定角色/伦理/空间 + 跨时期重构 → CN3；
2. 作品按何种文类/类型被生产和识别 → TY；
3. 围绕命名人物长期形成的故事生命 → CN1.2 figure_tradition；
4. 旧节点暂不删除，改为 `MIGRATED_LEGACY` 兼容入口；
5. 旧专题资产先保留，待新 CN3 模型正式 Topic Build 时逐项复用/拆分；
6. 不因迁移自动把候选升级为正式重型专题，仍需 CN3 Admission。

## 逐项审查

| 旧节点 | CN3 目标 | TY / CN1 保留职责 | migration_mode | 结论 |
|---|---|---|---|---|
| TY8.3.1 中国武侠 | 侠／江湖英雄模型 | TY 武侠继续承担类型史 | SPLIT_CN3_TY | PASS |
| TY8.3.2 欧洲骑士／骑士传奇 | 欧洲骑士英雄模型 | 骑士传奇作为类型/文类接口；亚瑟王等具体传统由 CN1.2 | SPLIT_CN3_TY_CN1 | PASS |
| TY8.3.3 日本武士／剑豪／时代小说 | 日本武士／剑豪英雄模型 | “时代小说”保留为 TY 接口，不等于武士文化模型 | SPLIT_CN3_TY | PASS |
| TY8.3.4 美国西部文学 | 美国西部 cowboy / outlaw 英雄模型 | Western / 西部文学保留为 TY 类型接口 | SPLIT_CN3_TY | PASS |
| TY8.3.5 欧洲剑客／披风剑客 | 欧洲剑客／Swashbuckler 英雄模型 | 披风剑客/冒险小说的类型史归 TY | SPLIT_CN3_TY | PASS |
| TY8.3.6 侠盗／Robin Hood／Outlaw | Robin Hood / social bandit / 法外英雄模型候选 | Robin Hood 命名人物传统优先由 CN1.2 承担 | SPLIT_CN3_CN1 | PASS |
| TY8.3.7 海盗／海洋冒险 | 海盗／海洋法外者英雄模型 | 海洋冒险作为 TY 类型接口 | SPLIT_CN3_TY | PASS |
| TY8.3.8 Gaucho 文学 | Gaucho 英雄文化模型 | Gaucho 文学的文类/区域文学史由 TY/R/T/作品层承接 | SPLIT_CN3_TY_RT | PASS |

## CN3.1 候选池迁移后范围

旧 TY8.3 贡献 8 个候选：

1. 侠／江湖英雄模型；
2. 欧洲骑士英雄模型；
3. 日本武士／剑豪英雄模型；
4. 美国西部 cowboy / outlaw 英雄模型；
5. 欧洲剑客／Swashbuckler 英雄模型；
6. Robin Hood / social bandit 模型；
7. 海盗／海洋法外者英雄模型；
8. Gaucho 英雄文化模型。

另保留一个**非旧 TY8.3 来源**的跨文化压力测试对象：

9. 古希腊英雄模型。

因此 CN3.1 当前候选池不是新造出来的一套目录，而是：

```text
旧 TY8.3 的 8 个历史资产
+
古希腊英雄模型压力测试
=
9 个候选
```

## 旧专题资产处理

- `TY8.1 武侠/00 武侠文学`：继续作为既有类型/专题资产，不迁移删除；未来 CN3 侠/江湖模型只复用其中与角色、伦理、江湖秩序、文化重构有关的内容。
- `TY8.2 欧洲骑士/00 欧洲骑士文学`：继续作为既有专题资产；未来 CN3 骑士模型只吸收历史化文化模型部分，并通过 CN1.2.3 亚瑟王等具体传统补叙事谱系。
- 其余旧节点标注“沿用原专题资产”的内容：不假定资产路径存在；正式 Topic Build 时逐项搜索和校验。

## 冻结结论

`MIGRATION REVIEW = PASS`

旧 TY8.3.x 后续不再作为新内容建设主入口；CN3.1 成为文化模型主入口，TY 继续承担文学类型职责，CN1 承担具体人物/故事传统职责。
