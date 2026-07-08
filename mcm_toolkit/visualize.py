

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

def plot_trend(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Trend",
    save_path: str | Path | None = None,
) -> Path | None:
    """Line plot for time-series or ordered x."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(df[x], df[y], marker="o", linewidth=1.5)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=150)
        plt.close(fig)
        return save_path
    plt.show()
    return None

def plot_scatter(
    df: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Scatter",
    save_path: str | Path | None = None,
) -> Path | None:
    """Scatter plot for bivariate exploration."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(df[x], df[y], alpha=0.75)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=150)
        plt.close(fig)
        return save_path
    plt.show()
    return None
