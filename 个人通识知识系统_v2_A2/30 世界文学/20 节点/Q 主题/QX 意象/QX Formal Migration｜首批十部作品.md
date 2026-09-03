---
id: WL-QX-FORMAL-MIGRATION-001
type: literature_qx_migration_report
name: QX Formal Migration｜首批十部作品
code: QX-MIGRATION-001
axis: Q
facet: QX
status: COMPLETE_WITH_REFRAMES_PENDING
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Migration｜首批十部作品

> 本文件记录两轮 Pilot 经 Precision Review 后向中央作品库的第一次正式 QX 迁移。
>
> 原则：只迁移 `DIRECT KEEP`；`MERGE` 吸收到对应正式对象的 `manifestation / evidence`；`DROP` 不迁移；`REFRAME` 未再次通过 Admission Gate 前不进入正式数据。

---

## 01｜迁移结果

| 作品 | 正式迁移关系数 | 迁移状态 |
|---|---:|---|
| 《百年孤独》 | 8 | COMPLETE |
| 《红楼梦》 | 7 | COMPLETE |
| 《1984》 | 7 | COMPLETE |
| 《基督山伯爵》 | 6 | COMPLETE |
| 《第一炉香》 | 4 | COMPLETE |
| 《局外人》 | 4 | COMPLETE |
| 《海底两万里》 | 6 | COMPLETE |
| 《小王子》 | 7 | COMPLETE |
| 《银河铁道之夜》 | 4 | COMPLETE |
| 《夜晚的潜水艇》 | 0 | DEFER_TO_WORK_LEVEL |

合计：

```text
FORMAL_WORKS_MIGRATED = 9
FORMAL_QX_RELATIONS = 53
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

## 04｜REFRAME 待处理

当前仍有 13 条 `REFRAME`。它们不自动成为正式关系，需按以下三类继续处理：

### 04.1 对象粒度重构

例如：

- 泛化服饰 → 具体服饰 / 伪装对象；
- 巨型海洋生物 → 具体动物对象；
- 身体 / 凝视 → 具体身体对象或退回 QH / 关系层。

### 04.2 类型边界重构

例如：

- 《小王子》的狐狸主要作为完整角色运作，不因“是动物”自动进入 QX；
- 《局外人》的棺木 / 葬礼应改审“守灵 / 葬礼仪式”这一社会仪式对象。

### 04.3 Work 粒度重构

《夜晚的潜水艇》为短篇小说集：

```text
COLLECTION_LEVEL_QX = 0
```

Pilot 中的潜水艇、夜、水下空间、影像、旧物、城市夜景、声音等候选均需先定位到具体单篇 Work，再按 `ADMISSION_GATE_V1` 重新审查。

---

## 05｜正式数据约束

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

## 06｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
PRECISION_REVIEW = COMPLETE_FOR_10_PILOT_WORKS
DIRECT_KEEP_MIGRATION = COMPLETE
FORMAL_QX_RELATIONS = 53
REFRAME_PENDING = 13
NIGHT_SUBMARINE_COLLECTION_MIGRATION = DEFERRED
```

下一阶段不再扩大 Pilot，而应：

1. 对 13 条 REFRAME 分类处理；
2. 对达到专题激活门槛的 object 做对象归一化与跨作品聚合；
3. 再进入更大规模的已读作品正式标注。

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Precision Review｜百年孤独与红楼梦]]
- [[QX Precision Review｜1984、基督山伯爵与第一炉香]]
- [[QX Precision Review｜第二批五部作品]]
