---
id: WL-QC2-FINAL-ACCEPTANCE
type: literature_topic_governance
status: FAIL_PRODUCT_INTEGRITY
reviewed_scope: QC2
---
# QC2｜最终迁移与产品层验收

## 1. 迁移结论

- 历史迁移：`QT8.2 → QC2`；`QT8.2.1–QT8.2.20 → QC2.1–QC2.20`。
- schema namespace：`qt82_* → qc2_*`；`legacy_*` 与 `source_version` 可继续保留旧命名作为 provenance。
- QC1 = 来源传统层；QC2 = 横向叙事组件层。
- QT8.3 未迁移、未重构，本轮保持 out of scope。

## 2. Cluster 验收

- 预期 cluster：20
- 完整 cluster shell：20 / 20
- 固定壳：`00 homepage + 01 Canvas + 02 component Base`

## 3. 正式 component 实体

正式 component 必须同时满足：目录内存在 `00 *.md`，且主页 `type: qc2_component`、`component_type`、`id/topic_id` 完整。

- 正式 component 总数：**10**
- 类型分布：`{"archetype": 2, "motif": 3, "plot_pattern": 2, "symbol": 3}`

- `symbol`｜世界树宇宙树｜QC2.1 创世、宇宙与世界秩序｜`WL-TOPIC-QC21-WORLD-TREE`
- `plot_pattern`｜世界父母分离结构｜QC2.1 创世、宇宙与世界秩序｜`WL-TOPIC-QC21-WORLD-PARENTS-SEPARATION`
- `motif`｜原初存在的身体化为世界｜QC2.1 创世、宇宙与世界秩序｜`WL-TOPIC-QC21-BODY-TO-WORLD`
- `motif`｜天地分离｜QC2.1 创世、宇宙与世界秩序｜`WL-TOPIC-QC21-SKY-EARTH-SEPARATION`
- `symbol`｜宇宙卵｜QC2.1 创世、宇宙与世界秩序｜`WL-TOPIC-QC21-COSMIC-EGG`
- `archetype`｜受苦义人｜QC2.15 牺牲、罪、救赎与替罪｜`WL-TOPIC-QC215-SUFFERING-RIGHTEOUS`
- `motif`｜洪水与灾后重建｜QC2.2 毁灭、灾变与世界重生｜`WL-TOPIC-QC22-FLOOD`
- `symbol`｜巴别塔｜QC2.3 神、人边界与禁忌越界｜`WL-TOPIC-QC23-BABEL`
- `plot_pattern`｜预言→逃避→实现｜QC2.5 命运、预言与自由意志｜`WL-TOPIC-QC25-PROPHECY-AVOIDANCE-FULFILLMENT`
- `archetype`｜所罗门王｜QC2.8 王权、合法性与秩序更替｜`WL-TOPIC-QC28-SOLOMON`

### 10 / 11 差异说明

“11 个”来自迁移前对候选目录/试验对象的人工预估，不是正式本体计数。按冻结后的产品契约重新扫描，只有上述 **10 个**满足正式 component 条件；不为匹配旧预估把治理、研究或不完整候选目录强行升级为 component。

未计入的候选目录：

- QC2.1 创世、宇宙与世界秩序 / Earth-diver 潜水取土创世: homepage exists but qc2_component contract incomplete

因此 `QC2_COMPONENT_COUNT = 10` 是当前权威计数；“11”废弃为旧人工估计。

## 4. 产品接口验收

- Structure Base：按 `structure_type_zh` 语义分组，PASS。
- Evidence Base：按 `component_id` 过滤并区分 source/work/component relation，PASS。
- Canvas：主页连接四个语义模块，不制造未经证实的传播边，PASS。
- 中央作品边界：证据记录不冒充 `40 作品`，PASS。
- QC1 → QC2：活动链接已切换到 QC namespace，PASS。
- 共享治理链接：修复文件数 23；扫描到迁移前旧根目录链接 20 处。
- active status vocabulary：修复 `external_source_pending_qt81_topic` 21 处。

产品壳缺失 / 结构问题：

- 无

迁移后仍存在的旧根目录 QC2 治理链接：

- 个人通识知识系统_v2_A2/30 世界文学/30 专题/QC2.2 毁灭、灾变与世界重生/洪水与灾后重建/00 洪水与灾后重建.md
- 个人通识知识系统_v2_A2/30 世界文学/30 专题/QC2.2 毁灭、灾变与世界重生/洪水与灾后重建/20 数据层/00 数据层索引.md
- 个人通识知识系统_v2_A2/30 世界文学/30 专题/QC2.3 神、人边界与禁忌越界/巴别塔/20 数据层/00 数据层索引.md

## 5. 兼容性债务

允许继续存在：`legacy_code / legacy_topic_id` 的 QT8.2 标识、`source_version` 的 qt8/qt82 历史版本号、历史 V0 治理文档中的旧命名，以及仍待建立 QC1.1 来源专题或中央作品映射的 evidence 状态。

需人工关注但不自动全局替换的活动 QT8.2/qt82 标记：

- 无

不得对历史 provenance 做盲目全局字符串替换。

## 6. 模板冻结

`[[QC2 组件型专题地图模板 V1]]` 已升级为完整治理模板并冻结。

```text
QC2_COMPONENT_TOPIC_TEMPLATE_V1 = FROZEN
REFERENCE_PILOTS = 5 (covering 4 component types)
QC2_1_TO_QC2_20_SHELL_REUSE = AUTHORIZED_AFTER_PER_COMPONENT_CONTENT_REVIEW
CONTENT_BLIND_COPY = NOT_AUTHORIZED
EVIDENCE_BLIND_COPY = NOT_AUTHORIZED
TITLE_ONLY_CANONICAL_MATCH = NOT_AUTHORIZED
```

## 7. 最终状态

```text
QC2_TAXONOMY = PASS
QC2_20_CLUSTER_LAYER = PASS
QC2_COMPONENT_ONTOLOGY = PASS
QC2_PRODUCT_SHELL = PASS
QC2_STRUCTURE_BASE = PASS
QC2_EVIDENCE_BASE = PASS
QC2_CANVAS = PASS
QC2_QC1_LINK_ALIGNMENT = PASS
QC2_SHARED_DATA_NAMESPACE = PASS
QC2_COMPONENT_COUNT = 10
QC2_COMPONENT_TOPIC_TEMPLATE_V1 = FROZEN
QC2_SYSTEMATIC_CONTENT_EXPANSION = OPEN
QT8.3 = UNCHANGED
```
