---
id: WL-QX-FORMAL-ANNOTATION-013
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次013
code: QX-ANNOTATION-013
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 平凡的世界
  - 骆驼祥子
  - 雷雨
  - 茶馆
---

# QX Formal Annotation｜增量批次013

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。只处理中央作品库中明确 `read_status: 已读` 且尚无正式 QX 的作品；不以作品知名度替代 Admission Gate，不因经典段落广为人知就自动拆出关系。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《平凡的世界》 | 2 | 黄土高原 / 双水村；煤矿井下 |
| 《骆驼祥子》 | 2 | 人力车；骆驼 |
| 《雷雨》 | 2 | 雷雨；周公馆 |
| 《茶馆》 | 3 | 裕泰茶馆；“莫谈国事”纸条 / 告示；纸钱 |

```text
BATCH_013_WORKS = 4
BATCH_013_FORMAL_RELATIONS = 9
FORMAL_QX_RELATIONS_BEFORE = 191
FORMAL_QX_RELATIONS_AFTER = 200
FORMAL_WORKS_WITH_QX_BEFORE = 52
FORMAL_WORKS_WITH_QX_AFTER = 56
```

---

## 02｜《平凡的世界》：劳动经验首先被空间组织

正式保留：

```text
黄土高原 / 双水村
煤矿井下
```

没有直接标注：

```text
贫困
奋斗
劳动
城乡差距
改革时代
```

这些属于 QH / T 等解释层。

本作两个 QX 对象构成明显的空间迁移：

```text
黄土高原 / 双水村
→ 家庭、农业、土地与乡村关系

煤矿井下
→ 工业劳动、工人身份、身体风险与城市生存
```

二者都不是单纯背景。双水村长期绑定孙、田两家人的生活与社会变化；煤矿则在少平进入矿区后成为稳定、反复而高度身体化的劳动环境。

本批暂不把它们进一步抽象为：

```text
乡村空间
工业空间
劳动空间
```

这些属于后续 pattern / constellation 层，而不是当前 object 层。

---

## 03｜《骆驼祥子》：物件与动物共同构成人物身份

本批只保留：

```text
人力车
骆驼
```

### 人力车

它是全作最稳定的物质关系之一：

```text
劳动工具
→ 独立生活目标
→ 买车 / 丢车 / 再积累
→ 人物命运结构
```

因此其功能不应简化为“象征希望”。首先成立的是它对行动、劳动身份和情节结构的直接组织作用。

### 骆驼

三匹骆驼本身并非高频反复出现，但通过 `singular_pivotal` 例外进入正式 QX：

```text
车被抢
→ 逃离兵营
→ 得到骆驼
→ 卖掉换钱
→ 获得“骆驼祥子”称呼
```

一次物质事件由此转化为人物长期身份标记。

### 为什么暂不标“烈日 / 暴雨”

烈日与暴雨段落具有极高文学辨识度，也高度身体化，但本批不因其著名就机械拆成两个对象。它们保留为后续 Full Corpus Audit 的候选：届时可统一判断“单一强场景天气”与 QX1 的关系边界。

```text
SUN_HEAT_AND_STORM = AUDIT_CANDIDATE
FORMAL_RELATION_THIS_BATCH = NO
```

---

## 04｜《雷雨》：天气不是标题标签，而是舞台时间结构

正式保留：

```text
雷雨
周公馆
```

“雷雨”通过 Admission Gate 的原因不是作品恰好以此命名，而是剧本持续积累：

```text
闷热
→ 将雨
→ 雷声 / 闪电
→ 风暴
→ 终局悲剧
```

天气贯穿同一日的舞台时间，并与冲突升级同步，因此属于稳定的感官与结构装置。

“周公馆”则将：

```text
家长权力
家庭秘密
阶级关系
旧日关系
人物进入与退出
```

集中在一个封闭住宅空间中。

本批没有继续把：

```text
窗
灯
电线
家具
```

拆成独立 QX。即便终局中某些物件参与关键事件，也不代表它们都具有独立跨作品比较价值。

---

## 05｜《茶馆》：一个空间跨三幕老去

正式保留：

```text
裕泰茶馆
“莫谈国事”纸条 / 告示
纸钱
```

### 裕泰茶馆

茶馆是本作最核心的空间结构：

```text
清末
→ 军阀时期
→ 抗战胜利后
```

同一空间跨时代持续存在，而陈设、顾客、经营方式与生存状态不断改变，因此空间本身承担时间标记和世界状态功能。

### “莫谈国事”告示

这不是普通文字背景。它持续规定茶馆中的言说边界，同时又与外部政治不断侵入茶馆形成反讽：

```text
文字要求“不谈国事”
↔
国事不断进入所有人的生活
```

因此它同时属于媒介对象与权力空间标记。

### 纸钱

终幕三位老人撒纸钱祭奠自己，是典型 `singular_pivotal + ritualized`：

```text
活人
→ 为自己举行祭奠
→ 个体一生失败
→ 茶馆时代终结
```

这里 QX 保留的是纸钱及其具体仪式动作，而“旧时代死亡”本身仍属于解释层。

---

## 06｜本批出现的空间类型差异

本批出现四类具有较强功能差异的空间对象：

```text
黄土高原 / 双水村
煤矿井下
周公馆
裕泰茶馆
```

它们暂时不能因为都属于“空间”而归一：

| 对象 | 当前主要机制 |
|---|---|
| 黄土高原 / 双水村 | 土地、家庭、生产、城乡距离 |
| 煤矿井下 | 工业劳动、身体风险、身份转换 |
| 周公馆 | 家庭权力、秘密暴露、封闭关系 |
| 裕泰茶馆 | 公共社会切片、时代变化、多人汇聚 |

这组差异进一步说明：

```text
SAME_QX_GROUP ≠ SAME_OBJECT
SAME_OBJECT_FAMILY ≠ SAME_LITERARY_FUNCTION
```

后续可在 function / pattern 层比较，但建设阶段不改 object ontology。

---

## 07｜对象粒度与专题检查

本批新增后续审计候选：

```text
黄土高原 / 双水村：自然空间 + 聚落是否需拆分
煤矿井下：煤矿 vs 井下
人力车：交通工具 / 劳动工具双重属性
骆驼：动物实例与人物称号的绑定
雷雨：复合天气 object 是否保持整体
周公馆：专名建筑 vs 宅邸 family
裕泰茶馆：专名公共空间 vs 茶馆 family
“莫谈国事”纸条 / 告示：文字内容 vs 媒介载体
纸钱：器物还是仪式物
```

当前全部延后至 Full Corpus Audit。

本批也没有触发新的正式 QX 叶专题：

```text
NEW_FORMAL_QX_LEAF = NO
OBJECT_ONTOLOGY_REFACTOR = DEFERRED
TOPIC_DERIVED_DATA_REFRESH = DEFERRED
```

---

## 08｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 200
FORMAL_WORKS_WITH_QX = 56
BATCH_013_FORMAL_RELATIONS = 9
ACTIVE_QX_LEAVES = 2
NEW_TOPIC_THIS_BATCH = NONE
FULL_CORPUS_AUDIT = DEFERRED_UNTIL_ANNOTATION_COMPLETION
```

当前 QX corpus 首次达到：

```text
200 formal Work —[HAS_IMAGERY]→ QX relations
```

这个数字仅代表正式关系规模，不构成质量目标；后续仍以 Admission Gate 精度优先。

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次012]]
- [[QX1.1 文学中的雨]]
- [[QX3.1 文学中的海]]
- [[QX16.1 文学中的书信]]
