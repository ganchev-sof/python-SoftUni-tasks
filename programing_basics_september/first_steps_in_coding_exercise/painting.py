price_nylon = 1.50
price_paint = 14.50
price_thinner = 5.00
price_bags = 0.40
percent_additionally_paint = 0.10
additionally_nylon = 2
percent_workers = 0.30

qty_nylon = int(input())
qty_paint = int(input())
qty_thinner = int(input())
hours_to_finish = int(input())

qty_nylon = qty_nylon + additionally_nylon
qty_paint = qty_paint + (qty_paint * percent_additionally_paint)

sum_materials = (qty_paint * price_paint) + (qty_thinner * price_thinner) + (qty_nylon * price_nylon) + price_bags
sum_repairs = (sum_materials * percent_workers) * hours_to_finish
total_sum = sum_materials + sum_repairs

print(total_sum)
