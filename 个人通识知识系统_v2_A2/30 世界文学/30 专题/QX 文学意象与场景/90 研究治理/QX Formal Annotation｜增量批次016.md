---
id: WL-QX-FORMAL-ANNOTATION-016
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次016
code: QX-ANNOTATION-016
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 钢铁是怎样炼成的
  - 金陵十三钗
  - 锌皮娃娃兵
  - 一百个人的十年
  - 一桩事先张扬的凶杀案
  - 银河系漫游指南
  - 离婚
  - 里斯本之夜
  - 两地书
  - 岛上书店
  - 达·芬奇密码
  - 河边的错误
---

# QX Formal Annotation｜增量批次016

> 本批继续“大批次 + 连续循环”模式。所有作品均由已读审计候选交叉确认当前中央 Work `read_status: 已读` 且原先无正式 `qx:` 后纳入。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《钢铁是怎样炼成的》 | 3 | 铁路 / 筑路工地；伤病身体；手稿 / 写作 |
| 《金陵十三钗》 | 3 | 教堂；地窖 / 地下室；旗袍 / 华丽衣饰 |
| 《锌皮娃娃兵》 | 3 | 锌皮棺材；口述声音；军装 / 制服 |
| 《一百个人的十年》 | 2 | 口述声音；照片 / 个人影像 |
| 《一桩事先张扬的凶杀案》 | 3 | 屠刀 / 杀猪刀；白色衣服 / 血迹；家门 / 前门 |
| 《银河系漫游指南》 | 3 | 电子指南；毛巾；黄金之心号 |
| 《离婚》 | 2 | 财政所办公室 / 衙门；隔壁房间 / 东屋 |
| 《里斯本之夜》 | 3 | 船票；里斯本港口 / 塔霍河夜岸；护照 / 假身份文件 |
| 《两地书》 | 1 | 书信 |
| 《岛上书店》 | 3 | 岛上书店；书籍 / 阅读；《帖木儿》珍本 / 稀有书 |
| 《达·芬奇密码》 | 3 | 密码筒；达·芬奇画作；卢浮宫 |
| 《河边的错误》 | 3 | 河 / 河边；柴刀；湿衣服 |

```text
BATCH_016_WORKS = 12
BATCH_016_FORMAL_RELATIONS = 32
FORMAL_QX_RELATIONS_BEFORE = 248
FORMAL_QX_RELATIONS_AFTER = 280
FORMAL_WORKS_WITH_QX_BEFORE = 73
FORMAL_WORKS_WITH_QX_AFTER = 85
```

## 02｜继续验证“稀疏标注合法”

《两地书》仅保留：

```yaml
qx_id: QX16.1
object: 书信
```

原因不是作品意象贫乏，而是其文本形式、关系结构和时间组织本身高度集中在书信这一 canonical object 上。

没有继续机械拆分：

```text
信纸
墨迹
邮票
信封
邮路
```

仅为增加数量而拆分会降低 object identity 的质量。

## 03｜标题词不自动进入 QX

《钢铁是怎样炼成的》没有把“钢铁”直接登记为 QX object。

本批正式保留的是：

```text
铁路 / 筑路工地
伤病身体
手稿 / 写作
```

“钢铁”更多承担标题层面的比喻和价值概括，而不是作品中可稳定定位、反复参与行动的单一物象。

```text
TITLE_METAPHOR ≠ AUTOMATIC_QX_OBJECT
```

## 04｜纪实文学继续出现“口述声音”对象

本批：

```text
锌皮娃娃兵 → 口述声音
一百个人的十年 → 口述声音
```

与此前：

```text
二手时间
切尔诺贝利的悲鸣
```

形成稳定跨作品候选簇。

但当前仍不执行：

```text
口述声音 canonical normalization audit
纪实文学媒介专题 activation
```

仅登记信号，等待 Full Corpus Audit。

## 05｜阈限 / 边界空间继续积累

本批出现：

```text
教堂
地窖
家门
里斯本港口
卢浮宫
河边
隔壁房间
```

其中“家门”尤其符合 singular pivotal：本应提供安全的家庭入口因误判被关闭，直接将圣地亚哥留在杀手面前。

这些空间虽然共享“边界 / 阈限”功能，但并非同一 object，不进行错误合并。

## 06｜媒介与知识对象密度上升

本批新增：

```text
手稿 / 写作
电子指南
书信
书籍 / 阅读
稀有书
达·芬奇画作
护照 / 假身份文件
```

说明 QX16 已形成较高密度，但目前仍按作品事实记录；不根据数量直接创建新的 QX16 子叶。

## 07｜明显元数据错误修正

《里斯本之夜》原文件存在：

```text
frontmatter author = 雷马克
正文基本信息作者 = 斯蒂芬·茨威格
```

本批统一修正为：

```text
作者 = 雷马克
```

这是确定性实体错误修正，不涉及轴结构或 schema 变更。

## 08｜对象粒度候选继续延期

新增 Full Corpus Audit 候选包括：

```text
伤病身体
教堂 vs 宗教建筑
地窖 / 地下室
旗袍 / 华丽衣饰
锌皮棺材 vs 铅棺 / 密封棺木
口述声音
照片 / 个人影像
白色衣服 / 血迹
家门 / 前门
电子指南
隔壁房间 / 东屋
港口 / 河岸
护照 / 身份文件
书籍 / 阅读
稀有书
密码筒
艺术图像
河 / 河边
柴刀 / 屠刀
湿衣服
```

特别注意：

```text
锌皮棺材 ≠ 自动合并 铅棺
柴刀 ≠ 自动合并 屠刀
```

它们功能可能相近，但 object identity 尚未完成审计。

## 09｜累计状态

从大批次模式开始：

```text
Batch 014 = 7 works / 21 relations
Batch 015 = 10 works / 27 relations
Batch 016 = 12 works / 32 relations
```

累计：

```text
CONTINUOUS_LOOP_WORKS = 29
CONTINUOUS_LOOP_RELATIONS = 80
```

全局当前：

```text
FORMAL_WORKS_WITH_QX = 85
FORMAL_QX_RELATIONS = 280
```

## 10｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 280
FORMAL_WORKS_WITH_QX = 85
NEW_QX_LEAF = NO
TOPIC_DERIVED_DATA_REFRESH = DEFERRED
SHORT_STORY_COLLECTION_DEFERRED = 夜晚的潜水艇
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
NEXT_BATCH = 017
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次015]]
- [[QX16.1 文学中的书信]]
