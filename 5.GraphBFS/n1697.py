from collections import deque
import sys
input = sys.stdin.readline


def bfs(sidx):
    queue = deque([])
    queue.append(sidx)

    while queue:
        nidx = queue.popleft()
        for idx in [nidx+1, nidx-1, nidx*2]:
            if 0 <= idx <= 100000 and idx != n:
                if li[idx] == 0 or li[nidx] + 1 < li[idx]:
                    li[idx] = li[nidx] + 1
                    queue.append(idx)


n, k = map(int, input().split())
li = [0] * 100001

bfs(n)

print(li[k])