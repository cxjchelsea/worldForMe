# R1 Semantic Review V1

## Scope

- Historical R1 population reviewed: 81 Works.
- Review dimensions: R1 membership, internal tradition, duplicate risk, historical coverage gaps.
- This report does not itself merge duplicate canonical Works.

## Confirmed membership correction

- `WL-WORK-3215` 《德里纳河上的桥》: **MOVE R1 → R4**.
  - Reason: the work belongs to Yugoslav/Balkan-European literary tradition. Ottoman imperial history is part of its subject and historical background, not its primary literary-tradition coordinate.

## Boundary review retained

- `WL-WORK-2851` 《移居北方的时节》: **R1/R7 BOUNDARY REVIEW**.
  - Arabic-language literary tradition supports an R1 connection.
  - Sudanese/African literary history strongly supports R7 as primary regional-tradition context.
  - Final primary-coordinate decision is deferred until R7 is built, to avoid deciding the R1/R7 boundary unilaterally.

## High-confidence duplicate candidates

These pairs should enter the global canonical dedup workflow before topic-level priority scoring:

1. `WL-WORK-2047` 《太阳下的人们》 / `WL-WORK-1783` 《烈日下的人们》
   - same author: Ghassan Kanafani
   - same work: *Men in the Sun*
2. `WL-WORK-1772` 《海法归来》 / `WL-WORK-2141` 《重返海法》
   - same author: Ghassan Kanafani
   - same work: *Returning to Haifa*
3. `WL-WORK-2095` 《爱的艺术》 / `WL-WORK-2096` 《爱经》
   - same author: Ovid
   - same Latin work: *Ars Amatoria*; 《爱经》 is a Chinese translation title of the same work.
4. `WL-WORK-1511` 《酒神的伴侣》 / `WL-WORK-1512` 《酒神的女信徒》
   - same author: Euripides
   - same Greek tragedy: *Bacchae* under different Chinese translation titles.

No duplicate is deleted by this report because canonical merge must preserve aliases, source refs, topic memberships and redirects.

## Taxonomy correction discovered by review

The original eight R1 internal traditions were insufficient. Ugaritic works such as 《巴力神话组诗》《凯雷特史诗》《阿卡特史诗》 cannot be accurately classified as Mesopotamian or Hebrew-Jewish.

Therefore R1 now includes a ninth internal analysis node:

- 黎凡特—迦南与乌加里特文学传统

This is an R1 topic-internal node, not a new global `axis_r` coordinate.

## Historical coverage diagnosis

The old R1 collection was dense in T0 and T1 but had a major T2–T4 discontinuity. The gap is partly real for traditions that migrate into R4 (e.g. post-classical Greek/Latin European developments), but it is clearly a collection gap for Arabic, Hebrew and Ottoman-Turkish traditions.

## Supplement Batch 1

Four new canonical Works were added as structural anchors:

- 《德德·科尔库特之书》 — T1 — 土耳其—奥斯曼文学传统 — oral/epic to manuscript transition.
- 福祖里《莱拉与马吉农》 — 1536 / T2 — 土耳其—奥斯曼文学传统 — Turkish masnavi and Persian-model rewriting.
- 亚伯拉罕·马普《锡安之爱》 — 1853 / T3 — 希伯来—犹太文学传统 — formation of modern Hebrew fiction.
- 海卡尔《宰娜卜》 — 1913 / T4 — 阿拉伯文学传统 — formation of modern Arabic novel.

## Next review priorities

1. Resolve the four duplicate pairs through canonical dedup governance.
2. Re-audit R1 counts after the new works and R4 correction.
3. Continue T2–T4 supplementation, especially Nahda/modern Arabic prose, Ottoman-to-modern Turkish transition, and modern Hebrew literature.
4. Only after supplementation stabilizes, assign `r1_priority` and `r1_role` across the final deduplicated population.

`R1_SEMANTIC_REVIEW_V1 = COMPLETE_WITH_DEDUP_AND_BOUNDARY_FOLLOWUPS`
