import sys
input = sys.stdin.readline


def move(line):
    for i in range(1, n):
        if abs(line[i] - line[i-1]) > 1:
            return False

        if line[i] < line[i-1]:
            for j in range(l):
                if i+j >= n or line[i] != line[i+j] or temp[i+j]:
                    return False
                elif line[i] == line[i+j]:
                    temp[i+j] = True

        if line[i] > line[i-1]:
            for j in range(l):
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or temp[i-j-1]:
                    return False
                elif line[i-1] == line[i-j-1]:
                    temp[i-j-1] = True

    return True


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

count = 0

for i in range(n):
    temp = [False] * n
    if move(arr[i]):
        count += 1

for j in range(n):
    temp = [False] * n
    if move([arr[i][j] for i in range(n)]):
        count += 1

print(count)