from collections import deque


def bfs(v, visited, adj):
    cnt = 0
    q = deque([[v, cnt]])
    # print(q)
    while q:
        val = q.popleft()
        # print(f'val = {val}')
        v = val[0]
        cnt = val[1]
        if visited[v] == -1:  # 처음 방문하는 곳
            visited[v] = cnt  # 몇번을 거쳐서 방문한건지 기록
            cnt += 1
            for arr in adj[v]:  # 방금 방문한 곳과 연결되어 있는 곳들 추가
                q.append([arr, cnt])
                # print(f'q = {q}')


def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]

    for arr in edge:
        x = arr[0]
        y = arr[1]
        adj[x].append(y)
        adj[y].append(x)

    print(adj)

    bfs(1, visited, adj)
    for val in visited:
        if val == max(visited):
            answer += 1

    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])