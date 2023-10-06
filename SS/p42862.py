def solution(n, lost, reserve):
    nreserve = set(reserve) - set(lost)
    nlost = list(set(lost) - set(reserve))
    nlost.sort()
    answer = n - len(nlost)

    for i in nlost:
        if i - 1 in nreserve:
            answer += 1
            nreserve -= set([i - 1])
        elif i + 1 in nreserve:
            answer += 1
            nreserve -= set([i + 1])

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))