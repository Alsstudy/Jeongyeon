def roll(d):
    global top, bottom, north, south, east, west
    if d == 1:  # 동쪽
        top, bottom, east, west = west, east, top, bottom

    elif d == 2:  # 서쪽
        top, bottom, east, west = east, west, bottom, top

    elif d == 3:  # 북쪽
        top, bottom, north, south = south, north, top, bottom

    elif d == 4:  # 남쪽
        top, bottom, north, south = north, south, bottom, top

    print(top)


n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s = list(map(int, input().split()))

top, bottom, north, south, east, west = 0, 0, 0, 0, 0, 0

for i in s:
    if i == 1:  # 동쪽
        if 0 <= y+1 < m:
            y += 1
        else:
            continue

    elif i == 2:  # 서쪽
        if 0 <= y-1 < m:
            y -= 1
        else:
            continue

    elif i == 3:  # 북쪽
        if 0 <= x-1 < n:
            x -= 1
        else:
            continue

    elif i == 4:  # 남쪽
        if 0 <= x+1 < n:
            x += 1
        else:
            continue

    roll(i)

    if arr[x][y] == 0:
        arr[x][y] = bottom
    else:
        bottom = arr[x][y]
        arr[x][y] = 0
