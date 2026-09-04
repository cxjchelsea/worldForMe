---
id: WL-QX-FORMAL-MIGRATION-001
type: literature_qx_migration_report
name: QX Formal Migration｜首批十部作品
code: QX-MIGRATION-001
axis: Q
facet: QX
status: COMPLETE_WITH_WORK_LEVEL_DEFERRED
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Migration｜首批十部作品

> 本文件记录两轮 Pilot 经 Precision Review 后向中央作品库的第一次正式 QX 迁移。
>
> 原则：`KEEP` 迁移；`MERGE` 吸收到对应正式对象的 `manifestation / evidence`；`DROP` 不迁移；`REFRAME` 必须重新通过 Admission Gate 后才可进入正式数据。

---

## 01｜迁移结果

| 作品 | 正式关系数 | 状态 |
|---|---:|---|
| 《百年孤独》 | 8 | COMPLETE |
| 《红楼梦》 | 7 | COMPLETE |
| 《1984》 | 7 | COMPLETE |
| 《基督山伯爵》 | 7 | COMPLETE_WITH_REFRAME_ADMITTED |
| 《第一炉香》 | 4 | COMPLETE |
| 《局外人》 | 5 | COMPLETE_WITH_REFRAME_ADMITTED |
| 《海底两万里》 | 6 | COMPLETE |
| 《小王子》 | 7 | COMPLETE |
| 《银河铁道之夜》 | 4 | COMPLETE |
| 《夜晚的潜水艇》 | 0 | DEFER_TO_WORK_LEVEL |

合计：

```text
FORMAL_WORKS_MIGRATED = 9
FORMAL_QX_RELATIONS = 55
COLLECTION_LEVEL_DEFERRED = 1
```

---

## 02｜MERGE 处理

Precision Review 中的 12 条 `MERGE` 不再作为独立关系计数，而被吸收到正式对象的具体形态或证据中。

典型例子：

- 《红楼梦》：海棠与诗社花木 → `花 / 落花` 的 manifestation / evidence；
- 《基督山伯爵》：地道 / 墙壁 → `伊夫堡 / 监狱`；钻石 → `宝藏 / 财富`；
- 《第一炉香》：珠宝 / 首饰 → `衣橱 / 华服`；
- 《局外人》：热 / 炎热、白色 / 强光 → `太阳 / 阳光`；
- 《海底两万里》：深海 / 海底、黑暗 → `海 / 海洋`；电光 / 人造光 → `鹦鹉螺号`；
- 《银河铁道之夜》：星星 / 星座、河 / 天河、光 / 发光物 → `银河 / 银河空间` 与 `夜`。

该处理避免同一感知系统被重复计权。

---

## 03｜DROP 处理

Precision Review 中明确判为 `DROP` 的候选不迁移到中央作品库。

```text
DROP_TOTAL = 9
```

删除的是“可解释但不值得成为正式 QX 关系”的对象，而不是否认其文学意义。

---

## 04｜REFRAME Resolution

原始：

```text
REFRAME_TOTAL = 13
```

### 04.1 再审后正式准入：2

#### 《基督山伯爵》

原：

```text
服饰 / 化装 / 身份外观
```

重构为：

```text
化装 / 伪装外观
```

判定：`ADMITTED`。

依据：原 Pilot 已支持其 recurrence + structural + binding；重构后对象不再泛指所有服饰，而明确指向唐泰斯借可感知外观进入不同社会关系网络的身份伪装机制。

#### 《局外人》

原：

```text
棺木 / 葬礼
```

重构为：

```text
守灵 / 葬礼仪式
```

判定：`ADMITTED`。

依据：真正稳定运作的是开篇社会哀悼仪式及其规范期待；该仪式后来在审判中重新成为人格与道德判断材料，满足 structural + distinctiveness。

```text
REFRAME_ADMITTED = 2
```

### 04.2 明确关闭，不进入 QX：3

#### 《红楼梦》：服饰 / 首饰

判定：`CLOSED_NOT_ADMITTED`。

原因：现有 Pilot 只支持泛化服饰大类，没有足够具体、稳定的单一 object 与 evidence。未来阅读若发现某件明确佩饰或服装达到 Gate，可作为新候选重新提名，但本条不继续悬挂。

