import unittest

from infix_rpn_converter.convert import infix_to_postfix


class InfixToRPNConverterTest(unittest.TestCase):

    def test_infix_to_postfix(self):
        result = infix_to_postfix(formula='(1+2)*3')
        self.assertEqual(result, '1 2 + 3 *')


if __name__ == '__main__':
    unittest.main()
