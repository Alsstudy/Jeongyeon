from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        nidx = queue.popleft()
        # print(nidx)
        if nidx == k:
            print(li[k])
            return
        for idx in [nidx+1, nidx-1, nidx*2]:
            if 0 <= idx <= 100000:
                if li[idx] == 0:
                    if idx == nidx*2:
                        li[idx] = li[nidx]
                    else:
                        li[idx] = li[nidx] + 1
                    queue.append(idx)

# 5, 10, 20, 40, 80, 160

n, k = map(int, input().split())

li = [0] * 100001

queue = deque([n])

bfs()