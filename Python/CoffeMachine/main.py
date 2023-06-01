# The Coffee Machine Project

# Import Modules
from menu import options, resources, coins
import os


# Define functions

def create_report(resources_qty, money_res):
    print(f"Water: {resources_qty['water']}ml\n"
          f"Milk: {resources_qty['milk']}ml\n"
          f"Coffee: {resources_qty['coffee']}g\n"
          f"Money: ${money_res}"
          )


def resource_sufficient(option, resources_qty):
    # print(option)
    # print(options[option])

    if option == 'espresso':
        if resources_qty['water'] >= options[option]['ingredients']['water']:
            if resources_qty['coffee'] >= options[option]['ingredients']['coffee']:
                # resources_qty['water'] = resources_qty['water'] - options[option]['ingredients']['water']
                # resources_qty['coffee'] = resources_qty['coffee'] - options[option]['ingredients']['coffee']
                return 1
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    else:
        if resources_qty['water'] >= options[option]['ingredients']['water']:
            if resources_qty['milk'] >= options[option]['ingredients']['milk']:
                if resources_qty['coffee'] >= options[option]['ingredients']['coffee']:
                    # resources_qty['water'] = resources_qty['water'] - options[option]['ingredients']['water']
                    # resources_qty['milk'] = resources_qty['milk'] - options[option]['ingredients']['milk']
                    # resources_qty['coffee'] = resources_qty['coffee'] - options[option]['ingredients']['coffee']
                    return 1
                else:
                    print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water")


def ask_for_coins(option):
    global money
    user_total = 0
    for key in coins:
        user_total = user_total + coins[key] * int(input(f"How many {key}: "))

    if options[option]['cost'] > user_total:
        print("Sorry that's not enough money. Money refunded.")
    elif options[option]['cost'] == user_total:
        money += user_total
        return 1
    else:
        money += user_total - round(user_total - options[option]['cost'], 2)
        print(f" Here is ${round(user_total - options[option]['cost'], 2)} dollars in change.")
        return 1


def reduce_resources(option, resources_qty):
    if option == 'espresso':
        resources_qty['water'] = resources_qty['water'] - options[option]['ingredients']['water']
        resources_qty['coffee'] = resources_qty['coffee'] - options[option]['ingredients']['coffee']
    else:
        resources_qty['water'] = resources_qty['water'] - options[option]['ingredients']['water']
        resources_qty['milk'] = resources_qty['milk'] - options[option]['ingredients']['milk']
        resources_qty['coffee'] = resources_qty['coffee'] - options[option]['ingredients']['coffee']


# Define Variables and/or Constants

machine_status = 'on'
# water = 300
# milk = 200
# coffee = 100
money = 0

while machine_status == 'on':
    user_choose = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choose in (['espresso', 'latte', 'cappuccino', 'report', 'off']):
        if user_choose == 'report':
            create_report(resources, money)
        elif user_choose == 'off':
            machine_status = 'off'
        else:
            money_flag = resource_sufficient(user_choose, resources)
            if money_flag == 1:
                buying = ask_for_coins(user_choose)
                if buying == 1:
                    reduce_resources(user_choose, resources)
                    print(f"Here is your {user_choose}. Enjoy!")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
