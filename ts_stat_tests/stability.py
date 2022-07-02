import pandas as pd
from tsfeatures import stability as ts_stability


def stability(data: pd.Series) -> float:
    """
    Full creadit to: tsfeatures
    """
    return ts_stability(data)["stability"]


def is_stable(data: pd.Series, alpha: float = 0.5) -> bool:
    return True if stability(data) > alpha else False
