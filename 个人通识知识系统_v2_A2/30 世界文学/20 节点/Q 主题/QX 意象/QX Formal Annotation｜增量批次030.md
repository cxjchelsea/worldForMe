---
id: WL-QX-FORMAL-ANNOTATION-030
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次030
code: QX-ANNOTATION-030
axis: Q
facet: QX
status: PARTIAL_SERIES_RECONCILIATION
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
---

# QX Formal Annotation｜增量批次030

> 本批进入 `SERIES / VOLUME GRANULARITY`。系列总称不直接挂 QX；先恢复真实阅读单元，再按 `SMALLEST_INDEPENDENT_NARRATIVE_UNIT` 进入正式标注。

## 01｜本批阶段结果

```text
HARRY_POTTER_SERIES = RESOLVED
HARRY_POTTER_CHILD_WORKS = 7
HARRY_POTTER_FORMAL_QX_WORKS = 7
HARRY_POTTER_FORMAL_RELATIONS = 21

SHERLOCK_HOLMES_SERIES = ONE_TO_MANY_RECONCILIATION
SHERLOCK_READ_SCOPE = COMPLETE_CANON_CONFIRMED
SHERLOCK_CANON_UNITS = 60
SHERLOCK_LONG_NOVELS_RECONCILED = 4
SHERLOCK_LONG_NOVEL_FORMAL_RELATIONS = 12
SHERLOCK_SHORT_STORIES_REMAINING = 56
SHERLOCK_QX = PARTIAL_4_NOVELS_COMPLETE

DRAGON_RAJAS_SERIES = DEFER_SERIES_GRANULARITY
DRAGON_RAJAS_READ_SCOPE = COMPLETE_SERIES_CONFIRMED
DRAGON_RAJAS_VERSION_BOUNDARY = UNRESOLVED

FORMAL_WORKS_WITH_QX_BEFORE = 124
FORMAL_QX_RELATIONS_BEFORE = 368
FORMAL_WORKS_WITH_QX_AFTER_GROUP_HP = 131
FORMAL_QX_RELATIONS_AFTER_GROUP_HP = 389
FORMAL_WORKS_WITH_QX_AFTER_SHERLOCK_NOVELS = 135
FORMAL_QX_RELATIONS_AFTER_SHERLOCK_NOVELS = 401
```

## 02｜《哈利·波特》：粒度闭环

此前 corpus ledger 将系列总记录列为 `DEFER_SERIES_GRANULARITY`。本批重新核验中央 `40 作品` 后发现七册 Work 均已存在，且全部明确为 `read_status = 已读`：

```text
哈利·波特与魔法石
哈利·波特与密室
哈利·波特与阿兹卡班的囚徒
哈利·波特与火焰杯
哈利·波特与凤凰社
哈利·波特与混血王子
哈利·波特与死亡圣器
```

因此不创建新实体，直接复用既有 Work，并完成正式 QX。

### 第一册｜《哈利·波特与魔法石》

```text
霍格沃茨城堡 → QX7 / dominant
分院帽 → QX15 / core
厄里斯魔镜 → QX11 / core
```

### 第二册｜《哈利·波特与密室》

```text
密室 → QX19 / dominant
汤姆·里德尔的日记 → QX16 / dominant
蛇怪 → QX5 / core
```

### 第三册｜《哈利·波特与阿兹卡班的囚徒》

```text
摄魂怪 → QX19 / dominant
活点地图 → QX16 / core
时间转换器 → QX15 / core
```

### 第四册｜《哈利·波特与火焰杯》

```text
火焰杯 → QX15 / dominant
三强争霸赛 → QX20 / dominant
小汉格顿墓地 → QX18 / core
```

### 第五册｜《哈利·波特与凤凰社》

```text
有求必应屋 → QX7 / core
血羽毛笔 → QX16 / core
预言球 → QX15 / core
```

### 第六册｜《哈利·波特与混血王子》

```text
混血王子的魔药课本 → QX16 / dominant
冥想盆 → QX15 / core
岩洞与黑湖 → QX6 / core
```

### 第七册｜《哈利·波特与死亡圣器》

```text
老魔杖 → QX15 / dominant
复活石 → QX15 / core
隐形衣 → QX14 / core
```

### 精度说明

