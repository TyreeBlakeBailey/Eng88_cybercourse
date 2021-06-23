import pytest
import unittest

from SimpleCalc import SimpleCalc

class Cacltest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):  # naming convention is essential as 'test' is the word we need to use when naming tests so
        # python interpreter recog nised it to run the test
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

