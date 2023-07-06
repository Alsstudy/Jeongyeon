import sys
input = sys.stdin.readline


def sol():
    global maxVal
    if len(ans) == n:
        sum = 0
        for i in range(n - 1):
            sum += abs(ans[i] - ans[i + 1])
        maxVal = max(maxVal, sum)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(li[i])
            sol()
            visited[i] = False
            ans.pop()


n = int(input())
li = sorted(list(map(int, input().split())))
maxVal = -1e10
ans = []
visited = [False] * n

sol()

print(maxVal)