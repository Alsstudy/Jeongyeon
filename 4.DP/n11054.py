import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

dp = [1] * n
dp1 = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if li[i] > li[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if li[i] > li[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

for i in range(n):
    dp[i] = max(dp1[i]+dp2[i]-1, dp1[i], dp2[i])

print(max(dp))