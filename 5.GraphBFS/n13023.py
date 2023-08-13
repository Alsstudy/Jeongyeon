import sys
input = sys.stdin.readline


def dfs(idx, cnt):
    if cnt == 4:
        print(1)
        exit(0)

    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False


n, m = map(int, input().split())

arr = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
