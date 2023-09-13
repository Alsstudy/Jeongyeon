def move(x, y, dx, dy):
    c = 0
    if 0 <= x+dx < n and 0 <= x+dy < m:
        while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
            x += dx
            y += dy
            c += 1
    return x, y, c


def bfs():
    while q:
        crx, cry, cbx, cby, cnt = q.pop(0)
        if cnt > 10:
            return -1
        for i in range(4):
            nrx, nry, rc = move(crx, cry, d[i][0], d[i][1])
            nbx, nby, bc = move(cbx, cby, d[i][0], d[i][1])
            if arr[nbx][nby] != 'O':
                if arr[nrx][nry] == 'O':
                    return cnt
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= d[i][0]
                        nry -= d[i][1]
                    else:
                        nbx -= d[i][0]
                        nby -= d[i][1]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, cnt+1))
    return -1


n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

q = []
q.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = True
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(bfs())