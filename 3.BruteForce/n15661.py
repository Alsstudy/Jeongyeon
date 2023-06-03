import sys
input = sys.stdin.readline


def calculate():
    global minVal
    s1, s2 = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                s1 += S[i][j]
            elif not visited[i] and not visited[j]:
                s2 += S[i][j]
    minVal = min(minVal, abs(s1 - s2))
    return


def sol(cnt):
    if cnt == N:
        calculate()
        return
    visited[cnt] = 1
    sol(cnt+1)
    visited[cnt] = 0
    sol(cnt+1)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
minVal = 2000
sol(0)
print(minVal)