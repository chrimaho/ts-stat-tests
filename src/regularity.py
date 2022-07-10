"""
As quoted from: https://www.machinelearningplus.com/time-series/time-series-analysis-python/

>   The more regular and repeatable patterns a time series has, the easier it is to forecast.
>   The 'Approximate Entropy' algorithm can be used to quantify the regularity and unpredictability of fluctuations in a time series.
>   The higher the approximate entropy, the more difficult it is to forecast it.
>   Another better alternate is the 'Sample Entropy'.
>   Sample Entropy is similar to approximate entropy but is more consistent in estimating the complexity even for smaller time series.
>   For example, a random time series with fewer data points can have a lower 'approximate entropy' than a more 'regular' time series, whereas, a longer random time series will have a higher 'approximate entropy'.

As such, the [`antropy`](https://raphaelvallat.com/antropy/build/html/index.html) package will be used to calculate these values
"""
from typing import Union

import numpy as np
from antropy import app_entropy as a_app_entropy
from antropy import sample_entropy as a_sample_entropy
from antropy import spectral_entropy as a_spectral_entropy
from statsmodels.tools.validation import array_like
from typeguard import typechecked


__all__ = ["entropy", "is_regular"]


@typechecked
def approx_entropy(x: array_like, order: int = 2, metric: str = "chebyshev") -> float:
    return a_app_entropy(x=x, order=order, metric=metric)


@typechecked
def sample_entropy(x: array_like, order: int = 2, metric: str = "chebyshev") -> float:
    return a_sample_entropy(x=x, order=order, metric=metric)


@typechecked
def spectral_entropy(
    x: array_like,
    sf: float = 1,
    method: str = "fft",
    nperseg: int = None,
    normalize: bool = False,
    axis: int = -1,
) -> float:
    return a_spectral_entropy(
        x=x, sf=sf, method=method, nperseg=nperseg, normalize=normalize, axis=axis
    )


@typechecked
def entropy(
    x: array_like,
    order: int = 2,
    sf: float = 1,
    metric: str = "chebyshev",
    algorithm: str = "sample",
    normalize: bool = True,
) -> float:
    sampl_options = ["sample", "sampl", "samp"]
    aprox_options = ["app", "aprox", "approx"]
    spect_options = ["spec", "spect", "spectral"]
    if algorithm in sampl_options:
        return sample_entropy(x=x, order=order, metric=metric)
    elif algorithm in aprox_options:
        return approx_entropy(x=x, order=order, metric=metric)
    elif algorithm in spect_options:
        return spectral_entropy(x=x, sf=sf, normalize=normalize)
    else:
        raise ValueError(
            f"Invalid option for `algorithm` parameter: {algorithm}.\n"
            f"For running the 'Sample Entropy' algorithm, use one of: {sampl_options}.\n"
            f"For running the 'Approximate Entropy' algorithm, use one of: {aprox_options}.\n"
            f"For running the 'Spectral Entropy' algorithm, use one of: {spect_options}."
        )


@typechecked
def is_regular(
    x: array_like,
    order: int = 2,
    sf: int = 1,
    metric: str = "chebyshev",
    algorithm: str = "sample",
    tolerance: Union[str, float, None] = "default",
    normalize: bool = True,
):
    if isinstance(tolerance, (float, int)):
        tol = tolerance
    elif tolerance in ["default", None]:
        tol = 0.2 * np.std(a=x)
    else:
        raise ValueError(
            f"Invalid option for `tolerance` parameter: {tolerance}.\n"
            f"Valid options are:\n"
            f"- Number with type `float`,\n"
            f"- String with value `default`,\n"
            f"- The value `None`."
        )
    value = entropy(
        x=x, order=order, sf=sf, metric=metric, algorithm=algorithm, normalize=normalize
    )
    result = True if value < tol else False
    return {"result": result, "entropy": value, "tolerance": tol}
