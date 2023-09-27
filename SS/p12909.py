def solution(s):
    answer = True

    arr = list(map(str, s))
    tmp = []

    for i in arr:
        if i == ')':
            if tmp[-1:] == ['(']:
                tmp.pop()
            else:
                return False
        elif i == '(':
            tmp.append(i)
    if tmp:
        return False

    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))