string = input()

while string != 'End':
    if string != 'SoftUni':
        [print(i * 2, end='') for i in string]
        print()
    string = input()