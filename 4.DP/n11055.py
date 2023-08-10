import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
dp = [li[n-1]]

for i in range(n-2, -1, -1):
    if li[i] < li[i+1]:
        dp.append(max(dp) + li[i])
    else:
        dp.append(max(li[i], min(dp)))

    print(dp)

print(max(dp))