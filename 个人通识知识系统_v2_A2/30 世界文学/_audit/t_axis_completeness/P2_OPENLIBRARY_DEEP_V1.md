# P2 Open Library Deep Edition-Year Audit V1

> Read-only. Uses exact title/author matching plus edition-year evidence within Open Library; no Work mutation occurs here.

- P2 population: **421**
- SAFE_T: **300**
- REVIEW: **121**

## Safe rule

A row is SAFE only when title+author match is strong and the earliest observed edition year and `first_publish_year` fall in the same frozen T interval. Exact boundary years are blocked.

`P2_OPENLIBRARY_DEEP_V1 = AUDITED_READ_ONLY`
