from ts_stat_tests.stability import is_stable
from ts_stat_tests.stability import stability
from ts_stat_tests.tests.test_base import BaseTester


class StabilityTests(BaseTester):
    def setUp(self):
        self.stability = stability(self.data)
        self.is_stable = is_stable(self.data)

    def test_stability(self):
        self.assertEqual(self.stability, 12702.672087912088)
        self.assertTrue(self.is_stable)
