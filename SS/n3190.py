def change(i):
    global didx

    if c[i] == 'D':
        didx += 1
        if didx == 4:
            didx = 0
    elif c[i] == 'L':
        didx -= 1
        if didx == -1:
            didx = 3


n = int(input())
arr = [[0] * n for _ in range(n)]

k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = -1

l = int(input())
x = []
c = []
for i in range(l):
    a, b = map(str, input().split())
    x.append(int(a))
    c.append(b)

didx = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

xidx, yidx, txidx, tyidx = 0, 0, 0, 0
cnt = 0

step = [(0, 0)]
while True:
    cnt += 1
    if 0 <= xidx + d[didx][0] < n and 0 <= yidx + d[didx][1] < n and arr[xidx + d[didx][0]][yidx + d[didx][1]] != 1:
        xidx += d[didx][0]
        yidx += d[didx][1]

        if arr[xidx][yidx] == -1:
            step.append((xidx, yidx))
            arr[xidx][yidx] = 1
        else:
            step.append((xidx, yidx))
            arr[xidx][yidx] = 1
            txidx, tyidx = step.pop(0)
            arr[txidx][tyidx] = 0

        if cnt in x:
            change(x.index(cnt))

    else:
        break

print(cnt)