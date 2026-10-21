variable_name = input("Enter the variable name in camelCase notation : ")

for c in variable_name:
    if c.isupper():
        c = c.lower()
        print("_", c, sep = "", end = "")
    else:
        print(c, end = "")