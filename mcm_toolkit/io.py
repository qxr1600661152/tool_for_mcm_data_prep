

from __future__ import annotations

from pathlib import Path

import pandas as pd

def load_table(path: str | Path, sheet: str | int = 0) -> pd.DataFrame:
    """Load CSV or Excel into a DataFrame."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet)
    raise ValueError(f"Unsupported format: {suffix}")

def save_table(df: pd.DataFrame, path: str | Path) -> Path:
    """Save DataFrame to CSV or Excel based on extension."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        df.to_csv(path, index=False, encoding="utf-8-sig")
    elif suffix in {".xlsx", ".xls"}:
        df.to_excel(path, index=False)
    else:
        raise ValueError(f"Unsupported format: {suffix}")
    return path