本批没有建立“魔杖、猫头鹰、扫帚、魔药、画像”等一般性对象大全。对象必须在对应单册中承担稳定结构作用；跨七册高频出现本身不等于每册自动 PASS。

## 03｜《福尔摩斯探案全集》：完整阅读事实转为 60-unit reconciliation

个人既有阅读事实明确为完整读过《福尔摩斯探案全集》。标准 canon 为：

```text
4 novels + 56 short stories = 60 independent narrative units
```

因此该记录不再属于“是否读完整未知”，而属于：

```text
ONE_TO_MANY_RECONCILIATION
```

### 03.1｜中央阅读状态冲突

四部长篇原中央 Work 均被专题书单状态写成 `read_status = 未读`：

```text
血字的研究
四签名
巴斯克维尔的猎犬
恐怖谷
```

Batch030 已依据完整全集阅读事实统一校正为：

```text
read_status = 已读
series = 福尔摩斯探案全集
verification_status = 个人阅读事实校正
```

这证明专题书单中的“未读 / 阅读优先级”不能覆盖个人阅读记录。

### 03.2｜四部长篇 QX

#### 《血字的研究》

```text
墙上的血字 → QX16 / core
婚戒 → QX15 / core
毒药丸 → QX15 / core
```

#### 《四签名》

```text
阿格拉宝藏 → QX15 / dominant
四人签名 / 盟约纸条 → QX16 / core
泰晤士河 → QX3 / core
```

#### 《巴斯克维尔的猎犬》

```text
达特穆尔荒原 → QX6 / dominant
巴斯克维尔猎犬 → QX5 / dominant
巴斯克维尔庄园 → QX7 / core
```

#### 《恐怖谷》

```text
密码信 → QX16 / core
伯尔斯通庄园与护城河 → QX7 / dominant
恐怖谷 / 维尔米萨矿区 → QX8 / dominant
```

### 03.3｜剩余福尔摩斯任务

```text
CANON_TOTAL = 60
NOVELS_COMPLETE = 4
SHORT_STORIES_REMAINING = 56
```

短篇不能继承长篇意象，也不能把“贝克街、烟斗、放大镜”等系列标志物自动批量挂到所有篇章。后续必须：

```text
1. 建立 56-story canonical reading map
2. 复用已存在中央 Work
3. 将与全集阅读事实冲突的 read_status 校正为 已读
4. 缺失 Work 才补建
5. 每篇独立通过 Gate；允许 ZERO_QX
```

## 04｜《龙族》：全集已读，但版本边界仍不稳定

个人阅读事实明确为《龙族》全集已读；中央库当前只有：

```text
40 作品/龙族.md
read_status = 已读
review_note = 个人已读补录，来时路：网文
```

但“龙族全集”不能直接等价于固定单行本集合。原始出版、修订版、第三部上中下分册、第五部连载与后续重写 / 重启存在不同粒度边界。

因此本批只收口：

```text
READ_SCOPE = COMPLETE_SERIES_CONFIRMED
QX_ON_SERIES_PARENT = PROHIBITED
VOLUME_MAP = DEFER_VERSION_BOUNDARY
```

在版本 / 阅读时间对应关系明确前，不把 `龙族.md` 直接挂“卡塞尔学院、龙、尼伯龙根”等跨卷 QX，否则会重新制造系列层污染。

## 05｜Batch030 当前状态

```text
SERIES_RECORDS_TOTAL = 3
SERIES_FULL_READ_FACT_CONFIRMED = 3
SERIES_GRANULARITY_CLOSED = 1
SERIES_ONE_TO_MANY_IN_PROGRESS = 1
SERIES_VERSION_BOUNDARY_DEFERRED = 1

HARRY_POTTER = CLOSED
SHERLOCK_HOLMES = 4_OF_60_UNITS_QX_COMPLETE
DRAGON_RAJAS = DEFER_VERSION_BOUNDARY
```

## 06｜下一步

```text
Batch030-B
→ 福尔摩斯 56 short-story reading map + central Work reconciliation + story-level QX

Batch030-C
→ 龙族版本 / 卷级边界恢复

完成后再进入：
Batch031 = STORY-LEVEL READING MAP
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Corpus Coverage｜特殊项与上游缺口台账]]
- [[QX Formal Annotation｜增量批次029]]
