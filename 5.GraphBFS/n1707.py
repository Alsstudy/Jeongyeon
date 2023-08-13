import sys
input = sys.stdin.readline


def bfs(sidx):
    queue = [sidx]
    visited[sidx] = 1

    while queue:
        idx = queue.pop(0)
        for i in arr[idx]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[idx] * -1
            elif visited[i] == visited[idx]:
                return False

    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())

    arr = [[] for _ in range(v+1)]
    visited = [False] * (v+1)

    result = False

    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            result = bfs(i)
            if not result:
                break

    print("YES" if result else "NO")