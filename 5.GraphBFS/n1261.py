from collections import deque


def bfs():
    while queue:
        nx, ny = queue.popleft()

        if nx == n-1 and ny == m-1:
            print(v[nx][ny])
            return

        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = nx + i[0]
            y = ny + i[1]
            if 0 <= x < n and 0 <= y < m:
                # print(v)
                if v[x][y] == -1:
                    if li[x][y] == 0:
                        queue.appendleft((x, y))
                        # print(queue)
                    if li[x][y] == 1:
                        queue.append((x, y))
                        # print(queue)
                    v[x][y] = v[nx][ny] + li[x][y]


m, n = map(int, input().split())
li = [list(map(int, input())) for _ in range(n)]
v = [[-1] * m for _ in range(n)]

queue = deque([])
queue.append((0, 0))

v[0][0] = 0
bfs()
