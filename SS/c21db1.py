def rotate():
    global d

    if down > arr[x][y]:
        d = (d + 1) % 4
    if down < arr[x][y]:
        d = (d-1) % 4


def dfs(i, j):
    global cnt
    for k in direct:
        nx, ny = i+k[0], j+k[1]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and arr[nx][ny] == arr[i][j]:
                visited[nx][ny] = True
                cnt += 1
                dfs(nx, ny)


def roll():
    global up, down, front, back, right, left  # 1, 6, 2, 5, 3, 4

    if d == 0:  # 우
        up, down, front, back, right, left = left, right, front, back, up, down
    if d == 1:  # 하
        up, down, front, back, right, left = back, front, up, down, right, left
    if d == 2:  # 좌
        up, down, front, back, right, left = right, left, front, back, down, up
    if d == 3:  # 상
        up, down, front, back, right, left = front, back, down, up, right, left


def move():
    global x, y, d

    nx, ny = x + direct[d][0], y + direct[d][1]  # 현재 방향으로 이동 가능함
    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny

    else:  # 현재 방향으로 이동 불가능
        d = (d + 2) % 4  # 반대 방향으로 변경
        x, y = x + direct[d][0], y + direct[d][1]  # 이동


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 시계방향 +1, 반시계방향 -1, 반대방향 +2
x, y, d = 0, 0, 0
up, down, front, back, right, left = 1, 6, 2, 5, 3, 4  # 상/하/앞/뒤/오/왼

val = 0

for i in range(m):
    move()  # 이동
    roll()  # 주사위 굴리기
    visited = [[False] * n for _ in range(n)]  # dfs 사용
    visited[x][y] = True  # 방문 표시
    cnt = 1  # 시작점 1개
    dfs(x, y)  # 같은 값 개수 세기
    val += (cnt * arr[x][y])
    rotate()  # 회전

print(val)