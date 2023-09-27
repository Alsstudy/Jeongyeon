def solution(progresses, speeds):
    answer = []

    tmp = [0] * len(progresses)
    for i in range(len(tmp)):
        tmp[i] = -((progresses[i] - 100) // speeds[i])

    for i in range(len(tmp)):
        if tmp[i] != -1:
            cnt = 1
            for j in range(i + 1, len(tmp)):
                if tmp[i] >= tmp[j]:
                    cnt += 1
                    tmp[j] = -1
                else:
                    break
            answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))