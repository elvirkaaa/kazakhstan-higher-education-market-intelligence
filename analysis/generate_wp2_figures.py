"""
Generate all WP2 figures from the processed data files in data/processed/wp2/.

Usage:
    python3 analysis/generate_wp2_figures.py

Outputs PNGs to reports/wp2/figures/images/, matching the files referenced by
the Figure_XX.md documentation wrappers in reports/wp2/figures/.

Run this script again after any update to the underlying processed XLSX files
to regenerate all figures with the latest numbers. Figures are built directly
from the values documented in the corresponding processed files under
data/processed/wp2/ — if you update those files, update the hardcoded values
below to match before re-running.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

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

OUT = "reports/wp2/figures/images"

years = [2021, 2022, 2023, 2024]


def figure_01_mobility_trend():
    incoming = [1971, 1582, 1226, 1207]
    outgoing = [3246, 3613, 4426, 4416]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(years, incoming, marker="o", color=NAVY, linewidth=2, label="Incoming mobility")
    ax.plot(years, outgoing, marker="o", color=GOLD, linewidth=2, label="Outgoing mobility")
    for x, y in zip(years, incoming):
        ax.annotate(f"{y:,}", (x, y), textcoords="offset points", xytext=(0, -16), ha="center", fontsize=9, color=NAVY)
    for x, y in zip(years, outgoing):
        ax.annotate(f"{y:,}", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9, color=GOLD)
    ax.set_xticks(years)
    ax.set_ylabel("Students")
    ax.set_title("Academic Mobility: Incoming vs Outgoing, 2021-2024", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.legend(frameon=False, loc="upper left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_01_mobility_trend.png", dpi=160)
    plt.close()


def figure_02_outbound_by_region():
    regions = ["Europe", "CIS", "South/SE Asia", "Americas", "Middle East", "Africa"]
    data_by_year = {
        2021: [1282, 1812, 139, 10, 3, 0],
        2022: [1695, 1602, 289, 24, 2, 1],
        2023: [2143, 1902, 326, 40, 13, 2],
        2024: [2360, 1402, 598, 56, 0, 0],
    }
    colors = [NAVY, GOLD, LIGHT, "#7a9e7e", GREY, "#c99a3e"]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    bottom = np.zeros(4)
    years_arr = np.array(years)
    for i, region in enumerate(regions):
        vals = np.array([data_by_year[y][i] for y in years])
        ax.bar(years_arr, vals, bottom=bottom, color=colors[i], label=region, width=0.55)
        bottom += vals
    ax.set_xticks(years)
    ax.set_ylabel("Students")
    ax.set_title("Outgoing Academic Mobility by Region, 2021-2024", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.legend(frameon=False, loc="upper left", fontsize=9, ncol=2)
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_02_outbound_by_region.png", dpi=160)
    plt.close()


def figure_03_top_countries_comparison():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5))

    inbound_countries = ["Kyrgyzstan", "Russia", "China", "Uzbekistan", "Japan"]
    inbound_vals = [411, 219, 114, 59, 22]
    axes[0].barh(inbound_countries[::-1], inbound_vals[::-1], color=NAVY)
    axes[0].set_title("Top Inbound Source Countries (2024)", fontsize=11, fontweight="bold", color=NAVY, loc="left")
    axes[0].spines[["top", "right"]].set_visible(False)

    outbound_countries = ["Turkey", "Poland", "Russia", "South Korea", "Germany"]
    outbound_vals = [792, 691, 594, 238, 193]
    axes[1].barh(outbound_countries[::-1], outbound_vals[::-1], color=GOLD)
    axes[1].set_title("Top Outbound Destination Countries (2024)", fontsize=11, fontweight="bold", color=GOLD, loc="left")
    axes[1].spines[["top", "right"]].set_visible(False)

    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_03_top_countries_comparison.png", dpi=160)
    plt.close()


def figure_04_bolashak_vs_inbound_asymmetry():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5))

    bolashak_labels = ["UK & Ireland", "USA & Canada", "Europe", "Asia & Oceania", "Russia"]
    bolashak_vals = [45.5, 28, 11.7, 7.9, 6.9]
    axes[0].pie(bolashak_vals, labels=bolashak_labels, autopct="%1.0f%%",
                colors=[NAVY, GOLD, LIGHT, "#7a9e7e", GREY], textprops={"fontsize": 9})
    axes[0].set_title("Bolashak Cumulative Graduates\nby Destination", fontsize=11, fontweight="bold", color=NAVY)

    inbound_labels = ["CIS", "South/SE Asia", "Europe", "Americas", "Other"]
    inbound_vals2 = [788, 181, 221, 10, 7]
    axes[1].pie(inbound_vals2, labels=inbound_labels, autopct="%1.0f%%",
                colors=[GOLD, NAVY, LIGHT, "#7a9e7e", GREY], textprops={"fontsize": 9})
    axes[1].set_title("2024 Incoming Mobility\nby Region of Origin", fontsize=11, fontweight="bold", color=GOLD)

    plt.suptitle("Elite Outbound (Bolashak) vs. General Inbound: An Asymmetry", fontsize=12, fontweight="bold", color=NAVY, y=1.02)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_04_bolashak_vs_inbound_asymmetry.png", dpi=160)
    plt.close()


def figure_05_indian_students_by_university():
    unis = ["Al-Farabi KazNU", "Karaganda Medical", "S.D. Asfendiyarov KazNMU", "Caspian Public",
            "South KZ Medical Academy", "Semey Medical", "Univ. of Intl Business",
            "W. KZ Medical (Ospanov)", "KazRos Medical", "Astana Medical",
            "Kokshetau Univ.", "N. Kazakhstan Univ."]
    vals = [483, 2746, 2194, 1284, 2480, 536, 767, 686, 205, 267, 274, 75]
    order = np.argsort(vals)
    unis_sorted = [unis[i] for i in order]
    vals_sorted = [vals[i] for i in order]

    fig, ax = plt.subplots(figsize=(9, 6.5))
    ax.barh(unis_sorted, vals_sorted, color=NAVY)
    ax.set_xlabel("Indian students (2024)")
    ax.set_title("Indian Students by University (2024)", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_05_indian_students_by_university.png", dpi=160)
    plt.close()


def figure_06_erasmus_growth():
    ppvo_years = [2022, 2023, 2024]
    ppvo_vals = [38, 47, 64]
    jm_years = [2021, 2022, 2023, 2024]
    jm_vals = [18, 19, 35, 53]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(ppvo_years, ppvo_vals, marker="o", color=NAVY, linewidth=2, label="PPVO applications submitted")
    ax.plot(jm_years, jm_vals, marker="s", color=GOLD, linewidth=2, label="Jean Monnet applications submitted")
    ax.set_xticks([2021, 2022, 2023, 2024])
    ax.set_ylabel("Applications submitted")
    ax.set_title("Erasmus+ Engagement Growth, 2021-2024", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.legend(frameon=False, loc="upper left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_06_erasmus_growth.png", dpi=160)
    plt.close()


def figure_07_recognition_applications():
    rec_years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    rec_vals = [10524, 16003, 22180, 15386, 22228, 23372, 18717, 15855, 18557]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.bar(rec_years, rec_vals, color=NAVY, width=0.6)
    ax.set_ylabel("Applications received")
    ax.set_title("Recognition/Nostrification Applications, 2017-2025", fontsize=13, fontweight="bold", color=NAVY, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.savefig(f"{OUT}/figure_07_recognition_applications.png", dpi=160)
    plt.close()


if __name__ == "__main__":
    import os
    os.makedirs(OUT, exist_ok=True)
    figure_01_mobility_trend()
    figure_02_outbound_by_region()
    figure_03_top_countries_comparison()
    figure_04_bolashak_vs_inbound_asymmetry()
    figure_05_indian_students_by_university()
    figure_06_erasmus_growth()
    figure_07_recognition_applications()
    print("All 7 WP2 figures generated in", OUT)