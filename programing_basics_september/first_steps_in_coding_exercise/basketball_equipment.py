basketball_shoes = 0.40
basketball_training_clothes = 0.20
ball = 0.25
basketball_accessories = 0.20

annual_tax = int(input())

basketball_shoes = annual_tax - (annual_tax * basketball_shoes)
basketball_training_clothes = basketball_shoes - (basketball_shoes * basketball_training_clothes)
ball = basketball_training_clothes * ball
basketball_accessories = ball * basketball_accessories

total_sum = annual_tax + basketball_shoes + basketball_accessories + basketball_training_clothes + ball

print(total_sum)