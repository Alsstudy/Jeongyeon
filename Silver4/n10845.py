import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    order = list(map(str, sys.stdin.readline().split()))

    msg = order[0]
    if msg == 'push':
        arr.append(order[1])
    elif msg == 'pop':
        print(arr.pop(0) if arr else -1)
    elif msg == 'size':
        print(len(arr))
    elif msg == 'empty':
        print(0 if arr else 1)
    elif msg == 'front':
        print(arr[0] if arr else -1)
    elif msg == 'back':
        print(arr[-1] if arr else -1)
    else:
        print("ERROR")
        exit(0)