total = 0

while total < 50:
    coin = int(input("Insert Coin: "))
    total += coin
    if total < 50:
        print(f"Amount Due: {50 - total}")

print(f"Change Owed: {total - 50}")