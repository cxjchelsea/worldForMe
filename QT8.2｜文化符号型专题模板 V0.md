# QT8.2｜文化符号型专题模板 V0

> 对象类型：`symbol`
>
> 状态：`V0_REVISED_AFTER_BABEL_PILOT_PASS_B`
>
> 前置治理：[[QT8.2｜世界文化母题、原型与叙事结构模板总则 V0]] + [[QT8.2｜共享数据层规范 V0]]

---

# 00｜对象主页

建议 frontmatter：

```yaml
type: qt82_component
component_type: symbol
name: ""
primary_clusters: []
secondary_clusters: []
status: PILOT
source_status: {}
admission_evidence: []
stable_meanings: []
meaning_shifts: []
```

主页首先回答：

1. 这个对象为什么已经是 symbol，而不只是故事道具／地点／形象？
2. 它最早／较早出现在哪些来源传统与文本，各自 `source_status` 是什么？
3. 它获得稳定文化意义的关键节点是什么？
4. 哪些证据组成 `admission_evidence`？
5. 有哪些 `stable_meanings` 与 `meaning_shifts`？
6. 它和哪些 motif / archetype / plot_pattern 稳定关联？
7. 后世如何跨文本、时代与媒介持续复用？

---

# 01｜定义、边界与 symbol 准入

必须通过以下准入：

- 超出单一情节功能；
- 在多个文本、版本、时代或媒介中重复调用；
- 形成相对稳定、可识别的文化意义；
- 可以追踪来源、关键定型与后世变体；
- 至少能给出一组可核证的 `admission_evidence`。

若只满足“故事里出现过”，保持为 source object，不进入 QT8.2 symbol。

必须区分：

```text
source object / place / image
≠ source-story function
≠ later cultural symbol
```

Pilot D 巴别塔进一步固定：

> ordinary visual similarity 不能替代来源／符号复用证据；一座“很像巴别塔”的高塔不自动进入 Babel symbol network。

---

# 02｜来源物象与来源谱系

按 QT8.1 记录来源，并继承共享 `source_status`：

```text
reference_topic
reference_topic_source_story_pending_index
external_source_pending_qt81_topic
external_source_verified_text_only
unknown_source_status
```

至少观察：

- source_tradition
- source_story
- source_object / source_place / source_image
- source_figure（若适用）
- early_textual_witness
- early_visual_or_ritual_witness（若适用）

来源数据使用共享 `qt82_source_reference`。

不要把后世已经成熟的符号义反投射到最早文本。

---

# 03｜符号化过程

这是 symbol 专题的核心。

至少追踪：

```text
来源对象／空间／意象
→ 重复接受与命名连续
→ 与特定意义关系绑定
→ 脱离单一情节仍可识别
→ 获得稳定意义族
→ 跨媒介复用
→ 发生可追踪的语义漂移
```

Pilot D 强调：

```text
visual stabilization
≠ source origin

semantic drift
≠ symbol continuity 必然断裂

symbol continuity
≠ literal object continuity
≠ visual-form continuity
```

巴别塔案例中，Bruegel 可作为视觉定型／再传播节点，但不能把其具体塔形倒写成《创世记》的来源物象；Borges 证明 literal tower 消失后，Babel 仍可通过名称与意义场保持符号连续；Iñárritu《Babel》(2006) 进一步证明在电影媒介中，即使建筑物象与建塔情节均消失，Babel 仍可通过明确命名与语言／沟通断裂意义族继续被识别。

---

# 04｜核心意义与语义漂移

不要写成“这个符号代表 X”单一答案。

建议分层：

```text
early_meaning
stable_meanings
later_meanings
inverted_meanings
contested_meanings
meaning_shifts
```

其中：

```text
stable_meanings
= 跨多个接受节点仍可识别的意义族
= 不要求每个后世实例同时承载全部 stable_meanings

meaning_shifts
= 某一接受节点对意义重心的新增、替换、抽象化或反转
```

不同意义必须尽量标记时代、文本／媒介与证据，不把后世解释倒灌为来源唯一含义。

