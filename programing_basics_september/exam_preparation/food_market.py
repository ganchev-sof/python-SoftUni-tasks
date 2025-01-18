strawberry_price = float(input())
quantity_banana = float(input())
quantity_orange = float(input())
quantity_raspberry = float(input())
quantity_strawberry = float(input())

raspberry_price = strawberry_price / 2
orange_price = raspberry_price - (0.4 * raspberry_price)
banana_price = raspberry_price - (0.8 * raspberry_price)

total_sum = ((raspberry_price * quantity_raspberry) + (strawberry_price * quantity_strawberry) +
             (orange_price * quantity_orange)) + (banana_price * quantity_banana)

print(total_sum)