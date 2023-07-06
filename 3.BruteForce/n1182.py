import sys
input = sys.stdin.readline


def dfs(idx):
    global cnt

    if len(ans) > 0:
        if sum(ans) == s:
            cnt += 1

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            ans.append(li[i])
            dfs(i)
            visited[i] = False
            ans.pop()


n, s = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
visited = [False] * n
ans = []
dfs(0)

print(cnt)