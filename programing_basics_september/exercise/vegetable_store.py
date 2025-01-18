price_vegetables = float(input())
price_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

earned_lvl = (price_vegetables * kg_vegetables) + (price_fruits * kg_fruits)
earned_eur = earned_lvl / 1.94

print(f"{earned_eur:.2f}")