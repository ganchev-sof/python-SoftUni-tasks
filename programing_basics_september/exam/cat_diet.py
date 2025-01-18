FAT_CALORIES_PER_GRAM = 9
PROTEIN_CALORIES_PER_GRAM = 4
CARB_CALORIES_PER_GRAM = 4

fat_percentage = int(input())
protein_percentage = int(input())
carb_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())

# Calculate the grams of each macronutrient
total_fat_grams = (fat_percentage / 100) * (total_calories / FAT_CALORIES_PER_GRAM)
total_protein_grams = (protein_percentage / 100) * (total_calories / PROTEIN_CALORIES_PER_GRAM)
total_carb_grams = (carb_percentage / 100) * (total_calories / CARB_CALORIES_PER_GRAM)

# Calculate the total grams of food (before subtracting water)
total_food_grams = total_fat_grams + total_protein_grams + total_carb_grams

# Calculate the calories per gram of food
calories_per_gram_before_water = total_calories / total_food_grams

# Calculate the actual calories per gram of food after removing water
calories_per_gram_after_water = calories_per_gram_before_water * (1 - water_percentage / 100)

print(f"{calories_per_gram_after_water:.4f}")