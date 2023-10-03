MENU = {
    "espresso": {
        "ingredients": {
            "coffee": 19,
            "water": 35,
        },
        "price": 1.99,
    },
    "latte": {
        "ingredients": {
            "coffee": 24,
            "water": 50,
            "milk": 150,
        },
        "price": 2.39,
    },
    "flat white": {
        "ingredients": {
            "coffee": 24,
            "water": 60,
            "milk": 50,
        },
        "price": 3.19,
    },
}

INVENTORY = {
    "coffee": 100,
    "water": 300,
    "milk": 300,
    "money": 0,
}


def print_report():
    print(f"Water: {INVENTORY['water']}ml")
    print(f"Milk: {INVENTORY['milk']}ml")
    print(f"Coffee: {INVENTORY['coffee']}g")
    print(f"Money: ${INVENTORY['money']:.2f}")


def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if INVENTORY[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_money_inserted = quarters + dimes + nickels + pennies
    return total_money_inserted


def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        INVENTORY[ingredient] -= amount
    INVENTORY["money"] += MENU[drink]["price"]
    print(f"Here is your {drink}. Enjoy!")


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        break
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        if check_resources(user_input):
            total_money_inserted = process_coins()
            if total_money_inserted < MENU[user_input]["price"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = total_money_inserted - MENU[user_input]["price"]
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_coffee(user_input)
        else:
            continue
    else:
        print("Invalid selection. Please choose from the menu.")
