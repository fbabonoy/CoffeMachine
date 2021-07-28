import machine

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
        make_drink(espresso)
    elif user_response == "latte":
        make_drink(latte)
    elif user_response == "cappuccino":
        make_drink(cappuccino)
    elif user_response == "off":
        pass
    else:
        print("this is not a valid input.")
        start_order()


def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(currentMoney.get_money()))
    start_order()


def make_drink(name):
    if check_resources(name):
        if process_coins(name.cost):
            resources["water"] -= name.water
            resources["milk"] -= name.milk
            resources["coffee"] -= name.coffee
            currentMoney.add_money(name.cost)
    start_order()

# TODO round float to two decimal places
# TODO what happpens if input is not a number like a STR
def process_coins(cost):
    money_inserted = 0
    print("please insert $" + str(cost))
    quarters = float(input("how many quarters? ")) * .25
    dimes = float(input("how many dimes? ")) * .10
    nickles = float(input("how many nickles? ")) * .05
    pennies = float(input("how many pennies? ")) * .01
    money_inserted = quarters + dimes + nickles + pennies
    if money_inserted > cost:
        total = money_inserted - cost
        print("your change is " + str(total))
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


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


if __name__ == '__main__':
    espresso = create_menu_item("espresso")
    latte = create_menu_item("latte")
    cappuccino = create_menu_item("cappuccino")
    start_order()
