# undo
def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            n1 = i
            m1 = j
            n2 = i
            m2 = j
            sol1 = 0
            sol2 = 0
            while n1 <= m1 and n2 <= m2:
                if s[n1] != s[m1]:
                    sol1 = m1 - n1
                    break
                else:
                    m1 -= 1
                if s[n2] != s[m2]:
                    sol2 = m2 - n2
                    break
                else:
                    n2 += 1
            answer += max(sol1, sol2)
    return answer


print(solution(input()))
