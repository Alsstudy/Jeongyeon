from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        nx, ny = queue.popleft()
        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = nx + i[0]
            y = ny + i[1]
            if 0 <= x < n and 0 <= y < m:
                if li[x][y] == 0:
                    li[x][y] = li[nx][ny] + 1
                    queue.append((x, y))


m, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            queue.append((i, j))

bfs()

res = 0
for i in li:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)