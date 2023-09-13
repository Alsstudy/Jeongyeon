def bfs(ridx, bidx):
    q = []
    q.append(ridx)
    cnt = 1
    nbi = bidx[0]
    nbj = bidx[1]
    mark = False

    while q:
        nidx = q.pop(0)
        nri = nidx[0]
        nrj = nidx[1]
        visited[nri][nrj] = 1

        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            bi = nbi
            bj = nbj
            while 0 <= bi + i[0] < n and 0 <= bj + i[1] < m and arr[bi + i[0]][bj + i[1]] != '#' and arr[bi + i[0]][bj + i[1]] != 'R':
                bi += i[0]
                bj += i[1]
                if arr[bi][bj] == 'O':
                    return -1

            ri = nri
            rj = nrj
            while 0 <= ri + i[0] < n and 0 <= rj + i[1] < m and arr[ri+i[0]][rj+i[1]] != '#' and arr[ri+i[0]][rj+i[1]] != 'B' and visited[ri+i[0]][rj+i[1]] != 1:
                ri += i[0]
                rj += i[1]
                visited[ri][rj] = 1
                mark = True
                if arr[ri][rj] == 'O':
                    return cnt
            q.append((ri, rj))
        if mark:
            cnt += 1
        mark = False

    return -1

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ridx = (i, j)
        elif arr[i][j] == 'B':
            bidx = (i, j)

print(bfs(ridx, bidx))