---

# 05｜文本／视觉／仪式／媒介证据

symbol 的证据不限文学文本，可分层记录：

- textual_witness
- visual_witness
- ritual_use
- material_culture
- later_media_reuse

不同证据类型不得互相替代。

若某类证据尚未核证，不为了填模板而强行补充。

---

# 06｜传播、借用与符号复用

至少区分：

```text
explicit_reference
symbol_reuse
historical_transmission
structural_similarity
independent_or_unknown
```

治理：

```text
相同物象
≠ 同一文化符号

图像相似
≠ iconographic inheritance

symbol reuse
≠ historical transmission
```

Pilot D Pass B 后，`iconographic_inheritance` **不进入当前共享 relation vocabulary**。原因不是该关系不可能存在，而是现阶段没有一条经独立证据核实、足以要求共享 schema 支持的具体视觉继承链。未来若出现作者／制作资料、图像学研究或可追踪传播证据，再单独提交 vocabulary review。

---

# 07｜与其他 QT8.2 对象关系

至少记录候选：

- `represents_motif`
- `associated_with_archetype`
- `appears_in_plot_pattern`
- `contrasts_with_symbol`
- `transforms_into_symbol`

正式关系使用共享 `qt82_component_relation`，只有 target 已完成自身准入且关系有实际解释价值时才创建。

```text
candidate relation
≠ formal component relation
```

---

# 08｜后世重写与跨媒介复用

重点追踪：

- 文学；
- 戏剧；
- 绘画／雕塑；
- 建筑；
- 电影／电视剧；
- 漫画／动画；
- 游戏；
- 政治／公共修辞（若确有稳定使用）。

只记录能证明稳定符号义、语义漂移或明确反转的代表性实例，不做“出现该物象即收录”的作品大全。

---

# 09｜作品实例

使用共享 `qt82_work_reference`。

通用字段继续使用：

```yaml
work: ...
component_id: ...
retained_features: []
modified_features: []
relation_type: ...
evidence_level: ...
source_evidence: []
```

Pilot D Pass B 后，symbol 类型正式允许以下可选 work fields：

```yaml
symbolic_meaning: []
meaning_shift: []
evidence_medium: textual | visual | material | ritual | media
```

使用规则：

```text
symbolic_meaning
= 当前实例实际承载的 stable meaning 子集

meaning_shift
= 当前实例新增／替换／抽象化／重新加权的意义

evidence_medium
= 媒介分类，不替代 relation_type
```

这三个字段已由 Bruegel（visual）、Borges（textual）与 Iñárritu《Babel》(2006)（media）完成跨媒介压力测试，因此从 candidate 升级为 symbol-specific optional extension。

若同一作品构成两种不同关系，仍遵守 relation atomicity，建立两条 work reference。

---

# 10｜阅读与研究

至少提供：

- 来源物象路线；
- 符号化关键节点路线；
- 语义漂移路线；
- 跨媒介路线；
- 图像学／符号研究入口；
- KEEP / REVISE / ADD / REMOVE 模板反馈。

---

# 文化符号型完成判定

- [ ] 已证明超出单一故事道具／地点／形象功能
- [ ] source object 与 later symbol 已分离
- [ ] `admission_evidence` 已明确
- [ ] `stable_meanings / meaning_shifts` 已明确
- [ ] 符号化过程可追踪
- [ ] 至少两次跨文本／时代／媒介复用证据，或明确候选状态
- [ ] 来源具有 `source_status`
- [ ] 来源已进入 `qt82_source_reference`
- [ ] 后世代表实例已进入 `qt82_work_reference`
- [ ] 核心意义与 contested / later meanings 已区分
- [ ] 至少识别一个 motif / archetype / plot_pattern 关系；target 未准入时允许保持 candidate
- [ ] `explicit_reference / symbol_reuse / ordinary similarity` 已区分
- [ ] iconographic inheritance 未由视觉相似直接推出
- [ ] relation record 遵守原子性
- [ ] 后世实例具有明确 evidence_level
