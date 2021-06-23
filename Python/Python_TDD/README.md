# Python TDD

## Test driven development
### Pytest and unittest
### Use pip to install the packages
`pip install pytest`

- nothing is set or pushed to production (in front of client) until it is tested 
- Red - everything failing
- Green - Write new code (if nothing is available) to pass  
- Blue - Refactoring the code improving the old code and start rge cycle again

- Unittest and pytest


#### Creates a file to write our tests 
#### Then we will create a file to add functionality to pass the test 

## Test code
```python
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


```

- run the test with terminal command `python -m pytest Calc_test.py`
- ` python -m inittest`

### Functionality to pass the test
```python


class SimpleCalc:

    def add(self, Num1, Num2):
        return Num1 + Num2

    def subtract(self, Num1, Num2):
        return Num1 - Num2

    def multiply(self, Num1, Num2):
        return Num1 * Num2

    def divide(self, Num1, Num2):
        return Num1/Num2
```
