# WP2 – Analytical Notes


## Source 1 — UNESCO UIS

### What does this dataset contain?

In its current form in this project, UNESCO UIS is represented only indirectly: through a pre-built interactive dashboard ("Kazakhstan — Bilateral Student Mobility (UNESCO UIS OPRI)") that was supplied as an existing asset rather than built from raw UIS data by Claude in this chat. UIS itself, as a source, publishes internationally comparable indicators on inbound and outbound mobile students by country of origin/destination, typically as ratios (e.g. outbound mobility ratio) and absolute counts.

### Strengths

- Global, standardised methodology — the only source in this project that would allow a genuine like-for-like comparison of Kazakhstan against other countries
- Long-standing, citable, internationally recognised statistical authority
- Bilateral (country-pair) detail available for many countries

### Limitations

- **Not yet independently verified in this project.** The dashboard's underlying extraction date, query parameters, and exact indicator definitions have not been confirmed against a live UIS query — this is the single largest open gap in the WP2 source base.
- UIS mobility statistics are known to lag by 1-2 years relative to national administrative sources (a general property of the dataset, not specific to Kazakhstan)
- Some country-level indicators are unavailable or suppressed for smaller flows

### Key indicators

- Inbound mobile students (count, by origin country)
- Outbound mobile students (count, by destination country)
- Mobility ratios (inbound/outbound as a share of total tertiary enrolment)

*(Exact indicators actually embedded in the existing dashboard have not yet been catalogued — this should be the first concrete task for this source, see Questions Raised below.)*

### Initial observations

- No independent observations can yet be drawn — this source has not been directly queried or re-verified in this project. Any figures currently visible only via the dashboard should be treated as provisional until cross-checked.

### Questions raised

- What exact indicators, years, and extraction date does the existing dashboard use?
- Does UIS data broadly agree with the National Report 2024's mobility figures (Section 6.1), or diverge — and if it diverges, by how much?
- Is UIS the best source for the cross-country comparison needed for RQ7 (opportunities for expansion), or would a smaller set of directly comparable countries (via their own national statistics) be more reliable?

---

## Source 2 — UNDESA

### What does this dataset contain?

Two official UN DESA Population Division files: (1) International Migrant Stock 2024 by destination country, both sexes/male/female, 1990-2024; (2) the bilateral version, migrant stock by destination × origin country pair, same time range. Both were downloaded directly and Kazakhstan-specific rows were extracted.

### Strengths

- Long, consistent time series (1990-2024, in 5-year intervals)
- Authoritative, methodologically consistent UN source — usable for genuine cross-country comparison
- Bilateral detail lets us see exactly which countries send the most migrants to Kazakhstan (and vice versa, in principle, though this project only extracted the Kazakhstan-as-destination view)

### Limitations

- **This is general migrant stock (total foreign-born population), not student mobility.** It must never be presented as "international students" — a distinction repeatedly flagged throughout this project's processed files.
- No breakdown by education level, field of study, or reason for migration
- 5-year intervals only (1990, 1995, 2000... 2024) — no annual granularity, unlike the National Report's year-by-year mobility tables

### Key indicators

- Total migrant stock in Kazakhstan by year (both sexes, male, female)
- Migrant stock by individual origin country, by year

### Initial observations

- Kazakhstan's 2024 migrant stock (destination) is dominated by Uzbekistan (744,161), Russia (552,258), and China (196,398) — an ordering that broadly echoes, but is not identical to, the CIS-dominance pattern seen in the education-specific mobility data (where Uzbekistan and Russia also lead, but the exact rankings and scale differ substantially since migrant stock includes all long-term residents, not just students).
- The scale gap is enormous: migrant stock figures (hundreds of thousands) dwarf the education-specific mobility figures (hundreds to low thousands) by roughly two to three orders of magnitude — a useful reminder that student mobility is a small slice of Kazakhstan's overall migration picture.

### Questions raised

- Does UNDESA's country ranking (Uzbekistan > Russia > China) hold up when restricted to just the working-age or student-age population, or is it driven mostly by older labour migration unrelated to education?
- Should this source be used only as background context (as currently planned) or could the bilateral time series support a genuine RQ6 analysis (how migration trends influence internationalisation) if paired with the mobility time series from the National Report?

