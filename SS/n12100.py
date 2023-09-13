def option(carr, t):
    narr = [[0] * n for _ in range(n)]

    if t == 0:  # 왼쪽
        for i in range(n):
            a = [carr[i][j] for j in range(n) if carr[i][j] != 0]
            move(-1, a)
            for j in range(n):
                narr[i][j] = a[j]
        return narr

    elif t == 1:  # 오른쪽
        for i in range(n):
            a = [carr[i][j] for j in range(n) if carr[i][j] != 0]
            move(1, a)
            for j in range(n):
                narr[i][j] = a[j]
        return narr

    elif t == 2:  # 위
        for j in range(n):
            a = [carr[i][j] for i in range(n) if carr[i][j] != 0]
            move(-1, a)
            for i in range(n):
                narr[i][j] = a[i]
        return narr

    elif t == 3:  # 아래
        for j in range(n):
            a = [carr[i][j] for i in range(n) if carr[i][j] != 0]
            move(1, a)
            for i in range(n):
                narr[i][j] = a[i]
        return narr


def move(dir, li):
    if dir == -1:
        for i in range(len(li) - 1):
            if li[i] == li[i+1]:
                li[i] += li[i + 1]
                li[i + 1] = 0
        while 0 in li:
            li.remove(0)
        for i in range(n - len(li)):
            li.append(0)

    if dir == 1:
        for i in range(len(li)-1, 0, -1):
            if li[i] == li[i - 1]:
                li[i] += li[i - 1]
                li[i - 1] = 0
        while 0 in li:
            li.remove(0)
        for i in range(n - len(li)):
            li.insert(0, 0)

    return li


def store(a):
    mval = 0
    for i in a:
        mval = max(max(i), mval)
    val.append(mval)


def bfs():
    while q:
        carr, cnt = q.pop(0)
        if cnt > 5:
            return
        for i in range(4):
            narr = option(carr, i)
            store(narr)
            q.append((narr, cnt+1))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

q = []
q.append((arr, 1))
val = []
bfs()

print(max(val))