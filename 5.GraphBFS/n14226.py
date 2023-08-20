from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while q:
        s, c = q.popleft()
        if dist[s][s] == -1:  # 붙여넣기
            dist[s][s] = dist[s][c] + 1
            q.append((s, s))
        if s + c <= n and dist[s + c][c] == -1:  # 복사
            dist[s + c][c] = dist[s][c] + 1
            q.append((s + c, c))
        if s - 1 >= 0 and dist[s - 1][c] == -1:  # 삭제
            dist[s - 1][c] = dist[s][c] + 1
            q.append((s - 1, c))


n = int(input())

dist = [[-1] * (n + 1) for _ in range(n + 1)]
q = deque()
q.append((1, 0))

dist[1][0] = 0

bfs()

answer = -1

for i in range(n + 1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]

print(answer)
