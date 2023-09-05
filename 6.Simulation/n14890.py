import sys
input = sys.stdin.readline


def check_line(line):
    for i in range(1, n):
        if abs(line[i] - line[i-1]) > 1:
            return False

        if line[i] < line[i-1]:
            for j in range(l):
                if i+j >= n or line[i] != line[i+j] or slope[i+j]:
                    return False
                if line[i] == line[i+j]:
                    slope[i+j] = True

        if line[i] > line[i-1]:
            for j in range(l):
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or slope[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    slope[i-j-1] = True

    return True


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    slope = [False] * n
    if check_line(arr[i]):
        ans += 1

for j in range(n):
    slope = [False] * n
    if check_line([arr[i][j] for i in range(n)]):
        ans += 1

print(ans)