import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
arrb = [list(map(int, input().split())) for _ in range(h+x)]

arra = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        arra[i][j] = arrb[i][j]

for i in range(x, h):
    for j in range(y, w):
        arra[i][j] = arrb[i][j] - arra[i-x][j-y]

for i in range(h):
    print(' '.join(map(str, arra[i])))