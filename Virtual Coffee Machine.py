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
    "Money": 0
}
# TODO 1: Extracting Data from the dictionary

cost_espresso = MENU['espresso']['cost']
cost_latte = MENU['latte']['cost']
cost_capuccino = MENU['cappuccino']['cost']
espresso_ingredients_water = MENU['espresso']['ingredients']['water']
espresso_ingredients_cofee = MENU['espresso']['ingredients']['coffee']
latte_water = MENU['latte']['ingredients']['water']
latte_milk = MENU['latte']['ingredients']['milk']
latte_coffee = MENU['latte']['ingredients']['coffee']
cappuccino_water = MENU['cappuccino']['ingredients']['water']
cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']

coffee_machine = True
while coffee_machine:
# TODO 2: Creating a variable called 'user' and in this variable we've given an input so that user must choice that which coffee they want.

    user = input("What Would you like? (Espresso,Latte,Cappuccino): ").lower()

# TODO 3 : We are creating a function called espresso,latte and cappuccino. In this function if the user chooses espresso then it should enter all the coins.If coins less than the price then the user getting feedback message
# TODO 4: If the user inserted more coins then it should give us back the extra coins which user have inserted
# Todo 5 : if the user gets coffee successful then the resources gets substracted from the coffee ingredients
    def espresso():
        print('Please Insert Coins.')
        quater = 0.25 * float(input("How much quater?: "))
        dimes = 0.10 * float(input("How much dimes?: "))
        nickles = 0.05 * float(input("How much nickles?: "))
        pennies = 0.01 * float(input("How much pennies?: "))
        total = quater + dimes + nickles + pennies
        if total == cost_espresso:
            resources['water'] -= espresso_ingredients_water
            resources['coffee'] -= espresso_ingredients_cofee
            resources['money'] = + cost_espresso
            return "Here is your 'Espresso'☕. Enjoy!"
        elif total > cost_espresso:
            monetary_value = total - cost_espresso
            resources['water'] -= espresso_ingredients_water
            resources['coffee'] -= espresso_ingredients_cofee
            resources['money'] = + cost_espresso
            return f"""Here is the change ${round(monetary_value, 2)}
Here is your 'Espresso'☕. Enjoy!"""
        elif total < cost_espresso:
            resources['money'] = 0
            return "Sorry that's not money. Money Refunded"

    def latte():
        print('Please Insert Coins.')
        quater = 0.25 * float(input("How much quater?: "))
        dimes = 0.10 * float(input("How much dimes?: "))
        nickles = 0.05 * float(input("How much nickles?: "))
        pennies = 0.01 * float(input("How much pennies?: "))
        total = quater + dimes + nickles + pennies
        if total == cost_latte:
            resources['water'] -= latte_water
            resources['milk'] -= latte_milk
            resources['coffee'] -= latte_coffee
            resources['money'] += cost_latte
            return "Here is your 'Latte'☕.Enjoy!"
        elif total > cost_latte:
            monetary_value = total - cost_latte
            resources['water'] -= latte_water
            resources['milk'] -= latte_milk
            resources['coffee'] -= latte_coffee
            resources['money'] += cost_latte
            return f"""Here is the change ${round(monetary_value, 2)}
Here is your 'Latte'☕. Enjoy!"""
        elif total < cost_espresso:
            resources['money'] = 0
            return 'Sorry there is not money.Money refunded.'


    def cappuccino():
        print('Please Insert Coins.')
        quater = 0.25 * float(input("How much quater?: "))
        dimes = 0.10 * float(input("How much dimes?: "))
        nickles = 0.05 * float(input("How much nickles?: "))
        pennies = 0.01 * float(input("How much pennies?: "))
        total = quater + dimes + nickles + pennies
        if total == cost_capuccino:
            resources['water'] -= cappuccino_water
            resources['milk'] -= cappuccino_milk
            resources['coffee'] -= cappuccino_coffee
            resources['money'] += cost_capuccino
            return 'Here is your "Cappuccino"☕.Enjoy!'
        elif total > cost_capuccino:
            monetary_value = total - cost_capuccino
            resources['water'] -= cappuccino_water
            resources['milk'] -= cappuccino_milk
            resources['coffee'] -= cappuccino_coffee
            resources['money'] += cost_capuccino
            return f"""Here is the change ${round(monetary_value, 2)}
Here is your 'Cappuccino'☕.Enjoy!"""
        elif total < cost_capuccino:
            resources['money'] = 0
            return "Sorry there is not enough money.Money refunded."
# Todo 6 : If user type report it should get full how much resources have left for making coffee.

    def report():
        return f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money : ${resources['money']}"""

# Todo 7 : If the resources is less than resources of making coffee then the user gets feedback prompt that this resources is not available for makin coffee.
    if user == 'espresso':
        if resources['water'] < espresso_ingredients_water:
            print("Sorry there is not enough water")
        elif resources['coffee'] < espresso_ingredients_cofee:
            print("Sorry there is not enough coffee")
        else:
            print(espresso())
    elif user == 'latte':
        if resources['water'] < latte_water:
            print("Sorry there is not enough water")
        elif resources['milk'] < latte_milk:
            print("Sorry there is not enough milk")
        elif resources['coffee'] < latte_coffee:
            print("Sorry there is not enough coffee")
        else:
            print(latte())
    elif user == 'cappuccino':
        if resources['water'] < cappuccino_water:
            print("Sorry there is not enough water")
        elif resources['milk'] < cappuccino_milk:
            print("Sorry there is not enough milk")
        elif resources['coffee'] < cappuccino_coffee:
            print("Sorry there is not enough coffee")
        else:
            print(cappuccino())
    elif user == 'report':
        print(report())
# Todo 8: If the user choses other than three options than it should give him feedback and the coffee machine stops
    else:
        print("You've chosen the wrong option. Bye!")
        coffee_machine = False