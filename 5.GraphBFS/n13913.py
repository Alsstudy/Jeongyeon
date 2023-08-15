from collections import deque
import sys
input = sys.stdin.readline


def path():
    s = k
    v = [k]
    while s != n:
        s = bef[s]
        v.append(s)

    return v


def bfs():
    while queue:
        nidx = queue.popleft()
        if nidx == k:
            print(li[k])
            print(' '.join(map(str, reversed(path()))))
            return
        for idx in [nidx-1, nidx+1, nidx*2]:
            if 0 <= idx <= 100000:
                if li[idx] == 0:
                    li[idx] = li[nidx] + 1
                    bef[idx] = nidx
                    queue.append(idx)


n, k = map(int, input().split())

li = [0] * 100001
bef = [0] * 100001

queue = deque([n])

bfs()