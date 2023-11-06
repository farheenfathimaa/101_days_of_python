from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
cm=CoffeeMaker()
mm=MoneyMachine()
menu=Menu()
mi=MenuItem
is_on=True
while is_on==True:
    order=input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if order=="off":
        is_on=False
    elif order=="report":
        cm.report()
        mm.report()
    else:
        drink=menu.find_drink(order)
        if drink is not None:
            if cm.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)
            else:
                    print(f"Sorry, there are not enough resources to make {order}.")
        else:
            print("Invalid drink choice. Please choose espresso, latte, or cappuccino.")

# MenuItem Class
# Attributes:
# - name
# - cost
# - ingredients

# Menu Class
# Methods:
# - get_items()
# - find_drink(order_name)

# CoffeeMaker Class
# Methods:
# - report()
# - is_resource_sufficient(drink)
# - make_coffee(order)

# MoneyMachine Class
# Methods:
# - report()
# - make_payment(cost)
