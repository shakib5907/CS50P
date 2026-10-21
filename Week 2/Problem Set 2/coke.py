def get_coin():
    while True:
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            return coin  

total = 0

while total < 50:
    coin = get_coin()
    total += coin
    if total < 50:
        print(f"Amount Due: {50 - total}")

print(f"Change Owed: {total - 50}")