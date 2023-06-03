import sys
input = sys.stdin.readline


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(0, N):
        if visited[i]:
            continue
        visited[i] = True
        s.append(arr[i])
        dfs()
        s.pop()
        visited[i] = False


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * N
s = []

dfs()