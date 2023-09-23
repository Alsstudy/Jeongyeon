def solution(clothes):
    answer = 1
    d = {}
    for n, t in clothes:
        if t not in d.keys():
            d[t] = 0
        d[t] += 1

    for i in d.values():
        answer *= (i+1)
    answer -= 1

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))