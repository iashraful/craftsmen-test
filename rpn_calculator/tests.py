import unittest

from .calculator_functions import multiply, addition, division, subtraction
from .calculator import rpn_calculator


class RPNCalculatorTest(unittest.TestCase):

    def test_rpn_calculator(self):
        result, errors = rpn_calculator(tokens='1 2 + 3 *'.split())
        self.assertEqual(result, 9)

    def test_multiply(self):
        stack = [3, 4]
        multiply(stack=stack)
        self.assertEqual(stack, [12])

    def test_addition(self):
        stack = [3, 4]
        addition(stack=stack)
        self.assertEqual(stack, [7])

    def test_division(self):
        stack = [10, 2]
        division(stack=stack)
        self.assertEqual(stack, [5.0])

    def test_subtraction(self):
        stack = [10, 2]
        subtraction(stack=stack)
        self.assertEqual(stack, [8])


if __name__ == '__main__':
    unittest.main()
