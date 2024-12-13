MENU = {
    "espresso": 
    {
        "ingredients": 
        {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": 
    {
        "ingredients": 
        {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": 
    {
        "ingredients": 
        {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

REPORT = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}

#print(MENU["cappuccino"]["ingredients"]["water"])

def check_of_ingredients(answer):
    if MENU[answer]["ingredients"]["water"] > REPORT["water"]:
        print("The is not enough water.")
        return False
    elif MENU[answer]["ingredients"]["milk"] > REPORT["milk"]:
        print("The is not enough water.")
        return False
    elif MENU[answer]["ingredients"]["coffee"] > REPORT["coffee"]:
        print("The is not enough water.")
        return False

    return True

need_coffee = 'y'
money = 0.0

while need_coffee == 'y':
    print("\n")
    answer = input("What would you like? espresso/latte/cappuccino | report/exit: ")
    while answer != "espresso" and answer != "latte" and answer != "cappuccino" and answer != "report" and answer != "exit":
        print("There is no option like this. Check if you didn't make a mistake and try again.")
        answer = input("What would you like? espresso/latte/cappuccino | report: ")

    if answer == "exit":
        break
    else:
        if answer == "espresso" or answer == "latte" or answer == "cappuccino":
            if check_of_ingredients(answer) == True:
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickles = int(input("How many nickles? "))
                pennies = int(input("How many pennies? "))
                money = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
                if money < MENU[answer]["cost"]:
                    print("Sorry, that is not enough money. Money refunded.")
                else:
                    print(f"Here is your {money - MENU[answer]['cost']} change.")
                    REPORT["water"] = REPORT["water"] - MENU[answer]["ingredients"]["water"]
                    REPORT["milk"] = REPORT["milk"] - MENU[answer]["ingredients"]["milk"]
                    REPORT["coffee"] = REPORT["coffee"] - MENU[answer]["ingredients"]["coffee"]
                    print(f"Here is your {answer}. Enjoy!")
                    need_coffee = input("Do you want something else? Yes - y, No - n: ")
        elif answer == "report":
            print(f"Water: {REPORT['water']} ml")
            print(f"Milk: {REPORT['milk']} ml")
            print(f"Coffee: {REPORT['coffee']} g")
            print(f"Money: ${REPORT['money']}")