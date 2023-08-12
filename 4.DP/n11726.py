import sys
input = sys.stdin.readline


n = int(input())
dp = [_ for _ in range(n+1)]

if n > 3:
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)