def solution(genres, plays):
    answer = []

    arr = []
    for i in range(len(genres)):
        arr.append([genres[i], plays[i], i])
    arr = sorted(arr, key=lambda x: (x[0], -x[1], x[2]))

    dic = {}
    for i in arr:
        if i[0] not in dic.keys():
            dic[i[0]] = i[1]
        else:
            dic[i[0]] += i[1]
    dic = sorted(dic.items(), key=lambda x: -x[1])

    for i in dic:
        cnt = 0
        for j in arr:
            if i[0] == j[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(j[2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))