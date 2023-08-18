from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        nidx = queue.popleft()
        if nidx == s:
            print(li[s])
            return
        for i in [0, nidx, nidx-1]:
            if 0 <= i <= 1000:
                if li[i] == 0:
                    li[i] = li[nidx] + 1


s = int(input())
li = [0] * 1001

queue = deque([1])

bfs()