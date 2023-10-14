def reindex(li):  # 재배열
    nli = []
    nlen = len(li)
    for i in range(nlen):
        cnt = 1
        for j in range(i+1, nlen):
            if li[i] == li[j] and li[j] != -1:
                li[j] = -1
                cnt += 1
            else:
                break
        if li[i] != -1:
            nli.append(cnt)
            nli.append(li[i])

    makearr(nli)


def remove(li):
    nli = []
    for i in li:
        if i > 0:
            nli.append(i)

    return nli


def check(li):  # 확인
    global totcnt
    nlen = len(li)
    mark = True

    for i in range(nlen-1):
        nli = [i]
        for j in range(i+1, nlen):
            if li[i] == li[j] and li[j] != -1:
                nli.append(j)
            else:
                break
        if len(nli) >= 4:
            mark = False
            if li[i] != -1:
                totcnt += li[i] * len(nli)
            for j in nli:
                li[j] = -1

    return mark, li


def duplicate():
    nli = getarr()
    v, li = check(nli)

    while v != True:
        li = remove(li)
        v, li = check(li)

    return remove(li)


def makearr(nli):
    nlen, plen = len(nli), len(parr)
    sx, sy = parr[0][0], parr[0][1]
    for i in range(plen):
        if i < nlen:
            arr[sx][sy] = nli[i]
        else:
            arr[sx][sy] = 0
        d = parr[i][2]
        sx, sy = sx + direct[d][0], sy + direct[d][1]



def getarr():  # 나선형 모양을 일차원 배열로 얻어오기 0이 아닌 것만 취급함
    li = []
    nlen = len(parr)

    sx, sy = parr[0][0], parr[0][1]
    for i in range(nlen):
        if arr[sx][sy] != 0:
            li.append(arr[sx][sy])
        d = parr[i][2]
        sx, sy = sx + direct[d][0], sy + direct[d][1]

    return li


def move():  # 이동
    nli = getarr()  # 현재 값 가져오기 0제외
    makearr(nli)


def attack(d, p):  # 공격
    global totcnt

    cx, cy = n // 2, n // 2
    for i in range(p):
        nx, ny = cx + direct[d][0], cy + direct[d][1]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] != 0:
                totcnt += arr[nx][ny]
                arr[nx][ny] = 0
        cx, cy = nx, ny


def getpath():
    sx, sy = n // 2, n // 2
    li = []
    sd = 2
    v = 1
    for i in range(n - 2):
        for j in range(2):
            for k in range(v):
                li.append((sx, sy, sd))
                nx, ny = sx + direct[sd][0], sy + direct[sd][1]
                sx, sy = nx, ny
            sd = (sd - 1) % 4
        v += 1
    for j in range(3):
        for k in range(v):
            li.append((sx, sy, sd))
            nx, ny = sx + direct[sd][0], sy + direct[sd][1]
            sx, sy = nx, ny
        sd = (sd - 1) % 4

    return li


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
marr = [list(map(int, input().split())) for _ in range(m)]

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
parr = getpath()
parr.pop(0)

totcnt = 0
for i in range(m):
    attack(marr[i][0], marr[i][1])
    move()
    narr = duplicate()
    reindex(narr)

print(totcnt)
