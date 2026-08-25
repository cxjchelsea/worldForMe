# Canonical Work Duplicate Scan — Manual Review V1

## Scope

- Full Work population scanned: **3216**
- Machine candidate pairs: **12**
- Confirmed duplicate pairs after manual semantic review: **7**
- Confirmed distinct / do-not-merge pairs: **5**
- Work mutation in this review stage: **NONE**

## A. CONFIRMED_DUPLICATE — ready for governed merge

1. `Noli Me Tangere.md` ↔ `社会毒瘤.md`
   - Same work: José Rizal, *Noli Me Tangere*.
   - English/original-title entity and Chinese-title entity split across T-axis/canon metadata.

2. `Rihla.md` ↔ `伊本·白图泰游记.md`
   - Same Ibn Battuta travel work/entity.
   - One entity carries QT14 travel metadata; the other carries T1 network metadata.

3. `佐罗的诅咒.md` ↔ `卡皮斯特拉诺的诅咒.md`
   - Same work: Johnston McCulley, *The Curse of Capistrano*.
   - Duplicate created by two Chinese translations/topic routes; metadata spans knight and swashbuckler branches.

4. `白鲸.md` ↔ `莫比·迪克.md`
   - Same work: Herman Melville, *Moby-Dick*.
   - One entity is the T3 curated anchor; the other is the CANON-129 Core entity.

5. `阿尔戈船英雄纪.md` ↔ `阿尔戈英雄纪.md`
   - Same work: Apollonius of Rhodes, *Argonautica*.
   - Duplicate created by adventure and mythology topic ingestion.

6. `开往巴基斯坦的列车.md` ↔ `开往巴基斯坦的火车.md`
   - Same work: Khushwant Singh, *Train to Pakistan* (1956).
   - Duplicate created by alternate Chinese translation wording; metadata spans T5 and historical-fiction topic routes.

7. `Facundo.md` ↔ `法昆多.md`
   - Same work: Domingo Faustino Sarmiento, *Facundo*.
   - Machine scanner downgraded this to TITLE_COLLISION because author normalization did not equate `萨米恩托 / Sarmiento` with the full Chinese author name; semantic review confirms identity.

## B. CONFIRMED_DISTINCT — explicitly do not merge

1. `Estoire del Saint Graal.md` ↔ `Queste del Saint Graal.md`
   - Distinct texts within the Lancelot-Grail / Vulgate Cycle; title similarity is not entity identity.

2. `人世间.md` ↔ `人世间（普拉姆迪亚）.md`
   - Different authors and different works: Liang Xiaosheng vs Pramoedya Ananta Toer.

3. `历史.md` ↔ `历史（莫兰特）.md`
   - Different works: Herodotus vs Elsa Morante.

4. `失乐园.md` ↔ `失乐园（弥尔顿）.md`
   - Different works: Junichi Watanabe's *Shitsurakuen* vs John Milton's *Paradise Lost*.

5. `凯瑟琳·安·波特短篇小说集.md` ↔ `琼·斯塔福德短篇小说集.md`
   - Different author-specific collections; generic translated collection naming is not sufficient for identity.

## Governance implications

- The 7 confirmed duplicates are eligible for **Dedup V2**: choose one canonical Work, union all axes/topics/source refs/read/canon metadata, preserve original/translated titles as aliases, redirect active references, then remove the duplicate Work.
- The 5 confirmed-distinct pairs should be added to a negative-match guard so future duplicate scanners do not repeatedly surface them.
- Author normalization needs an alias-aware layer; `Facundo` demonstrates that literal author matching is insufficient.
- The scan found **3216 Work entities**, materially more than the ~2145 entities covered by the previous T-axis population audit. This indicates that T-axis completeness and central Work completeness are separate governance dimensions.

`ENTITY_DEDUP_SCAN_MANUAL_REVIEW_V1 = COMPLETE`
`ENTITY_DEDUP_V2 = READY_NOT_APPLIED`
