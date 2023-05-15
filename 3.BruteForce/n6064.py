import sys
input = sys.stdin.readline

T = int(input())


def Answer(M, N, x, y):
    while x <= M * N:
        if (x-y) % N == 0:
            return x
        else:
            x += M
    return -1


for i in range(T):
    M, N, x, y = map(int, input().split())
    print(Answer(M, N, x, y))