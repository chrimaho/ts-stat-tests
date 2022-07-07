# `ts-stat-tests`: Time Series Statistical Tests

<!-- [![pypi](https://img.shields.io/pypi/v/ts-eval)](https://pypi.org/project/ts-eval/) -->
<!-- [![python3](https://img.shields.io/pypi/pyversions/ts-eval)](https://www.python.org/downloads/release/python-3105/) -->
[![unit tests](https://github.com/chrimaho/ts-stat-tests/actions/workflows/codecov.yml/badge.svg)](https://github.com/chrimaho/ts-stat-tests/actions/workflows/codecov.yml)
[![codecov](https://codecov.io/gh/chrimaho/ts-stat-tests/branch/main/graph/badge.svg)](https://codecov.io/gh/chrimaho/ts-stat-tests)
[![docs ci](https://github.com/chrimaho/ts-stat-tests/actions/workflows/docs-ci.yml/badge.svg)](https://github.com/chrimaho/ts-stat-tests/actions/workflows/docs-ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/pypi/l/ts-eval)](https://github.com/vshulyak/ts-eval/blob/master/LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/chrimaho/ts-stat-tests/issues)


## Motivation

Time Series Analysis has been around for a long time, especially for doing Statistical Testing. Some Python packages are going a long way to make this even easier than it has ever been before. Such as [`sktime`](https://sktime.org/) and [`pycaret`](https://pycaret.org/) and [`pmdarima`](https://www.google.com/search?q=pmdarima) and [`statsmodels`](https://www.statsmodels.org/).

There are some typical Statistical Tests which are accessible in these Python ([QS](#), [Normality](#), [Stability](#), etc). However, there are still some statistical tests which are not yet ported over to Python, but which have been written in R and are quite stable.

Moreover, there is no one single library package for doing time-series statistical tests in Python.

That's exactly what this package aims to achieve.

A single package for doing all the standard time-series statistical tests.


## Tests

Full credit goes to the packages listed in this table.

type | name | source package | source language | implemented
---|---|---|---|---
correlation | acf | `statsmodels` | python | :white_check_mark:
correlation | pacf | `statsmodels` | python | :white_check_mark:
correlation | ccf | `statsmodels` | python | :white_check_mark:
stability | stability | `tsfeatures` | python | :white_check_mark:
stability | lumpiness | `tsfeatures` | python | :white_check_mark:
suitability | white-noise (ljung-box) | `` | python | :white_large_square:
stationarity | adf | `` | python | :white_large_square:
stationarity | kpss | `` | python | :white_large_square:
normality | shapiro | `` | python | :white_large_square:
seasonality | qs | `` |  | :white_large_square:
seasonality | seasonal strength | `` |  | :white_large_square:
regularity | regularity | `` |  | :white_large_square:


## Known limitations

- These listed tests is not exhaustive, and there is probably some more that could be added. Therefore, we encourage you to raise issues or pull requests to add more statistical tests to this suite.
- This package does not re-invent any of these tests. It merely calls the underlying packages, and calls the functions which are already written elsewhere.
