def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

functions = {"+": add, "-": sub, "*": mul, "/": div}
cont = True

def calculator():
    number1 = float(input("Type a number: "))

    while cont:
        function = input("Type a function: ")
        number2 = float(input("Type a second number: "))
        result = functions[function](number1, number2)
        print(f"{number1} {function} {number2} = {result}")
        if input("Would you like to continue? (y/n): ") == "n":
            number1 = float(input("Type a number: "))
        else:
            number1 = float(result)

calculator()