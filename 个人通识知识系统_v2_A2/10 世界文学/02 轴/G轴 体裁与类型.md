---
id: WL-G
type: literature_axis
name: "体裁 / 类型 / 叙事传统"
axis: G
parent: WL
role: primary
priority_scheme: "S/A/B"
source_version: "2.4-taxonomy-v2"
node_model: "hierarchy_plus_facets"
---

# G轴：体裁 / 类型 / 叙事传统

> 核心问题：**它是什么文学形式或类型？**

- 角色：主坐标
- 分级：S/A/B

## 一级节点

- [[../03 节点/G 类型/G1 口述与民间文学|G1 口述与民间文学]] — S
- [[../03 节点/G 类型/G2 诗歌|G2 诗歌]] — S
- [[../03 节点/G 类型/G3 戏剧|G3 戏剧]] — S
- [[../03 节点/G 类型/G4 小说 ／ Fiction|G4 小说 / Fiction]]
- [[../03 节点/G 类型/G5 散文|G5 散文]] — A
- [[../03 节点/G 类型/G6 生命书写|G6 生命书写]] — A
- [[../03 节点/G 类型/G7 纪实文学|G7 纪实文学]] — A
- [[../03 节点/G 类型/G8 混合文类|G8 混合文类]] — A

## G轴 v2 规则

1. `G1 / G2 / ...` 是上位 taxonomy node，不能被其中一个代表性专题直接替代。
2. 专题应挂在能够完整代表其范围的最具体 leaf，例如：
   - 世界神话文学 → `G1.1 神话`
   - 旅行文学 → `G7.4 旅行文学 / Travel Writing`
3. `G4 小说` 采用 **facet 模型**。`G4.1–G4.7` 是不同分类维度的 facet group，不是互斥的七种小说。
4. 一本小说可以同时拥有多个 G leaf；`axis_g` 因此保持列表。
5. `facet_group` 只用于导航和分组，不作为已有专题的最终 canonical anchor；正式专题优先挂到其下的 `taxonomy_leaf`。

## 返回

- [[../世界文学地图|世界文学地图]]
