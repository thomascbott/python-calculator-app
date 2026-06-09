# Helper Methods
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

    # # split the string into a list of substrings
    expression = expression.split()
    #
    # # testing reading each substring (should be only a character each for valid input)
    # for char in expression:
    #     print(char)

    while stack_nums or stack_operators:


