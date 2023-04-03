from collections import Counter


def warshall(n, li):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if li[i][k] == 1 and li[k][j] == 1 and i != j:
                    li[i][j] = 1
                if li[i][k] == -1 and li[k][j] == -1 and i != j:
                    li[i][j] = -1

    return li


def solution(n, results):
    li = [[0] * n for _ in range(n)]

    for i, j in results:
        li[i-1][j-1] = 1
        li[j-1][i-1] = -1

    li = warshall(n, li)

    answer = 0
    for i in range(n):
        if Counter(li[i])[0] == 1:
            answer += 1

    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])