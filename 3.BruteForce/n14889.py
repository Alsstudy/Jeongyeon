import sys
input = sys.stdin.readline


def dfs(idx, cnt):
    global minVal
    if len(q) == N//2:
        s1, s2 = 0, 0
        for i in range(N):
            for j in range(N):
                if (i in q) and (j in q):
                    s1 += S[i][j]
                elif (i not in q) and (j not in q):
                    s2 += S[i][j]
        minVal = min(minVal, abs(s1-s2))
        return

    for i in range(idx, N):
        if i not in q:
            q.append(i)
            dfs(i+1, cnt+1)
            q.pop()


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
q = []
minVal = 1000
dfs(0, 0)
print(minVal)