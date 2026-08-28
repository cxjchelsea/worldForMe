# QT8.2.1｜Candidate Documents Status

> 当前权威状态源：[[QT8.2.1 创世、宇宙与世界秩序]]
>
> 用途：明确第一轮 Inventory 与第二轮 Triage 的文档角色，防止历史决策快照被误读为当前 component 状态。

## 文档角色

### [[QT8.2.1 Component Inventory V1]]

```text
DOCUMENT_ROLE = HISTORICAL_FIRST_PASS_INVENTORY_SNAPSHOT
CURRENT_STATUS_AUTHORITY = QT8.2.1 问题域主页
```

该文件保留第一轮候选生成、初始优先级与当时的 source-readiness 判断。其 `PROMOTE / HOLD / CANDIDATE` 等状态只表示当时决策，不再作为当前 active-component 状态源。

### [[QT8.2.1 Second-Pass Candidate Triage V1]]

```text
DOCUMENT_ROLE = HISTORICAL_SECOND_PASS_TRIAGE_SNAPSHOT
CURRENT_STATUS_AUTHORITY = QT8.2.1 问题域主页
```

该文件保留第二轮按 evidence maturity × type-boundary clarity × incremental value × source readiness × relation potential 的排序过程。

其中：

```text
M3 NEXT_BUILD_TARGET
S3 SECONDARY_NEXT_TARGET
```

均为历史阶段决策；M3 与 S3 当前已完成 admission + topic build + acceptance，并成为 `ACTIVE_V1_COMPONENT`。

## 当前已完成状态

```text
M2 天地分离 = ACTIVE_V1_COMPONENT
P1 世界父母分离结构 = ACTIVE_V1_COMPONENT
S1 宇宙卵 = ACTIVE_V1_COMPONENT
M3 原初存在的身体化为世界 = ACTIVE_V1_COMPONENT
S3 世界树／宇宙树 = ACTIVE_V1_COMPONENT
```

## 治理规则

```text
historical snapshot ≠ current status registry
```

后续不重写历史快照中的原始判断；当前状态变化统一记录在问题域主页、正式 Admission / Acceptance Review 与后续 Coverage Review 中。