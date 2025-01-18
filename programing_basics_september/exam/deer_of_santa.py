import math

days = int(input())
left_food = int(input())
food_per_day_deer1 = float(input())
food_per_day_deer2 = float(input())
food_per_day_deer3 = float(input())

needed_food_deer1 = days * food_per_day_deer1
needed_food_deer2 = days * food_per_day_deer2
needed_food_deer3 = days * food_per_day_deer3

total_needed_food = needed_food_deer1 + needed_food_deer2 + needed_food_deer3

if left_food >= total_needed_food:
    food_left = math.floor(left_food - total_needed_food)
    print(f"{food_left} kilos of food left.")
else:
    food_needed = math.ceil(total_needed_food - left_food)
    print(f"{food_needed} more kilos of food are needed.")