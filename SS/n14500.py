def dfs(x, y, cnt, sum):
    global maxVal

    if cnt == 4:
        maxVal = max(maxVal, sum)
        return

    for i in move:
        nx = x + i[0]
        ny = y + i[1]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, sum+arr[nx][ny])
            visited[nx][ny] = False


def exce(x, y):
    global maxVal

    for i in range(4):
        sum = arr[x][y]
        for j in range(3):
            idx = (i+j) % 4
            nx = x + move[idx][0]
            ny = y + move[idx][1]
            if 0 <= nx < n and 0 <= ny < m:
                sum += arr[nx][ny]
            else:
                sum = 0
                break

        maxVal = max(maxVal, sum)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

maxVal = 0
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False
        exce(i, j)

print(maxVal)