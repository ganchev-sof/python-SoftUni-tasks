number = int(input())

if number < 111 or number > 999:
    print("Числото трябва да е в интервала [111...999].")
else:
    digit1 = number % 10
    digit2 = (number // 10) % 10
    digit3 = number // 100

    for i in range(1, digit1 + 1):
        for j in range(1, digit2 + 1):
            for k in range(1, digit3 + 1):
                result = i * j * k
                print(f"{i} * {j} * {k} = {result};")