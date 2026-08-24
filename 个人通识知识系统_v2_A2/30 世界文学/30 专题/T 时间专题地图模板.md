---
type: literature_topic_map_template
axis: T
template_version: t-axis-topic-v1
status: seed
---

# T 轴专题地图模板

本模板用于 `30 专题/T# 时代名称/` 的最小专题包。专题主页是语义中心；Canvas 用于表达结构关系，不复述正文。

## Metadata

沿用既有 `literature_topic_map`，并以 registry 已登记的 stable Topic ID 为准：

```yaml
id: "WL-TOPIC-T#-..."
type: "literature_topic_map"
name: ""
primary_anchor: "WL-T#"
anchor_mode: "exact"
taxonomy_version: "literature-taxonomy-v2"
topic_role: "direct"
structure_status: "seed"
template_version: "t-axis-topic-v1"
```

不为尚未建立的作品数据库、结构数据库或来源档案预设字段。

## Markdown 结构

00–10 是固定一级入口；二级标题是按时代调整的工作提示，而非必须逐项填满的表单。没有可靠内容时保留简短待研究提示，不推断作品、作者或节点关系。

```markdown
# T#｜时代名称

## 00｜地图问题

> 这个时代的世界文学发生了什么根本变化？

## 01｜时代边界

## 02｜历史世界

## 03｜文学世界结构

## 04｜核心文学转变

## 05｜地域展开

## 06｜思潮与形式

## 07｜核心作品群

## 08｜时代遗产

## 09｜关联地图

## 10｜我的阅读与问题
```

`05` 固定保留 R1–R9 与 R10.2 的入口，但只记录该时代的地域变化，不复制 R 地图。`06` 只在研究确证后链接相关 M/G/QT/QH 节点。`07` 只链接既存于 `40 作品/` 的实体，绝不创建副本或占位作品。

## Canvas 生成规范

Canvas 必须包含如下主干，并使用文本节点保持轻量：

```text
T# → 历史世界 → 文学世界结构 → 核心文学转变
                                      ↙      ↓      ↘
                                   地域    思潮    文类
                                      ↘      ↓      ↙
                                         核心作品群
                                             ↓
                                         时代遗产
                                             ↓
                                         下一时代
```

侧边放置“地图问题”“关联地图”“我的阅读与问题”。只有确证的、已存在的 Markdown 才能作为 Canvas `file` 节点；本阶段不以虚构作品或未确证的跨轴关系填图。
