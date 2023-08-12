import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

dp1 = [i for i in li]
dp2 = [i for i in li]

for i in range(1, n):
    dp1[i] = max(dp1[i-1] + li[i], li[i])

for i in range(n-2, -1, -1):
    dp2[i] = max(dp2[i+1] + li[i], li[i])

m1 = max(dp1)
m2 = -1001

for i in range(1, n-1):
    m2 = max(m2, dp1[i-1] + dp2[i+1])

print(max(m1, m2))