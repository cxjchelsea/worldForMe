---
id: "WL-TAXONOMY-AUDIT-2026-08"
type: "system_audit"
domain: "literature"
scope: "six_axis_taxonomy"
baseline_commit: "fc8b1c283ee7bdeb8eb9e6fb1816655bcce7008f"
audit_date: "2026-08-19"
status: "DRAFT_DIAGNOSTIC_ONLY"
migration_allowed: false
---

# 世界文学六轴 Taxonomy 层级审计

> 本审计回答的是：**T / R / M / G / N / Q 六轴的分类节点本身是否语义稳定，现有专题到底应该挂在哪一层。**
>
> 它不回答专题内部内容是否成熟，也不在本轮迁移任何文件、stable ID、作品坐标或专题数据。

审计基线：`main @ fc8b1c283ee7bdeb8eb9e6fb1816655bcce7008f`。

---

## 1. 核心结论

当前系统的主要问题不是“不同位置的树深度不一致”。

真正的问题是：

> **Taxonomy Node、Topic Anchor 与 Topic Map 在早期建设过程中被部分混用，导致一个已经做出来的代表性专题，直接占据了更宽的父级分类位置。**

这可以称为 **分类坍缩（taxonomy collapse）**。

### 1.1 深度不一致本身允许存在

下列情况都是合法的：

```text
G1
└─ G1.1
   └─ Topic

T5
└─ Topic

Q15
└─ umbrella Topic
   └─ child Topic
```

专题地图不需要统一出现在固定深度。

真正的约束应当是：

> **专题挂载位置必须是能够完整代表该专题范围的最具体 canonical node。**

因此：

- `T5 二战后多极文学` 可以直接建立专题，因为专题范围与 T5 基本一致；
- `Q10 历史、记忆与时间` 可以直接建立专题，因为专题范围与 Q10 基本一致；
- `G1 口述与民间文学` 不能被“世界神话文学”直接替代，因为神话只是 G1 的一个子类；
- `M3 现代主义与先锋派` 不能被“现代主义文学”直接替代，因为现代主义只是 M3.1；
- `N2 聚焦与可靠性` 不能被“不可靠叙述”直接替代，因为不可靠叙述只是该节点中的一个机制；
- `Q2 爱、欲望与亲密关系` 不能被“爱情文学”直接替代；
- `Q6 战争、暴力与创伤` 不能被“战争文学”直接替代。

---

## 2. 审计对象与问题类型

### 2.1 三层对象必须拆开

以后固定区分：

```text
Layer 1  Taxonomy Node
         六轴中的分类节点

Layer 2  Topic Anchor
         某专题在六轴中的 canonical 挂载点

Layer 3  Topic Map
         20 专题地图/ 下的实际知识地图
```

三者有关，但绝不应自动视作同一对象。

### 2.2 问题编码

| 编码 | 名称 | 判断标准 |
|---|---|---|
| C1 | 父类坍缩 | 一个较窄 Topic 直接占据较宽父节点 |
| C2 | 中间层缺失 | 父节点与 Topic 之间存在明确但尚未实体化的子类 |
| C3 | 兄弟粒度错位 | 同层节点不是相近抽象层级 |
| C4 | Topic / Taxonomy 混用 | 比较专题、阅读专题或 umbrella 被当成普通分类节点 |
| C5 | 轴内维度污染 | 子节点不再回答该轴原本的问题 |
| C6 | 复合节点 | 一个节点揉合了两个以上不同分类原则 |
| C7 | 重复 / 重叠节点 | 同一概念在同轴多个位置重复出现，且关系未说明 |

---

## 3. 当前正式专题 Anchor 审计

`06 六轴代码对照.md` 当前列出 19 个正式顶层专题；Q15 的 8 个子专题另算。

### 3.1 统计

