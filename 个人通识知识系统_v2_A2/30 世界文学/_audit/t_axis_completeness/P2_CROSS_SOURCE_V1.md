# P2 Cross-Source T-axis Audit V1

> Read-only. Google Books is used only as a second bibliographic signal; no Work mutation occurs in this audit.

- P2 population queried: **421**
- SAFE_T (Open Library + Google Books agree on T interval): **0**
  - FILL_YEAR (source years within 2 years): **0**
  - T_ONLY_YEAR_REVIEW (same T but larger year gap): **0**
- REVIEW: **421**

## Safety gates

- title/author matching is required on Google Books.
- Open Library must already be HIGH.
- exact frozen boundary years are never auto-applied.
- the two sources must land in the same T interval.
- canonical `year` is proposed only when source years differ by <=2; otherwise only T is considered safe.

`P2_CROSS_SOURCE_V1 = AUDITED_READ_ONLY`
