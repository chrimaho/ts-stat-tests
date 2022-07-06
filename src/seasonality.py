from pmdarima.arima import auto_arima, ARIMA
from statsmodels.tools.validation import array_like, bool_like
from typeguard import typechecked
import numpy as np
from scipy.stats import chi2
from src.correlation import acf


@typechecked
def qs(
    x: array_like,
    freq: int = 0,
    diff: bool_like = True,
    residuals: bool_like = False,
    autoarima: bool_like = True,
):

    if x.isnull().all():
        print(f"All observations are NaN.")
    if diff and residuals:
        print(
            f"The differences of the residuals of a non-seasonal ARIMA model are computed and used. It may be better to either only take the differences or use the residuals."
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
            f"The Series is a constant (possibly after transformations). QS-Test cannot be computed on constants."
        )

    # Test Statistic
    rho = acf(x=y, nlags=freq * 2, missing="drop")[[freq, freq * 2]]
    rho = np.array([0, 0]) if any(rho <= 0) else rho

    N = len(y[~np.isnan(y)])
    QS = N * (N + 2) * (rho[0] ** 2 / (N - freq) + rho[1] ** 2 / (N - freq * 2))

    Pval = chi2.sf(QS, 2)

    return {"stat": QS, "Pval": Pval, "test": "QS", "model": model}
