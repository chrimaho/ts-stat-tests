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
        self.assertEqual(self.stability, 12702.672087912088)
        self.assertTrue(self.is_stable)
        self.assertEqual(self.lumpiness, 5558930.856730431)
        self.assertTrue(self.is_lumpy)
