import sys
input = sys.stdin.readline


def operation(arr, len, k, step):
    narr = [[0] * len for _ in range(len)]

    if k == 1:
        for i in range(len // step):
            for u in range(step // 2 + 1):
                narr[(step * i) + u], narr[(step * (i + 1)) - 1 - u] = arr[(step * (i + 1)) - 1 - u], arr[(step * i) + u]
        return narr

    elif k == 2:
        for i in range(len // step):
            for j in range(len // step):
                for u in range(step):
                    for v in range(step):
                        narr[(step*i) + u][(step * j) + v] = arr[(step * i) + u][(step * (j + 1)) - 1 - v]
        return narr

    elif k == 3:
        for i in range(len // step):
            for j in range(len // step):
                for u in range(step):
                    for v in range(step):
                        narr[(step*i) + u][(step * j) + v] = arr[(step * i) + step - 1 - v][(step * j) + u]
        return narr

    elif k == 4:
        for i in range(len // step):
            for j in range(len // step):
                for u in range(step):
                    for v in range(step):
                        narr[(step*i) + u][(step * j) + v] = arr[(step * i) + v][(step * j) + step - 1 - u]
        return narr

    elif k == 5:
        narr = operation(arr, len, 1, len)
        narr = operation(narr, len, 1, step)
        return narr

    elif k == 6:
        narr = operation(arr, len, 2, len)
        narr = operation(narr, len, 2, step)
        return narr

    elif k == 7:
        narr = operation(arr, len, 3, len)
        narr = operation(narr, len, 4, step)
        return narr

    elif k == 8:
        narr = operation(arr, len, 4, len)
        narr = operation(narr, len, 3, step)
        return narr


n, r = map(int, input().split())

len = pow(2, n)
arr = [list(map(int, input().split())) for _ in range(len)]

for _ in range(r):
    k, l = map(int, input().split())

    step = pow(2, l)

    arr = operation(arr, len, k, step)

for i in arr:
    print(' '.join(map(str, i)))