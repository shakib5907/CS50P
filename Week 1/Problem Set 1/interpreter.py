userInput = input("Enter the numbers and the operator : ")
x, y, z = userInput.split(" ")

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
else:
    result = x / z

print(float(result))