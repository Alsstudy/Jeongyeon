import sys
input = sys.stdin.readline


def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j


def dfs(s, cnt):
    global minVal, maxVal
    if cnt == k+1:
        if len(minVal) == 0:
            minVal = s
        else:
            maxVal = s
        return

    for i in range(10):
        if not visited[i]:
            if cnt == 0 or check(s[-1], str(i), arr[cnt - 1]):
                visited[i] = True
                dfs(s+str(i), cnt+1)
                visited[i] = False


k = int(input())
arr = list(map(str, input().split()))
visited = [False] * 10
minVal = ""
maxVal = ""
dfs("", 0)

print(maxVal)
print(minVal)