---
id: "WL-TEMPLATE-TOPIC-BASE"
type: "system_rule"
domain: "literature"
scope: "topic_base_standard"
template_version: "literature-topic-v1"
---

# 文学专题 Base 规范

## 1. 结构 Base

结构 Base 只聚合当前专题的知识节点：

```yaml
filters:
  and:
    - 'topic_id == "WL-TOPIC-XXX"'
```

推荐至少提供：
- 全部知识节点
- 核心结构
- 主分支

结构页继续使用现有 `literature_topic_structure` / `literature_topic_section` 类型，不在 Base 里保存解释性正文。

## 2. 作品 Base

作品 Base 的机器关系键固定使用：

```yaml
filters:
  and:
    - type == "work"
    - topics.contains("WL-TOPIC-XXX")
```

`topics` 必须使用稳定专题 ID，不写中文名，不做前缀匹配。

## 3. 最低推荐视图

每个专题作品 Base 至少应有：

1. 全部作品
2. 核心骨架 ★
3. 骨架未读
4. 系统扩展 ◆
5. 按专题主分支
6. 已读

可按专题需要增加：
- 母题已标注
- 需复核
- 按历史阶段
- 按地域传统
- 按机制 / 技法

## 4. 已读视图

已读视图建议显示六轴：

```text
axis_t
axis_r
axis_m
axis_g
axis_n
axis_q
```

用于读后校准，而不是要求未读作品提前批量填写六轴。

## 5. 专题私有字段

推荐命名：

```text
<topic_prefix>_priority
<topic_prefix>_history_stage
<topic_prefix>_branch
<topic_prefix>_axes
<topic_prefix>_motifs
```

只创建真正需要的字段，不要求每个专题全部拥有。
