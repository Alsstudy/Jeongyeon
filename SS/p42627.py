def solution(jobs):
    answer = 0
    cur = 0
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= cur:
                cur += jobs[i][1]
                answer += cur - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1:
                cur += 1

    return answer // length


print(solution([[0, 3], [1, 9], [2, 6]]))