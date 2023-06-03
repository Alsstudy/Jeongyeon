import sys


def dfs(num):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(num, N+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(i)
        s.pop()
        visited[i] = False


input = sys.stdin.readline

N, M = map(int, input().split())
s = []
visited = [False] * (N+1)

dfs(1)