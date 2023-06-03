import sys
input = sys.stdin.readline

def dfs(num):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(num, N+1):
        visited[i] = True
        s.append(i)
        dfs(i)
        s.pop()
        visited[i] = False


N, M = map(int, input().split())
s = []
visited = [False] * (N+1)

dfs(1)