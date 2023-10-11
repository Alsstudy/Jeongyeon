def death():
    global dval

    li = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                li.append(getmax(i, j))  # 나무가 존재하는 모든 칸마다 박멸 나무 개수 세기

    li.sort(key=lambda x: (-x[2], x[0], x[1]))  # 가장 조건을 충족시키는 칸
    x, y, val = li[0]

    dval += val

    d = getdir()
    arr[x][y] = 0
    marr[x][y] = c+1
    for i in range(4):
        for j in range(k):
            nx, ny = x + d[i][j][0], y + d[i][j][1]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != -1:
                    marr[nx][ny] = c+1
                if arr[nx][ny] > 0:  # 벽, 제초제가 없고 나무인 경우
                    arr[nx][ny] = 0  # 나무 박멸
                elif arr[nx][ny] == 0 or arr[nx][ny] == -1:  # 나무가 없거나 벽인 경우
                    break


def getdir():
    d = [[] for _ in range(4)]
    for i in range(4):  # 대각선 4개 방향
        for j in range(1, k + 1):  # k만큼 퍼져나감
            nx, ny = ndirect[i][0] * j, ndirect[i][1] * j
            d[i].append((nx, ny))
    return d


def getmax(x, y):
    d = getdir()

    val = arr[x][y]  # 박멸 나무 개수 저장
    for i in range(4):
        for j in range(k):
            nx, ny = x + d[i][j][0], y + d[i][j][1]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > 0 and marr[nx][ny] == 0:  # 벽, 제조체 없고 나무인 경우
                    val += arr[nx][ny]
                elif arr[nx][ny] == 0 or arr[nx][ny] == -1:  # 나무가 없거나 벽인 경우
                    break

    return x, y, val


def getcount(x, y):
    nli = [False] * 4
    cnt = 0

    for d in range(4):
        nx, ny = x + direct[d][0], y + direct[d][1]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 and marr[nx][ny] == 0:  # 나무, 벽, 제초제 모두 없는 경우
            nli[d] = True  # 인접 4개 칸들의 번식 가능 여부
            cnt += 1  # 번식 가능한 나무 개수
    return nli, cnt


def expand():
    v = [[0] * n for _ in range(n)]  # 번식하는 나무 값 저장

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                nli, cnt = getcount(i, j)
                if cnt > 0:
                    val = arr[i][j] // cnt
                    for t in range(4):
                        if nli[t]:
                            v[i + direct[t][0]][j + direct[t][1]] += val  # 번식하는 나무 값 증가

    for i in range(n):
        for j in range(n):
            arr[i][j] += v[i][j]  # 번식


def grow():
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:  # 나무가 존재할 때만 성장함
                cnt = 0
                for d in direct:
                    nx, ny = i + d[0], j + d[1]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                        cnt += 1  # 주위 나무가 존재하는만큼 세기
                arr[i][j] += cnt  # 값 증가


def timeflow():
    for i in range(n):
        for j in range(n):
            if marr[i][j] > 0:
                marr[i][j] -= 1


def check():
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                return True
    return False


n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

marr = [[0] * n for _ in range(n)]  # 제초제 값 저장
direct = [(-1, 0), (1, 0), (0, 1), (0, -1)]
ndirect = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
dval = 0

for i in range(m):
    if check():
        grow()
        expand()
        death()
        timeflow()

print(dval)