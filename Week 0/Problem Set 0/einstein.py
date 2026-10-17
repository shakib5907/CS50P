def MtoE(mass):
    return mass * pow(300000000, 2)

def main():
    mass = int(input("Enter Mass (in kilograms) : "))
    print(MtoE(mass))

main()
