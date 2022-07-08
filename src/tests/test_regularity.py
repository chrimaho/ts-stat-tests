from src.tests.test_base import BaseTester
from src.regularity import is_regular


class TestRegularity(BaseTester):
    def setUp(self):
        self.sample_result = is_regular(x=self.data, algorithm="sample")
        self.approx_result = is_regular(x=self.data, algorithm="approx", tolerance=20)

    def test_regularity(self):
        self.assertDictEqual(
            self.sample_result,
            {
                "result": True,
                "entropy": 0.6177074729583698,
                "tolerance": 23.909808306554297,
            },
        )
        self.assertDictEqual(
            self.approx_result,
            {
                "result": True,
                "entropy": 0.6451264780416452,
                "tolerance": 20,
            },
        )

    def test_regularity_errors(self):
        with self.assertRaises(ValueError):
            is_regular(x=self.data, algorithm="error")
        with self.assertRaises(ValueError):
            is_regular(x=self.data, tolerance="error")
