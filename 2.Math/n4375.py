while True:
    try:
        n = int(input())
        num = 0
        i = 1
    except EOFError:
        break
    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1