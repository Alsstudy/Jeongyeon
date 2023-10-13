def wminus():
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                if carr[i][j] != 0:
                    carr[i][j] -= 1


def wmix():
    li = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for d in [0, 1]:
                nx, ny = i+direct[d][0], j+direct[d][1]
                if 0 <= nx < n and 0 <= ny < n:
                    if (i, j, d) not in warr:
                        val = abs(carr[i][j] - carr[nx][ny]) // 4
                        if carr[i][j] > carr[nx][ny]:
                            li[i][j] += -val
                            li[nx][ny] += val
                        if carr[i][j] < carr[nx][ny]:
                            li[i][j] += val
                            li[nx][ny] += -val

    for i in range(n):
        for j in range(n):
            carr[i][j] += li[i][j]


def bfs(x, y, d, li):
    queue = [(x + direct[d][0], y + direct[d][1], 0)]
    visited = [[False] * n for _ in range(n)]
    li[x+direct[d][0]][y+direct[d][1]] += 5
    visited[x+direct[d][0]][y+direct[d][1]] = True

    while queue:
        bx, by, val = queue.pop(0)
        if val > 4:
            return li
        for pli in path:
            nbx, nby = bx, by
            mark = False
            for p in pli:  # 3가지 경로
                nd = (d + p) % 4
                nx, ny = nbx + direct[nd][0], nby + direct[nd][1]
                if 0 <= nx < n and 0 <= ny < n:
                    if (nbx, nby, nd) not in warr:  # 벽이 없고 이미 방문한 곳이 아닌 경우
                        mark = True
                    else:  # 벽이 있거나, 이미 방문한 곳인 경우
                        mark = False
                        break
                    nbx, nby = nx, ny
                else:
                    mark = False
            if mark and not visited[nbx][nby]:  # 조건에 충족하는 경우
                li[nbx][nby] += 5-val-1
                visited[nbx][nby] = True
                queue.append((nbx, nby, val+1))

    return li


def wspread():
    li = [[0] * n for _ in range(n)]  # 추가되는 시원한 공기들
    for i in range(len(narr)):
        x, y, d = narr[i][0], narr[i][1], narr[i][2] % 4
        li = bfs(x, y, d, li)

    for i in range(n):
        for j in range(n):
            carr[i][j] += li[i][j]


def getwall():
    li = []
    for i in range(m):
        if warr[i][2] == 0:
            li.append((warr[i][0]-1, warr[i][1]-1, 3))
            li.append((warr[i][0]-2, warr[i][1]-1, 1))
        if warr[i][2] == 1:
            li.append((warr[i][0]-1, warr[i][1]-1, 2))
            li.append((warr[i][0]-1, warr[i][1]-2, 0))
    return li


def check():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and carr[i][j] < k:
                return False
    return True


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # 사무실, 에어컨 정보
warr = [list(map(int, input().split())) for _ in range(m)]  # 벽 정보
warr = getwall()
warr = set(warr)

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽 0 - 아래 1 - 왼쪽 2 - 위 3
path = [[0], [1, 0], [-1, 0]]  # 직진, 오른쪽 아래, 왼쪽 아래
carr = [[0] * n for _ in range(n)]  # 시원함 정보
narr = []  # 에어컨 정보
for i in range(n):
    for j in range(n):
        if arr[i][j] > 1:
            narr.append((i, j, arr[i][j]))

cnt = 0
while not check() and cnt <= 100:
    wspread()  # 바람 퍼짐
    wmix()  # 시원한 공기 섞임
    wminus()  # 외벽 칸 -1
    cnt += 1

if cnt > 100:
    print(-1)
else:
    print(cnt)