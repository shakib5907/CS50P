print("Basic Calculator, Functions With Two Operands Only!")

while True:
    operand1 = float(input("Enter the first operand : "))
    operand2 = float(input("Enter the second operand : "))

    operator = input("Enter the operation you would like to perform (+, -, *, /, %) : ")

    while operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "%":
        operator = input("Invalid Input! Enter the valid operation you would like to perform (+, -, *, /, %) : ")

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "%":
        if operand2 == 0:
                print("Error! Division by zero is not possible")
        else:
            result = operand1 % operand2
    else:
        if operand2 == 0:
            print("Error! Division by zero is not possible")
        else:
            result = operand1 / operand2
    print(f"{operand1} {operator} {operand2} = {result}")

    cont = input("Would you like to continue? (Y/N) : ")
    while cont != 'Y' and cont != 'y' and cont != 'N' and cont != 'n':
         cont = input("Invalid Input! Would you like to continue? (Y/N) : ")

    if cont == 'N' or cont == 'n': break
              