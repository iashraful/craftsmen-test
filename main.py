#!/usr/bin/python3
from infix_rpn_converter.convert import infix_to_postfix
from rpn_calculator.calculator import rpn_calculator


def get_input(_format='list'):
    expression = input('Enter an expression: ')
    if _format == list.__name__:
        return expression.strip().split()
    return expression


def run_infix_to_rpn():
    print("Infix to RPN converter.")
    expression = get_input(_format=str.__name__)
    result = infix_to_postfix(expression)
    print(result)


def run_rpn_calculator():
    print("RPN Calculator.")
    expression = get_input()
    result, errors = rpn_calculator(tokens=expression)
    print(result)
    print('\n'.join(errors))


if __name__ == '__main__':
    print('''
        1: Infix to RPN Converter
        2: RPN Calculator
    ''')
    decision = input()
    if decision == '1':
        run_infix_to_rpn()
    elif decision == '2':
        run_rpn_calculator()
    else:
        print('Please enter a valid choice.')
