import numpy as np
from statsmodels.tsa.stattools import acf as st_acf
from statsmodels.tsa.stattools import ccf as st_ccf
from statsmodels.tsa.stattools import pacf as st_pacf

from src.correlation import acf
from src.correlation import ccf
from src.correlation import pacf
from src.tests.test_base import BaseTester


class CorrelationTests(BaseTester):
    def setUp(self):
        self.acf = acf(self.data)
        self.pacf = pacf(self.data)
        self.ccf = ccf(self.data, np.array(self.data) + 1)

    def test_acf(self):
        np.testing.assert_array_almost_equal(self.acf, st_acf(self.data))

    def test_pacf(self):
        np.testing.assert_array_almost_equal(self.pacf, st_pacf(self.data))

    def test_ccf(self):
        np.testing.assert_array_almost_equal(
            self.ccf, st_ccf(self.data, np.array(self.data) + 1)
        )
