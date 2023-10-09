def getpath(sx, sy, cx, cy):
    queue = [[sx, sy, [[sx, sy]]]]
    visited = [[False] * n for _ in range(n)]

    while queue:
        bx, by, li = queue.pop(0)
        for d in direct:
            nx, ny = bx + d[0], by + d[1]
            nli = li[:]
            nli.append([nx, ny])
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != -1 and not visited[nx][ny]:
                queue.append([nx, ny, nli])
                visited[nx][ny] = True
                if nx == cx and ny == cy:
                    return nli, len(nli)
    return False


def bcamp(idx):
    cx, cy = cidx[idx][0], cidx[idx][1]
    dis = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                re = getpath(i, j, cx, cy)
                if re:
                    nli, nlen = re
                    dis.append([nli[0][0], nli[0][1], nlen])
    if len(dis) > 0:
        dis.sort(key=lambda x: (x[2], x[0], x[1]))
        px, py = dis[0][0], dis[0][1]
        arr[px][py] = -1
        pidx[idx] = [px, py]


def move(idx):
    px, py = pidx[idx][0], pidx[idx][1]
    cx, cy = cidx[idx][0], cidx[idx][1]
    re = getpath(px, py, cx, cy)
    if re:
        nli, nlen = re
        nx, ny = nli[1][0], nli[1][1]
        pidx[idx] = [nx, ny]
        if cidx[idx] == [nx, ny]:
            arr[nx][ny] = -1
            goal[idx] = True


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cidx = [list(map(int, input().split())) for _ in range(m)]  # 편의점 위치
pidx = [[-1, -1] for _ in range(m)]  # 사람 위치
cnt = 0  # 시간
direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]
goal = [False] * m

for i in range(m):
    cidx[i][0], cidx[i][1] = cidx[i][0] - 1, cidx[i][1] - 1

while True:
    if all(g for g in goal):
        break
    for j in range(m):
        if not goal[j]:
            if pidx[j] != [-1, -1] and j < cnt:
                move(j)  # 편의점으로 이동
            if cnt <= j and pidx[cnt] == [-1, -1]:
                bcamp(cnt)
    cnt += 1

print(cnt)
