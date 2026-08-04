# Methodology

---

# Purpose

This document describes the methodological approach used throughout the project.

The objective is to ensure that all analyses are transparent, reproducible and based on reliable data sources.

---

# Research Design

This project follows an evidence-based analytical approach by integrating multiple datasets related to Kazakhstan's higher education sector.

The analysis combines descriptive statistics, comparative analysis and exploratory data analysis to identify trends, patterns and relationships across institutional, demographic and economic indicators.

---

# Analytical Workflow

The project follows nine analytical stages.

## Stage 1 — Research Planning

- Define research objectives
- Identify analytical questions
- Define project scope

---

## Stage 2 — Data Collection

Data are collected from official and publicly available sources.

Examples include:

- UNESCO UIS
- Bureau of National Statistics
- TALDAU
- World Bank
- OECD
- Ministry of Science and Higher Education
- University websites

---

## Stage 3 — Data Validation

Each dataset is evaluated according to:

- completeness
- reliability
- consistency
- update frequency
- source credibility

---

## Stage 4 — Data Cleaning

Typical preprocessing includes:

- duplicate removal
- missing value assessment
- standardisation
- formatting
- variable harmonisation

---

## Stage 5 — Data Integration

Datasets are merged where appropriate using common identifiers such as:

- university
- region
- academic year
- indicator

---

## Stage 6 — Exploratory Data Analysis

The project investigates:

- distributions
- trends
- regional differences
- international comparisons
- institutional characteristics

---

## Stage 7 — Visualisation

Results are presented using:

- dashboards
- charts
- maps
- summary tables

---

## Stage 8 — Interpretation

Analytical findings are interpreted in relation to:

- higher education policy
- demographic development
- internationalisation
- labour market

---

## Stage 9 — Reporting

The final outputs include:

- analytical reports
- dashboards
- datasets
- documentation
- executive summaries

---

# Data Quality Principles

The project follows five principles.

- Transparency
- Reproducibility
- Traceability
- Consistency
- Evidence-based interpretation

---

# Limitations

Some datasets may differ in:

- reporting methodology
- update frequency
- geographical coverage
- indicator definitions

These limitations are documented whenever relevant.

---
---

## WP3 – Demographic Analysis

### Research Design

WP3 follows the same evidence-first approach as WP1 and WP2: every dataset is documented and verified before use. Given this work package draws on three distinct official sources (BNS, UN WPP, World Bank) covering overlapping metrics (e.g. population growth appears in both BNS and World Bank data), cross-source verification is a required step before any figure is finalised, following the same method used in WP2 (see WP2's Kyrgyzstan/India cross-checks for the template).

### Data Sources

See the WP3 section of `Data_Sources.md` for full detail. In summary: BNS (national demographic statistics), UN WPP (population projections), World Bank (international comparators).

### Data Cleaning

- Each BNS source table is split into a national time series and a regional long-format table (Region, Year, Value), consistent with the WP1/WP2 one-table-per-file convention
- Region names are normalised where Cyrillic look-alike characters were found in the source (documented per-file)
- Dash ("-") values are preserved as missing, not converted to zero, particularly for regions created after 2000

### Validation

- Cross-check BNS and World Bank population totals for Kazakhstan where both exist, to confirm they align (not yet done - see Data_Inventory for status)
- Cross-check the Worldometer-transcribed UN WPP projection figures against a direct UN WPP download once obtained

### Integration

A region-name crosswalk (mapping each source's naming convention to one canonical region name) should be built before WP3's regional data is merged with WP1/WP2 regional findings.

### Limitations

See the WP3 section of `Data_Sources.md` for source-specific limitations. Cross-cutting: WP3 explicitly excludes international student mobility and academic migration (Bolashak, Erasmus+, foreign students) - these remain in WP2. WP3 covers only general population and migration context.