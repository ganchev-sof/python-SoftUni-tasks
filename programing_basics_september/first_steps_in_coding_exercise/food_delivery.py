chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
price_delivery_food = 2.50
percent_desert = 0.20

qty_chicken_menu = int(input())
qty_fish_menu = int(input())
qty_vegan_menu = int(input())

sum_menus = ((qty_vegan_menu * vegan_menu)
             + (qty_fish_menu * fish_menu)
             + (qty_chicken_menu * chicken_menu))
price_desert = sum_menus * percent_desert
total_sum = sum_menus + price_desert + price_delivery_food

print(total_sum)
