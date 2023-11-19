from machine_data import resources, MENU

menu = MENU
machine_resources = resources


def ingredient_check(drink_selection):
    """Checks ingredient levels for selected drink"""
    drink = menu[drink_selection]["ingredients"]

    for ingredient in drink:
        if machine_resources[ingredient] < drink[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return
        else:
            machine_resources[ingredient] -= drink[ingredient]
    return "collect money"


def check_applepay(drink_selection):
    print("Please insert coins:")
    applepay = float(input("How many quarters: ")) * .25
    applepay += float(input("How many dimes: ")) * .10
    applepay += float(input("How many nickles: ")) * .05
    applepay += float(input("How many pennies: ")) * .01

    drink_cost = menu[drink_selection]["cost"]

    if applepay == drink_cost:
        print(f"Here is your {drink_selection}. Enjoy!")
        return drink_cost
    elif applepay > drink_cost:
        change = format((applepay - drink_cost), ".2f")
        print(f"Here is {change} in change.\nHere is your {drink_selection}. Enjoy!")
        return drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")

def machine_report(profit):
    profit = format(profit, ".2f")
    print("Water: " + str(machine_resources["water"]) + "ml")
    print("Milk: " + str(machine_resources["milk"]) + "ml")
    print("Coffee: " + str(machine_resources["coffee"]) + "g")
    print(f"Money: ${profit}")


def create_drink(drink_selection):
    if ingredient_check(drink_selection) == "collect money":
        paid_amount = check_applepay(drink_selection)
        return paid_amount
    else:
        return 0


machine_on = True
profit = float(0)

#Start of the Application
while machine_on:
    print("~~~~~~~~~Menu~~~~~~~~~\nEspresso: $1.50\nLatte: $2.50\nCappuccino: $3.00")
    drink_selection = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if drink_selection == 'off':
        machine_on = False
    elif drink_selection == 'report':
        machine_report(profit)
    elif drink_selection in ['espresso', 'latte', 'cappuccino']:
        profit += create_drink(drink_selection)
    else:
        print("Incorrect Menu Option Entered")
