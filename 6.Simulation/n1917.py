import sys
input = sys.stdin.readline


def move(k):
    if k == 0:  # 동
        visited[1][0], visited[1][1], visited[1][2], visited[3][1] = visited[1][1], visited[1][2], visited[3][1], visited[1][0]
    elif k == 1:  # 서
        visited[1][0], visited[1][1], visited[1][2], visited[3][1] = visited[3][1], visited[1][0], visited[1][1], visited[1][2]
    elif k == 2:  # 남
        visited[0][1], visited[1][1], visited[2][1], visited[3][1] = visited[1][1], visited[2][1], visited[3][1], visited[0][1]
    elif k == 3:  # 북
        visited[0][1], visited[1][1], visited[2][1], visited[3][1] = visited[3][1], visited[0][1], visited[1][1], visited[2][1]


def dfs(x, y):
    cnt = 1

    for k in range(4):
        ax, ay = x + dx[k], y + dy[k]
        if 0 <= ax < 6 and 0 <= ay < 6 and arr[ay][ax] == 1:
            move(k)
            if not visited[1][1]:
                visited[1][1] = True
                cnt += dfs(ax, ay)
            move(dk[k])

    return cnt


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dk = [1, 0, 3, 2]

for t in range(3):
    arr = [list(map(int, input().split())) for _ in range(6)]

    visited = [[False] * 3 for _ in range(4)]
    flag = False

    for i in range(6):
        for j in range(6):
            if arr[i][j] == 1:
                visited[1][1] = True
                cnt = dfs(j, i)
                flag = True
                break

        if flag:
            break

    print("yes" if cnt == 6 else "no")