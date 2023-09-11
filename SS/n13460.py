def dfs(nidx, midx, cnt):
    if arr[nidx][midx] == '0':
        return cnt

    for i in range [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nidx += i[0]
        midx += i[1]
        if 0 <= nidx < n and 0 <= midx < m:
            if arr[nidx][midx] != '#':
                dfs(nidx, midx, cnt+1)


# def move(dir, nidx, midx):
#     if dir == 1:  # 동
#         while arr[nidx][midx+1] != '#' and (midx+1) < m:
#             midx += 1
#             if arr[nidx][midx] == '0':
#                 return 1
#     elif dir == 2:  # 서
#         while arr[nidx][midx-1] != '#' and (midx-1) >= 0:
#             midx -= 1
#             if arr[nidx][midx] == '0':
#                 return 1
#     elif dir == 3:  # 남
#         while arr[nidx+1][midx] != '#' and (nidx+1) < n:
#             nidx += 1
#             if arr[nidx][midx] == '0':
#                 return 1
#     elif dir == 4:  # 북
#         while arr[nidx-1][midx] != '#' and (nidx-1) >= 0:
#             nidx -= 1
#             if arr[nidx][midx] == '0':
#                 return 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R' or arr[i][j] == 'B':
            move()

