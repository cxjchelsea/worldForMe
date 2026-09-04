---
id: WL-QX-FORMAL-ANNOTATION-020
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次020
code: QX-ANNOTATION-020
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 解密
  - 今天也没变成玩偶呢
  - 群山回唱
  - 射雕英雄传
  - 皮囊
---

# QX Formal Annotation｜增量批次020

> 本批紧接 Batch 019 连续执行，审查 5 部已读单书。2 部形成正式 QX，3 部本轮判定 QX=0。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 / 结论 |
|---|---:|---|
| 《解密》 | 2 | 密码 / 密文；701秘密工作空间 |
| 《今天也没变成玩偶呢》 | 0 | 本轮无足够高置信对象通过 Gate |
| 《群山回唱》 | 0 | 多人物、多时空结构明显，但不把抽象“离散 / 亲缘回声”物象化 |
| 《射雕英雄传》 | 3 | 桃花岛；《九阴真经》；白雕 / 雕 |
| 《皮囊》 | 0 | 生命书写中的身体、故乡、亲人记忆不自动转为 QX object |

```text
BATCH_020_REVIEWED_WORKS = 5
BATCH_020_WORKS_WITH_FORMAL_QX = 2
BATCH_020_ZERO_QX_WORKS = 3
BATCH_020_FORMAL_RELATIONS = 5
FORMAL_QX_RELATIONS_BEFORE = 320
FORMAL_QX_RELATIONS_AFTER = 325
FORMAL_WORKS_WITH_QX_BEFORE = 101
FORMAL_WORKS_WITH_QX_AFTER = 103
```

## 02｜《解密》与《暗算》的同作者差异

《暗算》此前保留：

```text
无线电信号 / 电波
密码 / 密文
```

《解密》本批保留：

```text
密码 / 密文
701秘密工作空间
```

这说明同一作者、同一谍战 / 密码题材不应机械复制 object：

- `密码 / 密文` 具有真实跨作品复用潜力；
- `无线电信号` 与 `701秘密工作空间` 则是不同作品中的具体结构对象。

```text
SAME_AUTHOR ≠ SAME_QX_SET
```

## 03｜武侠作品的 QX 不等于“武功名词表”

《射雕英雄传》只保留：

```text
桃花岛
《九阴真经》
白雕 / 雕
```

没有批量录入：

```text
降龙十八掌
蛤蟆功
弹指神通
打狗棒法
全真剑法
```

因为招式 / 技能名称通常更接近能力系统，而不是稳定可感知物象。

《九阴真经》能够准入，是因为它首先是：

```text
可保存、抄录、阅读、争夺的文本对象
```

而非仅仅“武学概念”。

## 04｜标题仍然不能自动生成 QX

《皮囊》本轮 QX=0。

“皮囊”在标题和思想表达中具有高度身体意味，但若没有进一步确认它在全书作为具体可感知对象反复出现并承担结构功能，就不能把标题隐喻直接转为：

```yaml
object: 皮囊 / 身体
```

同理，《群山回唱》的“群山 / 回声”也不因标题本身而自动准入。

## 05｜网络文学的证据门槛不降低

《今天也没变成玩偶呢》本轮保持 QX=0，并不是否定类型文学的意象价值，而是当前批量审查阶段没有取得足够稳定、可定位、可区分的文本内部对象证据。

```text
UNFAMILIAR_WORK + LOW_CONFIDENCE
→ ZERO_QX_FOR_NOW
→ NOT INVENT OBJECTS
```

后续若获得更完整文本证据可重新审查。

## 06｜对象粒度候选

新增待 Full Corpus Audit 复核：

```text
密码 / 密文（暗算、解密）
701秘密工作空间 vs 裘庄 / 封闭别墅
桃花岛 vs 其他岛屿空间
武学秘笈文本 vs 一般书籍 / 手稿
白雕 / 雕 vs 动物伙伴
```

其中“桃花岛”再次加强了此前已经出现的岛屿空间 cluster 信号，但仍不在建设阶段强制 canonical normalization。

## 07｜连续循环累计

```text
Batch 019 = 7 reviewed / 9 relations
Batch 020 = 5 reviewed / 5 relations
CURRENT_CONTINUOUS_SEGMENT = 12 reviewed / 14 relations
```

当前正式状态：

```text
FORMAL_QX_RELATIONS = 325
FORMAL_WORKS_WITH_QX = 103
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
NEXT_BATCH = 021
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次019]]
