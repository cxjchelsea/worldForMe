---
type: qc2_work_reference
component_id: WL-TOPIC-QC25-PROPHECY-AVOIDANCE-FULFILLMENT
component_type: plot_pattern
work: The Song of the Wise Oleg
work_role: later_reworking
retained_features:
  - 预言先行并改变人物行为
  - 行动者主动规避预言所指向的危险来源
  - 预言最终仍实现
modified_features:
  - 规避对象是坐骑而非被预言者
  - 最终通过马骨中的蛇完成预言
matched_slots:
  - authoritative_prediction
  - avoidance_action
  - predicted_outcome_fulfilled
missing_slots:
  - avoidance_backfire
added_slots:
  - delayed_return_to_avoided_object
relation_type: structural_similarity
evidence_level: documented
source_evidence:
  - https://en.wikipedia.org/wiki/Oleg_the_Wise
canonical_work: null
sequence: 302
status: active
---

# 普希金《贤明的奥列格之歌》｜structural_similarity

奥列格得知自己将因战马而死，于是将马送走；多年后得知马已死，前往查看遗骨，却被马骨中的蛇咬死，预言实现。

该实例特别重要，因为它支持：

```text
fulfilled_despite_avoidance
```

而不是严格的：

```text
fulfilled_through_avoidance
```

因此“规避行为直接造成实现”不能升级为 core slot。
