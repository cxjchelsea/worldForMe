---
id: WL-QX-PRECISION-003
type: literature_qx_precision_review
name: QX Precision Review｜第二批五部作品
code: QX-PRECISION-003
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
source_pilot: QX-PILOT-002
works:
  - 局外人
  - 海底两万里
  - 小王子
  - 银河铁道之夜
  - 夜晚的潜水艇
---

# QX Precision Review｜第二批五部作品

> 本文件对第二批 Pilot 的 42 条高召回候选关系进行 Precision Review。
>
> 常规关系需在 `recurrence / structural / binding / distinctiveness` 中至少满足两项，并仍具有独立跨作品比较价值；`singular_pivotal` 可作为有明确 evidence 的例外。
>
> 本轮同时严格执行 `WORK_GRANULARITY_DEFAULT = SMALLEST_INDEPENDENT_NARRATIVE_UNIT`。Pilot 原文保留，不回写历史候选。

---

## 00｜判定口径

- **KEEP**：通过 Admission Gate，可作为独立正式 QX 关系。
- **DROP**：可解释，但独立信息增益不足。
- **MERGE**：有价值，但更适合作为另一稳定对象的 `manifestation / perceptual_channel / evidence`。
- **REFRAME**：对象粒度、类型或作品层级不合适，重构后再审；不自动计入正式关系。

---

# 01｜《局外人》

## 01.1 Precision Review

| Pilot 对象 | 判定 | Gate 依据 | 正式处理 | 理由 |
|---|---|---|---|---|
| 太阳 / 阳光 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 葬礼与海滩关键段落反复通过刺眼、灼热、反光影响人物身体与行动，是作品最具辨识度的感知条件之一。 |
| 热 / 炎热 | **MERGE** | recurrence + binding，但与太阳高度耦合 | 并入“太阳 / 阳光”的 `manifestation + perceptual_channel: thermal/bodily` | 其价值主要来自太阳在本作中的具体感知形态；独立建“热”节点会把同一经验拆成两个关系。 |
| 汗 / 身体湿热 | **DROP** | recurrence 有，但 structural / distinctiveness 弱 | 不进入正式 QX | 是身体物质性的重要描写，但现有证据更适合作为“太阳 / 炎热”的身体 manifestation，而非独立跨作品对象。 |
| 海 | **KEEP** | recurrence + binding + contrastive | 保留；`core` | 与玛丽的愉悦、亲密经验和后续暴力空间形成稳定反差，超出普通海滨背景。 |
| 白色 / 强光 | **MERGE** | recurrence 有，但对象与阳光/眩光重叠 | 并入“太阳 / 阳光”的视觉 manifestation | 主要承担刺眼、过曝式感知强化，独立建立“白色”关系信息增益不足。 |
| 枪 | **KEEP** | structural + singular_pivotal + distinctiveness | 保留；`core` | 把感官刺激、偶然情境和不可逆法律后果连接成全书结构断点。 |
| 法庭 / 审判空间 | **KEEP** | structural + binding + distinctiveness | 保留；`core` | 后半部长期把私人行为和情感表达转化为公共规范判断，是制度性空间而非普通场景。 |
| 棺木 / 葬礼 | **REFRAME** | structural + distinctiveness，但对象混合 | 改为“守灵 / 葬礼仪式”后再正式标注 | 真正稳定运作的是社会哀悼仪式及其规范期待，而不是“棺木”这一器物本身。重构后大概率可通过 Gate。 |

结果：

```text
PILOT = 8
KEEP = 4
MERGE = 2
DROP = 1
REFRAME = 1
```

### 01.2 观察

《局外人》说明：感官密集不意味着要把每种体感拆成独立意象。`太阳 + manifestation + perceptual_channel` 可以比“太阳 / 热 / 汗 / 白光”四个平行节点更准确、更稀疏。

---

# 02｜《海底两万里》

## 02.1 Precision Review

