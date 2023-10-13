def foldtwice():  # 두 번 반으로 접어주기
    narr = arr[:]
    nlen = len(narr) // 2  # 첫번째 반절 접기
    bef = [narr[:nlen]]
    aft = narr[nlen:]
    bef = rotate(bef)
    bef = rotate(bef)
    bef.append(aft)

    nbef = []  # 두번째 반절 접기
    naft = []
    nnlen = nlen // 2

    for i in range(2):
        tmp = []
        for j in range(nnlen):
            tmp.append(bef[i][j])
        nbef.append(tmp)
        tmp = []
        for j in range(nnlen, nlen):
            tmp.append(bef[i][j])
        naft.append(tmp)

    nbef = rotate(nbef)
    nbef = rotate(nbef)
    for a in naft:
        nbef.append(a)

    return nbef


def pushdown(narr):  # 눌러주기
    direct = [(1, 0), (0, 1)]
    xlen = len(narr)
    ylen = [len(a) for a in narr]
    mylen = max(ylen)
    li = [[False] * mylen for _ in range(xlen)]

    for i in range(xlen):
        for j in range(ylen[i]):
            li[i][j] = narr[i][j]

    for i in range(xlen):
        for j in range(ylen[i]):
            for d in direct:
                nx, ny = i+d[0], j+d[1]
                if 0 <= nx < xlen and 0 <= ny < ylen[nx] and li[nx][ny]:
                    val = abs(narr[i][j]-narr[nx][ny]) // 5
                    if narr[i][j] > narr[nx][ny]:
                        li[i][j] -= val
                        li[nx][ny] += val
                    elif narr[i][j] < narr[nx][ny]:
                        li[i][j] += val
                        li[nx][ny] -= val
    nli = []
    for j in range(mylen):
        for i in range(xlen-1, -1, -1):
            if li[i][j]:
                nli.append(li[i][j])
    return nli


def rotate(narr):
    xlen = len(narr)  # 3
    ylen = len(narr[0])  # 2
    li = [[0] * xlen for _ in range(ylen)]

    for i in range(xlen):
        for j in range(ylen-1, -1, -1):
            li[j][xlen-i-1] = narr[i][j]

    return li



def rollup():  # 말아주기
    narr = arr[:]
    li = []

    cnt = 2
    for i in range(len(arr)//2-1):  # 말아주기
        if i == 0:
            li.append([narr[1], narr[0]])
            narr = narr[cnt:]
        else:
            cnt = len(li[0])
            li.append(narr[:cnt])
            li = rotate(li)
            narr = narr[cnt:]
        if len(li)+1 > len(narr)-cnt:  # 만약 맨 밑에가 작아진다면, 멈춤
            li.append(narr)
            return li

    return li


def addone():  # 가장 작은 위치에 +1
    minval = min(arr)

    for i in range(n):
        if arr[i] == minval:
            arr[i] += 1


n, k = map(int, input().split())
arr = list(map(int, input().split()))
# print(arr)
# while 문으로 변경
cval = 0
while max(arr) - min(arr) > k:
    cval += 1
    addone()  # 가장 작은 위치에 +1
    rarr = rollup()  # 말아주기
    arr = pushdown(rarr)  # 눌러주기
    trarr = foldtwice()  # 두 번 반으로 접어주기
    arr = pushdown(trarr)  # 눌러주기

print(cval)