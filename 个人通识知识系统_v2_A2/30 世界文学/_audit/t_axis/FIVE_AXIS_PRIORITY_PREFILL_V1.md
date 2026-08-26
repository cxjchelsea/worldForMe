# 五轴坐标与 T专题优先级读前预填 V1

- T轴作品：**2397**
- 本次修改文件：**746**
- T0/T1 的 M轴按现行 taxonomy 记为不适用；未创建伪 M0，也未强制归入 M1。

## 自动补值来源

| T | R auto | M auto | M N/A | G auto | Q auto | priority auto |
|---|---:|---:|---:|---:|---:|---:|
| T0 | 0 | 0 | 82 | 14 | 22 | 15 |
| T1 | 0 | 0 | 90 | 4 | 22 | 5 |
| T2 | 0 | 10 | 0 | 4 | 17 | 5 |
| T3 | 37 | 3 | 0 | 40 | 62 | 41 |
| T4 | 0 | 16 | 0 | 9 | 125 | 10 |
| T5 | 5 | 8 | 0 | 6 | 243 | 6 |
| T6 | 11 | 5 | 0 | 2 | 221 | 3 |

## 校准优先级

1. `*_source=t_default` 是时代众数回退，最先复核。
2. `topic_model` 和 `author_model` 是基于已有坐标的读前推断。
3. `existing` 值本次未改写，不代表已经读后确认。
4. 逐作品值与来源见 `FIVE_AXIS_PRIORITY_PREFILL_V1.csv`。

`FIVE_AXIS_PRIORITY_PREFILL_V1 = APPLIED_AND_VERIFIED`
