# T0–T6 时间归类审计说明

## 当前状态

T0–T6 第一轮全量人工治理已经闭合：

- `T_AXIS_MOVE_V1 = APPLIED_AND_VERIFIED`
- `T_AXIS_BOUNDARY_V1 = RESOLVED_AND_VERIFIED`
- `T_AXIS_REVIEW_V1 = RESOLVED_AND_VERIFIED`
- `T_AXIS_FIRST_GOVERNANCE_PASS = CLOSED`

当前命中 T0–T6 的唯一作品实体：**2145**，当前 T 轴成员关系同为 **2145**。

| T | 当前实体数 |
|---|---:|
| T0 | 70 |
| T1 | 77 |
| T2 | 73 |
| T3 | 201 |
| T4 | 384 |
| T5 | 603 |
| T6 | 737 |

## 机器审计状态不是人工治理状态

本目录中的机器扫描依赖结构化 `year` 等字段。当前仍有大量作品缺少机器可读年份，因此机器输出可能显示大量 `REVIEW`。

这些机器 `REVIEW` 只表示“自动规则无法仅凭现有字段裁决”，**不能解释为 T 轴还有同数量的人工待处理作品**。

第一轮人工治理的权威状态请按以下顺序读取：

1. `MANUAL_T0_T6_SUMMARY.md`：当前总状态
2. `CORRECTION_V1.md`：149 条 MOVE 处理记录
3. `BOUNDARY_POLICY_V1.md`：统一断点政策
4. `BOUNDARY_RESOLUTION_V1.md`：26 条 BOUNDARY 决议
5. `REVIEW_RESOLUTION_V1.md`：18 条历史 REVIEW 关系（17 个唯一实体）决议

`MANUAL_T0_T2.md`、`manual_T0_T2_all.csv`、`MANUAL_T3_T6.md` 等保留为**第一轮人工筛查的历史证据**，其中的 MOVE / BOUNDARY / REVIEW 标签不应再被理解为当前未处理队列。

## 统一断代政策

- T0：`< 500`
- T1：`[500, 1500)`
- T2：`[1500, 1800)`
- T3：`[1800, 1890)`
- T4：`[1890, 1945)`
- T5：`[1945, 1980)`
- T6：`[1980, +∞)`

一般作品优先依据主要成书、定稿或完整文本形成时间；必要时采用首次完整发表/出版时间。故事背景、神话时代和历史题材不作为 T 轴依据。

口传传统、后世编纂本、跨断点连载、遗稿、聚合选本按当前仓库中具体作品实体的可证实文本形成/记录口径处理。

## 下一阶段

T-axis 不需要继续重复第一轮全量审计。后续更有价值的工作是：

- 中央作品实体去重与异译名合并
- 同名作品消歧
- `year` / `title_original` / aliases 等书目字段补全
- 聚合选本的 entity 建模
- R/M/G/Q 元数据审计
