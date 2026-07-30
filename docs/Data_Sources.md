# Data Sources — WP1

Detailed description of each source used in WP1 (Higher Education Landscape Assessment) — what it provides, its strengths, and its limitations.

---

## OPVO/EPVO Programme Classification Registry

**Purpose:** The primary and sole source for WP1's core dataset — a national registry of formally registered higher education programmes in Kazakhstan, including classification codes, degree levels, tuition fees (domestic and international), English-medium status, and subject-area classification.

**Strengths:**
- Comprehensive coverage: 46 universities, 8,530 raw programme-level records
- Official, government-maintained classification system (OPVO/EPVO codes)
- Contains both domestic (RK-citizen) and international tuition fee fields, enabling pricing analysis
- Covers the full academic pathway: Bachelor's, Master's, Doctoral, and Residency levels

**Limitations:**
- **Heavy row-level duplication**: 87% of raw rows sit inside groups sharing an identical university, classification code, and degree level — most plausibly from repeated registry export/ingestion rather than genuine repeated registration. The dataset resolves to approximately 2,417 distinct programmes once deduplicated.
- **OPVO classification codes are not guaranteed unique across institutions** — the same code has been observed attached to different programmes at different universities, discovered during cross-referencing in later work packages.
- **No native region or institution-type field** — region was inferred externally from each university's known home city (see Appendix A of the WP1 report), not sourced from the registry itself.
- **Character-encoding inconsistency**: approximately 3% of programme codes contain a Cyrillic "В" in place of the Latin "B", which silently breaks code-based matching if not normalised first.
- **Undocumented fields**: `status` (Active/New/Innovative) and `data_status` (Updated/Included) carry no official definition in the source and have been observed varying inconsistently across duplicate rows for the same programme.
- **Flat/placeholder pricing**: 13 institutions show zero tuition variance across their entire catalogue — every listed programme carries an identical fee, which may reflect either genuine flat-fee policy or an unpopulated per-programme pricing field; this cannot be distinguished from the data alone.
- **Incomplete foreign-fee data**: approximately 20% of records lack a foreign-student tuition figure, and the currency field (KZT/USD) is missing in about 12% of records.
- **`reg_date` is unreliable as a timestamp** — it does not behave as a consistent "last modified" indicator and varies non-chronologically within duplicate-record clusters.

---

## Publicly Available University Campus Location Information

**Purpose:** Used solely to construct the region mapping (assigning each of the 46 universities to an inferred home region/city), since the OPVO/EPVO registry carries no native region field.

**Strengths:**
- Enables regional analysis (Section 9 of the WP1 report) that would otherwise be impossible from the registry alone
- Based on each institution's well-established, publicly known primary campus location

**Limitations:**
- **This is an external analytical assumption, not a verified registry field** — every regional finding in WP1 inherits this assumption and should be read with that caveat
- Institutions with campuses in multiple cities were mapped to a single primary region, which may understate true multi-region presence for some universities
- The mapping was not independently verified against each institution's own official registration address

---

## Notes on citation practice for WP1

