total = 0
print(f"Amount Due: {50 - total}")

while total < 50:
    while True:
            coin = int(input("Insert Coin: "))
            if coin == 25 or coin == 10 or coin == 5:
                coin = coin
                break
            print(f"Amount Due: {50 - total}")

    total += coin
    if total < 50:
        print(f"Amount Due: {50 - total}")

print(f"Change Owed: {total - 50}")