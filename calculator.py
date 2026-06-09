def get_two_numbers():
    x, y = input("Give two numbers separated by a space: ").split()
    return float(x), float(y)

def add(x, y):
    return x + y

def print_result(z):
    print(f"Result: {z}\n")
