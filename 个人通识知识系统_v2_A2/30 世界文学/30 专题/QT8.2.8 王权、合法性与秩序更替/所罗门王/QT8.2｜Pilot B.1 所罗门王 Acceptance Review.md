# QT8.2｜Pilot B.1 所罗门王 Acceptance Review

> Review target: `WL-TOPIC-QT828-SOLOMON`
>
> Object type: `archetype / named_archetype`
>
> Template: [[QT8.2｜文化原型型专题模板 V0]]
>
> Shared governance: [[QT8.2｜共享数据层规范 V0]]

---

# 1. Acceptance conclusion

```text
QT8.2_PILOT_B1_CONTENT_ACCEPTANCE = PASS
QT8.2_PILOT_B1_NAMED_ARCHETYPE_BOUNDARY = PASS
QT8.2_PILOT_B1_IDENTITY_ANCHOR_MODEL = PASS
QT8.2_PILOT_B1_CORE_FUNCTION_MODEL = PASS_AFTER_REVISION
QT8.2_PILOT_B1_SOURCE_GOVERNANCE = PASS
QT8.2_PILOT_B1_RELATION_GOVERNANCE = PASS_AFTER_FIGURE_REWRITING_ADD
QT8.2_PILOT_B1_WORK_REFERENCE_ACCEPTANCE = PASS
QT8.2_PILOT_B1_COMPONENT_RELATION_GATE = PASS_BY_DEFERRED_GATE
QT8.2_PILOT_B1_REFERENCE_STATUS = ACCEPTED_REFERENCE_NAMED_ARCHETYPE_V0

QT8.2_ARCHETYPE_TEMPLATE_ABSTRACT_VALIDATION = PASS
QT8.2_ARCHETYPE_TEMPLATE_NAMED_VALIDATION = PASS
QT8.2_ARCHETYPE_TEMPLATE_V0 = VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
QT8.2_TEMPLATE_V1_FREEZE = NOT_AUTHORIZED
```

所罗门王可以作为 QT8.2 第一个正式 `named_archetype` Reference Topic。当前不需要继续增加案例来证明其准入。

---

# 2. Named archetype boundary

本 Pilot 已稳定区分：

```text
QT8.1 source figure Solomon
≠
QT8.2 named archetype Solomon
```

来源人物负责《列王纪》等来源文本中的具体王者形象；QT8.2 负责长期接受史中仍被识别为 Solomon / Sulayman、但功能和故事不断被重写的文化人物模型。

准入不是因为“所罗门很有名”，而是因为当前已有可追踪的：

```text
身份连续
+
稳定角色功能
+
跨时代／跨传统重写
+
结构化 work-reference 证据
```

因此对象边界通过。

---

# 3. Identity anchor model

Pass A 的单层 `identity_anchor` 经 Pass B 后拆为：

```text
required_identity_anchors
+
supporting_identity_anchors
```

当前所罗门：

```text
required
- Solomon / Sulayman 命名身份连续
- 大卫王族／以色列王者身份连续

supporting
- 智慧声望
```

这一拆分解决了 named archetype 特有问题：

> 角色功能可以显著变化，但仍需回答“为什么这还是同一个命名人物”。

同时避免把“智慧”这种其他匿名智慧王也可能具有的功能误写成纯身份同一性。

结论：

```text
QT8.2_IDENTITY_ANCHOR_MODEL = ACCEPTED_FOR_NAMED_ARCHETYPE_V0
```

---

# 4. Core functions / variable features

Pass A 中的：

```text
builder_and_centralizer
```

被正确识别为来源层偏置，并在 Pass B 降级为：

```text
temple_builder_and_centralizer
→ variable_feature
```

当前 core functions 收束为：

```text
wise_king_and_judge
divinely_authorized_kingship
extraordinary_knowledge_authority
```

这一修订证明：

```text
source-figure defining feature
≠ named-archetype cross-reception core function
```

所以 `core_functions / variable_features` 模型不仅可以复用到 named archetype，而且能阻止来源人物百科直接复制成原型字段。

状态：PASS_AFTER_REVISION。

---

# 5. Source governance

正式来源仍只有 QT8.1.1 中《列王纪》的所罗门：

```text
source_status = reference_topic
```

这是合理的单来源 named-archetype 结构：named archetype 不要求多个文明各自拥有一个独立“来源人物”，而是要求同一来源人物在后续接受中形成长期重写链。

Jewish / Christian / Islamic / esoteric materials 因此进入后世接受／重写层，而不是被伪装成多个独立 source figures。

