from itertools import permutations


def duncnt(li, k, dungeons):
    for i in li:
        nk = k
        ncnt = 0
        for j in i:
            if nk >= dungeons[j][0]:
                nk -= dungeons[j][1]
                ncnt += 1
            if ncnt == len(i):
                return True
    return False


def solution(k, dungeons):
    answer = 0

    nli = [i for i in range(len(dungeons))]

    for i in range(len(nli), 0, -1):
        if duncnt(set(permutations(nli, i)), k, dungeons):
            return i

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