- **范围与当前节点基本一致：4 个**
  - T5 二战后多极文学
  - R6 拉丁美洲文学（专题正文实际覆盖加勒比与多语言世界）
  - Q10 历史、记忆与时间
  - Q15 武人、英雄与秩序 umbrella

- **存在明显父类坍缩：15 个**
  - G 轴：11 个
  - M 轴：1 个
  - N 轴：1 个
  - Q 轴：2 个

换句话说：

> **当前顶层正式专题中，大多数 Topic Map 本身没有问题，但 primary anchor / 挂载层级过粗。**

### 3.2 逐专题矩阵

| Topic | 当前挂载节点 | 当前节点实际范围 | 判断 | canonical 目标 |
|---|---|---|---|---|
| 二战后多极文学 | T5 | 约1945—1980整体文学史阶段 | OK | 保持 T5 |
| 拉丁美洲文学 | R6 | 拉丁美洲与加勒比区域传统 | 基本 OK | 保持 R6；标题可继续作为简称 |
| 现代主义文学 | M3 | 现代主义 + 多个先锋派 | **C1/C2** | M3.1 现代主义 |
| 世界神话文学 | G1 | 口述与民间文学整体 | **C1/C2** | G1 下“神话”叶节点 |
| 成长文学 | G4.3 | 社会与人物型小说分组 | **C1/C2** | G4.3 下“成长小说 / Bildungsroman”叶节点 |
| 家族文学 | G4.3 | 社会与人物型小说分组 | **C1/C2** | G4.3 下“家族小说 / Family Saga”叶节点 |
| 历史文学 | G4.4 | 历史、战争、革命、殖民、移民、创伤等分组 | **C1/C2** | G4.4 下“历史小说 / Historical Fiction”叶节点；专题边界另保留 |
| 推理文学 | G4.5 | 多个现代类型文学的集合 | **C1/C2** | G4.5 下“推理 / 犯罪”叶节点 |
| 科幻文学 | G4.5 | 多个现代类型文学的集合 | **C1/C2** | G4.5 下“科幻”叶节点 |
| 奇幻文学 | G4.5 | 多个现代类型文学的集合 | **C1/C2** | G4.5 下“奇幻”叶节点 |
| 恐怖文学 | G4.5 | 多个现代类型文学的集合 | **C1/C2** | G4.5 下“恐怖 / 怪奇”叶节点 |
| 冒险文学 | G4.5 | 多个现代类型文学的集合 | **C1/C2** | G4.5 下“冒险”叶节点 |
| 反乌托邦文学 | G4.6 | 乌托邦、反乌托邦、架空历史、哲学小说等集合 | **C1/C2** | G4.6 下“反乌托邦”叶节点 |
| 旅行文学 | G7 | 纪实文学整体 | **C1/C2** | G7 下“旅行文学 / Travel Writing”叶节点 |
| 不可靠叙述 | N2 | 聚焦 + 可靠性两组机制 | **C1/C2/C6** | 先完成 N2 拆分，再建立“不可靠叙述”叶节点 |
| 爱情文学 | Q2 | 爱、欲望、婚姻、友谊、背叛、失去、哀悼 | **C1/C2** | Q2 下“爱情”叶节点 |
| 战争文学 | Q6 | 战争、屠杀、种族灭绝、国家暴力、家庭暴力、创伤等 | **C1/C2** | Q6 下“战争”叶节点 |
| 历史、记忆与时间 | Q10 | 与专题范围一致 | OK | 保持 Q10 |
| 世界武人、边疆与法外英雄文学 | Q15 | 与 umbrella 的核心问题一致 | OK / 特殊 | 保持 Q15，明确 `anchor_mode: umbrella` |

> 上表中的 leaf code 只确认**语义位置**。除已存在的 `M3.1` 外，本审计不冻结新的数字编号。

---

# 4. T 轴审计：一级稳定，二级发生轴污染

## 4.1 可以保留的部分

T 轴一级节点：