状态：PASS。

---

# 6. `figure_rewriting` relation validation

Pilot B.1 已证明原共享词汇存在真实缺口：

```text
character_or_name_borrowing
```

不足以表示“同一命名人物保持身份连续，但人物功能与故事系统被系统性重构”；而：

```text
direct_adaptation
```

又要求更强的来源故事／文本整体改编关系。

因此新增：

```text
figure_rewriting
```

边界固定为：

```text
character_or_name_borrowing
= 主要借人物／名字

figure_rewriting
= 同一可识别人物持续存在，但角色功能／故事系统被系统重写

direct_adaptation
= 以某一来源故事／文本为主要整体改编对象
```

真实记录已形成：

```text
Testament of Solomon
→ figure_rewriting / documented

Quranic Sulayman traditions
→ figure_rewriting / documented

Josephus, Antiquities 8.42–49
→ explicit_reference / documented

Key of Solomon
→ character_or_name_borrowing / documented
```

状态：PASS_AFTER_FIGURE_REWRITING_ADD。

---

# 7. Shared Data Layer

当前已验证：

```text
1 × qt82_source_reference
4 × qt82_work_reference
```

并继续遵守：

```text
one relation record
= one relation_type
+ one evidence_level
```

`qt82_component_relation` 仍未创建，因为“智慧王”“神授王”“魔法王”“相关 symbol”等相邻对象尚未通过自己的 QT8.2 准入。

这不是数据层失败，而是 promotion / target gate 正常工作：

```text
candidate relation
≠ formal component relation
```

状态：PASS_BY_DEFERRED_GATE。

---

# 8. Archetype template checklist

按当前文化原型型模板检查：

| 条件 | 结果 |
|---|---|
| abstract / named 类型确定 | PASS |
| source figure 与 archetype 分层 | PASS |
| core_functions 明确 | PASS |
| variable_features 明确 | PASS |
| archetype 与 theme / trait / plot 未混淆 | PASS |
| 来源状态明确 | PASS |
| qt82_source_reference 已建立 | PASS |
| 原型化过程存在证据链 | PASS |
| 非因“著名”而准入 | PASS |
| required_identity_anchors 已建立 | PASS |
| supporting anchors / core / variable 已区分 | PASS |
| borrowing / figure_rewriting / direct_adaptation 已区分 | PASS |
| 相邻 QT8.2 对象关系已识别 | PASS_WITH_CANDIDATE_GATE |
| functional similarity / historical transmission 治理未被破坏 | PASS |
| relation record 原子性 | PASS |
| 后世实例能解释 identity / core / variable 漂移 | PASS |

结论：基础完成条件全部满足；正式跨类型 component relation 延迟属于允许状态。

---

# 9. Non-blocking observations

## 9.1 `work` 字段可在 V1 Freeze 前再评估是否泛化

当前 `qt82_work_reference.work` 中存在：

```text
Quranic Sulayman traditions
Key of Solomon tradition
```

它们并不总是严格意义上的“单一作品”。V0 当前仍可容纳，因为 schema 职责本来包含后世作品或跨媒介实例；但在 V1 Freeze Review 前可考虑是否增加：

```text
reference_scope: work | text_cluster | corpus | tradition | media_instance
```

或将展示语义泛化为 `work_or_instance`。

这是非阻塞观察，不要求现在改 schema。

## 9.2 历史文件名保留旧 relation 名称

`Testament-of-Solomon-name-borrowing.md` 与 `Quran-Sulayman-name-borrowing.md` 为兼容已有 Obsidian 链接暂不重命名；frontmatter `relation_type` 已是数据真值。

状态：兼容性可接受，不阻塞验收。

---

# 10. Template-level conclusion

所罗门 Pilot 证明 archetype 模板需要同时支持两种不同生成机制：

```text
abstract_archetype
多个来源实例
→ 抽取共同 role-function bundle
→ abstract cultural model

named_archetype
一个来源人物
→ required identity continuity
→ stable core functions
→ reception-specific feature drift
→ figure rewriting
→ named cultural model
```

因此：

```text
QT8.2_ARCHETYPE_TEMPLATE_V0
= VALIDATED_BY_ABSTRACT_AND_NAMED_ARCHETYPE
```

但整个 QT8.2 Template V0 仍不能冻结为 V1，因为：

```text
Pilot C plot_pattern = NOT_YET
Pilot D symbol = NOT_YET
```

下一阶段应进入：

```text
QT8.2_PILOT_C
= 预言 → 逃避 → 实现
```

而不是继续扩充 archetype Pilot。