---

## Source 3 — CIS

### What does this dataset contain?

A translated Kazakhstani source report (translator: Danesh Shyngys, KAZGUU University) covering the 2022 academic year: outbound Kazakh students to CIS countries, inbound CIS students to Kazakhstan, faculty exchange in both directions, hired (extrabudgetary-funded) foreign specialists by country/qualification/subject, bilateral cooperation agreements, joint projects, joint/double-degree programmes (SOP/VDP), and Kazakhstani university representative offices abroad.

### Strengths

- Directly education-specific (unlike UNDESA) and reasonably granular — covers students, faculty, and institutional cooperation in one document
- Covers both directions of mobility (inbound and outbound) for the same reference year, enabling direct comparison
- Includes qualitative detail not available elsewhere (e.g. subject-area breakdown of hired foreign specialists)

### Limitations

- Single academic year only (2022) — no time series from this source alone (though the National Report's CIS-country tables for 2021-2024 partially fill this gap)
- Original issuing agency/source document not stated in the translation — should be confirmed before external publication
- Several internal inconsistencies found and documented during processing: a qualification-composition mismatch likely misattributing Ukraine's figures to Tajikistan; ambiguity over whether the source's Table 1 (titled "academic mobility of Kazakh students" but describing foreign students in Kazakhstan) reflects a translation/labelling error

### Key indicators

- Students in HEIs by direction and country (enrolled vs. short-term mobility — these are different metrics, both present)
- Faculty exchange counts by country and direction
- Hired foreign specialists: count, online/offline split, qualification, subject area
- Bilateral agreements, joint projects, SOP/VDP counts, representative offices

### Initial observations

- Uzbekistan and Russia dominate every CIS-mobility metric in this source (students, hired specialists, agreements), consistent with their dominance in the UNDESA migrant-stock data and the National Report's CIS tables — three independent sources agree on this ranking, which increases confidence in it despite each source's individual limitations.
- Russia alone accounts for 2,053 of Kazakhstan's 3,172 total CIS bilateral agreements (65%) — a concentration considerably higher than its share of student mobility, suggesting the institutional cooperation layer (agreements) is even more Russia-centric than the student-flow layer.

### Questions raised

- Do this source's 2022 CIS figures reconcile with the National Report's own CIS tables (6.1.3, 6.1.10) for the same year? (Not yet cross-checked — a clear next step.)
- Is the original source document identifiable and obtainable in the original language, to resolve the Table 1 labelling ambiguity and the Ukraine/Tajikistan qualification mismatch?

---

## Source 4 — ENIC-Kazakhstan (Bologna Process Analytical Report 2023)

### What does this dataset contain?

The National Center for Higher Education Development's annual monitoring report on Bologna Process implementation (2023 edition). Primarily covers quality assurance, accreditation, and Bologna-parameter compliance — internationalisation-relevant content is present but sparse and narratively scattered rather than tabulated.

### Strengths

- Official, government-published, annual series (editions exist from at least 2018-2023, giving a potential multi-year source if revisited)
- Contains a few internationalisation data points not found elsewhere in this project: English-medium foreign student concentration by field (dominated by Health care, with India at 45.3% within that subset), the Scholarship Programme for Foreign Citizens (550 grants/year, 150 reserved for Central Asia), and Central Asian Higher Education Space (CAHES) bilateral university counts

### Limitations

- **This source was initially mis-scoped in this project** — an early extraction pulled general Bologna-monitoring statistics (enrolment, graduation, employment) that were not actually about foreign students/migration and had to be discarded once this was noticed
- Genuinely on-topic content is thin: roughly four data points across a ~140-page document
- The single country-level statistic available (India, 45.3%) has an unclear percentage base, flagged but not resolved

### Key indicators

- Total foreign students enrolled (single year snapshot, no time series)
- Scholarship Programme for Foreign Citizens (grants/year)
- English-medium foreign student field concentration
- CAHES bilateral university ties (institution count, not student count)

### Initial observations

- This source is best used as a single-point qualitative supplement (e.g. to corroborate the National Report's richer 2024 foreign-student figures) rather than as a standalone quantitative source for WP2 — its value is confirmatory, not primary.

### Questions raised

- Do earlier editions of this same annual report (2018-2022, not yet reviewed) contain a genuine foreign-student time series that this 2023 edition lacks? Worth a targeted check only if a specific gap needs filling, given the low yield found so far.
- Can India's "45.3%" figure be resolved (share of what exactly) by cross-referencing the National Report 2024's much more detailed India/medical-university breakdown (which does reconcile internally)?

---

## Source 5 — National Report Mobility (MNVO 2024)

### What does this dataset contain?

Section 6 ("Internationalisation of Higher and Postgraduate Education") of the National Report on the State and Development of the Higher Education System of the Republic of Kazakhstan for 2024, issued by the Ministry of Science and Higher Education (MNVO) / ENIC-Kazakhstan. By far the richest and most granular WP2 source: inbound and outbound academic mobility (2021-2024, by country/region/level/field/funding source), foreign students by level and region, faculty exchange, the Bolashak scholarship programme, intergovernmental/interdepartmental grants, the Research Internships programme, and Erasmus+/Jean Monnet/PPVO participation.

### Strengths

- Purpose-built internationalisation chapter, not a byproduct of a different reporting focus (unlike Source 4)
- Genuine multi-year time series (2021-2024) for most metrics, at country/region/level/field granularity simultaneously
- Internally cross-referenced tables allow arithmetic verification — most tables reconcile exactly, and where they do not, the mismatch is precise and traceable (see below)

### Limitations

- Extremely large source file (>20MB) — could not be fetched directly and was processed entirely from user-supplied screenshots, in batches; extraction is not yet complete and further sections likely remain
- **Multiple confirmed internal inconsistencies**, all documented with cross-references in the processed files:
  - 2023 outgoing-mobility total: 4,426 (Tables 6.1.1, 6.1.13) vs. 4,458 (Table 6.1.7) — now resolved in favour of 4,426, since two independent tables agree on it and its own 4-year cumulative reconciles exactly
  - Figure 6.1.4: an identical total (26,979) repeated across 2020-2023 for foreign students by level, changing only in 2024 — very likely a chart/label artifact, not yet confirmed against the original PDF
  - Narrative-text CIS/Europe foreign-student figures do not match the same metrics shown in Figure 6.1.5's chart, within the same report section
  - Table 6.1.19 (faculty exchange by country): at least three cells where the printed percentage does not match the printed count (e.g. Uzbekistan "0.8%" for 160 of 769, which should be ~20.8%)

### Key indicators

- Inbound/outbound mobility counts by year, country, region, level, field, delivery mode, funding source
- Foreign student totals by level and region, and by specific university (for the largest cohort, Indian medical students)
- Faculty exchange counts, qualification composition, and country/university-type breakdown
- Bolashak: status distribution, cumulative graduates by field/country/level, contractual obligation fulfilment
- Intergovernmental/interdepartmental grants: two distinct channels, by country
- Research Internships programme: full application-to-award funnel by field
- Erasmus+: ICM and PPVO project counts by EU country, Jean Monnet trend, notable first-time achievements (EMDM)

### Initial observations

- Kyrgyzstan overtook Russia as Kazakhstan's top single source of inbound mobility students in 2024 (411 vs. 219) — a notable shift, since Russia had been the CIS leader in earlier years across multiple sources (UNDESA migrant stock, the CIS report, and this same report's 2021-2023 columns).
- Outbound mobility to Poland and Turkey both grew substantially 2023-2024 (Poland 668→691; Turkey 619→792, regaining the top European destination spot), while outbound mobility to CIS countries fell 26% in the same period — a possible substitution effect (Kazakhstani students shifting from CIS to European destinations) worth investigating quantitatively once the merged dataset exists.
- The Bolashak programme's cumulative destination profile (UK/Ireland 45.5%, USA/Canada 28%) is almost the inverse of the national inbound-mobility profile (dominated by CIS and Asia) — Kazakhstan's own outbound elite scholarship recipients go overwhelmingly Anglophone-West, while inbound foreign students come overwhelmingly from the region. This asymmetry is a strong, evidence-backed candidate insight for the eventual WP2 report.
- Three independent grant/scholarship channels (Bolashak, intergovernmental Channel B, interdepartmental Channel A) all show Hungary and China as leading non-CIS/non-Western partner countries for outbound study — a pattern not obviously connected to the CIS-dominated inbound picture, suggesting Kazakhstan's inbound and outbound internationalisation strategies are oriented toward largely different partner-country sets.

### Questions raised

- Is the Kyrgyzstan-overtakes-Russia shift (2024) a one-year anomaly or the start of a trend? Only resolvable once/if a 2025 edition of this report becomes available.
- Does the apparent CIS-to-Europe outbound substitution hold up once broken down by funding source (state budget vs. self-funded) — i.e. is this a policy-driven shift or a self-funded-student preference shift?
- What is the actual expansion of "PPVO", and does resolving it change how this project should categorise the Erasmus+ data relative to ICM and Jean Monnet?
- Given the volume of unresolved arithmetic mismatches, would it be worth requesting the original PDF directly (rather than continuing via screenshots) to resolve them definitively, especially before any figure from this source appears in a client-facing report?
---

## Source 6 — MSHE Foreign University Partnerships & Branch Campuses (2025)

### What does this dataset contain?

A press-material/infographic package from the Ministry of Science and Higher Education of the Republic of Kazakhstan (MSHE RK), titled "Kazakhstan Opens the Doors of the World's Leading Universities" with an accompanying map infographic "Centres of Academic and Research Excellence," as republished by ratel.kz and other outlets (~December 2025, "2025 year-end results" framing). Covers foreign university branch campuses, strategic partnerships, double-degree arrangements, investment partners, and international student totals by country.

### Strengths

- Directly addresses a gap no other WP2 source covers: institutional-level partnerships (branch campuses, consortia, double-degree arrangements) rather than student/faculty flow counts
- Names specific universities, cities, investment partners, and construction status - highly concrete
- Includes a forward-looking government target (100,000 international students by 2029) useful for RQ7

### Limitations

- **This is a news republication of a government press release/infographic, not a primary document** - the original MSHE press-release URL and exact publication date are not confirmed independently
- The geographic map component required visual transcription rather than clean text extraction, carrying materially higher transcription risk (documented per-row in `Regional_Campus_Map_by_City_2025.xlsx`)
- **Contains an internal self-contradiction**: the source's own headline claims Asia overtook CIS as the top student-origin region in 2024, but its own printed figures show CIS (17,816) slightly above Asia (17,788) - the claim contradicts its own numbers
- **India's student count here (9,969) does not match the National Report 2024's India figure (12,020)** processed earlier in WP2 - a 2,051-student gap between two apparently official Kazakhstani sources, not yet reconciled

### Key indicators

- Partnership counts by type (branch campus, strategic partnership, consortium, double degree, certification centre) and by operational status (functioning / opening 2025 / opening 2026)
- Partner countries (11) and programme count (162) at branch campuses
- International students by top country of origin, and CIS-vs-Asia regional comparison
- QS Asia 2026 ranking participation (44 Kazakhstani universities, 10 new)

### Initial observations

- This source introduces partner countries not prominent in any other WP2 source - notably South Korea, Italy, and Hungary (via MGIMO/branch campus links) - suggesting the *institutional* partnership layer of internationalisation draws on a broader country set than the *student mobility* layer (which remains CIS/Asia-dominated per Sources 3 and 5).
- The government's 100,000-by-2029 target represents roughly 3x the current reported figure (35,057) - an aggressive growth target against which all other WP2 mobility findings (e.g. the recent decline in mobility-specific inbound numbers, Insight #8) should be read with some tension.

### Questions raised

- Which of the three conflicting India/CIS/Asia figures across WP2 sources (this source; National Report Figure 6.1.5; National Report narrative text) is closest to a verifiable ground truth, and can the original MSHE press release or a primary statistical release resolve this?
- Do the newly-visible partner countries (South Korea, Italy, Hungary) appear anywhere in the mobility-specific data (Sources 3, 5) at a scale proportionate to their institutional presence here, or is this a case of institutional partnership activity outpacing actual student flow?