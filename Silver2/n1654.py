import sys

k, n = map(int, input().split())
li = [int(sys.stdin.readline()) for _ in range(k)]

start, end = 1, max(li)

while start <= end:
    mid = (start + end) // 2
    # print(f"mid = {mid}")
    cnt = 0
    for i in li:
        cnt += i // mid
    # print(f"cnt = {cnt}")

    if cnt >= n:  # 기준보다 개수가 많은 경우, 사이즈 늘리기
        start = mid + 1
    else:  # 기준보다 개수가 적은 경우, 사이즈 줄이기
        end = mid - 1

    # print(f"start = {start}, end = {end}")

print(end)