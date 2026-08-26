# R Axis Work Base Normalization V1

- Bases normalized: **10**
- Reference grammar: T6 work Base
- Display columns: **作品 / 作者 / 阅读状态 / 专题 / 优先级 / 内部传统（R10 为跨区域传统） / 机制与意义 / 时间 / 地域 / 思潮 / 类型 / 主题 / 编号 / 校验状态**
- Views: **全部作品 / 核心 ★ / 重点 ◆ / 扩展 △ / 未读 / 已读 / 按内部传统 / 按时间 / 按思潮 / 按类型 / 按主题 / 待校验**
- R10 remains filtered by topic membership, not synthetic `axis_r: R10`.
- Display-layer fallbacks prevent blank cells without mutating canonical Work metadata.
- View orders are explicit; no YAML anchors/aliases are used.

`R_AXIS_WORK_BASE_NORMALIZATION_V1 = PASS`
