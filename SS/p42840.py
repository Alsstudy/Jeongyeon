def solution(answers):
    answer = [0, 0, 0]
    person = []

    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len1, len2, len3 = len(n1), len(n2), len(n3)

    for i in range(len(answers)):
        if answers[i] == n1[i % len1]:
            answer[0] += 1
        if answers[i] == n2[i % len2]:
            answer[1] += 1
        if answers[i] == n3[i % len3]:
            answer[2] += 1

    smax = max(answer)
    for i in range(3):
        if answer[i] == smax:
            person.append(i+1)

    return person


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
