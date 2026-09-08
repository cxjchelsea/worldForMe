---
id: WL-TOPIC-CN123-11-02
topic_id: WL-TOPIC-CN123
structure_type_zh: 早期亚瑟与编年史定型
dimension: textual_witness_registry
sequence: 2
resource_type: witness_registry
history_position: 登记关键文本与循环见证
---
# 关键文本与循环 witness 清单

> 本页记录亚瑟传统第一轮关键 textual / cycle witness。它不等于中央作品书单；只有适合独立作品管理的对象才进入 `40 作品`。

| witness | 大致阶段 | 语言／环境 | 角色 | 当前数据处理 |
|---|---|---|---|---|
| 早期威尔士亚瑟材料 | 早期层 | 威尔士／不列颠 | 亚瑟前编年史人物与英雄记忆 | 中央 work：《马比诺吉昂》（集合见证，非整本亚瑟） |
| Geoffrey of Monmouth, *Historia Regum Britanniae* | 12世纪 | 拉丁 | 连贯亚瑟王者传记关键定型 | 中央 work：《不列颠诸王史》 |
| Wace, *Roman de Brut* | 12世纪 | 古法语／盎格鲁—诺曼 | 编年史传统向俗语传播；圆桌传统的重要阶段 | 中央 work：《布鲁特传奇》 |
| Chrétien de Troyes 亚瑟 romances | 12世纪后期 | 古法语 | 骑士人物、宫廷爱情、圣杯材料扩张 | 已挂四部；《伊万》为《Yvain》复名，不重复计数 |
| *Erec et Enide* | 12世纪后期 | 古法语 | 克雷蒂安较早亚瑟 romance；婚姻与骑士身份 | 中央 work：《Erec et Enide》 |
| *Lancelot, le Chevalier de la Charrette* | 12世纪后期 | 古法语 | 兰斯洛特—桂妮维亚传统重要定型 | 中央 work：《兰斯洛特：大车骑士》 |
| *Yvain, le Chevalier au Lion* | 12世纪后期 | 古法语 | 骑士冒险与王廷评价空间 | 中央 work：《Yvain, the Knight of the Lion》 |
| *Perceval, le Conte du Graal* | 12世纪后期 | 古法语 | 圣杯故事传统关键起点之一 | 中央 work：《佩尔西瓦尔或圣杯故事》 |
| Robert de Boron 的 Grail / Merlin 材料 | 约12—13世纪之交 | 古法语 | 圣杯历史化、梅林与亚瑟时间连接 | witness / work group；库内暂无独立 work |
| Lancelot-Grail / Vulgate Cycle | 13世纪前期 | 古法语散文 | 亚瑟世界大型循环化；兰斯洛特、梅林、圣杯、王国终结整合 | `cycle_witness` |
| Post-Vulgate Cycle | 13世纪 | 古法语散文 | 对 Vulgate、Tristan 等材料的再组织；更强调亚瑟／圣杯整体结构 | `cycle_witness` |
| *Prose Tristan* | 13世纪 | 古法语散文 | 将强独立特里斯坦传统大量吸收到亚瑟王廷 | `subtradition_integration_witness` |
| Tristan–Iseult 独立故事传统 | 中古多文本 | 法语／德语等 | 被亚瑟世界吸收前的强独立故事 | 中央占位：《特里斯坦与伊瑟》；非 Béroul / Thomas 定本 |
| *Sir Gawain and the Green Knight* | 14世纪 | 中古英语 | 高文人物伦理与王廷荣誉 | 中央 work：《高文爵士与绿骑士》 |
| *The Alliterative Morte Arthure* | 14世纪 | 中古英语 | 英语前马洛礼：战争／王国终结 | 中央 work |
| *Stanzaic Morte Arthur* | 14世纪 | 中古英语 | 英语前马洛礼：兰斯洛特—桂妮维亚／王国终结 | 中央 work |
| Thomas Malory, *Le Morte Darthur* | 15世纪 | 中古英语 | 多源大型晚期集成 | 中央 work：《亚瑟王之死》 |
| T. H. White, *The Once and Future King* | 20世纪 | 英语 | 将 Arthur 重构为现代政治、教育与战争问题的人物模型 | 中央 work：现代再发明锚点 |

## 1. Vulgate Cycle：cycle_witness → component witness

Lancelot-Grail / Vulgate 不作为“一本大书”压平，而分两层记录：

```text
Lancelot-Grail / Vulgate Cycle
│
├─ L'Estoire del Saint Graal
│  → 圣杯前史与神圣谱系
│
├─ L'Estoire de Merlin
│  → 梅林、亚瑟早期王国与预言框架
│
├─ Lancelot Proper / Lancelot en prose
│  → 兰斯洛特人物生涯、桂妮维亚爱情与王廷骑士网络核心
│
├─ La Queste del Saint Graal
│  → 圣杯求索、加拉哈德与骑士伦理宗教化
│
└─ La Mort le roi Artu / Mort Artu
   → 王廷瓦解、兰斯洛特冲突与亚瑟王国终结
```

这五部分是 `component_witness`，共同挂在 `cycle_witness: Vulgate Cycle` 下。它们各自可以独立叙述，又在整体中承担不同人物／子传统功能。Cambridge 的概述同样将 Vulgate 视为五部散文 romance 组成的循环，并指出 *Lancelot Proper* 是其中心文本，其余部分围绕其前后扩展。 

### 当前建议字段

```yaml
witness_type: cycle_witness | component_witness | story_witness
parent_witness:
figure_focus: []
subtraditions: []
text_stage:
network_role:
```

此处先局部验证，不立即建立全局 witness 数据库。

## 2. 为什么 Vulgate 不能简单当成一部书

它由多个散文 romance 组成并逐步形成循环；各部分拥有相对独立生命，又共同构成跨世代的亚瑟世界。因此：

```text
Vulgate Cycle
≠ 单一 work
```

而更接近：

```text
cycle_witness
→ 多个 component_witness
```

这也是 `figure_tradition` 比 `narrative_cycle` 更需要多层文本容器的证据之一。

## 3. 为什么 Chrétien 不只是一位“亚瑟作者”

其作品的重要性在于推动亚瑟王廷从王者历史背景转变为骑士个人冒险、爱情和求索的共享叙事空间；兰斯洛特与圣杯相关材料后来获得远超单部 romance 的子传统生命。

## 4. 为什么 Prose Tristan 特别重要

它测试 `subtradition_integration`：一个原本拥有自身传统生命的故事如何被大型亚瑟散文世界吸收，却没有完全失去独立性。

## 5. 为什么 T. H. White 是现代锚点

*The Once and Future King* 不只是把马洛礼材料改写成现代小说，而是把 Arthur 的人物功能重新转向教育、权力、战争、理想制度及其失败。这正适合测试 `figure_tradition` 的一个必要能力：

```text
同一中心人物
→ 在不同历史语境中承担不同文化／政治问题
```

因此它进入中央 `40 作品`，并标记为 `modern_figure_reinvention`。

## 6. 后续中央 work 准入

不是本表所有条目都必须变成 `40 作品`。只有满足至少一项时才优先中央化：
- 作为独立可阅读作品进入实际阅读计划；
- 多个专题需要复用其作品事实；
- 需要独立维护作者、年代、语言、版本与阅读状态；
- 不中央化会造成重复书目信息。
