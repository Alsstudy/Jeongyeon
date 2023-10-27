
def solution(participant, completion):
    d = {}
    sumHash = 0

    for i in participant:
        d[hash(i)] = i
        sumHash += hash(i)

    for i in completion:
        sumHash -= hash(i)

    return d[sumHash]


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))