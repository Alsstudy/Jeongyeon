import sys
input = sys.stdin.readline


def rotate(i, j, n, m):
    top = li[i][j]
    left = li[n-1][i]
    right = li[i][m-1]
    bottom = li[n-1][m-1]

    for x in range(n-1, i, -1):
        li[x][j] = li[x-1][j]
    for x in range(i, n-1):
        li[x][m-1] = li[x+1][m-1]
    for y in range(j, m-1):
        li[i][y] = li[i][y+1]
    for y in range(m-1, j, -1):
        li[n-1][y] = li[n-1][y-1]

    li[i+1][j] = top
    li[n-1][j+1] = left
    li[i][m-2] = right
    li[n-2][m-1] = bottom


n, m, r = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

depth = min(n, m) // 2
cycle = 2 * (n-1) + 2 * (m-1)

for i in range(depth):
    for _ in range(r % cycle):
        rotate(i, i, n-i, m-i)
    cycle -= 8

for i in li:
    print(' '.join(map(str, i)))