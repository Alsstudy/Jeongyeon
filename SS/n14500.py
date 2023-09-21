def move(cnt, x, y, val):
    global maxVal
    if cnt == 4:
        maxVal = max(maxVal, val)
        return

    if not visited[x][y]:
        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + i[0] < n and 0 <= y + i[1] < m:
                visited[x][y] = True
                move(cnt+1, x + i[0],  y + i[1], val+arr[x][y])


def check():
    global maxVal
    for j in range(m-2):
        maxVal = max(sum(arr[0][j:j+3]) + arr[1][j+1], maxVal)
        maxVal = max(sum(arr[n-1][j:j+3]) + arr[n-2][j+1], maxVal)

    for i in range(1, n-1):
        for j in range(m-2):
            maxVal = max(sum(arr[i][j:j+3]) + max(arr[i-1][j+1], arr[i+1][j+1]), maxVal)

    for i in range(n-2):
        maxVal = max(arr[i][0] + arr[i+1][0], arr[i+2][0] + arr[i+1][1], maxVal)
        maxVal = max(arr[i][m-1] + arr[i+1][m-1] + arr[i+2][m-1] + arr[i+1][m-1], maxVal)

    for i in range(n-2):
        for j in range(1, m-1):
            maxVal = max(arr[i][j] + arr[i+1][j] + arr[i+2][j] + max(arr[i+1][j-1], arr[i+1][j+1]), maxVal)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
maxVal = arr[0][0]

for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        move(0, i, j, 0)

check()

print(maxVal)