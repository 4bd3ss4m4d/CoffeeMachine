MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

coins = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.1,
    'quarter': 0.25,
}


# TODO 5 : Process coins
def drink_price(drink):
    print(f"The price of one {drink} is {MENU[drink]['cost']} ")


def add_coins():
    num_of_quarters = int(input("How many quarters?: "))
    num_of_dimes = int(input("How many dimes?: "))
    num_of_nickels = int(input("How many nickels?: "))
    num_of_pennies = int(input("How many pennies?: "))

    coins_inserted = float((num_of_quarters * coins['quarter']) + (num_of_dimes * coins['dime']) + (
            num_of_nickels * coins['nickel']) + (num_of_pennies * coins['penny']))
    return coins_inserted


def process_coins(drink):
    drink_price(drink)
    coins_added = add_coins()
    return coins_added


# TODO 6 : Check resources
def check_ingredients(choice, quantity):
    water_needed = MENU[choice]['ingredients']['water'] * quantity
    milk_needed = MENU[choice]['ingredients']['milk'] * quantity
    coffee_needed = MENU[choice]['ingredients']['coffee'] * quantity
    if (resources['water'] >= water_needed) and (resources['milk'] >= milk_needed) and (
            resources['coffee'] >= coffee_needed):
        return True
    else:
        return False


def make_coffee(choice, quantity):
    # Deduct ingredients from Resources
    water_needed = MENU[choice]['ingredients']['water'] * quantity
    current_water = resources['water'] - water_needed
    resources['water'] = current_water

    milk_needed = MENU[choice]['ingredients']['milk'] * quantity
    current_milk = resources['milk'] - milk_needed
    resources['milk'] = current_milk

    coffee_needed = MENU[choice]['ingredients']['coffee'] * quantity
    current_coffee = resources['coffee'] - coffee_needed
    resources['coffee'] = current_coffee

    # Give order
    print(f"Here are your {quantity} cups of {choice}. Enjoy!")


def check_resources(coins_inserted, choice, quantity, cashflow):
    price_of_choice = float(MENU[choice]['cost'])
    total_cost = price_of_choice * quantity
    if total_cost > coins_inserted:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif total_cost == coins_inserted:
        if check_ingredients(choice, quantity):
            cashflow += coins_inserted
            make_coffee(choice, quantity)
            return total_cost
        else:
            print("There is no enough ingredients")
            return 0
    elif total_cost < coins_inserted:
        if check_ingredients(choice, quantity):
            make_coffee(choice, quantity)
            change = (coins_inserted - total_cost)
            change_rounded = "{:.2f}".format(round(change, 2))
            print(f"Here is ${change_rounded} in change.")
            return total_cost
        else:
            print("There is no enough ingredients")
            return 0


def add_resources():
    for key in resources:
        resources[key] += float(input(f"Add {key}: "))


def main():
    status = 'on'
    profit = 0

    while status == 'on':
        # TODO 1 : Prompt the user by asking "What would you like? (espresso/latte/cappuccino):
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO 2 : Turn off the Coffee Machine by entering "off" to the prompt
        if choice == 'off':
            status == 'off'
            break

        # TODO 3 : Print report
        elif choice == 'report':
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Profit: ${profit}')

        #
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            coins_inserted = process_coins(choice)
            quantity = int(input(f"How many cups of {choice} would you like?: "))

            cashflow = profit
            profit += check_resources(coins_inserted, choice, quantity, cashflow)

        elif choice == 'add':
            add_resources()
        else:
            print("Wrong input!")


main()
