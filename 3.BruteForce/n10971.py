import sys
input = sys.stdin.readline


def dfs(start, cur, val, cnt):
    global minVal
    if cnt == n:
        if li[cur][start] != 0:
            val += li[cur][start]
            minVal = min(minVal, val)
            return

    if val > minVal:
        return

    for i in range(n):
        if not visited[i] and li[cur][i] != 0:
            visited[i] = True
            dfs(start, i, val+li[cur][i], cnt+1)
            visited[i] = False


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
minVal = 1e10

for i in range(n):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(minVal)