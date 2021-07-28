# This is a sample Python script.
import machine
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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

currentMoney = machine.Money()


def create_menu_item(name):
    water_selected = MENU[name]["ingredients"]["water"]
    if name == "espresso":
        milk_selected = 0
    else:
        milk_selected = MENU[name]["ingredients"]["milk"]
    coffee_selected = MENU[name]["ingredients"]["coffee"]
    cost_of_item = MENU[name]["cost"]
    return machine.Menu(water=water_selected, milk=milk_selected, coffee=coffee_selected, cost=cost_of_item)


def start_order():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    find_option(user_input)


def find_option(user_response):
    if user_response == "report":
        report()
    elif user_response == "espresso":
        make_espresso()
    elif user_response == "latte":
        make_latte()
    elif user_response == "cappuccino":
        make_cappuccino()
    elif user_response == "off":
        pass
    else:
        print("this is not a valid input.")
        start_order()


# TODO finish the report
def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(currentMoney.get_money()))
    start_order()


def make_espresso():
    if check_resources(espresso):
        resources["water"] -= espresso.water
        resources["milk"] -= espresso.milk
        resources["coffee"] -= espresso.coffee
        currentMoney.add_money(espresso.cost)

    start_order()


def make_latte():

    currentMoney.add_money(latte.cost)
    start_order()


def make_cappuccino():

    currentMoney.add_money(cappuccino.cost)
    start_order()


# what is needed and what is available
def check_resources(name):
    if resources["water"] < name.water:
        print("Sorry there is not enough water.")
        return False
    if resources["milk"] < name.milk:
        print("Sorry there is not enough milk.")
        return False
    if resources["coffee"] < name.coffee:
        print("Sorry there is not enough coffee.")
        return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    espresso = create_menu_item("espresso")
    latte = create_menu_item("latte")
    cappuccino = create_menu_item("cappuccino")
    start_order()
