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
from antropy import app_entropy as a_app_entropy, sample_entropy as a_sample_entropy
import numpy as np
from statsmodels.tools.validation import array_like
from typeguard import typechecked


__all__ = ["entropy", "is_regular"]


def approx_entropy(x: array_like, order: int = 2, metric: str = "chebyshev") -> float:
    return a_app_entropy(x=x, order=order, metric=metric)


def sample_entropy(x: array_like, order: int = 2, metric: str = "chebyshev") -> float:
    return a_sample_entropy(x=x, order=order, metric=metric)


def entropy(
    x: array_like, order: int = 2, metric: str = "chebyshev", algorithm: str = "sample"
) -> float:
    sampl_options = ["sample", "sampl", "samp"]
    aprox_options = ["app", "aprox", "approx"]
    if algorithm in sampl_options:
        return sample_entropy(x=x, order=order, metric=metric)
    elif algorithm in aprox_options:
        return approx_entropy(x=x, order=order, metric=metric)
    else:
        raise ValueError(
            f"Invalid option for `algorithm` parameter: {algorithm}.\n"
            f"For running the 'Sample Entropy' algorithm, use one of: {sampl_options}.\n"
            f"Fur running the 'Approximate Entropy' algorithm, use one of: {aprox_options}. "
        )


@typechecked
def is_regular(
    x: array_like,
    order: int = 2,
    metric: str = "chebyshev",
    algorithm: str = "sample",
    tolerance: Union[str, float, None] = "default",
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
    value = entropy(x=x, order=order, metric=metric, algorithm=algorithm)
    result = True if value < tol else False
    return {"result": result, "entropy": value, "tolerance": tol}