```text
T0 史前—500
T1 500—1500
T2 1500—1800
T3 1800—1890
T4 1890—1945
T5 1945—1980
T6 1980—至今
```

它们都在回答同一个问题：

> **它发生在文学史什么时候？**

因此 T0—T6 作为一级骨架可以继续保留。

T5 专题本身覆盖整个 T5，所以 `T5 → 二战后多极文学 Topic` 是当前少数没有坍缩的直接挂载。

## 4.2 当前问题：T0.1—T6.x 并不是时间子区间

当前代码中的下一级大量是：

- 口述—仪式文学系统
- 古典文学体系成熟
- 印刷文化扩张
- 小说成为核心文类
- 现实主义范式遭到挑战
- 去殖民化
- 冷战文学世界
- 小说再实验
- 全球化与跨国文学
- 性别、身体与酷儿文学
- 类型文学与纯文学融合

这些内容非常有价值，但它们回答的是：

> “这个时期发生了哪些结构变化？”

而不是：

> “这个时期还可以怎样继续按时间拆分？”

因此把它们编号成 `T5.1 / T5.2 / ...` 会制造 **C5 轴内维度污染**。

## 4.3 Canonical 建议

T 轴以后遵守：

> **只有具有时间边界的节点，才获得 T taxonomy code。**

历史阶段中的思想、体裁、区域、主题与制度变化改为：

- `period_features`
- `historical_processes`
- 指向 M / G / R / Q 节点的 cross-link
- 或具体 T Topic 内的结构页

例如 T5 可表达为：

```text
T5 1945—1980
├─ （若需要 taxonomy 子层）1945—1955
├─ 1955—1965
├─ 1965—1975
└─ 1975—1980

related processes:
- 去殖民化
- 冷战
- 身份政治
- 小说实验
- 类型文学扩张
```

不要再把“去殖民化”本身写成时间节点。

**T 轴结论：一级 A；二级编码规则需要重做。**

---

# 5. R 轴审计：整体可用，但应从“单树”升级为带交叉关系的传统网络

## 5.1 优点

R1—R10 已经较好地建立：

- 宏观地区；
- 语言 / 国别传统；
- 跨国传统；
- Diaspora / 流亡等跨区域关系。

R6 专题正文实际明确纳入加勒比、巴西、原住民、Afro-Latin 与多语言传统，因此当前 `R6 → 拉丁美洲文学 Topic` 基本能够代表整个节点范围。

## 5.2 当前问题

### C3：一级节点并非完全同型

例如：

- R2 = 东亚文学，明显是区域；
- R4 = 欧洲文学，明显是区域；
- R1 = 西亚—地中海**古老传统**，带强时间限定；
- R10 = **跨区域文学传统**，不是地理区域。

由于 R 轴本身定义为“地区 / 文学传统”，这种差异并非必须消灭，但应通过 `node_kind` 明示。

### C7：部分概念重复出现

例如：

- `R7.7 非洲离散文学`
- `R10.2 非洲离散文学`

同一概念不应在同一轴拥有两个彼此无说明的 canonical code。

类似的“区域母体 vs diaspora 网络”关系应改成：

```text
canonical node
+ broader / related tradition links
```

而不是复制节点。

## 5.3 Canonical 建议

给 R 节点增加语义类型：

- `regional_cluster`
- `language_tradition`
- `national_tradition`
- `civilizational_tradition`
- `diaspora_network`
- `transregional_network`

允许一个传统通过 `related_regions` / `broader_traditions` 建立多重关系。

**R 轴结论：骨架可保留；需要去重和关系类型化，不需要整体推倒。**

---

# 6. M 轴审计：需要区分“时代容器”与“真正思潮节点”

## 6.1 当前一级节点不是完全同一种对象

当前存在：

- M1 早期现代思想与美学 —— 时间容器
- M2 19世纪文学思潮 —— 时间容器
- M3 现代主义与先锋派 —— 运动群
- M4 政治、民族与文化运动 —— 功能 / 社会运动群
- M5 战后与当代美学范式 —— 时间容器

