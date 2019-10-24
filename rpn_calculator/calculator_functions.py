def multiply(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a * b)


def division(stack):
    b = stack.pop()
    a = stack.pop()
    try:
        stack.append(a / b)
    except ZeroDivisionError:
        return 0


def addition(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a + b)


def subtraction(stack):
    b = stack.pop()
    a = stack.pop()
    stack.append(a - b)
