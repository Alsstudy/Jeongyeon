import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if m:
    li = list(map(int, input().split()))

min_cnt = abs(100 - n)  # + 혹은 -만 사용하는 경우

for nums in range(1000001):
    nums = str(nums)
    for j in range(len(nums)):
        if int(nums[j]) in li:
            break
        elif j == len(nums) - 1:
            min_cnt = min(min_cnt, abs(int(nums)-n) + len(nums))

print(min_cnt)