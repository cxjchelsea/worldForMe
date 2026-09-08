---
id: WL-CN12-COMPARISON-V1
legacy_id: WL-QC12-COMPARISON-V1
type: literature_governance_review
system_role: work_knowledge_network
scope: CN1.2
status: FROZEN_REFERENCE
version: "1.1"
---
# CN1.2 样板横向比较 V1

比较对象：

- [[CN1.2.1 特洛伊故事循环]]
- [[CN1.2.2 沃尔松—尼伯龙根叙事传统]]

两个对象均已完成 `stage_freeze`。本文件保留为 `narrative_cycle` V1 模板的验证依据。

## 1. 两个样板真正不同在哪里

| 维度 | CN1.2.1 特洛伊 | CN1.2.2 沃尔松—尼伯龙根 |
|---|---|---|
| 主要组织方式 | 大型故事循环的连续区段 | 共享材料在不同文本分支中的重组 |
| 主问题 | 一个巨大故事如何被不同文本分段保存、补写、延伸 | 相近人物／事件如何在不同语言文本环境中发生分化 |
| chronology 权重 | 高 | 中 |
| branch 权重 | 中 | 高 |
| 人物对应复杂度 | 中 | 高 |
| 失传材料重要性 | 高 | 较低，但早期层次复杂 |
| 跨语言重写 | 希腊 → 拉丁及后世 | 北欧 ↔ 德语比较 + 后世现代重构 |
| 最重要证据风险 | 把叙事顺序误当作品谱系 | 把共享材料误当直接传播 |
| CN2 输出方式 | 从战争区段、归乡、复仇等情节抽象 | 从人物—事件变体与家族毁灭抽象 |

结论：两个样板虽然同属 `narrative_cycle`，但内部机制差异足够大，可以冻结这一 resource_type 的 V1 产品骨架。

## 2. 共同验证的六个稳定认知职责

```text
A. 定义、边界与核心叙事材料
B. 早期材料与文本见证
C. 文本谱系／版本／分支
D. 人物与叙事结构变体
E. 后世生命与跨语言／文类／媒介重构
F. CN2 组件、证据与阅读接口
```

规则：**冻结语义职责，不冻结二级页面标题。**

## 3. 共同验证的物理产品壳

```text
00 主页.md
01 Canvas.canvas
02 结构／谱系.base
03 作品／文本见证.base
10–15 六个认知职责层
```

对应正式模板：[[CN1.2 narrative_cycle 专题模板 V1]]。

## 4. 被正式冻结的模型原则

### chronology

可作为重要视图和结构维度，但不能成为所有 CN1.2 的唯一骨架。

### branch

必须作为通用能力保留，但不要求所有对象形成清晰树状分支。

### 人物对应

不得强制转换成 canonical identity。应允许 variant / functional correspondence / figure tradition 等关系。

### event_variant

当前仍不是标准独立层。只有更多样板持续产生同类检索需求时再升级。

### work / witness

`tradition ≠ story_witness ≠ work`。

CN1.2.2 进一步验证：一个中央 work 可以下钻到多个细粒度 witness；作品数量不是专题成熟度指标。

## 5. 证据纪律

冻结以下规则：

1. 叙事顺序 ≠ 文本年代；
2. 文本年代先后 ≠ 直接来源；
3. 情节相似 ≠ direct transmission；
4. 人物对应 ≠ 实体完全同一；
5. 后世完整叙事 ≠ 早期传统原貌；
6. 失传材料现代摘要 ≠ 完整现存作品；
7. Canvas 不得通过箭头暗示未经证实的传播；
8. `work`、`story_witness`、`tradition` 必须分层。

## 6. 冻结结论

```text
CN1.2.1 = STAGE_FROZEN
CN1.2.2 = STAGE_FROZEN
CN1.2 narrative_cycle 专题模板 V1 = FROZEN_V1
```

## 7. 适用边界

此次冻结只验证 `narrative_cycle`。

尚未验证：

- `figure_tradition`
- `story_tradition`
- `collection_tradition`

因此不能把当前模板称为 CN1.2 全类型最终模板。

## 8. 下一阶段

第三样板应故意选择不同 resource_type。

当前优先：

```text
亚瑟王叙事传统
resource_type: figure_tradition
```

重点测试：

- 人物中心型传统是否仍适用 10–15 六个职责；
- 人物网络是否需要独立能力；
- 圣杯、梅林、兰斯洛特、高文、特里斯坦等子传统如何分层；
- 多语言、多作者、多文类扩张是否迫使修改 `12–13` 的职责边界。

只有异质 resource_type 完成验证后，才重新判断是否升级为真正的 CN1.2 通用模板。
