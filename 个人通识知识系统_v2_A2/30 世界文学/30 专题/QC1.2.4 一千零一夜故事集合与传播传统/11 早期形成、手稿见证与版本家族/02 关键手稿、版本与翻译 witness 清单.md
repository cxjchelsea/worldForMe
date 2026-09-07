---
topic_id: WL-TOPIC-QC124
structure_type_zh: 早期形成、手稿见证与版本家族
dimension: witness_registry
sequence: 11.2
resource_type: witness_registry
---
# 关键手稿、版本与翻译 witness 清单

> 本页维护第一轮关键 `collection_witness / translation_witness / source_layer`，不是中央作品书单。具体年代、卷数与家族判断在需要精读时继续核验。

| witness | 类型 | 主要作用 | 数据处理 |
|---|---|---|---|
| 早期阿拉伯语残片／早期文献提及 | early_witness | 证明集合名称与文本传统的早期生命 | witness 群，不伪装单一 work |
| 加朗所据叙利亚系阿拉伯语手稿 | collection_witness | 重要早期长篇手稿见证，显示一套并非后期“全集”的集合边界 | manuscript witness |
| 后期埃及 recension | collection_witness | 与早期叙利亚系形态不同的后期集合重组 | recension witness |
| 加朗法译 *Les Mille et Une Nuits* | translation_witness | 将集合带入欧洲大规模传播，并发生选择、调整和新增来源整合 | translation_layer |
| Hanna / Jean-Baptiste Diyab 故事来源层 | source_layer | 解释若干著名故事如何进入加朗传播体系 | oral/written source layer |
| Bulaq 等19世纪阿拉伯语印本 | edition_witness | 印刷时代对后期文本形态的固定与传播 | print witness |
| Calcutta 等19世纪阿拉伯语印本 | edition_witness | 另一重要印刷见证与编辑层 | print witness |
| 后续英、德、汉等世界语言译本 | translation_witness | 对加朗层、阿拉伯印本或其他底本继续选择和重组 | translation layer |

## membership 示例：阿拉丁与阿里巴巴

第一轮不使用：

```text
原始故事 / 假故事
```

而使用：

```text
在哪一层首次得到可证集合归属？
→ 通过什么 source_mode 进入？
→ 后来哪些版本继续收录？
```

例如可采用：

```yaml
story_membership:
membership_status: translation_added
source_mode: oral_source / translator_source_layer
attested_in: Galland tradition
```

这样既不把后来的全球经典性反推回早期阿拉伯语手稿，也不否定这些故事后来确实成为《一千零一夜》接受史的重要成员。

## 第一轮 witness 规则

- manuscript / recension / edition / translation 必须分型；
- 译本的底本来源能核验时单独记录；
- “某故事在某版本缺失”本身也是有价值的数据；
- 不因为现代选本收录某故事就自动标记 `core_attested`。