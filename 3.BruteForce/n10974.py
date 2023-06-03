import sys
input = sys.stdin.readline


def dfs():
    if len(q) == n:
        arr.append(' '.join(map(str, q)))
        return

    for i in li:
        if i not in q:
            q.append(i)
            dfs()
            q.pop()


n = int(input())
li = list(range(1, n+1))
q = []
arr = []
dfs()
for i in arr:
    print(i)