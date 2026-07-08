

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats

@dataclass
class LinearFitResult:
    slope: float
    intercept: float
    r_squared: float
    p_value: float

    def predict(self, x: np.ndarray | pd.Series) -> np.ndarray:
        x = np.asarray(x, dtype=float)
        return self.slope * x + self.intercept

def linear_fit(x: pd.Series | np.ndarray, y: pd.Series | np.ndarray) -> LinearFitResult:
    """Ordinary least-squares linear regression."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    slope, intercept, r, p, _ = stats.linregress(x, y)
    return LinearFitResult(slope=slope, intercept=intercept, r_squared=r**2, p_value=p)

def poly_fit(
    x: pd.Series | np.ndarray,
    y: pd.Series | np.ndarray,
    degree: int = 2,
) -> np.ndarray:
    """Return polynomial coefficients (highest power first)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if degree < 1:
        raise ValueError("degree must be >= 1")
    return np.polyfit(x, y, degree)
