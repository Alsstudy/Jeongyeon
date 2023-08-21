from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while queue:
        a, b = queue.popleft()

        if li[a][a] == -1:
            li[a][a] = li[a][b] + 1
            queue.append((a, a))

        if a + b <= s and li[a+b][b] == -1:
            li[a+b][b] = li[a][b] + 1
            queue.append((a+b, b))

        if a - 1 >= 0 and li[a-1][b] == -1:
            li[a-1][b] = li[a][b] + 1
            queue.append((a-1, b))


s = int(input())

li = [[-1] * (s+1) for _ in range(s+1)]

queue = deque()
queue.append((1, 0))

li[1][0] = 0

bfs()

answer = -1

for i in range(s+1):
    if li[s][i] != -1:
        if answer == -1 or answer > li[s][i]:
            answer = li[s][i]

print(answer)