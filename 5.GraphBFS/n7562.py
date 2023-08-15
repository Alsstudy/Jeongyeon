from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx, sy):
    queue = deque([(sx, sy)])
    li[sx][sy] = 1

    while queue:
        nx, ny = queue.popleft()
        for i in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]:
            x, y = nx + i[0], ny + i[1]
            if 0 <= x < n and 0 <= y < n:
                if li[x][y] == 0:
                    li[x][y] = li[nx][ny] + 1
                    queue.append((x, y))


t = int(input())

for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    li = [[0] * n for _ in range(n)]
    bfs(sx, sy)
    print(li[ex][ey] - 1)
