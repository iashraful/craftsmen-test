from rpn_calculator.calculator_functions import *

errors = []

operators = {
    '*': multiply,
    '/': division,
    '+': addition,
    '-': subtraction,
}


def get_input():
    expression = input('Enter an expression: ')
    return expression.strip().split()


def rpn_calculator(tokens):
    """
    Calculate the value from the RPN expression
    :param tokens: expecting a list of tokens. i.e ['1', '2', '+', '3', '*']
    :return: return value after calculate using the calculator
    """
    stack = []
    for token in tokens:
        if token in operators:
            operators[token](stack)
        else:
            try:
                stack.append(eval(token))
            except SyntaxError:
                errors.append('{0} is invalid expression\nResult generated excluding this token.'.format(token))
    return stack[0], errors  # There will be always an item or 0 indexed for post fix RPN
