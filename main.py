MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
Money = 0
machine_on = True


def order(cost):
    global Money
    print("Insert coins \n number of coins of:")
    Money = (
        float(input("quarters: ")) * 0.25 +
        float(input("dimes: ")) * 0.10 +
        float(input("nickles: ")) * 0.05 +
        float(input("pennies: ")) * 0.01

    )

    if Money < cost:
        print("Sorry, not enough money. Money refunded.")
        Money = 0
        return False
    if Money > cost:
        print(f"Here is your return {round(Money - cost, 2)}")
        print(f"Here is your {user_input}. Enjoy !")
    Money = cost
    return True


while machine_on:


    user_input = input("What would you like? (espresso/latte/cappuccino)").lower()

    if user_input == "off":
        machine_on = False

    elif user_input == "report":
        print("current resources:-")
        print(f"water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffe: {coffee}")



    if user_input in ["espresso", "latte", "cappuccino"]:
        drink = MENU[user_input]["ingredients"]

        if water < drink["water"] or milk < drink["milk"] or coffee < drink["coffee"]:
            print("Sorry ! There are not enough resources")
            continue

        if order(MENU[user_input]["cost"]):
            water -= drink["water"]
            milk -= drink["milk"]
            coffee -= drink["coffee"]
        else:
            print("payment failed !")