它们作为阅读导航是好用的，但不是严格的同型 taxonomy siblings。

## 6.2 M3 的确定坍缩

M3 明确包含：

```text
M3.1 现代主义
M3.2 意象主义
M3.3 表现主义
M3.4 未来主义
M3.5 阿克梅主义
M3.6 达达主义
M3.7 超现实主义
...
```

因此“现代主义文学”应当挂在 **M3.1**，而不是直接占据 M3。

这是当前最清楚的 C1 / C2 之一。

## 6.3 M4 / M5 的节点种类需要显式化

目前同一层可能混有：

- aesthetic movement
- political literary movement
- cultural formation
- historical writer group / publishing phenomenon
- critical / identity formation

例如 `拉美文学 Boom` 与 `魔幻现实主义` 本来就不是同一种对象；当前文件已经意识到这一点，但 metadata 尚未表达。

## 6.4 Canonical 建议

增加：

```yaml
node_kind: aesthetic_movement | literary_movement | cultural_formation | critical_formation | historical_group
```

M1—M5 可以继续作为 **navigation cluster**，但真正作为作品 `axis_m` 精确坐标和 Topic anchor 的，应优先是具体 movement / paradigm 叶节点。

**M 轴结论：上层可保留为导航容器；精确语义必须下沉。**

---

# 7. G 轴审计：当前最严重，不能继续把 G4 当普通单继承树

## 7.1 G1 与 G7 是确定父类坍缩

### G1

当前 canonical 定义：

```text
G1 口述与民间文学
├─ 神话
├─ 传说
├─ 民间故事
├─ 童话
├─ 寓言
├─ 口传史诗
├─ 歌谣
└─ 都市传说
```

因此：

```text
G1 ≠ 世界神话文学
```

世界神话文学必须挂到 G1 下的“神话”叶节点。

### G7

当前 canonical 定义：

```text
G7 纪实文学
├─ 报告文学
├─ 文学新闻
├─ 口述史
├─ 旅行文学
├─ 自然写作
└─ 见证文学
```

因此：

```text
G7 ≠ 旅行文学
```

旅行文学必须挂到 G7 下的“旅行文学 / Travel Writing”叶节点。

## 7.2 G4.1—G4.7 的根本问题：它们不是同一种“子类型”

当前 G4 的第二层实际上按七种不同标准分类：

```text
G4.1  篇幅 / 基础形式
G4.2  历史形成的形式
G4.3  社会 / 人物取向
G4.4  历史 / 现实对象
G4.5  现代类型传统
G4.6  思辨 / 思想模式
G4.7  读者 / 市场
```

这七个维度可以同时描述同一本小说。

例如一本作品完全可能同时是：

```text
长篇
+ 家族小说
+ 历史小说
+ 推理小说
+ 反乌托邦
+ YA
```

因此 G4.1—G4.7 不是严格的 `is-a` 单继承树，而是 **facet groups**。

如果继续把它们当成互斥 taxonomy child，会不断制造：

- 兄弟粒度错位；
- 重复分类；
- Topic anchor 过粗；
- 一个作品不知道该选哪个唯一 G 坐标。

## 7.3 当前 9 个 G4 Topic 都挂在 facet group，而不是具体类型

当前：

```text
G4.3 → 成长文学 / 家族文学
G4.4 → 历史文学
G4.5 → 推理 / 科幻 / 奇幻 / 恐怖 / 冒险
G4.6 → 反乌托邦
```

这些 Topic 都比所在父节点更窄。

因此不是“G4 已经合理地下钻到 G4.x 才做专题”，而是：

> **专题仍然少了一层真正的 type leaf。**

## 7.4 Canonical 建议：G4 改成 faceted hierarchy

建议保留 `G4 小说 / Fiction`，但把 G4.1—G4.7 的语义角色改为：

