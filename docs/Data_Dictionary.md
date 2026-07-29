# Data Dictionary

**Dataset:** Kazakhstan Higher Education Programme Registry (consolidated)
**Records:** 8,530 raw programme-level records (≈2,417 distinct programmes after deduplication)
**Last updated:** 28 July 2026

This dictionary documents every field in the master dataset underlying the WP1 Higher Education Landscape Assessment, the Executive Brief, and all figures and tables.

| # | Variable | Type | Description | Example |
|---|---|---|---|---|
| 1 | `no` | Integer | Sequential row index from the source registry export. Not a stable record ID — do not use for joins. | `24` |
| 2 | `opvo_code` | Text | National OPVO/EPVO programme classification code. **Not guaranteed unique across institutions** — the same code has been found attached to unrelated programmes at different universities (see Methodology). | `6B03104` |
| 3 | `program_name` | Text | English-language programme title. | `Psychology` |
| 4 | `status` | Categorical | Registry status flag: `Active`, `New`, or `Innovative`. Meaning not fully documented by the source registry; has been observed varying across duplicate rows for the same programme. | `New` |
| 5 | `university` | Text | Institution name as recorded in the registry. Some entries carry malformed strings (unbalanced quotation marks) or bare abbreviations — see Cleaning Methodology. | `ALMAU` |
| 6 | `level` | Categorical | Degree level: `Bachelor`, `Master`, `Doctoral (PhD)`, or `Residency`. | `Bachelor` |
| 7 | `data_status` | Categorical | Update flag: `Updated` or `Included`. Meaning not fully documented by the source registry. | `Updated` |
| 8 | `reg_date` | Date (DD.MM.YYYY) | Recorded registration date. Not a reliable indicator of when a programme or price was last substantively changed (see Limitations). | `02.09.2019` |
| 9 | `rk_kzt` | Numeric | Annual tuition fee for domestic (RK-citizen) students, in Kazakhstani tenge. 8.8% missing. | `2600000` |
| 10 | `currency` | Categorical | Currency of the `foreign_val` field: `KZT` or `USD`. 11.7% missing. | `KZT` |
| 11 | `foreign_val` | Numeric | Annual tuition fee for international students, in the currency stated by `currency`. 19.7% missing. | `2600000` |
| 12 | `english` | Boolean (Yes/No) | Whether the programme is delivered in English. | `Yes` |
| 13 | `price_year` | Categorical | Academic year the listed price applies to (e.g. `2025-2026`). 8.8% missing, tracking `rk_kzt` missingness exactly. | `2025-2026` |
| 14 | `area` | Categorical | Broad subject-area classification (11 categories, e.g. Engineering & Technology, Business/Economics/Law). | `Social Sciences & Journalism` |

## Derived fields used in analysis

| Variable | Type | Derivation |
|---|---|---|
| `region` | Categorical | Inferred from each university's known home city. **Not a native registry field** — an analytical assumption made for this project. See `references/References.md` and the full mapping in the report Appendix A. |
| `eng_flag` | Boolean (0/1) | `1` if `english == "Yes"`, else `0`. Used for all English-medium share calculations. |

## Known data-quality notes (see also CHANGELOG and the full report's Limitations section)

- 87% of raw rows sit inside duplicate (`university`, `opvo_code`, `level`) groups — always deduplicate before counting "programmes."
- 13 institutions show zero tuition variance across their full catalogue (flat institutional pricing or an unpopulated field — cannot be distinguished from this data alone).
- `opvo_code` values occasionally contain a Cyrillic "В" in place of the Latin "B" (~3% of codes), which silently breaks code-based matching if not normalised first.