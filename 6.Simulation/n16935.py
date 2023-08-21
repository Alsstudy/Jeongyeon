import sys
input = sys.stdin.readline

def k1(a, u, v):
    for i in range(u//2):
        arr = a[i]
        a[i] = a[u-i-1]
        a[u-i-1] = arr

    return a, u, v

def k2(a, u, v):
    for i in range(u):
        for j in range(v // 2):
            val = a[i][j]
            a[i][j] = a[i][v-j-1]
            a[i][v-j-1] = val

    return a, u, v

def k3(a, u, v):
    nli = [[-1] * u for _ in range(v)]

    for i in range(u):
        for j in range(v):
            nli[j][u-i-1] = a[i][j]

    return nli, v, u

def k4(a, u, v):
    nli = [[-1] * u for _ in range(v)]

    for i in range(u):
        for j in range(v):
            nli[v-j-1][i] = a[i][j]

    return nli, v, u

def k5(a, u, v):
    nli = [[-1] * v for _ in range(u)]

    for i in range(u//2):
        for j in range(v//2):
            nli[i][j+v//2] = a[i][j]
        for j in range(v//2, v):
            nli[i+u//2][j] = a[i][j]

    for i in range(u//2, u):
        for j in range(v//2):
            nli[i-u//2][j] = a[i][j]
        for j in range(v//2, v):
            nli[i][j-v//2] = a[i][j]

    return nli, u, v

def k6(a, u, v):
    nli = [[-1] * v for _ in range(u)]

    for i in range(u//2):
        for j in range(v//2):
            nli[i+u//2][j] = a[i][j]
        for j in range(v//2, v):
            nli[i][j-v//2] = a[i][j]

    for i in range(u//2, u):
        for j in range(v//2):
            nli[i][j+v//2] = a[i][j]
        for j in range(v//2, v):
            nli[i-u//2][j] = a[i][j]

    return nli, u, v

n, m, r = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

k = list(map(int, input().split()))

a = li.copy()
u = n
v = m
for i in k:
    if i == 1:
        a, u, v = k1(a, u, v)
    if i == 2:
        a, u, v = k2(a, u, v)
    if i == 3:
        a, u, v = k3(a, u, v)
    if i == 4:
        a, u, v = k4(a, u, v)
    if i == 5:
        a, u, v = k5(a, u, v)
    if i == 6:
        a, u, v = k6(a, u, v)


for i in range(u):
    print(' '.join(map(str, a[i])))