| Pilot 对象 | 判定 | Gate 依据 | 正式处理 | 理由 |
|---|---|---|---|---|
| 海 / 海洋 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 海洋是全书世界本体，决定交通、资源、风险、社会关系和探索边界。 |
| 深海 / 海底 | **MERGE** | recurrence + structural，但与“海”上下位重叠 | 并入“海 / 海洋”的 manifestation / scope | 深海是本作中“海”的核心具体形态；独立并列会造成上位对象与 manifestation 重复计权。 |
| 鹦鹉螺号 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 同时是交通工具、居所、实验室、政治避难所和封闭社会，是全书核心技术—空间对象。 |
| 舷窗 / 观察窗 | **KEEP** | recurrence + binding + distinctiveness | 保留；`core` 可在正式入库时复核为 `significant` | 持续组织“内部安全空间—外部巨大海洋”的观看边界，具有独立跨作品比较价值。 |
| 电光 / 人造光 | **MERGE** | recurrence + binding，但独立结构性不足 | 并入“鹦鹉螺号”的 manifestation / function / perceptual evidence | 技术照明的重要性主要来自潜艇使深海可见的能力，作为独立节点会过度拆解技术系统。 |
| 黑暗 | **MERGE** | recurrence 有，但更多是环境感知条件 | 并入“海 / 深海”的 manifestation 与视觉对照 evidence | 与深海不可见性和人造光形成对照，但目前不足以成为独立正式对象。 |
| 海底森林 / 植物群 | **KEEP** | recurrence + binding + distinctiveness | 保留；`core` | 把陆地“森林”经验重构到海底，既是空间又是奇观，具有高度可比较的陌生化形态。 |
| 巨型海洋生物 | **REFRAME** | recurrence + structural，但对象过粗 | 不以“巨型海洋生物”入库；若具体物种/事件足够稳定再审 | “巨型生物”是类别，不是稳定 object；需具体化到章鱼等对象，并重新检查是否达到 Gate。 |
| 冰 / 冰层 | **KEEP** | structural + singular/climactic + distinctiveness | 保留；`core` | 极地冰层把海洋自由反转为困闭空间，使技术能力与自然边界发生决定性冲突。 |
| 海底墓地 / 珊瑚墓地 | **KEEP** | structural + binding + distinctiveness | 保留；`significant` | 将死亡、纪念和与陆地社会断绝统一到海洋空间，虽篇幅有限但具有独立、明确的空间—仪式结构。 |

结果：

```text
PILOT = 10
KEEP = 6
MERGE = 3
DROP = 0
REFRAME = 1
```

### 02.2 观察

本作证明 `manifestation` 的必要性：海、深海、黑暗并不都需要独立节点。QX 应避免把同一世界对象的不同环境状态重复计权。

---

# 03｜《小王子》

## 03.1 Precision Review

| Pilot 对象 | 判定 | Gate 依据 | 正式处理 | 理由 |
|---|---|---|---|---|
| 玫瑰 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 与离开、思念、比较和重新理解关系的主线稳定绑定，是最核心的具体对象之一。 |
| 狐狸 | **REFRAME / NOT YET ADMITTED** | structural + binding + distinctiveness，但更接近完整角色 | 不直接作为 QX 动物关系；优先由角色/QH/QC 层承载“驯养—关系—责任” | Pilot 中狐狸的主要价值来自对话、教导和角色功能，而非作为“狐狸这一动物意象”的可感知复用。QX 不应吞并完整角色。 |
| 星星 / 星空 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 从宇宙位置逐渐转化为叙述者记忆、失去和联系的媒介，前后回声明确。 |
| 沙漠 | **KEEP** | recurrence + structural + binding | 保留；`core` | 相遇、寻找水、离别与死亡边界均发生于此，是稳定阈限空间。 |
| 井 / 水 | **KEEP** | structural + binding + distinctiveness | 保留；`core` | 在沙漠中形成强对照，并承担寻找、生命和精神满足的决定性场景。 |
| 蛇 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`core` | 从初次出现到结尾返回，持续连接危险、死亡和返乡通道；其作用不只来自角色对话。 |
| 猴面包树 | **KEEP** | recurrence + structural + distinctiveness | 保留；`core` | 反复作为必须日常清理的潜在失控力量，直接参与小行星生活秩序。 |
| 小行星 / 星球 | **KEEP** | recurrence + structural + distinctiveness | 保留；`core` | 多个星球把不同人物和生活秩序压缩为空间单元，并组织旅行结构。 |
| 围巾 / 金色头发等人物视觉特征 | **DROP** | binding 有，但 structural / independent distinctiveness 弱 | 不进入正式 QX | 有人物识别作用，但更接近人物造型特征，独立跨作品分析价值不足。 |

结果：

```text
PILOT = 9
KEEP = 7
DROP = 1
REFRAME_NOT_ADMITTED = 1
MERGE = 0
```

### 03.2 观察

《小王子》验证了 QX 与角色层的边界：**具体动物并不因为“很重要”就一定是 QX。** 当其价值主要来自完整人物行为与语言功能时，应优先放回角色/QH/QC；只有作为稳定可感知对象本身运作时，才保留 QX。

