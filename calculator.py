def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        print("Cannot divide by zero.")
        return None
    return n1 / n2

def calculator():
    n1 = float(input("What's the first number: "))
    continue_calc = True
    while continue_calc:
        print("+")
        print("-")
        print("*")
        print("/")
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number: "))

        if operation == "+":
            result = add(n1, n2)
            print(f"{n1} + {n2} = {result}")
        elif operation == "-":
            result = subtract(n1, n2)
            print(f"{n1} - {n2} = {result}")
        elif operation == "*":
            result = multiply(n1, n2)
            print(f"{n1} * {n2} = {result}")
        elif operation == "/":
            result = divide(n1, n2)
            if result is not None:
                print(f"{n1} / {n2} = {result}")
        else:
            result = 0.0
            print(f"{n1} undefined {n2} = {result}")

        if result is None:
            continue

        condition = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if condition == "y":
            n1 = result
            continue_calc = True
        elif condition == "n":
            n1 = float(input("What's the first number: "))
        else:
            break

calculator()