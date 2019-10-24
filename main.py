#!/usr/bin/python3
from rpn_calculator.calculator import get_input, rpn_calculator

if __name__ == '__main__':
    # Read input from user
    _tokens = get_input()
    # Calculate the value using RPN calculator
    result, errors = rpn_calculator(tokens=_tokens)
    print(result)
    print('\n\n'.join(errors))
