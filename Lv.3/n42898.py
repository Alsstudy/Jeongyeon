# undo
def solution(m, n, puddles):
    arr = [[0] * m for _ in range(n)]

    for i in range(len(puddles)):
        arr[puddles[i][1] - 1][puddles[i][0] - 1] = -1

    i = 0
    j = 0
    mark = 0
    while i < n:
        while j < m:
            if i == 0 or j == 0:
                if arr[i][j] != -1:
                    if mark == 1:
                        arr[0][j] = 0
                    if mark == 2:
                        arr[i][0] = 0
                    else:
                        arr[i][j] = 1
                if arr[i][j] == -1:
                    if i == 0:
                        mark = 1
                    else:  # if j == 0
                        mark = 2
            elif arr[i][j] == -1:
                pass
            elif arr[i - 1][j] == -1:
                arr[i][j] = arr[i][j - 1]
            elif arr[i][j - 1] == -1:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
            j += 1
        i += 1
        j = 0

    print(arr)
    answer = arr[n - 1][m - 1] % 1000000007

    return answer


print(solution(4, 3, [[1, 2], [2, 1]]))