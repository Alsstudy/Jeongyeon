import sys
input = sys.stdin.readline


def dfs(i, j, cnt, sumVal):
    global maxVal
    if cnt == K:
        maxVal = max(sumVal, maxVal)
        return

    for n in range(i, N):
        for m in range(j if n == i else 0, M):
            if [n, m] not in q:
                if ([n + 1, m] not in q) and ([n - 1, m] not in q) and ([n, m - 1] not in q) and ([n, m + 1] not in q):
                    q.append([n, m])
                    dfs(n, m, cnt + 1, sumVal + arr[n][m])
                    q.pop()


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = []
maxVal = -1e10
dfs(0, 0, 0, 0)
print(maxVal)
