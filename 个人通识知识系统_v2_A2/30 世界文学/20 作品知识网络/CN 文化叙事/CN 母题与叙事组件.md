---
id: WL-CN
legacy_id: WL-CN
type: literature_network_subsystem
name: CN 文化叙事网络
code: CN
namespace: CN
legacy_code: QC
system_role: work_knowledge_network
network_kind: cultural_narrative
work_field: cultural_narrative_relations
legacy_axis: "Q"
legacy_parent: WL-Q
level: 1
status: ACTIVE
source_version: "3.0-coordinate-network"
---
# CN 文化叙事网络

> 新路径：世界文学 → 作品知识网络 → **CN 文化叙事网络**。物理目录 `20 作品知识网络/CN 文化叙事/` 仅为兼容旧 WikiLink 保留。

CN 不是普通作品坐标，也不追求每部作品都有标签。它研究作品与长期文化叙事网络之间有证据的关系：故事从哪里来、叙事组件如何迁移和变形、这些资源如何进入具体历史社会并形成稳定文化模型。

## 三层机制

- [[CN1 世界文化叙事传统|CN1 世界叙事资源与来源传统]]：**纵向谱系**。
  - [[CN1.1 神话、传说与民间叙事|CN1.1 来源环境 / 文化土壤]]：文化、宗教、区域性的来源环境 hubs。
  - [[CN1.2 故事循环、人物传说与跨文本叙事传统|CN1.2 具体叙事传统的历史生命]]：保留专名、人物、文化身份和文本谱系的具体传统包。
- [[CN2 世界文化母题、原型与叙事结构|CN2 可复用叙事组件]]：从具体传统中抽象出的结构零件，可跨文本、跨传统复用。
- [[CN3 历史化文化叙事传统|CN3 历史化文化模型]]：资源与组件进入具体社会后，与制度、阶层、伦理、空间经验和媒介传统结合形成的角色、关系、伦理与秩序模型。

```text
CN1 追踪：从哪里来、怎样演变
CN2 拆解：用了哪些可复用结构
CN3 解释：这些结构怎样被历史社会组织成稳定文化模型
```

## 作品侧关系

作品页逐步使用 `cultural_narrative_relations:`，而不是把 CN 当作普通标签塞进 `axis_q`：

```yaml
cultural_narrative_relations:
  - target: "CN1.2.3 亚瑟王叙事传统"
    relation: retells
    evidence:
      - "..."
```

推荐关系：`retells`、`adapts`、`continues`、`reframes`、`structural_similarity`、`uses`、`foregrounds`、`transforms`、`critiques`、`subverts`、`reorders`。

没有可靠证据就留空。结构相似不自动等于历史来源。

## 证据纪律

```text
text date ≠ origin
precedence ≠ direct source
plot similarity ≠ transmission
later coherent narrative ≠ early original
modern reconstruction ≠ extant original
```

## 节点职责

正式 CN 节点不是只做分类，而应逐步承担微型专题课程 / 学习路径：定义、边界、关键子问题、相关 CN 节点、核心作品、扩展作品、对照作品、阅读路线、证据纪律。

中央 `40 作品` 始终是作品唯一事实源。CN 节点只建立关系和投影，不复制作品实体。

> 全局治理：[[CN 总体架构与建设规范 V2]]  
> CN1 专属治理：[[CN1 建设规范 V1]]  
> 顶层系统：[[../../04 系统架构/02 作品知识网络|作品知识网络]]

核心原则：**树负责找路，网络负责表达知识；结构相似不等于历史传播；专题按真实阅读与研究需求深建，不按编号机械铺满。**
