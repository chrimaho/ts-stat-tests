from typing import Optional
from typing import Tuple
from typing import Union

import numpy as np
from statsmodels.tools.validation import array_like
from statsmodels.tsa.stattools import acf as st_acf
from statsmodels.tsa.stattools import ccf as st_ccf
from statsmodels.tsa.stattools import pacf as st_pacf


def acf(
    x: array_like,
    adjusted: bool = False,
    nlags: int = None,
    qstat: bool = False,
    fft: bool = True,
    alpha: float = None,
    bartlett_confint: bool = True,
    missing: str = "none",
) -> Union[np.ndarray, Tuple[Union[np.ndarray, Optional[np.ndarray]]]]:
    return st_acf(
        x=x,
        adjusted=adjusted,
        nlags=nlags,
        qstat=qstat,
        fft=fft,
        alpha=alpha,
        bartlett_confint=bartlett_confint,
        missing=missing,
    )


def pacf(
    x: array_like, nlags: int = None, method: str = "ywadjusted", alpha: float = None
) -> Union[np.ndarray, Tuple[Union[np.ndarray, Optional[np.ndarray]]]]:
    return st_pacf(x=x, nlags=nlags, method=method, alpha=alpha)


def ccf(
    x: array_like, y: array_like, adjusted: bool = True, fft: bool = True
) -> np.ndarray:
    return st_ccf(x=x, y=y, adjusted=adjusted, fft=fft)
