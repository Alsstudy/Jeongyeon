from itertools import permutations


def isprime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return 0
        return 1
    return 0


def makestr(nli, li):
    for i in li:
        nli.add(int(''.join(map(str, i))))

    return nli


def solution(numbers):
    answer = 0

    numbers = list(map(str, numbers))
    nli = set()

    for i in range(len(numbers)):
        nli = makestr(nli, set(permutations(numbers, i+1)))

    for i in nli:
        answer += isprime(i)

    return answer


print(solution("17"))
print(solution("011"))