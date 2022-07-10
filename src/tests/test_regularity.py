import logging

from src.regularity import is_regular
from src.tests.test_base import BaseTester


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class TestRegularity(BaseTester):
    def setUp(self):
        self.sample_result = is_regular(x=self.data, algorithm="sample")
        self.approx_result = is_regular(x=self.data, algorithm="approx", tolerance=20)
        self.spectral_result = is_regular(x=self.data, algorithm="spectral", sf=1)

    def test_regularity(self):

        # Check keys
        self.assertListEqual(
            list(self.sample_result.keys()), ["result", "entropy", "tolerance"]
        )

        # Check types
        params = [
            (self.sample_result["result"], bool),
            (self.sample_result["entropy"], (float, int)),
            (self.sample_result["tolerance"], (float, int)),
        ]
        for value, expected in params:
            self.assertIsInstance(value, expected)

        # Check values
        params = [
            (self.sample_result["entropy"], 0.6177074729583698),
            (self.sample_result["tolerance"], 23.909808306554297),
            (self.approx_result["entropy"], 0.6451264780416452),
            (self.approx_result["tolerance"], 20),
            (self.spectral_result["entropy"], 0.4287365561752448),
            (self.spectral_result["tolerance"], 23.909808306554297),
        ]
        for value, expected in params:
            self.assertAlmostEqual(value, expected)

        # Check results
        params = [
            (self.sample_result["result"], True),
            (self.approx_result["result"], True),
            (self.spectral_result["result"], True),
        ]
        for value, expected in params:
            self.assertTrue(value, expected)

    def test_regularity_errors(self):
        with self.assertRaises(ValueError):
            is_regular(x=self.data, algorithm="error")
        with self.assertRaises(ValueError):
            is_regular(x=self.data, tolerance="error")
