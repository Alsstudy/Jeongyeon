# undo
from collections import Counter


def solution(n, computers):
    t = 200
    li = [k for k in range(n)]
    for i in range(1, n):
        for j in range(i):
            if computers[i][j] == 1 and computers[j][i] == 1:
                if li[i] == 0 and li[j] == 0:
                    t += 1
                    li[i] = t
                    li[j] = t
                else:
                    li[i] = t
                    li[j] = t

    answer = len(Counter(li).keys())

    return answer


# print(solution(7, [[1,0,0,0,0,0,1], [0,1,1,0,1,0,0], [0,1,1,1,0,0,0], [0,0,1,1,0,0,0], [0,1,0,0,1,1,0], [0,0,0,0,1,1,1], [1,0,0,0,0,1,1]]))
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))
