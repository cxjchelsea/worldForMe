---
id: WL-QC124-SOURCE-READINESS
scope: QC1.2.4
type: literature_review
resource_type: collection_tradition
status: PASS_READY_FOR_ADMISSION
version: "1.0"
---
# QC1.2.4 一千零一夜故事集合与传播传统 Source Readiness Review

## 结论

`PASS_READY_FOR_ADMISSION`

《一千零一夜》适合成为 QC1.2 第一个 `collection_tradition` 正式样板。它的研究价值不在于故事数量，而在于：**同一集合在不同手稿、版本、印本与翻译中具有不同故事成员，却仍维持可识别的集合身份。**

---

# 1. 准入六项检查

| 条件 | 判断 | 说明 |
|---|---|---|
| 可识别边界 | PASS | 有稳定名称、框架叙事与长期集合身份，但成员边界可变 |
| 跨时期 | PASS | 早期材料、阿拉伯语手稿、近代印本、欧洲翻译与现代版本构成长时段生命 |
| 多文本／多见证 | PASS | 不存在单一手稿承担全部传统，多个手稿、recension、印本与译本共同构成见证网络 |
| 可研究谱系 | PASS | 可研究手稿家族、版本重组、故事增删、翻译来源与印本传播 |
| 跨语言／地域 | PASS | 阿拉伯语传统进入法语及其他世界语言，并形成强烈再生产 |
| 复用价值 | PASS | 可解释《阿拉丁》《阿里巴巴》等故事的集合归属问题，以及世界文学中的翻译／编纂机制 |

结论：`6 / 6 PASS`。

---

# 2. 最低历史链

```text
印度—波斯—阿拉伯等多层早期叙事资源与集合前史
↓
阿拉伯语《一千零一夜》早期形成与手稿传统
↓
不同 manuscript family / recension 的集合边界分化
↓
加朗所据叙利亚系手稿与法语翻译
↓
迪亚布等来源带入新的故事层
↓
后期埃及 recension 与阿拉伯语印本
↓
欧洲及全球翻译、选编与重新编辑
↓
现代学术版／通俗版继续重新定义“哪些故事属于《一千零一夜》”
```

这是一条**见证—版本—翻译—编辑史**，不是一个单一作者原稿逐本复制的线性谱系。

---

# 3. 为什么不能按普通 work 处理

《一千零一夜》的传统对象与具体版本必须分层：

```text
collection_tradition
≠
collection_witness / manuscript / recension / edition
≠
translation
≠
story_witness
≠
individual story_tradition
```

如果把整个传统压成一个 `work`，会直接丢失本专题最重要的信息：**故事成员在哪个版本出现、在哪个版本缺失，以及它通过什么来源进入集合。**

---

# 4. 第一轮必须建模的能力

```yaml
collection_boundary:
frame_narrative:
collection_witness:
manuscript_family:
recension:
story_membership:
membership_status:
addition_removal:
translation_layer:
editorial_recomposition:
source_mode:
```

其中 `membership_status` 第一轮建议：

```text
core_attested
branch_attested
translation_added
later_print_added
uncertain
```

这些状态描述**见证层级**，而不是用“真／假”“原版／伪作”替代复杂传播史。

---

# 5. 框架叙事的特殊作用

山鲁佐德—国王框架不是普通“第一篇故事”。它在集合传统中承担组织机制：

- 为不断嵌入故事提供叙事容器；
- 帮助不同成员规模的版本仍被识别为同一传统；
- 允许嵌套叙事与故事套故事结构持续扩展。

因此 `frame_narrative` 应作为 `collection_tradition` 的独立能力，而不是普通 story_membership 项。

---

# 6. Source readiness 风险

后续建设必须持续避免：

1. 把某一现代中文版目录当作整个传统目录；
2. 把加朗法译中的成员自动投射回全部阿拉伯手稿；
3. 把后期埃及印本当作唯一“标准原本”；
4. 仅凭故事地域风格推断其属于早期集合；
5. 把口述采集、译者重写、编辑增补与手稿直接见证混为一类。

---

# 7. 建设判定

```text
boundary_check        PASS
source_readiness      PASS
admission             PASS
resource_type         collection_tradition
next_stage            topic_build
```

正式编号：`QC1.2.4`。