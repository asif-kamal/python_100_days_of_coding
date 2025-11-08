MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

choice= ""
machine_is_running = True

while machine_is_running:
    if choice != "yes":
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    else:
        print("You chose an espresso.")
        choice = "espresso"

    if choice == "espresso" and resources["water"] >= MENU[choice]['ingredients']['water'] and resources["coffee"] >= MENU[choice]['ingredients']['coffee']:
        print(f"Cost is ${MENU.get(choice).get('cost')}0")

    elif resources["water"] >= MENU[choice]['ingredients']['water'] and resources["milk"] >= MENU[choice]['ingredients'][
        "milk"] and resources["coffee"] >= MENU[choice]['ingredients']['coffee']:

        if choice == "latte":
            print(f"Cost is ${MENU.get(choice).get('cost')}0")
        elif choice == "cappuccino":
            print(f"Cost is ${MENU.get(choice).get('cost')}0")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = round((quarters * 25 + dimes * 10 + nickels * 5 + pennies) / 100, 2)

    if total >= MENU[choice].get('cost'):

        if choice == "espresso":
            resources["water"] -= 50
            resources["coffee"] -= 18
        elif choice == "latte":
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150
        elif choice == "cappuccino":
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100

        print(f"Here is your {choice} ☕️. Enjoy!")
        print(resources)

        extra = round(total - MENU.get(choice).get('cost'), 2)
        print(f"Here is ${extra} in change.")

    elif total < MENU.get(choice).get('cost'):
        print(f"Sorry, you don't have enough money. Money refunded.")

    if 100 >= resources["water"] >= 50 and resources["coffee"] >= 18:
        choice = input("We are running low on resources. Try choosing an espresso instead? (yes/no): ").lower()
        if choice != "yes":
            machine_is_running = False
    else:
        print(f"Sorry, we don't have enough resources to make a {choice}.")
        machine_is_running = False
