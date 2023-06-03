import sys
input = sys.stdin.readline


def dfs(idx, s):
    if len(q) == L:
        cnt = sum([s.count('a'), s.count('e'), s.count('i'), s.count('o'), s.count('u')])
        if cnt >= 1 and len(s) - cnt >= 2:
            li.append(s)
        return

    for i in range(idx, C):
        if arr[i] not in q:
            q.append(arr[i])
            dfs(i+1, s + arr[i])
            q.pop()


L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
q = []

s = ""
li = []

dfs(0, "")

for i in li:
    print(i)