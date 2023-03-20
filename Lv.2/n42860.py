# undo
def solution(name):
    answer = 0
    idx1 = []  # 순서대로 idx 저장
    idx2 = []  # 거꾸로 idx 저장
    min1 = 100
    min2 = 100
    for i in range(len(name)):
        n = ord(name[i]) - ord('A')  # 'A'와 차이값 (ASCII) -> 알파벳 이동 조이스틱
        if 26-n < n:
            n = 26-n
        answer += n

        if i == 0:
            idx1.append(0)
            idx2.append(0)
        if i != 0:
            if n != 0:
                idx1.append(i)
                idx2.append(len(name) - i)
            else:
                idx1.append(0)
                idx2.append(0)

    for j in range(len(idx1) - 1):
        bef1 = idx1[j]
        if bef1 + 1 == idx1[j+1] or bef1 == 0:
            continue
        else:
            min1 = bef1
            break

    for j in range(len(idx1) - 1):
        bef2 = idx2[len(idx2) - j - 1]
        if bef2 + 1 == idx2[len(idx2) - j - 2] or bef2 == 0:
            continue
        else:
            min2 = bef2
            break

    answer += min(max(idx1), max(idx2), min1 * 2 + min2, min2 * 2 + min1)

    print(answer)
    return answer


def solution(name):
    answer = 0

    min_move = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - 65, 90 - ord(char) + 1)

        idx = i + 1
        while idx < len(name) and name[idx] == 'A':
            idx += 1

        min_move = min([min_move, 2 * i + len(name) - idx, i + 2 * (len(name) - idx)])

    answer += min_move
    return answer

solution("AAABBAB")