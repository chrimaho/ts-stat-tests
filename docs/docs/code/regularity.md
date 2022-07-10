## Intro

!!! quote "As quoted by [Selva Prabhakaran](https://www.machinelearningplus.com/author/selva86/) on : [Time Series Analysis in Python: A Comprehensive Guide with Examples](https://www.machinelearningplus.com/time-series/time-series-analysis-python/)"

    The 'Approximate Entropy' algorithm can be used to quantify the regularity and unpredictability of fluctuations in a time series.

    The higher the approximate entropy, the more difficult it is to forecast it.

    Another better alternate is the 'Sample Entropy'.

    Sample Entropy is similar to approximate entropy but is more consistent in estimating the complexity even for smaller time series.
    For example, a random time series with fewer data points can have a lower 'approximate entropy' than a more 'regular' time series, whereas, a longer random time series will have a higher 'approximate entropy'.

As such, the [`antropy`](https://raphaelvallat.com/antropy/build/html/index.html) package will be used to calculate these values.


## Entropy Algo's

::: src.regularity
    selection:
        filters:
            - "_entropy"
    rendering:
        show_root_heading: false
        heading_level: 3
        show_if_no_docstrings: true
        member_order: source
