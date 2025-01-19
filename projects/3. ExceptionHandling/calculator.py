operations = {
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y,
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y if y != 0 else "Division by zero error"
}

def calculator():
    while True:
        try:
            numberOne = int(input("Enter the first number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            operator = input("Enter the operator (+, -, *, /): ")
            if operator not in operations:
                raise  KeyError(f"Invalid operator")
            else:
                try:
                    numberTwo = int(input("Enter the second number: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                else:
                    result = operations[operator](numberOne, numberTwo)
                    print(result)
                    break

calculator()