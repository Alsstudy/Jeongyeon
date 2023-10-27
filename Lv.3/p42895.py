def solution(N, number):
    arr = [[]]

    for i in range(1, 9):
        narr = set()
        narr.add(int(str(N) * i))
        for j in range(1, i // 2 + 1):
            a1 = arr[i - j]
            a2 = arr[j]
            for u in a1:
                for v in a2:
                    narr.add(u + v)
                    narr.add(u - v)
                    narr.add(v - u)
                    narr.add(u * v)
                    if v != 0:
                        narr.add(u // v)
                    if u != 0:
                        narr.add(v // u)

        if number in narr:
            return i

        arr.append(narr)

    return -1


print(solution(5, 12))
print(solution(2, 11))