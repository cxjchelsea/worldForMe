---
id: "WL-TH"
legacy_id: WL-TH
type: literature_axis
name: 主题与人类问题
code: TH
legacy_code: QH
axis: TH
role: primary
system_role: work_coordinate
coordinate_field: axis_th
legacy_parent: "WL-Q"
parent: "WL-COORDINATES"
level: 1
priority_scheme:
  core: "★"
  important: "◆"
  extension: "△"
node_model: "group → leaf → topic map"
node_kind: coordinate_group
anchorable: false
topic_map: null
axis_status: frozen
axis_review: "[[TH 轴级总终审]]"
axis_contract: "[[TH 轴结构契约]]"
source_version: "TH-contract-v2"
---

# TH 主题与人类问题

> 路径：世界文学 → 作品坐标系统 → **TH 主题与人类问题**。

TH 与 T / R / M 同属作品坐标轴。它回答：**作品主要在思考什么主题 / 人类问题？**

一部作品可以同时拥有多个 TH；canonical 作品字段为 `axis_th`。迁移期旧 `axis_q` 中的 TH 值仍可作为 fallback 读取。

TH V1 已完成轴级总终审并冻结。TH9、TH10 当前不恢复；TH4–TH8 全局停在域一级，复杂度由各自专题内部问题承接。

## 坐标树

```text
TH  主题与人类问题
├─ TH1 自我、存在与生命
│   ├─ TH1.1 自我认同与主体性
│   ├─ TH1.2 自由与选择
│   ├─ TH1.3 孤独
│   ├─ TH1.4 死亡
│   └─ TH1.5 意义与荒诞
├─ TH2 亲密关系、家庭与成长
│   ├─ TH2.1 爱情与欲望
│   ├─ TH2.2 婚姻与亲密关系
│   ├─ TH2.3 家庭与家族
│   ├─ TH2.4 亲子与代际
│   └─ TH2.5 童年与成长
├─ TH3 社会身份、身体与归属
│   ├─ TH3.1 性别与身体
│   ├─ TH3.2 性、欲望与性规范
│   ├─ TH3.3 种族与族群
│   ├─ TH3.4 民族与文化身份
│   ├─ TH3.5 迁徙与流亡
│   ├─ TH3.6 故乡与归属
│   └─ TH3.7 殖民身份
├─ TH4 社会、阶级与劳动
├─ TH5 权力、制度与秩序
├─ TH6 战争、暴力与创伤
├─ TH7 历史、记忆与时间
└─ TH8 信仰、伦理与超越
```

## 子节点

- [[TH1 自我、存在与生命]]
- [[TH2 亲密关系、家庭与成长]]
- [[TH3 社会身份、身体与归属]]
- [[TH4 社会、阶级与劳动]]
- [[TH5 权力、制度与秩序]]
- [[TH6 战争、暴力与创伤]]
- [[TH7 历史、记忆与时间]]
- [[TH8 信仰、伦理与超越]]

## 优先级语义

TH 专题与 T / R / M 统一使用：

- `★`：核心骨架作品；
- `◆`：重要比较作品；
- `△`：扩展与边界作品。

具体字段前缀可以因专题而异，但语义不得改变。

## 节点模型

```text
TH 轴
→ taxonomy_group
→ taxonomy_leaf
→ literature_topic_map
→ topic structure / work projection
```

- group 不直接挂专题；
- leaf 是作品可标注坐标，并由专题地图展开；
- 专题内部核心问题不是新的 `axis_th` 坐标。

## 轴级治理

- [[TH 轴结构契约|TH 轴结构契约]]
- [[TH 轴级总终审|TH 轴级总终审]]
- [[TH 轴级边界速查|TH 轴级边界速查]]
- [[TH 轴级冻结状态|TH 轴级冻结状态]]

### 当前观察名单

以下方向继续观察，但不作为正式 TH：

- 自然、环境与非人世界
- 知识、科学与技术
- 艺术、语言与创作

只有在跨时期、跨地域作品压力测试证明现有 TH1—TH8 无法稳定承接时，才重新讨论新增 TH9。

## 与其他系统的边界

- **TH**：作品主要在思考什么；
- **TY**：作品采用什么类型、叙事与文化机制；
- **IM**：文本中出现什么高显著意象；
- **CN**：作品与什么长期文化叙事结构发生关系；
- **T / R / M / G**：作品处于什么时间、地域、思潮与体裁坐标。

## 冻结后的使用原则

TH 轴后续工作重点由“继续设计分类树”转为：作品补标、已读作品校准、专题内容丰满、跨作品比较和算法/检索验证。多重 TH 命中允许，但每个坐标都必须能说明该作品在此处具体追问什么独立问题。

## 返回

- [[../../04 系统架构/01 作品坐标系统|作品坐标系统]]
- [[../../00 世界文学使用规则|世界文学使用规则]]
