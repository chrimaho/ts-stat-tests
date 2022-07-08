from src.tests.test_base import BaseTester
from src.regularity import is_regular


class TestRegularity(BaseTester):
    def setUp(self):
        self.sample_result = is_regular(x=self.data, algorithm="sample")
        self.approx_result = is_regular(x=self.data, algorithm="approx", tolerance=20)

    def test_regularity(self):

        self.assertListEqual(
            list(self.sample_result.keys()), ["result", "entropy", "tolerance"]
        )
        self.assertIsInstance(self.sample_result["result"], bool)
        self.assertIsInstance(self.sample_result["entropy"], (float, int))
        self.assertIsInstance(self.sample_result["tolerance"], (float, int))

        self.assertAlmostEqual(
            self.sample_result["entropy"],
            0.6177074729583698,
        )
        self.assertAlmostEqual(
            self.sample_result["tolerance"],
            23.909808306554297,
        )

        self.assertAlmostEqual(
            self.approx_result["entropy"],
            0.6451264780416452,
        )
        self.assertEqual(
            self.approx_result["tolerance"],
            20,
        )

    def test_regularity_errors(self):
        with self.assertRaises(ValueError):
            is_regular(x=self.data, algorithm="error")
        with self.assertRaises(ValueError):
            is_regular(x=self.data, tolerance="error")