```yaml
node_kind: facet_group
anchorable: false
```

它们只负责组织不同分类视角，不直接作为狭义 Topic 的 final anchor。

真正可 anchor 的是其下具体叶节点，例如：

```text
[facet: social/person]
- 成长小说
- 艺术家小说
- 家庭小说
- 家族小说
- 社会小说
- 心理小说
...

[facet: genre tradition]
- 推理 / 犯罪
- 科幻
- 奇幻
- 恐怖 / 怪奇
- 冒险
- 爱情
...

[facet: historical/reality]
- 历史小说
- 战争小说
- 革命小说
...
```

> **本审计不冻结这些叶节点的数字编号。**
>
> 原因：先确认 facet 模型，再编号，比先创造 `G4.5.1 / G4.5.2...` 后再迁移安全得多。

## 7.5 G4.5 与 G4.6 还存在交叉

科幻 / 奇幻 与 Speculative Fiction、反乌托邦、架空历史等并非严格互斥。

因此以后必须允许：

- 一个作品拥有多个 G leaf；或
- G 中区分 `genre_tradition` 与 `mode/form`；
- 至少不要把 G4.5 / G4.6 当成互斥目录。

## 7.6 G 轴优先级

**P0。**

在 G4 facet 模型修复前，不建议再批量创建新的小说专题 anchor。

---

# 8. N 轴审计：结构总体清楚，但 N2 是复合节点

## 8.1 当前 N 轴的主要优点

N1—N8 大体都在回答：

> **故事怎样被讲述？**

时间、结构、人物语言、自反性、媒介等作为 mechanism families 是合理的。

## 8.2 N2 的问题

当前：

```text
N2 聚焦与可靠性
├─ 内聚焦
├─ 外聚焦
├─ 零聚焦
├─ 固定聚焦
├─ 变换聚焦
└─ 不可靠叙述
```

“聚焦”回答的是：

> 谁感知 / 谁知道 / 信息通过谁被限制？

“不可靠叙述”回答的是：

> 叙述话语的报告、解释或评价是否值得信赖？

两者相关，但不是同一分类维度。

因此 N2 是典型 **C6 复合节点**。

外部叙事学资料也把 narratorial unreliability 定义为叙述话语的可靠性问题，而不是聚焦类型本身。

## 8.3 Canonical 建议

先不急着给“不可靠叙述”补 `N2.x` 编号。

应先确定：

```text
N1 narrator / voice
N2 focalization
?  reliability
```

三者如何分工。

可以有两种安全方案：

### 方案 A：最小扰动

- 保留 N2 名称暂不改；
- 新增明确 leaf `不可靠叙述`；
- metadata 标记其 `dimension: reliability`；
- 后续再拆 N2。

### 方案 B：canonical 修复

- N1：叙述者 / 人称 / voice
- N2：聚焦 / 信息限制
- 新建独立 reliability family
- 不可靠叙述 Topic 挂 reliability leaf

本审计倾向 **B**，但编号待迁移计划阶段决定。

---

# 9. Q 轴审计：允许重叠，但 Topic 必须挂到正确问题层

## 9.1 Q 与 T/R/G 不一样

Q 是主题 / 母题 / 文学问题轴。

主题天然可以重叠，因此 Q 不需要追求严格互斥树。

例如：

```text
战争
→ 创伤
→ 记忆
→ 国家暴力
```

完全可以多重关联。

因此 Q 的目标不是制造“唯一父节点”，而是保证：

> **每个 Topic 的主问题 anchor 与专题范围匹配。**

## 9.2 两个确定坍缩

### Q2

```text
Q2 爱、欲望与亲密关系
├─ 爱情
├─ 欲望
├─ 婚姻
├─ 友谊
├─ 背叛
├─ 失去
└─ 哀悼
```

爱情文学只覆盖其中一条主线，因此应挂“爱情”叶节点，而不是整个 Q2。

### Q6

