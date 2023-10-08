def reindex():
    global x, y
    for i in range(m):
        if change[i] and people[i]:
            people[i] = change[i]
    if change[-1]:
        x, y = change[-1][0], change[-1][1]


def check(nx, ny, bx, by):
    global x, y
    for i in range(m):
        if people[i] == [bx, by]:
            change[i] = [nx, ny]
    if x == bx and y == by:
        change[-1] = [nx, ny]


def rotate(rlen, sx, sy):
    global x, y

    narr = [a[:] for a in arr[:]]
    ex = sx + rlen
    for j in range(rlen + 1):
        for k in range(rlen + 1):
            if narr[ex - k][sy + j] > 0:
                arr[sx + j][sy + k] = narr[ex - k][sy + j] - 1
            else:
                arr[sx + j][sy + k] = narr[ex - k][sy + j]
            check(sx + j, sy + k, ex - k, sy + j)


def makerect():
    rects = []
    for p in people:
        if p:
            px, py = p[0], p[1]
            h, w = abs(px - x), abs(py - y)
            if h > w:
                if px > x:
                    tx = px - h
                    ty = max(py, y) - h
                    if tx < 1:
                        tx = 1
                    if ty < 1:
                        ty = 1
                    rects.append([h, tx, ty])
                else:
                    tx = x - h
                    ty = max(py, y) - h
                    if tx < 1:
                        tx = 1
                    if ty < 1:
                        ty = 1
                    rects.append([h, tx, ty])
            else:
                if py > y:
                    tx = max(px, x) - w
                    ty = py - w
                    if tx < 1:
                        tx = 1
                    if ty < 1:
                        ty = 1
                    rects.append([w, tx, ty])
                else:
                    tx = max(px, x) - w
                    ty = y - w
                    if tx < 1:
                        tx = 1
                    if ty < 1:
                        ty = 1
                    rects.append([w, tx, ty])
    rects.sort(key=lambda x: (x[0], x[1], x[2]))
    return rects[0]


def goal():
    for i in range(m):
        if people[i] == [x, y]:
            people[i] = []


def move():
    global cnt
    for p in people:
        if p:
            mark = False
            px, py = p[0], p[1]
            curlen = abs(px - x) + abs(py - y)
            if px - x > 0:  # 상
                npx, npy = px + direct[0][0], py + direct[0][1]
                newlen = abs(npx - x) + abs(npy - y)
                if 1 <= npx <= n and 1 <= npy <= n and arr[npx][npy] == 0 and newlen < curlen and not mark:
                    p[0], p[1] = npx, npy
                    cnt += 1
                    mark = True
            if px - x < 0:  # 하
                npx, npy = px + direct[1][0], py + direct[1][1]
                newlen = abs(npx - x) + abs(npy - y)
                if 1 <= npx <= n and 1 <= npy <= n and arr[npx][npy] == 0 and newlen < curlen and not mark:
                    p[0], p[1] = npx, npy
                    cnt += 1
                    mark = True
            if py - y > 0:  # 좌
                npx, npy = px + direct[2][0], py + direct[2][1]
                newlen = abs(npx - x) + abs(npy - y)
                if 1 <= npx <= n and 1 <= npy <= n and arr[npx][npy] == 0 and newlen < curlen and not mark:
                    p[0], p[1] = npx, npy
                    cnt += 1
                    mark = True
            if py - y < 0:  # 우
                npx, npy = px + direct[3][0], py + direct[3][1]
                newlen = abs(npx - x) + abs(npy - y)
                if 1 <= npx <= n and 1 <= npy <= n and arr[npx][npy] == 0 and newlen < curlen and not mark:
                    p[0], p[1] = npx, npy
                    cnt += 1
                    mark = True


n, m, k = map(int, input().split())
arr = [[0 for _ in range(n + 1)]]
arr += [[0] + list(map(int, input().split())) for _ in range(n)]
people = [list(map(int, input().split())) for _ in range(m)]
x, y = map(int, input().split())
change = [[] for _ in range(m + 1)]

cnt = 0
dist = [0 for _ in range(m)]
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

for i in range(k):
    move()  # 이동
    goal()
    if all(p == [] for p in people):
        print(cnt)
        print(x, y)
        exit(0)
    else:
        length, rx, ry = makerect()  # 정사각형 구하기
        rotate(length, rx, ry)  # 회전 및 -1
        reindex()

print(cnt)
print(x, y)
