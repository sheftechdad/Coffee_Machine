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

def is_resource_sufficient(order_ingridient):
    for item in order_ingridient:
        if order_ingridient[item]>= resources[item]:
            print(f"sorry there is not enough {item}")
            return False

    return True

def process_coin():
    print("please,enter your coins")
    total= int(input("How  many quaters:? "))*0.25
    total += int(input("How  many dimes:? "))*0.1
    total += int(input("How  many nicklecs:? "))*0.5
    total += int(input("How  many pennies:? "))*0.01
    return total


def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"here, is ${change} your change")
        global profit
        profit +=drink_cost
        return True
    else:
        print("sorry, money is not sufficient. Money refund")
        return False


def make_coffee(drink_name, order_ingridient)  :
    for item in order_ingridient:
        resources[item] -= order_ingridient[item]
    print(f"here is your {drink_name}")


profit =0
is_on=True

while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino):"
)
    if choice=="off":
        is_on=False
    elif choice=="report" :
        print(f"Water: {resources['water']}ml")
        print(f" Milk:{resources['milk']}ml")
        print(f" Coffee:{resources['coffee']}ml")
        print(f" Money:${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
           payment=process_coin()
           is_transaction_successful(payment,drink["cost"])
           make_coffee(choice,drink["ingredients"])





