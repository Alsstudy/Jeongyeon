def solution(sizes):
    amin = []
    amax = []

    for i in sizes:
        amin.append(min(i))
        amax.append(max(i))

    return max(amin) * max(amax)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))