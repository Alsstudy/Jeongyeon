# undo
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

dp = [0] * n
dp[0] = li[0]

for i in range(1, n):
    for j in range(i):
        if li[i] > li[j]:
            dp[i] = max(dp[j] + li[i], dp[i])
        else:
            dp[i] = max(li[i], dp[i])


print(max(dp))