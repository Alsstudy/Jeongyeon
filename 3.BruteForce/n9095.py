t = int(input())

def calculate(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return calculate(n-1) + calculate(n-2) + calculate(n-3)


for i in range(t):
    n = int(input())
    print(calculate(n))