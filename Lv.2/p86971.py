def bfs(start, n, graph):
    visited = [0] * (n+1)
    q = [start]
    visited[start] = 1
    cnt = 1

    while q:
        idx = q.pop(0)
        for i in graph[idx]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1

    return cnt


def solution(n, wires):
    answer = n

    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        answer = min(abs(bfs(a, n, graph) - bfs(b, n, graph)), answer)

        graph[a].append(b)
        graph[b].append(a)

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
print(solution(3, [[1, 2], [2, 3]]))
