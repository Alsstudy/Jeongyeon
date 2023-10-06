def dfs(numbers, target, idx, val):
    global cnt
    if idx == len(numbers):
        if val == target:
            cnt += 1
        return

    dfs(numbers, target, idx + 1, val + numbers[idx])
    dfs(numbers, target, idx + 1, val - numbers[idx])


def solution(numbers, target):
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0)
    return cnt


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))