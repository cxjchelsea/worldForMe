---
id: WL-QC11-FINAL-ACCEPTANCE
type: literature_topic_governance
name: QC1.1 最终验收
status: PASS_WITH_TRACKED_COMPATIBILITY_DEBT
reviewed_topics:
  - QC1.1.1
  - QC1.1.2
---

# QC1.1｜传统型专题最终验收

## 1. 结论

```text
QC1.1_TAXONOMY = PASS
QC1.1_PRODUCT_SHELL = PASS
QC1.1_STRUCTURE_BASE = PASS
QC1.1_WORK_BASE = PASS
QC1.1_CANVAS = PASS
QC1.1_CANONICAL_WORK_ALIGNMENT = PASS_FOR_REFERENCE_CORE_SETS
QC1.1_SCOPED_METADATA = PASS
QC1.1_LOCAL_RELATION_ALIGNMENT = PASS_FOR_REFERENCE_CORE_SETS
QC1.1_RTM_PRODUCT_INTERFACE_ALIGNMENT = PASS
QC_TRADITION_TOPIC_TEMPLATE_V2 = FROZEN
```

QC1.1.1 与 QC1.1.2 已足够作为两种形成机制明显不同的 Reference Topics，用来冻结 QC 传统型专题的产品层标准。

## 2. 与 RTM 成熟专题的对照结果

### 产品外壳

两套 QC Reference Topics 均统一为：

```text
00 主页
01 Canvas
02 结构 Base
03 作品 Base
```

与 R/T/M 的使用界面一致。

### 结构 Base

已不再依赖 sequence 数字段划分一级知识模块，而按照：

```text
核心结构
内部文本与传统
母题与跨文化关系
后世传播与阅读
```

组织知识节点。

Base 现在优先读取 `structure_type_zh`；既有研究正文尚未全部补此字段时，以物理模块目录作为兼容 fallback，并提供“待模块元数据回填”视图。

该 fallback 不影响当前使用层验收，但以后新建 QC 专题不得把目录推导当成默认数据模型。

### 作品 Base

两套专题均直接查询中央 `40 作品` 的 `type: work` 实体，并使用各自 scoped metadata 作为专题归属与阅读组织依据。

视图已对齐成熟 RTM 的主要使用场景：

- ★ / ◆ / △
- 已读 / 未读
- 内部传统
- 传统阶段
- 专题角色
- T / M / G / Q 交叉视图
- 待校验

## 3. Reference Topic 1：QC1.1.1

核心 canonical works：

```text
创世记
出埃及记
申命记
撒母耳记
列王纪（希伯来圣经）
约伯记
诗篇
以赛亚书
```

Biblical Books of Kings 与菲尔多西 Shahnameh《列王纪》已经实体消歧，不共享 canonical work。

本地核心文本关系记录已连接中央作品；死海古卷、七十士译本等文本见证继续留在研究／关系层，不强行伪装为普通文学作品。

## 4. Reference Topic 2：QC1.1.2

核心 canonical works：

```text
伊利亚特
奥德赛
神谱
工作与时日
俄狄浦斯王
俄瑞斯忒亚
埃涅阿斯纪
奥维德《变形记》
```

奥维德《变形记》与其他同名作品使用中央作品身份消歧。

## 5. Canvas 验收

两套 Canvas 使用相同的稳定产品路径：

```text
主页
├─ 核心结构 → 母题与跨文化关系 → 阅读路线
└─ 内部文本与传统 → 作品 Base → 阅读路线
```

没有把结构相似、比较关系或候选传播画成确定历史传播边。

## 6. scoped metadata 词汇验收

V2 冻结四字段：

```text
<scope>_priority
<scope>_internal_tradition
<scope>_tradition_stage
<scope>_role
```

优先级词汇固定为：

```text
★ 核心
◆ 重点
△ 扩展
```

其余三个字段保留专题内部词汇自由，但职责固定，不允许互相替代。

## 7. 非阻塞兼容债务

当前仍允许以下 legacy 信息存在：

1. 既有研究正文中的 `WL-TOPIC-QT811 / QT812` 等 provenance；
2. 尚未迁移的 QT8.2 作为真实关系目标继续保留旧编号；
3. 两个 Reference Topics 的部分历史知识页尚未显式补 `structure_type_zh`，当前由目录 fallback 提供等价模块语义。

这些项目不会阻塞 QC1.1 产品层使用，也不应通过全局字符串替换处理。

## 8. 批量复用授权边界

```text
QC1.1.3_TO_QC1.1.11_SHELL_REUSE = AUTHORIZED
CONTENT_BLIND_COPY = NOT_AUTHORIZED
SCOPED_METADATA_BLIND_COPY = NOT_AUTHORIZED
CANONICAL_WORK_TITLE_ONLY_MATCH = NOT_AUTHORIZED
```

后续每个传统可以复用 V2 的产品壳、Base 结构与字段职责，但内部文本传统、核心作品、阶段、角色和跨文化关系必须按具体传统重新研究。

## 9. Final Status

```text
QC1.1_REFERENCE_LAYER = ACCEPTED
QC_TRADITION_TOPIC_TEMPLATE_V2 = FROZEN
NEXT_RECOMMENDED_SCOPE = QC1.1.3 日耳曼—北欧神话传统
QT8.2 / QT8.3 = STILL_OUT_OF_SCOPE
MAIN = UNCHANGED_UNTIL_PR17_MERGE
```
