def format_name(f_name, l_name):
    """function to titlecase first name and last name"""

    return f"{f_name} {l_name}".title()

result = format_name(input("Enter first name: "), input("Enter last name: "))
print(result)