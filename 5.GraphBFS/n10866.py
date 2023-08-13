import sys
input = sys.stdin.readline

n = int(input())

d = []
for i in range(n):
    s = input().split()

    if s[0] == 'push_front':
        d.insert(0, s[1])
    elif s[0] == 'push_back':
        d.append(s[1])
    elif s[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop(0))
    elif s[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif s[0] == 'size':
        print(len(d))
    elif s[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif s[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    else:
        exit(0)