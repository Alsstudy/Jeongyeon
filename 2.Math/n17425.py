n = int(input())
ans = []

MAX = 1000000
dp = [1] * (MAX+1)
s = [0] * (MAX+1)

for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
    s[i] = s[i-1] + dp[i]

for i in range(n):
    num = int(input())
    ans.append(s[num])

print('\n'.join(map(str, ans)))