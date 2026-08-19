---
id: WL-MNQ-CANONICAL-V2
type: taxonomy_spec
axes: [M, N, Q]
version: "2.4-taxonomy-v2"
status: active
---

# M / N / Q 轴 Canonical Taxonomy v2（首批修复）

> 本页只冻结本轮已被正式 Topic 使用的坍缩节点，不宣称一次性实体化 M/N/Q 的全部潜在叶节点。

## M3 现代主义与先锋派

```text
M3 现代主义与先锋派      [taxonomy_group]
├─ M3.1 现代主义         [taxonomy_leaf] ← 现代主义文学 Topic
├─ M3.2 意象主义
├─ M3.3 表现主义
├─ M3.4 未来主义
├─ M3.5 阿克梅主义
├─ M3.6 达达主义
├─ M3.7 超现实主义
└─ M3.8 其他先锋派
```

现代主义 Topic stable ID `WL-TOPIC-M3-MODERNISM` 不变；canonical anchor 为 `WL-M3.1`。

## N2 聚焦与可靠性

```text
N2 聚焦与可靠性          [taxonomy_group]
├─ N2.1 聚焦             [taxonomy_group]
│  ├─ 零聚焦
│  ├─ 内聚焦
│  ├─ 外聚焦
│  ├─ 固定聚焦
│  └─ 变换聚焦
└─ N2.2 叙述可靠性        [taxonomy_group]
   ├─ N2.2.1 可靠叙述     [taxonomy_leaf]
   └─ N2.2.2 不可靠叙述   [taxonomy_leaf] ← 不可靠叙述 Topic
```

这里的关键修复不是单纯“多加一级”，而是把 focalization 与 narratorial reliability 分开。

不可靠叙述 Topic stable ID `WL-TOPIC-N2-UNRELIABLE` 不变；canonical anchor 为 `WL-N2.2.2`。

## Q2 爱、欲望与亲密关系

```text
Q2 爱、欲望与亲密关系    [taxonomy_group]
├─ Q2.1 爱情             [taxonomy_leaf] ← 爱情文学 Topic
├─ 欲望
├─ 婚姻
├─ 友谊
├─ 背叛
├─ 失去
└─ 哀悼
```

爱情文学 Topic stable ID `WL-TOPIC-Q2-LOVE` 不变；canonical anchor 为 `WL-Q2.1`。

## Q6 战争、暴力与创伤

```text
Q6 战争、暴力与创伤      [taxonomy_group]
├─ Q6.1 战争             [taxonomy_leaf] ← 战争文学 Topic
├─ 屠杀
├─ 种族灭绝
├─ 革命暴力
├─ 国家暴力
├─ 家庭暴力
├─ 生存
├─ 创伤
└─ 创伤后记忆
```

战争文学 Topic stable ID `WL-TOPIC-Q6-WAR` 不变；canonical anchor 为 `WL-Q6.1`。

## 本轮迁移规则

- 父节点改为 `anchorable: false`，其 `topic_map` 清空。
- 真实 Topic leaf 使用 `anchorable: true`。
- Topic 首页增加 `anchor_mode: leaf`、`taxonomy_version: literature-taxonomy-v2`、`path_status: legacy_compatible`。
- 不移动现有物理专题目录。
- 不修改 `30 作品/` 或作品 schema。
- 未成为正式专题的兄弟概念暂不为追求编号完整而批量创建空文件。
