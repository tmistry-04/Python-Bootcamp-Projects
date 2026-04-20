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

profit = 0

def enough_resources(drink):
    enough = True
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there's not enough {item}")
            enough = False
    return enough


while True:
    # reset inserted_money for every new customer:
    inserted_money = 0
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        break
    elif order == "report":
        print(
            f"Water: {resources['water']}ml",
            f"Milk: {resources['milk']}ml",
            f"Coffee: {resources['coffee']}g",
            f"Money: ${profit}",
        )
    # only want to prompt for coin insertion if order is not report:
    elif enough_resources(order):
        print("Please insert coins")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        inserted_money = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01

        if inserted_money >= MENU[order]["cost"]:
            profit += MENU[order]["cost"]
            ingredients = MENU[order]["ingredients"]
            for item in ingredients:
                resources[item] -= ingredients[item]

            print(f"Here is ${round(inserted_money - MENU[order]['cost'], 2):.2f} in change."
                  f"\nHere is your {order} ☕️. Enjoy!")

        else:
            print("Sorry, that's not enough money. Money refunded")

    else:
        print("Sorry, that's not a valid option")























