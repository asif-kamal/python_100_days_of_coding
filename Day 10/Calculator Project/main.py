def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {}

operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

first_num = float(input("Enter a number to operate on: \n"))
operation_symbol = input("Enter a symbol to perform the operation on +, -, *, / \n")
second_num = float(input("Enter a number to perform the operation on: \n"))
for symbol, the_function in operations.items():
    if symbol == operation_symbol:
        print(f"{first_num} {symbol} {second_num} = {the_function(first_num, second_num)}")


