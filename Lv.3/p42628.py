import heapq
def solution(operations):
    answer = []

    for i in operations:
        s, n = i.split()
        if s == 'I':
            heapq.heappush(answer, int(n))

        elif s == 'D' and len(answer) > 0:
            if int(n) == -1:
                heapq.heappop(answer)
            elif int(n) == 1:
                answer.pop()

    if len(answer) == 0:
        return [0, 0]

    return [max(answer), min(answer)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))