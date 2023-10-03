class CoffeeMachine:
    def __init__(self):
        self.menu = {
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

        self.inventory = {
            "coffee": 100,
            "water": 300,
            "milk": 300,
            "money": 0,
        }

    def print_report(self):
        print(f"Water: {self.inventory['water']}ml")
        print(f"Milk: {self.inventory['milk']}ml")
        print(f"Coffee: {self.inventory['coffee']}g")
        print(f"Money: ${self.inventory['money']:.2f}")

    def check_resources(self, drink):
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            if self.inventory[ingredient] < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total_money_inserted = quarters + dimes + nickels + pennies
        return total_money_inserted

    def make_coffee(self, drink):
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            self.inventory[ingredient] -= amount
        self.inventory["money"] += self.menu[drink]["price"]
        print(f"Here is your {drink}. Enjoy!")

    def run(self):
        while True:
            user_input = input(
                "What would you like? (espresso/latte/cappuccino): "
            ).lower()

            if user_input == "off":
                break
            elif user_input == "report":
                self.print_report()
            elif user_input in self.menu:
                if self.check_resources(user_input):
                    total_money_inserted = self.process_coins()
                    if total_money_inserted < self.menu[user_input]["price"]:
                        print("Sorry, that's not enough money. Money refunded.")
                    else:
                        change = total_money_inserted - self.menu[user_input]["price"]
                        if change > 0:
                            print(f"Here is ${change:.2f} in change.")
                        self.make_coffee(user_input)
                else:
                    continue
            else:
                print("Invalid selection. Please choose from the menu.")


coffee_machine = CoffeeMachine()
coffee_machine.run()
