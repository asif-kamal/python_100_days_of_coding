def format_name(f_name, l_name):
    return f"{f_name} {l_name}".title()

result = format_name(input("Enter first name: "), input("Enter last name: "))
print(result)