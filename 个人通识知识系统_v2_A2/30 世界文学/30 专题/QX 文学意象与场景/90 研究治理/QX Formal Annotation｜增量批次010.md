---
id: WL-QX-FORMAL-ANNOTATION-010
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次010
code: QX-ANNOTATION-010
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 堂吉诃德
  - 鲁滨逊漂流记
  - 格列佛游记
  - 第七天
---

# QX Formal Annotation｜增量批次010

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`，并保持“具体 object 优先、抽象主题不进入 QX、不同作品数量允许不均匀”的原则。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《堂吉诃德》 | 3 | 骑士小说与书籍；风车；理发师铜盆 / 曼布里诺头盔 |
| 《鲁滨逊漂流记》 | 4 | 海；荒岛；沙滩脚印；栅栏与堡垒住所 |
| 《格列佛游记》 | 4 | 小人国居民的微小身体；大人国居民的巨型身体；飞岛国拉普达；绳上舞蹈 |
| 《第七天》 | 2 | 殡仪馆与火化空间；死无葬身之地 |

```text
BATCH_010_WORKS = 4
BATCH_010_FORMAL_RELATIONS = 13
FORMAL_QX_RELATIONS_BEFORE = 159
FORMAL_QX_RELATIONS_AFTER = 172
FORMAL_WORKS_WITH_QX_BEFORE = 40
FORMAL_WORKS_WITH_QX_AFTER = 44
```

---

## 02｜《堂吉诃德》：抽象“骑士精神”不进入 QX

本批没有直接标注：

```text
骑士精神
理想主义
幻想与现实
```

这些属于 QT / QH / QC 层。

QX 保留的是其具体物质载体：

```text
骑士小说与书籍
风车
理发师铜盆 / 曼布里诺头盔
```

其中“骑士小说与书籍”尤其重要，因为作品把：

```text
阅读媒介
→ 命名
→ 身份重建
→ 行动规则
```

直接串成了叙事机制。

---

## 03｜QX3.1 文学中的海继续扩展

《鲁滨逊漂流记》的“海”正式复用：

```yaml
qx_id: QX3.1
object: 海
```

`QX3.1` 当前达到 6 部正式作品：

1. 《基督山伯爵》：跨越、逃亡与身份转换；
2. 《局外人》：身体经验与关系反差；
3. 《海底两万里》：世界本体与探索空间；
4. 《老人与海》：劳动、生存与搏斗空间；
5. 《少年Pi的奇幻漂流》：漂流世界、生存资源与持续威胁；
6. 《鲁滨逊漂流记》：冒险路径、海难与人生转折条件。

```text
QX3.1_ACTIVATION_WORKS = 6
```

---

## 04｜岛屿空间：强准聚类，但暂不激活

现有正式数据已经出现多个岛屿对象：

- 《基督山伯爵》：基督山岛；
- 《少年Pi的奇幻漂流》：食人岛；
- 《无人生还》：士兵岛；
- 《鲁滨逊漂流记》：荒岛。

它们的空间功能存在明显可比较性：

```text
藏宝 / 身份重构
生存诱惑 / 危险反转
封闭审判 / 隔离
生存劳动 / 自我组织
```

但当前 object 仍然是具体岛屿，而不是统一的“岛”。

因此暂时采用：

```text
ISLAND_CLUSTER = STRONG_CANDIDATE
ISLAND_OBJECT_NORMALIZATION = NOT_FORCED
NEW_QX_LEAF = NO
```

如果未来更多作品稳定出现岛屿，并且需要以“岛屿空间”作为跨作品比较层级，再评估是否建立一个对象级叶节点或派生结构。

---

## 05｜《格列佛游记》：身体尺度成为制度可视化机制

小人国与大人国没有被简单标成两个“奇幻国家”。本批重点保留的是身体尺度：

```text
微小身体
↔ 巨型身体
```

同一个格列佛在两种尺度环境中分别成为巨人和微小者，使：

```text
身体尺度
× 权力位置
× 日常感知
× 制度讽刺
```

直接发生联动。

“飞岛国拉普达”和“绳上舞蹈”则分别把技术权力与政治晋升转化为可见空间 / 公共仪式。

---

## 06｜《第七天》：死亡主题必须落到具体空间

本批只保留 2 条：

- 殡仪馆与火化空间；
- 死无葬身之地。

没有建立：

```text
死亡
亡灵
记忆
社会不公
```

等抽象 QX 对象。

因此它继续验证：

```text
DEATH_THEME → QH
DEATH_SPACE / MATERIAL DEATH INFRASTRUCTURE → QX
```

---

## 07｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 172
FORMAL_WORKS_WITH_QX = 44
ACTIVE_QX_LEAVES = 2
QX3.1_ACTIVATION_WORKS = 6
QX16.1_ACTIVATION_WORKS = 4
NEW_TOPIC_THIS_BATCH = NONE
STRONG_CANDIDATE_CLUSTER = ISLAND_SPACE
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次009]]
- [[QX3.1 文学中的海]]
- [[QX16.1 文学中的书信]]
