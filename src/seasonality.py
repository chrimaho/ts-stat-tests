from typing import Dict, Union
from pmdarima.arima.arima import ARIMA
from pmdarima.arima.auto import auto_arima
from pmdarima.arima.seasonality import CHTest, OCSBTest
from statsmodels.tools.validation import array_like, bool_like
from typeguard import typechecked
import numpy as np
from scipy.stats import chi2
from src.correlation import acf

"""
For a really good article on CH & OCSB tests, check: [When A Time Series Only Quacks Like A Duck: Testing for Stationarity Before Running Forecast Models. With Python. And A Duckling Picture.](https://towardsdatascience.com/when-a-time-series-only-quacks-like-a-duck-10de9e165e)
"""

@typechecked
def qs(
    x: array_like,
    freq: int = 0,
    diff: bool_like = True,
    residuals: bool_like = False,
    autoarima: bool_like = True,
) -> Dict[str, Union[str, float, ARIMA, None]]:
    """
    Summary:
        Implement the `QS` Seasonality test.

    Params:
        x (array_like):
            The univariate time series data to test.
        freq (int, optional):
            The frequency of the time series data. Defaults to `0`.
        diff (bool_like, optional):
            Whether or not to run `np.diff()` over the data. Defaults to `True`.
        residuals (bool_like, optional):
            Whether or not to run & return the residuals from the function. Defaults to `False`.
        autoarima (bool_like, optional):
            Whether or not to run the `AutoARIMA()` algorithm over the data. Defaults to `True`.

    Raises:
        AttributeError:
            If `x` is empty, or `freq` is too low for the data to be adequately tested.
        ValueError:
            If, after differencing the data (by using `np.diff()`), any of the values are `None` (or `Null` or `np.nan`), then it cannot be used for QS Testing.

    Returns:
        Dict[str, Union[str,float,ARIMA,type(None)]]:
            The dictionary containing the information, attributes, and model from running the tests.

    ???+ Info "Details"
        This is a translation from the `R` language, which can be found in `qs()` function of the `seastests` package.
        For more details on the original function, see:
            - [github/seastests/qs.R](https://github.com/cran/seastests/blob/master/R/qs.R)
            - [rdrr/seastests/qs](https://rdrr.io/cran/seastests/man/qs.html)
            - [rdocumentation/seastests/qs](https://www.rdocumentation.org/packages/seastests/versions/0.15.4/topics/qs)
            - [Machine Learning Mastery/How to Identify and Remove Seasonality from Time Series Data with Python](https://machinelearningmastery.com/time-series-seasonality-with-python)
            - [StackOverflow/Simple tests for seasonality in Python](https://stackoverflow.com/questions/62754218/simple-tests-for-seasonality-in-python)

    ???+ Example "Examples"
        Basic usage:
        ```python linenums="1"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> qs(x=data, freq=12)
        {'stat': 194.4692892087745,
         'Pval': 5.90922325801522e-43,
         'test': 'QS',
         'model': None}
        ```
        Advanced usage:
        ```python linenums="1"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> qs(x=data, freq=12, diff=True, residuals=True, autoarima=True)
        {'stat': 101.85929391917927,
         'Pval': 7.612641184541459e-23,
         'test': 'QS',
         'model': ARIMA(order=(1, 1, 1), scoring_args={}, suppress_warnings=True)}
    """
    if x.isnull().all():
        raise AttributeError(f"All observations are NaN.")
    if diff and residuals:
        print(
            f"The differences of the residuals of a non-seasonal ARIMA model are computed and used."
            f"It may be better to either only take the differences or use the residuals."
        )
    if freq < 2:
        raise AttributeError(
            f"The number of observations per cycle is '{freq}', which is too small."
        )

    if residuals:
        if autoarima:
            max_order = 1 if freq < 8 else 3
            allow_drift = True if freq < 8 else False
            try:
                model = auto_arima(
                    y=x,
                    max_P=1,
                    max_Q=1,
                    max_p=3,
                    max_q=3,
                    seasonal=False,
                    stepwise=False,
                    max_order=max_order,
                    allow_drift=allow_drift,
                )
            except:
                try:
                    model = ARIMA(order=(0, 1, 1)).fit(y=x)
                except:
                    x = x
                    print(
                        f"Could not estimate any ARIMA model, original data series is used."
                    )
            else:
                x = model.resid()
        else:
            try:
                model = ARIMA(order=(0, 1, 1)).fit(y=x)
            except:
                x = x
                print(
                    f"Could not estimate any ARIMA model, original data series is used."
                )
            else:
                x = model.resid()
    else:
        model = None

    # Do diff
    y = np.diff(x) if diff else x

    # Pre-check
    if np.var(y[~np.isnan(y)]) == 0:
        raise ValueError(
            f"The Series is a constant (possibly after transformations)."
            f"QS-Test cannot be computed on constants."
        )

    # Test Statistic
    rho = acf(x=y, nlags=freq * 2, missing="drop")[[freq, freq * 2]]
    rho = np.array([0, 0]) if any(rho <= 0) else rho
    N = len(y[~np.isnan(y)])
    QS = N * (N + 2) * (rho[0] ** 2 / (N - freq) + rho[1] ** 2 / (N - freq * 2))
    Pval = chi2.sf(QS, 2)

    return {"stat": QS, "Pval": Pval, "test": "QS", "model": model}


@typechecked
def ocsb(x: array_like, m: int, lag_method: str = "aic", max_lag: int = 3):
    return OCSBTest(
        m=m, lag_method=lag_method, max_lag=max_lag
    ).estimate_seasonal_differencing_term(x)


@typechecked
def ch(x: array_like, m: int):
    return CHTest(m=m).estimate_seasonal_differencing_term(x)
