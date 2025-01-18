landscape_square_meters = float(input())
price_for_landscaping_the_whole_yard = landscape_square_meters * 7.61

discount = price_for_landscaping_the_whole_yard * 0.18

total_price = price_for_landscaping_the_whole_yard - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")

