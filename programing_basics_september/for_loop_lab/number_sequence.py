# Въвеждане на броя числа
n = int(input())

# Инициализация на списък, където ще съхраняваме числата
numbers = []

# Четене на числата от потребителя
for i in range(n):
    num = int(input())
    numbers.append(num)

# Намиране на най-голямото и най-малкото число
max_number = max(numbers)
min_number = min(numbers)

# Принтиране на резултата
print("Max number:", max_number)
print("Min number:", min_number)