- Every figure, table, and finding in the WP1 report traces back to the OPVO/EPVO registry extract described above.
- Where a claim in the report is qualitative background (e.g. general statements about Kazakhstan's internationalisation policy), it is written at a general, non-citation-dependent level rather than attributed to a specific unverified source.
- The full region-to-university mapping is documented in Appendix A of the WP1 report for independent verification.

# WP2 Internationalisation

Detailed description of each source used in WP2 — what it provides, its strengths, and its limitations. For the processing status of each, see `Data_Inventory.md`.

---

## UN DESA International Migrant Stock 2024

**Purpose:** Provides mid-year international migrant stock estimates (1990–2024) by destination country and, in a second file, by bilateral destination × origin pair.

**Strengths:**
- Long, consistent time series (1990–2024)
- Bilateral (country-pair) detail available
- Authoritative UN source, methodologically consistent across countries

**Limitations:**
- Measures general migrant stock (foreign-born population), not students specifically — must not be presented as "international students" without clear labelling
- No breakdown by education level or field of study

---

## CIS Academic Mobility Background Report (translated)

**Purpose:** Reports 2022 academic-year bilateral academic mobility, faculty exchange, joint/double-degree programmes, and cooperation agreements between Kazakhstan and CIS countries.

**Strengths:**
- Direct, education-specific mobility figures (not just migrant stock)
- Covers both students and faculty, both directions
- Includes qualitative detail (fields of specialisation, online/offline format)

**Limitations:**
- Original source document and issuing agency not stated in the translation — should be confirmed before external publication
- Single academic year (2022) only — no time series
- Some internal figures (e.g. qualification composition by country) contain apparent transcription errors, documented in the relevant processed files

---

## ENIC-Kazakhstan Bologna Process Analytical Report (2023 edition)

**Purpose:** Annual monitoring report on Bologna Process implementation; contains scattered but useful data on foreign students, English-medium instruction, and international qualification recognition infrastructure.

**Strengths:**
- Official, government-published annual series (editions exist back to 2018)
- Contains some data not available elsewhere (e.g. English-medium foreign student concentration by field)

**Limitations:**
- Primary focus is Bologna Process compliance, not international student statistics — foreign-student data is sparse and narratively scattered rather than tabulated
- Some percentage figures do not reconcile with their own stated counts (documented per-file)

---

## National Report on the State and Development of the Higher Education System of the Republic of Kazakhstan for 2024

**Purpose:** The single richest source identified for WP2 — a dedicated, comprehensive annual report with a full chapter (Section 6) on internationalisation, covering mobility, foreign students, faculty exchange, the Bolashak scholarship programme, intergovernmental/interdepartmental grants, Research Internships, and Erasmus+.

**Strengths:**
- Purpose-built internationalisation chapter with dozens of granular tables
- Time series 2021–2024 for most mobility metrics
- Country-level, region-level, field-level, and level-of-study breakdowns

**Limitations:**
- Very large file (>20MB), requiring page-by-page extraction rather than automated bulk processing
- Multiple confirmed internal inconsistencies between tables covering the same metric (e.g. outgoing mobility totals for 2023 differ between Table 6.1.1/6.1.13 and Table 6.1.7) — documented per-file, with cross-references
- Some chart-derived figures (e.g. Figure 6.1.4) show suspicious repeated values across years, likely a source-side chart/label artifact
- Not yet fully extracted — only the pages provided so far have been processed; further sections may exist

---

## Kazakhstan's Path in Higher Education Recognition (Borgekova et al., 2026)

**Purpose:** Peer-reviewed journal article providing recognition/nostrification application statistics by year (2017–2025) and by top-5 origin country (Russia, Uzbekistan, India, China, Kyrgyzstan).

**Strengths:**
- Peer-reviewed, citable academic source
- Clean, already-tabulated data (Table 1 and Table 2 in the original article)
- Long time series (9 years)

**Limitations:**
- Only covers the top 5 applicant countries — no view of the long tail
- Some internal figures (e.g. applications received vs. recognised in the same year) do not reconcile, as recognition often lags application by more than one year — this is disclosed in the article itself, not a transcription error

---

## Bilateral Student Mobility Dashboard (existing HTML asset)

**Purpose:** A pre-built interactive dashboard, titled "Kazakhstan — Bilateral Student Mobility (UNESCO UIS OPRI)".

**Strengths:** Ready-made visual asset; potentially already reflects UNESCO UIS bilateral mobility data.

**Limitations:** The underlying data has not yet been independently re-extracted or verified against a live UNESCO UIS query — the extraction date and query parameters used to build it are not documented anywhere accessible so far.

---

## UNESCO Institute for Statistics (UIS) — planned

**Purpose:** Would provide internationally comparable inbound/outbound mobility ratios and counts for Kazakhstan, enabling direct comparison with other countries.

**Strengths:** Global coverage; standardised methodology across countries.

**Limitations:** Not yet accessed directly for WP2 (only indirectly via the existing dashboard, above); some indicators may be unavailable or lagged for Kazakhstan specifically.
---

## MSHE Foreign University Partnerships & Branch Campuses (2025)

**Purpose:** Provides institutional-level internationalisation data - foreign university branch campuses, strategic partnerships, double-degree arrangements, and investment partners - not covered by any other WP2 source.

**Strengths:**
- Only WP2 source addressing branch campuses and institutional partnerships directly
- Names specific universities, investment partners, and construction status
- Includes a forward-looking government target (100,000 international students by 2029)

**Limitations:**
- News republication of a government press release/infographic; original MSHE source URL and date not independently confirmed
- Geographic map component required visual transcription (higher error risk, documented per-row)
- Contains an internal self-contradiction on the CIS-vs-Asia claim
- India's student count (9,969) conflicts with the National Report 2024 figure (12,020) - unresolved
