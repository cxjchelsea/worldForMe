---
id: WL-QC1.2.4
type: literature_node
name: 一千零一夜故事集合与传播传统
code: QC1.2.4
axis: Q
system_role: work_knowledge_network
parent: WL-QC1.2
level: 5
coverage_priority: Core
node_kind: taxonomy_leaf
anchorable: true
resource_type: collection_tradition
status: ACTIVE
build_stage: stage_frozen
---
# QC1.2.4 一千零一夜故事集合与传播传统

QC1.2 的第一个 `collection_tradition` 冻结样板。

本专题研究的不是“一千零一夜故事全集”，而是：

> **一个开放、流动、跨语言、跨地域、持续增补的故事集合，如何通过框架叙事、抄本传统、翻译、印刷与现代接受形成可追踪的传播传统？**

## 核心模型

```text
frame narrative
      ↓
story collection
      ↓
manuscript witnesses
      ↓
regional / linguistic recensions
      ↓
translation and print circulation
      ↓
modern canonization and reinvention
```

## 已冻结的 collection_tradition 能力

```text
frame_narrative
collection_boundary
story_membership
manuscript_witness
recension
translation_witness
print_witness
provenance_status
modern_collection_reinvention
```

## 与 narrative_cycle / figure_tradition 的差异

QC1.2.1、QC1.2.2 主要通过故事循环与版本分支组织；QC1.2.3 通过中心人物与人物网络组织；QC1.2.4 证明：

- 集合边界可以开放且历史上持续变化；
- 单篇故事进入集合的时间与路径可能不同；
- 版本关系不能简单压缩为单一“原本”；
- 翻译与出版可能反向塑造后世认知中的“经典全集”；
- provenance 必须与 story membership 分开管理。

## 当前中央证据层

```text
框架故事传统
→ 阿拉伯语抄本见证
→ 埃及／叙利亚等版本系统
→ Galland 法译
→ 欧洲语言转译与印刷
→ 19—20 世纪全集化与经典化
```

## 当前核心关注

1. 山鲁佐德框架叙事作为集合结构；
2. 不同阿拉伯语抄本与版本系统；
3. Galland 翻译及其新增故事的来源问题；
4. 阿拉丁、阿里巴巴等故事的传播身份；
5. 欧洲东方主义语境中的接受与再造；
6. 现代“标准全集”观念如何形成。

## Membership 与 Provenance 分离

```text
story_membership:
  core_witnessed
  later_attested
  translation_added
  modern_canonical

provenance_status:
  manuscript_attested
  oral_source_reported
  translator_mediated
  uncertain
```

同一故事可以在现代版本中高度 canonical，但其早期阿拉伯语抄本 provenance 仍不同。

## 方法约束

- 不把现代全集目录倒投射为中世纪固定文本；
- 不因故事广为人知就假定其属于最早层；
- 不用单一民族／语言所有权解释跨区域传播；
- 不使用“原始／伪作”二分取代 provenance。

## 已完成验证

- Source Readiness：PASS
- Topic Build：PASS
- Coverage Review：PASS
- Membership Matrix：PASS
- Real-edition Provenance Test：PASS
- Stage Freeze：PASS

专题主页：[[../../../30 专题/QC1.2.4 一千零一夜故事集合与传播传统/00 一千零一夜故事集合与传播传统|QC1.2.4 专题主页]]
冻结模板：[[QC1.2 collection_tradition 专题模板 V1]]

## 当前状态

`STAGE_FROZEN`

除非真实阅读暴露新版本无法解释、关键证据修正或第二 collection_tradition 样板迫使模板升级，否则停止横向扩充本专题。
