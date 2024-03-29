import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if li[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(li[i][1] + dp[i+li[i][0]], dp[i+1])

print(dp[0])