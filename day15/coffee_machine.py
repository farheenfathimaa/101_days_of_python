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
    "money": 0,
}

def report():
    for resource, quantity in resources.items():
        if resource == "coffee":
            print(f"{resource.capitalize()}: {quantity}g ☕️")
        elif resource == "money":
            print(f"{resource.capitalize()}: ${quantity} 💰")
        else:
            print(f"{resource.capitalize()}: {quantity}ml 🥛")

def check_resources_sufficient(drink_choice):
    drink = MENU[drink_choice]
    ingredients = drink["ingredients"]

    for ingredient, amount_required in ingredients.items():
        if resources[ingredient] < amount_required:
            print(f"Sorry, there is not enough {ingredient} ☹️")
            return False
    return True

def check_resources_sufficient(drink_choice):
    drink = MENU[drink_choice]
    ingredients = drink["ingredients"]

    for ingredient, amount_required in ingredients.items():
        if resources[ingredient] < amount_required:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_money_inserted = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    return total_money_inserted

def check_transaction_successful(drink_choice, total_money_inserted):
    drink_cost = MENU[drink_choice]["cost"]
    if total_money_inserted >= drink_cost:
        change = round(total_money_inserted - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_choice):
    drink = MENU[drink_choice]
    ingredients = drink["ingredients"]

    for ingredient, amount_required in ingredients.items():
        resources[ingredient] -= amount_required

    resources["money"] += drink["cost"]
    print(f"Here is your {drink_choice}☕️. Enjoy!")

while True:
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        exit()
    elif choice == "report":
        report()
    elif choice in MENU:
        if check_resources_sufficient(choice):
            total_money_inserted = process_coins()
            if check_transaction_successful(choice, total_money_inserted):
                make_coffee(choice)
    else:
        print("Invalid choice. Please select from espresso, latte, or cappuccino. ☕️")
