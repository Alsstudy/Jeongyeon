from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        nidx = queue.popleft()

        if nidx == k:
            print(li[nidx])
            return
        if 0 <= nidx * 2 <= 100000 and li[nidx*2] == -1:
            li[nidx*2] = li[nidx]
            queue.appendleft(nidx*2)
        if 0 <= nidx - 1 <= 100000 and li[nidx-1] == -1:
            li[nidx-1] = li[nidx] + 1
            queue.append(nidx-1)
        if 0 <= nidx + 1 <= 100000 and li[nidx+1] == -1:
            li[nidx+1] = li[nidx] + 1
            queue.append(nidx+1)



n, k = map(int, input().split())

li = [-1] * 100001

queue = deque([])
queue.append(n)

li[n] = 0

bfs()