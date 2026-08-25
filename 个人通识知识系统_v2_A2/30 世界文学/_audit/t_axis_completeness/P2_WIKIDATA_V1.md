# P2 Wikidata Bibliographic Verification V1

> Read-only. Wikidata P577/P50 is treated as a work-level bibliographic signal; no Work mutation occurs here.

- P2 population: **421**
- SAFE total: **0**
  - SAFE_T cross-source agreement: **0**
  - SAFE_T_WIKIDATA_ONLY work-level match: **0**
- REVIEW: **421**

## Rules

- Wikidata candidate requires strong title match, author P50 match, and work-level publication date P577.
- When Open Library HIGH exists, both sources must agree on the T interval.
- A cross-T conflict blocks automatic completion.
- Exact frozen boundary years are blocked.
- For accepted rows, canonical year candidate comes from Wikidata P577 rather than edition-oriented catalog dates.

`P2_WIKIDATA_V1 = AUDITED_READ_ONLY`
