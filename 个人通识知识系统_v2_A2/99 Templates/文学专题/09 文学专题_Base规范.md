---
id: "WL-TEMPLATE-TOPIC-BASE"
type: "system_rule"
domain: "literature"
scope: "topic_base_standard"
template_version: "literature-topic-v1"
---

# 文学专题 Base 规范

## 1. 结构 Base 的机器边界

结构 Base 只聚合当前专题知识节点：

```yaml
filters:
  and:
    - 'topic_id == "WL-TOPIC-XXX"'
```

不要让结构 Base 同时承担作品数据库职责。

## 2. 知识节点类型

`literature-topic-v1` 允许按职责使用：

```text
literature_topic_structure
```

用于 `10 结构/` 的高层解释与导航节点。

```text
literature_topic_section
```

用于 `11` 第一主维度、历史阶段、传统入口、umbrella 系统注册 / 比较节点等。

```text
literature_topic_mechanism
```

推荐用于 direct topic 中可跨多个 `11` 节点复用的 `12` 第二分析维度。

注意：**类型不是目录编号的机械映射。** 已有成熟专题若使用 `section + parent + dimension` 表达 umbrella 比较维度，不为了统一 type 制造无收益迁移。

## 3. 结构 Base 推荐视图

最低建议：
1. 全部知识节点；
2. 核心结构；
3. 第一主维度。

只有专题存在成熟第二维时才增加：
4. 第二分析维度 / 机制深化。

推荐属性：

```yaml
file.name
id
type
dimension
parent
sequence
```

再按专题添加：
- 历史阶段字段；
- 传统入口字段；
- system_class；
- compare_cluster；
- mechanism cluster 等。

### 核心结构视图

```yaml
filters:
  and:
    - 'type == "literature_topic_structure"'
```

### 第一维视图

优先用 `parent` 或 `dimension` 精确过滤，不要只靠文件夹名称推断。

### 第二维视图

若 direct topic 使用 `literature_topic_mechanism`：

```yaml
filters:
  and:
    - 'type == "literature_topic_mechanism"'
```

若 umbrella 已有不同稳定模型，则按 `parent / dimension` 过滤。

## 4. 作品 Base

机器关系键固定使用：

```yaml
filters:
  and:
    - type == "work"
    - topics.contains("WL-TOPIC-XXX")
```

`topics` 必须使用稳定专题 ID：
- 不写中文名；
- 不做前缀匹配；
- 不因为专题移动目录而修改稳定 ID。

## 5. 作品 Base 最低推荐视图

通常至少包含：
1. 全部作品；
2. 核心骨架 ★；
3. 骨架未读；
4. 系统扩展 ◆；
5. 按专题第一主维度；
6. 已读。

按专题需要增加：
- 按历史阶段；
- 按地域传统；
- 按问题 / 机制；
- 母题已标注；
- 需复核。

不要为了模板对称给每个专题建立同样数量的视图。

## 6. 已读视图

已读 / 重读视图建议显示：

```text
axis_t
axis_r
axis_m
axis_g
axis_n
axis_q
```

用于读后校准，不要求未读作品提前批量填写六轴。

## 7. 专题私有字段

推荐按实际职责命名：

```text
<topic_prefix>_priority
<topic_prefix>_history_stage
<topic_prefix>_branch
<topic_prefix>_axes
<topic_prefix>_motifs
```

只创建真正需要的字段，不要求每个专题全部拥有。

已有稳定作品 schema 在知识层重构时默认保持不变。

## 8. Base 与 Markdown 的边界

- Base：回答“有哪些实体 / 如何筛选 / 如何分组”。
- Markdown：回答“为什么这样分 / 这些关系意味着什么 / 应该怎样读”。

专题首页和结构页不维护动态作品总数。
