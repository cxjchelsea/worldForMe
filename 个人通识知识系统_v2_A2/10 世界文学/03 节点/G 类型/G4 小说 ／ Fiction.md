---
id: WL-G4
type: literature_node
name: "小说 / Fiction"
code: G4
axis: G
parent: WL-G
level: 1
node_kind: taxonomy_group
node_model: faceted
anchorable: false
topic_map: null
source_version: "2.4-taxonomy-v2"
---

# G4 小说 / Fiction

> 路径：[[../../世界文学地图|世界文学]] → [[../../02 轴/G轴 体裁与类型|G轴]] → **G4 小说 / Fiction**

G4 不再被建模成一棵互斥的单继承类型树。小说可以同时从多个维度被描述，因此 `G4.1–G4.7` 是 **facet group**。

## 七个 Facet Group

- [[G4.1 按篇幅与基础形式|G4.1 按篇幅与基础形式]] — `length_form`
- [[G4.2 历史形成的小说形式|G4.2 历史形成的小说形式]] — `historical_form`
- [[G4.3 社会与人物型小说|G4.3 社会与人物型小说]] — `social_character`
- [[G4.4 历史与现实类型|G4.4 历史与现实类型]] — `historical_reality`
- [[G4.5 现代类型文学|G4.5 现代类型文学]] — `genre_tradition`
- [[G4.6 思辨与思想类型|G4.6 思辨与思想类型]] — `speculative_idea`
- [[G4.7 读者与市场类型|G4.7 读者与市场类型]] — `audience_market`

## 使用规则

一本作品可以同时属于多个 facet。例如《1984》可以同时具有现代类型、思辨类型等坐标；后续校准时应进一步写到具体 leaf，而不是只停在 facet group。

专题地图必须优先挂在具体 `taxonomy_leaf`；facet group 只负责导航与聚类。
