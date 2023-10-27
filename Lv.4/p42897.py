def solution(money):
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n

    # 첫번째 집을 털고 마지막 집을 안 터는 경우
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], money[i] + dp1[i-2])
    dp1[n-1] = dp1[n-2]

    # 첫번째 집을 안 털고 마지막 집을 터는 경우
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])

    return max(dp1[-1], dp2[-1])


print(solution([1, 1, 0, 4]))
print(solution([2, 0, 2, 2, 1]))
print(solution([1, 3, 2]))
