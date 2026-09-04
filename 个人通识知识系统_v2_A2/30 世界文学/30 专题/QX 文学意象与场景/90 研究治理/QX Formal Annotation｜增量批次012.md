---
id: WL-QX-FORMAL-ANNOTATION-012
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次012
code: QX-ANNOTATION-012
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 白鹿原
  - 恶时辰
  - 二手时间
  - 芳华
---

# QX Formal Annotation｜增量批次012

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。执行策略保持不变：优先推进全部已读作品的 formal annotation；只修明显错误，不在建设阶段提前进行 object ontology 重构；纪实作品同样允许极少量关系，不能为了数量把抽象主题物象化。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《白鹿原》 | 3 | 白鹿；白鹿祠堂；白鹿原 / 土地 |
| 《恶时辰》 | 2 | 匿名帖 / 匿名纸条；雨 |
| 《二手时间》 | 2 | 厨房；口述声音 |
| 《芳华》 | 3 | 红楼 / 文工团练功空间；军装 / 演出服；刘峰失去的右臂 / 义肢 |

```text
BATCH_012_WORKS = 4
BATCH_012_FORMAL_RELATIONS = 10
FORMAL_QX_RELATIONS_BEFORE = 181
FORMAL_QX_RELATIONS_AFTER = 191
FORMAL_WORKS_WITH_QX_BEFORE = 48
FORMAL_WORKS_WITH_QX_AFTER = 52
```

---

## 02｜《白鹿原》：把“民族秘史”落实到动物、制度空间与土地

本批没有直接标注：

```text
宗法制度
传统文化
家族命运
历史变迁
```

这些仍属于 QH / M / T 等解释层。

QX 保留三个互不替代的可感知层级：

```text
白鹿
白鹿祠堂
白鹿原 / 土地
```

它们分别承担：

```text
白鹿
→ 地方传说、吉瑞世界状态、结构性预示

白鹿祠堂
→ 宗族身份、礼仪、惩戒与权力的固定空间

白鹿原 / 土地
→ 家族行动、生产生活与长期历史变化的物质场域
```

这里没有把三者合并成抽象的“传统文化意象”。同一作品可以同时存在动物、建筑和自然 / 农业空间三个 QX 对象，只要每一条都独立通过 Admission Gate。

---

## 03｜《恶时辰》：匿名帖是事件发动机，雨是持续世界条件

本批只保留：

```text
匿名帖 / 匿名纸条
雨
```

没有为了增加关系数而正式标注：

```text
死牛
老鼠
牙痛
吊床
普通门窗
```

这些虽然具有感官辨识度，但当前不足以证明都稳定承担核心结构功能。

“匿名帖”通过 Gate 的原因最明确：

- 持续出现；
- 暴露私人秘密；
- 触发杀人、猜疑和社会冲突；
- 推动镇长的控制与镇上秩序变化；
- 是作品最具辨识度的物质叙事装置之一。

“雨”则不是“压抑 = 雨”的象征词典式解释，而是长期改变街道、房屋、行动和小镇感官状态的天气条件。

```text
ANONYMOUS_POSTERS = DOMINANT_QX
RAIN = MATERIAL_WORLD_CONDITION
SYMBOL_DICTIONARY = REJECTED
```

---

## 04｜《二手时间》：纪实文学不需要强行制造大量物象

本批仅保留 2 条：

```text
厨房
口述声音
```

没有直接标注：

```text
苏联
社会主义
记忆
历史
自由
怀旧
创伤
```

这些都是主题、制度或解释层概念，而不是 QX object。

“厨房”之所以进入 QX，是因为作品反复把普通人的政治讨论、私人记忆和关系交流放在苏联家庭的狭小厨房里，使厨房从生活背景成为一种稳定的见证空间。

“口述声音”之所以进入 QX，则是因为全书不是先有抽象“集体记忆”再找例子，而是通过大量彼此差异甚至矛盾的第一人称声音来组成文本本身：

```text
不同人的声音
→ 并置
→ 冲突
→ 复调结构
→ 历史经验可听见化
```

因此：

```text
DOCUMENTARY_WORK_QX_COUNT_CAN_BE_LOW = TRUE
ORAL_VOICE_AS_FORMAL_MEDIUM = KEEP
ABSTRACT_MEMORY = DROP_FROM_QX
```

---

## 05｜《芳华》：青春集体与战争后果通过身体和空间变得可见

正式保留：

```text
红楼 / 文工团练功空间
军装 / 演出服
刘峰失去的右臂 / 义肢
```

三条关系分别覆盖：

### A. 集体空间

红楼、练功房及相关集体生活空间把：

```text
训练
演出
议论
亲密关系
集体评价
纪律处分
```

压缩在同一文工团共同体中。

### B. 身份外观

军装与演出服同时承担军人身份和舞台化青春形象，两者使个人身体持续处于集体可见性之中。

### C. 身体断裂

刘峰失去的右臂及其后使用的义肢，把战争后果固定在人物身体上。尤其重要的是，这只右臂在此前曾反复参与做饭、维修、缝补和帮助战友等劳动，因此“能干的手臂”与“战后缺失 / 义肢”形成强烈前后回声。

```text
YOUTH_AS_ABSTRACT_THEME = QH
MILITARY_COLLECTIVE_SPACE = QX
UNIFORMED_BODY = QX
WAR-DAMAGED_BODY = QX
```

---

## 06｜对象粒度：继续延后治理

本批出现新的后续审计候选：

```text
白鹿原 / 土地
白鹿祠堂 vs 一般祠堂
匿名帖 / 匿名纸条
口述声音 vs 声音 / 口吻
红楼 / 文工团练功空间
失去的右臂 / 义肢 vs 身体 / 肢体
```

当前不做 canonical object 强制归一。

原因仍然是：

```text
完整 corpus 尚未建成
→ 当前优先保留作品内部最有解释力的对象粒度
→ 等全部已读作品完成后统一做 Object Identity Review
```

因此：

```text
OBJECT_ONTOLOGY_REFACTOR = DEFERRED
SCHEMA_MIGRATION = NO
CURRENT_SCHEMA = QX_RELATION_SCHEMA_V1
```

---

## 07｜已有对象复用与专题检查

《恶时辰》的“雨”复用现有对象页：

```yaml
qx_id: QX1.1
object: 雨
```

但本批不因单个新增实例重写 `QX1.1` 的专题总结，也不在建设阶段做全量派生数据同步；专题实例统计留待 Full Corpus Audit / aggregation 阶段统一生成。

其余对象暂未触发新的稳定 canonical object 叶专题。

```text
NEW_FORMAL_QX_LEAF = NO
TOPIC_DERIVED_DATA_REFRESH = DEFERRED
```

---

## 08｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 191
FORMAL_WORKS_WITH_QX = 52
BATCH_012_FORMAL_RELATIONS = 10
NEW_TOPIC_THIS_BATCH = NONE
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次011]]
- [[QX1.1 文学中的雨]]
- [[QX3.1 文学中的海]]
- [[QX16.1 文学中的书信]]
