import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
first = True
second = True

while first:
    # result = 0
    first_number = float(input("What's your first number?: "))

    while second:

        for operator in operations:
            print(operator)
        user_operation = input("pick an operation : ")
        next_number = float(input("What's your next number? : "))
        result = operations[user_operation](first_number, next_number)
        print(result)
        confirmation = input(
            f"Type 'y' to continue calculating with {result}, type 'no' to start a new calculation or type 'quit' to stop calculation: ").lower()
        if confirmation == "no":
            break
        elif confirmation == "quit":
            first = False
            second = False
        else:
            first_number = result
            second = True
