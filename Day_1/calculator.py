def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

boolean =True

def calculator():
    n3 = int(input("What's the First number?"))
    while boolean:
        operation ={
            "+" : add,
            "-" : sub,
            "*" : mul,
            "/" : div
        }
        for operators in operation:
            print(operators)
        symbol = input("Pick an operation: ")
        n4 = int(input("What's the next number? "))
        result = operation[symbol](n3,n4)
        print(f"{n3} {symbol} {n4} = {result}")

        user_input = input(f"Type 'y' to continue with {result}, or type 'n' to Start a new calculation : ")
        if user_input == "y":
            n3 = result
        else:
            calculator()

calculator()