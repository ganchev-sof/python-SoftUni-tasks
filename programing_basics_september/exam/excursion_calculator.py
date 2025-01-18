people = int(input())
season = input("Enter the season ( eg. spring, summer, autumn, winter): ").strip().lower()
price = 0

if people <= 5:
    if season == 'spring':
        price = 50.00
    elif season == 'summer':
        price = 48.50
    elif season == 'autumn':
        price = 60.00
    elif season == 'winter':
        price = 86.00
else:
    if season == 'spring':
        price = 48.00
    elif season == 'summer':
        price = 45.00
    elif season == 'autumn':
        price = 49.50
    elif season == 'winter':
        price = 85.00

total_sum = price * people

if season == 'summer':
    total_sum *= 0.85
elif season == 'winter':
    total_sum *= 1.08

print(f"{total_sum:.2f} leva.")