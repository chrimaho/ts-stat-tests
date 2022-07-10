###
# !!! quote "As quoted by [Selva Prabhakaran](https://www.machinelearningplus.com/author/selva86/) on : [Time Series Analysis in Python: A Comprehensive Guide with Examples](https://www.machinelearningplus.com/time-series/time-series-analysis-python/)"
#
#     The 'Approximate Entropy' algorithm can be used to quantify the regularity and unpredictability of fluctuations in a time series.
#
#     The higher the approximate entropy, the more difficult it is to forecast it.
#
#     Another better alternate is the 'Sample Entropy'.
#
#     Sample Entropy is similar to approximate entropy but is more consistent in estimating the complexity even for smaller time series.
#     For example, a random time series with fewer data points can have a lower 'approximate entropy' than a more 'regular' time series, whereas, a longer random time series will have a higher 'approximate entropy'.
#
# As such, the [`antropy`](https://raphaelvallat.com/antropy/build/html/index.html) package will be used to calculate these values.
###
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
    """
    !!! Summary
        Approximate Entropy.

    Params:
        x (array_like):
            One-dimensional time series of shape (n_times).
        order (int, optional):
            Embedding dimension. Defaults to `2`.
        metric (str, optional):
            Name of the distance metric function used with [`sklearn.neighors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree). Default is to use the [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance). Defaults to `"chebyshev"`.

    Returns:
        (float):
            Approximate Entropy score.

    ???+ Info "Details"
        Approximate entropy is a technique used to quantify the amount of regularity and the unpredictability of fluctuations over time-series data. Smaller values indicates that the data is more regular and predictable.

        The tolerance value ($r$) is set to $0.2*std(x)$.

        Code adapted from the mne-features package by Jean-Baptiste Schiratti and Alexandre Gramfort.

    !!! Success "Credit"
        All credit goes to the [`AntroPy`](https://raphaelvallat.com/antropy/) library.

    ???+ Example "Examples"
        ```python linenums="1" title="Basic usage"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> approx_entropy(x=data)
        0.6451264780416452
        ```

    ??? Question "References"
        - Richman, J. S. et al. (2000). Physiological time-series analysis using approximate entropy and sample entropy. American Journal of Physiology-Heart and Circulatory Physiology, 278(6), H2039-H2049.
        - https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html

    ??? Tip "See Also"
        - [`sample_entropy()`][src.regularity.sample_entropy]
        - [`spectral_entropy()`][src.regularity.spectral_entropy]
    """
    return a_app_entropy(x=x, order=order, metric=metric)


@typechecked
def sample_entropy(x: array_like, order: int = 2, metric: str = "chebyshev") -> float:
    """
    !!! Summary
        Sample Entropy.

    Params:
        x (array_like):
            One-dimensional time series of shape (n_times).
        order (int, optional):
            Embedding dimension. Defaults to `2`.
        metric (str, optional):
            Name of the distance metric function used with [`sklearn.neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree). Default is to use the [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance). Defaults to `"chebyshev"`.

    Returns:
        (float):
            _description_

    ???+ Info "Details"
        Sample entropy is a modification of approximate entropy, used for assessing the complexity of physiological time-series signals. It has two advantages over approximate entropy: data length independence and a relatively trouble-free implementation. Large values indicate high complexity whereas smaller values characterize more self-similar and regular signals.

        The sample entropy of a signal $x$ is defined as:

        $$
        H(x, m, r) = -\\log\\frac{C(m + 1, r)}{C(m, r)}
        $$

        Where:

        - $m$ is the embedding dimension ($=$ order),
        - $r$ is the radius of the neighbourhood (default = $0.2*std(x)$),
        - $C(m+1,r)$ is the number of embedded vectors of length $m$+1 having a [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance) inferior to $r$ and
        - $C(m,r)$ is the number of embedded vectors of length $m$ having a [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance) inferior to $r$.

        Note that if `metric == 'chebyshev'` and `len(x) < 5000` points, then the sample entropy is computed using a fast custom Numba script. For other distance metric or longer time-series, the sample entropy is computed using a code from the [`mne-features`](https://mne.tools/mne-features/) package by Jean-Baptiste Schiratti and Alexandre Gramfort (requires sklearn).

    !!! Success "Credit"
        All credit goes to the [`AntroPy`](https://raphaelvallat.com/antropy/) library.

    ???+ Example "Examples"
        ```python linenums="1" title="Basic usage"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> sample_entropy(x=data)
        0.6177074729583698
        ```

    ??? Question "References"
        - Richman, J. S. et al. (2000). Physiological time-series analysis using approximate entropy and sample entropy. American Journal of Physiology-Heart and Circulatory Physiology, 278(6), H2039-H2049.
        - https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html

    ??? Tip "See Also"
        - [`approx_entropy()`][src.regularity.approx_entropy]
        - [`spectral_entropy()`][src.regularity.spectral_entropy]
    """
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
    """
    !!! Summary
        Spectral Entropy

    Params:
        x (array_like):
            `1-D` or `N-D` data array.
        sf (float, optional):
            Sampling frequency, in Hz. Defaults to `1`.
        method (str, optional):
            Spectral estimation method:

            - `'fft'`: Fourier Transformation ([`scipy.signal.periodogram()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html#scipy.signal.periodogram))
            - `'welch'`: Welch periodogram ([`scipy.signal.welch()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html#scipy.signal.welch))

            Defaults to `"fft"`.
        nperseg (int, optional):
            Length of each FFT segment for Welch method. If `None`, uses `scipy`'s default of 256 samples. Defaults to `None`.
        normalize (bool, optional):
            If `True`, divide by $log2(psd.size)$ to normalize the spectral entropy to be between $0$ and $1$. Otherwise, return the spectral entropy in bit. Defaults to `False`.
        axis (int, optional):
            The axis along which the entropy is calculated. Default is the last axis. Defaults to `-1`.

    Returns:
        (float):
            Spectral Entropy score.

    ???+ Info "Details"
        Spectral Entropy is defined to be the Shannon entropy of the power spectral density (PSD) of the data:

        $$
        H(x, sf) =  -\\sum_{f=0}^{f_s/2} P(f) \\log_2[P(f)]
        $$

        Where $P$ is the normalised PSD, and $f_s$ is the sampling frequency.

    !!! Success "Credit"
        All credit goes to the [`AntroPy`](https://raphaelvallat.com/antropy/) library.

    ???+ Example "Examples"
        ```python linenums="1"  title="Basic usage"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> spectral_entropy(x=data, sf=1)
        2.6538040647031726
        ```
        ```python linenums="1"  title="Advanced usage"
        >>> from sktime.datasets import load_airline
        >>> data = load_airline()
        >>> spectral_entropy(data, 2, 'welch', normalize=True)
        0.3371369604224553
        ```

    ??? Question "References"
        - Inouye, T. et al. (1991). Quantification of EEG irregularity by use of the entropy of the power spectrum. Electroencephalography and clinical neurophysiology, 79(3), 204-210.
        - https://en.wikipedia.org/wiki/Spectral_density
        - https://en.wikipedia.org/wiki/Welch%27s_method

    ??? Tip "See Also"
        - [`approx_entropy()`][src.regularity.approx_entropy]
        - [`sample_entropy()`][src.regularity.sample_entropy]
    """
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
