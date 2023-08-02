import sys
input = sys.stdin.readline


dp = [_ for _ in range(12)]
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

n = int(input())
for i in range(n):
    num = int(input())
    print(dp[num])