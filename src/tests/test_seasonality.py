import pandas as pd
from pmdarima.arima import ARIMA

from src.seasonality import ch, seasonal_strength, spikiness, trend_strength
from src.seasonality import ocsb
from src.seasonality import qs
from src.tests.test_base import BaseTester


class SeasonalityTests(BaseTester):
    def setUp(self):
        self.qs_result = qs(x=self.data, freq=12)
        self.ocsb_result = ocsb(x=self.data, m=12)
        self.ch_result = ch(x=self.data, m=12)
        self.seasonal_strength_result = seasonal_strength(x=self.data, m=12)
        self.trend_strength_result = trend_strength(x=self.data, m=12)
        self.spikiness_result = spikiness(x=self.data, m=12)

    def test_qs_defaults(self):
        self.assertIsInstance(self.qs_result, dict)
        self.assertListEqual(
            list(self.qs_result.keys()), ["stat", "Pval", "test", "model"]
        )
        self.assertIsInstance(self.qs_result["stat"], float)
        self.assertIsInstance(self.qs_result["Pval"], float)
        self.assertIsInstance(self.qs_result["test"], str)
        self.assertIsInstance(self.qs_result["model"], (dict, type(None), ARIMA))

    def test_qs(self):

        # To get the full list of necessary permutations, run:
        # >>> import itertools
        # >>> print(list(itertools.product(*[[True,False]]*3)))

        params = [
            (True, True, True, 101.85929391917927, 7.612641184541459e-23),
            (True, True, False, 131.44999855937297, 2.85756086669558e-29),
            (True, False, True, 194.4692892087745, 5.90922325801522e-43),
            (True, False, False, 194.4692892087745, 5.90922325801522e-43),
            (False, True, True, 132.58238294394926, 1.6221885995406117e-29),
            (False, True, False, 145.12096239944535, 3.071732627217893e-32),
            (False, False, True, 141.71278764765492, 1.6883370644788516e-31),
            (False, False, False, 141.71278764765492, 1.6883370644788516e-31),
        ]

        for diff, residuals, autoarima, expected_stat, expected_pval in params:
            qs_result = qs(
                x=self.data,
                freq=12,
                diff=diff,
                residuals=residuals,
                autoarima=autoarima,
            )
            self.assertAlmostEqual(qs_result["stat"], expected_stat, 5)
            self.assertAlmostEqual(qs_result["Pval"], expected_pval, 5)

    def test_qs_failures(self):
        with self.assertRaises(AttributeError):
            qs(pd.Series([None, None]), 12)
        with self.assertRaises(AttributeError):
            qs(self.data, 1)
        with self.assertRaises(ValueError):
            qs(pd.Series([1, 1]), 12, True, True, False)
        with self.assertRaises(ValueError):
            qs(pd.Series([0, 1]), 4, True, True, True)

    def test_ocsb(self):
        self.assertEqual(self.ocsb_result, 1)

    def test_ch(self):
        self.assertEqual(self.ch_result, 0)

    def test_seasonal_strength(self):
        self.assertAlmostEqual(self.seasonal_strength_result, 0.9815304216549953)
        self.assertEqual(seasonal_strength(self.data, 1), 0)
        self.assertEqual(seasonal_strength([1, 1], 2), 0)

    def test_trend_strength(self):
        self.assertAlmostEqual(self.trend_strength_result, 0.9971375301013928)
        self.assertEqual(trend_strength(self.data, 1), 0)
        self.assertEqual(trend_strength([1, 1], 2), 0)

    def test_spikiness(self):
        self.assertAlmostEqual(self.spikiness_result, 0.16276032794671697)
