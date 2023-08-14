def bfs():
    queue = [(0, 0)]

    while queue:
        (x, y) = queue.pop(0)
        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + i[0]
            ny = y + i[1]
            if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 1:
                queue.append((nx, ny))
                li[nx][ny] = li[x][y] + 1


n, m = map(int, input().split())
li = [list(map(int, input())) for _ in range(n)]

bfs()
print(li[n-1][m-1])