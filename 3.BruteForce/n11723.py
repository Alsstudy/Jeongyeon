import sys
input = sys.stdin.readline


def calc(m):
    global s
    if m[0] == "add":
        if int(m[1]) not in s:
            s.append(int(m[1]))
    elif m[0] == "remove":
        if int(m[1]) in s:
            s.remove(int(m[1]))
    elif m[0] == "check":
        if int(m[1]) in s:
            print(1)
        else:
            print(0)
    elif m[0] == "toggle":
        if int(m[1]) in s:
            s.remove(int(m[1]))
        else:
            s.append(int(m[1]))
    elif m[0] == "all":
        s = []
        for i in range(1, 21):
            s.append(i)
    elif m[0] == "empty":
        s = []

    return


s = []
n = int(input())
for i in range(n):
    calc(list(input().split()))