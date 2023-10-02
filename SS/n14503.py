def move(nr, nc, nd):
    count = 0

    while True:
        if arr[nr][nc] == 0:
            count += 1
            arr[nr][nc] = -1

        nclear = False
        for i in dir:
            if 0 <= nr + i[0] < n and 0 <= nc + i[1] < m:
                if arr[nr + i[0]][nc + i[1]] == 0:
                    nclear = True  # 청소 할 게 있는 경우
        if not nclear:  # 청소를 할 게 없는 경우
            if 0 <= nr + dir[(nd+2) % 4][0] < n and 0 <= nc + dir[(nd+2) % 4][1] < m:
                if arr[nr + dir[(nd+2) % 4][0]][nc + dir[(nd+2) % 4][1]] == 1:
                    return count
                else:
                    nr += dir[(nd+2) % 4][0]
                    nc += dir[(nd+2) % 4][1]
        else:
            for i in range(4):
                nd -= 1
                if nd == -1:
                    nd = 3
                if 0 <= nr + dir[nd][0] < n and 0 <= nc + dir[nd][1] < m:
                    if arr[nr + dir[nd][0]][nc + dir[nd][1]] == 0:
                        nr += dir[nd][0]
                        nc += dir[nd][1]
                        break


n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

print(move(r, c, d))