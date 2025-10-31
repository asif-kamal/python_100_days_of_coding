import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {}
next_step = "new"
result = 0

operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

def calculate(param_next_step, result_of_operation):
    first_num = 0.0
    if param_next_step == "new":
        first_num = float(input("Enter a number to operate on: \n"))
    elif param_next_step == "yes":
        first_num = result_of_operation
    operation_symbol = input("Enter a symbol to perform the operation on +, -, *, / \n")
    second_num = float(input("Enter a number to perform the operation on: \n"))

    for symbol, the_function in operations.items():

        if symbol == operation_symbol:
            result_of_operation = the_function(first_num, second_num)
            print(f"{first_num} {symbol} {second_num} = {result_of_operation}")
            next_step_input = input("\nType 'yes' to continue compounding another operation on the result, "
                "or 'new' to calculate a new operation. Type 'no' to end the program: \n")
            if next_step_input == "yes":
                calculate(next_step_input, result_of_operation)
            elif next_step_input == "new":
                calculate(next_step_input, 0)
            elif next_step_input == "no":
                print("Goodbye!")


calculate(next_step, result)