from tsfeatures import lumpiness as ts_lumpiness
from tsfeatures import stability as ts_stability

from src.stability import is_lumpy
from src.stability import is_stable
from src.stability import lumpiness
from src.stability import stability
from src.tests.test_base import BaseTester


class StabilityTests(BaseTester):
    def setUp(self):
        self.stability = stability(self.data)
        self.is_stable = is_stable(self.data)
        self.lumpiness = lumpiness(self.data)
        self.is_lumpy = is_lumpy(self.data)

    def test_stability(self):
        self.assertEqual(self.stability, ts_stability(self.data)["stability"])
        self.assertTrue(self.is_stable)

    def test_lumpiness(self):
        self.assertEqual(self.lumpiness, ts_lumpiness(self.data)["lumpiness"])
        self.assertTrue(self.is_lumpy)
