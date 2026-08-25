# T0–T6 全量作品时间归类治理汇总

## 1. 当前结论

第一轮 T0–T6 全量人工语义治理已经闭合。

- 唯一作品实体：**2145**
- 当前 T 轴成员关系：**2145**
- 已不存在《82年生的金智英》《夜晚的潜水艇》的 T5/T6 双挂
- 第一轮人工审计中的 **149 MOVE、26 BOUNDARY、18 REVIEW 均已形成正式决议并写回/记录**
- R/M/G/Q 不在本轮治理范围

当前各 T 节点机器快照：

| T | 当前实体数 |
|---|---:|
| T0 | 70 |
| T1 | 77 |
| T2 | 73 |
| T3 | 201 |
| T4 | 384 |
| T5 | 603 |
| T6 | 737 |
| **合计** | **2145** |

## 2. 统一时间政策

T 轴采用左闭右开的操作性断代：

- T0：`< 500`
- T1：`[500, 1500)`
- T2：`[1500, 1800)`
- T3：`[1800, 1890)`
- T4：`[1890, 1945)`
- T5：`[1945, 1980)`
- T6：`[1980, +∞)`

一般作品优先依据主要成书、定稿或完整文本形成时间；必要时采用首次完整发表/出版时间。故事背景、神话时代和历史题材不作为 T 轴依据。

口传传统、后世编纂本、跨断点连载、遗稿和聚合选本不因题材“古老”而自动归 T0，而以当前仓库中具体作品实体可证实的文本形成/记录口径处理。

详见 `BOUNDARY_POLICY_V1.md` 与 `REVIEW_RESOLUTION_V1.md`。

## 3. 第一轮人工审计基线

修正前人工语义筛查共得到：

| 状态 | 成员关系 |
|---|---:|
| PASS | 1954 |
| MOVE | 149 |
| BOUNDARY | 26 |
| REVIEW | 18 |
| **总计** | **2147** |

其中 2147 比 2145 个实体多出的 2 条来自当时的两个 T5/T6 双挂。

这些数字现在只作为**历史审计基线**，不再代表当前未处理问题数量。

## 4. 已完成的治理阶段

### A. MOVE Correction V1

- 149 条 MOVE 全部处理
- 149 个作品实体实际修改 `axis_t`
- 两个 T5/T6 双挂清理完成
- 记录：`CORRECTION_V1.md`

### B. Boundary Resolution V1

- 26 条 BOUNDARY 全部形成决议
- 15 个 `axis_t` 修改
- 11 个原归属符合统一断点政策，保留
- 记录：`BOUNDARY_POLICY_V1.md`、`BOUNDARY_RESOLUTION_V1.md`

### C. REVIEW Resolution V1

- 历史 REVIEW 成员关系：18
- 唯一作品实体：17（《契诃夫短篇小说选》曾在 T3/T4 历史审计中各出现一次）
- 12 个 `axis_t` 修改
- 5 个保留现有 `axis_t`
- 17 个实体均补入消歧/成书史审核说明；可可靠确定者同时补入 `title_original` / `year`
- 记录：`REVIEW_RESOLUTION_V1.md`

## 5. 机器审计数字如何理解

`README.md`、`T0.csv` … `T6.csv`、`all_t_axis_works.csv` 等机器快照仍可能把大量缺少结构化 `year` 的作品标为 `REVIEW`。

这类机器 `REVIEW` 的含义是“机器缺少足够字段自动判定”，**不等于第一轮人工治理仍有 2083 个待处理作品**。人工治理结论以本汇总以及 `CORRECTION_V1.md`、`BOUNDARY_RESOLUTION_V1.md`、`REVIEW_RESOLUTION_V1.md` 为准。

## 6. 第一轮治理中发现的长期数据问题

以下问题不属于 T-axis 第一轮归类未完成，而是下一阶段中央作品实体治理对象：

- 异译名/重复实体
- 聚合选本的 work/entity 建模
- 同名作品消歧
- `year`、`title_original` 等结构化书目字段补全
- R/M/G/Q 元数据审计

典型重复/异译实体包括：

- 《卡特丽奥娜》 / 《卡特里奥娜》
- `The Well at the World's End` / 《世界尽头的井》
- `The Wood Beyond the World` / 《世界彼端的森林》
- `Biografía de Tadeo Isidoro Cruz` / 《Tadeo Isidoro Cruz小传》
- `El Sur` / 《南方》
- `El fin` / 《结局》

## 7. 当前状态

`T_AXIS_FULL_POPULATION_SCREENING = COMPLETE`

`T_AXIS_MOVE_V1 = APPLIED_AND_VERIFIED`

`T_AXIS_BOUNDARY_V1 = RESOLVED_AND_VERIFIED`

`T_AXIS_REVIEW_V1 = RESOLVED_AND_VERIFIED`

`T_AXIS_FIRST_GOVERNANCE_PASS = CLOSED`

下一阶段不应继续重复审 T0–T6，而应转入中央作品实体去重/别名合并与书目字段治理。
