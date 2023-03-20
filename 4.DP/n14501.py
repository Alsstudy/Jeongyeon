import sys

n = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + li[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])  # 상담을 안 하는 것과 하는 것 중 뭐가 이득인지

print(dp[0])