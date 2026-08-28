---
id: WL-QC11-FINAL-ACCEPTANCE
type: literature_topic_governance
name: QC1.1 最终验收
status: PASS_AFTER_V2_1_CONSISTENCY_FIX
reviewed_topics:
  - QC1.1.1
  - QC1.1.2
---

# QC1.1｜传统型专题最终验收 V2.1

## 1. 当前结论

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
QC_TRADITION_TOPIC_TEMPLATE_V2_1 = FROZEN
```

QC1.1.1 与 QC1.1.2 继续作为 QC 传统型专题的两个 Reference Topics，但 V2.1 已根据本地使用检查修正两个问题：Structure Base 接口不统一、作品池误把 8 部核心参考集当成专题全量。

## 2. 产品外壳

两套 Reference Topics 均统一为：

```text
00 主页
01 Canvas
02 结构 Base
03 作品 Base
```

内部模块统一为：

```text
10 核心结构
11 内部文本与传统
12 母题与跨文化关系
13 后世传播与阅读
20 数据层
```

## 3. Structure Base V2.1

当前两套结构 Base 已与成熟 R/T/M 接口对齐：

- 以当前 `topic_id` 过滤：`WL-TOPIC-QC111 / WL-TOPIC-QC112`；
- 直接按显式 `structure_type_zh` 分组；
- `dimension` 负责专题内部语义维度并映射为中文显示；
- `sequence / history_position / id` 保持与成熟专题一致的排序和说明职责。

QC1.1.1 与 QC1.1.2 的正式结构知识页均已回填当前 QC topic id 与 `structure_type_zh`。**目录 fallback 已从正式产品模型移除。**

历史正文中若出现 `WL-TOPIC-QT811 / QT812` 或 QT8.2 等内容性、来源性引用，可以继续作为 provenance 或尚未迁移目标保留；这与 frontmatter 的当前产品标识是两回事。

## 4. 作品池 V2.1

原 8 部作品保留为“核心参考骨架”，不再代表完整专题书目。

当前参考实现：

```text
QC1.1.1 希伯来—圣经叙事传统 = 20 部
QC1.1.2 希腊—罗马神话传统 = 20 部
```

每个专题均通过：

```text
★ 核心
◆ 重点
△ 扩展
```

组织完整阅读池。20 部是这两个 Reference Topics 的当前合理覆盖量，不是后续 QC 专题必须机械复制的数量。

### QC1.1.1 核心骨架

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

新增重点／扩展入口包括：

```text
利未记
民数记
约书亚记
士师记
耶利米书
以西结书
箴言
传道书
路得记
以斯帖记
但以理书
雅歌
```

### QC1.1.2 核心骨架

```text
伊利亚特
奥德赛
神谱
工作与时日
俄狄浦斯王
俄瑞斯忒亚
埃涅阿斯纪
变形记（奥维德）
```

新增重点／扩展入口包括：

```text
荷马颂歌
安提戈涅
美狄亚
酒神的女信徒
阿尔戈英雄纪
书库（伪阿波罗多洛斯）
被缚的普罗米修斯
七将攻忒拜
特洛伊妇女
岁时记（奥维德）
英雄书简
传说集（许癸努斯）
```

新建中央作品实体若书目元数据尚未完成统一核证，保留 `verification_status: 待核验`，不为了补数量伪造年代或原文题名。

## 5. Canvas 与关系层

两套 Canvas 保持稳定路径：

```text
主页
├─ 核心结构 → 母题与跨文化关系 → 阅读路线
└─ 内部文本与传统 → 作品 Base → 阅读路线
```

没有把结构相似、比较关系或候选传播画成确定历史传播边。

`20 数据层/10 文本关系` 继续承担 local relation / source witness 职责；抄本、译本和文本见证不强行转为普通作品实体。

## 6. scoped metadata

V2.1 继续冻结四字段：

```text
<scope>_priority
<scope>_internal_tradition
<scope>_tradition_stage
<scope>_role
```

优先级固定为 `★ / ◆ / △`，其余字段允许专题内部词汇不同，但语义职责固定。

## 7. 批量复用授权边界

```text
QC1.1.3_TO_QC1.1.11_SHELL_REUSE = AUTHORIZED
CONTENT_BLIND_COPY = NOT_AUTHORIZED
SCOPED_METADATA_BLIND_COPY = NOT_AUTHORIZED
CANONICAL_WORK_TITLE_ONLY_MATCH = NOT_AUTHORIZED
```

后续每个传统可以复用 V2.1 产品壳、Base 接口与字段职责，但核心文本、内部传统、阶段、角色和作品数量必须按具体传统重新研究。

## 8. Final Status

```text
QC1.1_REFERENCE_LAYER = ACCEPTED_V2_1
QC_TRADITION_TOPIC_TEMPLATE_V2_1 = FROZEN
NEXT_RECOMMENDED_SCOPE = QC1.1.3 日耳曼—北欧神话传统
QT8.2 / QT8.3 = STILL_OUT_OF_SCOPE
MAIN = UPDATED_AND_READY_FOR_LOCAL_REVIEW
```
