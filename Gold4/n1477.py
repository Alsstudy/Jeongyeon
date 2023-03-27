import sys

n, m, l = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.append(0)
li.append(l)
li = sorted(li)

left = 1
right = l-1

while left <= right:
    mid = (left + right) // 2
    cnt = 0  # 설치한 휴게소 수 count
    for i in range(1, len(li)):
        if li[i] - li[i-1] > mid:
            cnt += (li[i] - li[i-1] - 1) // mid

    if cnt > m:
        left = mid + 1

    else:
        val = mid
        right = mid - 1

print(val)