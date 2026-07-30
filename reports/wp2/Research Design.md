## Research Design

WP2 follows the same evidence-first, audit-before-analysis approach established in WP1: every dataset is documented (source, date, processing steps) before it is used in any figure, table, or claim. Where a source contains internal inconsistencies (e.g. two tables in the same report disagreeing on the same metric), these are flagged explicitly rather than silently resolved, unless a later source provides clear reconciling evidence — in which case earlier files are updated with a visible "UPDATE" note rather than overwritten silently.

## Data Sources

Full source-by-source detail is in `Data_Sources.md`. In summary, WP2 draws on:
- UN DESA International Migrant Stock 2024 (general migration context)
- A translated Kazakhstani source report on CIS academic mobility, agreements, and faculty exchange (2022 academic year)
- ENIC-Kazakhstan's 2023 Bologna Process analytical report (foreign student and internationalisation indicators)
- The National Report on the State and Development of the Higher Education System of the Republic of Kazakhstan for 2024 (Section 6 — Internationalisation of Higher and Postgraduate Education), covering academic mobility, foreign students, faculty exchange, the Bolashak programme, intergovernmental/interdepartmental grants, Research Internships, and Erasmus+
- A peer-reviewed journal article on Kazakhstan's qualification recognition system (Borgekova et al., 2026), including recognition/nostrification statistics by year and by country
- An existing interactive dashboard on bilateral student mobility (UNESCO UIS OPRI-sourced)

## Data Cleaning

- Each source table is transcribed into a single-topic spreadsheet (one table = one file), with a title, the data itself, and a source/caveat note.
- Dash ("-") values in original tables are preserved as blank/missing, not converted to zero, unless the source explicitly states the dash means zero.
- Country and institution names are standardised to English throughout, even where the source was in Russian.

## Validation

- Every multi-row table is checked for internal arithmetic consistency (do the rows sum to the stated total?) before being finalised.
- Where the same metric appears in more than one source table, the values are cross-checked against each other.
- Confirmed inconsistencies are documented in the file's own note, not corrected silently.
- When a later-processed source resolves an earlier open question, the earlier file is revisited and updated with a dated "UPDATE" note rather than left stale.

## Integration

Processed datasets are organised by source under `data/processed/wp2/<source>/`, mirroring the WP1 convention (`data/processed/wp1/epvo/` etc.). A merged, analysis-ready dataset has not yet been built (see `09_TODO.md`) — this methodology document will be updated once that integration step begins.

## Limitations

See `Data_Sources.md` for source-specific limitations and the individual dataset files (each carries its own caveats in an in-file note). Cross-cutting limitations affecting the whole work package are tracked in `Research_Assets_Register.md` under each asset's status.