```text
Q6 战争、暴力与创伤
├─ 战争
├─ 屠杀
├─ 种族灭绝
├─ 革命暴力
├─ 国家暴力
├─ 家庭暴力
├─ 生存
├─ 创伤
└─ 创伤后记忆
```

战争文学不应代表家庭暴力、国家暴力等全部问题，因此应挂“战争”叶节点。

## 9.3 Q10 是正例

`Q10 历史、记忆与时间` 与当前 Topic 的边界基本一致，因此可以直接 anchor 在 Q10。

## 9.4 Q15 是特殊正例，不应被普通化

Q15 不是普通单主题 Topic，而是一个 comparative umbrella：

```text
武人、英雄与秩序
└─ 武侠 / 骑士 / 武士 / 剑客 / Western / Gaucho / 侠盗 / 海盗
```

Q15 本身可以继续作为主题问题 anchor。

但八个子专题不应被误认为八个 Q taxonomy child。

建议以后区分：

```yaml
primary_anchor: WL-Q15
anchor_mode: umbrella
topic_parent: WL-TOPIC-Q15
```

这样能说明：

> 子专题挂在 Q15 是出于比较 umbrella 的治理关系，而不是声称“武侠 is-a Q15 主题子类”。

---

# 10. Canonical Taxonomy Contract vNext

本审计建议后续正式增加以下合同。

## 10.1 节点类型

```yaml
node_kind:
  axis_root
  taxonomy_group
  taxonomy_leaf
  facet_group
  navigation_cluster
  umbrella_anchor
  historical_feature
```

### 含义

- `taxonomy_leaf`：可直接作为精确 Topic anchor / 作品坐标；
- `taxonomy_group`：真正的上位类，只有 Topic 覆盖整个节点时才允许直接 anchor；
- `facet_group`：组织一个分类视角，本身通常 `anchorable: false`；
- `navigation_cluster`：为阅读导航组织一组异质节点，不声称严格 is-a；
- `umbrella_anchor`：比较型 Topic 的治理锚点；
- `historical_feature`：某时间段的重要现象，不应伪装成 T 子时间节点。

## 10.2 Anchor 规则

```yaml
anchor_mode: exact | leaf | umbrella
```

规则：

1. Topic 与一个 group 范围完全一致 → `exact`；
2. Topic 只是 group 下一个具体类型 → 必须指向 `taxonomy_leaf`；
3. 比较型子专题依赖 umbrella 治理 → `umbrella`；
4. `facet_group` 默认不允许成为 final anchor；
5. Topic ID 不因为 anchor 改变而改变。

## 10.3 Topic 身份与位置解耦

例如当前：

```yaml
id: WL-TOPIC-G1-MYTH
```

这个 stable Topic ID 应继续保留。

未来变化的是：

```yaml
primary_anchor: WL-G1
```

改成新的“神话”leaf anchor。

因此：

> **专题是谁，不因为它在 taxonomy 中搬家而改变。**

## 10.4 作品坐标规则

当前使用规则写着 `axis_g` 优先填到 `G4.3 / G4.5` 这一层。

这一规则应在 taxonomy 修复后改为：

> **优先填写当前已存在的最具体 stable leaf；没有稳定 leaf 时才回退到 group。**

且：

- 不为未读作品批量补坐标；
- 已读 / 主动校准作品才迁移；
- 一个作品允许在适当轴上拥有多个不冲突的 leaf 标签，而不是被迫选择一个 facet group。

---

# 11. 修复优先级

## P0 — G 轴

原因：

- 11 个当前 G Topic 全部存在挂载粒度问题；
- G4.1—G4.7 本身是多种 facet，被误建成单继承树；
- 当前作品坐标规则又鼓励停在 G4.3 / G4.5 粗粒度。

工作顺序：

```text
G4 facet model
→ G1 / G7 leaf 实体化
→ G4 具体类型 leaf 设计
→ Topic re-anchor
→ 最后才校准已读作品 axis_g
```

