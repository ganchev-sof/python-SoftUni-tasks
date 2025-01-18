n = int(input())

for _ in range(n):
    num = int(input())

    if num == 88:
        message = 'Hello'
    elif num == 86:
        message = 'How are you?'
    elif num < 88 and num != 88 and num != 86:
        message = 'GREAT!'
    else:
        message = 'Bye.'

    print(message)