# R1 Topic Coverage Audit V1

> Read-only audit. No canonical Work was modified.

## Population

- Total canonical Work entities: **3209**
- Works currently mapped to R1: **81**
- R1 share of canonical Works: **2.5%**

## R1 metadata completeness

- Missing `year`: **64**
- Missing `r1_priority`: **81**
- Missing `r1_tradition`: **81**
- Missing `r1_role`: **81**

## T distribution inside R1

- T0: **42**
- T1: **17**
- T2: **1**
- T3: **0**
- T4: **1**
- T5: **15**
- T6: **4**

## Provenance coverage

- batch1_source_refs: **4** works
- batch2_source_refs: **9** works
- batch3_source_refs: **43** works
- batch4_source_refs: **6** works
- batch5_source_refs: **13** works
- batch6_source_refs: **2** works

## Interpretation

1. This audit measures current R1 mapping coverage, not the historical completeness of the R1 canon.
2. Empty `r1_*` fields are expected before topic enrichment; they define the next enrichment queue.
3. Works with missing year should reuse the governed year/T bibliographic policy rather than infer dates from modern editions.
4. A later semantic review must test whether current R1 assignments contain false positives and whether major R1 works are currently unmapped.

`R1_TOPIC_COVERAGE_V1 = AUDITED_READ_ONLY`
