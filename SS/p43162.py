def solution(n, computers):
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)

    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))