## P1 — N / M / Q Topic anchor

- M3 → M3.1 现代主义
- N2 先拆 reliability / focalization
- Q2 → 爱情 leaf
- Q6 → 战争 leaf

## P1 — T 二级编码

- 保留 T0—T6；
- 停止把文学史现象编码成 T 子时间节点；
- 重新决定哪些真实时间子区间值得实体化。

## P2 — R 去重与关系类型化

- 处理 diaspora 重复；
- 给区域 / 文明 / 跨区域网络增加 node_kind；
- 不需要整体重写 R1—R10。

---

# 12. 迁移治理方案

## Phase A — 本审计

只诊断，不修改任何正式节点。

## Phase B — Canonical Taxonomy Spec

冻结：

- 每轴允许什么 node_kind；
- 什么节点允许 anchor；
- G4 facet 模型；
- N narrator / focalization / reliability 分工；
- T 二级节点只能表达时间还是允许 feature code。

这一阶段仍不迁 Topic。

## Phase C — 节点实体化

新增缺失 leaf / metadata：

- 神话
- 旅行文学
- 现代主义
- 爱情
- 战争
- G4 各专题叶节点
- N reliability 相关节点

同步：

- `03 节点/`
- `06 六轴代码对照.md`
- `id-registry-world-literature.json`
- 世界文学 Canvas / Base

## Phase D — Topic re-anchor

只修改 Topic 的 taxonomy 位置关系：

- `primary_anchor`
- 路径说明
- taxonomy node 的 `topic_map`

保持：

- `WL-TOPIC-*` stable ID 不变；
- `topics` 机器关系不变；
- Topic 内部 10 / 11 / 12 内容不因搬家重写。

## Phase E — 作品坐标渐进校准

只处理：

- 已读；
- `axis_source: read_calibrated`；
- 或明确主动校准的作品。

不批量给未读作品填新六轴坐标。

---

# 13. 本轮禁止事项

本审计明确禁止：

- 为了编号整齐直接重命名 stable Topic ID；
- 现在就把 `WL-TOPIC-G1-MYTH` 改名；
- 现在就批量改作品 `axis_*`；
- 现在就移动 20 专题地图目录；
- 在 G4 facet 模型未冻结前批量创造 `G4.5.1 / G4.5.2...`；
- 为追求同深度给所有轴制造无意义中间节点；
- 把 Q15 八个子专题伪装成普通 Q taxonomy children。

---

# 14. 审计后的系统模型

未来系统应该明确变成：

```text
六轴 Axis
  ↓
Canonical Taxonomy / Facet Graph
  ↓
最具体可解释 Anchor
  ↓
Topic Map
  ↓
Works
```

而不是：

```text
已经做了什么 Topic
  ↓
就把它塞进最近的父编号
  ↓
再反过来把父编号当成 Topic 定义
```

最终原则：

> **分类深度可以不同；分类语义不能坍缩。**
>
> **Topic 可以在任何深度展开；但必须挂在真正代表它的 canonical node 上。**
>
> **树只表示真正的 broader / narrower；多维分类必须用 facet / related relation 表达，不能为了目录整齐伪装成单继承树。**

---

# 15. 外部概念校验（仅用于设计原则，不替代本库决策）

- Dan Shen, “Unreliability”, *The Living Handbook of Narratology*：叙述不可靠性是 narratorial discourse 的可靠性问题，这支持把 reliability 与 focalization 分开建模。
- Marina MacKay, “Genre and subgenre”, *The Cambridge Introduction to the Novel*：现代小说的 genre / subgenre 边界并非天然稳定、互斥，这支持 G4 使用 facet / multi-label，而不是把不同分类原则强制压成一棵互斥树。

本系统最终仍以“个人通识地图的可维护性 + 文学概念的基本准确性 + stable identity”作为 canonical 决策标准。
