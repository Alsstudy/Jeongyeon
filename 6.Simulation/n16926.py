import sys
input = sys.stdin.readline


def roat(a):
    arr = [[-1] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(i+1, m-i):
            arr[i][j-1] = a[i][j]
        for j in range(i, m - i - 1):
            arr[n-i-1][j+1] = a[n-i-1][j]

    for j in range(m // 2):
        for i in range(j, n-j-1):
            arr[i+1][j] = a[i][j]
        for i in range(j+1, n-j):
            arr[i-1][m-j-1] = a[i][m-j-1]

    return arr


n, m, r = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

nli = roat(li)
for i in range(r-1):
    nli = roat(nli)

for i in nli:
    print(' '.join(map(str, i)))
