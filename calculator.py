# Helper Methods
from operator import truediv


def get_two_numbers():
    x, y = input("Give two numbers separated by a space: ").split()
    return float(x), float(y)

def print_result(z):
    print(f"Result: {z}\n")

# Four Basic Arithmetic Operation Methods
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Undefined: Division by zero"
    return x / y

# expression evaluator

def evaluate_expression(expression: str):
    # use a list as a stack
    stack_operators = []
    stack_nums = []
    counter = 0

    # # split the string into a list of substrings
    expression = expression.split()
    #
    # # testing reading each substring (should be only a character each for valid input)
    # for char in expression:
    #     print(char)

    while stack_nums or stack_operators:
        #check if operator
        if is_operator(expression[counter]):
            stack_operators.append(expression[counter])
        # check if number
        elif isinstance(expression[counter], (int, float)):
            stack_nums.append(expression[counter])


# expression evaluator Helper Methods

def is_operator(operator) -> bool:
    match operator:
        case '(':
            return True
        case ')':
            return True
        case '+':
            return True
        case '-':
            return True
        case '*':
            return True
        case '/':
            return True
        case _:
            return False

