import pandas as pd

from mcm_toolkit.preprocess import fill_missing, minmax_scale, zscore

def test_fill_missing_median():
    df = pd.DataFrame({"a": [1.0, None, 3.0], "b": ["x", "y", "z"]})
    out = fill_missing(df, strategy="median")
    assert out["a"].tolist() == [1.0, 2.0, 3.0]
    assert out["b"].tolist() == ["x", "y", "z"]

def test_minmax_scale():
    df = pd.DataFrame({"x": [0.0, 5.0, 10.0]})
    out = minmax_scale(df)
    assert out["x"].tolist() == [0.0, 0.5, 1.0]

def test_zscore_constant_column():
    df = pd.DataFrame({"x": [3.0, 3.0, 3.0]})
    out = zscore(df)
    assert out["x"].tolist() == [0.0, 0.0, 0.0]
