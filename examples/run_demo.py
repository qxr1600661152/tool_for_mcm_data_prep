

import sys
from pathlib import Path

ROOT_PKG = Path(__file__).resolve().parents[1]
if str(ROOT_PKG) not in sys.path:
    sys.path.insert(0, str(ROOT_PKG))

from mcm_toolkit.fit import linear_fit
from mcm_toolkit.io import load_table, save_table
from mcm_toolkit.preprocess import fill_missing, minmax_scale
from mcm_toolkit.report import correlation_matrix, describe_numeric
from mcm_toolkit.visualize import plot_scatter, plot_trend

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"

def main() -> None:
    OUT.mkdir(exist_ok=True)
    df = load_table(ROOT / "sample_data.csv")
    df = fill_missing(df, strategy="median")
    stats = describe_numeric(df)
    corr = correlation_matrix(df)
    scaled = minmax_scale(df, columns=["gdp_index", "energy_use"])

    fit = linear_fit(df["year"], df["gdp_index"])
    print("Linear fit: slope={:.3f}, R^2={:.3f}".format(fit.slope, fit.r_squared))
    print(stats)
    print(corr)

    plot_trend(df, "year", "gdp_index", title="GDP index trend", save_path=OUT / "trend.png")
    plot_scatter(scaled, "gdp_index", "energy_use", title="Scaled scatter", save_path=OUT / "scatter.png")
    save_table(stats.reset_index().rename(columns={"index": "column"}), OUT / "summary.csv")
    print(f"Outputs written to {OUT}")

if __name__ == "__main__":
    main()
