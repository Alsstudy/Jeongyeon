import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for _ in range(2)] for i in range(n+1)]
for i in range(1, 2):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(2):
        if j == 1:
            dp[i][j] = dp[i-1][0]
        else:
            dp[i][j] = dp[i-1][0] + dp[i-1][1]

print(sum(dp[n]))