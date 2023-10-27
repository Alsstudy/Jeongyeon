from itertools import product

def solution(word):
    answer = []
    w = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for pro in product(w, repeat=i):
            answer.append(''.join(pro))
    answer.sort()

    return answer.index(word) + 1


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))