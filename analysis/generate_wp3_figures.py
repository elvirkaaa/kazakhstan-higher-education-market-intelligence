"""
Generate all WP3 figures from the processed data files in data/processed/wp3/.

Usage:
    python3 analysis/generate_wp3_figures.py

Outputs PNGs to reports/wp3/figures/images/. Every figure here reads its
numbers DIRECTLY from the processed XLSX files at run time (via openpyxl)
rather than from hardcoded/estimated values - re-running this script after
updating a source file will always reflect the current data, with no manual
number-editing required.

The one exception is figure_10 (the WP1 x WP3 cross-work-package comparison),
which combines a WP3 file value with a WP1 report figure that lives in a
different work package's report, not a WP3 processed file - those constants
are labelled clearly in that function.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#cccccc",
    "axes.linewidth": 0.8,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})
NAVY = "#0d1f42"
GOLD = "#b8860b"
LIGHT = "#5b7fb5"
GREY = "#8a8a8a"
RED = "#9b1c1c"

DATA = "data/processed/wp3"
OUT = "reports/wp3/figures/images"


def read_series(path, min_row=4):
    """Read a (label, value) time series from a processed WP3 xlsx file,
    stopping at the first row whose first cell is not numeric (the note row)."""
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb.active
    out = []
    for row in ws.iter_rows(min_row=min_row, values_only=True):
        if row[0] is None or not isinstance(row[0], (int, float)):
            break
        out.append((row[0], row[1]))
    return out


def figure_01_population_total():
    series = read_series(f"{DATA}/world_bank/KZ_Population_Total_1960_2024.xlsx")
    series = [(y, v) for y, v in series if y >= 1990]
    years, pop = zip(*series)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(years, pop, color=NAVY, linewidth=2)
    ax.fill_between(years, pop, min(pop) * 0.98, color=NAVY, alpha=0.06)
    ax.set_ylabel("Population")
    ax.set_title("Population of Kazakhstan, 1990-2025", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_01_population_total.png", dpi=160)
    plt.close()


def figure_02_population_projection():
    hist = read_series(f"{DATA}/world_bank/KZ_Population_Total_1960_2024.xlsx")
    last_hist_year, last_hist_pop = hist[-1]
    proj = read_series(f"{DATA}/un_wpp/KZ_UN_WPP_Population_Projection_2030_2050.xlsx")
    proj_years = [last_hist_year] + [y for y, v in proj]
    proj_pop = [last_hist_pop] + [v for y, v in proj]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot([last_hist_year], [last_hist_pop], marker="o", color=NAVY)
    ax.plot(proj_years, proj_pop, marker="o", color=GOLD, linewidth=2, linestyle="--")
    ax.axvline(last_hist_year, color=GREY, linestyle=":", linewidth=1)
    ax.text(last_hist_year + 0.3, last_hist_pop, f"Last observed ({int(last_hist_year)})", fontsize=8, color=GREY)
    for x, y in zip(proj_years, proj_pop):
        ax.annotate(f"{y/1e6:.1f}M", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9)
    ax.set_ylabel("Population")
    ax.set_title("Population Projection to 2050 (UN WPP, Medium-Fertility Variant)", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_02_population_projection.png", dpi=160)
    plt.close()


def figure_03_births_deaths_natural_increase():
    births = read_series(f"{DATA}/bns/KZ_Births_National_1991_2025.xlsx")
    deaths = read_series(f"{DATA}/bns/KZ_Deaths_National_1991_2025.xlsx")
    by, bv = zip(*births)
    dy, dv = zip(*deaths)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(by, bv, color=NAVY, linewidth=2, label="Births")
    ax.plot(dy, dv, color=RED, linewidth=2, label="Deaths")
    common_years = sorted(set(by) & set(dy))
    b_map = dict(births); d_map = dict(deaths)
    ax.fill_between(common_years, [b_map[y] for y in common_years], [d_map[y] for y in common_years],
                     color=GOLD, alpha=0.15, label="Natural increase")
    ax.set_ylabel("Persons")
    ax.set_title("Births, Deaths, and Natural Increase, 1991-2025", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.legend(frameon=False, loc="upper left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_03_births_deaths.png", dpi=160)
    plt.close()


def figure_04_population_growth_rate():
    series = read_series(f"{DATA}/world_bank/KZ_Population_Growth_Rate_1961_2024.xlsx")
    series = [(y, v) for y, v in series if y >= 1990]
    years, growth = zip(*series)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    colors = [RED if g < 0 else NAVY for g in growth]
    ax.bar(years, growth, color=colors, width=0.8)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_ylabel("Annual population growth (%)")
    ax.set_title("Annual Population Growth Rate, 1990-2025", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_04_growth_rate.png", dpi=160)
    plt.close()


def figure_05_age_pyramid():
    wb = openpyxl.load_workbook(f"{DATA}/un_wpp/KZ_Age_Pyramid_2025.xlsx", data_only=True)
    ws = wb.active
    rows = []
    for row in ws.iter_rows(min_row=4, values_only=True):
        if row[0] is None or not isinstance(row[0], str):
            break
        rows.append(row)  # (age_group, male, female, total)
    age_groups = [r[0] for r in rows]
    male = [-r[1] / 1000 for r in rows]
    female = [r[2] / 1000 for r in rows]
    y = np.arange(len(age_groups))
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.barh(y, male, color=NAVY, label="Male")
    ax.barh(y, female, color=GOLD, label="Female")
    ax.set_yticks(y)
    ax.set_yticklabels(age_groups, fontsize=8)
    ax.set_xlabel("Population (thousands)")
    ax.set_title("Kazakhstan Age Pyramid, 2025", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.legend(frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_05_age_pyramid.png", dpi=160)
    plt.close()


def figure_06_youth_cohort_trend():
    wb = openpyxl.load_workbook(f"{DATA}/un_wpp/KZ_Population_Age_15_24_1990_2026.xlsx", data_only=True)
    ws = wb.active
    rows = []
    for row in ws.iter_rows(min_row=4, values_only=True):
        if row[0] is None or not isinstance(row[0], (int, float)):
            break
        rows.append(row)  # (Year, 15-19, 20-24, 17-24 approx)
    years = [r[0] for r in rows]
    cohort = [r[3] for r in rows]  # the 15-19+20-24 combined column
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(years, cohort, marker=".", color=NAVY, linewidth=1.5)
    ax.axvspan(2024, max(years), color=GOLD, alpha=0.15)
    ax.text(2024.1, min(cohort), "Projected\nreversal", fontsize=9, color=GOLD, fontweight="bold")
    ax.set_ylabel("Population aged 15-24 (15-19 + 20-24 bands)")
    ax.set_title("Youth (15-24) Cohort Trend, 1990-2026", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_06_youth_cohort_trend.png", dpi=160)
    plt.close()


def figure_07_regional_population():
    wb = openpyxl.load_workbook(f"{DATA}/bns/KZ_Regional_Population_2025.xlsx", data_only=True)
    ws = wb.active
    rows = []
    for row in ws.iter_rows(min_row=4, values_only=True):
        if row[0] is None or not isinstance(row[0], str):
            break
        rows.append(row)  # (Region, Population)
    rows = [r for r in rows if "Total" not in r[0]]
    rows.sort(key=lambda r: r[1])
    top10 = rows[-10:]
    regions = [r[0] for r in top10]
    pop = [r[1] for r in top10]
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.barh(regions, pop, color=NAVY)
    ax.set_xlabel("Population (2025)")
    ax.set_title("Largest Regions by Population, 2025 (Top 10)", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_07_regional_population.png", dpi=160)
    plt.close()


def figure_08_net_migration():
    series = read_series(f"{DATA}/bns/KZ_External_Migration_Balance_National_2000_2025.xlsx")
    years, balance = zip(*series)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    colors = [RED if b < 0 else NAVY for b in balance]
    ax.bar(years, balance, color=colors, width=0.8)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.set_ylabel("Net external migration")
    ax.set_title("External Migration Balance (Net), 2000-2025", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_08_net_migration.png", dpi=160)
    plt.close()


def figure_09_dependency_ratio():
    series = read_series(f"{DATA}/un_wpp/KZ_Total_Dependency_Ratio_1990_2026.xlsx")
    years, ratio = zip(*series)
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(years, ratio, color=GOLD, linewidth=2)
    ax.set_ylabel("Dependents per 100 working-age")
    ax.set_title("Total Dependency Ratio, 1990-2026", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_09_dependency_ratio.png", dpi=160)
    plt.close()


def figure_10_supply_demand_mismatch():
    # Cross-work-package figure (WP1 x WP3) - see analysis/WP3_Insights.md, Insights #12-14.
    # WP3 values: read directly from data/processed/wp3/bns/KZ_Regional_Age_Structure_2024.xlsx
    wb = openpyxl.load_workbook(f"{DATA}/bns/KZ_Regional_Age_Structure_2024.xlsx", data_only=True)
    ws = wb.active
    youth_pct = {}
    for row in ws.iter_rows(min_row=4, values_only=True):
        if row[0] is None or not isinstance(row[0], str):
            break
        region, total, men, women, y0_15, work, pension = row
        if total:
            youth_pct[region] = round(100 * y0_15 / total, 1)

    # WP1 values: NOT in a WP3 file - taken from the WP1 report's regional supply table
    # (reports/wp1/Higher_Education_Landscape_Assessment.md, Table 9.1). Hardcoded here
    # because they belong to a different work package's report, not a WP3 data file.
    wp1_programme_share = {
        "Turkistan": 1.0, "Mangystau": 0.3, "Shymkent city": 1.3, "Kyzylorda": 0.3,
        "Atyrau": 0.2, "Almaty city": 71.6, "Shygys Kazakhstan": 10.0, "Pavlodar": 5.0,
    }
    labels_map = {"Turkistan": "Turkistan", "Mangystau": "Mangystau", "Shymkent city": "Shymkent city",
                  "Kyzylorda": "Kyzylorda", "Atyrau": "Atyrau", "Almaty city": "Almaty",
                  "Shygys Kazakhstan": "Ust-Kamenogorsk\n(East KZ)", "Pavlodar": "Pavlodar"}

    regions = list(wp1_programme_share.keys())
    programme_share = [wp1_programme_share[r] for r in regions]
    youth_share = [youth_pct[r] for r in regions]
    display_labels = [labels_map[r] for r in regions]

    fig, ax1 = plt.subplots(figsize=(10, 6))
    x = np.arange(len(regions))
    width = 0.35
    ax1.bar(x - width/2, programme_share, width, color=NAVY, label="Share of national HE programmes (WP1)")
    ax1.set_ylabel("Share of national HE programmes (%)", color=NAVY)
    ax1.set_xticks(x)
    ax1.set_xticklabels(display_labels, fontsize=9)
    ax1.tick_params(axis='y', labelcolor=NAVY)

    ax2 = ax1.twinx()
    ax2.bar(x + width/2, youth_share, width, color=GOLD, label="Share of population aged 0-15 (WP3)")
    ax2.axhline(youth_pct.get("Republic of Kazakhstan", 31.2), color=GREY, linestyle="--", linewidth=1)
    ax2.set_ylabel("Share of population aged 0-15 (%)", color=GOLD)
    ax2.tick_params(axis='y', labelcolor=GOLD)

    fig.suptitle("Higher-Education Supply vs. Youth Population Share, by Region", fontsize=13, fontweight="bold", color=NAVY, y=1.02)
    ax1.set_title("WP1 x WP3: regions with the youngest populations hold the smallest share of national HE supply", fontsize=9, color=GREY, loc="left")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, frameon=False, loc="upper center", fontsize=8, ncol=2, bbox_to_anchor=(0.5, -0.12))
    ax1.spines[["top"]].set_visible(False)
    ax2.spines[["top"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_10_supply_demand_mismatch.png", dpi=160, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    import os
    os.makedirs(OUT, exist_ok=True)
    figure_01_population_total()
    figure_02_population_projection()
    figure_03_births_deaths_natural_increase()
    figure_04_population_growth_rate()
    figure_05_age_pyramid()
    figure_06_youth_cohort_trend()
    figure_07_regional_population()
    figure_08_net_migration()
    figure_09_dependency_ratio()
    figure_10_supply_demand_mismatch()
    print("All 10 WP3 figures generated in", OUT)
