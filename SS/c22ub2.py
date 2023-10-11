def rotatemid(idx):
    narr = [a[:] for a in arr]

    for j in range(n-1, -1, -1):
        for i in range(n):
            narr[n-j-1][i] = arr[i][j]
    for i in range(n):
        for j in range(n):
            if i == idx or j == idx:
                arr[i][j] = narr[i][j]


def rotateside(sx, ex, sy, ey):
    narr = [a[:] for a in arr]
    cx, cy = 0, 0
    for j in range(sy, ey):
        cy = 0
        for i in range(ex-1, sx-1, -1):
            arr[sx+cx][sy+cy] = narr[i][j]
            cy += 1
        cx += 1


def rotate():
    mid = n // 2
    rotatemid(mid)
    rotateside(0, mid, 0, mid)
    rotateside(0, mid, mid+1, n)
    rotateside(mid+1, n, 0, mid)
    rotateside(mid+1, n, mid+1, n)


def compute(aidx, bidx):  # a와 b의 점수 계산
    global score

    ali = gli[aidx]
    bli = gli[bidx]

    dval = 0  # 맞닿아 있는 변의 수
    for i in ali:
        ax, ay = i[0], i[1]
        for d in direct:
            nax, nay = ax + d[0], ay + d[1]
            if [nax, nay] in bli:
                dval += 1
    if dval == 0:
        return

    acnt = len(ali)  # a에 속한 칸의 수
    bcnt = len(bli)  # b에 속한 칸의 수
    aval = arr[ali[0][0]][ali[0][1]]  # a를 이루고 있는 숫자 값
    bval = arr[bli[0][0]][bli[0][1]]  # b를 이루고 있는 숫자 값

    score += ((acnt + bcnt) * aval * bval * dval)


def getscore(length):  # 조합 구하기
    for i in range(length):
        for j in range(i+1, length):
            compute(i, j)  # a와 b의 점수 계산


def dfs(i, j, val, li):  # dfs 활용해서 각 그룹 찾기
    if arr[i][j] != val:
        return

    for d in direct:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < n and 0 <= nj < n:
            if not visited[ni][nj] and arr[ni][nj] == val:
                visited[ni][nj] = True
                li.append([ni, nj])
                dfs(ni, nj, val, li)

    return li

def findgroup():  # 그룹 찾기
    li = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                li.append(dfs(i, j, arr[i][j], [[i, j]]))

    return li


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
score = 0

for i in range(4):
    visited = [[False] * n for _ in range(n)]
    gli = findgroup()  # 그룹 찾기
    nlen = len(gli)
    if nlen > 1:  # 그룹이 2개 이상일 경우
        getscore(nlen)
        rotate()

print(score)