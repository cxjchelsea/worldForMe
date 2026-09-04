---
id: WL-QX-PRECISION-002
type: literature_qx_precision_review
name: QX Precision Review｜1984、基督山伯爵与第一炉香
code: QX-PRECISION-002
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
source_pilot: QX-PILOT-001
works:
  - "1984"
  - 基督山伯爵
  - 第一炉香
---

# QX Precision Review｜《1984》《基督山伯爵》《第一炉香》

> 本文件对第一批 Pilot 剩余三部作品的高召回候选关系进行 Precision Review。
>
> 判定只依据既有 Pilot 记录与 `ADMISSION_GATE_V1`：常规关系需在 recurrence / structural / binding / distinctiveness 中至少满足两项，且仍需具备独立跨作品比较价值；`singular_pivotal` 可作为有明确 evidence 的例外。
>
> `KEEP / DROP / MERGE / REFRAME` 是正式迁入作品库前的准入判定。Pilot 原文保留，不回写历史候选。

---

## 00｜判定口径

### KEEP

通过 Admission Gate，作为独立 QX 关系进入正式作品数据。

### DROP

可以进行文学解释，但独立信息增益不足，或主要属于普通氛围、背景、局部道具。

### MERGE

对象本身有价值，但独立节点会造成近义或局部过分拆分，应并入更稳定对象的 manifestation / evidence。

### REFRAME

原对象粒度或类型不合适，需要改成更具体、可感知、可比较的对象后再进入正式数据。

---

# 01｜《1984》

## 01.1 Precision Review

