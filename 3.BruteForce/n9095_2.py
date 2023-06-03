import sys
input = sys.stdin.readline


def getAnswer(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    elif i == 3:
        return 4
    else:
        return getAnswer(i-1) + getAnswer(i-2) + getAnswer(i-3)


T = int(input())

for i in range(T):
    n = int(input())
    print(getAnswer(n))