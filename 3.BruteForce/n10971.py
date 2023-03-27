import sys

n = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visit = [0] * n
minVal = 10000000

def dfs(start, next, val, cnt):
    global minVal
    if cnt == n:  # 모든 도시를 방문했을 경우
        if cost[next][start] != 0:
            val += cost[next][start]
            print(start)
            print(next)
            print(val)
            if minVal > val:
                minVal = val
        return

    if val > minVal:
        return

    for i in range(n):  # 모든 도시를 방문하도록
        if not visit[i] != 0 and cost[next][i] != 0:  # 이전에 방문한 적 없고 방문 가능한 도시일 경우
            visit[i] = 1  # 방문
            dfs(start, i, val + cost[next][i], cnt + 1)
            visit[i] = 0


# 모두 출발점으로 설정하여 dfs 탐색
for i in range(n):
    visit[i] = 1
    dfs(i, i, 0, 1)
    visit[i] = 0

print(minVal)