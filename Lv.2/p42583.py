def solution(bridge_length, weight, truck_weights):
    answer = bridge_length
    tmp = [0] * bridge_length
    s = 0

    while len(truck_weights) != 0:
        answer += 1
        s -= tmp.pop()
        tmp.insert(0, 0)
        if s + truck_weights[0] <= weight:
            tmp[0] = truck_weights.pop(0)
            s += tmp[0]

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