---

# 04｜《银河铁道之夜》

## 04.1 Precision Review

| Pilot 对象 | 判定 | Gate 依据 | 正式处理 | 理由 |
|---|---|---|---|---|
| 银河 / 银河空间 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 同时是天体、旅程空间和现实/彼岸边界，是整部作品世界本体。 |
| 夜 | **KEEP** | recurrence + structural + distinctiveness | 保留；`dominant` 可在正式入库时复核为 `core` | 夜不是局部氛围，而是整段宇宙旅程的基本感知条件和阈限状态。 |
| 银河列车 / 铁道 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 把沿途空间、乘客和生死经验串成移动结构，是作品最核心的交通—边界对象。 |
| 星星 / 星座 | **MERGE** | recurrence + spatial，但与银河上位对象高度重叠 | 并入“银河 / 银河空间”的 manifestation / spatial evidence | 主要用于细化银河旅程的视觉与空间节点，独立计为平行对象会重复加权。 |
| 河 / 天河 | **MERGE** | recurrence + spatial，但属于银河的感知形态 | 并入“银河 / 银河空间”的 manifestation | “银河被感知为河流式空间”正是 manifestation 的典型用途，无需再造独立水域关系。 |
| 光 / 发光物 | **MERGE** | recurrence 有，但主要承担视觉呈现 | 并入银河/夜的 `perceptual_channel + manifestation` | 作用主要是让夜间宇宙空间可见并构成明暗对照，独立信息增益不足。 |
| 十字架 / 南十字星 | **KEEP** | structural + binding + distinctiveness | 保留；`core` | 后段与乘客、生死和宗教语义集中汇合，形成明确可定位的结构节点。 |
| 鸟 / 鸟群 | **DROP** | recurrence 有限；structural / binding 弱 | 不进入正式 QX | 可强化异世界奇观，但现有 evidence 尚不足以证明独立结构性和作品辨识核心地位。 |

结果：

```text
PILOT = 8
KEEP = 4
MERGE = 3
DROP = 1
REFRAME = 0
```

### 04.2 观察

本作进一步证明：意象簇不应靠“多建几个相近节点”实现。银河、星座、天河、光可以在底层关系上适度归并，再由未来 `IMAGERY_CONSTELLATION` 从功能和 manifestation 中派生整体“夜间宇宙旅程”。

---

# 05｜《夜晚的潜水艇》

## 05.1 作品粒度判定

Pilot 明确承认该书为短篇小说集，并在集子层暂时聚合了标题篇与多篇候选。按照已冻结规则：

```text
WORK_GRANULARITY_DEFAULT = SMALLEST_INDEPENDENT_NARRATIVE_UNIT
COLLECTION_LEVEL_RELATION = REQUIRES_COLLECTION_LEVEL_EVIDENCE
```

因此，本轮**不把集子层 Pilot 候选直接转成正式 QX**。

这不是判断“本书没有意象”，而是判断：

> 当前证据粒度不足以证明这些关系属于整个 collection，而不是某一篇或若干篇。

## 05.2 Precision Review

| Pilot 对象 | 判定 | 正式处理 | 理由 |
|---|---|---|---|
| 潜水艇 | **REFRAME_TO_WORK_LEVEL** | 下沉到标题篇《夜晚的潜水艇》后重审 | 题名与标题篇辨识度极强，但“标题级强形象”本身不足以证明整部小说集存在 collection-level HAS_IMAGERY。 |
| 夜 | **REFRAME_TO_WORK_LEVEL** | 按具体短篇拆分 evidence | Pilot 写“标题篇及多个夜间经验”，但缺乏足够篇目级证据证明跨集子稳定同构。 |
| 水下 / 下潜空间 | **REFRAME_TO_WORK_LEVEL** | 下沉标题篇 | 主要 evidence 明确属于标题篇。 |
| 电影 / 银幕 / 影像 | **REFRAME_TO_WORK_LEVEL** | 先定位具体篇目，再判断是否存在真正 collection-level 反复 | “多篇”仍不足以避免假共现；需要篇级关系后才能向上聚合。 |
| 旧物 / 收藏物 | **REFRAME_TO_WORK_LEVEL** | 具体化对象并定位篇目 | 当前 object 过粗，同时存在 collection 聚合问题。 |
| 城市夜景 / 街道 | **REFRAME_TO_WORK_LEVEL** | 拆到具体篇目后审 | 当前更多是跨篇环境概括，尚不能建立正式 collection-level QX。 |
| 声音 / 音乐 / 广播式媒介声 | **REFRAME_TO_WORK_LEVEL** | 具体化声音媒介与篇目后审 | 同时存在对象过粗和作品粒度问题；不能因听觉通道稀缺而降低 Admission Gate。 |

