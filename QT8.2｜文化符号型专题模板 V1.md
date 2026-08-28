# QT8.2｜文化符号型专题模板 V1

> 对象类型：`symbol`
>
> 状态：`QT8.2_SYMBOL_TEMPLATE_V1_FROZEN`
>
> Reference Pilot：巴别塔。

## 00｜对象主页

```yaml
type: qt82_component
component_type: symbol
name: ""
primary_clusters: []
secondary_clusters: []
status: active
source_status: {}
admission_evidence: []
stable_meanings: []
meaning_shifts: []
```

主页首先回答：为什么它已经是文化 symbol，而不只是故事中的道具、地点或形象。

## 01｜定义、边界与 symbol 准入

必须证明：

- 超出单一情节功能；
- 在多个文本、时代或媒介中重复调用；
- 形成相对稳定、可识别的文化意义；
- 来源、关键定型与后世变体可追踪；
- 有可核证的 admission_evidence。

冻结边界：

```text
source object / place / image
≠ source-story function
≠ later cultural symbol
```

普通视觉相似不能替代来源／符号复用证据。

## 02｜来源物象与来源谱系

按 QT8.1 记录来源，统一使用 `qt82_source_reference` 与 source_status。

不得把后世成熟符号义反投射为最早文本唯一含义。

## 03｜符号化过程

至少追踪：

```text
来源对象／空间／意象
→ 重复接受与命名连续
→ 与意义关系绑定
→ 脱离单一情节仍可识别
→ 稳定意义族
→ 跨媒介复用
→ 可追踪语义漂移
```

冻结原则：

```text
visual stabilization ≠ source origin
semantic drift ≠ symbol continuity 必然断裂
symbol continuity ≠ literal object continuity ≠ visual-form continuity
```

## 04｜核心意义与语义漂移

必须区分 early_meaning / stable_meanings / later_meanings / contested_meanings / meaning_shifts。

`stable_meanings` 是整个 symbol network 中跨接受节点仍可识别的意义族，不要求每个后世实例全部覆盖。

## 05｜文本／视觉／仪式／媒介证据

证据可来自 textual / visual / ritual / material / media，但不同证据类型不得互相替代。

## 06｜传播、借用与符号复用

至少区分：

```text
explicit_reference
symbol_reuse
historical_transmission
structural_similarity
independent_or_unknown
```

冻结治理：

```text
same image ≠ same symbol automatically
visual similarity ≠ iconographic inheritance
symbol reuse ≠ historical transmission
```

`iconographic_inheritance` 不进入 V1 relation vocabulary；出现 documented visual chain 后才可 amendment review。

## 07｜与其他 QT8.2 对象关系

候选包括 represents_motif / associated_with_archetype / appears_in_plot_pattern / contrasts_with_symbol / transforms_into_symbol。

正式边遵守 meaningful target gate。

## 08｜后世重写与跨媒介复用

只收录能证明稳定符号义、语义漂移、明确反转或传播链的代表性实例，不做“出现同一物象即收录”的作品大全。

## 09｜作品实例

统一使用 `qt82_work_reference`，并允许 symbol-specific optional fields：

```yaml
symbolic_meaning: []
meaning_shift: []
evidence_medium: textual | visual | material | ritual | media
```

其中 evidence_medium 不替代 relation_type，也不自动证明历史传播。

## 10｜阅读与研究

至少包含来源物象路线、符号化关键节点、语义漂移、跨媒介路线与图像学／符号研究入口。

## 完成判定

- [ ] 已证明超出单一故事道具／地点／形象功能
- [ ] source object 与 later symbol 已分离
- [ ] admission_evidence / stable_meanings / meaning_shifts 已明确
- [ ] 至少具有跨文本／时代／媒介复用证据，或明确候选状态
- [ ] explicit_reference / symbol_reuse / ordinary similarity 已区分
- [ ] iconographic inheritance 未由视觉相似直接推出
- [ ] 后世实例具有明确 evidence_level

冻结结论：

```text
QT8.2_SYMBOL_TEMPLATE_V1 = FROZEN
```
