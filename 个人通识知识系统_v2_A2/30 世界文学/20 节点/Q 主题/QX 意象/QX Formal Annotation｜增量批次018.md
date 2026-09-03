---
id: WL-QX-FORMAL-ANNOTATION-018
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次018
code: QX-ANNOTATION-018
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 爱的教育
  - 暗算
  - 霸王别姬
  - 摆渡人
  - 悲伤逆流成河
  - 被嫌弃的松子的一生
  - 冰是睡着的水
  - 病隙碎笔
  - 沧浪之水
  - 朝花夕拾
---

# QX Formal Annotation｜增量批次018

> 本批继续“大批次 + 严格 Admission Gate”模式，审查 10 部中央作品库中明确 `read_status: 已读` 且此前未正式写入 QX 的作品。5 部形成正式关系，5 部本轮判定为 QX=0。

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 / 结论 |
|---|---:|---|
| 《爱的教育》 | 2 | 日记 / 日记本；书信 |
| 《暗算》 | 2 | 无线电信号 / 电波；密码 / 密文 |
| 《霸王别姬》 | 2 | 戏台 / 京剧舞台；戏服 / 戏妆 |
| 《摆渡人》 | 2 | 荒原；安全屋 |
| 《悲伤逆流成河》 | 0 | 本轮无对象通过 Admission Gate |
| 《被嫌弃的松子的一生》 | 0 | 本轮无对象通过 Admission Gate |
| 《冰是睡着的水》 | 0 | 标题意象不足以直接准入 |
| 《病隙碎笔》 | 0 | 疾病 / 生死主题不自动转写为 QX |
| 《沧浪之水》 | 0 | 标题典故 / 比喻不足以直接准入 |
| 《朝花夕拾》 | 3 | 百草园；三味书屋；《山海经》 |

```text
BATCH_018_REVIEWED_WORKS = 10
BATCH_018_WORKS_WITH_FORMAL_QX = 5
BATCH_018_ZERO_QX_WORKS = 5
BATCH_018_FORMAL_RELATIONS = 11
FORMAL_QX_RELATIONS_BEFORE = 300
FORMAL_QX_RELATIONS_AFTER = 311
FORMAL_WORKS_WITH_QX_BEFORE = 93
FORMAL_WORKS_WITH_QX_AFTER = 98
```

## 02｜标题意象不能绕过 Admission Gate

本批特别出现：

```text
冰是睡着的水
沧浪之水
悲伤逆流成河
```

这些书名本身具有高度意象性，但 QX 记录的是作品内部可定位、可感知、具有结构作用的对象，而不是标题修辞。

因此：

```text
TITLE_METAPHOR ≠ FORMAL_QX
```

除非正文中同一对象还能满足 recurrence / structural role / stable binding / distinctiveness，才允许进入正式关系。

## 03｜QX=0 比低质量补足更有价值

本批 5 部作品暂记为：

```text
ZERO_QX_FOR_NOW
```

它们不是“没有意象”，而是当前高置信候选不足以越过准入门槛。

### 《悲伤逆流成河》

校园、弄堂、河流等候选容易与青春叙事背景混淆，目前不把“悲伤”“河流”从标题直接物化。

### 《被嫌弃的松子的一生》

人物身体、住所和表情均有潜在候选，但在缺少稳定跨段落结构证据时不强行建立 canonical object。

### 《冰是睡着的水》

“冰 / 水”首先是标题性比喻；特情、武器、训练等又容易退化为类型背景，与 Batch 017 对《狼牙》的处理保持一致。

### 《病隙碎笔》

疾病、残疾、死亡、信仰等高度核心，但它们首先属于 QH；如果没有足够明确、反复、可感知的物象载体，就不从主题反推 QX。

### 《沧浪之水》

“沧浪之水”具有典故与价值判断意义，但目前不以标题典故代替正文中的正式对象证据。

## 04｜《爱的教育》：书写媒介就是叙事结构

本批正式写入：

```text
日记 / 日记本
书信
```

《爱的教育》以一个学年的日记推进叙事，并穿插父母等写给安利柯的书信。

这里的 QX16 并非因为“这是日记体小说”这一体裁判断，而是因为：

- 日记作为具体书写载体持续出现；
- 日期承担时间标记与结构分段；
- 书信作为可见文本稳定介入亲子关系与教育过程。

其中 `书信` 复用：

```text
qx_id: QX16.1
```

不新建 leaf。

## 05｜《暗算》：不可见信息被媒介化

本批保留：

```text
无线电信号 / 电波
密码 / 密文
```

二者都属于 QX16，但感知机制不同：

```text
电波 → auditory
密文 → visual
```

它们共同形成《暗算》中“秘密信息如何被感知、读取、破译”的物质层。

这里没有把抽象的“国家秘密”“天才”“神秘”标成 QX。

## 06｜《霸王别姬》：舞台与身体装扮

正式关系：

```text
戏台 / 京剧舞台
戏服 / 戏妆
```

两者共同构成作品最稳定的“台上 / 台下”边界：

- 舞台提供公共表演空间；
- 戏服与戏妆把角色身份落实到身体；
- 程蝶衣“人戏不分”的状态因此不是抽象主题，而有持续可见的物质载体。

暂不把“虞姬”“霸王”作为独立 QX object，因为它们首先是角色 / 戏中身份。

## 07｜《摆渡人》：阈限旅行空间

正式关系：

```text
荒原
安全屋
```

二者不是普通奇幻背景：

- 荒原决定灵魂必须如何移动；
- 安全屋反复切分旅程节奏；
- “赶路—避难—再出发”成为稳定的空间结构。

未来 Object Identity Review 可比较：

```text
荒原
荒岛
沙漠
废墟
边境地带
```

但本阶段不建立 object family。

## 08｜《朝花夕拾》：合集 Work 允许 singular_pivotal

《朝花夕拾》当前中央 Work 粒度是整部散文集，因此本批使用 `singular_pivotal` 保留三项高度辨识的具体物象：

```text
百草园
三味书屋
《山海经》
```

它们虽然主要集中在单篇内部，但均满足：

- 可明确定位；
- 不是普通背景；
- 对人物记忆 / 关系 / 结构有强作用；
- 在整部回忆性散文集中具有足够高的辨识度。

这不代表以后所有短篇集都可按同样方式直接标注。编辑型选集、多人合集以及作品粒度不稳定的 collection 仍继续延期。

## 09｜对象粒度待审计候选

本批新增：

```text
日记 / 日记本
书信
无线电信号 / 电波
密码 / 密文
戏台 / 京剧舞台
戏服 / 戏妆
荒原
安全屋
百草园
三味书屋
《山海经》
```

未来重点检查：

```text
日记 vs 手稿 / 笔记 / 文档
密码 / 密文 vs 书写文本
戏服 / 戏妆 vs 服饰 / 身体装饰
荒原 vs 其他阈限自然空间
百草园 / 三味书屋：专名空间是否保持 work-specific canonical object
《山海经》：具体书册 vs “书”object family
```

当前不提前合并。

## 10｜当前状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 311
FORMAL_WORKS_WITH_QX = 98
REVIEWED_WORKS_THIS_BATCH = 10
ZERO_QX_REVIEWED_WORKS_THIS_BATCH = 5
NEW_QX_LEAF = NO
TOPIC_DERIVED_DATA_REFRESH = DEFERRED
SHORT_STORY_COLLECTION_DEFERRED = ACTIVE
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
NEXT_BATCH = 019
```

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次017]]
- [[QX16.1 文学中的书信]]
