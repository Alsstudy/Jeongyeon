import sys
input = sys.stdin.readline


def bfs(sidx):
    global cnt

    cnt += 1

    queue = [sidx]

    visited[sidx] = cnt

    while queue:
        idx = queue.pop(0)
        for i in range(1, n+1):
            if visited[i] == 0 and arr[idx][i] == 1:
                queue.append(i)
                visited[i] = cnt


n, m = map(int, input().split())

arr = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    arr[u][v] = arr[v][u] = 1

for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)

print(cnt)