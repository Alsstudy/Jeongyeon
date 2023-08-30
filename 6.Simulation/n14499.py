import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice = [0] * 6

for d in command:
    nx = x + move[d][0]
    ny = y + move[d][1]

    if not 0 <= nx < n or not 0 <= ny < m:
        continue

    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if d == 1:  # 동
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif d == 2:  # 서
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif d == 3:  # 북
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif d == 4:  # 남
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    if li[nx][ny] == 0:
        li[nx][ny] = dice[5]
    else:
        dice[5] = li[nx][ny]
        li[nx][ny] = 0

    print(dice[4])
    x, y = nx, ny
