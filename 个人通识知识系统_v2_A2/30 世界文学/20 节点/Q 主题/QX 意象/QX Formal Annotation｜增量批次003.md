---
id: WL-QX-FORMAL-ANNOTATION-003
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次003
code: QX-ANNOTATION-003
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 活着
  - 傲慢与偏见
  - 了不起的盖茨比
  - 呼啸山庄
---

# QX Formal Annotation｜增量批次003

> 本批次继续在 `feat/qx-literary-imagery` 上执行正式标注，不同步或合并 `main`。
>
> 四部作品均为中央作品库中的已读 Work，继续按冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1` 执行：**不设数量配额，只录入通过质量门槛的对象。**

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《活着》 | 3 | 田地 / 土地；老牛 / 牛；赌桌 / 赌具 |
| 《傲慢与偏见》 | 3 | 舞会 / 舞厅；彭伯里庄园；书信 |
| 《了不起的盖茨比》 | 5 | 绿灯；灰谷；T. J. Eckleburg 的眼睛 / 广告牌；汽车；派对 / 宴会 |
| 《呼啸山庄》 | 5 | 呼啸山庄；画眉田庄；荒原 / moors；风 / 暴风；窗 / 窗户 |

```text
BATCH_003_WORKS = 4
BATCH_003_FORMAL_RELATIONS = 16
FORMAL_QX_RELATIONS_BEFORE = 69
FORMAL_QX_RELATIONS_AFTER = 85
FORMAL_WORKS_WITH_QX_BEFORE = 13
FORMAL_WORKS_WITH_QX_AFTER = 17
```

---

## 02｜本批验证的问题

本批刻意加入现实主义、婚恋 / 家庭叙事与现代社会小说，用于检验：

> QX 是否会天然偏向幻想、冒险、科幻或高象征密度作品？

结果是否定的。

现实主义与社会婚恋小说同样可以形成稳定 QX，只是对象分布明显不同：

```text
社会仪式
+ 宅邸与生活空间
+ 书信 / 媒介
+ 现代交通与公共景观
```

相较于幻想、冒险作品中的超自然对象、极端自然空间或奇异器物，这一类作品的 QX 更常嵌入日常社会基础设施。

---

## 03｜四部作品的主要结构信号

### 《活着》

三个对象分别落在：

- `田地 / 土地`：生存与劳作的现实空间；
- `老牛 / 牛`：晚年陪伴与生命状态映照；
- `赌桌 / 赌具`：人物身份与家庭命运的转折装置。

它说明现实主义作品的 QX 不必追求华丽象征；**日常物与生存空间本身就可以承担稳定结构功能。**

### 《傲慢与偏见》

核心关系形成：

```text
舞会 / 舞厅 → 公共关系与婚恋判断
彭伯里庄园 → 阶层空间与人物重新理解
书信 → 私人信息、误解校正与自我反省
```

因此这类婚恋小说的 QX 很大一部分不是爱情“象征物”，而是关系形成所依赖的社会装置。

### 《了不起的盖茨比》

本批中 QX 密度最高的作品之一，主要形成两类对象：

1. 高凝缩视觉对象：绿灯；广告牌眼睛；
2. 现代社会空间 / 装置：灰谷；汽车；派对。

这使个人欲望、阶层空间与现代性装置在同一作品内部可以通过 QX 关系并置，而不必把它们压缩成单一“美国梦象征”。

### 《呼啸山庄》

形成强烈空间网络：

```text
呼啸山庄
↔ 画眉田庄
↔ 荒原
↔ 窗户这一内外阈限
```

再由 `风 / 暴风` 持续强化环境状态。

这里最重要的不是单个对象分别“象征什么”，而是多个对象共同组织：

```text
封闭 / 开放
文明 / 野性
室内 / 荒原
生者 / 死者
```

---

## 04｜跨作品潜在结构簇

### A. 社交仪式—关系网络

- 《傲慢与偏见》：舞会 / 舞厅
- 《了不起的盖茨比》：派对 / 宴会

二者并非同一 normalized object，因此不强行归并；但它们在：

- `关系映射`
- `身份标识`
- `ritualized`

等关系属性上具有明显相似性。

### B. 宅邸空间—身份与关系重构

- 彭伯里庄园
- 呼啸山庄
- 画眉田庄

再与此前已有的大观园、梁宅、农舍等对象相连，可以观察不同作品如何借居住空间组织阶层、家族与人物关系。

这些对象仍应保持各自 object 身份，结构相似性由：

```text
primary_group
+ function
+ mode
+ 跨轴关系
```

计算，而不是通过粗暴 object 合并获得。

### C. 日常装置—命运转折

- 《活着》：赌桌 / 赌具
- 《了不起的盖茨比》：汽车
- 《傲慢与偏见》：书信

三者物性完全不同，却都通过 `情节转折 / transformative` 参与人物命运重排。

这再次证明未来作品相似度不能只计算 object 名称重合。

---

## 05｜Object Normalization 与专题激活检查

本批新增对象没有满足“至少 3 部可比较作品 + 至少两种稳定使用方式”的正式专题激活门槛。

需要保留但不提前激活的潜在聚类包括：

- 社交仪式：舞会、派对、宴会；
- 宅邸 / 居住空间：庄园、山庄、田庄、宅邸；
- 私人书写媒介：书信；
- 阈限装置：窗 / 窗户。

因此：

```text
NEW_QX_TOPIC_ACTIVATED = 0
QX3.1_STATUS = UNCHANGED
```

不因语义相近而把不同 object 强行归一。

---

## 06｜本批得到的建模结论

### 结论 1：QX 不依赖“象征主义式作品”

现实主义、婚恋与家庭小说同样能产生高质量 QX。

区别主要在对象来源：

```text
幻想 / 冒险作品
→ 异常对象、自然世界、旅行动线、奇异空间

现实主义 / 社会小说
→ 宅邸、仪式、书写、交通、劳动与生活空间
```

### 结论 2：文学意象可以是社会基础设施

QX 不应被狭义理解成“月亮、雨、花、镜子”式传统意象。

舞会、书信、庄园、汽车、工业荒地同样可以成为稳定的文学对象，只要它们通过 Admission Gate。

### 结论 3：结构相似比对象相同更重要

未来派生分析继续优先使用：

```text
object category
+ function
+ mode
+ relation structure
```

而不是：

```text
exact object overlap only
```

---

## 07｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 85
FORMAL_WORKS_WITH_QX = 17
QX3.1_ACTIVATION_WORKS = 4
NEW_TOPIC_THIS_BATCH = NONE
BATCH_003_STATUS = COMPLETE
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次002]]
- [[QX Object Normalization｜首批55条正式关系]]
- [[QX 文学意象与场景]]
