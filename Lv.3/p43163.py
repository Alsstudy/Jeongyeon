from collections import deque


def find(start, end, arr):
    n = len(start)
    visited = [False] * len(arr)
    queue = deque([])
    queue.append((start, 0))

    while queue:
        w, cnt = queue.popleft()
        if w == end:
            return cnt
        for i in range(len(arr)):
            if not visited[i]:
                wcnt = 0
                for j in range(n):
                    if w[j] != arr[i][j]:
                        wcnt += 1
                if wcnt == 1:
                    visited[i] = True
                    queue.append((arr[i], cnt+1))


def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        return find(begin, target, words)


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))