---
id: WL-Q
type: literature_legacy_entry
name: Q 兼容入口
axis: Q
parent: WL
role: legacy_namespace
status: DEPRECATED_AS_AXIS
compatibility: true
source_version: "3.0-coordinate-network"
---

# Q：旧内容域兼容入口

> `Q` 自 2026-09-07 起不再作为一个 canonical 作品坐标轴。本文件保留原路径与 `WL-Q` 标识，只用于旧 WikiLink、旧 `axis_q`、旧 Canvas 与历史说明的兼容。

新的权威架构：[[../04 系统架构/00 作品坐标与知识网络总则|作品坐标与知识网络总则]]。

## 旧模型 → 新模型

```text
旧：Q 文学内容域
├─ QH 主题
├─ QT 类型
├─ QX 意象
└─ QC 文化叙事

新：
A 作品坐标系统
├─ QH 主题
└─ QT 类型

B 作品知识网络
├─ QX 意象网络
└─ QC 文化叙事网络
```

因此四者不再是等价 facet：

- [[../20 节点/Q 主题/QH 主题/QH 主题与人类问题|QH 主题]]：作品坐标，回答“作品在思考什么”；
- [[../20 节点/Q 主题/QT 类型/QT 类型与叙事传统|QT 类型]]：作品坐标，回答“作品采用什么类型 / 叙事机制”；
- [[../20 节点/Q 主题/QX 意象/QX 文学意象与场景|QX 意象网络]]：稀疏作品内抽取，回答“作品有什么显著意象”；
- [[../20 节点/Q 主题/QC 母题/QC 母题与叙事组件|QC 文化叙事网络]]：稀疏关系网络，回答“作品与哪些长期文化叙事结构有关”。

## 字段兼容

旧作品页可能仍有：

```yaml
axis_q:
  - QT...
  - QH...
```

迁移期允许读取，但新写入优先拆分为：

```yaml
axis_qt: []
axis_qh: []
```

QX 继续使用 `qx:`；QC 使用 `qc_relations:`。QX / QC 不得写回 `axis_q`。

## 路径兼容

`10 轴/` 与 `20 节点/Q 主题/` 暂不移动，避免破坏已有 WikiLink、专题、Base 和 Canvas。目录名只是历史地址，不再定义概念归属。

旧 `Q1–Q16` 继续保持 legacy，不恢复。

## 返回

- [[../00 世界文学使用规则|世界文学使用规则]]
- [[../04 系统架构/01 作品坐标系统|作品坐标系统]]
- [[../04 系统架构/02 作品知识网络|作品知识网络]]
