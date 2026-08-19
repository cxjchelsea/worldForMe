---
id: WL-G-CANONICAL-V2
type: taxonomy_spec
axis: G
version: "2.4-taxonomy-v2"
status: active
---

# G轴 Canonical Taxonomy v2

> 本文件是 G 轴在六轴 taxonomy 修复阶段的 canonical 对照。`06 六轴代码对照.md` 中旧 G4.x 粗粒度映射保留作历史兼容；发生冲突时以本页与实际节点文件为准。

## 1. 一级骨架

```text
G1 口述与民间文学
G2 诗歌
G3 戏剧
G4 小说 / Fiction
G5 散文
G6 生命书写
G7 纪实文学
G8 混合文类
```

一级骨架不因已有专题而改变。

## 2. G1 口述与民间文学

```text
G1
├─ G1.1 神话              ← 世界神话文学 Topic
├─ G1.2 传说
├─ G1.3 民间故事
├─ G1.4 童话
├─ G1.5 寓言
├─ G1.6 口传史诗
├─ G1.7 歌谣
└─ G1.8 都市传说
```

世界神话文学的 Topic ID 继续是 `WL-TOPIC-G1-MYTH`，但 `primary_anchor` 已改为 `WL-G1.1`。

## 3. G4 小说：Facet 模型

`G4.1–G4.7` 是 facet group：

| code | facet_dimension | 作用 |
|---|---|---|
| G4.1 | length_form | 篇幅与基础形式 |
| G4.2 | historical_form | 历史形成的小说形式 |
| G4.3 | social_character | 人物形成、家庭、社会角色等 |
| G4.4 | historical_reality | 历史、现实对象与社会经验 |
| G4.5 | genre_tradition | 现代类型传统 |
| G4.6 | speculative_idea | 思辨、制度与思想实验 |
| G4.7 | audience_market | 读者、媒介与市场分层 |

这些 facet 不是互斥关系。一本作品可以同时落入多个 facet。

### 当前正式专题 leaf

```text
G4.3
├─ G4.3.1 成长小说          ← 成长文学
└─ G4.3.4 家族小说          ← 家族文学

G4.4
└─ G4.4.1 历史小说          ← 历史文学

G4.5
├─ G4.5.1 推理 / 犯罪       ← 推理文学
├─ G4.5.2 科幻              ← 科幻文学
├─ G4.5.3 奇幻              ← 奇幻文学
├─ G4.5.4 恐怖 / 怪奇       ← 恐怖文学
└─ G4.5.5 冒险              ← 冒险文学

G4.6
└─ G4.6.2 反乌托邦          ← 反乌托邦文学
```

爱情、西部、武侠等仍可以是 G 类型值，但其现有专题主入口分别由 Q2 / Q15 承担；G 轴不重复建 Topic 首页。

## 4. G7 纪实文学

```text
G7
├─ G7.1 报告文学
├─ G7.2 文学新闻
├─ G7.3 口述史
├─ G7.4 旅行文学 / Travel Writing  ← 旅行文学 Topic
├─ G7.5 自然写作
└─ G7.6 见证文学
```

旅行文学 Topic ID `WL-TOPIC-G7-TRAVEL` 保持不变，`primary_anchor` 改为 `WL-G7.4`。

## 5. Topic Anchor 映射

| Topic | stable Topic ID | canonical anchor |
|---|---|---|
| 世界神话文学 | WL-TOPIC-G1-MYTH | WL-G1.1 |
| 成长文学 | WL-TOPIC-G43-BILDUNGSROMAN | WL-G4.3.1 |
| 家族文学 | WL-TOPIC-G43-FAMILY | WL-G4.3.4 |
| 历史文学 | WL-TOPIC-G44-HISTORICAL | WL-G4.4.1 |
| 推理文学 | WL-TOPIC-G45-MYSTERY | WL-G4.5.1 |
| 科幻文学 | WL-TOPIC-G45-SF | WL-G4.5.2 |
| 奇幻文学 | WL-TOPIC-G45-FANTASY | WL-G4.5.3 |
| 恐怖文学 | WL-TOPIC-G45-HORROR | WL-G4.5.4 |
| 冒险文学 | WL-TOPIC-G45-ADVENTURE | WL-G4.5.5 |
| 反乌托邦文学 | WL-TOPIC-G46-DYSTOPIA | WL-G4.6.2 |
| 旅行文学 | WL-TOPIC-G7-TRAVEL | WL-G7.4 |

## 6. 迁移状态

本轮已完成：

- taxonomy group / facet group / taxonomy leaf 语义分离；
- G1 与 G7 父类坍缩修复；
- G4 facet 模型落盘；
- 当前 11 个 G Topic 重挂到 leaf；
- Topic stable ID 不变；
- 作品 schema 不变；
- 作品数据不批量迁移。

本轮有意不做：

- 不移动 `20 专题地图/` 现有物理目录；
- 不批量改 `30 作品/axis_g`；
- 不实体化所有尚未成为正式专题的 G4 facet value。

这样可以在语义先正确的前提下，后续再做 link-safe path migration 和 read-calibrated works 的渐进细化。
