# TDD Calculator test task

### The task was to add four functions in a class and test them using pytest

 `AdvanceCalc file`
 ```python
class Adavance_calc:

    def cm_to_inches(self, Num1):
        return Num1 * 2.54

    def modular(self, Num1, Num2):
        if Num1 % Num2 == 0:
            return True
        else:
            return False

    def triangle(self, Num1, Num2):
        return (Num1*Num2)/2

    def percentage(self, Num1, Num2):
        return (Num1 / 100)*Num2

```
`The Calc_test file used to test the calc`
```python
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

```
- run the test with terminal command `python -m pytest Calc_test.py`
- ` python -m inittest`