# water = 300
# milk = 200
# coffe = 100
# money = 0.0

report = {
    "Water" : 300,
    "Milk" : 100,
    "Coffee" : 100,
    "Money" : 0.0
}

def machine_report():
    print(f"Water :{water}ml")
    print(f"Milk :{milk}ml")
    print(f"Coffe :{coffe}ml")
    print(f"Money :${money}")

def coin_process():
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many quarters?: "))
    nickel = int(input("How many quarters?: "))
    pennies = int(input("How many quarters?: "))

coffe_ingredients = [
    ["espresso",{ "Water" : 50, "Coffe" : 18}],
    ["Latte",{"Water" : 200, "Coffe" : 24 , "Milk" : 150}],
    ["Cappuccino",{"Water" : 250, "Coffe" : 24 , "Milk" : 100}]
]

print(coffe_ingredients[0][1]["Water"])
def espresso():
    report["Water"] -= coffe_ingredients[0][1]["Water"]
    print(report)
    print(report)
espresso()