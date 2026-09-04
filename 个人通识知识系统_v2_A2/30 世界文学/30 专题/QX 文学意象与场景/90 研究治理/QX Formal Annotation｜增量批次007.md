---
id: WL-QX-FORMAL-ANNOTATION-007
type: literature_qx_annotation_report
name: QX Formal Annotation｜增量批次007
code: QX-ANNOTATION-007
axis: Q
facet: QX
status: COMPLETE
schema: QX_RELATION_SCHEMA_V1
admission_gate: ADMISSION_GATE_V1
works:
  - 陆犯焉识
  - 佩德罗·巴拉莫
  - 微微一笑很倾城
  - 平面国
---

# QX Formal Annotation｜增量批次007

> 本批继续使用冻结的 `QX_RELATION_SCHEMA_V1 + ADMISSION_GATE_V1`。
>
> 重点测试：历史创伤空间、亡灵声音、数字媒介空间、几何身体与维度世界。

---

## 01｜批次结果

| 作品 | 正式 QX 关系数 | 主要对象 |
|---|---:|---|
| 《陆犯焉识》 | 2 | 劳改农场与荒原；书信 |
| 《佩德罗·巴拉莫》 | 4 | 科马拉；低语与亡灵声音；炎热与尘土；坟墓 |
| 《微微一笑很倾城》 | 2 | 网络游戏《梦游江湖》；游戏婚礼 |
| 《平面国》 | 4 | 二维平面世界；几何形状身体；球体；线国与点国 |

```text
BATCH_007_WORKS = 4
BATCH_007_FORMAL_RELATIONS = 12
FORMAL_QX_RELATIONS_BEFORE = 127
FORMAL_QX_RELATIONS_AFTER = 139
FORMAL_WORKS_WITH_QX_BEFORE = 29
FORMAL_WORKS_WITH_QX_AFTER = 33
```

---

## 02｜新专题激活：QX16.1 文学中的书信

《陆犯焉识》的“书信”加入后，正式数据中已有 3 部作品稳定使用同一 object：

1. 《傲慢与偏见》：达西长信纠正错误判断；
2. 《一个陌生女人的来信》：临终长信构成迟到的完整生命叙述；
3. 《陆犯焉识》：私人通信穿越长期政治与家庭分离，维系关系和记忆。

因此满足：

```text
WORK_COUNT = 3
FUNCTION_VARIANTS >= 2
ACTIVATION_STATUS = PASS
```

正式激活：

```text
QX16.1 文学中的书信
```

三部作品已经统一 normalization 为：

```yaml
qx_id: QX16.1
object: 书信
```

差异继续保留在 `manifestation / function / mode / evidence` 中。

---

## 03｜《佩德罗·巴拉莫》：声音可以成为空间结构

本作的“低语与亡灵声音”并非抽象的“记忆”或“死亡主题”，而是持续可感知的听觉对象。

其运行方式为：

```text
亡灵声音
× auditory
× 空间绑定
× 记忆触发
× 场景转换
```

这使科马拉不是单纯“一个死城”，而是被声音持续重建的叙事空间。

因此：

```text
SOUND_OBJECT can carry SPATIAL_FUNCTION
```

---

## 04｜《微微一笑很倾城》：数字空间也可以进入 QX

本批没有把“网络爱情”“虚拟身份”等抽象概念录入 QX。

正式保留的是：

- 网络游戏《梦游江湖》：持续在线的虚拟空间与关系媒介；
- 游戏婚礼：可见、公开、重复可识别的数字社会仪式。

因此 QX 的“可感知对象”不等于必须是物理世界实体：

```text
DIGITAL_OBJECT / DIGITAL_SPACE
can enter QX
when it has stable manifestation + narrative function
```

---

## 05｜《平面国》暴露出的分类边界

《平面国》正式保留：

```text
二维平面世界
几何形状身体
球体
线国与点国
```

这四项可以进入现有 schema，但其 `primary_group` 暴露了一个需要长期观察的边界：

- 几何身体可以较自然地进入 QX9 身体；
- 二维/一维/三维世界则暂时归入 QX19 阈限与超常空间，但这不是完全理想的本体位置。

当前处理原则：

```text
DO NOT CHANGE TAXONOMY FOR ONE WORK
KEEP OBSERVING
```

只有未来更多作品稳定出现“维度空间 / 几何世界 / 非欧几何场景”等对象时，再决定是否修改 QX 顶层分类。

---

## 06｜低密度仍然有效

《陆犯焉识》和《微微一笑很倾城》都只保留 2 条正式关系。

这继续证明：

```text
NO QUANTITY CAP
NO MINIMUM COUNT
QUALITY_GATE > DENSITY
```

作品可以重要、好读或具有明确主题，但不意味着必须拥有大量 QX 对象。

---

## 07｜当前正式状态

```text
QX_SCHEMA = FROZEN_V1
ADMISSION_GATE = ACTIVE
FORMAL_ANNOTATION_MODE = ACTIVE
FORMAL_QX_RELATIONS = 139
FORMAL_WORKS_WITH_QX = 33
ACTIVE_QX_LEAVES = 2
ACTIVE_QX_LEAF_1 = QX3.1 文学中的海
ACTIVE_QX_LEAF_2 = QX16.1 文学中的书信
NEW_TOPIC_THIS_BATCH = QX16.1
```

---

## 返回

- [[QX 作品意象标注与关系治理规则]]
- [[QX Formal Annotation｜增量批次006]]
- [[QX16.1 文学中的书信]]
- [[QX3.1 文学中的海]]
