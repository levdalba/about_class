from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
is_on = True
while is_on:
    choice = input(menu.get_items())
    if choice == "off":
        break
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffe_maker.make_coffee(drink)

    elif choice == "report":
        coffe_maker.report()
    else:
        break
