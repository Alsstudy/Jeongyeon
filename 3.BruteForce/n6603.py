import sys
input = sys.stdin.readline


def dfs(li, idx):
    if len(ans) == 6:
        print(' '.join(map(str, ans)))
        return

    for i in range(idx, len(li)):
        if li[i] not in ans:
            ans.append(li[i])
            dfs(li, i+1)
            ans.pop()


ans = []
li = list(map(int, input().split()))
while li[0] != 0:
    dfs(li, 1)
    print()
    li = list(map(int, input().split()))