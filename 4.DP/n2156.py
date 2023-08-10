import sys
input = sys.stdin.readline

n = int(input())
li = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)

if n >= 1:
    dp[1] = li[1]

if n >= 2:
    dp[2] = dp[1] + li[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+li[i-1]+li[i], dp[i-2]+li[i], dp[i-1])

print(dp[n])