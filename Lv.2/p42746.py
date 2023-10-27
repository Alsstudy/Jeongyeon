def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    for i in numbers:
        answer += i

    return str(int(answer))


print(solution([653, 662]))
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))