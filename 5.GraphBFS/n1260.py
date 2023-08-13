import sys
input = sys.stdin.readline


def dfs(idx):
    visited[idx] = 1

    print(idx, end=' ')

    for i in range(1, n+1):
        if visited[i] == 0 and arr[idx][i] == 1:
            dfs(i)


def bfs(sidx):
    queue = [sidx]

    visited[sidx] = 0

    while queue:
        idx = queue.pop(0)
        print(idx, end=' ')
        for i in range(1, n+1):
            if visited[i] == 1 and arr[idx][i] == 1:
                queue.append(i)
                visited[i] = 0


n, m, v = map(int, input().split())

arr = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

dfs(v)
print()
bfs(v)