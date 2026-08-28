---
id: WL-QC2-FINAL-ACCEPTANCE
type: literature_topic_governance
status: PASS_WITH_TRACKED_COMPATIBILITY_DEBT
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
- cluster 仅作为一级问题域与导航容器，不冒充 component。

## 3. 正式 component 实体

正式 component 必须至少满足：

1. `type: qc2_component`；
2. `component_type` 明确；
3. `id / topic_id` 稳定；
4. 通过对应本体准入；
5. 有真实来源/文本证据；
6. 产品壳与 Base/Canvas 可用。

当前正式 component 总数：**11**。

类型分布：

```text
motif = 4
archetype = 2
plot_pattern = 2
symbol = 3
```

正式组件：

- `symbol`｜世界树宇宙树｜QC2.1｜`WL-TOPIC-QC21-WORLD-TREE`
- `plot_pattern`｜世界父母分离结构｜QC2.1｜`WL-TOPIC-QC21-WORLD-PARENTS-SEPARATION`
- `motif`｜原初存在的身体化为世界｜QC2.1｜`WL-TOPIC-QC21-BODY-TO-WORLD`
- `motif`｜天地分离｜QC2.1｜`WL-TOPIC-QC21-SKY-EARTH-SEPARATION`
- `symbol`｜宇宙卵｜QC2.1｜`WL-TOPIC-QC21-COSMIC-EGG`
- `motif`｜Earth-diver / 潜水取土创世｜QC2.1｜`WL-TOPIC-QC21-EARTH-DIVER`
- `motif`｜洪水与灾后重建｜QC2.2｜`WL-TOPIC-QC22-FLOOD`
- `symbol`｜巴别塔｜QC2.3｜`WL-TOPIC-QC23-BABEL`
- `plot_pattern`｜预言→逃避→实现｜QC2.5｜`WL-TOPIC-QC25-PROPHECY-AVOIDANCE-FULFILLMENT`
- `archetype`｜所罗门王｜QC2.8｜`WL-TOPIC-QC28-SOLOMON`
- `archetype`｜受苦义人｜QC2.15｜`WL-TOPIC-QC215-SUFFERING-RIGHTEOUS`

### Earth-diver 的最终准入

早期迁移扫描曾得到 10 个正式 component，原因是 Earth-diver 当时虽已有 motif 定义、两条正式 `qc2_source_reference` 与完整内容研究，但主页尚缺稳定 `id/topic_id`，且 00/01/02/03 产品壳未封口。

本轮完成：

```text
id = WL-TOPIC-QC21-EARTH-DIVER
topic_id = WL-TOPIC-QC21-EARTH-DIVER
component_type = motif
source_reference_count = 2
product_shell = COMPLETE
```

因此当前权威计数正式更新为 **11**；10 是迁移过程中合法的中间状态，不再作为最终计数。

## 4. 产品接口验收

### Structure Base

PASS。

- 使用 `topic_id` 过滤；
- 以 `structure_type_zh` 做语义分组；
- 固定模块：核心结构 / 来源与证据 / 跨传统关系 / 后世重写与阅读；
- 不使用 sequence 区间冒充模块。

### Evidence Base

PASS。

固定区分：

```text
qc2_source_reference
qc2_work_reference
qc2_component_relation
```

Evidence Base 使用 `component_id` 过滤；来源见证、手稿、译本与研究证据不冒充中央 `40 作品`。

### Canvas

PASS。

稳定拓扑：

```text
主页
├─ 核心结构
├─ 来源与证据
├─ 跨传统关系
└─ 后世重写与阅读
```

Canvas 只承担导航与认知入口，不创建未获证据支持的传播边。

### QC1 ↔ QC2 边界

PASS。

```text
QC1 = 资源从哪套文化传统来
QC2 = 跨传统反复出现什么叙事组件
```

活动产品链接已使用 QC namespace；不再把 QC2 当作 QC1 的子内容列表。

## 5. 共享数据与治理链接复核

PASS。

迁移阶段报告曾记录 3 处“旧根目录 QC2 治理链接”风险。本轮逐项复核后确认：

- 洪水数据层当前链接已指向 `00 模板/QC2 组件型专题体系/`；
- 巴别塔数据层使用同名 Obsidian wiki-link，不是 QT8.2 活动路径；
- 未发现需要因此阻断产品验收的活动 QT8.2 根路径。

迁移阶段的该项风险记录因此关闭，不再列为产品缺陷。

## 6. 兼容性债务

以下内容允许保留，并明确不阻断验收：

1. `legacy_code / legacy_topic_id` 中的 QT8.2 历史标识；
2. `source_version` 中的 qt8 / qt82 历史版本号；
3. `90 历史 V0` 中的旧治理命名；
4. 部分早期组件仍保留迁移前的平铺研究页，同时正式产品入口已切换到 `10/11/12/13` 语义目录；
5. 尚待未来建立 QC1.1 来源专题或中央作品映射的 evidence 状态。

不得为了“字符串纯净”盲目全局替换 provenance。

Earth-diver 的平铺 `01–10` 页面当前属于第 4 类兼容性债务：保留研究来源，正式产品入口已由 00/01/02/03 + 10/11/12/13 + 20 接管。

## 7. 模板冻结

`[[QC2 组件型专题地图模板 V1]]` 继续保持冻结。

```text
QC2_COMPONENT_TOPIC_TEMPLATE_V1 = FROZEN
REFERENCE_PILOTS = 5 (covering 4 component types)
ADDITIONAL_FORMAL_COMPONENT_VALIDATION = EARTH_DIVER
QC2_1_TO_QC2_20_SHELL_REUSE = AUTHORIZED_AFTER_PER_COMPONENT_CONTENT_REVIEW
CONTENT_BLIND_COPY = NOT_AUTHORIZED
EVIDENCE_BLIND_COPY = NOT_AUTHORIZED
TITLE_ONLY_CANONICAL_MATCH = NOT_AUTHORIZED
```

Earth-diver 的正式准入验证了模板可以吸收“先研究、后产品化”的既有候选，而无需重开 component ontology。

## 8. 最终状态

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
QC2_COMPONENT_COUNT = 11
QC2_COMPONENT_TYPE_DISTRIBUTION = motif:4 / archetype:2 / plot_pattern:2 / symbol:3
QC2_COMPONENT_TOPIC_TEMPLATE_V1 = FROZEN
QC2_FINAL_ACCEPTANCE = PASS_WITH_TRACKED_COMPATIBILITY_DEBT
QC2_SYSTEMATIC_CONTENT_EXPANSION = OPEN
QT8.3 = UNCHANGED
```

## 9. 下一阶段授权

QC2 的迁移与产品层重构至此收束。后续不再以“迁移补丁”为主，而进入 **systematic content expansion**：逐个 QC2 cluster 研究并准入真正有价值的 component。

优先原则：

```text
coverage gap / conceptual value / cross-tradition evidence
> 为每个 cluster 凑数量
> 为四种 component_type 凑矩阵
```

每个新 component 必须单独通过内容准入，不允许从模板盲复制内容或证据。
