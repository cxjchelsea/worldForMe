# T-axis Completeness Audit V1

> Read-only audit. No Work entity is modified by this stage.

## Population

- Total canonical Work entities: **3209**
- With valid T0–T6 coordinate: **2262**
- Missing / invalid T coordinate: **947**
- Missing/invalid with aggregate/oral/tradition hint: **59**

## Missing-T classification

- MISSING_T_AUTO_CANDIDATE: **0**
- MISSING_T_BOUNDARY_YEAR: **0**
- MISSING_T_REVIEW_NO_YEAR: **947**
- INVALID_T_LABEL: **0**

## Current valid T distribution

- T0: **70**
- T1: **84**
- T2: **88**
- T3: **220**
- T4: **392**
- T5: **614**
- T6: **794**

## Governance interpretation

1. `MISSING_T_AUTO_CANDIDATE` is eligible for a governed batch-fill only after a sample/reasonableness check; year is a candidate signal, not proof for long-formation texts.
2. `MISSING_T_BOUNDARY_YEAR` must follow the already-frozen boundary policy and should not be assigned by generic interval code alone.
3. `MISSING_T_REVIEW_NO_YEAR` requires bibliographic/formation-history review; aggregate, oral, anonymous, and tradition texts should be reviewed first as model-special cases.
4. `INVALID_T_LABEL` is a schema-integrity issue, not a missing-data issue.

## Next stage

- First resolve schema-invalid/boundary/special-text cases and sample-check AUTO candidates.
- Then apply T-axis completion in controlled batches with postcondition checks.

`T_AXIS_COMPLETENESS_V1 = AUDITED_READ_ONLY`
