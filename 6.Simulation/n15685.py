import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    x, y, d, g = map(int, input().split())
    graph[y][x] = 1

    curve = [d]
    for i in range(g):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]

        if not 0 <= x <= 100 or not 0 <= y <= 100:
            continue

        graph[y][x] = 1

count = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            count += 1

print(count)