def loser(lidx):
    x, y, d = people[lidx][0], people[lidx][1], people[lidx][2]
    arr[x][y] = arr[x][y] + gunlist[lidx]
    gunlist[lidx] = [0]

    for i in range(0, 4):
        nd = (d + i) % 4
        nx, ny = x + direct[nd][0], y + direct[nd][1]
        if 0 <= nx < n and 0 <= ny < n and len(checkp(nx, ny)) == 0:
            people[lidx][0], people[lidx][1], people[lidx][2] = nx, ny, nd
            return


def getpoint(widx, lidx):
    sumw = sum(gunlist[widx])
    suml = sum(gunlist[lidx])
    p = (people[widx][3] + sumw) - (people[lidx][3] + suml)
    point[widx] += p


def fight(fp):
    i, j = fp[0], fp[1]

    sumi = sum(gunlist[i])
    sumj = sum(gunlist[j])

    if people[i][3] + sumi > people[j][3] + sumj:
        widx, lidx = i, j
    elif people[i][3] + sumi < people[j][3] + sumj:
        widx, lidx = j, i
    else:
        if people[i][3] > people[j][3]:
            widx, lidx = i, j
        else:  # 초기 능력치는 모두 다르므로 else를 사용해도 됨
            widx, lidx = j, i

    return widx, lidx


def getgun(i):
    # 현재 위치의 값과 내가 가진 값 중 큰 것을 가지고, 작은 것을 arr에 위치시킴
    x, y = people[i][0], people[i][1]
    mapgun = arr[x][y]

    if gunlist[i] == [0]:
        if len(mapgun) >= 1:
            mapgun.sort(reverse=True)
            gunlist[i] = [mapgun[0]]
            arr[x][y] = mapgun[1:]
    else:
        ngun = mapgun + gunlist[i]
        ngun.sort(reverse=True)
        gunlist[i] = [ngun[0]]
        arr[x][y] = ngun[1:]


def checkp(x, y):
    li = []
    for i in range(m):
        if people[i][0] == x and people[i][1] == y:
            li.append(i)
    return li


def move(p):
    # 현재 내가 가진 방향대로 1만큼 움직임 - 범위 밖이라면 정반대 방향으로 (d+2) % 4
    px, py, pd = people[p][0], people[p][1], people[p][2]
    nx, ny = px + direct[pd][0], py + direct[pd][1]
    if 0 <= nx < n and 0 <= ny < n:
        people[p][0], people[p][1] = nx, ny
    else:
        nd = (pd + 2) % 4
        nx, ny = px + direct[nd][0], py + direct[nd][1]
        people[p][0], people[p][1], people[p][2] = nx, ny, nd

    return nx, ny


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
people = [list(map(int, input().split())) for _ in range(m)]  # x, y, d, s
gunlist = [[0] for _ in range(m)]
point = [0] * m  # 각 사람별 point
direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(n):
    for j in range(n):
        arr[i][j] = [arr[i][j]]

for i in range(m):
    people[i][0], people[i][1] = people[i][0] - 1, people[i][1] - 1

for _ in range(k):
    for i in range(m):
        x, y = move(i)
        fp = checkp(x, y)
        if len(fp) == 1:
            getgun(i)
        elif len(fp) == 2:
            w, l = fight(fp)
            getpoint(w, l)  # 이긴사람 1. 포인트 획득
            loser(l)  # 진 사람 1. 총 내려놓기, 2. 이동
            getgun(l)
            getgun(w)  # 이긴사람 2. 총 교환

print(' '.join(map(str, point)))