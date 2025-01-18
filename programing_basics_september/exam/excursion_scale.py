sea_excursion = int(input())
mountain_excs = int(input())
profit = 0

sea_price = 680
mountain_price = 499

while True:
    command = input()

    if command == "Stop":
        break

    if command == "sea":
        if sea_excursion > 0:
            profit += sea_price
            sea_excursion -= 1
    elif command == "mountain":
        if mountain_excs > 0:
            profit += mountain_price
            mountain_excs -= 1

    if sea_excursion == 0 and mountain_excs == 0:
        break

if sea_excursion == 0 and mountain_excs == 0:
    print("Good job! Everything is sold.")
print(f"Profit: {profit} leva.")