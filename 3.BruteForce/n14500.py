# undo
import sys
import numpy as np

N, M = map(int, input().split())

li = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
li = np.pad(li, ((1,1),(1,1)), 'constant', constant_values=0)


def getMax(i, j):
    cnt = 0
    val = li[i][j]
    n = i
    m = j
    while cnt < 3:
        mVal = max(li[n-1][m], li[n][m-1], li[n+1][m], li[n][m+1])  # 만약 max값이 여러개일 경우 고려 필요
        val += mVal
        print(mVal)
        for _ in (li[n-1][m], li[n][m-1], li[n+1][m], li[n][m+1]):
            if mVal == li[n-1][m]:
                n = n-1  # getMax(n-1, m)
                break
            elif mVal == li[n][m-1]:
                m = m-1  # getMax(n, m-1)
                break
            elif mVal == li[n+1][m]:
                n = n+1  # getMaX(n+1, m)
                break
            elif mVal == li[n][m+1]:
                m = m+1  # getMax(n, m+1)
                break
        cnt += 1
    print(f'{li[i][j]}, {val}')
    return val


maxVal = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        val = getMax(i, j)
        if val > maxVal:
            maxVal = val

print(maxVal)
