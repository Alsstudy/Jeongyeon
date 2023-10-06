from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    cnt = 0
    queue = deque([(0, 0, 1)])
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, cnt = queue.popleft()
        maps[x][y] = -1
        for d in direct:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = -1
                    queue.append((nx, ny, cnt + 1))
                    if nx == n - 1 and ny == m - 1:
                        return cnt + 1

    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))