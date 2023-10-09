def attack(sx, sy, ex, ey, rlist):
    arr[sx][sy] += (n + m)
    dval = arr[sx][sy]

    for r in rlist:
        rx, ry = r[0], r[1]
        if ex == rx and ey == ry:
            arr[rx][ry] = max(arr[rx][ry]-dval, 0)
        elif not (rx == sx and ry == sy):
            arr[rx][ry] = max(arr[rx][ry] - dval//2, 0)

    for i in range(n):
        for j in range(m):
            if [i, j] not in rlist:
                if not (i == sx and j == sy) and arr[i][j] != 0:  # 정비
                    arr[i][j] = arr[i][j] + 1


def makeside(ex, ey):
    rlist = [[ex, ey]]
    side = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for s in side:
        nx, ny = (ex + s[0]) % n, (ey + s[1]) % m
        rlist.append([nx, ny])

    return rlist


def makeroot(sx, sy, ex, ey):
    queue = []
    queue.append([sx, sy, []])
    visited = [[False] * m for _ in range(n)]

    while queue:
        bx, by, li = queue.pop(0)
        visited[bx][by] = True
        for i in direct:
            nx, ny = (bx + i[0]) % n, (by + i[1]) % m
            if arr[nx][ny] != 0 and not visited[nx][ny]:
                nli = li[:]
                nli.append([nx, ny])
                queue.append([nx, ny, nli])
                visited[nx][ny] = True
                if [nx, ny] == [ex, ey]:
                    return nli


def pickgoal():
    nli = []  # i, j, arr[i][j], alist[i][j]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                nli.append([i, j, arr[i][j], alist[i][j]])

    nli.sort(key=lambda x: (x[2], -x[3], -(x[0]+x[1]), -x[1]))
    return nli[0][:2], nli[-1][:2]


def count0():
    cnt = 0
    for a in arr:
        for i in a:
            if i == 0:
                cnt += 1
    return cnt


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
alist = [[0] * m for _ in range(n)]  # 공격 시간
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상 우선순위

for i in range(k):
    if count0() == n*m-1:  # 1개만 제외하고 전부 0일때
        break
    else:
        [fx, fy], [tx, ty] = pickgoal()  # 공격자, 공격대상자 선정
        alist[fx][fy] = i+1  # 공격 시간 업데이트
        path = makeroot(fx, fy, tx, ty)  # 경로 탐색
        if not path:
            path = makeside(tx, ty)  # 레이저 공격 및 정비
        attack(fx, fy, tx, ty, path)

print(max(max(a) for a in arr))