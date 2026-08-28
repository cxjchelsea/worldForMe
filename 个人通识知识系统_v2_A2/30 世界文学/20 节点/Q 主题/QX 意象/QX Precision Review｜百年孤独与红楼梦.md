---
id: WL-QX-PRECISION-001
type: literature_qx_precision_review
name: QX Precision Review｜百年孤独与红楼梦
code: QX-PRECISION-001
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
source_pilot: WL-QX-PILOT-001
works:
  - 百年孤独
  - 红楼梦
---

# QX Precision Review｜《百年孤独》与《红楼梦》

> 本文件对 Pilot 高召回候选集进行正式精度审查。
>
> 判定只使用：`KEEP / DROP / MERGE / REFRAME`。
>
> **Pilot 保留为历史候选与 schema 测试记录，不直接视为正式作品关系。只有本文件通过 Admission Gate 的关系，才可进入后续正式作品库。**

---

## 00｜Precision Review 规则

常规正式准入要求以下四项至少满足两项：

1. `recurrence`：反复出现且重复本身有意义；
2. `structural`：参与关键结构、转折、首尾、人物命运或作品阶段；
3. `binding`：与人物、关系、空间或阶段形成稳定绑定；
4. `distinctiveness`：明显参与作品文学辨识度。

例外：

```text
singular_pivotal = true
+ evidence 明确
```

可作为单次决定性意象进入正式关系。

特别强调：

> **可进行文学解释 ≠ 应进入 QX。**

---

# 01｜《百年孤独》

## 01.1 候选逐条判定

| Pilot 候选 | 判定 | Gate 依据 | 正式处理 |
|---|---|---|---|
| **雨** | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` 合理。长期降雨不仅营造氛围，而是直接组织马孔多后期的时间、空间和衰败状态。 |
| **冰** | **KEEP** | structural + distinctiveness；兼具关键首尾记忆结构 | 保留。它与作品开篇最著名的时间回环、早期马孔多面对知识与奇观的经验高度绑定。 |
| **黄色 / 黄花** | **KEEP** | recurrence + binding + distinctiveness | 保留。不是普通色彩描写，而是反复与死亡、异常事件和命运性时刻形成稳定网络。 |
| **栗树** | **KEEP** | recurrence + binding + distinctiveness | 保留。与家族始祖晚年、孤独和家宅空间长期绑定，具有稳定识别度。 |
| **小金鱼** | **KEEP** | recurrence + binding + distinctiveness | 保留。反复制作—熔化—再制作形成高度稳定的人物仪式，并参与战争后空虚与循环结构。 |
| **羊皮卷 / 手稿** | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant` 合理。手稿直接参与预言、历史保存、阅读行为与结尾世界毁灭的结构闭合。 |
| **火车 / 铁路** | **KEEP** | structural + binding + distinctiveness | 保留，但 `salience` 建议由 Pilot 的 `core` 下调为 **significant**。它明确标记现代资本和外部世界进入，但不是全书最核心的反复意象。 |
| **血** | **KEEP** | singular_pivotal exception + distinctiveness | 保留为 **significant**。其价值不在重复，而在血液自行穿过家宅抵达家人的高度异常、可辨识场景，满足单次决定性例外。 |

## 01.2 正式结果

```text
PILOT_CANDIDATES = 8
KEEP = 8
DROP = 0
MERGE = 0
REFRAME = 0
```

但精度审查并不意味着原 salience 全部原样接受：

- `火车 / 铁路`: `core → significant`；
- `血`: 保持 `significant`，明确依赖 `singular_pivotal` 例外；
- 其余可沿用 Pilot salience，正式入库时再按 V1 补齐 `manifestation / perceptual_channel` 等字段。

### 01.3 为什么《百年孤独》仍然有 8 条

这不是“每本书应该有很多意象”的模板，而是该作品本身具有高密度、重复型和结构型意象网络。

它同时存在：

- 世界状态型：雨；
- 开篇奇观 / 记忆锚点：冰；
- 色彩网络：黄色；
- 人物—空间绑定：栗树；
- 人物仪式：小金鱼；
- 元文本 / 结局结构：羊皮卷；
- 历史阶段标记：火车；
- 单次决定性异常场景：血。

这些关系彼此功能独立，因此不应为了追求低数量而删掉有效信息。

---

# 02｜《红楼梦》

## 02.1 候选逐条判定

