# Canonical Work Duplicate Candidate Scan V1

- Work entities scanned: **3216**
- HIGH_CONFIDENCE pairs: **4**
- REVIEW pairs: **3**
- TITLE_COLLISION pairs: **5**

This scan is read-only for `40 作品`: it does not merge or delete Work entities.

## HIGH_CONFIDENCE

- `Noli Me Tangere.md` ↔ `社会毒瘤.md` — same normalized title/original/alias + same author
- `Rihla.md` ↔ `伊本·白图泰游记.md` — same normalized title/original/alias + same author
- `佐罗的诅咒.md` ↔ `卡皮斯特拉诺的诅咒.md` — same normalized title/original/alias + same author
- `白鲸.md` ↔ `莫比·迪克.md` — same normalized title/original/alias + same author

## REVIEW

- `阿尔戈船英雄纪.md` ↔ `阿尔戈英雄纪.md` — score 0.923; similar title + same author
- `开往巴基斯坦的列车.md` ↔ `开往巴基斯坦的火车.md` — score 0.889; similar title + same author
- `Estoire del Saint Graal.md` ↔ `Queste del Saint Graal.md` — score 0.872; similar title + same author

## TITLE_COLLISION

Same/similar titles with different or unresolved authors are explicitly not auto-merge candidates.

- `Facundo.md` ↔ `法昆多.md` — same normalized title but author differs/unknown
- `人世间.md` ↔ `人世间（普拉姆迪亚）.md` — same normalized title but author differs/unknown
- `凯瑟琳·安·波特短篇小说集.md` ↔ `琼·斯塔福德短篇小说集.md` — same normalized title but author differs/unknown
- `历史.md` ↔ `历史（莫兰特）.md` — same normalized title but author differs/unknown
- `失乐园.md` ↔ `失乐园（弥尔顿）.md` — same normalized title but author differs/unknown

`ENTITY_DEDUP_SCAN_V1 = COMPLETE_READ_ONLY_SCAN`
