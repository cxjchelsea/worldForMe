---
id: WL-QC124-PROVENANCE-TEST-V1
type: literature_review
scope: QC1.2.4
resource_type: provenance_test
status: PASS
version: "1.0"
---
# QC1.2.4 Provenance Test V1

> 目的：验证 `translation_layer / editorial_recomposition / source_mode / collection_witness` 是否足以服务一次现实阅读，而不只停留在抽象模板层。

## 1. 实测阅读版本

选择：

**Husain Haddawy, *The Arabian Nights***（1990；后续 Norton / Everyman 重印）。

选择原因：

1. 它是现实中可以直接购买、借阅、阅读的现代英文译本；
2. 译本明确基于 Muhsin Mahdi 校订的14世纪叙利亚手稿文本；
3. 它没有为了满足现代读者对“经典《一千零一夜》”的期待，把《阿拉丁》《阿里巴巴》等 Galland 层著名故事重新塞回核心正文；
4. 因而 provenance 路径非常清楚，适合做第一个模板验证样本。

## 2. provenance 路径

```text
Haddawy 现代英文译本
        ↓ translated_from
Muhsin Mahdi critical edition
        ↓ edited_from
14世纪叙利亚系 Arabic manuscript witness
        ↓ belongs_to
早期 Syrian manuscript family / recension
        ↓
QC1.2.4 collection_tradition
```

这条链中每一层对象不同：

```text
translation_witness
≠ critical_edition
≠ manuscript_witness
≠ manuscript_family
≠ collection_tradition
```

## 3. 需要记录的数据

### translation_witness

```yaml
name: Husain Haddawy, The Arabian Nights
witness_type: translation_witness
language: English
translation_layer: modern_scholarly_translation
source_mode: direct_translation_from_critical_edition
editorial_recomposition: low / source-bounded
```

### critical edition

```yaml
editor: Muhsin Mahdi
witness_type: critical_edition
base_witness: fourteenth-century Syrian manuscript tradition
role: reconstruct / edit early Syrian text witness
```

### manuscript layer

```yaml
witness_type: manuscript_witness
manuscript_family: Syrian
collection_boundary: incomplete / non-vulgate / early-core form
```

这里的 `incomplete` 不是“残缺所以不够好”的价值判断，而是描述它没有后期埃及印本那种追求1001夜完整化的集合边界。

## 4. membership selection 实测

Haddawy 译本目录明确包含：

- 山鲁佐德框架；
- 商人与魔鬼；
- 渔夫与魔鬼；
- 脚夫与三个女人；
- 三个苹果；
- 驼背故事；
- Nur al-Din / Shams al-Nahar；
- Anis al-Jalis；
- Jullanar of the Sea 等。

同时不以 Galland 后来整合的《阿拉丁》《阿里巴巴》作为该核心手稿译本的正文成员。

因此现代阅读时可以明确解释：

> 你读 Haddawy 时，并不是在读“缺少了阿拉丁的残缺版《一千零一夜》”，而是在读一个有明确早期叙利亚手稿 provenance 的现代译本；《阿拉丁》《阿里巴巴》属于另一条重要的 Galland / Diyab 传播成员路径。

这正是 `collection_tradition` 应为实际阅读提供的解释能力。

## 5. 与 Galland 路径的对照

```text
Galland 法译
├─ manuscript translation
├─ separate Sinbad material integration
├─ Diyab oral/written source layer
│   ├─ Aladdin
│   └─ Ali Baba 等
└─ literary adaptation / editorial recomposition
```

所以两个“《一千零一夜》”现代入口可能拥有不同 provenance：

```text
Haddawy
→ Mahdi
→ Syrian manuscript

Galland-derived edition
→ Galland translation / adaptation
→ Syrian manuscript + other manuscript materials + Diyab source layer
```

它们不是“一个正确、一个错误”，而是**不同 collection witness / translation lineage**。

## 6. 实测后的字段判断

以下字段全部有现实用途：

```text
collection_witness        PASS
manuscript_family         PASS
recension                 PASS
translation_layer         PASS
source_mode               PASS
editorial_recomposition   PASS
story_membership          PASS
membership_status         PASS
```

同时证明还应保留：

```text
base_witness / translated_from / edited_from
```

但这三个可以作为关系类型，不必膨胀成新的顶级语义层。

## 7. 判定

```text
Reading-version provenance test = PASS
```

当前模型已经能够回答真实阅读问题：

- 我手中的版本从哪里来？
- 它为什么收这些故事而不收另一些？
- 一个著名故事为什么在另一个版本里没有？
- 这种差异来自手稿家族、后期 recension，还是翻译／编辑层？

因此 PATCH B 已关闭。