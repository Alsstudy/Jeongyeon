import sys
input = sys.stdin.readline


def answer(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return answer(n-1) + answer(n-2) + answer(n-3)


T = int(input())

for i in range(T):
    n = int(input())
    print(answer(n))
