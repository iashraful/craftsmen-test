# Declaring supported operators
OPERATORS = {'+', '-', '*', '/', '(', ')'}

# Setting priority of operators.
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


def infix_to_postfix(formula):
    """
    1)Fixing the priority level for each operator. High to low order:
    3.    - (negation)
    2.    * /
    1.    + - (subtraction)

    2) If the token is an operand, do not stack it. Pass it to the output.

    3) If token is an operator or parenthesis:
        3.1) if it is '(', push
        3.2) if it is ')', pop until we found '('
        3.3) push the incoming operator if its priority > top operator; else pop and popped stack item will
        be written into the output

    4) Pop the remainder of the stack and write to the output (except left parenthesis)

    :param formula: a string type formula. i.e: ( 1 + 2 ) * 3
    :return: "( 1 + 2 ) * 3" =>  "1 2 + 3 *"
    """
    stack = []
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch + ' '
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop() + ' '
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack:
        output += stack.pop()
    return output
