def dfs(x, y):
    global val

    if li[x][y] != 1:
        return

    if li[x][y] == 1:
        li[x][y] = 0
        val += 1
        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + i[0]
            ny = y + i[1]
            if 0 <= nx < n and 0 <= ny < n:
                dfs(nx, ny)

    return val


n = int(input())
li = [list(map(int, input())) for _ in range(n)]

cnt = 0
v = []

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            cnt += 1
            val = 0
            v.append(dfs(i, j))

print(cnt)
v.sort()
for i in v:
    print(i)
