import sys
input = sys.stdin.readline


n = int(input())
p = list(map(int, input().split()))
p.insert(0, 10001)

dp = [10001 for _ in range(n+1)]
dp[0] = 10001
dp[1] = p[1]

for i in range(1, n+1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j] + p[j])
    dp[i] = min(dp[i], p[i])

print(dp[n])