| Pilot 对象 | 判定 | Gate 依据 | 正式处理 | 理由 |
|---|---|---|---|---|
| 电幕 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 贯穿日常空间，兼具宣传、监控与人物行动约束；不是一般科技背景，而是制度环境的核心感知装置。 |
| “老大哥”海报 / 眼睛 | **KEEP** | recurrence + binding + distinctiveness | 保留；`core` | 公共空间中稳定重复，将“被观看”具体化；与电幕不同，一个是监控装置，一个是视觉权力符号。 |
| 日记 / 空白书页 | **KEEP** | structural + binding + distinctiveness | 保留；`core` | 与温斯顿私人思想和反抗起点稳定绑定，书写行为使思想成为可追责物质痕迹。 |
| 珊瑚玻璃镇纸 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`core` | 与朱莉娅关系、楼上房间和过去世界稳定连接；破碎时承担明确结构回声。 |
| 楼上房间 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`core` | 形成暂时私人空间，后又被揭示为监控空间；其意义随情节发生结构性反转。 |
| 老鼠 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` 可下调为 `core` 后正式复核 | 从早期恐惧线索一直连接到 101 室终极背叛，明确满足高准入门槛；是否需要 `dominant` 留待正式入库时校准。 |
| 101 室 | **KEEP** | structural + binding + distinctiveness；singular_pivotal 强 | 保留；`core` | 是制度把抽象权力转化为个体最深恐惧的决定性空间，不是普通审讯地点。 |
| 钟 / 十三点 | **DROP** | structural 弱；distinctiveness 有限 | 不进入正式 QX | 开篇“十三点”有很强世界建构作用，但主要是一次性时间偏移信号；作为独立跨作品意象的长期比较价值不足。 |
| 胜利牌杜松子酒 / 烟草 | **DROP** | recurrence 有；其余弱 | 不进入正式 QX | 能表现匮乏、麻醉与宣传反差，但 Pilot evidence 主要支持日常世界质感，尚不足以证明其具有独立结构性或作品辨识核心地位。 |

## 01.2 正式候选集

```text
电幕
“老大哥”海报 / 眼睛
日记 / 空白书页
珊瑚玻璃镇纸
楼上房间
老鼠
101 室
```

结果：

```text
PILOT = 9
KEEP = 7
DROP = 2
MERGE = 0
REFRAME = 0
```

### 01.3 观察

《1984》说明：

- 制度装置可以是非常明确的 QX；
- 但“能快速建立世界观”的一次性细节不一定值得独立入库；
- 日常消费品即使反复出现，也不能仅凭 recurrence 自动通过 Admission Gate。

---

# 02｜《基督山伯爵》

## 02.1 Precision Review

| Pilot 对象 | 判定 | Gate 依据 | 正式处理 | 理由 |
|---|---|---|---|---|
| 海 | **KEEP** | recurrence + structural + binding | 保留；`core` | 从水手生活、伊夫堡逃亡到身份转换持续参与人物行动与空间转换，作用并非普通环境。 |
| 伊夫堡 / 监狱 | **KEEP** | structural + binding + distinctiveness | 保留；`dominant` | 囚禁阶段直接改造人物身份、知识结构与命运，是整部作品最核心的转换空间之一。 |
| 地道 / 墙壁 | **MERGE** | structural + binding，但独立粒度偏细 | 并入“伊夫堡 / 监狱”的 manifestation / evidence | 地道与墙壁的主要文学作用发生在伊夫堡系统内部，独立建立跨作品节点会把同一空间机制过度拆分。 |
| 基督山岛 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 连接宝藏、秘密、新身份与控制能力，是伯爵身份的地理核心。 |
| 宝藏 / 黄金 / 珠宝 | **KEEP** | recurrence + structural + binding + distinctiveness | 归一为“宝藏 / 财富”对象；`dominant` | 财富不是普通财物，而是角色从受害者转变为能够重塑社会关系的行动资源。 |
| 钻石 | **MERGE** | structural 局部强；binding 局部 | 并入“宝藏 / 财富”的 manifestation / evidence | 钻石在卡德鲁斯线具有明确作用，但跨全作独立稳定性不足；更适合作为财富对象的一种具体 manifestation。 |
| 裹尸袋 / 尸体身份 | **KEEP** | singular_pivotal + structural + distinctiveness | 保留；`core` | 一次性但决定越狱与“旧身份死亡—新身份出生”的关键转换，正是 singular_pivotal 例外的典型。 |
| 毒药 | **KEEP** | recurrence + structural + binding | 保留；`core` 可下调 `significant` 后正式复核 | 在维尔福家庭线反复推动死亡、怀疑与家庭内部腐败，具有独立机制，不只是一次性凶器。 |
| 服饰 / 化装 / 身份外观 | **REFRAME** | recurrence + structural + binding，但对象过粗 | 改为“化装 / 伪装外观”再正式标注 | 原对象混合了服饰类别与身份表演机制；正式 QX 应落到更具体的“化装 / 伪装外观”，而不是泛化“服饰”。 |

## 02.2 正式候选集

```text
海
伊夫堡 / 监狱
基督山岛
宝藏 / 财富
裹尸袋 / 尸体身份
毒药
化装 / 伪装外观（REFRAME 后）
```

结果：

```text
PILOT = 9
KEEP = 6
MERGE = 2
REFRAME = 1
DROP = 0
```

若 REFRAME 完成后计入正式关系，则预计正式关系数为 7。

### 02.3 观察

《基督山伯爵》说明：

- 情节型小说可以拥有很多明确 QX，但应防止把同一情节机制拆得过细；
- “地道 / 墙壁”与“钻石”都有文学功能，却更适合作为上位对象的具体 manifestation；
- `singular_pivotal` 的确需要保留，否则裹尸袋这种决定性对象会被错误过滤。

---

# 03｜《第一炉香》

## 03.1 Precision Review

| Pilot 对象 | 判定 | Gate 依据 | 正式处理 | 理由 |
|---|---|---|---|---|
| 炉香 / 香气 | **KEEP** | recurrence + structural + distinctiveness | 保留；`dominant` | 题名、开篇框架、叙事时间与感官氛围高度绑定，是作品极强辨识对象。 |
| 梁宅 / 洋房 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` | 不是普通住宅背景，而是重塑薇龙生活方式、关系网络与价值尺度的核心空间。 |
| 衣橱 / 华服 | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`core`，原 `dominant` 建议下调 | 与薇龙身份变化和进入上流社交机制稳定绑定，但不足以单独组织全作感知世界。 |
| 珠宝 / 首饰 | **MERGE** | recurrence + binding，但与衣橱 / 华服高度重叠 | 并入“衣橱 / 华服”的 manifestation / evidence | Pilot 证据显示其主要与服饰共同构成同一物质身份系统，独立关系的信息增益有限。 |
| 花园 / 亚热带植物 | **DROP** | recurrence + spatial_bound，但 structural / distinctiveness 弱 | 不进入正式 QX | 能营造香港湿热、繁复、异域化环境，但现有 evidence 主要支持氛围与空间质感，尚不足以证明其独立辨识与结构作用。 |
| 舞会 / 宴饮 / 社交场 | **KEEP** | recurrence + structural + binding | 归一为“舞会 / 社交场”；`core` 可下调 `significant` 后正式复核 | 反复成为婚恋、阶层与关系交换发生的主要场域，明显超过一般背景性社交描写。 |
| 夜 / 灯光 | **DROP** | recurrence 有；其余弱 | 不进入正式 QX | 主要承担魅惑、暧昧和都市氛围塑造；缺乏独立结构性和稳定绑定，符合“可解释但不必入库”。 |
| 身体 / 凝视 | **REFRAME / NOT YET ADMITTED** | binding + thematic relevance；对象边界不清 | 暂不进入正式 QX；未来若能落到具体身体对象再重审 | “身体 / 凝视”把可感知对象和社会观看机制混在一起，过于抽象；其当前信息更适合由服饰、社交场及 QH 身体/性别关系承载。 |

