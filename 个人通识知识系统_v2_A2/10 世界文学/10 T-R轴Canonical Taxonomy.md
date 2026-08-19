---
id: WL-TR-CANONICAL-V2
type: taxonomy_spec
axes: [T, R]
version: "2.4-taxonomy-v2"
status: active
---

# T / R 轴 Canonical Taxonomy v2

## T：时间轴

### Canonical 坐标

当前全局 T 轴只冻结：

```text
T0 史前—约500
T1 约500—1500
T2 约1500—1800
T3 约1800—1890
T4 约1890—1945
T5 约1945—1980
T6 约1980—至今
```

这些节点 `node_kind: period`，可以直接作为作品 `axis_t` 坐标。

### 旧 T*.x 的新语义

旧版 `T0.1、T3.5、T5.2...` 描述的是一个时期中的制度、文类、思潮或历史过程，而不是更细时间范围。因此 v2 统一将其解释为：

```text
historical_feature / stage_feature
```

它们作为 legacy alias 留在阶段说明中，但不再是新的 canonical `axis_t` 值。

真正需要细分时间时必须显式给时间范围；例如 T5 专题内部的 1945—1955 等可以用于专题比较，但不自动升格为全局 T 子节点。

### T5 Topic

`WL-TOPIC-T5-POSTWAR` 与 T5 范围基本一致，因此：

```yaml
primary_anchor: WL-T5
anchor_mode: exact
```

## R：地区 / 文学传统轴

R 轴不是纯国家树，而允许不同种类的文学传统节点：

```text
regional_cluster
civilizational_cluster
national_or_language_tradition
transregional_network_group
diaspora_network
```

因此 R1、R2、R6、R10 不必假装是完全同一种对象，但必须声明 node_kind，并避免同一网络拥有多个 canonical ID。

### 非洲离散文学去重

旧版同时存在：

```text
R7.7 非洲离散文学
R10.2 非洲离散文学
```

v2 统一为：

```text
R10.2 非洲离散文学   ← canonical diaspora_network
R7 非洲文学          → relationship → R10.2
```

不再保留 `R7.7` 作为第二个正式 R 坐标。

### R6 Topic

拉丁美洲文学专题实际覆盖拉丁美洲、加勒比、多语言和跨国问题，与 R6 的范围基本一致，因此保持：

```yaml
primary_anchor: WL-R6
anchor_mode: exact
```

## 数据迁移规则

- 不批量修改 `30 作品/`。
- 新的 `axis_t` 只使用 T0–T6 canonical period，除非未来另行冻结真实时间子区间。
- R 的跨区域关系使用 canonical node + relationship，不复制第二个同义坐标。
- 已有 legacy 值在重读或主动校准时渐进修正。
