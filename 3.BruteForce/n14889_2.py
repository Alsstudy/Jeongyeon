import sys
input = sys.stdin.readline


def dfs(idx):
    global minVal
    if len(team) == n / 2:
        s1, s2 = 0, 0
        for i in range(n):
            for j in range(n):
                if (i in team) and (j in team):
                    s1 += li[i][j]
                elif (i not in team) and (j not in team):
                    s2 += li[i][j]
        minVal = min(minVal, abs(s1 - s2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            team.append(i)
            dfs(i)
            visited[i] = False
            team.pop()


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
minVal = 1e10
visited = [False] * n
team = []
dfs(0)

print(minVal)