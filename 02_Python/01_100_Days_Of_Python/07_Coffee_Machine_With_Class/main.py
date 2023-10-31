from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while is_on:
    user_choose = input(f"What would you like " + menu.get_items() + ": ")
    if user_choose == "off":
        is_on = False
    elif user_choose == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choose)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