| Pilot 候选 | 判定 | Gate 依据 | 正式处理 |
|---|---|---|---|
| **通灵宝玉 / 玉** | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant`。人物身份、命运、情缘和全书真假结构都与玉高度绑定。 |
| **梦 / 太虚幻境** | **KEEP** | recurrence + structural + distinctiveness | 保留；`dominant`。梦境不是一般心理描写，而是命运预示和现实层解释框架。 |
| **大观园 / 园林** | **KEEP** | recurrence + structural + binding + distinctiveness | 保留；`dominant`。其空间状态与青春共同体形成、繁盛、受侵入和离散同步变化。 |
| **花 / 落花** | **KEEP** | recurrence + binding + distinctiveness | 保留；`core`。葬花、花谢和花事持续把自然生命周期与黛玉及众女儿的青春命运连接起来。 |
| **泪** | **KEEP** | recurrence + binding + structural + distinctiveness | 保留；`core`。“还泪”前缘与黛玉反复流泪形成稳定关系结构。 |
| **镜子 / 风月宝鉴** | **KEEP** | singular_pivotal exception + structural | 保留，但 `core → significant`。它是高度明确的单次关键器物，却主要集中于贾瑞支线，不宜与玉、大观园同级。 |
| **海棠与诗社花木** | **MERGE** | 与“花 / 落花”对象和功能高度重叠，独立辨识度不足 | 不单建关系；作为 `花 / 落花` 的 manifestation / evidence 之一保留，例如海棠诗社、咏菊等群体花事。 |
| **宴席 / 家宴** | **KEEP** | recurrence + structural + binding | 保留为 **significant**，不建议 `core`。多次宴饮稳定展示贾府等级、亲疏、资源与繁华秩序，但它更像社会场景机制而非作品核心象征。 |
| **服饰 / 首饰** | **REFRAME** | 当前对象粒度过粗；“服饰/首饰”作为大类虽反复出现，但跨作品比较信息密度低 | Pilot 的泛化关系不直接入库。未来应下沉为有独立绑定和结构功能的具体对象后重新 Admission，例如某件稳定佩饰；没有具体 evidence 时宁可不标。 |
| **灯 / 夜间灯火** | **DROP** | 主要满足氛围 / 时间背景，缺少足够 structural / binding / distinctiveness | 不进入正式 QX。可以继续存在于文本分析，但不足以成为结构化跨作品关系。 |
| **雪** | **DROP** | 可解释，但目前 Pilot 证据主要是诗性空间和反差；独立结构权重与辨识度不足 | 不进入正式 QX。若未来专题阅读发现雪在特定章节形成更强结构证据，可重新提名。 |

## 02.2 正式结果

```text
PILOT_CANDIDATES = 11
KEEP = 7
DROP = 2
MERGE = 1
REFRAME = 1
```

直接进入正式关系候选的 7 项：

1. 通灵宝玉 / 玉
2. 梦 / 太虚幻境
3. 大观园 / 园林
4. 花 / 落花
5. 泪
6. 镜子 / 风月宝鉴
7. 宴席 / 家宴

其中：

- 海棠与诗社花木并入“花 / 落花”；
- 泛化“服饰 / 首饰”不直接入库，必须具体化后重新审；
- 灯火、雪删除于正式结构化关系，但不否认其文学分析价值。

---

# 03｜两部作品对 Admission Gate 的校准结果

## 03.1 数量不是目标，精度才是目标

本轮出现两个非常不同的结果：

```text
《百年孤独》  8 → 8
《红楼梦》   11 → 7 + 1 MERGE + 1 REFRAME
```

这证明正式规则不能设统一数量配额。

- 某些作品确实存在大量彼此独立的高辨识度意象；
- 某些高密度作品虽然“什么都能分析”，但仍需要把一般物象、过粗类别和背景性场景过滤掉；
- 正式 QX 的目标不是把作品的所有文学意象记录完整，而是保留**跨作品计算和比较最有信息增益的关系**。

## 03.2 本轮验证的三类淘汰原因

### A｜可解释但不够独立

例如《红楼梦》的雪、灯火。

它们当然有文学价值，但当前证据不足以证明应成为长期结构化关系。

### B｜与已有对象高度重叠

例如“海棠与诗社花木”相对于“花 / 落花”。

应通过 `manifestation / evidence` 保存差异，而不是制造平行节点。

### C｜对象过粗

例如“服饰 / 首饰”。

这种大类容易成为高频低信息 hub。应具体化成稳定、有独立功能的对象后再重新审查。

---

# 04｜下一步

本轮结果可作为正式标注的第一组精度基线。

下一批建议继续审查：

1. 《1984》
2. 《基督山伯爵》
3. 《第一炉香》

若精度标准保持稳定，再审第二批 Pilot 的五部作品。

在 10 部作品 Precision Review 完成前：

```text
PILOT_DATA = HIGH_RECALL_CANDIDATE_SET
FORMAL_MIGRATION = ONLY_AFTER_PRECISION_KEEP
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Pilot｜五部经典作品意象试标]]
- [[QX 文学意象与场景]]
