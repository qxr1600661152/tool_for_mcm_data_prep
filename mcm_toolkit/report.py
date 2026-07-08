

from __future__ import annotations

import pandas as pd

def describe_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Extended describe with missing count and missing rate."""
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        return pd.DataFrame()
    base = numeric.describe().T
    base["missing"] = numeric.isna().sum()
    base["missing_rate"] = numeric.isna().mean()
    return base

def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Pearson correlation for numeric columns."""
    numeric = df.select_dtypes(include="number")
    if numeric.shape[1] < 2:
        return pd.DataFrame()
    return numeric.corr(method="pearson")
