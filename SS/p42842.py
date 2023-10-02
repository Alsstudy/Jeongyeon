def solution(brown, yellow):
    answer = []

    for i in range(1, yellow+1):
        if yellow % i == 0:
            j = yellow // i
            if brown == (j+2) * 2 + i * 2:
                answer = [i+2, j+2]
                break

    return sorted(answer, reverse=True)


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))