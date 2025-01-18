import math

N = int(input())
M = float(input())

total_distance = M
current_distance = M

for _ in range(N):
    K = int(input())
    current_distance += current_distance * (K / 100)
    total_distance += current_distance

if total_distance >= 1000:
    extra_distance = total_distance - 1000
    print(f"You've done a great job running {math.ceil(extra_distance)} more kilometers!")
else:
    deficit = 1000 - total_distance
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(deficit)} more kilometers")