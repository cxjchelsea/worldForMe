---
id: WL-QX-FORMAL-ANNOTATION-004
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次004
code: QX-ANNOTATION-004
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 挪威的森林
  - 许三观卖血记
  - 一个陌生女人的来信
  - 献给阿尔吉侬的花束
---

# QX Formal Annotation｜增量批次004

> 本批次继续在 `feat/qx-literary-imagery` 上执行正式标注，不同步或合并 `main`。
>
> 四部作品均为中央作品库中的已读 Work，继续执行 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《挪威的森林》 | 4 | 《Norwegian Wood》/ 音乐；草地中的井 / 暗井；萤火虫；山中疗养院 |
| 《许三观卖血记》 | 3 | 血；炒猪肝与黄酒；水 / 卖血前喝水 |
| 《一个陌生女人的来信》 | 2 | 来信 / 书信；白玫瑰 / 生日花束 |
| 《献给阿尔吉侬的花束》 | 4 | 进步报告 / 书写记录；迷宫 / 实验迷宫；阿尔吉侬 / 实验鼠；花 / 献花 |

```text
BATCH_004_WORKS = 4
BATCH_004_FORMAL_RELATIONS = 13
FORMAL_QX_RELATIONS_BEFORE = 85
FORMAL_QX_RELATIONS_AFTER = 98
FORMAL_WORKS_WITH_QX_BEFORE = 17
FORMAL_WORKS_WITH_QX_AFTER = 21
```

---

## 02｜本批扩展出的对象类型

本批验证了四种此前相对较少的 QX 来源：

```text
声音 / 音乐媒介
身体液体与身体资源
私人书写
实验装置与非人实验对象
```

这说明 QX 不能被收窄为视觉性的“文学意象”。只要对象具有可感知性、稳定文学功能和文本证据，声音媒介、程序性饮食、书写记录与实验空间同样可以进入关系模型。

---

## 03｜关键跨作品信号

### A. 书信 / 私人书写

- 《傲慢与偏见》：书信用于暴露信息、纠正误解与重构人物判断；
- 《一个陌生女人的来信》：书信承载一个长期未被识别者的生命叙述，使单向关系在死后才被接收；
- 《献给阿尔吉侬的花束》：进步报告不是普通通信，而是主体认知变化本身的可见记录。

三者表明：

> **“书写媒介”是一个高价值结构簇，但当前 normalized object 仍不同，不提前创建同一叶节点。**

未来可以通过 `QX16 + function + mode` 发现其相似性。

### B. 身体资源与生存机制

《许三观卖血记》的：

```text
血
→ 卖血前喝水
→ 卖血后炒猪肝 + 黄酒
```

形成一条非常完整的身体—交易—补偿仪式链。

这里不需要把“血”解释成固定象征。它首先是：

- 身体物质；
- 可交换资源；
- 家庭危机中的行动条件；
- 重复出现的结构装置。

### C. 非人对象与人物边界

《献给阿尔吉侬的花束》中的阿尔吉侬被正式录入 QX5，并不意味着“所有重要动物角色都算意象”。

它通过 Gate 的原因在于：

- 它与查理处于同一实验机制；
- 其能力变化具有稳定比较功能；
- 其衰退和死亡直接形成命运预示；
- 其文学作用高度依赖“实验鼠这一非人对象”的物质身份。

这与《动物农场》中以完整社会角色运作的猪、马等仍有明确区别。

---

## 04｜《挪威的森林》对媒介边界的验证

`《Norwegian Wood》/ 音乐` 被纳入 QX16，是本批一个重要边界扩展。

原因不是歌曲“象征”某种情绪，而是：

```text
声音出现
→ 触发记忆
→ 打开整部回忆叙事
→ 在人物关系中反复回响
```

因此 QX 的“可感知对象”应包括：

- 视觉对象；
- 听觉对象 / 声音媒介；
- 气味等其他感官对象（仍需继续积累）；
- 具有空间、物质或媒介承载形式的对象。

这也继续回应此前《第一炉香》“香气”暴露出的感官分类问题：**暂时仍不需要新增 QX21；感官性可以先由 object + primary_group + function 承载。**

---

## 05｜Object Normalization 与专题激活检查

本批出现若干值得继续观察的候选簇：

- `书信 / 私人书写`：当前至少《傲慢与偏见》《一个陌生女人的来信》形成强对照，另有进步报告作为邻近媒介对象；
- `血`：与此前《百年孤独》中的血形成第二个可比较实例；
- `花`：白玫瑰、红楼梦中的花 / 落花、阿尔吉侬墓前献花具有关系，但 manifestation 和文学功能差异较大；
- `动物—非人对应者`：老牛、阿尔吉侬、大鱼等可由 QX5 进行功能层比较，但不能合并 object。

目前仍没有一个新增 normalized object 稳定满足正式叶节点激活条件。

```text
NEW_QX_TOPIC_ACTIVATED = 0
QX3.1_STATUS = UNCHANGED
```

---

## 06｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 98
FORMAL_WORKS_WITH_QX = 21
QX3.1_ACTIVATION_WORKS = 4
NEW_TOPIC_THIS_BATCH = NONE
BATCH_004_STATUS = COMPLETE
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次003]]
- [[QX Object Normalization｜首批55条正式关系]]
- [[QX 文学意象与场景]]
