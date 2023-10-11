def getpoint(step):
    global point

    cnt = 0
    for i in range(3):
        ncx, ncy = cx + direct[cd][0] * i, cy + direct[cd][1] * i
        for i in range(m):
            if people[i]:
                if people[i][:2] == [ncx, ncy] and [ncx, ncy] not in tree:
                    cnt += 1
                    people[i] = []

    point += cnt * (step+1)


def move(step):
    global cx, cy, cd
    nlen = len(path)

    cx += path[step % nlen][0]
    cy += path[step % nlen][1]
    cd = dlist[(step+1) % nlen]


def run():
    for i in range(m):
        if people[i]:
            px, py, pd = people[i][0], people[i][1], people[i][2]
            if abs(px - cx) + abs(py - cy) <= 3:  # 술래와의 거리가 3 이하인 도망자만 움직임
                nx, ny = px + direct[pd][0], py + direct[pd][1]
                if 0 <= nx < n and 0 <= ny < n:  # 범위 안인 경우
                    if not (nx == cx and ny == cy):  # 술래가 없는 경우, 이동함
                        people[i][0], people[i][1] = nx, ny
                else:  # 범위 밖인 경우
                    nd = (pd + 2) % 4  # 방향 반대로
                    nx, ny = px + direct[nd][0], py + direct[nd][1]
                    if not (nx == cx and ny == cy):  # 술래가 없는 경우, 이동함
                        people[i][0], people[i][1], people[i][2] = nx, ny, nd


def makepath():
    li = []
    dli = []

    pd = 0
    for i in range(1, n-1):
        for j in range(2):
            for k in range(i):
                li.append(direct[pd])
                dli.append(pd)
            pd = (pd+1) % 4

    for j in range(3):
        for k in range(n-1):
            li.append(direct[pd])
            dli.append(pd)
        pd = (pd+1) % 4

    pd = 2
    for j in range(3):
        for k in range(n-1):
            li.append(direct[pd])
            dli.append(pd)
        pd = (pd-1) % 4

    for i in range(n-2, 0, -1):
        for j in range(2):
            for k in range(i):
                li.append(direct[pd])
                dli.append(pd)
            pd = (pd-1) % 4

    return li, dli


n, m, h, k = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(m)]   # x, y, d
tree = [list(map(int, input().split())) for _ in range(h)]  # x, y

for i in range(m):
    people[i][0], people[i][1] = people[i][0] - 1, people[i][1] - 1

for i in range(h):
    tree[i][0], tree[i][1] = tree[i][0] - 1, tree[i][1] - 1

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌
cx, cy, cd = n // 2, n // 2, 0
path, dlist = makepath()

point = 0
for i in range(k):
    if not all(p == [] for p in people):
        run()
        move(i)
        getpoint(i)

print(point)