结果：

```text
PILOT = 7
KEEP_AT_COLLECTION_LEVEL = 0
REFRAME_TO_WORK_LEVEL = 7
DROP = 0
MERGE = 0
```

### 05.3 观察

这是 Precision Review 中非常重要的“0 KEEP”案例。

`0 KEEP` **不等于没有文学意象**，而是说明：在当前 Work 实体粒度下，没有足够证据建立正式 collection-level QX 关系。正式标注必须先把小说集拆到单篇，再按同一 Admission Gate 审查。

---

# 06｜第二批 Precision 汇总

| 作品 | Pilot 候选 | KEEP | MERGE | DROP | REFRAME |
|---|---:|---:|---:|---:|---:|
| 《局外人》 | 8 | 4 | 2 | 1 | 1 |
| 《海底两万里》 | 10 | 6 | 3 | 0 | 1 |
| 《小王子》 | 9 | 7 | 0 | 1 | 1 |
| 《银河铁道之夜》 | 8 | 4 | 3 | 1 | 0 |
| 《夜晚的潜水艇》 | 7 | 0 | 0 | 0 | 7 |

第二批合计：

```text
PILOT_CANDIDATES = 42
DIRECT_KEEP = 21
MERGE = 8
DROP = 3
REFRAME = 10
```

其中《夜晚的潜水艇》的 7 条 REFRAME 主要是 Work 粒度治理，不应解读成低意象密度。

---

# 07｜两批十部作品总汇总

第一批 Precision：

```text
PILOT_001 = 45
DIRECT_KEEP = 32
MERGE = 4
DROP = 6
REFRAME = 3
```

第二批 Precision：

```text
PILOT_002 = 42
DIRECT_KEEP = 21
MERGE = 8
DROP = 3
REFRAME = 10
```

总计：

```text
TOTAL_PILOT_CANDIDATES = 87
DIRECT_KEEP = 53
MERGE = 12
DROP = 9
REFRAME = 13
```

直接 KEEP 率约为 61%。但这个比例不能简单解释为“原来标多了 39%”：

- 12 条 MERGE 仍然保留其信息，只是不再作为独立关系；
- 13 条 REFRAME 中，多条只是对象或 Work 粒度需要重构；
- 真正明确 DROP 的只有 9 条。

因此 Pilot 的主要问题不是大量错误，而是**高召回阶段把 manifestation、局部对象、抽象关系和 collection 聚合也暂时作为独立候选保存**。Precision Review 已把这些边界整理出来。

---

# 08｜Precision Review 后的稳定结论

1. **数量不应该预设。** 《百年孤独》可保留 8 条，而《夜晚的潜水艇》在 collection 层可为 0。
2. **QX = 0 是合法高质量结果。** 可能因为作品本身没有强 QX，也可能因为当前 Work 粒度不允许建立关系。
3. **manifestation 是降噪核心。** “热 / 白光 / 深海 / 天河 / 星光”等很多候选不必成为平行节点。
4. **角色不是自动等于意象。** 《小王子》的狐狸提示：完整人物功能优先走角色/QH/QC，不能因其动物形态自动进入 QX。
5. **感官维度不降低准入门槛。** 嗅觉、听觉、温度只通过 `perceptual_channel` 增强已有关系。
6. **作品粒度优先于标签数量。** 短篇集先拆 Work，再做关系，避免假共现。
7. **派生意象簇应建立在 Precision 后数据上。** 被 MERGE 的信息仍可通过 manifestation/function 参与未来聚类，不需要依靠节点膨胀保存。

---

## 状态

```text
QX_PRECISION_REVIEW_PILOT_002 = COMPLETE
TOTAL_PILOT_WORKS = 10
TOTAL_PILOT_CANDIDATES = 87
DIRECT_KEEP = 53
MERGE = 12
DROP = 9
REFRAME = 13
QX_RELATION_SCHEMA_V1 = STABLE_AFTER_PRECISION
ADMISSION_GATE_V1 = STABLE_AFTER_PRECISION
FORMAL_MIGRATION = READY_WITH_REFRAME_RESOLUTION
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Pilot｜第二批五部作品意象试标]]
- [[QX Precision Review｜百年孤独与红楼梦]]
- [[QX Precision Review｜1984、基督山伯爵与第一炉香]]
