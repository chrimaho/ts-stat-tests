import unittest

from sktime.datasets import load_airline


class BaseTester(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = load_airline()

    @classmethod
    def tearDownClass(self):
        pass
