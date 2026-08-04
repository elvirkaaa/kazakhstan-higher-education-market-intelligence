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

---

## WP3 — Administrative Regions of Kazakhstan (Oblasts)

As of 1 January 2024, the Republic of Kazakhstan comprises **17 regions (oblasts)** and **3 cities of republican significance** (Astana, Almaty, Shymkent), which are administered independently and do not belong to any oblast. This structure is directly relevant to WP3's regional demographic tables and to WP1/WP2's regional findings — see the cross-cutting region-name crosswalk note below.

| Region (English) | Administrative centre | Notes |
|---|---|---|
| Abai Region | Semey | Established 8 June 2022, split from East Kazakhstan Region |
| Akmola Region | Kokshetau | |
| Aktobe Region | Aktobe | |
| Almaty Region | Konaev (formerly Kapchagai; administrative centre relocated here in 2023 — verify against a current official source before citing) | Not to be confused with Almaty city, which is a separate republican-significance city |
| Atyrau Region | Atyrau | |
| East Kazakhstan Region | Oskemen (Ust-Kamenogorsk) | |
| Jetisu (Zhetysu) Region | Taldykorgan | Established 8 June 2022, split from Almaty Region |
| Karaganda Region | Karaganda | |
| Kostanay Region | Kostanay | |
| Kyzylorda Region | Kyzylorda | |
| Mangystau Region | Aktau | |
| North Kazakhstan Region | Petropavl | |
| Pavlodar Region | Pavlodar | |
| Turkistan Region | Turkistan | |
| Ulytau Region | Zhezkazgan | Established 8 June 2022, split from Karaganda Region |
| West Kazakhstan Region | Oral (Uralsk) | |
| Zhambyl Region | Taraz | |
| **Astana** (city of republican significance) | — | National capital since 1997 (as Astana/Nur-Sultan/Astana) |
| **Almaty** (city of republican significance) | — | Former capital; largest city by population |
| **Shymkent** (city of republican significance) | — | Gained republican-significance status in 2018 |

**Total administrative units at this level: 20** (17 regions + 3 cities).

### Sources

- Bureau of National Statistics of the Republic of Kazakhstan, "Administrative-territorial units of the Republic of Kazakhstan" (as of 1 January 2024) — stat.gov.kz
- Law "On Administrative-Territorial Division of the Republic of Kazakhstan" — adilet.zan.kz (Adilet Legal Information System)

### Important note on the 2022 territorial reform

Three new regions (Abai, Jetisu/Zhetysu, Ulytau) were created on 8 June 2022 by splitting existing regions (East Kazakhstan, Almaty, and Karaganda respectively). **This is why every time-series regional dataset in this project (WP1, WP2, and WP3) shows blank/dash values for these three regions before 2022** — they did not exist as separate administrative units before that date, and their populations were previously counted within their parent region's totals. This is not missing data; it is a genuine structural break in the regional time series and should always be disclosed alongside any pre/post-2022 regional comparison.

### Cross-cutting note: region-name inconsistency across sources

As already flagged in the WP2 addendum, region names are not standardised across all sources used in this project:

| Canonical (English) | Also seen as |
|---|---|
| West Kazakhstan Region | Batys Kazakhstan (Kazakh transliteration, used in some BNS exports) |
| North Kazakhstan Region | Soltustik Kazakhstan (Kazakh transliteration) |
| East Kazakhstan Region | Shygys Kazakhstan (Kazakh transliteration) |
| Jetisu Region | Zhetysu Region / Zhetisu (older English spelling) |

A region-name crosswalk table should be finalised before any cross-source regional dataset is merged for analysis (see `docs/Methodology.md`, WP3 section, Integration).