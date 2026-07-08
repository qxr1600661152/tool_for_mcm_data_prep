

from __future__ import annotations

import pandas as pd

def fill_missing(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    """Fill numeric missing values; non-numeric columns left unchanged."""
    out = df.copy()
    numeric = out.select_dtypes(include="number")
    if strategy == "median":
        out[numeric.columns] = numeric.fillna(numeric.median(numeric_only=True))
    elif strategy == "mean":
        out[numeric.columns] = numeric.fillna(numeric.mean(numeric_only=True))
    elif strategy == "zero":
        out[numeric.columns] = numeric.fillna(0)
    else:
        raise ValueError("strategy must be median, mean, or zero")
    return out

def minmax_scale(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """Min-max normalize selected numeric columns to [0, 1]."""
    out = df.copy()
    cols = columns or list(out.select_dtypes(include="number").columns)
    for col in cols:
        lo, hi = out[col].min(), out[col].max()
        if hi == lo:
            out[col] = 0.0
        else:
            out[col] = (out[col] - lo) / (hi - lo)
    return out

def zscore(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """Z-score standardize selected numeric columns."""
    out = df.copy()
    cols = columns or list(out.select_dtypes(include="number").columns)
    for col in cols:
        mu = out[col].mean()
        sigma = out[col].std(ddof=0)
        out[col] = 0.0 if sigma == 0 else (out[col] - mu) / sigma
    return out
