fruit = input()
day_of_week = input()
quantity = float(input())
price = 0

valid_fruit = True
valid_day = True

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if fruit == 'banana':
        price = quantity * 2.50
    elif fruit == 'apple':
        price = quantity * 1.20
    elif fruit == 'orange':
        price = quantity * 0.85
    elif fruit == 'grapefruit':
        price = quantity * 1.45
    elif fruit == 'kiwi':
        price = quantity * 2.70
    elif fruit == 'pineapple':
        price = quantity * 5.50
    elif fruit == 'grapes':
        price = quantity * 3.85
    else:
        valid_fruit = False

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = quantity * 2.70
    elif fruit == 'apple':
        price = quantity * 1.25
    elif fruit == 'orange':
        price = quantity * 0.90
    elif fruit == 'grapefruit':
        price = quantity * 1.60
    elif fruit == 'kiwi':
        price = quantity * 3.00
    elif fruit == 'pineapple':
        price = quantity * 5.60
    elif fruit == 'grapes':
        price = quantity * 4.20
    else:
        valid_fruit = False

else:
    valid_day = False

if not valid_fruit or not valid_day:
    print('error')
else:
    print(f'{price:.2f}')