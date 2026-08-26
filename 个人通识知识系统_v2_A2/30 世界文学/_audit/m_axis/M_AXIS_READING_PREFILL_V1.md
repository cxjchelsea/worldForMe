# M轴文学作品读前预填 V1

- 专题成员关系：**622**
- 唯一作品文件：**593**
- 本次修改文件：**593**
- 原有非空五轴坐标不覆盖；仅补空值并去除完全重复项。

## 专题覆盖

| 专题 | 数量 |
|---|---:|
| M1 | 76 |
| M2 | 85 |
| M3.1 | 149 |
| M3.2 | 68 |
| M4 | 90 |
| M5.1 | 80 |
| M5.2 | 74 |

## 自动补值

- `axis_g:author_model`：45
- `axis_g:conservative_default`：183
- `axis_g:title_or_tag`：97
- `axis_q:topic_default`：79
- `axis_q:topic_tags`：246
- `axis_r:author_model`：56
- `axis_r:topic_default`：254
- `axis_t_auto`：335
- `role:cross_membership`：49
- `role:mechanism_tag`：155
- `role:priority_core`：271
- `role:priority_focus`：147

## 校准说明

1. 谱系位置由专题历史语境与作品角色组合生成。
2. 专题角色优先依据原专题标签，其次依据跨专题关系与优先级。
3. 缺失五轴依次使用年代、专题、作者模型、标题及原专题标签推断。
4. 逐项结果见 `M_AXIS_READING_PREFILL_V1.csv`。

`M_AXIS_READING_PREFILL_V1 = APPLIED_AND_VERIFIED`
