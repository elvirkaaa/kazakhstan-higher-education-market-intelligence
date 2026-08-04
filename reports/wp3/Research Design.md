# Research Design — WP3

## Objective

To assess demographic and migration trends that influence current and future demand for higher education in Kazakhstan.

## Research Questions

**RQ1.** How has Kazakhstan's population changed since 1990?

**RQ2.** What are future population projections?

**RQ3.** How is the youth population (17-24, approximated via available 15-24 / 14-28 age bands) changing?

**RQ4.** Which regions are growing and which are shrinking?

**RQ5.** How does migration (external and interregional) influence higher education demand?

**RQ6.** What implications does this have for universities?

## Scope

**In scope:** General population trends, natural increase (births/deaths), age structure, dependency ratio, population projections, external and interregional migration, regional population distribution.

**Explicitly out of scope:** International student mobility, academic exchange, Bolashak, Erasmus+, foreign university branch campuses, and qualification recognition — these remain part of WP2 and are not duplicated here. Migration in WP3 refers only to general population migration (all migrants), not international students specifically.

## Methodology

Following the same evidence-first approach as WP1 and WP2: every dataset is documented in `Data_Inventory.md` before use, source-by-source analytical notes are recorded before any insight is drawn, and insights are recorded before the final report is written (Data -> Notes -> Insights -> Report -> Visualisation).

### Data Sources

Three primary sources, each covering a distinct gap:
- **Bureau of National Statistics (BNS)** - Kazakhstan's own official statistics: births, deaths, natural growth, regional population, external and interregional migration.
- **UN World Population Prospects (UN WPP)**, via the Population Division Data Portal - the only source providing forward-looking projections, dependency ratio, and youth-cohort age bands.
- **World Bank Open Data** - international-standard long time series for population, growth rate, urbanisation, and fertility, useful for cross-country benchmarking if needed.

Full source-by-source detail (strengths, limitations) is in `docs/Data_Sources.md` (WP3 section) and `analysis/WP3_Analytical_Notes.md`.

### Data Cleaning

- Each BNS source table is split into a national time series and a regional long-format table, consistent with the WP1/WP2 one-table-per-file convention.
- Region names are normalised where Cyrillic look-alike characters were found in source files (the same character-encoding issue documented in WP1's OPVO registry).
- Dash ("-") values are preserved as missing, not converted to zero, particularly for the three regions created in the 2022 territorial reform (Abai, Zhetisu, Ulytau).

### Validation

- Cross-checked UN WPP's 15-19/20-24 age-band figures (2025) against BNS/TALDAU's independently-sourced equivalent - found to match within ~1.3%, a reasonably strong independent confirmation between two different data-producing agencies.
- A planned cross-check of BNS vs. World Bank national population totals has been identified but not yet completed.

### A Documented Limitation: No Regional x Age-Band Cross-Tabulation

WP3 made a sustained, direct attempt (via TALDAU, Kazakhstan's official interactive statistics portal) to obtain a combined regional and age-band (ideally 17-24 or 15-24) population time series - the single most valuable dataset for RQ3 and RQ4 jointly. This was **not achievable**: TALDAU's export function for the relevant indicator (KSP 611111) allows only one "side" classification (either region breakdown OR age-group breakdown) per export, not both simultaneously. This was confirmed through direct testing, not assumed.

**Resolution:** RQ3 (youth cohort trends) is answered at the **national level only**, using UN WPP and BNS national age-band data. RQ4 (regional growth/decline) is answered using regional population, migration, and natural-growth data **without a precise youth-specific breakdown**, supplemented by a coarser 3-band regional age structure (child/working-age/pension-age) from a separate BNS bulletin. These two evidence bases are presented side by side in the report rather than forced into a single combined regional-youth metric that the underlying data does not support.

## Limitations

See `docs/Data_Sources.md` (WP3 section) for source-specific limitations. Cross-cutting: region names are not standardised across all BNS exports (Kazakh transliterations vs. English names) - see the Data Dictionary crosswalk note. The 2022 territorial reform creates a structural break in every regional time series prior to that date for the three new regions.
