import pandas as pd
from tsfeatures import stability as ts_stability

# from src.utils.docstrings import overwrite_docs_from

# overwrite_docs_from(parent_function=ts_stability)
def stability(data: pd.Series, freq: int = 1) -> float:
    """
    !!! Summary
        Test for stability.

    Params:
        data (pd.Series):
            The time series.
        freq (int, optional):
            Frequency of the time series

    Returns:
        (float):
            Variance of the means of tiled windows.

    ??? Note
        For full documentation, see:

        - Python: [`tsfeatures`](https://github.com/Nixtla/tsfeatures/blob/master/tsfeatures/tsfeatures.py)
        - R: [`tsfeatures`](http://pkg.robjhyndman.com/tsfeatures/reference/lumpiness.html)

    ??? Example "Examples"
        Basic usage:
        ```python linenums="1"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> print(stability(data))
        12702.672087912088
        ```
    """
    return ts_stability(x=data, freq=freq)["stability"]


def is_stable(data: pd.Series, freq: int = 1, alpha: float = 0.5) -> bool:
    """
    !!! Summary
        Check whether a data series is stable or not.

    Params:
        data (pd.Series):
            The time series.
        freq (int, optional):
            The frequency of the time series. Defaults to `1`.
        alpha (float, optional):
            The value, above which, the data will be stable. Defaults to `0.5`.

    Returns:
        (bool):
            A confirmaiont of whether or nto the data is stable.

    ??? Note
        For full documentation, see:

        - Python: [`tsfeatures`](https://github.com/Nixtla/tsfeatures/blob/master/tsfeatures/tsfeatures.py)
        - R: [`tsfeatures`](http://pkg.robjhyndman.com/tsfeatures/reference/lumpiness.html)

    ??? Example "Examples"
        Basic usage:
        ```python linenums="1"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> print(is_stable(data))
        True
        ```
    """
    return True if stability(data=data, freq=freq) > alpha else False
