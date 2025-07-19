report = {
    "Water" : 300,
    "Milk" : 100,
    "Coffee" : 100,
    "Money" : 0.0
}
Coffe_price = {
    "espresso" : 0.5,
    "latte" : 1,
    "cappuccino":2
}
coffe_ingredients = [
    ["espresso",{ "Water" : 50, "Coffe" : 18}],
    ["Latte",{"Water" : 200, "Coffe" : 24 , "Milk" : 150}],
    ["Cappuccino",{"Water" : 250, "Coffe" : 24 , "Milk" : 100}]
]
coins = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickels" : 0.05,
    "pennies" : 0.01
}
def report_func():
    for key, value in report.items():
        print(f"{key} : {value}")
def coins_process(coin):
    print("Please insert the coins!")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    pennie = int(input("How many pennies?: "))
    final_money = round(coin["quarters"]*quarter + coin["dimes"]*dime +coin["nickels"]*nickel + coin["pennies"]*pennie,2)
    print(final_money)
    return final_money

coins_process(coins)

def espresso():
    for key in report:
        report[key] -= coffe_ingredients[0][1]["Water"]

def coffe_production(user_input):
