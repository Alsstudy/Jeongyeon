import copy
from collections import deque

def bfs():
    queue = deque()
    narr = copy.deepcopy(arr)

    for i in range(n):
        for j in range(m):
            if narr[i][j] == 2:
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            dr = r + dx[i]
            dc = c + dy[i]

            if 0 <= dr < n and 0 <= dc < m:
                if narr[dr][dc] == 0:
                    narr[dr][dc] = 2
                    queue.append((dr, dc))

    global result
    count = 0
    for i in range(n):
        count += narr[i].count(0)

    result = max(result, count)


def make_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(count+1)
                arr[i][j] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0
make_wall(0)
print(result)