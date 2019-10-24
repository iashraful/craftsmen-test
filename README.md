# Craftsmen | SDEQ419 | Practical Test

## Implement a Reverse Polish Notation calculator in Python
#### Part (I) -- An RPN Calculator
**Algorithm**
```text
1. Define stack
2. Read Tokens 
3. If token is operand push to stack
4. if token is operator then, b = pop(), a = pop() and apply according the operator
5. Run this process until token is finished
6. Print result
```

#### Part (II) -- An Infix to RPN Converter
**Algorithm**
```text
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
```
### How to run?

This package require Python3 to run. Follow the steps to run and use.  
* Open up your terminal/console inside the project directory and type `$ python main.py`
* You'll get some instruction provided by the project. Just follow them.

### How to run tests?

* **Run for RPN Calculator** `python -m unittest rpn_calculator/tests.py`
* **Run for Infix to RPN Converter** `python -m unittest infix_rpn_converter/tests.py`