## 03.2 正式候选集

```text
炉香 / 香气
梁宅 / 洋房
衣橱 / 华服
舞会 / 社交场
```

结果：

```text
PILOT = 8
KEEP = 4
MERGE = 1
DROP = 2
REFRAME_NOT_ADMITTED = 1
```

### 03.3 观察

《第一炉香》是新 Admission Gate 最有价值的压力测试之一：

- 感官性强、描写丰富，不意味着所有感官材料都应进入 QX；
- “夜色”“植物”可以非常有文学效果，但主要作为环境氛围时应 DROP；
- “身体 / 凝视”显示 QX 必须坚持具体对象边界，不能把抽象观看关系伪装成意象；
- 反而“炉香”“梁宅”“衣橱 / 华服”“舞会 / 社交场”具有清晰独立结构和跨作品比较价值。

---

# 04｜第一批 Pilot Precision 汇总

结合上一份 [[QX Precision Review｜百年孤独与红楼梦]]：

| 作品 | Pilot 候选 | KEEP | MERGE | DROP | REFRAME |
|---|---:|---:|---:|---:|---:|
| 《百年孤独》 | 8 | 8 | 0 | 0 | 0 |
| 《红楼梦》 | 11 | 7 | 1 | 2 | 1 |
| 《1984》 | 9 | 7 | 0 | 2 | 0 |
| 《基督山伯爵》 | 9 | 6 | 2 | 0 | 1 |
| 《第一炉香》 | 8 | 4 | 1 | 2 | 1 |

第一批合计：

```text
PILOT_CANDIDATES = 45
KEEP = 32
MERGE = 4
DROP = 6
REFRAME = 3
```

其中 REFRAME 不自动等于正式入库；只有重构为符合 QX 对象边界的新对象并再次通过 Admission Gate 后，才计为正式关系。

### 04.1 Precision 信号

第一批从 45 条高召回候选中直接 KEEP 32 条，说明：

- Pilot 确实偏 recall-first，但并非全面过标；
- 高密度经典作品可以自然保留很多 QX；
- 新门槛主要过滤三类噪声：
  1. 纯氛围材料；
  2. 同一上位对象的过细拆分；
  3. 把抽象关系 / 主题误装成具体意象。

这比人为规定“每本最多几个”更稳定。

---

## 状态

```text
QX_PRECISION_REVIEW_PILOT_001 = COMPLETE
PILOT_001_CANDIDATES = 45
DIRECT_KEEP = 32
MERGE = 4
DROP = 6
REFRAME = 3
FORMAL_MIGRATION = NOT_YET_EXECUTED
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Pilot｜五部经典作品意象试标]]
- [[QX Precision Review｜百年孤独与红楼梦]]
