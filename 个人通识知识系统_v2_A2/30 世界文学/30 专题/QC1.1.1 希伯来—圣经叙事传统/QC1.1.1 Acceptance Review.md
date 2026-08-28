# QC1.1.1｜希伯来—圣经叙事传统 Retrofit Acceptance Review

> Review type: `QC_TOPIC_PRODUCT_SHELL_V2_RETROFIT`
>
> Historical baseline: former `QC1.1.1` research topic
>
> Current topic: `QC1.1.1`

---

## 1. Current acceptance result

```text
QC1.1.1_CONTENT_RESEARCH = PRESERVED
QC1.1.1_PRODUCT_SHELL = PASS
QC1.1.1_STRUCTURE_BASE = PASS
QC1.1.1_WORK_BASE = PASS
QC1.1.1_CANVAS = PASS
QC1.1.1_CANONICAL_WORK_ALIGNMENT = PASS_FOR_CORE_SET
QC1.1.1_LOCAL_RELATION_ALIGNMENT = PASS_FOR_CORE_SET
```

本次验收不推翻旧 QC1.1.1 的研究结论，而是确认其已经从“研究数据库专题”升级为可浏览、选书和比较的 QC 产品专题。

## 2. Product shell

当前稳定外壳：

```text
00 主页
01 Canvas
02 结构.base
03 作品.base
10 核心结构
11 内部文本与传统
12 母题与跨文化关系
13 后世传播与阅读
20 数据层
```

`02 结构.base` 使用语义模块，不再依赖 sequence 数字段切片；`03 作品.base` 直接查询中央 `40 作品` 的 `type: work` 实体，并以 `qc111_*` scoped metadata 组织。

## 3. Core canonical works aligned

已对齐：

- 《创世记》
- 《出埃及记》
- 《申命记》
- 《撒母耳记》
- 《列王纪》（Biblical Books of Kings，使用独立消歧 canonical work）
- 《约伯记》
- 《诗篇》
- 《以赛亚书》

中央库原 `列王纪.md` 为菲尔多西 *Shahnameh*，本专题不复用该实体；Biblical Books of Kings 使用 `列王纪（希伯来圣经）.md`。

## 4. Data-layer rule

`20 数据层/10 文本关系` 仅保存专题—文本关系与文本见证。核心作品关系已经通过 `canonical_work` 指向中央作品实体。

死海古卷、七十士译本等文本见证不因产品化而强制转为普通 `work`；它们继续作为文本史／传播证据对象维护。

## 5. Remaining work

以下属于增量研究，不阻塞当前产品层通过：

- 增加更多次级经卷与第二圣殿时期文本；
- 继续核证具体形成层次、版本差异与文本批判问题；
- 扩展后世犹太、基督教、伊斯兰接受中的具体作品；
- 等 QC1.2（原 QC2）迁移时再统一改写目标层编号。

## 6. Final status

```text
QC1.1.1 = PRODUCT_ACCEPTED_V2
QC1.1_TRADITION_TOPIC_MODEL = READY_FOR_REUSE_WITH_QC1.1.2
```
