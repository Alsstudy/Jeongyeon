def changedir(tidx):
    li = team[tidx]
    nlen = len(li)

    fidx, bidx = 0, 0

    for i in range(nlen):
        if li[i][-1] == 1:
            fidx = i
        if li[i][-1] == 3:
            bidx = i

    li[fidx][-1] = 3
    li[bidx][-1] = 1


def countplus(li, sidx, x, y):
    global val
    nlen = len(li)
    v = 0
    for i in range(sidx, sidx+nlen):
        ni = i % nlen
        if li[ni][-1] != 4:
            v += 1
            if li[ni][:2] == [x, y]:
                val += pow(v, 2)
                return


def countminus(li, sidx, x, y):
    global val
    nlen = len(li)
    v = 0
    for i in range(nlen):
        ni = sidx - i
        if li[ni][-1] != 4:
            v += 1
            if li[ni][:2] == [x, y]:
                val += pow(v, 2)
                return


def getscore(tidx, pidx):
    global val
    li = team[tidx]
    nlen = len(li)
    px, py = li[pidx][0], li[pidx][1]

    for i in range(nlen):
        if li[i][-1] == 1:
            if li[i-1][-1] < li[(i+1) % nlen][-1]:
                countminus(li, i, px, py)
                return
            elif li[i-1][-1] > li[(i+1) % nlen][-1]:
                countplus(li, i, px, py)
                return


def catch(li):
    for i in li:
        for j in range(m):
            for t in range(len(team[j])):
                if team[j][t][:2] == i and team[j][t][-1] != 4:
                    getscore(j, t)
                    changedir(j)
                    return


def ball(r):
    r = r % (4 * n)
    nr = r % n
    d = []
    if r < n:  # 1
        for i in range(n):
            d.append([nr, i])
    elif r < 2 * n:  # 2
        for i in range(n-1, -1, -1):
            d.append([i, nr])
    elif r < 3 * n:  # 3
        for i in range(n-1, -1, -1):
            d.append([n-nr-1, i])
    else:  # 4
        for i in range(n):
            d.append([i, n-nr-1])
    catch(d)


def moveplus(idx):
    li = team[idx]
    nlen = len(li)

    bef = li[nlen-1][-1]
    for i in range(0, nlen-1):
        cur = li[i][-1]
        li[i][-1] = bef
        bef = cur
    li[nlen-1][-1] = bef


def moveminus(idx):
    li = team[idx]
    nlen = len(li)

    nxt = li[0][-1]
    for i in range(nlen-1, 0, -1):
        cur = li[i][-1]
        li[i][-1] = nxt
        nxt = cur
    li[0][-1] = nxt


def move(idx):
    li = team[idx]
    nlen = len(li)

    for i in range(nlen):
        if li[i][-1] == 1:
            if li[i-1][-1] < li[(i+1) % nlen][-1]:
                moveplus(idx)
                return
            elif li[i-1][-1] > li[(i+1) % nlen][-1]:
                moveminus(idx)
                return

def getteam(x, y, idx):
    if arr[x][y] == 0:
        return

    for d in direct:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                team[idx].append([nx, ny, arr[nx][ny]])
                getteam(nx, ny, idx)


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 각 팀 정보 구하기
visited = [[False] * n for _ in range(n)]
team = [[] for _ in range(m)]
cnt = 0
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and not visited[i][j]:
            visited[i][j] = True
            team[cnt] = [[i, j, arr[i][j]]]
            getteam(i, j, cnt)
            cnt += 1

val = 0
for i in range(k):
    for j in range(m):
        move(j)
    ball(i)

print(val)
