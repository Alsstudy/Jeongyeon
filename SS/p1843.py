def solution(arr):
    M, m = {}, {}
    nums = [int(x) for x in arr[::2]]  # 숫자만 저장
    ops = [x for x in arr[1::2]]  # 연산만 저장

    for i in range(len(nums)):
        M[(i, i)] = nums[i]
        m[(i, i)] = nums[i]

    for d in range(1, len(nums)):
        for i in range(len(nums)):
            j = i + d

            if j >= len(nums):
                continue

            maxli, minli = [], []
            for k in range(i+1, j+1):
                if ops[k-1] == '-':
                    maxv = M[(i, k-1)] - m[(k, j)]
                    minv = m[(i, k-1)] - M[(k, j)]
                    maxli.append(maxv)
                    minli.append(minv)
                else:
                    maxv = M[(i, k-1)] + M[(k, j)]
                    minv = m[(i, k-1)] + m[(k, j)]
                    maxli.append(maxv)
                    minli.append(minv)

            M[(i, j)] = max(maxli)
            m[(i, j)] = min(minli)

    return M[(0, len(nums) - 1)]


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))