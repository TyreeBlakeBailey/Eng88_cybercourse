from Advance_Calc import Adavance_calc
import unittest


class Cacltest(unittest.TestCase):
    calc = Adavance_calc()

    def test_cm_to_inches(self):
        self.assertEqual(self.calc.cm_to_inches(10), 25.4)

    def test_modular(self):
        self.assertEqual(self.calc.modular(4, 2), True)

    def test_triangle(self):
        self.assertEqual(self.calc.triangle(4, 2), 4)

    def test_percentage(self):
        self.assertEqual(self.calc.percentage(50, 10), 5)