#### 《第一炉香》：身体 / 凝视

判定：`CLOSED_TO_QH_RELATION_LAYER`。

原因：“身体 / 凝视”混合了对象与社会观看机制；现有信息更适合由 `衣橱 / 华服`、`舞会 / 社交场` 与 QH 身体 / 性别 / 欲望关系承载，不应为补齐数量而制造 QX 对象。

#### 《小王子》：狐狸

判定：`CLOSED_TO_CHARACTER_QH_QC_LAYER`。

原因：现有 Pilot 支持的主要是完整角色的对话、教导与“驯养—关系—责任”功能，而不是“狐狸作为动物意象”的独立物象运作。QX 不吞并完整角色。

```text
REFRAME_CLOSED_NOT_QX = 3
```

### 04.3 证据不足，保留为未来新提名：1

#### 《海底两万里》：巨型海洋生物

原对象是类别而非稳定 object。Pilot 仅提供“巨型章鱼、鲸类等”作为群组 evidence，尚不足以在不补充文本材料的前提下选定某一具体动物并证明其独立 Gate。

因此：

```text
STATUS = CLOSED_AS_GENERIC_CATEGORY
FUTURE_RENOMINATION = ALLOWED_WITH_SPECIFIC_OBJECT_AND_EVIDENCE
```

它不再计入当前待处理 REFRAME。

### 04.4 Work 粒度延后：7

《夜晚的潜水艇》当前中央作品库只有集子 Work：

```text
WL-WORK-2734 = 夜晚的潜水艇（collection-level entity）
```

Pilot 中以下 7 条：

```text
潜水艇
夜
水下 / 下潜空间
电影 / 银幕 / 影像
旧物 / 收藏物
城市夜景 / 街道
声音 / 音乐 / 广播式媒介声
```

均不能直接迁移到 collection 层。仓库当前没有这些候选所属具体短篇的独立 Work 实体，因此不在缺少作品粒度证据时人工猜测归属。

```text
REFRAME_DEFERRED_TO_STORY_WORK = 7
COLLECTION_LEVEL_QX = 0
```

---

## 05｜REFRAME 最终状态

```text
REFRAME_TOTAL = 13
REFRAME_ADMITTED = 2
REFRAME_CLOSED_NOT_QX = 3
REFRAME_GENERIC_CATEGORY_CLOSED = 1
REFRAME_DEFERRED_TO_STORY_WORK = 7
REFRAME_UNRESOLVED_AT_CURRENT_WORK_LEVEL = 7
```

换言之，除《夜晚的潜水艇》需要未来建立单篇 Work 外，其余 REFRAME 已全部收敛。

---

## 06｜正式数据约束

本次迁移后的中央 Work 文件遵守：

```text
QX_RELATION_SCHEMA_V1
ADMISSION_GATE_V1
WORK_GRANULARITY_DEFAULT = SMALLEST_INDEPENDENT_NARRATIVE_UNIT
```

正式关系至少包含：

```text
object
salience
function
evidence
```

候选对象尚未激活正式 QX 叶节点时：

```yaml
qx_id: null
```

只有已经存在的正式节点才使用实际编号，例如《百年孤独》的“雨”使用 `QX1.1`。

---

## 07｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
PRECISION_REVIEW = COMPLETE_FOR_10_PILOT_WORKS
FORMAL_MIGRATION = COMPLETE_FOR_AVAILABLE_WORK_LEVEL
FORMAL_QX_RELATIONS = 55
REFRAME_RESOLVED_EXCEPT_STORY_GRANULARITY = YES
NIGHT_SUBMARINE_COLLECTION_MIGRATION = DEFERRED
```

下一阶段：

1. 对 55 条正式关系做 object normalization；
2. 检查哪些 object 已达到专题激活门槛；
3. 对达到门槛的对象建立正式 QX 叶节点并回填 `qx_id`；
4. 再进入更大规模的已读作品正式标注。

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Precision Review｜百年孤独与红楼梦]]
- [[QX Precision Review｜1984、基督山伯爵与第一炉香]]
- [[QX Precision Review｜第二批五部作品]]
