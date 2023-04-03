import bisect

n = int(input())
li = list(map(int, input().split()))

result = [li[0]]

for i in range(1, n):
    idx = bisect.bisect_left(result, li[i])  # LIS에 삽입할 index return

    # 삽입
    if idx == len(result):
        result.append(li[i])
    else:
        result[idx] = li[i]

print(len(li) - len(result))  # 전체 길이 - LIS 길이
