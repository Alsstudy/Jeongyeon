import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr[r][c] = -1
count = 1

while arr[r][c] != 1:
    temp = False

    for _ in range(4):
        d -= 1  # 회전
        if d == -1:
            d = 3

        nr = r + dir[d][0]  # 이동
        nc = c + dir[d][1]

        if arr[nr][nc] == 0:
            r = nr
            c = nc
            arr[r][c] = -1  # 청소
            count += 1
            temp = True
            break  # 처음으로 돌아감

    if not temp:  # 사방이 전부 빈 칸이 없는 경우, 후진
        r += dir[d-2][0]
        c += dir[d-2][1]

print(count)