# TH 格式迁移说明

## 迁移目标

本轮只统一 TH 与 T / R / M 的公共工程格式，不修改已冻结的主题划分、核心问题结论和稳定 topic ID。

## 已统一

1. **轴入口**：新增 `00 TH 主题入口.md`，使用 `type: literature_axis / role / priority_scheme / node_model`。
2. **兼容入口**：旧 `TH 主题与人类问题.md` 保留为跳转文件，不再重复定义 `WL-TH`。
3. **轴契约**：新增 `TH 轴结构契约.md`，冻结公共字段和目录职责。
4. **作品 Base**：TH1.1—TH8 统一使用 `★ / ◆ / △ / 已读 / 未读 / 全部作品` 的公共视图，并统一展示 `axis_t / axis_r / axis_m / axis_g / axis_th`。
5. **结构 Base**：TH3.1—TH8 使用 `topic_id + 路径兼容` 双读取模式，统一提供“全部知识节点 / 核心结构 / 核心问题”。
6. **兼容专题**：TH2.1、TH2.3、TH2.5、TH6、TH7 的旧历史字段和稳定 ID 均保留。

## 为什么没有机械重写所有内部文件

T / R / M 的成熟做法并不是让所有专题拥有相同的内部目录，而是共享相同 contract。TH1 / TH2 的成熟专题已经拥有较完整 `topic_id / type / dimension` 元数据；TH3 后段至 TH8 仍有一些轻量文件缺少 frontmatter。

本轮结构 Base 因此使用兼容读取：

```text
有 topic_id 的节点
        +
现有 10 结构 / 11 核心问题 / 13 THx核心问题 文件
        ↓
统一进入结构 Base
```

以后编辑这些内部节点时，再逐步补齐：

```yaml
type: literature_topic_structure | literature_topic_section
topic_id: ...
parent: ...
dimension: ...
sequence: ...
```

这样可以避免为了“格式统一”一次性重写几百个已经有内容的文件，同时新旧节点在 Obsidian 中已经使用同一套入口和数据库视图。

## 后续新增 TH 专题规则

新专题不得复制旧轻量模板，必须先遵守 [[TH 轴结构契约]]，再增加专题特有结构。
