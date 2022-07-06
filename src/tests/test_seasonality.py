import numpy as np
import pandas as pd
from src.tests.test_base import BaseTester
from src.seasonality import qs
from pmdarima.arima import ARIMA

from src.utils.dict_helpers import dict_slice_by_keys


class SeasonalityTests(BaseTester):
    def setUp(self):
        self.qs_result = qs(self.data, freq=12)

    def test_qs(self):

        self.assertIsInstance(self.qs_result, dict)
        self.assertListEqual(
            list(self.qs_result.keys()), ["stat", "Pval", "test", "model"]
        )
        self.assertIsInstance(self.qs_result["stat"], float)
        self.assertIsInstance(self.qs_result["Pval"], float)
        self.assertIsInstance(self.qs_result["test"], str)
        self.assertIsInstance(self.qs_result["model"], (dict, type(None), ARIMA))

        # To get the full list of necessary permutations, run:
        # >>> import itertools
        # >>> print(list(itertools.product(*[[True,False]]*3)))

        self.assertDictEqual(
            dict_slice_by_keys(qs(self.data, 12, True, True, True), ["stat", "Pval"]),
            {"stat": 101.85929391917927, "Pval": 7.612641184541459e-23},
        )

        self.assertDictEqual(
            dict_slice_by_keys(qs(self.data, 12, True, True, False), ["stat", "Pval"]),
            {"stat": 131.44999855937297, "Pval": 2.85756086669558e-29},
        )

        self.assertDictEqual(
            dict_slice_by_keys(qs(self.data, 12, True, False, True), ["stat", "Pval"]),
            {"stat": 194.4692892087745, "Pval": 5.90922325801522e-43},
        )

        self.assertDictEqual(
            dict_slice_by_keys(qs(self.data, 12, True, False, False), ["stat", "Pval"]),
            {"stat": 194.4692892087745, "Pval": 5.90922325801522e-43},
        )

        self.assertDictEqual(
            dict_slice_by_keys(qs(self.data, 12, False, True, True), ["stat", "Pval"]),
            {"stat": 132.58238294394926, "Pval": 1.6221885995406117e-29},
        )

        self.assertDictEqual(
            dict_slice_by_keys(qs(self.data, 12, False, True, False), ["stat", "Pval"]),
            {"stat": 145.12096239944535, "Pval": 3.071732627217893e-32},
        )

        self.assertDictEqual(
            dict_slice_by_keys(qs(self.data, 12, False, False, True), ["stat", "Pval"]),
            {"stat": 141.71278764765492, "Pval": 1.6883370644788516e-31},
        )

        self.assertDictEqual(
            dict_slice_by_keys(
                qs(self.data, 12, False, False, False), ["stat", "Pval"]
            ),
            {"stat": 141.71278764765492, "Pval": 1.6883370644788516e-31},
        )

    def test_qs_failures(self):
        with self.assertRaises(AttributeError):
            qs(pd.Series([None, None]), 12)
        with self.assertRaises(AttributeError):
            qs(self.data, 1)
        with self.assertRaises(ValueError):
            qs(pd.Series([1, 1]), 12, True, True, False)
        with self.assertRaises(ValueError):
            qs(pd.Series([0, 1]), 4, True, True, True)
