orders = int(input())

total_price = 0

for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    price = price_per_capsule * capsules_needed_per_day * days

    print(f'The price for the coffee is: ${price:.2f}')

    total_price += price

print(f'Total: ${total_price:.2f}')



