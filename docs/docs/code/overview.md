# Details about the tests

## Intro

!!! tldr "TL;DR"

    There are actually three really good libraries which implements these tests:

    - [`pmdarima`](https://alkaline-ml.com/pmdarima)
    - [`statsmodels`](https://www.statsmodels.org)
    - [`arch`](https://arch.readthedocs.io)

    These pachages all implement the statistical tests in a slightly different way.
    <br>
    No one library contains all of the listed packages.


## Tests

!!! details "Details"

    === "Test Info"

        | category           | algorithm                                                                     | library:test |
        |--------------------|-------------------------------------------------------------------------------|--------------|
        | Stationarity       | Augmented Dickey-Fuller test for stationarity (ADF)                           | `pmdarima`:[`ADFTest()`](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.ADFTest.html)<br>`statsmodels`:[`adfuller()`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html)<br>`arch`:[`ADF()`](https://arch.readthedocs.io/en/latest/unitroot/generated/arch.unitroot.ADF.html)
        | Stationarity       | Kwiatkowski-Phillips-Schmidt-Shin test for stationarity (KPSS)                | `pmdarima`:[`KPSSTest()`](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.KPSSTest.html)<br>`statsmodels`:[`kpss()`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.kpss.html)<br>`arch`:[`KPSS()`](https://arch.readthedocs.io/en/latest/unitroot/generated/arch.unitroot.KPSS.html)
        | Stationarity       | Phillips-Peron test for stationarity (PP)                                     | `pmdarima`:[`PPTest()`](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.PPTest.html)<br>`arch`:[`PhillipsPerron()`](https://arch.readthedocs.io/en/latest/unitroot/generated/arch.unitroot.PhillipsPerron.html)
        | Stationarity       | Range unit-root test for stationarity (RUR)                                   | `statsmodels`:[`range_unit_root_test()`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.range_unit_root_test.html)
        | Stationarity       | Zivot-Andrews structural-break unit-root test (ZA)                            | `statsmodels`:[`zivot_andrews()`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.zivot_andrews.html)<br>`arch`:[`ZivotAndrews()`](https://arch.readthedocs.io/en/latest/unitroot/generated/arch.unitroot.ZivotAndrews.html)
        | Seasonality        | Osborn-Chui-Smith-Birchenhall test of seasonality (OCSB)                      | `pmdarima`:[`OCSBTest()`](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.OCSBTest.html)
        | Seasonality        | Canova-Hansen test for seasonal differences (CH)                              | `pmdarima`:[`CHTest()`](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.CHTest.html)
        | Correlation        | Auto-Correlation (ACF)                                                        | `pmdarima`:[`acf()`](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.utils.acf.html)<br>`statsmodels`:[`acf()`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.acf.html)
        | Correlation        | Partial Auto-Correlation (PACF)                                               | `pmdarima`:[`pacf()`](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.utils.pacf.html)<br>`statsmodels`:[`pacf()`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.pacf.html)
        | Correlation        | Partial Auto-Correlation (PACF)                                               | `statsmodels`:[`ccf()`](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.ccf.html)
        | Correlation        | Ljung-Box test of autocorrelation in residuals (LB)                           | `statsmodels`:[`acorr_ljungbox()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.acorr_ljungbox.html)
        | Correlation        | Lagrange Multiplier tests for autocorrelation (LM)                            | `statsmodels`:[`acorr_lm()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.acorr_lm.html)
        | Correlation        | Breusch-Godfrey Lagrange Multiplier tests for residual autocorrelation (BGLM) | `statsmodels`:[`acorr_breusch_godfrey()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.acorr_breusch_godfrey.html)
        | Normality          | Jarque-Bera test of normality (JB)                                            | `statsmodels`:[`jarque_bera()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.stattools.jarque_bera.html)
        | Normality          | Omnibus test for normality (OB)                                               | `statsmodels`:[`omni_normtest()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.stattools.omni_normtest.html)
        | Linearity          | Harvey Collier test for linearity (HC)                                        | `statsmodels`:[`linear_harvey_collier()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.linear_harvey_collier.html)
        | Linearity          | Lagrange Multiplier test for linearity (LM)                                   | `statsmodels`:[`linear_lm()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.linear_lm.html)
        | Linearity          | Rainbow test for linearity (RB)                                               | `statsmodels`:[`linear_rainbow()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.linear_rainbow.html)
        | Linearity          | Ramsey's RESET test for neglected nonlinearity (RR)                           | `statsmodels`:[`linear_reset()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.linear_reset.html)
        | Heteroscedasticity | Engle's Test for Autoregressive Conditional Heteroscedasticity (ARCH)         | `statsmodels`:[`het_arch()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_arch.html)
        | Heteroscedasticity | Breusch-Pagan Lagrange Multiplier test for heteroscedasticity (BPL)           | `statsmodels`:[`het_breuschpagan()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_breuschpagan.html)
        | Heteroscedasticity | Goldfeld-Quandt test for homoskedasticity (GQ)                                | `statsmodels`:[`het_goldfeldquandt()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_goldfeldquandt.html)
        | Heteroscedasticity | White's Lagrange Multiplier Test for Heteroscedasticity (WLM)                 | `statsmodels`:[`het_white()`](https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_white.html)
        | Covariance         | ...                                                                           | 

    === "Python Import"

        | test | library:import |
        |------|----------------|
        | ADF  | pmdarima: `from pmdarima.arima import ADFTest`<br>statsmodels: `from statsmodels.tsa.stattools import adfuller`<br>arch: `from arch.unitroot import ADF`
        | KPSS | pmdarima: `from pmdarima.arima import KPSSTest`<br>statsmodels: `from statsmodels.tsa.stattools import kpss`<br>arch: `from arch.unitroot import KPSS`
        | PP   | pmdarima: `from pmdarima.arima import PPTest`<br>arch: `from arch.unitroot import PhillipsPerron`
        | RUR  | pmdarima: `from statsmodels.tsa.stattools import range_unit_root_test`
        | ZA   | pmdarima: `from statsmodels.tsa.stattools import zivot_andrews`<br> arch: `from arch.unitroot import ZivotAndrews`
        | OCSB | pmdarima: `from pmdarima.arima import OCSBTest`
        | CH   | pmdarima: `from pmdarima.arima import CHTest`
        | ACF  | pmdarima: `from pmdarima.utils import acf`<br>statsmodels: `from statsmodels.tsa.stattools import acf`
        | PACF | pmdarima: `from pmdarima.utils import pacf`<br>statsmodels: `from statsmodels.tsa.stattools import pacf`
        | CCF  | statsmodels: `from statsmodels.tsa.stattools import ccf`
        | LB   | statsmodels: `from statsmodels.stats.diagnostic import acorr_ljungbox`
        | LM   | statsmodels: `from statsmodels.stats.diagnostic import acorr_lm`
        | BGLM | statsmodels: `from statsmodels.stats.diagnostic import acorr_breusch_godfrey`
        | JB   | statsmodels: `from statsmodels.stats.stattools import jarque_bera`
        | OB   | statsmodels: `from statsmodels.stats.stattools import omni_normtest`
        | HC   | statsmodels: `from statsmodels.stats.diagnostic import linear_harvey_collier`
        | LM   | statsmodels: `from statsmodels.stats.diagnostic import linear_lm`
        | RB   | statsmodels: `from statsmodels.stats.diagnostic import linear_rainbow`
        | RR   | statsmodels: `from statsmodels.stats.diagnostic import linear_reset`
        | ARCH | statsmodels: `from statsmodels.stats.diagnostic import het_arch`
        | BPL  | statsmodels: `from statsmodels.stats.diagnostic import het_breuschpagan`
        | GQ   | statsmodels: `from statsmodels.stats.diagnostic import het_goldfeldquandt`
        | WLM  | statsmodels: `from statsmodels.stats.diagnostic import het_white`


<!-- 
| category     | algorithm                         | import script                         | url |
|--------------|-----------------------------------|---------------------------------------|-----|
| Stationarity | Augmented Dickey-Fuller           | `from pmdarima.arima import ADFTest`  | [ADF](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.ADFTest.html#pmdarima.arima.ADFTest)
| Stationarity | Kwiatkowski-Phillips-Schmidt-Shin | `from pmdarima.arima import KPSSTest` | [KPSS](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.KPSSTest.html)
| Stationarity | Phillips-Peron                    | `from pmdarima.arima import PPTest`   | [PP](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.PPTest.html)
| Seasonality  | Osborn-Chui-Smith-Birchenhall     | `from pmdarima.arima import OCSBTest` | [OCSB](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.OCSBTest.html)
| Seasonality  | Canova-Hansen                     | `from pmdarima.arima import CHTest`   | [CH](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.CHTest.html)
| Correlation  | Auto-Correlation                  | `from pmdarima.utils import acf`      | [ACF](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.utils.acf.html#pmdarima.utils.acf)
| Correlation  | Partial Auto-Ccorrelation         | `from pmdarima.utils import pacf`     | [PACF](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.utils.pacf.html)
-->



