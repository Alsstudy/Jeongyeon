import sys
input = sys.stdin.readline


def dfs(idx):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(idx, N):
        s.append(arr[i])
        dfs(i)
        s.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []

dfs(0)