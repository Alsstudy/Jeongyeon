import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    li[i][0] += li[i-1][0]
    for j in range(1, i):
        li[i][j] += max(li[i-1][j-1], li[i-1][j])
    li[i][i] += li[i-1][i-1]

print(max(li[n-1]))