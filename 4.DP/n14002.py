import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

cnt = max(dp)
print(cnt)
li = []
for i in range(n-1, -1, -1):
    if dp[i] == cnt:
        li.append(a[i])
        cnt -= 1

print(' '.join(map(str, reversed(li))))